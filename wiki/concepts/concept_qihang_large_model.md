---
id: concept-qihang-large-model
created: 2026-05-07
updated: 2026-05-07
title: "启航大模型"
type: concept
domain: [ai, aviation, tech-innovation]
tags: [concept, ai, aviation, tech-innovation]
confidence: 0.99
summary: "启航（Qihang）是中航信（Travelsky）团队打造的民航行业大模型，参数规模30B-80B，2025年7月18日发布于AI环信平台。具备生成式人工智能服务备案和深度合成算法备案"双备案"，适配国产算力生态，支撑智能客服到运行决策等民航场景。"
conflicts: []
versions: []
claims: [
  {
    "id": "qihang001",
    "text": "启航大模型（Qihang）由中航信团队打造，参数规模30B-80B，2025年7月18日发布于AI环信平台。",
    "para_index": 0,
    "entities": ["Travelsky"],
    "domains": ["ai", "aviation"],
    "type": "fact"
  },
  {
    "id": "qihang002",
    "text": "通过国家网信办与国资委"生成式人工智能服务备案"和"深度合成算法备案"双备案，适配国产算力生态。",
    "para_index": 0,
    "entities": ["Travelsky"],
    "domains": ["ai", "policy"],
    "type": "fact"
  },
  {
    "id": "qihang003",
    "text": "技术特点：数据侧采用高斯布局感知的文档智能理解方法；训练侧采用纯解码结构与多专家算法（MoE）+ 流水线并行技术。",
    "para_index": 1,
    "entities": [],
    "domains": ["ai"],
    "type": "fact"
  },
  {
    "id": "qihang004",
    "text": "五大核心优势：民航垂直领域专家；中国民航旅客服务系统深度对接；全场景民航支撑（智能客服/运行决策/业务合规/企业管理）；安全合规央企基因（双备案+全链路数据脱敏）；开放生态赋能。",
    "para_index": 1,
    "entities": [],
    "domains": ["ai", "aviation"],
    "type": "fact"
  },
  {
    "id": "qihang005",
    "text": "访问量132次，语言支持中文和英文，分类归属自然语言理解→文本生成，申请制使用。",
    "para_index": 0,
    "entities": [],
    "domains": ["ai"],
    "type": "data"
  }
]
---

## Summary

启航（Qihang）是[[company_travelsky]]团队面向民航领域打造的行业大模型，参数规模**30B-80B**，2025年7月18日发布于AI环信平台（aihuanxin.cn）。深度融合通用AI能力和民航专业知识，具备多场景泛化能力。

通过国家网信办与国资委**"生成式人工智能服务备案"和"深度合成算法备案"双备案**，适配国产算力生态，支撑从智能客服到运行决策的多场景服务。

## Details

### 基本信息

| 字段 | 值 |
|---|---|
| 全称 | 启航大模型（Qihang） |
| 研发单位 | [[company_travelsky]] |
| 参数规模 | 30B-80B |
| 发布时间 | 2025-07-18 |
| 更新时间 | 2025-07-18 |
| 发布时间 | 2025-07-18 |
| 所属平台 | AI环信（aihuanxin.cn） |
| 模型ID | 1415 |
| 分类 | 自然语言理解 → 文本生成（text_generation） |
| 许可证 | Other |
| 使用方式 | 申请制 |
| 访问量 | 132次 |
| 语言 | 中文、英文 |

### 备案信息

- **生成式人工智能服务备案**：国家网信办与国资委认证
- **深度合成算法备案**：国家网信办与国资委认证
- 双备案，安全合规体系完善

### 技术特点

**数据侧：**
- 基于高斯布局感知的文档智能理解方法，增强对民航专业文档的语义解析能力

**训练侧：**
- 纯解码结构与多专家算法（MoE），显著提升推理效率
- 流水线并行技术，降低资源消耗，加速训练进程

### 行业特点

1. **民航知识专精**：海量民航专业数据专项训练，强化民航业务理解深度与知识准确性
2. **业务系统对接**：通过智能体协同，对接[[company_travelsky]]核心业务系统，整合航司、机场、代理人数据
3. **民航场景支撑**：有效支撑服务端、运行端、管理端等民航场景

### 五大核心优势

| 优势 | 说明 |
|---|---|
| 民航垂直领域专家 | 海量民航数据专项训练，精准掌握行业术语、规范及业务流程 |
| 旅客服务系统深度对接 | 支持对接中国民航旅客服务系统接口 |
| 全场景民航支撑 | 覆盖智能客服、运行决策、业务合规、企业管理等 |
| 安全合规央企基因 | 双备案 + 全链路数据脱敏与加密传输 |
| 开放生态赋能 | 依托民航智能服务平台，向合作伙伴开放模型能力 |

### 使用协议

面向民航生态合作伙伴开放：
- **云端API接入**：支持快速集成智能客服、数据分析等场景
- **本地化部署**：满足高安全性场景需求

### 与[[concept_qianrang_large_model]]的关系

- [[concept_qianrang_large_model]]（千穰）：2023年8月发布，参数规模>1000亿，移动科技研发，**仅有生成式AI单备案**（非双备案）
- **启航**：2025年7月发布，参数规模30B-80B，中航信团队研发，**双备案**
- 两者同属中航信AI产品线，但定位不同（千穰侧重超大规模，启航侧重场景落地）

## Related

- [[concept_qianrang_large_model]]
- [[concept_qianrang_high_quality_civil_aviation_dataset]]
- [[355fdcab_2025travelsky-sasac-caac-aviation-policy-ai]]
