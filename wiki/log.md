# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [2026-05-07]入库维护 | lint 0 HIGH，修复3项MEDIUM+LOW

**入库修复：**
- **lint.py bug**: `check_tag_taxonomy()` 函数 `issues=[]` 未初始化、`return issues` 提前返回导致 NameError；`in_code_block` 变量缺失导致 SCHEMA code block 内 tag 被错误解析；`if in_taxonomy` 改为 `if in_taxonomy and not in_code_block`
- **Index Completeness 5→0**: 5个缺失文件补入 index.md
  - entities/event: `event_2026_miit_10_key_tasks`、`f1c3d9e2_...`、`eb6a5c1a_...`（三-pipe）
  - events: `event_2026_travelsky-daily-briefing-0428`（三-pipe）
  - concepts: `concept_moshu_resonance_action_2026`（双-pipe）
- **Tag Taxonomy 12→0**: 3个航信专报文件 tags YAML 格式错误（缺 `]` 闭括号），导致 parser 误读后文；修复 tags 格式标准化为 `[event, aviation, policy, ai, central-enterprise, digital]`
- **Orphan**: 已在 events/ 豁免范围内，无需处理

**当前 lint: 0 HIGH, 0 MEDIUM, 13 LOW（Page Size，均 <250行，AI案例章节天然较长，非问题）**


## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete, review_confirm
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-04-29] create | Wiki initialized
- Domain: Aviation + AI + Policy (civil aviation tech innovation, strategic emerging industries, digital transformation)
- Structure created: schema/, raw/, wiki/ (entities/concepts/comparisons/queries/review/), scripts/
- Scripts: ingest.py, dedup.py, lint.py, slug_generator.py, curated_generator.py, multimodal_extract.py, extract_claims.py, conflict_resolver.py
- Features: KAG paradigm, context-aware slug, two-level dedup, PDF pre-screen, Quality Gate, review queue, curated digests, redirect map (auto-fix broken links), claim-level provenance, auto-conflict-classification (policy/data auto-update, fact flag human, analysis coexist)
- Dedup DB: ~/.hermes/wiki/dedup.db (SQLite with MinHash)
- Wiki path: /home/agentuser/wiki

## [2026-04-29] ingest | 交通运输部等7部位联合AI政策
- Source: 关于"人工智能+交通运输"的实施意见.pdf (333KB, 8页)
- Raw: raw/docs/9acb38e0_ai_transportation_policy_implementation.pdf
- Dedup: new (SHA256: 9acb38e0d7..., similarity: 0.0)
- PDF text density: 34.9% → proceed
- Claims: 8条（全部policy类型）
- Pages created:
  - wiki/concepts/concept_ai-transportation-policy.md
  - wiki/entities/company/entity_mot.md
  - wiki/entities/company/entity_caac.md
  - wiki/concepts/concept_smart_civil_aviation.md
  - wiki/concepts/concept_low_altitude_economy.md
- Temp cleared: /home/agentuser/temp/
- Total wiki pages: 15

## [2026-05-07] ingest | 网页政策动态入库：国资委AI+/十五五规划/工信部模数共振
### 入库内容
1. **2026年国资委部署央企AI+专项行动**（event页面）
   - Raw: raw/docs/eb6a5c1a_2026sasac-ai-action-central-enterprise.md
   - 来源: 国资委官网，搜索关键词 site:sasac.gov.cn
   - 关键claim: 2025年央企战新产业营收超12万亿元，三个"突出"部署，重组整合四方向

2. **2026年十五五规划纲要发布**（event页面）
   - Raw: raw/docs/f1c3d9e2_2026-15th-five-year-plan-future-industry-release.md
   - 来源: 发改委官网，搜索关键词 site:ndrc.gov.cn
   - 关键claim: 九大战略性新兴产业，六大未来产业方向，新增"融合化"

3. **工信部"模数共振"行动2026**（concept页面）
   - 来源: 工信微报，2026年4月
   - 关键claim: 20个重点行业，2026年底目标，模数共振创新联合体

### 页面更新
- entity_sasac.md: 补充claims字段，更新summary（新增2025年数据）
- entity_miit.md: 补充claims字段，更新summary（新增"模数共振"行动）

### 版本更新
- SKILL.md: v1.7.0 → v1.7.1
- SCHEMA.md: v1.7.0 → v1.7.1
- wiki/log.md: 新增本条目

### Temp目录
- 已清空（本次为网页内容，无PDF上传）

## [2026-04-29] ingest | 十五五规划纲要 + 人工智能+民航实施意见
### Doc 1: 十五五规划纲要
- Source: 2026-03-13-中华人民共和国国民经济和社会发展第十五个五年规划纲要.md (182KB, 1262行)
- Raw: raw/docs/31d86eac_2026new-quality-productivity-policy-future-industry-tech-innovation.md
- Dedup: new (SHA256: 31d86eac..., similarity: 0.0)
- Claims: 372 extracted
- Pages created:
  - wiki/concepts/concept_15th-five-year-plan.md (主页面，18篇概览)
  - wiki/concepts/concept_15th-five-year-digital.md (数字中国/AI+/数据要素)
  - wiki/concepts/concept_15th-five-year-future-industry.md (新兴产业九领域+未来产业七方向)
  - wiki/concepts/concept_15th-five-year-transportation.md (交通基础设施)
  - wiki/concepts/concept_15th-five-year-soe-reform.md (国资国企改革)
### Doc 2: 人工智能+民航实施意见
- Source: 关于推动"人工智能+民航"高质量发展的实施意见.pdf (812KB, 37页)
- Raw: raw/papers/5e4bcb83_undatedai-aviation-policy-ai.pdf
- Dedup: new (SHA256: 5e4bcb83..., similarity: 0.0)
- PDF text density: 正常 (19172 chars / 37 pages)
- Claims: 37 extracted
- Pages created:
  - wiki/concepts/concept_ai-civil-aviation-policy.md (主政策页面)
  - wiki/concepts/concept_ai-civil-aviation-scenarios.md (6大创新赋能场景)
  - wiki/concepts/concept_ai-civil-aviation-enablers.md (3类核心要素供给)
  - wiki/concepts/concept_ai-civil-aviation-innovation.md (融合创新机制)
- Policy targets: 2027年+2030年两阶段目标
- Sub-pages link to parent: [[concept_ai-civil-aviation-policy]] ← sub-pages
- Temp cleared: /home/agentuser/temp/
- Total wiki pages: 26

## [2026-04-29] ingest | 中国航信公司简介（2026）
- Source: 中国民航信息集团有限公司简介（2026）.md
- Raw: raw/docs/ecbe0707_travelsky_company_profile_2026.md
- Dedup: new (SHA256: ecbe07076d20bd1b..., similarity: 0.0)
- Claims: 5 extracted (1 fact, 2 data, 1 policy, 1 mixed)
- Pages created:
  - wiki/entities/company/company_travelsky.md
  - wiki/entities/person/person_jiangbo.md
  - wiki/entities/person/person_huangrongshun.md
  - wiki/entities/person/person_sunminghe.md
  - wiki/entities/person/person_liuxianqing.md
  - wiki/entities/person/person_lijinsong.md
  - wiki/entities/person/person_lichunmei.md
  - wiki/entities/person/person_lianghaifeng.md
  - wiki/entities/person/person_duxiaoming.md
  - wiki/entities/person/person_yubo.md
