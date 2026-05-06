# core/tasks.py
from textwrap import dedent
from crewai import Task

class B2BSalesTasks:
    def gather_company_info(self, agent, company_name: str) -> Task:
        return Task(
            description=dedent(f"""\
                请全面搜集关于【{company_name}】的最新商业情报。
                你需要关注以下几个维度：
                1. 公司近半年的重大新闻、财报披露或高管发言。
                2. 公司的核心业务模式及所处行业的竞争格局。
                3. 近期是否有裁员、并购、技术转型等重大战略动作。
                
                务必确保信息的准确性和时效性，过滤掉无价值的公关软文。
                """),
            expected_output=f"一份关于{company_name}的结构化深度背景调查报告，包含近期重大事件、财务健康状况和业务扩张方向。",
            agent=agent
        )

    def analyze_pain_points(self, agent, context_tasks: list) -> Task:
        return Task(
            description=dedent("""\
                基于搜集到的目标公司背景信息，进行深度的逻辑和商业推理。
                你需要：
                1. 提炼出该公司当前最可能面临的 1-3 个核心业务痛点（如：获客成本高、系统老旧、合规风险等）。
                2. 分析他们近期的战略目标（如：出海、降本增效、数字化转型）。
                3. 解释为什么这些痛点会阻碍他们实现战略目标。
                """),
            expected_output="一份包含详细逻辑推理的痛点分析报告，明确指出客户痛点、战略目标以及两者之间的因果联系。",
            context=context_tasks,
            agent=agent
        )

    def match_solutions(self, agent, context_tasks: list) -> Task:
        return Task(
            description=dedent("""\
                作为方案架构师，请提取上一步分析出的客户痛点，并使用知识库工具检索我方的产品线。
                你需要：
                1. 为每一个痛点匹配最合适的我方产品或功能模块。
                2. 阐述该产品是如何解决客户痛点的（价值主张）。
                3. 给出初步的报价区间或合作模式建议（SaaS订阅/私有化部署）。
                """),
            expected_output="一份精准的【痛点-产品】映射矩阵，以及整体的商业解决方案概述。",
            context=context_tasks,
            agent=agent
        )

    def generate_outreach_materials(self, agent, context_tasks: list) -> Task:
        return Task(
            description=dedent("""\
                基于匹配好的产品解决方案，撰写高转化率的触达物料。
                你需要输出两部分内容：
                1. 一封 Cold Email（冷触达邮件）：标题要具有吸引力，正文需包含客户痛点共鸣、我方价值主张以及明确的 Call to Action (CTA)。
                2. 一份 Pitch Deck（商业计划书）大纲：规划出在与客户开会时，前 5 页 PPT 应该讲什么，重点突出哪些数据。
                """),
            expected_output="一封随时可以发送的高转化率 Cold Email 文本，以及一份结构清晰的 Pitch Deck 演示大纲。",
            context=context_tasks,
            agent=agent
        )
