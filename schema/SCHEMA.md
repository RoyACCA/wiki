# Wiki Schema — LLM Wiki v1.8.9

## Version
- **v1.8.9** (2026-05-09): **Bug fix**: extract_claims.py 新增 split_into_paragraphs() 两段式分段（Pass1空白行分割，Pass2单\n分割+500字符聚合），解决2024年报PDF全文无空白行导致只提取1条claim的问题；修复后2024年报入库获18条claims
- **v1.8.8** (2026-05-09): **Bug fix**: ingest.py PDF提取跳过第0页封面（<200字符检测）；extract_claims.py 分词从 `\n\n` 改为空白行检测（`(?<=\n)[ \t]*(?=\n)`），解决年报类PDF无段落分隔问题；修复后2023年报入库获438条claims
- **v1.8.7** (2026-05-09): **Bug fix**: lint.py `auto_fix_index_completeness()` 两处 bug：① event 类型 prefix 缺少 `[[`，导致生成 `||| path]]`；② slug 取值未剥离目录前缀，导致写入 `||| wiki/entities/event/xxx]]`；修复后生成正确格式 `||| [[slug]] | summary |`
- **v1.8.6** (2026-05-09): **国内网络 push GitHub 方案固化**: HTTPS 被封时，配置 SSH over 443 + gh auth git-credential，无需 VPN 即可 push。具体步骤固化到 SKILL.md Pitfalls。
- **v1.8.4** (2026-05-08): **lint.py 修复两处 bug**: ① `find_orphan_pages()` inbound map 构建漏扫 `index.md` 链接（`index.md` 本身不加入 `all_pages`，但其 wikilink 应计入 inbound），导致通过 index.md 入口的概念页面产生误报；② `check_page_size()` 只豁免 `log.md`，未豁免 `log-YYYY-MM.md` 轮转文件，导致历史日志产生 Page Size 误报；两处修复后 lint 全绿
- **v1.8.3** (2026-05-07): **进化机制 v1**: lint.py --fix 新增 index completeness 自动修复（auto_fix_index_completeness）；新增 log 轮转自动化（auto_fix_log_rotation）；lint.py skip log* 轮转文件（orphan/frontmatter/index_completeness 三处）；修复 post-commit hook 漏扫 log-YYYY-MM.md
- **v1.8.2** (2026-05-07): **Fix orphan pages false positive**: lint.py skip_types 新增 `'company'`，entity-company 类型页面不再产生 orphan 告警；迁移 00cbbaec_2025travelsky-aviation.md（company→event），修复 broken link 历史遗留问题
- **v1.8.1** (2026-05-07): **51-doc batch ingest**: 中国航信新闻/专报/政策文档入库（35 event + 14 company + 2 paper）；修复ingest.py/slug_generator.py无扩展名文件处理；修复index.md漏加16条+错误格式
- **v1.8.0** (2026-05-07): **Format standardization**: ① Provenance单行格式（`> [!source]| c001: text`）；② domain/tags YAML list格式化（无引号）；③ conflicts/versions YAML list格式化；④ 全部6个TEMPLATE标准化；⑤ lint.py: events/目录豁免orphan检查；⑥ qa.py — 版本同步+lint双重QA卡点
- **v1.7.1** (2026-05-07): **Ingest**: 网页搜索结果入库 — 2026年国资委AI+专项行动、十五五规划纲要发布、工信部"模数共振"行动；新增event页面2个、concept页面1个、raw源文件2个；更新entity_sasac/entity_miit并补充claims字段；wikilink格式已统一为underscore
- **v1.6.0** (2026-05-06): **Fix**: `estimate_confidence()` 去除对元数据字段（发布时间/浏览量）的误扣分；`detect_page_type()` 新增事件关键词（获批/入选/荣获/获颁/首次），避免被"公司"规则误判
- **v1.5.9** (2026-05-06): **New**: ingest.py 末尾新增 `auto_git_commit()`，入库后自动 git add + commit，触发 post-commit hook；wiki 初始化 git 仓库

## Domain