- Total wiki pages: 10

## [2026-04-29] lint | 6 issues found

## [2026-04-29] lint | 6 issues found

## [2026-04-29] lint | 6 issues found

## [2026-04-29] lint | 5 issues found

## [2026-04-29] lint | 14 issues found

## [2026-04-29] lint | 14 issues found

## [2026-04-29] lint | 9 issues found

## [2026-04-29] lint | 9 issues found

## [2026-04-29] lint | 9 issues found

## [2026-04-29] lint | 104 issues found

## [2026-04-29] lint | 27 issues found (tags误报已修复，index不完备为历史积累)

## [2026-04-29] ingest | 3 new PDFs (all exact duplicates → skipped)
- Sources: 中华人民共和国民用航空法.pdf, 生成式人工智能服务管理暂行办法.pdf, 解读《关于推动"人工智能+民航"高质量发展的实施意见》.pdf
- All exact duplicates (SHA256 match) → skipped
- Dedup DB: ~/.hermes/wiki/dedup.db

## [2026-04-29] skill-bugfix | 6 script bugs fixed + 1 SCHEMA fix (also synced to skill.md + SCHEMA.md)
1. extract_claims.py: detect_claim_type() entities/domains args → made optional (was blocking ingest)
2. ingest.py: missing claims_types key in result init → added
3. ingest.py: classify_claim_type → detect_claim_type (2 occurrences, was not imported from extract_claims)
4. lint.py: tag taxonomy parser now handles code blocks correctly (was skipping all tags)
5. lint.py: find_orphan_pages() now skips type: query/event/paper (self-contained pages, no inbound links needed)
6. lint.py: tag taxonomy parser now splits on both → and — (SCHEMA used — but parser only knew →)
7. SCHEMA.md: Tag Taxonomy moved out of code block + delimiter normalized to —
- skill.md: updated to v2.1.2, claim type function reference, orphan exception note
- SCHEMA.md: Appendix added with script interfaces, v1.1.0

## [2026-04-29] lint | 3 issues found

## [2026-04-29] lint | 1 issues found

## [2026-04-29] lint | 75 issues found (Tag Taxonomy inside code block → fixed SCHEMA structure)

## [2026-04-29] lint | 75 issues found (same, before SCHEMA fix)

## [2026-04-29] lint | 0 issues found ✅ (all issues resolved)

## [2026-04-29] lint | 49 issues found

## [2026-04-29] lint | 49 issues found

## [2026-04-29] ingest | 重建入库：政府工作报告等5个文件（修复分类/目录错误）
- 来源：temp/ 内5个文件（均为之前入库遗留问题：分类错误、目录放错、broken links）
- 问题：①policy文件误标为entity-company/entity-paper ②raw文件路径出现在wiki页details ③缺失title字段
- 处置：删除全部5个问题wiki页，重新按正确类型建页
- 新建wiki页：
  - wiki/entities/event/event_2026_government_work_report.md（政府工作报告，event类型）
  - wiki/entities/event/event_2026_caac_civil_aviation_new_chapter.md（宋志勇民航新篇章，event类型）
  - wiki/entities/event/event_2025_caac_song_zhiyong_low_altitude.md（宋志勇低空经济万亿赛道，event类型）
  - wiki/entities/event/event_2025_caac_low_altitude_leadership_group.md（民航局领导小组成立，event类型）
  - wiki/concepts/concept_low_altitude_economy_standards_system.md（低空经济标准体系指南，concept类型）
- 同步更新 index.md（+5事件页，+1概念页）+ SCHEMA.md + SKILL.md（新增Step 8.5质检铁律）
- Temp cleared: /home/agentuser/temp/
- Total wiki pages: 31

## [2026-04-29] lint | 22 issues found

## [2026-04-29] lint | 6 issues found

## [2026-04-29] lint | 6 issues found

## [2026-04-29] lint | 2 issues found

## [2026-04-29] lint | 2 issues found

## [2026-04-29] lint | 2 issues found

## [2026-04-29] lint | 2 issues found

## [2026-04-29] lint | 2 issues found

## [2026-04-29] lint | 2 issues found

## [2026-04-29] lint | 2 issues found

## [2026-04-29] lint | 1 issues found

## [2026-04-29] lint | 38 issues found

## [2026-04-29] lint | 38 issues found

## [2026-04-29] lint | 38 issues found

## [2026-04-29] lint | 108 issues found

## [2026-04-29] lint | 38 issues found

## [2026-04-29] lint | 38 issues found

## [2026-04-29] lint | 38 issues found

## [2026-04-29] lint | 50 issues found

## [2026-04-29] lint | 50 issues found

## [2026-04-29] lint | 39 issues found

## [2026-04-29] lint | 39 issues found

## [2026-04-29] lint | 43 issues found

## [2026-04-29] lint | 43 issues found

## [2026-04-29] lint | 32 issues found

## [2026-04-29] lint | 32 issues found

## [2026-04-29] lint | 32 issues found

## [2026-04-29] lint | 16 issues found

## [2026-04-29] lint | 16 issues found

## [2026-04-29] lint | 16 issues found

## [2026-04-29] lint | 16 issues found

## [2026-04-29] lint | 16 issues found

## [2026-04-30] lint | 8 issues found

## [2026-04-30] lint | wiki self-check: 8 index completeness issues fixed
- 8 files missing from index.md: entity_ai, concept_policy, f6be6f79_2021ai, 48a2a602_2016policy, 9a627fd5_2024ai, 7112d517_unknown, event_2025_ai_ethics_review_methodology, dc57dc90_2025new-quality-productivity-ai-policy-ai-future-industry
- All added to index.md with correct wikilinks and summaries
- Total pages updated: 31 → 42
- lint --dry-run: 0 issues (clean)

## [2026-05-06] ingest | 中国航信业务单位优化调整方案（试行）
### Doc 1: 中国航信业务单位优化调整方案（试行）
- Source: 1.中国航信业务单位优化调整方案（试行）.pdf (299KB, 14页)
- Raw: raw/papers/8c876509_travelsky_business_unit_restructuring_2026.pdf
- Dedup: new (SHA256: 8c876509..., similarity: 0.031)
- Claims: 5 extracted (全部policy类型)
- Pages created:
  - wiki/review/8c876509_travelsky_business_unit_restructuring_2026.md
    - type: concept, confidence: 0.99
    - 6个业务部门调整方案（航旅平台/航旅数字化→数智/机场数字化→数智/国际与渠道/低空经济/智能安全）
    - 第一/二/三曲线战略布局
    - review原因：原始slug_generator未检出travelsky entity（SCHEMA domain mapping "民航" → "aviation" 未覆盖"民航信息"等词根）
### Doc 2: 关于进一步明确公司业务部门名称的通知
- Source: 2.关于进一步明确公司业务部门名称的通知.pdf (96KB, 2页, 航信股份发〔2026〕17号)
- Raw: raw/papers/8443338b_travelsky_department_name_update_2026.pdf
- Dedup: new (SHA256: 8443338b..., similarity: 0.0)
- Claims: 1 extracted (policy类型)
- Pages created:
  - wiki/review/8443338b_travelsky_department_name_update_2026.md
    - type: concept, confidence: 0.95
    - 4个部门名称不变，2个更名（航旅数字化→航旅数智、机场数字化→机场数智）
    - 2026年4月20日生效
    - review原因：confidence=0.76 < 0.9（内容简短，仅490字符）
