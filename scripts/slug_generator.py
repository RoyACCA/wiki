#!/usr/bin/env python3
"""
Context-Aware Slug Generator for LLM Wiki
Generates English-only filenames from Chinese/raw input files.

Steps:
1. Read file header → extract business entities (person/company/terminology)
2. Map to domain tags from SCHEMA.md
3. Combine entities + domain → generate semantic English slug
4. Prepend SHA256 first 8 chars as uniqueness prefix

Usage:
    python slug_generator.py --file <path> --domain <tag1,tag2>
"""

import argparse
import hashlib
import re
import sys
import os

# Domain keyword mapping for entity extraction
DOMAIN_KEYWORDS = {
    "aviation": ["航空", "民航", "机场", "航司", "航空公司", "航班", "航线", "Travelsky", "中国航信", "中航信"],
    "policy": ["政策", "规定", "办法", "指南", "通知", "意见", "规划", "国资委", "民航局", "工信部", "发改委"],
    "ai": ["人工智能", "AI", "大模型", "LLM", "模型", "机器学习", "深度学习", "ChatGPT", "GPT", "文心", "通义"],
    "low-altitude": ["低空", "无人机", "eVTOL", "UAM", "通用航空", "低空经济"],
    "future-industry": ["未来产业", "战新", "战略性新兴产业", "新质生产力"],
    "digital": ["数字化", "数字化转型", "数字经济", "数据要素"],
    "central-enterprise": ["央企", "国有企业", "国企", "中央企业"],
    "tech-innovation": ["科技创新", "技术创新", "研发", "创新联合体"],
}

# Known entity mappings (extend as needed)
KNOWN_ENTITIES = {
    "中国航信": "travelsky",
    "Travelsky": "travelsky",
    "中国民航信息": "travelsky",
    "国资委": "sasac",
    "国务院国资委": "sasac",
    "民航局": "caac",
    "中国民航局": "caac",
    "中国民用航空局": "caac",
    "工信部": "miit",
    "工业和信息化部": "miit",
    "发改委": "ndrc",
    "国家发展和改革委员会": "ndrc",
    "焦雷": "jiaolei",
    "低空经济": "low-altitude-economy",
    "战略性新兴产业": "strategic-emerging-industry",
    "新质生产力": "new-quality-productivity",
    "人工智能": "ai",
    "大模型": "llm",
    "行业大模型": "industry-llm",
}

def compute_sha256_prefix(file_path: str) -> str:
    """Compute SHA256 hash, return first 8 hex chars."""
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()[:8]

def extract_entities_from_content(content: str) -> list[str]:
    """Extract known entities from content using keyword matching."""
    found = []
    for cn, en in KNOWN_ENTITIES.items():
        if cn in content:
            found.append(en)
    return found

def detect_domains(content: str) -> list[str]:
    """Detect applicable domain tags from content."""
    detected = []
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for kw in keywords:
            if kw in content:
                if domain not in detected:
                    detected.append(domain)
                break
    return detected

def extract_version_info(filename: str) -> str:
    """Extract version info from filename."""
    patterns = [
        r'v(\d+)',
        r'edition',
        r'version',
        r'第[一二三四五六七八九十\d]+版',
        r'（?(修正版|修订版)?）?',
    ]
    parts = []
    for p in patterns:
        m = re.search(p, filename.lower())
        if m:
            parts.append(m.group(0))
    return '_'.join(parts) if parts else ''

def generate_slug(file_path: str, content_preview: str, domains: list[str] = None) -> str:
    """Generate a semantic English slug from file content and domains."""
    # Extract entities from content
    entities = extract_entities_from_content(content_preview[:500])

    # Detect domains
    detected_domains = detect_domains(content_preview[:1000]) if not domains else domains

    # Deduplicate while preserving order
    entities = list(dict.fromkeys(entities))
    detected_domains = list(dict.fromkeys(detected_domains))

    # Build slug parts
    slug_parts = []

    # Add detected/specified entities
    if entities:
        slug_parts.extend(entities[:3])  # max 3 entities

    # Add domain tags
    slug_parts.extend(detected_domains[:3])  # max 3 domains

    # Add version info if present
    version = extract_version_info(os.path.basename(file_path))
    if version:
        slug_parts.append(version)

    # Deduplicate final slug parts
    slug_parts = list(dict.fromkeys(slug_parts))

    # Clean and join
    if not slug_parts:
        return "unknown"

    # Generate year from content or use placeholder
    year_match = re.search(r'20\d{2}', content_preview[:200])
    year = year_match.group(0) if year_match else "undated"

    slug = f"{year}_{'-'.join(slug_parts)}"
    # Clean: only alphanum and hyphens
    slug = re.sub(r'[^a-z0-9\-]', '', slug.lower())
    slug = re.sub(r'-+', '-', slug)
    return slug

def main():
    parser = argparse.ArgumentParser(description='Context-aware slug generator for LLM Wiki')
    parser.add_argument('--file', required=True, help='Path to the file')
    parser.add_argument('--domain', default='', help='Comma-separated domain tags (optional)')
    args = parser.parse_args()

    file_path = args.file

    # Read file header
    content_preview = ""
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext in ['.txt', '.md']:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content_preview = f.read(2000)
        elif ext == '.pdf':
            import fitz
            doc = fitz.open(file_path)
            for page in doc[:3]:
                content_preview += page.get_text()
            doc.close()
        elif ext == '.docx':
            from docx import Document
            doc = Document(file_path)
            for para in doc.paragraphs[:20]:
                content_preview += para.text + '\n'
        else:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content_preview = f.read(500)
    except Exception as e:
        print(f"Warning: failed to read content preview: {e}", file=sys.stderr)
        content_preview = ""

    domains = args.domain.split(',') if args.domain else None
    slug = generate_slug(file_path, content_preview, domains)
    sha_prefix = compute_sha256_prefix(file_path)
    ext = os.path.splitext(file_path)[1].lower()

    # Output: SHA_prefix_slug.ext
    output_filename = f"{sha_prefix}_{slug}{ext}"

    import json
    result = {
        "sha_prefix": sha_prefix,
        "slug": slug,
        "filename": output_filename,
        "detected_entities": extract_entities_from_content(content_preview[:500]),
        "detected_domains": detect_domains(content_preview[:1000]) if not domains else domains,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
