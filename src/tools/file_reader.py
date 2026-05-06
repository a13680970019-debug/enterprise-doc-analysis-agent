# -*- coding: utf-8 -*-

from pathlib import Path


def read_text_file(path: str) -> str:
    """
    基础文本读取工具。
    后续可扩展为 PDF、Word、Excel 读取。
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    return p.read_text(encoding="utf-8")