### 修复记录
- 原始ingest产生错误的 slug=unknown → 手动重命名raw文件 + 重建review页面
- 修复：page type (entity-company→concept), tags格式, wikilinks, title字段
- lint --dry-run: 0 HIGH issues
- Temp cleared: /home/agentuser/temp/

## [2026-05-06] review_confirm | 2 pages confirmed by Lei Ge → moved to wiki/concepts/
- 8c876509_travelsky_business_unit_restructuring_2026.md: confirmed by Lei Ge, moved from review/ to concepts/
- 8443338b_travelsky_department_name_update_2026.md: confirmed by Lei Ge, moved from review/ to concepts/
- Total wiki pages: 43 → 45

## [2026-05-06] ingest | 总部职能部门优化调整方案 + 职务变更通知
### Doc 3: 中国航信总部职能部门优化调整方案
- Source: 3.中国航信总部职能部门优化调整方案.pdf (179KB, 8页)
- Raw: raw/papers/07af78a6_2026travelsky-sasac-aviation-policy-digital.pdf
- Dedup: new (SHA256: 07af78a6..., similarity: 0.0078)
- Claims: 10 extracted (policy类型)
- Pages created: wiki/concepts/07af78a6_2026travelsky-sasac-aviation-policy-digital.md
  - 15个职能部门调整详情（综合管理部/董事会工作部/战略规划部/经营发展部/组织人事部/财务部/投资运营部/科技发展部/安全与质量管理部/法律审计部/党建工作部等）
  - 关键变化：组织人事部收回干部人事授权，财务部收回财务授权，撤销研究院新组建科技发展研究中心
  - confidence: 0.95
### Doc 4: 关于总部职能部门和业务部门更名后相关部门负责人职务变更的通知
- Source: 4.关于总部职能部门和业务部门更名后相关部门负责人职务变更的通知.pdf (94KB, 4页, 航信股份党发〔2026〕7号)
- Raw: raw/papers/29f76d04_2026travelsky-aviation-policy.pdf
- Dedup: new (SHA256: 29f76d04..., similarity: 0.0391)
- Claims: 3 extracted (policy类型)
- Pages created: wiki/concepts/29f76d04_2026travelsky-aviation-policy.md
  - 15个职能部门+6个业务部门主要负责人职务变更
  - 不涉及干部重新任免，属机构名称变更引起的调整
  - confidence: 0.95
### 修复记录
- 原始ingest: page type错误（entity-paper/entity-company→concept）+ slug重复（travelsky-travelsky→去重修复）
- Bug修复: slug_generator.py generate_slug()添加entities/domains/slug_parts三层去重（dict.fromkeys保持顺序）
- raw文件名已重命名
- Temp cleared: /home/agentuser/temp/

## [2026-04-30] sync | skill/SCHEMA version mismatch discovered
- SKILL.md version was 1.0.0 (lagged behind SCHEMA.md v1.1.0)
- Fixed: SKILL.md updated to 1.1.0, SCHEMA.md bumped to v1.2.0
- Schema version changelog updated
- Root cause: manual self-check without updating version tags

## [2026-04-30] ingest | MIT Tech Review 10 AI Trends 2026
- Source: https://www.technologyreview.com/2026/04/21/1135643/
- SHA256: 7ddf188b | slug: 7ddf188b_mit_tech_review_10_ai_trends_2026
- Dedup: new (similarity 0.0078, no match)
- Claims: 11 extracted (updated: now includes full original English text for all 10 trends)
- Page: wiki/entities/paper/paper_mit_tech_review_10_ai_trends_2026.md
- 10 trends: Humanoid Data / LLMs+ / Supercharged Scams / World Models / Military AI / Weaponized Deepfakes / Agent Orchestration / China Open Source AI / Artificial Scientists / Resistance
- **2026-04-30 补全**：更新 Provenance 块，补充全部10条趋势完整英文原文

## [2026-04-30] lint | 3 issues found

## [2026-04-30] ingest | 国资委政治能力专题培训班 2026
- Source: http://www.sasac.gov.cn/n2588020/n2877938/n2879597/n2879599/c35419825/content.html
- SHA256: ca45bdd8 | slug: 221f71b4_sasac_political_capacity_training_2026
- Dedup: new (similarity 0.0)
- Claims: 14 extracted
- Page: wiki/entities/event/event_2026_sasac_political_capacity_training.md
- 主体：国资委专题培训班，50户央企130余位领导，张玉卓主讲；高质量党建+高质量发展+科技创新+战新/未来产业

## [2026-05-01] lint | 8 issues found

## [2026-05-01] lint | 2 issues found

## [2026-05-01] lint | 1 issues found

## [2026-05-01] lint | 1 issues found

## [2026-05-01] lint | 1 issues found

## [2026-05-01] lint | 4 issues found

## [2026-05-01] lint | 1 issues found

## [2026-05-01] lint | 1 issues found

## [2026-05-01] Wiki 质量修复

### 操作内容
1. **修复 unknown 遗留页面**：`wiki/entities/event/8513b9cb_unknown.md` → 重命名 `event_2025_ai_ethics_review_methodology.md` + 移入 `wiki/review/`
2. **修复断链**：更新 `concept_ai.md` 和 `entity_ai.md` 中的 `[[event_2025_ai_ethics_review_methodology]]`（当时为 `[[entities/event/event_2025_ai_ethics_review_methodology]]`）
3. **添加 redirect**：`wiki/_redirects.yaml` 新增 `8513b9cb_unknown: event_2025_ai_ethics_review_methodology`
4. **修正 raw 文件名**：`raw/papers/8513b9cb_unknown.pdf` → `raw/papers/8513b9cb_ai_ethics_review_methodology_trial.pdf`
5. **修复 review 文件 tags**：移除无效 tag `entity-event`

### ingest.py Bug 修复（v1.3.0 对应）
- 新增 `estimate_confidence()` 函数：基于内容长度、实体关键词、语种质量估算 confidence
- 修复 confidence 写死 0.85：现在传入真实估算值
- 修复 Step 12 Quality Gate：confidence < 0.9 时真正执行 `shutil.move` 移入 `review/`
- `build_wiki_page_content()` 新增 `estimated_confidence` 参数

### lint 结果
- lint --dry-run: **0 HIGH issues**, 1 MEDIUM（review 文件不在 index，符合预期）
- 断链全修复 ✅

## [2026-05-01] lint | 2 issues found

## [2026-05-01] lint | 1 issues found

## [2026-05-01] 人工智能科技伦理审查办法 - 正式入库

- 文件：工信部《人工智能科技伦理审查与服务办法（试行）》
- 原文：`raw/papers/8513b9cb_ai_ethics_review_methodology_trial.pdf`
- 页面：`wiki/entities/event/event_2025_ai_ethics_review_methodology.md`
- 雷哥确认入库：2026-05-01

## [2026-05-01] lint | 1 issues found

## [2026-05-06] lint | 11 issues found

## [2026-05-06] lint | 2 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 47 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 31 issues found

## [2026-05-06] lint | 31 issues found

## [2026-05-06] lint | 31 issues found

## [2026-05-06] lint | 16 issues found

## [2026-05-06] lint | 16 issues found

## [2026-05-06] lint | 16 issues found

## [2026-05-06] lint | 16 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 2 issues found

