# -*- coding: utf-8 -*-

class BusinessAnalysisAgent:
    """
    商业价值判断 Agent。
    """

    def run(self, document_type: str, text: str, facts: dict) -> dict:
        if document_type == "policy":
            opportunities = [
                "判断企业是否符合政策支持方向。",
                "识别补贴、试点、资质、项目申报机会。",
                "转化为内部申报计划。"
            ]
        elif document_type == "contract":
            opportunities = [
                "明确合作边界。",
                "优化谈判条件。",
                "提前识别履约风险。"
            ]
        elif document_type == "competitor":
            opportunities = [
                "识别竞品业务边界。",
                "发现市场缺口。",
                "反推我方产品和销售策略。"
            ]
        elif document_type == "project":
            opportunities = [
                "判断项目是否值得投入。",
                "明确资源与收益关系。",
                "形成推进计划。"
            ]
        else:
            opportunities = [
                "将资料转化为结构化信息。",
                "辅助团队决策。"
            ]

        return {
            "business_value": opportunities,
            "commercial_judgement": "当前为初步商业判断，正式结论需结合更多业务数据。"
        }
