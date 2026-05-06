# -*- coding: utf-8 -*-

class DocumentClassifierAgent:
    """
    文档识别 Agent。
    负责判断资料类型。
    """

    def run(self, text: str) -> str:
        if any(k in text for k in ["政策", "申报", "补贴", "主管部门", "通知"]):
            return "policy"
        if any(k in text for k in ["甲方", "乙方", "违约", "合同", "付款"]):
            return "contract"
        if any(k in text for k in ["竞品", "客户类型", "商业模式", "市场定位"]):
            return "competitor"
        if any(k in text for k in ["项目目标", "里程碑", "预算", "交付"]):
            return "project"
        if any(k in text for k in ["培训", "课程", "学习", "考核"]):
            return "training"
        return "general"