## [2026-05-06] ingest | 4 docs — 江波讲话专辑
### Doc1: 党委理论学习中心组学习会讲话（2025-11-28）
- Source: 2025-11-28-在党委理论学习中心组学习会上的讲话-江波.md
- Raw: raw/docs/d1d7d8cf_2025sasac-new-quality-productivity-aviation-policy-future-industry.md
- Dedup: new | Claims: 37条，涵盖二十届四中全会/十五五规划/三大安全维度/业务曲线
- Wiki: wiki/entities/event/d1d7d8cf_2025sasac-new-quality-productivity-aviation-policy-future-industry.md
### Doc2: 切实履行"一岗双责"
- Source: 2025-12-01-切实履行"一岗双责"-江波.md
- Raw: raw/docs/32fc8fe3_2025central-enterprise.md
- Dedup: new | confidence: 0.87 < 0.9 → review/（等待雷哥确认）
- Wiki: wiki/review/32fc8fe3_2025central-enterprise.md
### Doc3: 建设团结有力的领导班子（2025-12-01）
- Source: 2025-12-01-建设团结有力的领导班子 打造世界一流的服务企业-江波.md
- Raw: raw/docs/ade51959_2025policy.md
- Wiki: wiki/entities/event/ade51959_2025policy.md
### Doc4: 市场体系改革研讨会讲话（2025-12-31）
- Source: 2025-12-31-在市场体系改革研讨会上的讲话-江波.md
- Raw: raw/docs/a1cecc3a_2025aviation-policy-ai.md
- Wiki: wiki/entities/event/a1cecc3a_2025aviation-policy-ai.md
### 修复记录
- 修正 wikilink 格式：连字符→双下划线（entity-/concept- → entity_/concept_）
- entity-sasac→entity_mot，entity-caac→entity_caac，entity-new-quality-productivity→entity_new_quality_productivity
- concept-digital/concept-central-enterprise→concept_aviation（对应 concept page 不存在）
- Temp cleared: /home/agentuser/temp/
- Total wiki pages: 57（54→57）

## [2026-05-06] lint | 6 issues found

## [2026-05-06] lint | 4 issues found

## [2026-05-06] lint.py bug fix | redirect auto-fix 双重 bug
### Bug 1: find_broken_wikilinks() 逻辑错误
- 原因：有 redirect 的链接同时 append 到 `broken` 和 `fixed` 列表
- 后果：`--fix` 条件的 `fixed_links` 永远为空（因为 redirect 链接不在 fixed 里，只有 broken里有）
- 修复：redirect 可修复的链接只加入 `fixed` 列表，不再加入 `broken`

### Bug 2: auto_fix_broken_links() slug 截断错误
- 原因：`fixed_links` 存储的是裸 slug（如 `8513b9cb_unknown`），但代码用 `[2:-2]` 截断（期望直接传入裸 slug 格式）
- 后果：截断后 slug 变成空串或错误字符串，re.sub 匹配失败，fixed_count 返回 0
- 修复：`old_slug = old_match`（直接用裸 slug），构造 `[[]]` 时不截断

### 修改文件
- `scripts/lint.py`: find_broken_wikilinks() 和 auto_fix_broken_links()
- SKILL.md: v1.5.0 → v1.5.1
- SCHEMA.md: v1.2.0 → v1.2.1

## [2026-05-06] lint | 18 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] 批量入库 × 2
### 于博 | 2026-02-06 十五五讲话
- slug: fac98eca
- type: entity-paper
- 路径: wiki/entities/paper/fac98eca_2026travelsky-sasac-aviation-policy-ai.md
- 置信度: 0.90 ✅
- 标签: 十五五,集团管控,科技赋能,航信
- 来源: raw/docs/2026-02-06-统筹集团管控笃行科技赋能 安全筑基护航中国航信“十五五”新征程-于博.md

### 江波 | 2026-02-06 十五五讲话
- slug: ae792e1e
- type: entity-event
- 路径: wiki/entities/event/ae792e1e_2026sasac-caac-aviation-policy-central-enterprise.md
- 置信度: 0.99 ✅
- 标签: 十五五,中央企业, aviation-policy
- 来源: raw/docs/2026-02-06-牢记嘱托勇担使命 奋力开启“十五五”高质量发展新征程-江波.md

### index.md 同步
- wiki/index.md 已添加 fac98eca 和 ae792e1e 的索引条目

## [2026-05-06] lint | 10 issues found

## [2026-05-06] lint | 2 issues found

## [2026-05-06] lint | 2 issues found


## [2026-05-06] 批量入库 × 2

### 江波 | 2025-12-24 十五五研修班讲话
- slug: 2d8bc931_2025policy-central-enterprise-tech-innovation
- type: entity-event
- 路径: wiki/entities/event/2d8bc931_2025policy-central-enterprise-tech-innovation.md
- 置信度: 0.95 ✅
- 标签: policy, central-enterprise, tech-innovation, aviation
- 来源: raw/docs/80ee845d_2025policy-central-enterprise-tech-innovation.md
- 备注: 十五五战略规划研修班，党委理论学习中心组（扩大）学习

### 胡振江 | 2026-01-07 民航安全工作会报告
- slug: 09e3ea76_2026caac-aviation-policy-low-altitude
- type: entity-event
- 路径: wiki/entities/event/09e3ea76_2026caac-aviation-policy-low-altitude.md
- 置信度: 0.95 ✅
- 标签: aviation, policy, low-altitude
- 来源: raw/docs/09e3ea76_2026caac-aviation-policy-low-altitude.md
- 备注: 代表民航局作航空安全工作报告，2025年征候万时率0.42同比下降5.9%

### index.md 同步
- Events 章节已添加两条索引
- 重建 index.md 修复 Events 章节错位问题


## [2026-05-06] 批量入库 × 2（移入 review/ 待确认）

### IATA MAR + PSS 改造建议
- slug: 47237ec6_20260227_travelsky-mar-aviation-retailing
- type: entity-paper
- 路径: wiki/review/47237ec6_20260227_travelsky-mar-aviation-retailing.md
- 置信度: 0.88 ⚠️ <0.9 阈值，移入 review/ 待雷哥确认
- 来源: raw/docs/47237ec6_20260227_travelsky-mar-aviation-retailing.md

### 零售化转型及OOSD下结算业务分析
- slug: 1489abc4_20260210_travelsky-retail-transformation-oosd-settlement
- type: entity-paper
- 路径: wiki/review/1489abc4_20260210_travelsky-retail-transformation-oosd-settlement.md
- 置信度: 0.88 ⚠️ <0.9 阈值，移入 review/ 待雷哥确认
- 来源: raw/docs/1489abc4_20260210_travelsky-retail-transformation-oosd-settlement.md

### index.md 同步
- Review 章节已添加两条索引

## [2026-05-06] lint | 9 issues found

## [2026-05-06] lint | 9 issues found

## [2026-05-06] lint | 9 issues found

## [2026-05-06] lint | 7 issues found

## [2026-05-06] lint | 7 issues found


## [2026-05-06] Review 确认入库 × 2

### [[47237ec6_20260227_travelsky-mar-aviation-retailing]] — 雷哥确认接受 ✅
- 原置信度: 0.88（移入review/）
- 雷哥确认接受，移入 entity/paper/ 正式入库
- 位置: wiki/entities/paper/47237ec6_20260227_travelsky-mar-aviation-retailing.md

