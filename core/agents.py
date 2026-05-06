from crewai import Agent
from tools.web_search import WebSearchTool
from tools.vector_db import ProductKnowledgeBaseTool

class B2BSalesAgents:
    def __init__(self, llm_instance):
        self.llm = llm_instance

    def researcher_agent(self) -> Agent:
        return Agent(
            role='资深商业情报调查员',
            goal='全面搜集目标公司的全量上下文信息，包括近期财报、新闻、高管发言和行业动态。',
            backstory='你是一个在B2B领域拥有10年经验的情报专家，擅长从海量互联网信息中提取有价值的商业信号。',
            verbose=True,
            allow_delegation=False,
            tools=[WebSearchTool()],
            llm=self.llm
        )

    def strategist_agent(self) -> Agent:
        return Agent(
            role='首席商业战略分析师',
            goal='基于搜集到的情报进行长链推理，精准洞察目标公司的核心业务目标与潜在痛点。',
            backstory='你具备极强的逻辑推理能力，能从杂乱无章的非结构化数据中推演出企业的真实痛点和战略缺口。',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def matcher_agent(self) -> Agent:
        return Agent(
            role='产品解决方案架构师',
            goal='将客户痛点与我方产品知识库进行交叉比对，推理并组合出最佳的定制化产品方案。',
            backstory='你对我方产品了如指掌，能够将复杂的技术功能转化为解决客户业务痛点的商业价值。',
            verbose=True,
            allow_delegation=False,
            tools=[ProductKnowledgeBaseTool()],
            llm=self.llm
        )

    def copywriter_agent(self) -> Agent:
        return Agent(
            role='B2B 顶尖营销文案专家',
            goal='基于匹配出的解决方案，生成高度定制化的触达邮件（Cold Email）与商业计划书（Pitch Deck）大纲。',
            backstory='你的文字极具说服力，懂得以客户为中心（Customer-Centric）的沟通技巧，转化率极高。',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
