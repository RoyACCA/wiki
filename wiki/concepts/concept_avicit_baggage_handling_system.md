---
id: concept-avicit-baggage-handling-system
created: 2026-05-06
updated: 2026-05-06
title: "机场行李智能搬运系统"
type: concept
domain: [ai, aviation, tech-innovation]
tags: [concept, ai, aviation, tech-innovation]
confidence: 0.99
summary: "机场行李智能搬运系统由移动科技（中航信移动科技有限公司）自主研发，集成千穰大模型与边云协同技术，实现机器人系统与视觉识别系统协同，2025年6月入选北京市2025年第一批首台（套）重大技术装备目录（机器人及智能制造装备-机器人-工业机器人），技术水平达国内领先。"
conflicts: []
versions: []
claims: [
  {
    "id": "c001",
    "text": "机场行李智能搬运系统入选北京市2025年第一批首台（套）重大技术装备目录",
    "para_index": 0,
    "entities": ["AVICIT"],
    "domains": ["ai", "policy"],
    "type": "fact"
  },
  {
    "id": "c002",
    "text": "具体领域：机器人及智能制造装备-机器人-工业机器人",
    "para_index": 0,
    "entities": [],
    "domains": ["tech-innovation"],
    "type": "fact"
  },
  {
    "id": "c003",
    "text": "技术水平达国内领先",
    "para_index": 1,
    "entities": [],
    "domains": ["tech-innovation"],
    "type": "fact"
  },
  {
    "id": "c004",
    "text": "核心技术：千穰大模型+边云协同技术；底层集成多种传感器与控制器，模块化设计",
    "para_index": 1,
    "entities": ["QianRang"],
    "domains": ["ai"],
    "type": "fact"
  },
  {
    "id": "c005",
    "text": "视觉识别系统借助大模型图像识别能力精准定位行李位置与姿态",
    "para_index": 2,
    "entities": ["QianRang"],
    "domains": ["ai"],
    "type": "fact"
  },
  {
    "id": "c006",
    "text": "机器人系统覆盖多种分拣终端，完成行李抓取、搬运和码放，支持异形、软包等特殊行李处理",
    "para_index": 2,
    "entities": [],
    "domains": ["aviation"],
    "type": "fact"
  },
  {
    "id": "c007",
    "text": "边云协同：边缘计算实时控制机械臂，云端大模型根据航班动态调整工作策略",
    "para_index": 2,
    "entities": ["QianRang"],
    "domains": ["ai"],
    "type": "fact"
  },
  {
    "id": "c008",
    "text": "移动科技自研，可对接现有机场管理系统，打通机场行李处理无人化最后一公里",
    "para_index": 3,
    "entities": ["AVICIT"],
    "domains": ["aviation"],
    "type": "fact"
  }
]
---

# Concept: 机场行李智能搬运系统（AVICIT Baggage Handling System）

## Summary

机场行李智能搬运系统由移动科技（中航信移动科技有限公司）自主研发，集成千穰大模型与边云协同技术，实现机器人系统与视觉识别系统协同，2025年6月入选北京市2025年第一批首台（套）重大技术装备目录（机器人及智能制造装备-机器人-工业机器人），技术水平达国内领先。

## Details

### 基本信息

| 项目 | 内容 |
|---|---|
| 产品名称 | 机场行李智能搬运系统 |
| 研发单位 | 中航信移动科技有限公司（移动科技） |
| 入选目录 | 北京市2025年第一批首台（套）重大技术装备目录 |
| 入选领域 | 机器人及智能制造装备-机器人-工业机器人 |
| 发布时间 | 2025年6月9日（公告） |
| 技术水平 | 国内领先 |
| 来源 | 移动科技，作者：张淑君，浏览量：681 |

### 核心架构

**系统构成：**
1. **机器人系统**：覆盖多种分拣终端，完成行李抓取、搬运和码放，支持异形、软包等特殊行李处理及托盘自动撤取
2. **视觉识别系统**：借助大模型图像识别能力，精准定位行李位置与姿态

**核心技术：**
- **千穰大模型**：基于深度学习算法，挖掘航班时段、行李类型等历史数据，学习最优处理策略
- **边云协同**：边缘计算节点实时分析行李位置、重量等信息并快速做出基础判断；云端大模型进行全局调度与策略优化

### 与其他行李机器人的区别

| | 机场行李智能搬运系统 | 机场行李全向叉取智能机器人 |
|---|---|---|
| 研发单位 | 移动科技 | 资本运营与创新业务部 |
| 核心技术 | 千穰大模型+边云协同 | 6DOF机械臂+2D/3D视觉+RFID |
| 技术架构 | 视觉识别+机器人搬运 | 叉取式末端执行器+码垛算法 |
| 定位 | 首台（套）重大技术装备 | 全球首个民航行李转运全向叉取机器人 |
| 归口（2026） | 移动科技（子公司，架构不变） | 机场数智业务部 |

> **部门归属说明**：机场行李智能搬运系统由**中航信移动科技有限公司**（子公司）研发，架构独立于航信股份公司内部部门调整。

## Related

- [[concept_avicit_baggage_handling_system]]
- [[concept_qianrang_large_model]] — 千穰大模型（核心技术）
- [[concept_baggage_robot]] — 机场行李全向叉取智能机器人（另一款行李机器人，研发单位不同）
- [[concept_ai]] — 人工智能
- [[concept_ai-civil-aviation-scenarios]] — AI民航应用场景
- [[company_travelsky]] — 中国航信（母公司）
- [[entity_caac]] — 中国民用航空局

## Source

- 原始文档: `raw/docs/f113b2a8_avicit_baggage_handling_system.txt`
