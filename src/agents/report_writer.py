# -*- coding: utf-8 -*-

import json


class ReportWriterAgent:
    """
    报告生成 Agent。
    """

    def run(
        self,
        document_type: str,
        summary: dict,
        facts: dict,
        risks: dict,
        business: dict,
        actions: dict,
        checklist: dict,
    ) -> str:
        return f"""# 企业资料分析报告

## 1. 文档类型

{document_type}

## 2. 结构化摘要

{self._format_json(summary)}

## 3. 关键事实

{self._format_json(facts)}

## 4. 风险点识别

{self._format_json(risks)}

## 5. 商业价值判断

{self._format_json(business)}

## 6. 执行方案

{self._format_json(actions)}

## 7. 复核清单

{self._format_json(checklist)}

## 8. 审计说明

当前版本为基础演示版。正式用于企业决策时，应接入真实文档解析、依据定位、权限控制、日志审计和人工复核流程。
"""

    def _format_json(self, data: dict) -> str:
        return "```json\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n```"
