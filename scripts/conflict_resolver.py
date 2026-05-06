#!/usr/bin/env python3
"""
Conflict Classifier + Auto-Resolver for LLM Wiki.

Classifies conflicts and applies the correct resolution rule:
- time-series/policy/data → auto-update + notify Lei Ge
- historical fact → flag for human review
- analysis/judgment → keep both, no review needed

Usage:
    python conflict_resolver.py --old <claim_json> --new <claim_json>
    python conflict_resolver.py --classify-text <text>
"""

import argparse
import json
import re
import sys

# Claim types for resolution guidance
TYPE_POLICY = "policy"
TYPE_DATA = "data"
TYPE_FACT = "fact"
TYPE_ANALYSIS = "analysis"

# Confidence thresholds
HIGH_CONFIDENCE_THRESHOLD = 0.85

def classify_claim_type(text: str, entities: list = None, domains: list = None) -> str:
    """
    Classify a claim into one of four types for conflict resolution.

    Returns: 'policy' | 'data' | 'fact' | 'analysis'
    """
    text_lower = text.lower()

    # Policy/normative indicators (highest priority for auto-update)
    policy_patterns = [
        # Chinese
        r'规定', r'办法', r'指南', r'通知', r'意见', r'规划',
        r'关于印发', r'关于发布', r'制定', r'印发', r'发布',
        r'应当', r'必须', r'不得', r'鼓励', r'推进', r'落实',
        # English
        r'policy', r'guideline', r'regulation', r'requires', r'shall',
        r'mandates', r'issued by', r'published', r'forthcoming',
    ]
    for p in policy_patterns:
        if re.search(p, text):
            return TYPE_POLICY

    # Data/numeric indicators
    data_patterns = [
        r'\d+[\u4e00-\u9fa5]',
        r'\d+\.?\d*%',
        r'\d+\.\d+[亿万元]',
        r'增长|下降|增加|减少|同比|环比|营收|利润|规模|投资|占比',
        r'increased|decreased|revenue|profit|growth|decline|percent|%',
        r'yoy|qoq| QoQ| YoY',
    ]
    has_number = any(re.search(p, text) for p in data_patterns)
    temporal = any(kw in text for kw in ['年', '月', '日', '202', '203', '204', 'year', 'month', '季度'])
    if has_number and temporal:
        return TYPE_DATA

    # Analysis/judgment indicators
    analysis_patterns = [
        r'认为', r'分析', r'判断', r'预测', r'展望', r'建议',
        r'think', r'believe', r'analyze', r'predict', r'forecast',
        r'意义', r'价值', r'作用', r'影响', r'利弊', r'优势', r'劣势',
        r'将有助于', r'有望', r'预计', r'预期', r'看来',
    ]
    for p in analysis_patterns:
        if re.search(p, text):
            return TYPE_ANALYSIS

    # Default: fact (historical, cannot change)
    return TYPE_FACT

def classify_text(text: str) -> str:
    """Standalone text classification."""
    return classify_claim_type(text)

def resolve_conflict(old_claim: dict, new_claim: dict) -> dict:
    """
    Given two conflicting claims, classify and resolve.

    Returns:
    {
        "resolution": "auto_update" | "keep_both" | "flag_human",
        "type": "policy" | "data" | "fact" | "analysis",
        "action": str,  # Human-readable action description
        "auto_update": {  # if resolution == auto_update
            "winner": "new" | "old",
            "replace_with": new_claim or old_claim,
            "version_chain": ["old_claim_id", "new_claim_id"]
        },
        "reason": str
    }
    """
    old_type = old_claim.get("type", classify_claim_type(old_claim.get("text", "")))
    new_type = new_claim.get("type", classify_claim_type(new_claim.get("text", "")))

    # If types differ, use new claim's type for resolution
    # (new claim type may have been refined during ingestion)
    resolution_type = new_type if new_type else old_type

    if resolution_type in (TYPE_POLICY, TYPE_DATA):
        # Time-series / normative → auto-update with new
        winner = new_claim
        loser = old_claim

        return {
            "resolution": "auto_update",
            "type": resolution_type,
            "action": f"[AUTO] {resolution_type.upper()} conflict: newer overrides older. Update page, add old to versions[].",
            "auto_update": {
                "winner": "new",
                "replace_with": new_claim,
                "version_chain": [old_claim.get("id", "old"), new_claim.get("id", "new")],
                "old_claim": old_claim,
                "new_claim": new_claim
            },
            "notify_lei_ge": True,
            "reason": f"{resolution_type.upper()} conflicts are resolved by logical precedence (newer is more accurate)"
        }

    elif resolution_type == TYPE_FACT:
        # Historical fact → cannot override, flag human
        return {
            "resolution": "flag_human",
            "type": TYPE_FACT,
            "action": "[HUMAN REVIEW] Historical fact conflict. Both versions cannot coexist. Lei Ge must decide which is correct.",
            "auto_update": None,
            "notify_lei_ge": True,
            "reason": "Historical facts are immutable. Conflicting versions need human adjudication."
        }

    else:  # TYPE_ANALYSIS
        # Analysis / judgment → keep both, no conflict
        return {
            "resolution": "keep_both",
            "type": TYPE_ANALYSIS,
            "action": "[NO CONFLICT] Different analyses coexist. Note both perspectives in respective pages.",
            "auto_update": None,
            "notify_lei_ge": False,
            "reason": "Analysis and judgment are perspectives, not facts. Multiple viewpoints are valid and should coexist."
        }

def build_notification_message(resolution: dict, page_name: str) -> str:
    """Build a human-readable notification for Lei Ge."""
    lines = [
        f"🔔 Wiki Conflict Alert — {page_name}",
        "",
        f"**Type:** {resolution['type'].upper()}",
        f"**Resolution:** {resolution['resolution']}",
        f"**Reason:** {resolution['reason']}",
        "",
        f"**Action:** {resolution['action']}",
    ]

    if resolution.get("notify_lei_ge"):
        lines.append("")
        lines.append("⚠️ Please confirm or correct.")

    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description='LLM Wiki conflict classifier + auto-resolver')
    parser.add_argument('--classify-text', metavar='TEXT', help='Classify a single text')
    parser.add_argument('--old', help='Old claim JSON string')
    parser.add_argument('--new', help='New claim JSON string')
    parser.add_argument('--page-name', default='unknown', help='Page name for notifications')
    parser.add_argument('--notify', action='store_true', help='Print notification message for Lei Ge')
    args = parser.parse_args()

    if args.classify_text:
        result = classify_claim_type(args.classify_text)
        print(json.dumps({"text": args.classify_text, "type": result}, ensure_ascii=False, indent=2))
        return

    if args.old and args.new:
        try:
            old_claim = json.loads(args.old) if isinstance(args.old, str) else args.old
            new_claim = json.loads(args.new) if isinstance(args.new, str) else args.new
        except json.JSONDecodeError as e:
            print(json.dumps({"error": f"Invalid JSON: {e}"}))
            sys.exit(1)

        resolution = resolve_conflict(old_claim, new_claim)

        output = {
            "old_claim_id": old_claim.get("id"),
            "new_claim_id": new_claim.get("id"),
            "resolution": resolution
        }

        if args.notify:
            output["notification"] = build_notification_message(resolution, args.page_name)

        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    parser.print_help()

if __name__ == '__main__':
    main()
