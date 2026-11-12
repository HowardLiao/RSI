#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open('/Users/howard/Desktop/HermesAgent/PortFilio/RSI/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio', 'r', encoding='utf-8') as f:
    xml_content = f.read()

with open('/Users/howard/Desktop/HermesAgent/PortFilio/RSI/rsi_duke_uml2_viewer.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
replaced = False

for line in lines:
    if line.strip().startswith('const DRAWIO_XML =') or line.strip().startswith('var DRAWIO_XML ='):
        new_lines.append(f"    const DRAWIO_XML = {json.dumps(xml_content)};\n")
        replaced = True
    else:
        new_lines.append(line)

if replaced:
    with open('/Users/howard/Desktop/HermesAgent/PortFilio/RSI/rsi_duke_uml2_viewer.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("[SUCCESS] Successfully updated DRAWIO_XML in rsi_duke_uml2_viewer.html!")
else:
    print("[WARNING] Could not find DRAWIO_XML line to replace.")
