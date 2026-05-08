#!/usr/bin/env python3
"""
LLM Wiki Lint — 10-Point Health Check + Auto-Fix Broken Links.

Usage:
    python lint.py [--wiki-path <path>] [--fix] [--dry-run]
"""

import argparse
import json
import os
import re
import sys
import yaml
from collections import defaultdict
from datetime import datetime, timedelta

WIKI_PATH = os.environ.get('WIKI_PATH', '/home/agentuser/wiki')

def load_redirects(wiki_path: str) -> dict:
    """Load _redirects.yaml as {old_slug: new_slug}."""
    redirect_path = os.path.join(wiki_path, 'wiki/_redirects.yaml')
    if not os.path.exists(redirect_path):
        return {}
    with open(redirect_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Parse simple YAML: old_slug: new_slug
    redirects = {}
    for line in content.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            old_slug, new_slug = line.split(':', 1)
            old_slug = old_slug.strip()
            new_slug = new_slug.strip()
            if old_slug and new_slug:
                redirects[old_slug] = new_slug
    return redirects

def save_redirects(wiki_path: str, redirects: dict):
    """Save redirects back to _redirects.yaml."""
    redirect_path = os.path.join(wiki_path, 'wiki/_redirects.yaml')
    lines = ["# Wiki Redirects", "", "# Format: old_slug: new_slug"]
    lines.append("# Auto-generated / maintained by lint --fix")
    lines.append("")
    for old, new in sorted(redirects.items()):
        lines.append(f"{old}: {new}")
    lines.append("")
    lines.append(f"# Last updated: {datetime.now().strftime('%Y-%m-%d')}")
    with open(redirect_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def find_wikilinks(content: str) -> list[tuple[str, str]]:
    """Extract [(full_match, target_slug), ...] from content."""
    # Match [[slug]] or [[slug|display]]
    # Exclude raw file references: [[../raw/...pdf]], [[raw/...]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    matches = re.findall(pattern, content)
    result = []
    for m in matches:
        target = m.split('|')[0].strip()
        # Skip raw file references (paths containing / or file extensions)
        if target.startswith('../') or target.startswith('raw/') or '.' in target:
            continue
        result.append((m, target))
    return result

def find_all_wikilinks_in_dir(wiki_path: str) -> dict:
    """Return {target_slug: [(filepath, matched_text), ...]}."""
    wiki_dir = os.path.join(wiki_path, 'wiki')
    link_map = defaultdict(list)

    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if not f.endswith('.md') or f == '_redirects.yaml':
                continue
            fpath = os.path.join(root, f)
            try:
                with open(fpath, 'r', encoding='utf-8') as fp:
                    content = fp.read()
            except:
                continue

            for full_match, target in find_wikilinks(content):
                rel = fpath.replace(wiki_path + '/', '')
                link_map[target].append((rel, full_match))

    return link_map

def find_existing_pages(wiki_path: str) -> set:
    """Return set of all valid page slugs (no extension, no path prefix)."""
    wiki_dir = os.path.join(wiki_path, 'wiki')
    pages = set()
    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if f.endswith('.md') and f not in ['index.md', 'log.md', '_redirects.yaml']:
                slug = os.path.join(root, f).replace(wiki_path + '/wiki/', '').replace('.md', '')
                pages.add(slug)
                # Also add basename-only for top-level lookups
                pages.add(os.path.basename(slug))
    return pages

def find_broken_wikilinks(wiki_path: str, redirects: dict) -> tuple[list, list]:
    """
    Find all broken wikilinks.
    Returns (broken_links, fixed_links) where fixed_links are ones auto-fixed via redirects.
    """
    existing_pages = find_existing_pages(wiki_path)
    all_links = find_all_wikilinks_in_dir(wiki_path)

    broken = []
    fixed = []

    for target_slug, occurrences in all_links.items():
        if target_slug in existing_pages:
            continue
        if target_slug in redirects:
            # Redirect exists — auto-fixable, add to fixed list only (NOT broken)
            new_slug = redirects[target_slug]
            for filepath, full_match in occurrences:
                fixed.append((filepath, full_match, new_slug))
        else:
            # No redirect — truly broken
            for filepath, full_match in occurrences:
                broken.append({
                    "file": filepath,
                    "broken_link": full_match,
                    "target": target_slug,
                    "can_fix": False,
                    "new_slug": None
                })

    return broken, fixed

def auto_fix_broken_links(wiki_path: str, fixed_links: list):
    """
    Apply redirects to all broken links.
    fixed_links: [(filepath, old_full_match, new_slug), ...]
    """
    if not fixed_links:
        return 0

    fixed_count = 0
    # Group by file to minimize file I/O
    by_file = defaultdict(list)
    for filepath, old_match, new_slug in fixed_links:
        by_file[filepath].append((old_match, new_slug))

    for filepath, replacements in by_file.items():
        full_path = os.path.join(wiki_path, filepath) if not filepath.startswith('/') else filepath
        if not os.path.exists(full_path):
            full_path = os.path.join(wiki_path, 'wiki', filepath)

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue

        original = content
        for old_match, new_slug in replacements:
            # full_match: if bare slug, wrap in [[ ]] for reliable replacement
            full_match = f"[[{old_match}]]" if not old_match.startswith('[[') else old_match
            old_slug = old_match  # already bare slug
            pattern = re.compile(re.escape(f"[[{old_slug}]]"))
            content = pattern.sub(f"[[{new_slug}]]", content)

        if content != original:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += len(replacements)

    return fixed_count


def auto_fix_index_completeness(wiki_path: str, index_issues: list[dict], dry_run: bool = False) -> int:
    """
    Auto-fix index completeness: add missing pages to index.md.
    Each issue: {"issue": "file not in index", "file": "wiki/entities/event/foo.md"}

    Strategy: read each missing page's frontmatter → determine section → append to index.md
    Returns number of pages added.
    """
    if not index_issues:
        return 0

    index_path = os.path.join(wiki_path, 'wiki/index.md')
    if not os.path.exists(index_path):
        print("  ! index.md not found, cannot auto-fix")
        return 0

    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()

    added_count = 0
    for issue in index_issues:
        if issue.get('issue') != 'file not in index':
            continue
        filepath = issue.get('file')
        if not filepath:
            continue

        full_path = os.path.join(wiki_path, filepath)
        if not os.path.exists(full_path):
            full_path = os.path.join(wiki_path, 'wiki', os.path.basename(filepath))

        if not os.path.exists(full_path):
            continue

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                page_content = f.read()
        except:
            continue

        # Extract frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---', page_content, re.DOTALL)
        if not fm_match:
            continue

        fm_text = fm_match.group(1)
        title_m = re.search(r'^title:\s*(.+?)\s*$', fm_text, re.MULTILINE)
        type_m = re.search(r'^type:\s*(.+?)\s*$', fm_text, re.MULTILINE)
        summary_m = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)

        title = title_m.group(1).strip('"\' ') if title_m else os.path.basename(filepath).replace('.md', '')
        page_type = type_m.group(1).strip() if type_m else 'unknown'
        summary = summary_m.group(1).strip('"\' ') if summary_m else '（无摘要）'

        # Determine target section from type
        if 'person' in page_type:
            section = '### person'
            prefix = '| [['
        elif 'company' in page_type:
            section = '### company'
            prefix = '| [['
        elif 'paper' in page_type:
            section = '### paper'
            prefix = '| [['
        elif 'event' in page_type:
            section = '### company'
            prefix = '| [['
        elif 'query' in page_type:
            section = '## Queries'
            prefix = '| [['
        elif 'comparison' in page_type:
            section = '## Comparisons'
            prefix = '| [['
        else:
            section = '## Concepts'
            prefix = '| [['

        slug = filepath.replace('.md', '').replace(wiki_path + '/wiki/', '')
        new_entry = f"{prefix}{slug}]] | {summary} |"

        # Find insertion point: last occurrence of section header or the last entry before next section
        section_pattern = re.compile(rf'^{re.escape(section)}', re.MULTILINE)
        match = section_pattern.search(index_content)

        if not match:
            # Section doesn't exist — find appropriate place to insert
            if section == '## Concepts':
                insert_pos = len(index_content)
                for marker in ['## Queries', '## Review', '## Curated']:
                    m = re.search(rf'^## {re.escape(marker[3:])}', index_content, re.MULTILINE)
                    if m:
                        insert_pos = min(insert_pos, m.start())
            elif section == '## Queries':
                insert_pos = len(index_content)
                for marker in ['## Review', '## Curated']:
                    m = re.search(rf'^## {re.escape(marker[3:])}', index_content, re.MULTILINE)
                    if m:
                        insert_pos = min(insert_pos, m.start())
            else:
                insert_pos = len(index_content)
        else:
            # Find the end of this section (next ## or end of file)
            section_start = match.start()
            rest = index_content[section_start:]
            next_section = re.search(r'^## ', rest[5:], re.MULTILINE)
            if next_section:
                insert_pos = section_start + 5 + next_section.start()
            else:
                insert_pos = len(index_content)

        if dry_run:
            print(f"  [DRY-RUN] Would add to {section}: {slug}")
        else:
            index_content = index_content[:insert_pos] + new_entry + '\n' + index_content[insert_pos:]
            added_count += 1
            print(f"  [FIX] Added to {section}: {slug}")

    if not dry_run and added_count > 0:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

        # Update total count in header
        with open(index_path, 'r', encoding='utf-8') as f:
            header = f.read()
        total_m = re.search(r'Total pages:\s*(\d+)', header)
        if total_m:
            old_total = int(total_m.group(1))
            # Count actual pages in index
            actual = header.count('| [[')
            new_total = old_total + added_count
            header = re.sub(r'Total pages:\s*\d+', f'Total pages: {actual}', header)
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(header)
            print(f"  [FIX] Updated total pages {old_total} -> {actual}")

    return added_count


def find_orphan_pages(wiki_path: str) -> list[str]:
    """Find pages with no inbound wikilinks (skipping query/event/paper types which are self-contained)."""
    wiki_dir = os.path.join(wiki_path, 'wiki')
    if not os.path.exists(wiki_dir):
        return []

    # Types that are self-contained and don't need inbound links
    skip_types = {'query', 'event', 'paper', 'company'}

    # Build inbound link map
    inbound = defaultdict(list)
    all_pages = []

    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if not f.endswith('.md') or f in ['_redirects.yaml'] or f.startswith('log'):
                continue
            fpath = os.path.join(root, f)
            rel = fpath.replace(wiki_path + '/', '')
            # index.md is excluded from all_pages (doesn't need self-check) but its links count as inbound
            if f != 'index.md':
                all_pages.append(rel)

            try:
                with open(fpath, 'r', encoding='utf-8') as fp:
                    content = fp.read()
            except:
                continue

            for _, target in find_wikilinks(content):
                if not target.startswith('../'):
                    inbound[target].append(rel)

    orphans = []
    for page in all_pages:
        # Skip self-contained page types
        fpath = os.path.join(wiki_path, page)
        try:
            with open(fpath, 'r', encoding='utf-8') as fp:
                raw = fp.read()
            # Quick frontmatter type check
            fm_match = re.match(r'^---\n(.*?)\n---', raw, re.DOTALL)
            if fm_match:
                fm_text = fm_match.group(1)
                type_match = re.search(r'^type:\s*(.+?)\s*$', fm_text, re.MULTILINE)
                if type_match:
                    type_val = type_match.group(1).strip()
                    # Skip if type contains any of the skip_types (handles entity-event, entity-paper, query, event, paper)
                    if any(s in type_val for s in skip_types):
                        continue
        except:
            pass

        # Get all possible slug forms
        basename = os.path.basename(page).replace('.md', '')
        variants = {page, basename, os.path.join(os.path.dirname(page), basename)}

        has_inbound = False
        for variant in variants:
            if variant in inbound or basename in inbound:
                has_inbound = True
                break

        if not has_inbound:
            orphans.append(page)

    return orphans

def check_frontmatter_completeness(wiki_path: str) -> list[dict]:
    """Check all wiki pages have required frontmatter fields."""
    required_fields = ['title', 'created', 'updated', 'type', 'tags']
    issues = []

    wiki_dir = os.path.join(wiki_path, 'wiki')
    if not os.path.exists(wiki_dir):
        return issues

    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if not f.endswith('.md') or f in ['index.md', '_redirects.yaml'] or f.startswith('log'):
                continue
            fpath = os.path.join(root, f)
            rel = fpath.replace(wiki_path + '/', '')
            try:
                with open(fpath, 'r', encoding='utf-8') as fp:
                    content = fp.read()
            except:
                continue

            in_fm = False
            fm_fields = {}
            for line in content.split('\n'):
                if line.strip() == '---':
                    if not in_fm:
                        in_fm = True
                        continue
                    else:
                        break
                if in_fm and ':' in line:
                    key = line.split(':', 1)[0].strip()
                    fm_fields[key] = True

            if not in_fm:
                issues.append({"file": rel, "issue": "no frontmatter"})
                continue

            for field in required_fields:
                if field not in fm_fields:
                    issues.append({"file": rel, "issue": f"missing field: {field}"})

    return issues

def check_stale_content(wiki_path: str, threshold_days: int = 90) -> list[dict]:
    """Find pages not updated in >90 days."""
    stale = []
    wiki_dir = os.path.join(wiki_path, 'wiki')
    if not os.path.exists(wiki_dir):
        return stale

    cutoff = (datetime.now() - timedelta(days=threshold_days)).strftime('%Y-%m-%d')

    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if not f.endswith('.md') or f in ['index.md', 'log.md', '_redirects.yaml']:
                continue
            fpath = os.path.join(root, f)
            rel = fpath.replace(wiki_path + '/', '')
            try:
                with open(fpath, 'r', encoding='utf-8') as fp:
                    content = fp.read()
            except:
                continue

            in_fm = False
            updated = None
            for line in content.split('\n'):
                if line.strip() == '---':
                    if not in_fm:
                        in_fm = True
                        continue
                    else:
                        break
                if in_fm and line.startswith('updated:'):
                    updated = line.split(':', 1)[1].strip()

            if updated and updated < cutoff:
                stale.append({"file": rel, "updated": updated, "stale_days": (datetime.now() - datetime.strptime(updated, '%Y-%m-%d')).days})

    return stale

def check_tag_taxonomy(wiki_path: str) -> list[dict]:
    """Check all tags are in SCHEMA.md taxonomy."""
    schema_path = os.path.join(wiki_path, 'schema/SCHEMA.md')
    valid_tags = set(['person', 'company', 'lab', 'paper', 'event', 'concept', 'comparison', 'query'])

    if os.path.exists(schema_path):
        with open(schema_path, 'r', encoding='utf-8') as f:
            content = f.read()
        in_taxonomy = False
        in_code_block = False
        for line in content.split('\n'):
            # Track code block boundaries
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            # Only parse outside code blocks
            if in_code_block:
                continue
            if 'Tag Taxonomy' in line or 'tag taxonomy' in line.lower():
                in_taxonomy = True
                continue
            if in_taxonomy and line.startswith('## '):
                break
            if in_taxonomy and line.strip().startswith('- '):
                tag = line.strip()[2:].split('→')[0].split('—')[0].split(',')[0].strip()
                valid_tags.add(tag)

    issues = []
    wiki_dir = os.path.join(wiki_path, 'wiki')
    if not os.path.exists(wiki_dir):
        return issues

    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if not f.endswith('.md') or f in ['index.md', 'log.md', '_redirects.yaml']:
                continue
            fpath = os.path.join(root, f)
            rel = fpath.replace(wiki_path + '/', '')
            try:
                with open(fpath, 'r', encoding='utf-8') as fp:
                    content = fp.read()
            except:
                continue

            in_fm = False
            found_tags = []
            for line in content.split('\n'):
                if line.strip() == '---':
                    if not in_fm:
                        in_fm = True
                        continue
                    else:
                        break
                if in_fm and line.startswith('tags:'):
                    tags_str = line.split(':', 1)[1].strip().strip('[]')
                    found_tags = [t.strip().strip('"\'') for t in tags_str.split(',')]

            for tag in found_tags:
                if tag and tag not in valid_tags:
                    issues.append({"file": rel, "invalid_tag": tag})

    return issues

def check_page_size(wiki_path: str, threshold: int = 500) -> list[dict]:
    """Find pages >500 lines."""
    oversized = []
    wiki_dir = os.path.join(wiki_path, 'wiki')
    if not os.path.exists(wiki_dir):
        return oversized

    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if not f.endswith('.md') or f in ['index.md', '_redirects.yaml'] or f.startswith('log'):
                continue
            fpath = os.path.join(root, f)
            rel = fpath.replace(wiki_path + '/', '')
            try:
                with open(fpath, 'r', encoding='utf-8') as fp:
                    lines = fp.readlines()
            except:
                continue

            if len(lines) > threshold:
                oversized.append({"file": rel, "line_count": len(lines)})

    return oversized

def check_log_rotation(wiki_path: str, threshold: int = 500) -> dict:
    """Check if log.md needs rotation."""
    log_path = os.path.join(wiki_path, 'wiki/log.md')
    if not os.path.exists(log_path):
        return {"needs_rotation": False, "reason": "log.md not found"}

    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            entries = [l for l in f.readlines() if l.strip().startswith('## ')]
        if len(entries) > threshold:
            return {"needs_rotation": True, "entry_count": len(entries), "threshold": threshold}
    except:
        pass

    return {"needs_rotation": False, "entry_count": 0}


def auto_fix_log_rotation(wiki_path: str, dry_run: bool = False) -> dict:
    """Rotate log.md: rename to log-YYYY-MM-DD.md + create new log.md with header."""
    log_path = os.path.join(wiki_path, 'wiki/log.md')
    if not os.path.exists(log_path):
        return {"rotated": False, "reason": "log.md not found"}

    today = datetime.now().strftime('%Y-%m-%d')
    rotated_path = os.path.join(wiki_path, f'wiki/log-{today}.md')

    # Check if this exact date already exists
    if os.path.exists(rotated_path):
        return {"rotated": False, "reason": f"log-{today}.md already exists"}

    if dry_run:
        print(f"  [DRY-RUN] Would rotate log.md -> log-{today}.md")
        return {"rotated": True, "rotated_path": f"log-{today}.md"}

    # Read old log for the rotation entry
    with open(log_path, 'r', encoding='utf-8') as f:
        old_log_content = f.read()

    # Count entries
    entries = [l for l in old_log_content.split('\n') if l.strip().startswith('## ')]
    entry_count = len(entries)

    # Save rotated version
    with open(rotated_path, 'w', encoding='utf-8') as f:
        f.write(old_log_content)
    print(f"  [FIX] Rotated log.md -> log-{today}.md ({entry_count} entries)")

    # Create new log.md
    new_log = f"""# Wiki Changelog

> Chronological action log. Every ingest, update, and structural change recorded.
> Format: `## [YYYY-MM-DD] Action | Details`

## [{today}] rotation | Rotated {entry_count} entries → log-{today}.md

"""
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(new_log)
    print(f"  [FIX] Created new log.md")

    return {"rotated": True, "rotated_path": f"log-{today}.md", "entry_count": entry_count}


def check_review_overdue(wiki_path: str, threshold_days: int = 30) -> list[dict]:
    """Find items in review/ not processed in >30 days."""
    overdue = []
    review_dir = os.path.join(wiki_path, 'wiki/review')
    if not os.path.exists(review_dir):
        return overdue

    cutoff = (datetime.now() - timedelta(days=threshold_days)).strftime('%Y-%m-%d')

    for f in os.listdir(review_dir):
        if not f.endswith('.md'):
            continue
        fpath = os.path.join(review_dir, f)
        rel = f"wiki/review/{f}"
        try:
            with open(fpath, 'r', encoding='utf-8') as fp:
                content = fp.read()
        except:
            continue

        in_fm = False
        created = None
        for line in content.split('\n'):
            if line.strip() == '---':
                if not in_fm:
                    in_fm = True
                    continue
                else:
                    break
            if in_fm and line.startswith('created:'):
                created = line.split(':', 1)[1].strip()

        if created and created < cutoff:
            overdue.append({"file": rel, "created": created, "overdue_days": (datetime.now() - datetime.strptime(created, '%Y-%m-%d')).days})

    return overdue

def check_index_completeness(wiki_path: str) -> list[dict]:
    """Check index.md vs filesystem consistency."""
    issues = []
    index_path = os.path.join(wiki_path, 'wiki/index.md')
    wiki_dir = os.path.join(wiki_path, 'wiki')

    fs_pages = set()
    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if f.endswith('.md') and f not in ['index.md', '_redirects.yaml'] and not f.startswith('log'):
                rel = os.path.join(root, f).replace(wiki_path + '/', '')
                fs_pages.add(rel)

    index_pages = set()
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        for _, target in find_wikilinks(content):
            index_pages.add(target)

    for page in fs_pages:
        slug = page.replace(wiki_path + '/wiki/', '').replace('.md', '')
        basename = os.path.basename(slug)
        if slug not in index_pages and basename not in index_pages:
            issues.append({"issue": "file not in index", "file": page})

    return issues

def check_content_conflicts(wiki_path: str) -> list[dict]:
    """Find pages with <CONFLICT> markers or frontmatter conflicts field."""
    conflicts = []
    wiki_dir = os.path.join(wiki_path, 'wiki')
    if not os.path.exists(wiki_dir):
        return conflicts

    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if not f.endswith('.md') or f in ['index.md', 'log.md', '_redirects.yaml']:
                continue
            fpath = os.path.join(root, f)
            rel = fpath.replace(wiki_path + '/', '')
            try:
                with open(fpath, 'r', encoding='utf-8') as fp:
                    content = fp.read()
            except:
                continue

            if '<CONFLICT>' in content:
                conflicts.append({"file": rel, "issue": "contains <CONFLICT> marker"})

            # Check conflicts in frontmatter
            in_fm = False
            fm_content = []
            in_conflicts = False
            for line in content.split('\n'):
                if line.strip() == '---':
                    if not in_fm:
                        in_fm = True
                        continue
                    else:
                        break
                if in_fm:
                    fm_content.append(line)

            fm_text = '\n'.join(fm_content)
            conflict_match = re.search(r'conflicts:\s*\[([^\]]+)\]', fm_text)
            if conflict_match:
                conflicts_list = conflict_match.group(1).strip()
                if conflicts_list:
                    conflicts.append({"file": rel, "issue": f"has conflict references: {conflicts_list}"})

    return conflicts

def main():
    parser = argparse.ArgumentParser(description='LLM Wiki Lint — 10-point health check + auto-fix')
    parser.add_argument('--wiki-path', default=WIKI_PATH, help='Wiki root path')
    parser.add_argument('--fix', action='store_true', help='Auto-fix: broken links (redirects) + index completeness + log rotation')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be fixed without modifying files')
    args = parser.parse_args()

    wiki_path = args.wiki_path
    dry_run = args.dry_run

    print(f"Running lint on: {wiki_path}")
    if args.fix:
        print("[MODE] Fix mode: will auto-apply redirects")
    print("=" * 50)

    # Load redirects
    redirects = load_redirects(wiki_path)
    if redirects:
        print(f"Loaded {len(redirects)} redirect(s) from _redirects.yaml")

    results = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "wiki_path": wiki_path,
        "issues": [],
        "fixed_count": 0
    }

    # Check 1: Broken links (with auto-fix)
    broken_links, fixed_links = find_broken_wikilinks(wiki_path, redirects)

    fixable = [b for b in broken_links if b['can_fix']]
    truly_broken = [b for b in broken_links if not b['can_fix']]

    if args.fix and fixed_links and not dry_run:
        fixed_count = auto_fix_broken_links(wiki_path, fixed_links)
        results['fixed_count'] = fixed_count
        print(f"\n[AUTO-FIX] Applied {fixed_count} link fix(es) via redirects")
        # Re-scan to verify
        broken_links, _ = find_broken_wikilinks(wiki_path, redirects)
        truly_broken = [b for b in broken_links if not b['can_fix']]
        fixable = []
        print(f"[VERIFY] Re-scanned: {len(truly_broken)} truly broken links remain")
    elif args.fix and fixed_links and dry_run:
        print(f"\n[DRY-RUN] Would fix {len(fixed_links)} link(s):")
        for filepath, old_match, new_slug in fixed_links[:10]:
            print(f"  {filepath}: {old_match} → [[{new_slug}]]")
        if len(fixed_links) > 10:
            print(f"  ... and {len(fixed_links) - 10} more")

    if fixable and not args.fix:
        print(f"\n[HIGH] Broken Links (auto-fixable via redirects): {len(fixable)}")
        for b in fixable[:10]:
            print(f"  - {b['file']}: {b['broken_link']} → [[{b['new_slug']}]]")
        results['issues'].append({"check": "1. Broken Links (fixable)", "severity": "HIGH", "count": len(fixable), "details": fixable})

    if truly_broken:
        print(f"\n[HIGH] Broken Links (no redirect): {len(truly_broken)}")
        for b in truly_broken[:10]:
            print(f"  - {b['file']}: {b['broken_link']} (target: {b['target']})")
        results['issues'].append({"check": "1. Broken Links (unfixable)", "severity": "HIGH", "count": len(truly_broken), "details": truly_broken})

    # Check 2: Content conflicts
    conflicts = check_content_conflicts(wiki_path)
    if conflicts:
        print(f"\n[HIGH] Content Conflicts: {len(conflicts)}")
        for c in conflicts[:5]:
            print(f"  - {c}")
        results['issues'].append({"check": "3. Content Conflicts", "severity": "HIGH", "count": len(conflicts), "details": conflicts})

    # Check 3: Orphan pages
    orphans = find_orphan_pages(wiki_path)
    if orphans:
        print(f"\n[HIGH] Orphan Pages: {len(orphans)}")
        for p in orphans[:10]:
            print(f"  - {p}")
        results['issues'].append({"check": "2. Orphan Pages", "severity": "HIGH", "count": len(orphans), "details": orphans})

    # Check 4: Index completeness
    index_issues = check_index_completeness(wiki_path)
    if index_issues:
        print(f"\n[MEDIUM] Index Completeness: {len(index_issues)}")
        for i in index_issues[:5]:
            print(f"  - {i}")
        results['issues'].append({"check": "4. Index Completeness", "severity": "MEDIUM", "count": len(index_issues), "details": index_issues})
        if args.fix and not dry_run:
            idx_fixed = auto_fix_index_completeness(wiki_path, index_issues)
            if idx_fixed > 0:
                print(f"\n[AUTO-FIX] Added {idx_fixed} page(s) to index")
                # Re-check
                index_issues = check_index_completeness(wiki_path)
                results['issues'] = [i for i in results['issues'] if i['check'] != '4. Index Completeness']
                if not index_issues:
                    print(f"[VERIFY] Index now complete")
                else:
                    print(f"[VERIFY] {len(index_issues)} still missing")
        elif args.fix and dry_run:
            auto_fix_index_completeness(wiki_path, index_issues, dry_run=True)

    # Check 5: Frontmatter completeness
    fm_issues = check_frontmatter_completeness(wiki_path)
    if fm_issues:
        print(f"\n[MEDIUM] Frontmatter Completeness: {len(fm_issues)}")
        for i in fm_issues[:5]:
            print(f"  - {i}")
        results['issues'].append({"check": "5. Frontmatter Completeness", "severity": "MEDIUM", "count": len(fm_issues), "details": fm_issues})

    # Check 6: Stale content
    stale = check_stale_content(wiki_path)
    if stale:
        print(f"\n[MEDIUM] Stale Content (>90 days): {len(stale)}")
        for s in stale[:5]:
            print(f"  - {s['file']} (updated: {s['updated']}, {s.get('stale_days', '?')} days ago)")
        results['issues'].append({"check": "6. Stale Content", "severity": "MEDIUM", "count": len(stale), "details": stale})

    # Check 7: Tag taxonomy
    tag_issues = check_tag_taxonomy(wiki_path)
    if tag_issues:
        print(f"\n[LOW] Tag Taxonomy Compliance: {len(tag_issues)}")
        for t in tag_issues[:5]:
            print(f"  - {t}")
        results['issues'].append({"check": "7. Tag Taxonomy", "severity": "LOW", "count": len(tag_issues), "details": tag_issues})

    # Check 8: Page size
    oversized = check_page_size(wiki_path)
    if oversized:
        print(f"\n[LOW] Page Size (>500 lines): {len(oversized)}")
        for o in oversized[:5]:
            print(f"  - {o['file']} ({o['line_count']} lines)")
        results['issues'].append({"check": "8. Page Size", "severity": "LOW", "count": len(oversized), "details": oversized})

    # Check 9: Log rotation
    log_check = check_log_rotation(wiki_path)
    if log_check.get('needs_rotation'):
        print(f"\n[LOW] Log Rotation Needed: {log_check['entry_count']} entries (threshold: {log_check['threshold']})")
        results['issues'].append({"check": "9. Log Rotation", "severity": "LOW", "count": 1, "details": log_check})
        if args.fix and not dry_run:
            rot = auto_fix_log_rotation(wiki_path)
            if rot.get('rotated'):
                print(f"\n[AUTO-FIX] {rot}")
        elif args.fix and dry_run:
            auto_fix_log_rotation(wiki_path, dry_run=True)

    # Check 10: Review overdue
    overdue = check_review_overdue(wiki_path)
    if overdue:
        print(f"\n[MEDIUM] Review Overdue (>30 days): {len(overdue)}")
        for o in overdue[:5]:
            print(f"  - {o['file']} (created: {o['created']}, {o.get('overdue_days', '?')} days ago)")
        results['issues'].append({"check": "10. Review Overdue", "severity": "MEDIUM", "count": len(overdue), "details": overdue})

    # Summary
    total_issues = sum(i['count'] for i in results['issues'])
    truly_broken_count = len(truly_broken)
    print(f"\n{'=' * 50}")
    print(f"Total issues: {total_issues} ({truly_broken_count} high, {results['fixed_count']} auto-fixed)")

    # Write to log.md
    if total_issues > 0 or results['fixed_count'] > 0:
        log_path = os.path.join(wiki_path, 'wiki/log.md')
        if os.path.exists(log_path):
            fix_note = f" (auto-fixed: {results['fixed_count']})" if results['fixed_count'] > 0 else ""
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f"\n## [{datetime.now().strftime('%Y-%m-%d')}] lint | {total_issues} issues found{fix_note}\n")

    # JSON output
    results['total_issues'] = total_issues
    print("\n--- JSON OUTPUT ---")
    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