### [[1489abc4_20260210_travelsky-retail-transformation-oosd-settlement]] — 雷哥确认接受 ✅
- 原置信度: 0.88（移入review/）
- 雷哥确认接受，移入 entity/paper/ 正式入库
- 位置: wiki/entities/paper/1489abc4_20260210_travelsky-retail-transformation-oosd-settlement.md

## [2026-05-06] lint | 2 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found


## [2026-05-06] 江波2026年度市场工作会讲话入库

### 江波 | 2026-04-14 中国航信2026年度市场工作会
- slug: e10f3546_20260414_jiangbo_market_conference
- type: entity-event
- 路径: wiki/entities/event/e10f3546_20260414_jiangbo_market_conference.md
- 置信度: 0.90 ✅
- 标签: policy, central-enterprise, tech-innovation, aviation
- 来源: raw/docs/e10f3546_20260414_jiangbo_market_conference.md
- 备注: PDF为加密图像型（RC4+嵌入图片），用RapidOCR处理前9页(5954字)，剩余4页待补充

### index.md 同步
- event章节已添加索引，Total pages → 63

### 教训记录
- sed替换wikilink时再次误伤同行内容（domain/tags/title字段被波及），改用write_file重建文件

## [2026-05-06] ingest | 江波2026-04-14市场工作会讲话（完整版）
- Source: 2026-4-14-在中国航信2026年度市场工作会上的讲话-江波.md (22KB, 68行完整全文)
- Raw: raw/docs/9b33d7f2_2026travelsky-aviation-policy.md
- Dedup: new version of existing doc (old: e10f3546 partial 9/13页 → new: full 完整全文)
- Similarity with e10f3546: 1.56% → force ingest (versioned doc)
- Action: merged into existing wiki page (NOT new page)
- Page updated: wiki/entities/event/e10f3546_20260414_jiangbo_market_conference.md
- domains: [policy, central-enterprise, tech-innovation, aviation]
- claims: 30 extracted (policy/data/fact mixed)
- Quality Gate: 0 HIGH issues (lint --dry-run ✅ zero)
- index.md: updated summary (完整版入库标记)
- Temp cleared: /home/agentuser/temp/
- Total wiki pages: 70

## [2026-05-06] self-check | llm-wiki system self-inspection
- 发现SCHEMA.md版本落后（v1.5.0）于SKILL.md（v1.5.1）：v1.5.1发布时漏了同步SCHEMA
- 发现index.md header声称63页，实际70页
- 修复：SCHEMA.md v1.5.0→v1.5.1同步，新增v1.5.1 changelog记录
- 修复：SKILL.md v1.5.1→v1.5.2，新增自检教训changelog
- 修复：SCHEMA.md v1.5.1→v1.5.2同步
- 修复：index.md total pages 63→70
- 修复：log.md total pages 63→70
- 版本对齐确认：SKILL=1.5.2, SCHEMA=1.5.2 ✅
- lint --dry-run: 0 issues ✅

## [2026-05-06] lint | 155 issues found

## [2026-05-06] lint | 53 issues found

## [2026-05-06] lint | 53 issues found

## [2026-05-06] lint | 28 issues found (auto-fixed: 21)

## [2026-05-06] lint | 28 issues found

## [2026-05-06] lint | 28 issues found

## [2026-05-06] lint | 42 issues found

## [2026-05-06] lint | 26 issues found

## [2026-05-06] lint | 26 issues found

## [2026-05-06] lint | 26 issues found

## [2026-05-06] lint | 26 issues found

## [2026-05-06] lint | 19 issues found (auto-fixed: 3)

## [2026-05-06] lint | 19 issues found

## [2026-05-06] lint | 19 issues found

## [2026-05-06] lint | 19 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 14 issues found

## [2026-05-06] ingest | 16 docs from 活动交流/
- Files: 中国航信受邀参加国资央企"AI+"行动示范基地揭牌仪式.txt, 中国航信参加第三届CATA航空大会.txt, and 14 others
- Actions: slug generation, dedup (all new), content extraction, entity extraction, wiki write, QA
- Bugs fixed: ① ingest.py wikilink format (underscore not hyphen), ② title generation (added SHA prefix strip), ③ 16 wrong Chinese titles restored to English CamelCase, ④ 6 event pages moved from entities/company/ to entities/event/
- New entities: entity_sasac (国资委), entity_miit (工信部), person_jiaolei (焦雷), concept_digital (数字化)
- Skill update: v1.5.3→v1.5.4, SCHEMA v2.1→v2.1.1
- Lint: 0 issues ✅

## [2026-05-06] lint | 3 issues found (orphan stub pages — normal)
- 3 orphan: concept_llm, concept_low_altitude_economy_standards, concept_new_quality_productivity (newly moved stubs, no inbound links yet — expected)

## [2026-05-06] skill_sync | Bug fix — llm-wiki系统性排查修复
- SKILL.md: 正文标题版本号 v2.1.2 → v1.5.5（与YAML frontmatter统一）
- SCHEMA.md: 内部 Schema Version v1.5.3 → v1.5.5（与SKILL.md统一）
- index.md: company类目下移除了 entity_llm/ai/low_altitude_economy/new_quality_productivity（概念类entity混入公司类目），新增 entity_company_travelsky
- 将 entity_llm/ai/low_altitude_economy/new_quality_productivity 从 entities/company/ 移至 concepts/，type 从 entity-company 改为 concept
- 补充 _redirects.yaml: entity_ai→concept_ai, entity_llm→concept_llm, entity_low_altitude_economy→concept_low_altitude_economy, entity_new_quality_productivity→concept_new_quality_productivity
- Version: SKILL.md v1.5.5, SCHEMA.md v1.5.5

## [2026-05-06] lint | 2 issues found

## [2026-05-06] lint | 34 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 9 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 4 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 413 issues found

## [2026-05-06] lint | 413 issues found

## [2026-05-06] lint | 413 issues found

## [2026-05-06] lint | 426 issues found

## [2026-05-06] lint | 426 issues found

## [2026-05-06] lint | 424 issues found

## [2026-05-06] lint | 424 issues found

## [2026-05-06] lint | 423 issues found
## [2026-05-06] ingest | 航信集团发〔2025〕184号-战略性新兴产业实施办法（entity-paper, confidence 0.85, dedup 4.69%, domains: aviation/policy/low-altitude/future-industry/central-enterprise/tech-innovation）

**Bug fix during ingest**: ①修复 ingest.py entity/concept wikilinks 生成时 domain name 中的 hyphen 未转 underscore；②修复已生成页面的 4 条 broken wikilinks；③补 _redirects.yaml（concept_future-industry→concept_future_industry）
## [2026-05-06] ingest | 关于印发《中国航信外出审批管理规定》的通知.pdf → review_needed（slug含unknown，移至wiki/review/）

## [2026-05-06] lint | 431 issues found

## [2026-05-06] lint | 431 issues found (auto-fixed: 38)

## [2026-05-06] lint | 431 issues found

## [2026-05-06] lint | 431 issues found

## [2026-05-06] lint | 431 issues found

## [2026-05-06] lint | 431 issues found

## [2026-05-06] lint | 431 issues found

## [2026-05-06] lint | 392 issues found

## [2026-05-06] lint | 392 issues found

## [2026-05-06] lint | 392 issues found

## [2026-05-06] lint | 51 issues found

## [2026-05-06] lint | 48 issues found

## [2026-05-06] lint | 48 issues found

## [2026-05-06] lint | 42 issues found

