# Wiki Changelog

> Chronological action log. Every ingest, update, and structural change recorded.
> Format: `## [YYYY-MM-DD] Action | Details`


## [2026-05-07] lint | 4 issues found

## [2026-05-07] lint | 3 issues found

## [2026-05-07] lint | 3 issues found

## [2026-05-07] lint | 2 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 1 issues found
## [2026-05-07] self-check | 自检 llm-wiki skill + wiki 知识库

- 发现并修复 index 漏录4个 event 页面（0fa43212/2c13e8df/d4da1c23/eda756e9）
- log.md 轮转 → wiki/log-2026-05.md（1254行→5行新建）
- lint.py 修复：orphan/frontmatter/index_completeness 三个检查均跳过 log* 轮转文件
- QA 0 HIGH issues


## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 1 issues found
## [2026-05-07] evolution | lint.py --fix 进化机制 v1.8.3

- 新增 auto_fix_index_completeness(): 自动将漏录页面加入 index.md（读 frontmatter 判断 section）
- 新增 auto_fix_log_rotation(): 自动轮转 log.md → log-YYYY-MM-DD.md + 创建新 log
- lint.py orphan/frontmatter/index_completeness 三处检查均跳过 log* 轮转文件
- lint.py --fix 现在覆盖: broken links + index completeness + log rotation
- SKILL.md + SCHEMA.md 双生子版本同步 → v1.8.3


## [2026-05-07] lint | 1 issues found
## [2026-05-07] update | 低空经济概念页v2

- concept_low_altitude_economy.md 占位桩 → 完整版（confidence 0.5→0.95）
- 新增12条claims（市场规模/政策脉络/应用场景/发展阶段/地方进展/挑战）
- 新增raw源文件 raw/web/low_altitude_economy_knowledge_2026.md
- 补全wikilinks（aviation/smart_civil_aviation/caac/sasac/miit）


## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 3 issues found

## [2026-05-07] lint | 4 issues found

## [2026-05-07] lint | 6 issues found

## [2026-05-07] lint | 8 issues found

## [2026-05-07] lint | 10 issues found

## [2026-05-07] lint | 12 issues found

## [2026-05-07] lint | 14 issues found
