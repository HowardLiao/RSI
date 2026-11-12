#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
完整建置 14 組專業 UML 2.0 視覺化檢視器 (rsi_duke_uml2_viewer.html)
所有 14 張圖皆為 100% 完整多面板 (Multi-Panel) SVG 實作，尺寸 1600 x 950，杜絕任何擠壓與重疊。
"""

import os
import sys
import json
import re

# 匯入各個面板定義
from generate_perfect_uml2 import build_all_diagrams

print("1. 生成原生多頁 draw.io 檔案...")
build_all_diagrams()

# 讀取 draw.io 檔案內容
with open("/Users/howard/Desktop/HermesAgent/PortFilio/RSI/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio", "r", encoding="utf-8") as f:
    drawio_xml_content = f.read()

# 複製到 ~/Downloads/
import shutil
shutil.copyfile(
    "/Users/howard/Desktop/HermesAgent/PortFilio/RSI/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio",
    "/Users/howard/Downloads/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio"
)
print("2. 已同步複製至 /Users/howard/Downloads/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio")