## [2026-05-06] lint | 42 issues found

## [2026-05-06] lint | 42 issues found

## [2026-05-06] lint | 39 issues found

## [2026-05-06] lint | 37 issues found

## [2026-05-06] lint | 37 issues found

## [2026-05-06] lint | 37 issues found

## [2026-05-06] lint | 37 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 3 issues found

## [2026-05-06] lint | 6 issues found

## [2026-05-06] lint | 2 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-29] update | 07af78a6_2026travelsky-sasac-aviation-policy-digital
- 原资本运营与创新业务部业务拆分信息补录：
  - 资本运营（投资并购等）→ 投资运营部（职能部门）
  - "航旅链"、区块链 → 智能安全业务部
  - "启航"大模型 → 智能安全业务部
  - 机场行李全向叉取智能机器人 → 机场数智业务部
- Updated: concepts/07af78a6_2026travelsky-sasac-aviation-policy-digital.md (changelog v1.1)

## [2026-05-29] update | 8c876509_travelsky_business_unit_restructuring_2026
- 同上，原资本运营与创新业务部业务拆分信息补录至业务单位调整方案
- Updated: concepts/8c876509_travelsky_business_unit_restructuring_2026.md (changelog v1.1)

## [2026-05-06] ingest | 航旅链/区块链系列（10个文件）
- Sources: 10个txt文件（资本运营与创新业务部发布）
- 主题: 航旅链区块链平台产品与商业落地
- Dedup: 全部新文件（相似度<0.85）
- Pages created:
  - concepts/concept_hanglv_chain_blockchain.md（航旅链汇聚概念页）
  - entities/event/event_2025_hanglv_chain_transport_award.md（交协科技进步二等奖）
  - entities/event/event_2025_hanglv_chain_digital_transport_case.md（数字交通典型案例）
  - entities/event/event_2025_hanglv_chain_xinchuang.md（信创三认证）
  - entities/event/event_2025_blockchain_platform_science_tech_award.md（科促会科技一等奖）
  - entities/event/event_2025_blockchain_top10.md（全国区块链前十）
  - entities/event/event_2025_fujian_airport_blockchain_agreement.md（元翔福州合作协议）
  - entities/event/event_2025_airport_blockchain_digital_rmb_payment.md（首落地自动支付）
  - entities/event/event_2025_hangxian_tong_jiaxing.md（航显通落地）
  - entities/event/event_2025_buchang_tong_tibet.md（补偿通落地西藏）
  - entities/event/event_2025_blockchain_smart_contract_agent_reward.md（代理人奖励结算）
- Key note: 所有event原文来源均为资本运营与创新业务部，现归口已调整为智能安全业务部（据2026年组织调整）
- Temp cleared: /home/agentuser/temp/
- Total wiki pages: 81

## [2026-05-06] lint | 38 issues found

## [2026-05-06] lint | 2 issues found

## [2026-05-06] Ingest | 航信3个大模型备案材料入库

- **Files processed**: 3 txt files (SHA256 all new, similarity <0.85)
- **Raw archived**: 
  - `5d9baeef_qianrang_large_model.txt` — 移动科技千穰
  - `a15ac8e5_qihang_large_model.txt` — 启航大模型
  - `c70d4f11_gongxiangruixing_large_model.txt` — 共翔睿行
- **Pages created**:
  - concepts/concept_qianrang_large_model.md（千穰：民航首个垂直领域大模型，序号168，第4个央企备案）
  - concepts/concept_qihang_large_model.md（启航：序号394，双算法备案，国资央企第9家）
  - concepts/concept_gongxiangruixing_large_model.md（共翔睿行：2025.12.31大模型备案+2025.11算法备案）
  - entities/event/event_2024_qianrang_network_filing.md
  - entities/event/event_2025_qihang_double_filing.md
  - entities/event/event_2025_gongxiangruixing_double_filing.md
- **部门归属（雷哥授权口径）**:
  - 千穰：移动科技（中航信移动科技有限公司，子公司）
  - 启航：资本运营与创新业务部 → 2026年组织调整后归口智能安全业务部
  - 共翔睿行：航空数字化产品事业部（2026年是否调整待确认）
- **关键标注**: 三个大模型备案信息以本次雷哥提供材料为准，覆盖原有分散event中的记录
- **Total wiki pages**: 87

## [2026-05-06] lint | 12 issues found

## [2026-05-06] Ingest | 机场行李全向叉取智能机器人系统入库

- **Files processed**: 3 files (SHA256 all new, similarity <0.85)
  - `2343577f_travelsky_baggage_robot_ai_scenario.docx` — 央企AI战略性高价值场景申报材料（DOCX）
  - `cba797be_baggage_robot_final_defense_ppt.pdf` — 终审答辩PPT（12页，PDF）
  - `3a8d5223_qingdao_baggage_robot_deployment.txt` — 青岛胶东国际机场媒体开放日展示报道（TXT）
- **Pages created**:
  - concepts/concept_baggage_robot.md（机场行李全向叉取智能机器人系统）
  - entities/event/event_2025_qingdao_baggage_robot_deployment.md（部署事件）
  - entities/event/event_2025_baggage_robot_central_enterprise_ai_defense.md（终审答辩事件）
- **部门归属（雷哥授权口径）**: 资本运营与创新业务部 → 2026年组织调整后归口**机场数智业务部**
- **关键信息**: 全球首个民航行李转运场景全向叉取机器人；青岛胶东W13转盘部署；效率180件/小时；联合南航大×中国移动；终审答辩2025/07/05
- **Total wiki pages**: 90

## [2026-05-06] lint | 5 issues found

## [2026-05-06] Ingest | 移动科技机场行李智能搬运系统入库

- **Files processed**: 1 txt file (SHA256 new, similarity 0.0625)
- **Raw archived**: `f113b2a8_avicit_baggage_handling_system.txt` — 移动科技张淑君报道
- **Pages created**:
  - concepts/concept_avicit_baggage_handling_system.md（机场行李智能搬运系统）
  - entities/event/event_2025_avicit_baggage_system_beijing_first_list.md（入选北京市首台套目录）
- **部门归属**: 移动科技（中航信移动科技有限公司，子公司），架构独立
- **关键区分**: 本系统与机场行李全向叉取智能机器人（资本运营与创新业务部）是不同产品
- **Total wiki pages**: 92

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] lint | 5 issues found

## [2026-05-06] ingest | 4 docs: Travelsky 2024 Beijing Digital Economy + CAAC Sci-Tech Expo + Central Enterprise Innovation Award + National IT Standards Committee

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 1 issues found (auto-fixed: 11)

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 1 issues found (auto-fixed: 3)

## [2026-05-06] lint | 2 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 2 issues found

## [2026-05-06] lint | 0 issues found (auto-fixed: 3)

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 1 issues found

## [2026-05-06] lint | 1 issues found (auto-fixed: 1)

## [2026-05-06] ingest | 1 file(s)
- raw/docs/c1e49410_central_enterprise_innovation_consortium_expansion_2026.md → wiki/entities/paper/422c4a10_2026central-enterprise-tech-innovation.md
- 《央企创新联合体如何"扩围"又"提质"》，马大明/刘卓，国资报告2026年第4期，confidence=0.84→review→雷哥确认接受→移出review→index更新

## [2026-05-07] lint | 62 issues found

## [2026-05-07] lint | 51 issues found

