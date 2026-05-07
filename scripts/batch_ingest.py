#!/usr/bin/env python3
"""Batch ingest all .txt files from /home/agentuser/temp/"""

import sys
import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from ingest import ingest_file

TEMP_DIR = '/home/agentuser/temp'

files = sorted(os.listdir(TEMP_DIR))
txt_files = [f for f in files if f.endswith('.txt')]

print(f"Found {len(txt_files)} .txt files to ingest")
print("=" * 60)

results = []
for i, fname in enumerate(txt_files, 1):
    fpath = os.path.join(TEMP_DIR, fname)
    print(f"[{i}/{len(txt_files)}] {fname[:50]}...")
    try:
        result = ingest_file(fpath)
        results.append({'filename': fname, 'result': result})
        status = result.get('status', 'unknown')
        print(f"  → {status.upper()}")
        if status == 'success':
            dest = result.get('dest', '')
            print(f"  → dest: {dest}")
        elif status == 'skipped':
            print(f"  → reason: {result.get('reason', 'unknown')}")
        elif status == 'error':
            print(f"  → ERROR: {result.get('error', 'unknown')}")
    except Exception as e:
        print(f"  → EXCEPTION: {e}")
        import traceback
        traceback.print_exc()
        results.append({'filename': fname, 'result': {'status': 'error', 'error': str(e)}})
    print()

print("=" * 60)
print(f"Done: {len(results)} files")
success = [r for r in results if r['result'].get('status') == 'success']
skipped = [r for r in results if r['result'].get('status') == 'skipped']
errors = [r for r in results if r['result'].get('status') == 'error']
print(f"  Success: {len(success)}")
print(f"  Skipped (dedup): {len(skipped)}")
print(f"  Errors: {len(errors)}")

with open('/tmp/batch_ingest_results.json', 'w', encoding='utf-8') as fp:
    json.dump(results, fp, ensure_ascii=False, indent=2)
print(f"\nResults → /tmp/batch_ingest_results.json")
