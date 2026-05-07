#!/usr/bin/env python3
"""Split AI cases PDF into chapter-level .txt files for batch ingest."""

import sys
import os
import fitz
import re

PDF_PATH = '/home/agentuser/temp/中国航信人工智能应用案例汇编.pdf'
OUTPUT_DIR = '/home/agentuser/temp'

# Chapter start pages (0-indexed content page number → PDF page index = content_page + 5)
CHAPTERS = [
    (1,  "基于大模型与Agent驱动的智能出行助手",              5),
    (2,  "基于自然语言处理NLP和检索增强RAG技术的智能机票搜索应用", 13),
    (3,  "基于大模型的智能体在旅客自助服务场景中的创新应用",      18),
    (4,  "基于大模型的机场运行管理数智分析系统",               23),
    (5,  "基于DeepSeek引擎的智能客服系统",                    28),
    (6,  "基于区块链与人工智能技术的民航危险品智能服务助手",      33),
    (7,  "基于RAG+AIAgent框架的航信鸿鹄智能运维助手",          39),
    (8,  "基于AI大模型的呼叫中心服务质量管理智能质检系统",       46),
    (9,  "基于RAG技术的智能问答系统以TOD软件为例",             53),
    (10, "重研研发知识问答助手懂小生",                         64),
    (11, "基于Boosting集成学习的风险URL检测模型",             76),
    (12, "云化应用运维智能小助手",                            84),
    (13, "AI赋能下的智能运维进阶基于知识图谱与社区驱动运维效能跃迁", 90),
    (14, "摩达MODA基于多源数据融合的运维分析决策智能体",      100),
    (15, "基于多智能体机制的报表生成与分析应用",               108),
    (16, "深度学习在人才盘点的应用研究",                      120),
    (17, "基于大模型的民航智能培训考核系统",                   139),
    (18, "合同与效能管理平台",                                150),
    (19, "智能差旅AI助理",                                   154),
    (20, "中国航信高科技产业园餐饮管理系统",                  168),
    (21, "基于接口服务维度的民航业务流程数据集",              174),
    (22, "民航领域知识图谱赋能知识库的创新应用",              181),
    (23, "基于LLMRAG技术的企业运营AI服务助手",               187),
    (24, "基于大模型的综合管理智能助手",                      199),
    (25, "多模态知识检索与生成RAG智能助手航信小飞",          205),
    (26, "HETAI开放平台",                                    213),
    (27, "中国航信嘉兴智算中心绿色低碳实践",                  219),
]

def slugify(text):
    """Simple ASCII slug from Chinese title."""
    # Remove special chars, keep Chinese + ASCII + digits
    text = re.sub(r'[^\u4e00-\u9fff\w]', ' ', text)
    text = re.sub(r'\s+', '_', text.strip())
    return text.lower()

doc = fitz.open(PDF_PATH)
total_pages = len(doc)

for idx, (ch_num, ch_title, start_content_page) in enumerate(CHAPTERS):
    # PDF page index
    pdf_start = start_content_page  # 0-indexed
    # End page = next chapter start - 1, or end of doc
    if idx + 1 < len(CHAPTERS):
        next_start = CHAPTERS[idx + 1][2]
        pdf_end = next_start - 1
    else:
        pdf_end = total_pages - 1

    # Extract text from this chapter
    chapter_text_parts = []
    for page_idx in range(pdf_start, pdf_end + 1):
        if page_idx < total_pages:
            text = doc[page_idx].get_text()
            # Remove page number footers like '— XX —'
            lines = []
            for line in text.split('\n'):
                line = line.strip()
                if re.match(r'^—\s*\d+\s*—\s*$', line):
                    continue
                lines.append(line)
            chapter_text_parts.append('\n'.join(lines))

    chapter_text = '\n\n'.join(chapter_text_parts)

    # Generate slug
    short_title = slugify(ch_title)[:40]
    filename = f"cf5d5705_ch{ch_num:02d}_{short_title}.txt"
    out_path = os.path.join(OUTPUT_DIR, filename)

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"【第{ch_num}章】{ch_title}\n\n")
        f.write(chapter_text)

    print(f"Chapter {ch_num:02d}: {filename} (pages {pdf_start+1}-{pdf_end+1}, {len(chapter_text)} chars)")

doc.close()
print(f"\nDone: {len(CHAPTERS)} chapter files written to {OUTPUT_DIR}")
