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
