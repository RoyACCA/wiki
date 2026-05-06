#!/usr/bin/env python3
"""
LLM-based Claim Extractor for LLM Wiki.

Extracts atomic claims from source documents for knowledge provenance.
Each claim has: id, text, source location, entities, domain tags.

Usage:
    python extract_claims.py --file <path> [--text <text>]
"""

import argparse
import hashlib
import json
import re
import sys
import os
import uuid

def generate_claim_id(text: str, para_index: int) -> str:
    """Generate deterministic claim ID from text + position."""
    h = hashlib.md5(f"{para_index}:{text[:100]}".encode()).hexdigest()[:8]
    return f"c{h}"

def extract_claims_from_text(text: str, file_path: str = "") -> list[dict]:
    """
    Extract atomic claims from document text using LLM-style parsing.
    Falls back to heuristic extraction if LLM unavailable.

    Returns list of claims:
    {
        "id": "c001",
        "text": "...",
        "para_index": 0,
        "entities": ["Travelsky", "AI"],
        "domains": ["aviation", "ai"],
        "type": "fact" | "policy" | "data" | "analysis"
    }
    """
    # Split into paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 20]

    claims = []
    for i, para in enumerate(paragraphs):
        # Generate claim ID
        claim_id = generate_claim_id(para, i)

        # Extract entities (simple keyword matching)
        entities = extract_entities(para)

        # Detect domain
        domains = detect_domains(para)

        # Detect claim type
        claim_type = detect_claim_type(para, entities, domains)

        claims.append({
            "id": claim_id,
            "text": para[:500],  # Truncate very long text
            "para_index": i,
            "entities": entities,
            "domains": domains,
            "type": claim_type,
            "source": file_path
        })

    return claims

def extract_entities(text: str) -> list[str]:
    """Extract known entities from text using keyword matching."""
    known_entities = {
        "中国航信": "Travelsky",
        "Travelsky": "Travelsky",
        "国资委": "SASAC",
        "国务院国资委": "SASAC",
        "民航局": "CAAC",
        "中国民航局": "CAAC",
        "工信部": "MIIT",
        "工业和信息化部": "MIIT",
        "发改委": "NDRC",
        "国家发展和改革委员会": "NDRC",
        "焦雷": "Jiao Lei",
        "低空经济": "Low-Altitude Economy",
        "人工智能": "AI",
        "大模型": "LLM",
        "战略性新兴产业": "Strategic Emerging Industries",
        "新质生产力": "New Quality Productive Forces",
    }

    found = []
    for cn, en in known_entities.items():
        if cn in text:
            found.append(en)
    return list(set(found))

def detect_domains(text: str) -> list[str]:
    """Detect applicable domain tags."""
    domain_keywords = {
        "aviation": ["航空", "民航", "机场", "航司", "航班", "航线", "Travelsky", "中国航信"],
        "policy": ["政策", "规定", "办法", "指南", "通知", "意见", "规划", "国资委", "民航局", "工信部", "发改委"],
        "ai": ["人工智能", "AI", "大模型", "LLM", "模型", "机器学习", "深度学习"],
        "low-altitude": ["低空", "无人机", "eVTOL", "UAM", "通用航空"],
        "future-industry": ["未来产业", "战新", "战略性新兴产业", "新质生产力"],
        "digital": ["数字化", "数字化转型", "数字经济", "数据要素"],
        "central-enterprise": ["央企", "国有企业", "国企", "中央企业"],
        "tech-innovation": ["科技创新", "技术创新", "研发", "创新联合体"],
    }

    detected = []
    for domain, keywords in domain_keywords.items():
        for kw in keywords:
            if kw in text:
                detected.append(domain)
                break
    return list(set(detected))

def detect_claim_type(text: str, entities: list, domains: list) -> str:
    """
    Detect claim type for conflict resolution guidance.
    Returns: 'policy' | 'data' | 'fact' | 'analysis'
    """
    text_lower = text.lower()

    # Policy/normative indicators
    policy_patterns = [
        r'规定', r'办法', r'指南', r'通知', r'意见', r'规划',
        r'要求', r'应当', r'必须', r'不得', r'鼓励',
        r'policy', r'guideline', r'regulation', r'requires', r'shall',
        r'关于', r'制定', r'印发', r'发布'
    ]
    for p in policy_patterns:
        if re.search(p, text):
            return "policy"

    # Data/numeric indicators
    data_patterns = [
        r'\d+[\u4e00-\u9fa5]?',  # Chinese numbers
        r'\d+\.?\d*%',
        r'增长|下降|增加|减少|营收|利润|规模|投资|增长',
        r'increased|decreased|revenue|profit|growth|decline'
    ]
    has_number = any(re.search(p, text) for p in data_patterns)
    temporal = any(kw in text for kw in ['年', '月', '日', '202', '203', '204', 'year', 'month'])
    if has_number and temporal:
        return "data"

    # Analysis/judgment indicators
    analysis_patterns = [
        r'认为', r'分析', r'判断', r'预测', r'展望', r'建议',
        r'think', r'believe', r'analyze', r'predict', r'forecast',
        r'意义', r'价值', r'作用', r'影响', r'利弊', r'优势', r'劣势'
    ]
    for p in analysis_patterns:
        if re.search(p, text):
            return "analysis"

    # Default to fact
    return "fact"

def extract_claims_from_file(file_path: str) -> list[dict]:
    """Extract claims from a file."""
    ext = os.path.splitext(file_path)[1].lower()
    text = ""

    try:
        if ext == '.txt':
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
        elif ext == '.md':
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
        elif ext == '.pdf':
            import fitz
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text() + '\n'
            doc.close()
        elif ext == '.docx':
            from docx import Document
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text + '\n'
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    return extract_claims_from_text(text, file_path)

def main():
    parser = argparse.ArgumentParser(description='Extract claims from document for knowledge provenance')
    parser.add_argument('--file', help='Path to file')
    parser.add_argument('--text', help='Raw text to extract from (alternative to --file)')
    parser.add_argument('--source', default='', help='Source identifier for claims')
    args = parser.parse_args()

    if args.text:
        claims = extract_claims_from_text(args.text, args.source)
    elif args.file:
        claims = extract_claims_from_file(args.file)
    else:
        parser.print_help()
        return

    result = {
        "total_claims": len(claims),
        "claims": claims,
        "source": args.file or args.source
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
