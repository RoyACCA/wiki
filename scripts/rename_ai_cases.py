#!/usr/bin/env python3
"""Rename AI cases event pages from generic slugs to chapter-specific slugs."""

import os
import re
import uuid
import yaml
import json

WIKI = '/home/agentuser/wiki'
REDIRECTS_PATH = os.path.join(WIKI, 'wiki/_redirects.yaml')
INDEX_PATH = os.path.join(WIKI, 'wiki/index.md')

# old_sha -> (new_slug, new_title)
RENAME_MAP = {
    '11dc0740': ('ch01_smart_travel_assistant_agent',        '第1章 智能出行助手'),
    '6ef56a58': ('ch02_smart_ticket_search_nlp_rag',       '第2章 智能机票搜索'),
    'eadf77ca': ('ch03_passenger_self_service_agent',       '第3章 旅客自助服务智能体'),
    'd383e04e': ('ch04_airport_operations_ai_system',      '第4章 机场运行管理数智分析'),
    '33e4a24f': ('ch05_deepseek_smart_customer_service',    '第5章 DeepSeek智能客服'),
    '2ee3be64': ('ch06_dangerous_goods_ai_assistant',       '第6章 危险品智能服务助手'),
    '12369b1b': ('ch07_hangxin_honghu_ops_assistant',       '第7章 航信鸿鹄智能运维'),
    '4445f0a3': ('ch08_call_center_ai_quality_inspection', '第8章 呼叫中心AI质检'),
    'cad1a570': ('ch09_rag_qa_system_tod_software',         '第9章 RAG智能问答TOD'),
    'c6baa8f2': ('ch10_rd_knowledge_assistant_dongxiaosheng','第10章 懂小生研发知识问答'),
    '94aba6b2': ('ch11_boosting_url_risk_detection',        '第11章 风险URL检测'),
    '3b43e176': ('ch12_cloud_ops_ai_assistant',             '第12章 云化运维智能助手'),
    '7a724dae': ('ch13_ai_ops_knowledge_graph_kb',         '第13章 AI智能运维进阶'),
    'c4188918': ('ch14_moda_multi_source_ops_decision',      '第14章 摩达MODA运维决策'),
    'e506601d': ('ch15_multi_agent_report_generation',       '第15章 多智能体报表生成'),
    '0aa24b18': ('ch16_deep_learning_talent_assessment',     '第16章 深度学习人才盘点'),
    '61f9c2a4': ('ch17_aviation_ai_training_exam',           '第17章 民航智能培训考核'),
    'fa012de0': ('ch18_contract_efficiency_management',      '第18章 合同与效能管理'),
    '0e7bcaf1': ('ch19_smart_travel_ai_assistant',          '第19章 智能差旅AI助理'),
    'b449f2a0': ('ch20_canteen_management_system',           '第20章 餐饮管理系统'),
    '7bb049f4': ('ch21_aviation_business_data_pipeline',     '第21章 民航业务流程数据集'),
    '0e5ff6b0': ('ch22_aviation_knowledge_graph_kb',        '第22章 民航知识图谱'),
    'da827324': ('ch23_llmrag_enterprise_ai_assistant',      '第23章 LLMRAG企业运营AI助手'),
    '45338e80': ('ch24_general_mgmt_ai_assistant',          '第24章 综合管理智能助手'),
    '80cca634': ('ch25_xiaofei_multimodal_rag_assistant',   '第25章 航信小飞'),
    'd224b386': ('ch26_hetai_open_platform',                 '第26章 HETAI开放平台'),
    '717af075': ('ch27_jiaxing_green_ai_datacenter',        '第27章 嘉兴智算中心'),
}

# Build old_slug -> new_slug for each type
# Old pattern: {sha}_{generic_slug}
# Need to find the actual files
EVENT_DIR = os.path.join(WIKI, 'wiki/entities/event')

def find_old_file(sha):
    """Find the current file for a given SHA prefix."""
    for f in os.listdir(EVENT_DIR):
        if f.startswith(sha + '_'):
            return f
    return None

# Step 1: Load existing redirects
with open(REDIRECTS_PATH) as f:
    redirects = yaml.safe_load(f) or {}
if 'chunks' not in redirects:
    redirects['chunks'] = {}
if 'pages' not in redirects:
    redirects['pages'] = {}

# Step 2: Rename each file
for sha, (new_slug, new_title) in RENAME_MAP.items():
    old_fname = find_old_file(sha)
    if not old_fname:
        print(f'NOT FOUND: {sha}')
        continue
    
    old_slug = old_fname.replace('.md', '')
    new_fname = new_slug + '.md'
    old_path = os.path.join(EVENT_DIR, old_fname)
    new_path = os.path.join(EVENT_DIR, new_fname)
    
    # Read content
    with open(old_path) as f:
        content = f.read()
    
    # Update frontmatter: id, title, updated
    new_id = str(uuid.uuid4())[:8]
    content = re.sub(r'^id: .+$', f'id: {new_id}', content, flags=re.MULTILINE)
    content = re.sub(r'^title: .+$', f'title: "{new_title}"', content, flags=re.MULTILINE)
    content = re.sub(r'^updated: .+$', 'updated: 2026-05-07', content, flags=re.MULTILINE)
    
    # Write new file
    with open(new_path, 'w') as f:
        f.write(content)
    
    # Remove old file
    os.remove(old_path)
    
    # Add redirect
    redirects['pages'][old_slug] = new_slug
    
    print(f'Renamed: {old_fname} -> {new_fname}')

# Step 3: Save redirects
with open(REDIRECTS_PATH, 'w') as f:
    yaml.dump(redirects, f, allow_unicode=True, default_flow_style=False)

print(f'\nUpdated {REDIRECTS_PATH}')

# Step 4: Update index.md - replace old slugs with new slugs
with open(INDEX_PATH) as f:
    index_content = f.read()

for sha, (new_slug, new_title) in RENAME_MAP.items():
    old_pattern = f'[[{sha}_undatedtravelsky-llm-aviation-policy-ai]]'
    new_pattern = f'[[{new_slug}]]'
    if old_pattern in index_content:
        index_content = index_content.replace(old_pattern, new_pattern)
        print(f'Updated index: {old_pattern} -> {new_pattern}')
    else:
        # Try other variants
        for variant in [f'[[{sha}_undatedtravelsky-aviation-ai]]',
                        f'[[{sha}_undatedllm-aviation-policy-ai]]',
                        f'[[{sha}_undatedllm-aviation-ai-digital]]',
                        f'[[{sha}_undatedtravelsky-llm-aviation-ai-tech-innovation]]',
                        f'[[{sha}_undatedtravelsky-aviation-policy-ai]]',
                        f'[[{sha}_undatedtravelsky-aviation-ai-tech-innovation]]',
                        f'[[{sha}_undatedtravelsky-llm-aviation-policy-ai]]',
                        f'[[{sha}_undatedsasac-aviation-policy-ai]]',
                        f'[[{sha}_undatedaviation-tech-innovation]]',
                        f'[[{sha}_undatedai-aviation-policy]]',
                        f'[[{sha}_2023travelsky-aviation-ai]]',
                        f'[[{sha}_2024travelsky-aviation-ai-digital]]',
                        f'[[{sha}_2025travelsky-sasac-ai-aviation-policy]]']:
            if variant in index_content:
                index_content = index_content.replace(variant, f'[[{new_slug}]]')
                print(f'Updated index [{variant}]: -> {new_pattern}')
                break

with open(INDEX_PATH, 'w') as f:
    f.write(index_content)

print('\nDone. Run lint to verify.')
