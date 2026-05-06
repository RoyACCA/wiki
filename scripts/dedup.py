#!/usr/bin/env python3
"""
Deduplication module for LLM Wiki.
Two-level dedup: SHA256 exact match + MinHash content similarity.

Usage:
    python dedup.py --check <file_path> [--db-path <path>]
    python dedup.py --init [--db-path <path>]

Output JSON:
    {
        "status": "exact_duplicate" | "similar" | "new",
        "sha256": "...",
        "similarity": 0.0-1.0,
        "similar_to": "<path if similar>",
        "action": "skip" | "force_ingest" | "ingest"
    }
"""

import argparse
import hashlib
import json
import os
import re
import sys
import sqlite3

# MinHash
from datasketch import MinHash

DB_PATH = os.path.expanduser("~/.hermes/wiki/dedup.db")
SIMILARITY_THRESHOLD = 0.85
VERSION_PATTERNS = [r'v\d+', r'edition', r'version', r'第[一二三四五六七八九十\d]+版']

def is_versioned_document(filename: str) -> bool:
    return any(re.search(p, filename.lower()) for p in VERSION_PATTERNS)

def compute_sha256(file_path: str) -> str:
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def extract_text_content(file_path: str) -> str:
    """Extract text from file for MinHash."""
    ext = os.path.splitext(file_path)[1].lower()
    content = ""

    try:
        if ext == '.txt':
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        elif ext == '.md':
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        elif ext == '.pdf':
            import fitz
            doc = fitz.open(file_path)
            for page in doc:
                content += page.get_text()
            doc.close()
        elif ext == '.docx':
            from docx import Document
            doc = Document(file_path)
            for para in doc.paragraphs:
                content += para.text + '\n'
    except Exception:
        pass

    # Normalize: lowercase, strip, remove extra whitespace
    content = re.sub(r'\s+', ' ', content.lower().strip())
    return content

def compute_minhash(text: str, num_perm: int = 128) -> MinHash:
    m = MinHash(num_perm=num_perm)
    # Split by sentences/words for better similarity
    tokens = text.split(' ')
    for token in tokens:
        if len(token) > 2:
            m.update(token.encode('utf8'))
    return m

def init_db(db_path: str):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS files (
            sha256 TEXT PRIMARY KEY,
            filepath TEXT NOT NULL,
            filename TEXT NOT NULL,
            minhash BLOB,
            is_versioned INTEGER DEFAULT 0,
            added_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(json.dumps({"status": "initialized", "db_path": db_path}))

def check_dedup(file_path: str, db_path: str = DB_PATH) -> dict:
    """
    Check if file is duplicate.
    Returns JSON with status, similarity, and recommended action.
    """
    if not os.path.exists(db_path):
        # No db yet, treat as new
        return {
            "status": "new",
            "sha256": compute_sha256(file_path),
            "similarity": 0.0,
            "similar_to": None,
            "action": "ingest"
        }

    sha = compute_sha256(file_path)
    filename = os.path.basename(file_path)
    versioned = 1 if is_versioned_document(filename) else 0

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Step 1: SHA256 exact match
    c.execute('SELECT * FROM files WHERE sha256 = ?', (sha,))
    row = c.fetchone()
    if row:
        conn.close()
        return {
            "status": "exact_duplicate",
            "sha256": sha,
            "similarity": 1.0,
            "similar_to": row['filepath'],
            "action": "skip"
        }

    # Step 2: MinHash content similarity
    content = extract_text_content(file_path)
    if not content or len(content) < 50:
        # Can't compute similarity, treat as new
        conn.close()
        return {
            "status": "new",
            "sha256": sha,
            "similarity": 0.0,
            "similar_to": None,
            "action": "ingest"
        }

    new_minhash = compute_minhash(content)

    # Load all stored minhashes and compare
    c.execute('SELECT filepath, filename, minhash, is_versioned FROM files')
    best_similarity = 0.0
    best_match = None

    for row in c.fetchall():
        if row['minhash']:
            import pickle
            stored_minhash = pickle.loads(row['minhash'])
            sim = new_minhash.jaccard(stored_minhash)
            if sim > best_similarity:
                best_similarity = sim
                best_match = row['filepath']

    conn.close()

    if best_similarity >= SIMILARITY_THRESHOLD:
        if versioned:
            return {
                "status": "similar_versioned",
                "sha256": sha,
                "similarity": round(best_similarity, 4),
                "similar_to": best_match,
                "action": "force_ingest"
            }
        else:
            return {
                "status": "similar",
                "sha256": sha,
                "similarity": round(best_similarity, 4),
                "similar_to": best_match,
                "action": "skip"
            }

    return {
        "status": "new",
        "sha256": sha,
        "similarity": round(best_similarity, 4),
        "similar_to": None,
        "action": "ingest"
    }

def add_to_db(file_path: str, db_path: str = DB_PATH, wiki_filepath: str = None):
    """Add a file record to the dedup database."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    sha = compute_sha256(file_path)
    filename = os.path.basename(file_path)
    versioned = 1 if is_versioned_document(filename) else 0

    content = extract_text_content(file_path)
    minhash_bytes = None
    if content:
        m = compute_minhash(content)
        import pickle
        minhash_bytes = pickle.dumps(m)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO files (sha256, filepath, filename, minhash, is_versioned)
        VALUES (?, ?, ?, ?, ?)
    ''', (sha, wiki_filepath or file_path, filename, minhash_bytes, versioned))
    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='LLM Wiki deduplication')
    parser.add_argument('--check', metavar='PATH', help='Check file for duplication')
    parser.add_argument('--add', metavar='PATH', help='Add file to dedup DB')
    parser.add_argument('--init', action='store_true', help='Initialize dedup DB')
    parser.add_argument('--db-path', default=DB_PATH, help='Path to dedup SQLite DB')
    parser.add_argument('--wiki-path', default='', help='Wiki filepath (for --add)')
    args = parser.parse_args()

    if args.init:
        init_db(args.db_path)
        return

    if args.check:
        result = check_dedup(args.check, args.db_path)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if args.add:
        add_to_db(args.add, args.db_path, args.wiki_path or None)
        print(json.dumps({"status": "added", "path": args.add}))
        return

    parser.print_help()

if __name__ == '__main__':
    main()
