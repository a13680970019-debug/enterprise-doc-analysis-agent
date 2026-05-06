#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Enterprise Document Analysis & Decision Support Agent

基础命令行演示版。

运行示例：

python src/main.py --type policy --input examples/policy_example.txt
python src/main.py --type contract --input examples/contract_example.txt
python src/main.py --type competitor --input examples/competitor_example.txt
"""

import argparse
from pathlib import Path

from chains.router import route_analysis


def read_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"文件不存在: {path}")
    return p.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="企业资料分析与决策支持 Agent")
    parser.add_argument("--type", required=True, help="资料类型：policy / contract / competitor / project / training / auto")
    parser.add_argument("--input", required=True, help="输入文本文件路径")
    args = parser.parse_args()

    text = read_text(args.input)
    result = route_analysis(document_type=args.type, text=text)

    print(result)


if __name__ == "__main__":
    main()
