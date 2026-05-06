# -*- coding: utf-8 -*-

from agents.document_classifier import DocumentClassifierAgent
from agents.fact_extraction import FactExtractionAgent
from agents.structure_summary import StructureSummaryAgent
from agents.risk_review import RiskReviewAgent
from agents.business_analysis import BusinessAnalysisAgent
from agents.action_plan import ActionPlanAgent
from agents.checklist import ChecklistAgent
from agents.report_writer import ReportWriterAgent


def route_analysis(document_type: str, text: str) -> str:
    """
    根据资料类型选择分析链路。
    当前版本是规则演示版，后续可替换为真实 LLM / RAG / 多 Agent 调度器。
    """

    classifier = DocumentClassifierAgent()
    fact_agent = FactExtractionAgent()
    summary_agent = StructureSummaryAgent()
    risk_agent = RiskReviewAgent()
    business_agent = BusinessAnalysisAgent()
    action_agent = ActionPlanAgent()
    checklist_agent = ChecklistAgent()
    report_agent = ReportWriterAgent()

    if document_type == "auto":
        document_type = classifier.run(text)

    facts = fact_agent.run(text)
    summary = summary_agent.run(document_type, facts)
    risks = risk_agent.run(document_type, text, facts)
    business = business_agent.run(document_type, text, facts)
    actions = action_agent.run(document_type, summary, risks, business)
    checklist = checklist_agent.run(document_type, facts, risks, business)

    report = report_agent.run(
        document_type=document_type,
        summary=summary,
        facts=facts,
        risks=risks,
        business=business,
        actions=actions,
        checklist=checklist,
    )

    return report
