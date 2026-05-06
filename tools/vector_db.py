# tools/vector_db.py
import yaml
import os
from langchain.tools import tool

@tool("我方产品向量知识库")
def ProductKnowledgeBaseTool(query: str) -> str:
    """根据客户痛点关键词，检索我方（乙方）的产品库，寻找匹配的解决方案。"""
    # 模拟 RAG (检索增强生成) 过程，实际会使用 Chroma/Pinecone + OpenAI Embeddings
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'company_products.yaml')
    
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            products = yaml.safe_load(file)
            
        # 模拟基于关键词的简单检索逻辑
        matched_products = []
        for product in products.get('products', []):
            if any(keyword in query.lower() for keyword in product.get('keywords', [])):
                matched_products.append(product)
                
        if not matched_products:
            return "知识库中未找到完全匹配的产品，请推荐通用的数字化咨询服务。"
            
        response = "找到以下匹配产品：\n"
        for p in matched_products:
            response += f"- 产品名：{p['name']}\n  功能：{p['description']}\n  报价：{p['pricing']}\n"
        return response
        
    except FileNotFoundError:
        return "知识库配置文件未找到，请检查 config 目录。"
