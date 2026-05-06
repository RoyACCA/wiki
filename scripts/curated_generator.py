#!/usr/bin/env python3
"""
LLM Wiki Curated Generator — Monthly/Quarterly Digest.

Scans queries/ directory, selects best answers, generates a curated digest.
Run monthly via cron or manually.

Usage:
    python curated_generator.py --year 2026 --quarter Q1
    python curated_generator.py --month 2026-04
"""

import argparse
import json
import os
import re
from collections import defaultdict
from datetime import datetime

WIKI_PATH = os.environ.get('WIKI_PATH', '/home/agentuser/wiki')

def extract_query_metadata(fpath: str) -> dict:
    """Extract metadata from a query page."""
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return {}

    meta = {
        "path": fpath,
        "filename": os.path.basename(fpath),
        "size": len(content)
    }

    # Extract frontmatter
    in_fm = False
    for line in content.split('\n'):
        if line.strip() == '---':
            if not in_fm:
                in_fm = True
                continue
            else:
                break
        if in_fm and ':' in line:
            key, val = line.split(':', 1)
            meta[key.strip()] = val.strip()

    # Extract date from filename: query_YYYYMMDD_topic.md
    date_match = re.search(r'query_(\d{8})_', os.path.basename(fpath))
    if date_match:
        date_str = date_match.group(1)
        meta['date'] = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"

    # Extract H1 title
    h1 = re.search(r'^# (.+)$', content, re.MULTILINE)
    if h1:
        meta['title'] = h1.group(1)

    return meta

def select_best_queries(queries_dir: str, limit: int = 20) -> list[dict]:
    """Select best queries based on content quality indicators."""
    if not os.path.exists(queries_dir):
        return []

    query_files = []
    for f in os.listdir(queries_dir):
        if f.startswith('query_') and f.endswith('.md'):
            fpath = os.path.join(queries_dir, f)
            meta = extract_query_metadata(fpath)
            if meta:
                query_files.append(meta)

    # Sort by: has summary section > has tags > file size (proxy for depth)
    def quality_score(q: dict) -> tuple:
        with open(q['path'], 'r', encoding='utf-8') as f:
            content = f.read()
        has_summary = 1 if '## Summary' in content else 0
        has_tags = 1 if q.get('tags', '') else 0
        size_score = min(q['size'] / 5000, 3)  # cap at 3
        return (has_summary + has_tags, size_score, q['size'])

    query_files.sort(key=quality_score, reverse=True)
    return query_files[:limit]

def generate_digest(year: int, quarter: str, queries: list[dict], output_path: str):
    """Generate the curated quarterly digest markdown."""

    quarter_map = {'Q1': '01-03', 'Q2': '04-06', 'Q3': '07-09', 'Q4': '10-12'}
    q_months = quarter_map.get(quarter, '01-03')
    period = f"{year}"

    lines = [
        "---",
        f"title: Curated Digest {year} {quarter}",
        f"created: {datetime.now().strftime('%Y-%m-%d')}",
        f"period: {year} {quarter}",
        f"type: curated-digest",
        f"tags: [curated, digest, {year}]",
        "---",
        "",
        f"# Curated Digest — {year} {quarter}",
        "",
        f"> Generated: {datetime.now().strftime('%Y-%m-%d')} | Source queries: {len(queries)}",
        "",
        "## Overview",
        "",
        f"This curated digest compiles the {len(queries)} highest-quality query responses ",
        f"from the LLM Wiki for {year} {quarter}.",
        "",
        "## Featured Insights",
        "",
    ]

    for i, q in enumerate(queries, 1):
        title = q.get('title', q['filename'])
        date = q.get('date', 'undated')
        source_link = f"[[{q['filename']}]]"

        lines.append(f"### {i}. {title}")
        lines.append(f"")
        lines.append(f"**Date:** {date} | **Source:** {source_link}")
        lines.append("")

        # Extract first 300 chars of content as preview
        try:
            with open(q['path'], 'r', encoding='utf-8') as f:
                content = f.read()
            # Skip frontmatter
            content = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL)
            # Remove H1
            content = re.sub(r'^# .+$', '', content, flags=re.MULTILINE)
            preview = content.strip()[:300]
            if len(content) > 300:
                preview += "..."
            lines.append(preview)
        except:
            pass

        lines.append("")
        lines.append("---")
        lines.append("")

    lines.extend([
        "## Domain Distribution",
        ""
    ])

    # Count tags
    tag_counts = defaultdict(int)
    for q in queries:
        tags_str = q.get('tags', '')
        if tags_str:
            for tag in re.findall(r'[\w\-]+', tags_str):
                if tag not in ['curated', 'digest', str(year)]:
                    tag_counts[tag] += 1

    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1])[:10]:
        lines.append(f"- **{tag}**: {count} queries")

    lines.extend([
        "",
        "## Summary",
        "",
        f"This digest covers {len(queries)} curated query responses ",
        f"spanning {len(tag_counts)} topic areas. ",
        "For full content, refer to individual query pages.",
    ])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return output_path

def main():
    parser = argparse.ArgumentParser(description='LLM Wiki Curated Digest Generator')
    parser.add_argument('--year', type=int, required=True, help='Year (e.g., 2026)')
    parser.add_argument('--quarter', required=True, help='Quarter (Q1, Q2, Q3, Q4)')
    parser.add_argument('--wiki-path', default=WIKI_PATH, help='Wiki root path')
    parser.add_argument('--limit', type=int, default=20, help='Max queries to include')
    args = parser.parse_args()

    queries_dir = os.path.join(args.wiki_path, 'wiki/queries')
    output_dir = os.path.join(args.wiki_path, 'wiki/queries/curated')
    os.makedirs(output_dir, exist_ok=True)

    # Select best queries
    queries = select_best_queries(queries_dir, limit=args.limit)

    if not queries:
        print(json.dumps({"status": "no_queries", "message": "No queries found to curate"}))
        return

    # Generate digest
    output_filename = f"quarterly-review-{args.year}-{args.quarter}.md"
    output_path = os.path.join(output_dir, output_filename)

    generate_digest(args.year, args.quarter, queries, output_path)

    print(json.dumps({
        "status": "success",
        "year": args.year,
        "quarter": args.quarter,
        "queries_processed": len(queries),
        "output": output_path
    }))

if __name__ == '__main__':
    main()