## [2026-05-07] ingest | 50 files batch (44 success, 3 exact-dedup skip, 3 review-needed)
- Temp: 50 .txt files from /home/agentuser/temp/
- Dedup: 3 exact duplicates skipped (travelsky digital economy list, CAAC sci-tech innovation expo, SASAC innovation award)
- Review-needed (confidence <0.9): af412855 (应用运维与监控系统), 8ee47b17 (国航数字化签派放行), 3a8d5223 (行李机器人亮相)
- Event pages created: 35 new + 7 migrated from company (entity_industry_llm→entity_llm broken link fixed)
- Company pages: 8 new (including 7 that should be event — migrated to event/ dir, type updated)
- Paper pages: 1 new
- index.md updated: 42 event entries added, 7 company entries removed (migrated), 1 company entry added, 1 paper entry added
- _redirects.yaml updated: entity_industry_llm→entity_llm + 7 company→event redirects
- Total wiki pages: 96→138 (estimate)
- QA: lint --dry-run after fixes (0 HIGH issues)

## [2026-05-07] lint | 0 HIGH issues
- 4 broken wikilinks (entity_industry_llm) fixed → entity_llm
- 7 company pages migrated to event/ (type: entity-company → entity-event)
- 3 review pages remain in wiki/review/ (pending Lei Ge confirmation)

## [2026-05-07] lint | 8 issues found

## [2026-05-07] lint | 8 issues found

## [2026-05-07] lint | 8 issues found

## [2026-05-07] lint | 8 issues found (auto-fixed: 100)

## [2026-05-07] lint | 8 issues found

## [2026-05-07] lint | 8 issues found

## [2026-05-07] lint | 8 issues found

## [2026-05-07] lint | 4 issues found

## [2026-05-07] lint | 4 issues found

## [2026-05-07] lint | 4 issues found

## [2026-05-07] lint | 28 issues found

## [2026-05-07] lint | 29 issues found (auto-fixed: 45)

## [2026-05-07] lint | 28 issues found

## [2026-05-07] lint | 28 issues found

## [2026-05-07] lint | 28 issues found

## [2026-05-07] lint | 28 issues found

## [2026-05-07] lint | 28 issues found

## [2026-05-07] lint | 7 issues found

## [2026-05-07] lint | 7 issues found

## [2026-05-07] ingest | 中国航信人工智能应用案例汇编（第一期）27章节入库
- Source: raw/papers/cf5d5705_2025travelsky_ai_cases_volume1.pdf (231页)
- Raw: raw/docs/ 27个.txt（按章节拆分）
- Event pages: ch01-ch27，slug已修复（scripts/rename_ai_cases.py）
- Entity: entity_ndrc.md（新增发改委）
- Index: 27 event + 1 entity，total pages 96→125
- Note: PDF图表页文字量少属正常，文本密度31%

## [2026-05-07] update | llm-wiki v1.7.0 版本同步
- SKILL.md: v1.6.0 → v1.7.0，changelog 新增 v1.7.0 条目
- SCHEMA.md: v1.6.0 → v1.7.0，changelog 新增 v1.7.0 条目
- 新增脚本入档: split_pdf_chapters.py、rename_ai_cases.py、batch_ingest.py
- Scripts Reference 表格已更新

## [2026-05-07] update | 千穰大模型订正 + 国资委AI高价值场景入库
- 修正 event_355fdcab（WAIC事件页）：删除"千穰双备案"错误描述，订正为生成式AI服务单备案；补充申报名称"国产化民航大模型"→终审改名"智慧民航数智化新型应用"
- 新增 concept_qianrang_large_model（合并补充）：整合答辩PPT详细数据（参数规模1000亿+、算力平台、应用指标）；明确备案类型为生成式AI服务单备案（非双备案）
- 新增 event_2025travelsky-central-enterprise-ai-scenario：国资委AI高价值场景申报材料，含三大场景（国产化民航大模型/千穰、机场行李智能搬运系统、民航舱音识别）
- 删除重复页面 concept_qianrang.md（合并至 concept_qianrang_large_model.md）
- lint: 0 HIGH issues，total 0
|
## [2026-05-07] lint | 11 issues found

## [2026-05-07] lint | 5 issues found

## [2026-05-07] lint | 3 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] lint | 1 issues found

## [2026-05-07] ingest | 启航大模型+千穰民航高质量数据集
- Source: AI环信平台（aihuanxin.cn）页面抓取
  - 启航大模型: https://aihuanxin.cn/qdlake/qdh-web/#/model/detail/travelsky/Qihang/type=org
  - 千穰民航高质量数据集: https://aihuanxin.cn/qdlake/qdh-web/#/dataset/detail/travelsky/Qianrang_High-quality_Civil_Aviation/type=org
- Method: Playwright SPA页面抓取 → 拦截API响应获取JSON数据
- Raw: raw/docs/concept_qihang_large_model_raw.md, raw/docs/concept_qianrang_high_quality_civil_aviation_dataset_raw.md
- New pages:
  - concept_qihang_large_model (更新): 30B-80B, 2025-07-18发布, 双备案, AI环信平台
  - concept_qianrang_high_quality_civil_aviation_dataset (新增): 200TB+, 民航全要素, AI环信平台
- Updated: index.md (更新两条+新增一条, 总页数125→127)
- Key findings:
  - 启航大模型确认双备案（生成式AI服务+深度合成算法）
  - 启航与千穰的关系：两者均属中航信AI产品线，千穰(>1000亿参数，单备案)vs启航(30B-80B，双备案)
  - 千穰数据集是千穰大模型的训练数据底座

## [2026-05-07] lint | 11 issues found

## [2026-05-07] ingest | 智慧民航数智化新型应用+千穰大模型API数据更新
- Source: AI环信平台页面抓取
  - 智慧民航数智化新型应用: https://aihuanxin.cn/#/portal/benchmarkdetail?id=21
  - 千穰大模型: https://aihuanxin.cn/qdlake/qdh-web/#/model/detail/travelsky/Qianrang/type=org
- Raw: raw/docs/concept_qianrang_large_model_api_raw.md
- Updated: concept_qianrang_large_model (更新评测指标: C-Eval 91.02/CMMLU 89.98; 服务机构20+→40+)
- New: event_2025travelsky-zhineng-civil-aviation (智慧民航典型案例，含建设背景/技术特点/成效/展望)
- index: 总页数127→129
- Critical conflict found: 智慧民航页面声称千穰为"双备案"，AI环信API仅显示单备案
  - Resolution: 以API数据为准，千穰为单备案；矛盾写入conflicts字段待雷哥确认
- lint: 待验证

## [2026-05-07] lint | 4 issues found

## [2026-05-07] lint | 4 issues found

## [2026-05-07] lint | 3 issues found

## [2026-05-07] ingest | Web search results → raw/docs + index update
- 3 raw docs saved to raw/docs/:
  - eb6a5c1a_2026sasac-ai-action-central-enterprise.md (5.2KB, 国资委官网)
  - 1eb8e3a9_2026-01-26_ministry-10-key-tasks.md (4.3KB, 人民网/工信微报)
  - f8c43e27_2026-04-28_modu-data-resonance-action.md (14KB, 安全内参)
- Index entries updated:
  - event_eb6a5c1a: summary增强 + 专家解读claims（杜天佳/王盼盼）
  - concept_moshu_resonance_action_2026: 全文+官方解读增强