Aviation + AI + Policy. This wiki covers technology innovation, strategic emerging industries, future industries, and digital transformation in the context of China's aviation industry and central enterprises.

**Scope:** Civil aviation information technology, AI policy and applications, low-altitude economy, strategic新兴产业, digital transformation of central enterprises.

**Outside scope:** Personal matters unrelated to professional domain.

---

## Conventions

### Naming (ALL ENGLISH — CRITICAL)
### Wikilink Format (CRITICAL)

- Wiki page wikilinks: `[[entity_xxx]]`, `[[concept_xxx]]`, `[[person_xxx]]` (underscore, NOT hyphen)
- Related section wikilinks must use underscore format — `[[entity_xxx]]` not `[[entity-xxx]]`

- ALL filenames lowercase, hyphen-separated, English-only
- Allowed: `a-z 0-9 - _`
- NO Chinese characters, NO full-width chars, NO special symbols
- Input files with Chinese names → convert to English slug before entering `raw/`

**Raw file naming:**
```
{SHA256_prefix}_{context_aware_slug}.{ext}
```
Example: `a3f7c921_travelsky_aviation_ai_policy_2026.pdf`

**Wiki page naming:**
```
person_{name}.md           → person_jiaolei.md
company_{name}.md          → company_travelsky.md
paper_{slug}.md            → paper_llm_wiki_2026.md
event_{year}_{name}.md    → event_2026_aviation_tech.md
concept_{slug}.md         → concept_ai_policy.md
comparison_{a}_vs_{b}.md  → comparison_low_altitude_vs_ufu.md
query_{YYYYMMDD}_{topic}.md → query_20260429_cac_ai_direction.md
```

### Wiki Page Structure

Every wiki page MUST have:
1. YAML frontmatter (required)
2. `## Summary` section
3. `## Details` section with bidirectional wikilinks
4. `## Related` section

### Wikilinks

- Format: `[[english-name]]` or `[[english-name|Display Text]]`
- Every page must have ≥2 outbound wikilinks
- Never link to `raw/` files directly from wiki pages — link to wiki entity/concept pages instead
- Wikilinks to Chinese content are forbidden

### Version Control

When updating a page with new information:
- Always bump the `updated` date in frontmatter
- If new info contradicts existing content → note both with dates, mark in frontmatter: `conflicts: [page-name]`
- Flag for Lei Ge review if contradiction is major

### Ingest Entry Point

ALL source files enter via: `/home/agentuser/temp/`

Trigger command: "学习入库" (Learn & Ingest)

Workflow: Scan temp/ → Process each file → Ingest to raw/ → Compile to wiki/ → Update index + log → **QA: lint.py --dry-run (zero issues)** → Clear temp/

---

## Tag Taxonomy

### Entity Types

- person — People (named individuals)
- company — Companies and organizations
- lab — Research labs, institutes
- paper — Academic papers, reports
- event — Conferences, meetings, events

### Domain Tags

- aviation — Civil aviation industry
- policy — Government policy, regulations
- ai — Artificial intelligence, LLMs, ML
- low-altitude — Low-altitude economy, drones, eVTOL
- future-industry — Strategic emerging industries, future industries
- digital — Digital transformation, digital economy
- central-enterprise — Central state-owned enterprises
- tech-innovation — Technology innovation, R&D
- transportation — Transportation, logistics, multimodal transport

### Meta Tags

- comparison — Side-by-side comparisons
- timeline — Historical timelines
- prediction — Forecasts, forward-looking statements
- unresolved — Open questions, pending decisions
- curated — Human-curated best content

### Industry Terms

- GDS — Global Distribution System
- BSP — Billing and Settlement Plan
- 15th-five-year — 十五五规划相关

**Rule:** Every tag used on a wiki page MUST appear in this taxonomy. If a new tag is needed, add it to this taxonomy BEFORE using it.

---

## Domain Keyword Mapping (for entity extraction)

Used by slug_generator.py to detect domain context:

