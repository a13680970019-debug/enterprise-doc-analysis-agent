# -*- coding: utf-8 -*-

class FactExtractionAgent:
    """
    事实提取 Agent。
    当前版本采用简单规则，后续可替换为 LLM。
    """

    def run(self, text: str) -> dict:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        key_lines = []

        keywords = [
            "政策", "申报", "条件", "对象", "时间", "金额",
            "甲方", "乙方", "付款", "交付", "违约",
            "客户", "市场", "商业模式", "竞品",
            "项目", "预算", "风险", "培训"
        ]

        for line in lines:
            if any(k in line for k in keywords):
                key_lines.append(line)

        return {
            "source_length": len(text),
            "key_lines": key_lines[:30],
            "note": "当前为规则提取版，正式版本应标注文档页码、段落或原文位置。"
        }