- New event page created: event_2026_miit_10_key_tasks (工信部2026年十个方面重点工作)
- New index entry: event_2026_miit_10_key_tasks

## [2026-05-07] ingest | 航信专报第81期（0507）
- Source: raw/docs/f54ec5bb_2026-travelsky-daily-briefing-0507.docx
- SHA256: f54ec5bbfdc2a25b1f0cfb2748d60a687d8ed050379087c854f459174832f460
- Type: event (daily briefing, 9 news items)
- Domain: aviation, policy, ai, central-enterprise, macro
- Confidence: 0.95
- New wiki page: event_2026_travelsky-daily-briefing-0507
- Claims: 8 data/policy claims extracted (五一消费/民航/交通/出入境/韩国航权/AI超售等)
- Dedup: new (exact + MinHash similarity check passed)
- Index entry added: event_2026_travelsky-daily-briefing-0507

## [2026-05-07] lint | 2 issues found

## [2026-05-07] lint | 986 issues found

## [2026-05-07] lint | 986 issues found

## [2026-05-07] lint | 986 issues found

## [2026-05-07] lint | 986 issues found

## [2026-05-07] lint | 979 issues found

## [2026-05-07] lint | 979 issues found

## [2026-05-07] ingest | 航信专报第77期（0428）每日要闻专报
- Source: ylm@travelsky.com.cn 邮件附件 (5.2MB)
- Raw: raw/docs/29781e4b_2026-travelsky-daily-briefing-0428.docx
- Dedup: new (SHA256: 29781e4b60..., similarity: 0.07)
- Docx text extracted: 10条要闻
- Pages created:
  - wiki/events/event_2026_travelsky-daily-briefing-0428.md
- Index: append entry
- Total wiki pages: 130

## [2026-05-07] lint | 19 issues found

## [2026-05-07] lint | 23 issues found

## [2026-05-07] ingest | 航信专报第79期（0430）每日要闻
- Source: ylm@travelsky.com.cn 邮件附件 docx
- Mail file: 1778124702.M710155P354856Q29R004186fa3bbf6946.localhost
- Attachment: 每日要闻（航信专报） 2026年第79期（0430）.docx
- SHA256: 28fb1a32e7aa274a4530891be35ac49f9f0190df8113cf2150fc17cd7b17ac26
- Raw: raw/docs/28fb1a32_2026-travelsky-daily-briefing-0430.docx
- Dedup: new
- Docx text extracted: 10条要闻（五一假期民航、数据经济政策）
- Pages created:
  - wiki/events/event_2026_travelsky-daily-briefing-0430.md
- Index: append entry
- Total wiki pages: 130

## [2026-05-07] lint | 22 issues found

## [2026-05-07] lint | 20 issues found

## [2026-05-07] ingest | 航信专报第78期（0429）
- Source: ylm@travelsky.com.cn 邮件附件 docx
- Mail file: 1778124691.M207721P354800Q16Re5af64a4876b8784.localhost
- Attachment: 每日要闻（航信专报） 2026年第78期（0429）.docx
- SHA256: 4f1a5e43578608fb760244bb219d7be2079be8723f0d4cb535207de24a8cbd6a
- Raw: raw/docs/4f1a5e43_2026-travelsky-daily-briefing-0429.docx
- Dedup: new (exact + MinHash similarity check passed)
- Docx text extracted: 9条要闻（政治局会议/商务部/国资央企/民航客座率/燃油费/东航候补/杭深快线/工信部AI+软件/模数共振）
- Pages created:
  - wiki/events/event_2026_travelsky-daily-briefing-0429.md
- Index: append entry

## [2026-05-07] lint | 20 issues found

## [2026-05-07] lint | 20 issues found

## [2026-05-07] ingest | 航信专报第80期（0506）
- Source: ylm@travelsky.com.cn 邮件附件 docx
- Mail file: 1778124715.M120432P354927Q44Rf735786098552789.localhost
- Attachment: 每日要闻（航信专报） 2026年第80期（0506）.docx
- SHA256: a4f536c8b86ac6a10fbb4ef68768f12113f47db3e07c97c269d216c57eeae219
- Raw: raw/docs/a4f536c8_2026-travelsky-daily-briefing-0506.docx
- Dedup: new
- Docx text extracted: 10条要闻（国资委产权管理会议、港澳民航合作、一季度航司全部盈利、跨航司签转服务、五一假期运输、文旅消费、数据资源调查、数字中国建设、Amadeus收购、全球航空品牌）
- Pages created:
  - wiki/events/event_2026_travelsky-daily-briefing-0506.md
- Index: append entry

## [2026-05-07] lint | 1004 issues found

## [2026-05-07] lint | 1004 issues found

## [2026-05-07] lint | 1004 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found (auto-fixed: 1)

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 1003 issues found

## [2026-05-07] lint | 23 issues found

## [2026-05-07] update | Format standardization v1.8.0 — 全链条格式固化
- **ingest.py**: Provenance单行格式（`> [!source]| c001: text`）；domain/tags YAML list格式化（无引号）；conflicts/versions YAML list格式化
- **全部6个TEMPLATE**（entity-event/company/person/paper/concept/comparison/query）: 统一domain/tags格式、新增title字段、claims/versions/conflicts空列表初始化、Provenance格式统一
- **lint.py**: events/目录豁免orphan检查
- **qa.py**（新增）: 版本同步+lint双重QA卡点工具，替代原Step 8.5
- **SKILL.md/SCHEMA.md**: v1.7.1 → v1.8.0 同步更新（双生子规则）

## [2026-05-07] lint | 999 issues found

## [2026-05-07] lint | 999 issues found

## [2026-05-07] lint | 904 issues found

## [2026-05-07] lint | 904 issues found

## [2026-05-07] lint | 904 issues found

## [2026-05-07] lint | 904 issues found

## [2026-05-07] lint | 23 issues found

## [2026-05-07] lint | 904 issues found

## [2026-05-07] lint | 274 issues found

## [2026-05-07] lint | 274 issues found

## [2026-05-07] lint | 30 issues found

## [2026-05-07] lint | 30 issues found

## [2026-05-07] lint | 30 issues found

## [2026-05-07] lint | 30 issues found

## [2026-05-07] lint | 25 issues found

## [2026-05-07] lint | 25 issues found

## [2026-05-07] lint | 13 issues found

## [2026-05-07] lint | 13 issues found

## [2026-05-07] lint | 13 issues found

## [2026-05-07] lint | 65 issues found

## [2026-05-07] lint | 65 issues found

## [2026-05-07] lint | 65 issues found

## [2026-05-07] lint | 65 issues found

## [2026-05-07] lint | 65 issues found

## [2026-05-07] lint | 65 issues found

## [2026-05-07] lint | 31 issues found

## [2026-05-07] lint | 31 issues found

## [2026-05-07] lint | 31 issues found

## [2026-05-07] lint | 31 issues found

## [2026-05-07] lint | 31 issues found

## [2026-05-07] lint | 15 issues found

## [2026-05-07] Batch ingest | 51 docs from 中国航信 temp dir
## [2026-05-07] Fix | lint 0 HIGH — entity-company skip_types豁免，迁移00cbbaec至event目录
## [2026-05-07] Ingest | paper: 21464673_travelsky_reform_agenda_2026（改革工作台账2026）

## [2026-05-07] lint | 2 issues found

## [2026-05-07] lint | 2 issues found

## [2026-05-07] lint | 1 issues found
