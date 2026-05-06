#!/usr/bin/env python3
"""
LLM Wiki QA — Version Sync + Lint 双重检查

Usage:
    python qa.py [--wiki-path <path>] [--fix] [--strict]
    python qa.py --strict   # lint 有 HIGH 直接 exit 1（用于 CI/卡点）

等同于 post-commit hook 的检查逻辑，但可以手动调用。
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

WIKI_DEFAULT = '/home/agentuser/wiki'
SKILL_PATH = Path('/home/ubuntu/.hermes/skills/research/llm-wiki/SKILL.md')
SCHEMA_PATH_DEFAULT = 'schema/SCHEMA.md'


def get_version(file_path: Path) -> str:
    """提取 version: 1.2.3 或 **v1.2.3** 格式。"""
    if not file_path.exists():
        return None
    content = file_path.read_text(encoding='utf-8')

    m = re.search(r'^version:\s*([\d.]+)', content, re.MULTILINE)
    if m:
        return m.group(1)

    m = re.search(r'\*\*v([\d.]+)\*\*', content)
    if m:
        return m.group(1)

    return None


def check_version_sync(wiki_path: str) -> tuple[bool, str, str]:
    """检查双生子版本号是否同步。Returns (ok, msg, version)。"""
    schema_path = Path(wiki_path) / SCHEMA_PATH_DEFAULT

    skill_ver = get_version(SKILL_PATH)
    schema_ver = get_version(schema_path)

    if skill_ver is None:
        return False, f"无法从 SKILL.md 提取 version（路径: {SKILL_PATH}）", ""
    if schema_ver is None:
        return False, f"无法从 SCHEMA.md 提取 version（路径: {schema_path}）", ""

    if skill_ver != schema_ver:
        return False, f"版本号不一致！SKILL.md={skill_ver}, SCHEMA.md={schema_ver}", skill_ver

    return True, f"版本号同步: {skill_ver}", skill_ver


def run_lint(wiki_path: str, fix: bool = False) -> tuple[bool, str]:
    """运行 lint.py。Returns (ok, output)。"""
    lint_script = Path(wiki_path) / 'scripts' / 'lint.py'
    if not lint_script.exists():
        return False, f"lint.py 不存在: {lint_script}"

    cmd = [sys.executable, str(lint_script), '--wiki-path', wiki_path, '--dry-run']
    if fix:
        cmd.remove('--dry-run')

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except Exception as e:
        return False, f"lint.py 执行失败: {e}"

    output = result.stdout + result.stderr

    # 统计 HIGH 问题数量
    high_count = output.count('[HIGH]')
    medium_count = output.count('[MEDIUM]')
    low_count = output.count('[LOW]')

    if high_count > 0:
        return False, f"存在 {high_count} 个 HIGH 问题（另有 MEDIUM×{medium_count}, LOW×{low_count}）\n{output}"

    if medium_count > 0 or low_count > 0:
        return True, f"存在 MEDIUM×{medium_count}, LOW×{low_count}，无 HIGH 问题 ✅"

    return True, "lint 0 issues ✅"


def main():
    parser = argparse.ArgumentParser(description='LLM Wiki QA — 版本同步 + lint 检查')
    parser.add_argument('--wiki-path', default=os.environ.get('WIKI_PATH', WIKI_DEFAULT))
    parser.add_argument('--fix', action='store_true', help='自动修复 broken links')
    parser.add_argument('--strict', action='store_true', help='lint 有 HIGH 问题则 exit 1（用于 CI 卡点）')
    args = parser.parse_args()

    wiki = args.wiki_path
    print(f"\n{'='*50}")
    print(f"🔍 LLM Wiki QA — {wiki}")
    print(f"{'='*50}\n")

    # 1. 版本号同步检查
    print("① SKILL.md / SCHEMA.md 版本同步检查")
    ok, msg, ver = check_version_sync(wiki)
    status = "✅" if ok else "❌"
    print(f"   {status} {msg}")
    if not ok:
        print(f"\n   修复方法:")
        print(f"   ① 先改 SKILL.md: version + changelog")
        print(f"   ② 再改 SCHEMA.md: ## Version 标题下的 **vX.X.X**")
        print(f"   ③ 最后写 log.md（可选）")

    print()

    # 2. lint 检查
    print("② lint --dry-run 检查")
    ok, msg = run_lint(wiki, fix=args.fix)
    status = "✅" if ok else "❌"
    print(f"   {status} {msg.split(chr(10))[0]}")
    if not ok and args.fix:
        print("   → 已执行 --fix，请检查输出并重新提交")

    print(f"\n{'='*50}")
    if not ok and args.strict:
        print("❌ QA 失败（strict 模式）")
        sys.exit(1)
    else:
        print("✅ QA 完成")
    print(f"{'='*50}\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
