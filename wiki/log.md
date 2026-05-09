# Wiki Changelog

## [2026-05-09] update | llm-wiki skill 1.8.4→1.8.5
- Bug fix: lint.py 第242行 `'event'` 类型错误映射到 `'### company'`，应为 `'## Events'`
- 同步更新 SKILL.md（version + changelog）+ SCHEMA.md（version + changelog）
- 操作顺序：①修lint.py → ②SKILL.md version+changelog → ③SCHEMA.md version+changelog → ④log.md

## [2026-05-09] ingest | 中国航信年报（2015-2019）
- 批量入库5个年报：dac5ed14_2015travelsky-aviation, 2d7ff618_2016travelsky-aviation-policy, 74250208_2017travelsky-aviation-policy, 340038ec_2018travelsky-aviation-policy, 6a37249d_2019travelsky-aviation-policy-tech-innovation
- raw/docs/ 入库，wiki page type: entity-event，domains: aviation/policy/tech-innovation
- 无冲突，无重复，claim_types: policy/data/fact/analysis
- 修复 index.md: event类型条目被误归company区（lint auto_fix分类bug）+ 链接格式wiki/xxx/xxx修复为裸slug
- QA: lint 0 HIGH ✅


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

## [2026-05-07] lint | 15 issues found

## [2026-05-07] lint | 16 issues found

## [2026-05-07] lint | 16 issues found

## [2026-05-07] update | AI里程碑论文批量入库（9篇）

入库9篇AI里程碑论文，全部进入review队列：
- paper_transformer_attention (1706.03762) → review/41c0ab87
- paper_bert (1810.04805) → review/5692a551  
- paper_gpt3 (2005.14165) → review/89018f77
- paper_gan (1406.2661) → review/ff5819e3
- paper_resnet (1512.03385) → review/1e0651b6
- paper_clip (2103.00020) → review/ee9e13e3
- paper_ddpm (2006.11239) → review/3597bc1c
- paper_instructgpt (2203.02155) → review/c1984bb5
- paper_llama (2302.13971) → review/2e663675
raw文件存储于 raw/papers/
PDF原文存储于 /home/agentuser/temp/papers/


## [2026-05-07] lint | 16 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 6 issues found

## [2026-05-07] lint | 6 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] update | Review队列全量清空（14件）

批量处理review队列14件：
- 9篇AI里程碑论文入库（paper/）：Transformer/BERT/GPT-3/GAN/ResNet/CLIP/DDPM/InstructGPT/LLaMA
- 5篇航信内部文档转正（event/）：梁海峰系列活动3件+江波时间戳事件+AI家交流活动
- QA通过，HIGH×0

## [2026-05-08] lint | 3 issues found

## [2026-05-08] lint | 4 issues found

## [2026-05-08] lint | 3 issues found

## [2026-05-08] lint | 3 issues found

## [2026-05-08] lint | 2 issues found

## [2026-05-08] lint | 1 issues found

## [2026-05-08] lint | 1 issues found

## [2026-05-08] lint | 0 issues found (auto-fixed: 2)

## [2026-05-08] ingest | [[9da5d623_china_southern_ai_strategy_report]] 南航深入实施创新驱动与AI赋能战略报告入库（entity-event，slug修正：undatedsasac-caac-ai-aviation-policy → china_southern_ai_strategy_report，修正 title/frontmatter/source/Related/source-link）

## [2026-05-08] ingest | [[e21409fe_china_southern_vs_travelsky_tech_innovation_comparison]] 南航vs航信科技创新对标分析报告入库（comparison）

## [2026-05-08] lint | 1 issues found

## [2026-05-08] lint | 3 issues found (auto-fixed: 2)

## [2026-05-08] lint | 3 issues found

## [2026-05-08] lint | 1 issues found

## [2026-05-08] lint | 1 issues found

## [2026-05-08] lint | 1 issues found

## [2026-05-08] lint | 45 issues found

## [2026-05-08] lint | 45 issues found

## [2026-05-08] lint | 45 issues found

## [2026-05-08] lint | 45 issues found

## [2026-05-09] lint | 1 issues found

## [2026-05-09] lint | 1 issues found

## [2026-05-09] lint | 2 issues found

## [2026-05-09] lint | 3 issues found

## [2026-05-09] lint | 4 issues found

## [2026-05-09] lint | 5 issues found

## [2026-05-09] lint | 6 issues found

## [2026-05-09] lint | 6 issues found

## [2026-05-09] lint | 6 issues found

## [2026-05-09] lint | 0 issues found (auto-fixed: 14)

## [2026-05-09] lint | 6 issues found

## [2026-05-09] lint | 6 issues found

## [2026-05-09] lint | 1 issues found

## [2026-05-09] lint | 2 issues found

## [2026-05-09] lint | 1 issues found

## [2026-05-09] lint | 2 issues found

## [2026-05-09] lint | 2 issues found
## [2026-05-09] ingest | 2020年年报 (303 claims, 303 pages)
- SHA: 4123fd78 | slug: 2020aviation | domain: aviation
- method: fitz (text density 47.7%) | claims: 303
- wiki page: wiki/entities/event/4123fd78_2020aviation.md
- commit: 685a899


## [2026-05-09] lint | 2 issues found

## [2026-05-09] lint | 2 issues found

## [2026-05-09] lint | 3 issues found

## [2026-05-09] ingest | 2021年年报 (255 claims, 255 pages)
- SHA: e84d1bd4 | slug: 2021aviation | domain: aviation
- method: fitz (text density 52.9%) | claims: 255
- wiki page: wiki/entities/event/e84d1bd4_2021aviation.md
- 手动修复 index.md auto_fix bug（||| 格式→标准 ||| 裸slug格式）
## [2026-05-09] lint | 2 issues found

## [2026-05-09] lint | 2 issues found

## [2026-05-09] lint | 3 issues found

## [2026-05-09] ingest | 2022年年报 (265 claims, 267 pages)
- SHA: e220d0d8 | slug: 2022aviation | domain: aviation
- method: fitz (text density 50.3%) | claims: 265
- wiki page: wiki/entities/event/e220d0d8_2022aviation.md
- 手动修复 slug: undatedaviation→2022aviation；手动修 index.md auto_fix format bug（第三次触发）
## [2026-05-09] lint | 3 issues found

## [2026-05-09] lint | 3 issues found

## [2026-05-09] lint | 3 issues found

## [2026-05-09] lint | 3 issues found

## [2026-05-09] lint.py bug fix | auto_fix_index_completeness 两处 bug
- Bug 1: event 类型 prefix 缺少左括号，生成错误格式（三竖线后直接是路径）
- Bug 2: slug 取值未剥离目录前缀，导致写入 wiki/entities/event/xxx
- Fix 1: prefix = `'||| [['` (line 243)
- Fix 2: slug = `os.path.basename(filepath).replace('.md', '')` (line 254)
- SKILL.md v1.8.5→v1.8.6 | SCHEMA.md v1.8.6→v1.8.7
- lint --dry-run: 0 HIGH ✓

## [2026-05-09] lint | 4 issues found

## [2026-05-09] lint | 4 issues found

## [2026-05-09] lint | 3 issues found

## [2026-05-09] lint | 3 issues found

## [2026-05-09] lint | 4 issues found
