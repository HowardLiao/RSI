#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
完全同步建置工具：
1. 產生 RSI_DUKE_UML2_ALL_DIAGRAMS.drawio (14 頁、每頁多子圖面板、零重疊、工業級排版)。
2. 同步複製至 ~/Downloads/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio。
3. 產生 rsi_duke_uml2_viewer.html (14 分頁皆具備完整多子圖面板 SVG 渲染，絕非空白佔位卡片)。
"""

import os
import sys
import json
import html

# 1. 執行 generate_perfect_uml2.py 產生 draw.io 檔案
sys.path.append("/Users/howard/Desktop/HermesAgent/PortFilio/RSI/diagrams")
from generate_perfect_uml2 import build_all_diagrams
build_all_diagrams()

# 讀取剛剛生成的 draw.io 原始碼
drawio_file = "/Users/howard/Desktop/HermesAgent/PortFilio/RSI/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio"
with open(drawio_file, "r", encoding="utf-8") as f:
    drawio_xml_content = f.read()

json_drawio_xml = json.dumps(drawio_xml_content)

print(f"[OK] 讀取 draw.io 檔案成功，長度: {len(drawio_xml_content)} 字元")
