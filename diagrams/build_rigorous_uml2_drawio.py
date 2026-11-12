#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
UML 2.0 原生 draw.io 多面板產生器 (mxGraphModel XML 格式)
嚴格執行 XML 特殊字元跳脫 (&lt;, &gt;, &quot;, &amp;)
"""

import html

# 配色常數 (Professional Executive Architectural Palette)
C_PANEL_BG     = "#f8fafc"
C_PANEL_BORDER = "#0284c7"
C_PANEL_HEADER = "#0369a1"

C_BLUE_FILL    = "#f0f9ff"
C_BLUE_BORDER  = "#0284c7"
C_BLUE_HEADER  = "#0369a1"

C_AMBER_FILL   = "#fef3c7"
C_AMBER_BORDER = "#d97706"
C_AMBER_HEADER = "#b45309"

C_PURPLE_FILL  = "#f3e8ff"
C_PURPLE_BORDER= "#9333ea"
C_PURPLE_HEADER= "#7e22ce"

C_GREEN_FILL   = "#dcfce7"
C_GREEN_BORDER = "#16a34a"
C_GREEN_HEADER = "#15803d"

C_ORANGE_FILL  = "#ffedd5"
C_ORANGE_BORDER= "#ea580c"
C_ORANGE_HEADER= "#c2410c"

C_RED_FILL     = "#fee2e2"
C_RED_BORDER   = "#dc2626"
C_RED_HEADER   = "#b91c1c"

C_DARK_FILL    = "#1e293b"
C_DARK_BORDER  = "#0f172a"

def xml_attr_escape(text):
    """確保 XML 屬性中的 HTML 標籤與字元被正確編碼"""
    if not text:
        return ""
    # 先做 standard html escape
    escaped = html.escape(str(text), quote=True)
    return escaped.replace("\n", "&#xa;")

class MultiPanelDiagramBuilder:
    def __init__(self, diag_id, diag_name, width=2200, height=1400):
        self.diag_id = diag_id
        self.diag_name = diag_name
        self.width = width
        self.height = height
        self.cells = []
        self.cell_id_counter = 2
        self.cells.append('<mxCell id="0"/>')
        self.cells.append('<mxCell id="1" parent="0"/>')

    def add_page_header(self, title, category, note):
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        raw_val = f"&lt;b&gt;{html.escape(title)}&lt;/b&gt;&#xa;&lt;font style='font-size:11px;font-weight:normal;color:#475569;'&gt;分類：{html.escape(category)} ｜ 專案：RSI 2027 蜂巢計畫 ｜ 資料來源：Duke 2026-11-12 交付架構 ｜ 備註：{html.escape(note)}&lt;/font&gt;"
        style = f"rounded=1;arcSize=6;fillColor=#ffffff;strokeColor={C_BLUE_BORDER};strokeWidth=2;align=left;spacingLeft=20;verticalAlign=middle;fontSize=15;fontColor=#0f172a;shadow=1;html=1;"
        xml = f'<mxCell id="{cid}" value="{raw_val}" style="{style}" vertex="1" parent="1">'
        xml += f'<mxGeometry x="40" y="20" width="{self.width - 80}" height="55" as="geometry"/>'
        xml += '</mxCell>'
        self.cells.append(xml)
        return cid

    def add_panel(self, title, x, y, w, h, bg_color=C_PANEL_BG, border_color=C_PANEL_BORDER, header_color=C_PANEL_HEADER):
        """建立子圖容器面板，確保內部元素有獨立的視覺邊界，絕不與其他圖表混雜"""
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        escaped_title = xml_attr_escape(title)
        style = f"swimlane;horizontal=1;startSize=32;fillColor={bg_color};strokeColor={border_color};strokeWidth=1.5;fontSize=12;fontStyle=1;fontColor=#1e293b;rounded=1;arcSize=4;collapsible=0;shadow=0;html=1;"
        xml = f'<mxCell id="{cid}" value="【子圖面板】{escaped_title}" style="{style}" vertex="1" parent="1">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        xml += '</mxCell>'
        self.cells.append(xml)
        return cid

    def add_box(self, text, x, y, w, h, style, parent_id="1"):
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        escaped_val = xml_attr_escape(text)
        if "html=1" not in style:
            style += ";html=1;"
        xml = f'<mxCell id="{cid}" value="{escaped_val}" style="{style}" vertex="1" parent="{parent_id}">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        xml += '</mxCell>'
        self.cells.append(xml)
        return cid

    def add_uml_class(self, class_name, stereotype, attributes, operations, x, y, w, h, fill=C_BLUE_FILL, stroke=C_BLUE_BORDER, parent_id="1"):
        """繪製標準 UML 2.0 類別圖 (帶屬性與方法獨立區塊)"""
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        st_text = f"&amp;lt;&amp;lt;{html.escape(stereotype)}&amp;gt;&amp;gt;&#xa;" if stereotype else ""
        attr_text = "&#xa;".join([f"+ {html.escape(a)}" for a in attributes])
        ops_text = "&#xa;".join([f"+ {html.escape(o)}" for o in operations])
        val = f"{st_text}&lt;b&gt;{html.escape(class_name)}&lt;/b&gt;&#xa;--&#xa;{attr_text}&#xa;--&#xa;{ops_text}"
        style = f"swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;fontSize=11;"
        xml = f'<mxCell id="{cid}" value="{val}" style="{style}" vertex="1" parent="{parent_id}">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        xml += '</mxCell>'
        self.cells.append(xml)
        return cid

    def add_uml_node(self, node_name, stereotype, details, x, y, w, h, fill=C_BLUE_FILL, stroke=C_BLUE_BORDER, parent_id="1"):
        """繪製標準 UML 2.0 部署節點 (3D 伺服器方塊)"""
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        st_text = f"&amp;lt;&amp;lt;{html.escape(stereotype)}&amp;gt;&amp;gt;&#xa;" if stereotype else ""
        det_text = "&#xa;".join([f"• {html.escape(d)}" for d in details])
        val = f"{st_text}&lt;b&gt;{html.escape(node_name)}&lt;/b&gt;&#xa;--&#xa;{det_text}"
        style = f"shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.08;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;fontSize=11;align=center;verticalAlign=top;spacingTop=10;fontColor=#0f172a;"
        xml = f'<mxCell id="{cid}" value="{val}" style="{style}" vertex="1" parent="{parent_id}">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        xml += '</mxCell>'
        self.cells.append(xml)
        return cid

    def add_uml_component(self, name, stereotype, details, x, y, w, h, fill=C_PURPLE_FILL, stroke=C_PURPLE_BORDER, parent_id="1"):
        """繪製標準 UML 2.0 元件圖元件 (帶元件徽章)"""
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        st_text = f"&amp;lt;&amp;lt;{html.escape(stereotype)}&amp;gt;&amp;gt;&#xa;" if stereotype else ""
        det_text = "&#xa;".join([f"• {html.escape(d)}" for d in details])
        val = f"{st_text}&lt;b&gt;{html.escape(name)}&lt;/b&gt;&#xa;--&#xa;{det_text}"
        style = f"shape=component;align=left;spacingLeft=36;html=1;whiteSpace=wrap;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;fontSize=11;fontColor=#0f172a;"
        xml = f'<mxCell id="{cid}" value="{val}" style="{style}" vertex="1" parent="{parent_id}">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        xml += '</mxCell>'
        self.cells.append(xml)
        return cid

    def add_uml_lifeline(self, name, x, y, w=150, h=480, fill="#ffffff", stroke="#475569", parent_id="1"):
        """繪製標準 UML 循序圖生命線"""
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        val = f"&lt;b&gt;{html.escape(name)}&lt;/b&gt;"
        style = f"shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;size=40;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;fontSize=11;fontColor=#0f172a;"
        xml = f'<mxCell id="{cid}" value="{val}" style="{style}" vertex="1" parent="{parent_id}">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        xml += '</mxCell>'
        self.cells.append(xml)
        return cid

    def add_edge(self, label, src_id, tgt_id, style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#475569;strokeWidth=1.5;", parent_id="1"):
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        escaped_label = xml_attr_escape(label)
        xml = f'<mxCell id="{cid}" value="{escaped_label}" style="{style}" edge="1" parent="{parent_id}" source="{src_id}" target="{tgt_id}">'
        xml += '<mxGeometry relative="1" as="geometry"/>'
        xml += '</mxCell>'
        self.cells.append(xml)
        return cid

    def to_xml(self):
        body = "".join(self.cells)
        return f'<diagram id="{self.diag_id}" name="{self.diag_name}"><mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.width}" pageHeight="{self.height}" math="0" shadow="0"><root>{body}</root></mxGraphModel></diagram>'

print("[OK] MultiPanelDiagramBuilder reloaded with strict XML escaping")
