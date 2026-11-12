#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
將全部 14 張多面板 UML 2.0 SVG 程式碼完整注入至 rsi_duke_uml2_viewer.html
"""

import sys
import os
import re

# 匯入各模組
sys.path.append('/Users/howard/Desktop/HermesAgent/PortFilio/RSI/diagrams')
from build_full_svg_library_all import get_case_0, get_case_1, get_case_2
from build_full_svg_library_all_cases import get_case_3, get_case_4
from build_cases_5_to_8 import get_case_5, get_case_6, get_case_7, get_case_8
from build_cases_9_to_13 import get_case_9, get_case_10, get_case_11, get_case_12, get_case_13

w = 1600
h = 950

cases = [
    get_case_0(w, h),
    get_case_1(w, h),
    get_case_2(w, h),
    get_case_3(w, h),
    get_case_4(w, h),
    get_case_5(w, h),
    get_case_6(w, h),
    get_case_7(w, h),
    get_case_8(w, h),
    get_case_9(w, h),
    get_case_10(w, h),
    get_case_11(w, h),
    get_case_12(w, h),
    get_case_13(w, h),
]

# 組裝 generateSvgForIndex 函式
func_body = f"""    function generateSvgForIndex(index) {{
      const w = {w};
      const h = {h};
      
      switch(index) {{
""" + "\n".join(cases) + f"""
        default:
          return `
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <text x="{w//2}" y="{h//2}" font-family="'Noto Sans TC', sans-serif" font-size="18" fill="#64748b" text-anchor="middle">Diagram 載入中...</text>
            </svg>
          `;
      }}
    }}"""

# 讀取目標 viewer 檔案
viewer_path = '/Users/howard/Desktop/HermesAgent/PortFilio/RSI/rsi_duke_uml2_viewer.html'
with open(viewer_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正則替換 generateSvgForIndex 函式
pattern = r'function\s+generateSvgForIndex\s*\(index\)\s*\{[\s\S]*?\n\s*function\s+openInDrawio'
replacement = func_body + "\n\n    function openInDrawio"

new_content, count = re.subn(pattern, lambda m: replacement, content, count=1)

if count == 0:
    print("[ERROR] 無法定位 function generateSvgForIndex 函式區塊，請檢查 pattern")
    sys.exit(1)

with open(viewer_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"[SUCCESS] 成功將 14 個多面板 SVG 注入至 {viewer_path}！檔案大小: {len(new_content)} 位元組")