```
aviation:        航空, 民航, 机场, 航司, 航班, 航线, Travelsky, 中国航信, 中航信
policy:          政策, 规定, 办法, 指南, 通知, 意见, 规划, 国资委, 民航局, 工信部, 发改委
ai:              人工智能, AI, 大模型, LLM, 模型, 机器学习, 深度学习, ChatGPT, GPT
low-altitude:    低空, 无人机, eVTOL, UAM, 通用航空, 低空经济
future-industry: 未来产业, 战新, 战略性新兴产业, 新质生产力
digital:         数字化, 数字化转型, 数字经济, 数据要素
central-enterprise: 央企, 国有企业, 国企, 中央企业
tech-innovation: 科技创新, 技术创新, 研发, 创新联合体
```

---

## Page Thresholds

| Action | Condition |
|---|---|
| Create entity page | Entity appears in 2+ sources OR is central to 1 source |
| Create concept page | Concept discussed in 2+ sources |
| Add to existing page | Source mentions something already covered |
| Skip / no page | Single passing mention, minor detail |
| Split page | Page exceeds ~500 lines |
| Archive page | Content fully superseded — move to `_archive/`, remove from index |

---

## Frontmatter Required Fields

```yaml
---
id: auto-generated-uuid (8 chars minimum)
title: page title (Chinese)
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity-person | entity-company | entity-paper | entity-event | concept | comparison | query
source: raw/{subdir}/{filename}
domain: [aviation, ai, policy, ...]
tags: [entity-type, domain tags]
confidence: 0.0-1.0   # <0.9 → move to wiki/review/
summary: "3-sentence core summary"
conflicts: []          # Claim IDs that conflicted
versions: []           # Version chain for policy/data docs
claims: [              # Knowledge provenance
  {id, text, para_index, entities, domains, type}
]
---
```

---

## Confidence Thresholds

```
≥ 0.9  → Auto-ingest, normal processing
< 0.9  → Move to wiki/review/ for Lei Ge confirmation
```

Confidence is estimated by:
1. LLM entity extraction confidence (primary)
2. Rule-based fallback: regex match on known entities → high confidence; no match → low confidence

---

## PDF Processing Rules

```
TEXT_DENSITY_THRESHOLD = 0.10 (10%)
PDF_SIZE_THRESHOLD_MB = 10

Normal PDF (text density > 10%):
  → fitz direct text extraction

Small scanned PDF (density ≤ 10%, file ≤ 10MB):
  → RapidOCR fallback

Large complex PDF (density ≤ 10%, file > 10MB):
  → Move to review/ (needs VLM — rare for Lei Ge's docs)
```

Note: Lei Ge's PDFs are almost all searchable. VLM path is only for rare edge cases.

---

## Versioned Document Rules

```python
VERSION_PATTERNS = [r'v\d+', r'edition', r'version', r'第[一二三四五六七八九十\d]+版']
```

| Scenario | Action |
|---|---|
| Similarity ≥ 0.85 + regular doc | Skip (duplicate) |
| Similarity ≥ 0.85 + versioned doc | **Force ingest: if existing wiki page found → update in place (version chain); else → create new page |
| Similarity < 0.85 | Normal ingest |

---

## Dedup Database

Location: `~/.hermes/wiki/dedup.db` (SQLite)

Tables:
- `files`: sha256 (PK), filepath, filename, minhash, is_versioned, added_at

---

## Query Flow

```
Lei Ge asks question
  ↓
Read wiki/index.md → locate relevant pages
  ↓
search_files key terms
  ↓
Read relevant pages (including review/ items)
  ↓
Synthesize answer, cite [[sources]]
  ↓
Reverse沉淀 → queries/query_YYYYMMDD_{topic}.md
  ↓
Monthly: curated_generator.py → queries/curated/quarterly-review.md
```

### 反向沉淀机制（Reverse Precipitation）

**触发条件（满足任一即沉淀，无需请示）：**
- 雷哥的提问非常精彩，具有代表性或洞察力
- 生成了新的分析框架、对比表格、系统性总结
- 问答中产生了库中不存在的新知识关联
- 回答涉及多个知识点的跨域整合

**沉淀路径：** `wiki/queries/query_YYYYMMDD_{topic}.md`

