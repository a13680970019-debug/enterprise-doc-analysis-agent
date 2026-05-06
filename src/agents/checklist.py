# -*- coding: utf-8 -*-

class ChecklistAgent:
    """
    复核清单 Agent。
    """

    def run(self, document_type: str, facts: dict, risks: dict, business: dict) -> dict:
        return {
            "checklist": [
                "资料类型是否判断正确？",
                "关键事实是否来自原文？",
                "是否区分事实、判断和推测？",
                "风险点是否需要专业人员复核？",
                "商业建议是否具备落地条件？",
                "是否存在无法确认但被写成确定结论的内容？"
            ],
            "must_verify": risks.get("unverified_items", [])
        }
