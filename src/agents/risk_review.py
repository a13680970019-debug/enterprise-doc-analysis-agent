# -*- coding: utf-8 -*-

class RiskReviewAgent:
    """
    风险审查 Agent。
    """

    def run(self, document_type: str, text: str, facts: dict) -> dict:
        risks = []

        if document_type == "contract":
            risks.extend([
                "需核验付款条件是否明确。",
                "需核验违约责任是否对等。",
                "需核验交付标准是否可验收。"
            ])
        elif document_type == "policy":
            risks.extend([
                "需核验政策是否仍在有效期内。",
                "需核验企业是否符合申报主体条件。",
                "需核验申报窗口和材料要求。"
            ])
        elif document_type == "competitor":
            risks.extend([
                "竞品资料可能不完整，需核验其真实客户与收费模式。",
                "市场缺口判断需要更多样本支持。"
            ])
        elif document_type == "project":
            risks.extend([
                "需核验预算是否覆盖资源投入。",
                "需核验关键里程碑是否有负责人。"
            ])
        else:
            risks.append("当前资料类型不明确，结论需要人工复核。")

        return {
            "risk_level": "medium",
            "risks": risks,
            "unverified_items": [
                "原文未明确的信息不能作为确定结论。",
                "涉及法律、财务、政策申报的内容需人工复核。"
            ]
        }