**沉淀内容：**
- 原始问题（雷哥提问原文）
- 回答要点（提炼后的结构化知识）
- 知识点来源（关联的 wiki/ 页面，支持溯源）
- 价值说明（为什么值得沉淀）

**模板：** 见 `schema/TEMPLATES/query.md`

---

## Lint: 10 Health Checks

| # | Check | Severity |
|---|---|---|
| 1 | Broken wikilinks | HIGH |
| 2 | Orphan pages (no inbound links) | HIGH |
| 3 | Content contradictions (`<CONFLICT>`) | HIGH |
| 4 | Index completeness | MEDIUM |
| 5 | Frontmatter completeness | MEDIUM |
| 6 | Stale content (>90 days) | MEDIUM |
| 7 | Tag taxonomy compliance | LOW |
| 8 | Page size (>500 lines) | LOW |
| 9 | Log rotation (>500 entries) | LOW |
| 10 | Review overdue (>30 days) | MEDIUM |

---

## Log Format

```markdown
## [YYYY-MM-DD] action | subject
- Detail 1
- Detail 2
```

Actions: `ingest`, `update`, `query`, `lint`, `create`, `archive`, `delete`, `review_confirm`

Log rotation: When log.md exceeds 500 entries → rename to `log-YYYY.md`, start fresh.

---

## Review Queue

**wiki/review/ entries require Lei Ge confirmation when:**
- Entity extraction confidence < 0.9
- Slug contains `unknown`
- Version conflict needs decision
- Key person/official position mentioned

**Flow:** File lands in review/ → Report to Lei Ge → Lei Ge confirms/corrects → Agent updates wiki → Move out of review/ → Update log.md

---

## File Type Routing

| Extension | Route |
|---|---|
| .txt | Direct read → raw/docs/ |
| .md | Direct read → raw/docs/ |
| .docx | python-docx → raw/docs/ |
| .pdf | fitz/RapidOCR → raw/papers/ |
| Other | Skip, log |

---

## Redirect Map (Page Rename Safety)

Location: `wiki/_redirects.yaml`

When renaming a wiki page:
1. Update `wiki/_redirects.yaml`: add `old-slug: new-slug`
2. Run `python scripts/lint.py --fix` to auto-repair all broken links
3. Verify with `python scripts/lint.py --dry-run` first

```yaml
# wiki/_redirects.yaml
concept-aitransportationimplementation: concept-aitransportpolicy
```

---

# Schema Version

## v1.8.5 (2026-05-09)
Changes from v1.8.4: **Bug fix**: `auto_fix_index_completeness()` 第242行，`'event'` 类型错误映射到 `'### company'`，应为 `'## Events'`

## v1.6.0 (2026-05-06)
Changes from v1.5.9: `estimate_confidence()` 去除对元数据字段（发布时间/浏览量）的误扣分，短新闻稿不再误入 review；`detect_page_type()` 新增"获批/入选/荣获/获颁/首次"等事件关键词，避免被"公司"规则误判为 entity-company

