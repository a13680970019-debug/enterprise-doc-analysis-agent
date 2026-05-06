# -*- coding: utf-8 -*-

class StructureSummaryAgent:
    """
    结构化摘要 Agent。
    """

    def run(self, document_type: str, facts: dict) -> dict:
        key_lines = facts.get("key_lines", [])

        return {
            "document_type": document_type,
            "summary": "基于提取事实生成结构化摘要。",
            "key_points": key_lines[:10],
            "structure": self._structure_by_type(document_type),
        }

    def _structure_by_type(self, document_type: str) -> list:
        mapping = {
            "policy": ["政策目标", "适用对象", "申报条件", "机会窗口", "落地建议"],
            "contract": ["合同主体", "权利义务", "付款条款", "交付条款", "违约责任"],
            "competitor": ["业务范围", "商业模式", "客户类型", "产品能力", "市场缺口"],
            "project": ["项目目标", "资源需求", "执行路径", "风险阻塞", "下一步行动"],
            "training": ["培训对象", "知识点", "学习路径", "实操步骤", "考核标准"],
        }
        return mapping.get(document_type, ["背景", "要点", "风险", "建议"])