## v1.5.7 (2026-05-06)
Changes from v1.5.6: ingest.py entity/concept wikilinks 生成时，domain names 中的 hyphen 未转 underscore（`low-altitude` → `low_altitude`），导致 lint 报 broken links
Changes from v1.0.0: 初始化版本，KAG paradigm, context-aware slug, two-level dedup, PDF pre-screen, Quality Gate, review queue, curated digests, redirect map, logical conflict resolution, claim-level provenance, auto-conflict-classification, 反向沉淀机制
Changes from v1.1.0: 新增 Step 8.5 自动 lint --dry-run QA（铁律①），修正 ingest.py 完成后必须手动运行 lint --dry-run，log.md 更新增加入库文件记录
Changes from v1.2.0: 新增 ingest.py `estimate_confidence()` 函数（基于内容长度/实体关键词/语种质量估算），修复 confidence 写死 0.85，修复 Step 12 Quality Gate 真正执行 move to review/，`build_wiki_page_content()` 新增 `estimated_confidence` 参数
Changes from v1.3.0: 修复 ingest.py::write_raw_file() 对 PDF 文件使用错误文本提取（500字节二进制流→fitz前三页文本），导致中文实体匹配失败；修复 docx 文本提取
Changes from v1.4.0: 修复 slug_generator.py::generate_slug() entities/domains 列表未去重导致 slug 出现重复（如 travelsky-travelsky）；新增三层去重：entities去重、domains去重、slug_parts最终去重
Changes from v1.5.0: 修复 lint.py redirect auto-fix 双重 bug：① find_broken_wikilinks() 把 redirect 可修复链接同时放入 broken+fixed 列表，导致 --fix 条件永远不满足；② auto_fix_broken_links() 用 [2:-2] 截断已存储的裸 slug，导致匹配失败
Changes from v1.5.1: 自检修复：SCHEMA.md v1.5.0→v1.5.1 同步（v1.5.1发布时漏了SCHEMA更新）；index.md/log.md header total pages 63→70
Changes from v1.5.2: 教训固化：Pitfalls 新增「SKILL/SCHEMA 同步铁律（已固化）」，明确双生子版本更新三步操作顺序
Changes from v1.5.3: 修复 lint.py redirect auto-fix 双重 bug：① find_broken_wikilinks() 把 redirect 可修复链接同时放入 broken+fixed 列表，导致 --fix 条件永远不满足；② auto_fix_broken_links() 用 [2:-2] 截断已存储的裸 slug，导致匹配失败
Changes from v1.5.4: ingest.py build_wiki_page_content() wikilink格式从 `[[entity-xxx]]` (hyphen) 修正为 `[[entity_xxx]]` (underscore)；title生成新增去除SHA前缀逻辑；将6个错误分类至entities/company/的event页移至entities/event/
Changes from v1.5.5: SKILL.md正文标题v2.1.2→v1.5.4（版本统一）；SCHEMA.md内部Schema Version v1.5.3→v1.5.4（版本统一）；修复index.md company类目混入概念类entity（entity_llm/ai/low_altitude_economy/new_quality_productivity），移至concepts/，type改为concept；补充_redirects.yaml redirects
## Appendix: Script Interface Reference

### detect_claim_type (extract_claims.py)

```python
def detect_claim_type(text: str, entities: list, domains: list) -> str:
    """
    Classify a claim into one of four types for conflict resolution.
    Returns: 'policy' | 'data' | 'fact' | 'analysis'

    - policy: 规定/办法/指南/通知/意见/规划等规范性文件特征
    - data: 数字+时间戳（如"2024年营收100亿"）
    - fact: 一般陈述性语句
    - analysis: 认为/分析/判断/预测/建议等主观性语句
    """
```

**注意：** `entities` 和 `domains` 参数在当前实现中未使用，可传空列表 `[]`。

### Ingest Result Schema

ingest.py 的 `result` 字典必须包含以下字段：

```python
result = {
    "status": "success" | "skipped" | "error",
    "source": str,           # 原始文件路径
    "dest": str,             # raw/ 目标路径
    "page_created": bool,
    "page_updated": bool,
    "new_claims": list,      # 来自 extract_claims_from_text
    "conflicts": list,       # 冲突列表
    "dedup": str,            # "exact-match" | "similar" | "new"
    "claims_types": list,    # ["policy", "data", ...] — 必填，供 conflict_resolver 使用
}
```

### Conflict Resolution Claim Types

conflict_resolver.py 根据 claim type 决定处理策略：

| Type | 冲突行为 |
|---|---|
| `policy` | 自动更新（较新政策覆盖旧政策） |
| `data` | 自动更新（较新数据覆盖旧数据） |
| `fact` | 标记待雷哥确认（历史事实不可回溯修改） |
| `analysis` | 保留两者，不冲突（不同分析视角共存） |

### Tag Taxonomy Parser (lint.py)

lint.py 的 `check_tag_taxonomy()` 会解析 SCHEMA.md 中的 Tag Taxonomy section，
自动提取所有有效 tags 用于校验。代码块内的 tags 会被正确跳过。
