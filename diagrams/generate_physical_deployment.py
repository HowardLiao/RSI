# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import html
import os

def build_diagram():
    root = ET.Element("mxfile", host="app.diagrams.net", agent="HowardAgent", version="21.6.8")
    diagram = ET.SubElement(root, "diagram", id="rsi-hardware-deployment-diagram", name="RSI_Global_Hardware_Deployment")
    mxGraphModel = ET.SubElement(diagram, "mxGraphModel", 
                                 dx="2400", dy="1800", grid="1", gridSize="10", guides="1", 
                                 tooltips="1", connect="1", arrows="1", fold="1", page="1", 
                                 pageScale="1", pageWidth="3800", pageHeight="2400", background="#0b1120")
    
    root_cell = ET.SubElement(mxGraphModel, "root")
    
    # Base cells
    ET.SubElement(root_cell, "mxCell", id="0")
    ET.SubElement(root_cell, "mxCell", id="1", parent="0")

    cell_id_counter = 100
    def next_id():
        nonlocal cell_id_counter
        cell_id_counter += 1
        return str(cell_id_counter)

    def add_cell(tag="mxCell", parent="1", value="", style="", vertex="1", edge="0", x=0, y=0, w=100, h=40):
        cid = next_id()
        cell = ET.SubElement(root_cell, tag, id=cid, parent=parent, value=value, style=style)
        if vertex == "1":
            cell.set("vertex", "1")
            geo = ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), as_="geometry")
        elif edge == "1":
            cell.set("edge", "1")
            geo = ET.SubElement(cell, "mxGeometry", relative="1", as_="geometry")
        return cid, cell

    def add_edge(source_id, target_id, label="", style="", parent="1", points=None):
        cid = next_id()
        cell = ET.SubElement(root_cell, "mxCell", id=cid, parent=parent, value=label, style=style, edge="1")
        cell.set("source", source_id)
        cell.set("target", target_id)
        geo = ET.SubElement(cell, "mxGeometry", relative="1", as_="geometry")
        if points:
            pts = ET.SubElement(geo, "Array", as_="points")
            for px, py in points:
                ET.SubElement(pts, "mxPoint", x=str(px), y=str(py))
        return cid

    # Diagram Title Header Banner
    title_html = (
        "<div style='font-family:Arial,sans-serif; text-align:left;'>"
        "<div style='font-size:24px; font-weight:bold; color:#f8fafc; letter-spacing:1px;'>"
        "信源全球（RSI Group） Project Hive 全球混合雲實體硬體部署架構圖 (UML 2.0 Hardware Deployment)"
        "</div>"
        "<div style='font-size:13px; color:#94a3b8; margin-top:4px;'>"
        "核心節點：台北內湖總部核心機房 ｜ 越南同奈廠 (RDV) ｜ 柬埔寨柴楨廠 (RDG) ｜ AWS 雲端混合運算節點 ｜ 跨國 MPLS + IPsec VPN 雙軌拓撲"
        "</div>"
        "</div>"
    )
    add_cell(value=title_html, 
             style="text;html=1;whiteSpace=wrap;fillColor=#1e293b;strokeColor=#3b82f6;strokeWidth=2;rounded=1;shadow=1;spacingLeft=20;", 
             x=60, y=40, w=3660, h=70)

    # Global Legend / Port Matrix Quick Summary Box
    legend_html = (
        "<div style='font-family:Arial,sans-serif; font-size:11px; color:#cbd5e1; line-height:1.6;'>"
        "<b style='color:#38bdf8; font-size:12px;'>【圖例與通訊矩陣標準標示說明】</b><br/>"
        "<span style='display:inline-block; width:10px; height:10px; background:#10b981; border-radius:50%; margin-right:4px;'></span>主機正常運作 / Link Active &nbsp;&nbsp;"
        "<span style='display:inline-block; width:10px; height:10px; background:#3b82f6; border-radius:50%; margin-right:4px;'></span>iDRAC / System ID LED &nbsp;&nbsp;"
        "<span style='display:inline-block; width:10px; height:10px; background:#f59e0b; border-radius:50%; margin-right:4px;'></span>RAID 快取 / Fault LED &nbsp;&nbsp;"
        "<span style='color:#f43f5e; font-weight:bold;'>━ ━</span> MPLS 專線 (100M/50M) &nbsp;&nbsp;"
        "<span style='color:#38bdf8; font-weight:bold;'>━━━</span> IPsec VPN (UDP 500/4500) &nbsp;&nbsp;"
        "<span style='color:#a855f7; font-weight:bold;'>━━━</span> 10GbE iSCSI SAN Fabric (Port 3260) &nbsp;&nbsp;"
        "<span style='color:#10b981; font-weight:bold;'>━━━</span> 25GbE RoCE / Trunk LAN"
        "</div>"
    )
    add_cell(value=legend_html,
             style="text;html=1;whiteSpace=wrap;fillColor=#0f172a;strokeColor=#475569;strokeWidth=1;rounded=1;spacingLeft=15;",
             x=2680, y=45, w=1020, h=60)

    # -------------------------------------------------------------
    # Helper: Build Realistic Server Rackmount Chassis with Drive Bays & LEDs
    # -------------------------------------------------------------
    def draw_realistic_server(parent, x, y, w, h, model_name, form_factor, serial, 
                              hw_spec, hypervisor, vms_pods, status="HEALTHY"):
        container_style = (
            "swimlane;html=1;whiteSpace=wrap;collapsible=0;recursiveResize=0;"
            "fillColor=#0f172a;strokeColor=#334155;strokeWidth=2;rounded=1;shadow=1;"
            "fontFamily=Arial;fontColor=#f8fafc;fontSize=13;fontStyle=1;startSize=28;"
            "swimlaneFillColor=#090d16;"
        )
        chassis_title = f"«device» {model_name} [{form_factor}] &nbsp;&nbsp;|&nbsp;&nbsp; S/N: {serial}"
        srv_id, _ = add_cell(parent=parent, value=chassis_title, style=container_style, x=x, y=y, w=w, h=h)

        # 1. Physical Front Bezel Assembly (1U / 2U Server Faceplate)
        bezel_h = 74 if form_factor == "2U" else 52
        bezel_style = (
            "rounded=1;whiteSpace=wrap;html=1;fillColor=#181d28;strokeColor=#475569;strokeWidth=2;"
            "shadow=0;glass=0;"
        )
        bezel_id, _ = add_cell(parent=srv_id, value="", style=bezel_style, x=15, y=38, w=w-30, h=bezel_h)

        # Rackmount Ear Left & Right (Silver metallic brackets with screw holes)
        ear_style = "rounded=0;whiteSpace=wrap;html=1;fillColor=#64748b;strokeColor=#334155;strokeWidth=1;"
        add_cell(parent=bezel_id, value="", style=ear_style, x=0, y=0, w=14, h=bezel_h)
        add_cell(parent=bezel_id, value="", style="ellipse;fillColor=#0f172a;strokeColor=#334155;", x=3, y=8, w=8, h=8)
        add_cell(parent=bezel_id, value="", style="ellipse;fillColor=#0f172a;strokeColor=#334155;", x=3, y=bezel_h-16, w=8, h=8)

        add_cell(parent=bezel_id, value="", style=ear_style, x=(w-30)-14, y=0, w=14, h=bezel_h)
        add_cell(parent=bezel_id, value="", style="ellipse;fillColor=#0f172a;strokeColor=#334155;", x=(w-30)-11, y=8, w=8, h=8)
        add_cell(parent=bezel_id, value="", style="ellipse;fillColor=#0f172a;strokeColor=#334155;", x=(w-30)-11, y=bezel_h-16, w=8, h=8)

        # Left Control & Diagnostic Panel (Power LED, ID LED, Health LED, USB port)
        ctrl_panel_style = "rounded=0;whiteSpace=wrap;html=1;fillColor=#0a0e17;strokeColor=#334155;strokeWidth=1;"
        ctrl_id, _ = add_cell(parent=bezel_id, value="", style=ctrl_panel_style, x=18, y=4, w=50, h=bezel_h-8)
        # Power button & LED (Green)
        add_cell(parent=ctrl_id, value="", style="ellipse;fillColor=#10b981;strokeColor=#059669;shadow=1;", x=6, y=6, w=8, h=8)
        # System ID (Blue)
        add_cell(parent=ctrl_id, value="", style="ellipse;fillColor=#3b82f6;strokeColor=#1d4ed8;shadow=1;", x=20, y=6, w=8, h=8)
        # Fault/Status LED (Amber)
        add_cell(parent=ctrl_id, value="", style="ellipse;fillColor=#22c55e;strokeColor=#15803d;", x=34, y=6, w=8, h=8)
        # Model badge
        add_cell(parent=ctrl_id, value="<b style='color:#94a3b8;font-size:8px;'>DELL</b>", 
                 style="text;html=1;align=center;verticalAlign=middle;fontColor=#ffffff;fontSize=8;", 
                 x=2, y=bezel_h-26, w=46, h=14)

        # Hot-Swap Drive Bays (Array of Drive Trays with Status LEDs and Release Levers)
        num_drives = 8 if form_factor == "2U" else 6
        bay_start_x = 75
        bay_avail_w = (w - 30) - 270
        bay_w = int(bay_avail_w / num_drives) - 4
        bay_h = bezel_h - 10

        for i in range(num_drives):
            bx = bay_start_x + i * (bay_w + 4)
            tray_style = (
                "rounded=1;whiteSpace=wrap;html=1;fillColor=#1e293b;strokeColor=#475569;strokeWidth=1;"
                "shadow=0;"
            )
            tray_id, _ = add_cell(parent=bezel_id, value="", style=tray_style, x=bx, y=5, w=bay_w, h=bay_h)
            # Drive latch handle
            add_cell(parent=tray_id, value="", style="rounded=1;fillColor=#334155;strokeColor=#1e293b;", x=3, y=bay_h-12, w=bay_w-6, h=7)
            # Drive Status LEDs (Green activity, amber fault)
            add_cell(parent=tray_id, value="", style="ellipse;fillColor=#10b981;strokeColor=#059669;", x=4, y=4, w=5, h=5)
            add_cell(parent=tray_id, value="", style="ellipse;fillColor=#0284c7;strokeColor=#0369a1;", x=12, y=4, w=5, h=5)
            # Mini slot number / drive type
            drive_lbl = f"<div style='font-size:7px;color:#94a3b8;text-align:center;'>BAY{i}<br/>SSD</div>"
            add_cell(parent=tray_id, value=drive_lbl, style="text;html=1;align=center;verticalAlign=middle;", x=0, y=10, w=bay_w, h=bay_h-24)

        # Right Panel: Physical Ports (SFP+ Optical, RJ45 10GbE, Dual Hot-swap PSUs)
        right_panel_x = (w - 30) - 185
        rpanel_style = "rounded=0;whiteSpace=wrap;html=1;fillColor=#0f172a;strokeColor=#334155;strokeWidth=1;"
        rpanel_id, _ = add_cell(parent=bezel_id, value="", style=rpanel_style, x=right_panel_x, y=4, w=165, h=bezel_h-8)
        
        # Dual 1400W PSU indicators
        psu_lbl = "<div style='font-size:8px;color:#38bdf8;font-weight:bold;line-height:1.2;'>"                   "PSU1: 1400W AC ●<br/>PSU2: 1400W AC ●</div>"
        add_cell(parent=rpanel_id, value=psu_lbl, style="text;html=1;align=left;verticalAlign=middle;", x=6, y=2, w=75, h=bezel_h-12)

        # 2x SFP+ 10GbE Optical Ports + 2x RJ45 10GbE Ports
        nic_lbl = "<div style='font-size:8px;color:#a7f3d0;font-weight:bold;line-height:1.2;'>"                   "SFP+ [10G] ■ ■<br/>RJ45 [10G] ☲ ☲</div>"
        add_cell(parent=rpanel_id, value=nic_lbl, style="text;html=1;align=left;verticalAlign=middle;", x=85, y=2, w=75, h=bezel_h-12)

        # 2. Hardware Specification Banner (CPU, RAM, Storage RAID, Network, Out-of-band)
        hw_box_y = 42 + bezel_h
        hw_box_h = 76
        hw_html = (
            f"<div style='font-family:Arial,sans-serif; font-size:10px; color:#e2e8f0; line-height:1.45; text-align:left;'>"
            f"<b style='color:#38bdf8; font-size:11px;'>【實體硬體規格 Physical Hardware Specs】</b><br/>"
            f"• <b>處理器 CPU:</b> {hw_spec.get('cpu', 'Intel Xeon Gold')}<br/>"
            f"• <b>記憶體 RAM:</b> {hw_spec.get('ram', '256GB ECC DDR5')}<br/>"
            f"• <b>本機儲存 Storage:</b> {hw_spec.get('disk', '8x 1.92TB NVMe SSD RAID10')}<br/>"
            f"• <b>網卡 NIC:</b> {hw_spec.get('nic', '4x 10GbE SFP+ / 2x 25GbE')} &nbsp;|&nbsp; <b>帶外管理 OOB:</b> {hw_spec.get('oob', 'Dell iDRAC9 Enterprise (Port 443)')}"
            f"</div>"
        )
        add_cell(parent=srv_id, value=hw_html, 
                 style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1e293b;strokeColor=#334155;strokeWidth=1;spacingLeft=10;",
                 x=15, y=hw_box_y, w=w-30, h=hw_box_h)

        # 3. Hypervisor / Host OS Container
        hyp_y = hw_box_y + hw_box_h + 8
        hyp_h = h - hyp_y - 12
        hyp_style = (
            "swimlane;html=1;whiteSpace=wrap;collapsible=0;recursiveResize=0;"
            "fillColor=#132035;strokeColor=#2563eb;strokeWidth=1.5;rounded=1;"
            "fontFamily=Arial;fontColor=#60a5fa;fontSize=11;fontStyle=1;startSize=24;"
            "swimlaneFillColor=#0b1526;"
        )
        hyp_title = f"«executionEnvironment» {hypervisor.get('name', 'Hypervisor')} | Host IP: {hypervisor.get('ip', '192.168.0.x')}"
        hyp_id, _ = add_cell(parent=srv_id, value=hyp_title, style=hyp_style, x=15, y=hyp_y, w=w-30, h=hyp_h)

        # 4. Nested VMs or Containers / Pods
        num_vms = len(vms_pods)
        vm_padding = 10
        vm_w = int((w - 30 - 20 - (num_vms - 1) * vm_padding) / num_vms) if num_vms > 0 else (w - 50)
        vm_h = hyp_h - 34

        for vi, vm in enumerate(vms_pods):
            vx = 10 + vi * (vm_w + vm_padding)
            vy = 28
            is_k8s = vm.get("type", "vm") == "k8s" or vm.get("type", "vm") == "pod"
            vm_border = "#10b981" if is_k8s else "#f59e0b"
            vm_hdr_bg = "#064e3b" if is_k8s else "#78350f"
            vm_bg = "#062820" if is_k8s else "#1c1409"
            
            vm_container_style = (
                "swimlane;html=1;whiteSpace=wrap;collapsible=0;recursiveResize=0;"
                f"fillColor={vm_hdr_bg};strokeColor={vm_border};strokeWidth=1.5;rounded=1;"
                f"fontFamily=Arial;fontColor=#f8fafc;fontSize=11;fontStyle=1;startSize=22;"
                f"swimlaneFillColor={vm_bg};"
            )
            vm_header_label = f"«{vm.get('type','VM')}» {vm.get('name')} ({vm.get('ip')})"
            vm_id, _ = add_cell(parent=hyp_id, value=vm_header_label, style=vm_container_style, x=vx, y=vy, w=vm_w, h=vm_h)

            # VM / Container Inner Services & Listening Port Matrix
            services_html = (
                f"<div style='font-family:Arial,sans-serif; font-size:10px; color:#e2e8f0; line-height:1.45; text-align:left;'>"
                f"<b style='color:#fcd34d;'>規格:</b> {vm.get('resources', '4 vCPU / 16GB RAM')}<br/>"
                f"<b style='color:#38bdf8;'>作業系統:</b> {vm.get('os', 'Windows Server / Ubuntu')}<br/>"
                f"<div style='height:4px;'></div>"
                f"<b style='color:#4ade80;'>【核心服務與對應 Port 矩陣】</b><br/>"
            )
            for s in vm.get("services", []):
                proto = s.get("proto", "TCP")
                port = s.get("port")
                sname = s.get("name")
                desc = s.get("desc", "")
                services_html += (
                    f"• <span style='color:#67e8f9; font-weight:bold;'>{proto} {port}:</span> "
                    f"<span style='color:#ffffff; font-weight:bold;'>{sname}</span> "
                    f"<span style='color:#94a3b8; font-size:9px;'>({desc})</span><br/>"
                )
            services_html += "</div>"

            add_cell(parent=vm_id, value=services_html,
                     style="text;html=1;whiteSpace=wrap;spacingLeft=8;spacingRight=6;spacingTop=6;",
                     x=4, y=24, w=vm_w-8, h=vm_h-28)

        return srv_id

    # -------------------------------------------------------------
    # Helper: Build Storage Array (Dell Unity 480XT All-Flash SAN)
    # -------------------------------------------------------------
    def draw_san_storage(parent, x, y, w, h, model_name, serial, hw_spec, targets):
        san_id, _ = add_cell(parent=parent, value=f"«SAN Storage» {model_name} | S/N: {serial}", 
                             style="swimlane;html=1;whiteSpace=wrap;collapsible=0;fillColor=#1e1b4b;strokeColor=#818cf8;strokeWidth=2;rounded=1;fontFamily=Arial;fontColor=#e0e7ff;fontSize=13;fontStyle=1;startSize=28;swimlaneFillColor=#09091b;",
                             x=x, y=y, w=w, h=h)

        # 2U DPE Front Bezel with 25x 2.5" Flash Drive Slots
        bezel_h = 76
        bezel_id, _ = add_cell(parent=san_id, value="", style="rounded=1;whiteSpace=wrap;html=1;fillColor=#17153a;strokeColor=#6366f1;strokeWidth=2;", x=15, y=36, w=w-30, h=bezel_h)
        # Left ear & right ear
        add_cell(parent=bezel_id, value="", style="rounded=0;fillColor=#64748b;", x=0, y=0, w=14, h=bezel_h)
        add_cell(parent=bezel_id, value="", style="rounded=0;fillColor=#64748b;", x=(w-30)-14, y=0, w=14, h=bezel_h)
        # Unity Badge
        add_cell(parent=bezel_id, value="<b style='color:#a5b4fc;font-size:9px;'>DELL EMC<br/>Unity 480XT</b>", 
                 style="text;html=1;align=center;verticalAlign=middle;", x=16, y=6, w=65, h=bezel_h-12)
        
        # 16 mini SSD slots visual
        bay_w = 26
        for bi in range(16):
            bx = 88 + bi * (bay_w + 3)
            tid, _ = add_cell(parent=bezel_id, value="", style="rounded=1;fillColor=#1e1b4b;strokeColor=#4338ca;", x=bx, y=6, w=bay_w, h=bezel_h-12)
            add_cell(parent=tid, value="", style="ellipse;fillColor=#10b981;", x=4, y=4, w=4, h=4)
            add_cell(parent=tid, value=f"<div style='font-size:7px;color:#c7d2fe;text-align:center;'>SAS<br/>{bi+1}</div>", 
                     style="text;html=1;align=center;", x=0, y=14, w=bay_w, h=bezel_h-30)

        # Dual Controller Module on right
        add_cell(parent=bezel_id, value="<b style='color:#38bdf8;font-size:8px;'>Dual SP-A/B<br/>Active/Active<br/>8x 10G iSCSI<br/>4x 16G FC</b>",
                 style="text;html=1;align=center;verticalAlign=middle;", x=(w-30)-130, y=4, w=110, h=bezel_h-8)

        # Specs box
        specs_html = (
            f"<div style='font-family:Arial,sans-serif; font-size:10px; color:#e0e7ff; line-height:1.45; text-align:left;'>"
            f"<b style='color:#a5b4fc; font-size:11px;'>【全快閃儲存陣列規格 SAN Storage Architecture】</b><br/>"
            f"• <b>控制器控制器架構:</b> Dual Active-Active Storage Processors (Intel Xeon 8C 1.8GHz, 128GB NVRAM 快取)<br/>"
            f"• <b>實體硬碟池:</b> 25x 3.84TB SAS 12Gbps Enterprise SSD (RAID 6 動態硬碟池, 80TB 淨可用容量)<br/>"
            f"• <b>主機介面與通訊埠:</b> 8x 10GbE Optical SFP+ iSCSI (Port 3260), 4x 16Gbps Fibre Channel, 4x 1GbE Mgmt (Port 443 Unisphere)<br/>"
            f"• <b>LUN 掛載與共享目標 (Targets):</b>"
            f"</div>"
        )
        add_cell(parent=san_id, value=specs_html,
                 style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1e1b4b;strokeColor=#4338ca;spacingLeft=10;",
                 x=15, y=36 + bezel_h + 8, w=w-30, h=72)

        # LUN mapping cards
        lun_start_y = 36 + bezel_h + 88
        for li, tgt in enumerate(targets):
            lx = 15 + li * 270
            lcard_html = (
                f"<div style='font-family:Arial,sans-serif; font-size:10px; color:#ffffff; line-height:1.4;'>"
                f"<b style='color:#38bdf8;'>LUN #{tgt['lun']}: {tgt['name']}</b><br/>"
                f"• 容量: {tgt['size']} | RAID 6<br/>"
                f"• 掛載端: {tgt['client']}<br/>"
                f"• 傳輸通道: iSCSI Port 3260 (MPIO 雙路徑)<br/>"
                f"• 用途: {tgt['desc']}"
                f"</div>"
            )
            add_cell(parent=san_id, value=lcard_html,
                     style="rounded=1;whiteSpace=wrap;html=1;fillColor=#2e1065;strokeColor=#7c3aed;strokeWidth=1;spacingLeft=8;",
                     x=lx, y=lun_start_y, w=260, h=76)

        return san_id

    # -------------------------------------------------------------
    # Helper: Build Physical Firewall / Switch Appliance
    # -------------------------------------------------------------
    def draw_network_appliance(parent, x, y, w, h, model_name, role_name, ip, ports_info):
        app_id, _ = add_cell(parent=parent, value=f"«appliance» {model_name} [{role_name}]",
                             style="swimlane;html=1;whiteSpace=wrap;collapsible=0;fillColor=#1e293b;strokeColor=#0284c7;strokeWidth=2;rounded=1;fontFamily=Arial;fontColor=#38bdf8;fontSize=12;fontStyle=1;startSize=26;swimlaneFillColor=#090d16;",
                             x=x, y=y, w=w, h=h)

        # 1U Chassis Bezel
        bezel_id, _ = add_cell(parent=app_id, value="", style="rounded=1;fillColor=#111827;strokeColor=#374151;strokeWidth=1;", x=10, y=32, w=w-20, h=44)
        # Ears
        add_cell(parent=bezel_id, value="", style="rounded=0;fillColor=#64748b;", x=0, y=0, w=10, h=44)
        add_cell(parent=bezel_id, value="", style="rounded=0;fillColor=#64748b;", x=(w-20)-10, y=0, w=10, h=44)
        # Model
        add_cell(parent=bezel_id, value=f"<b style='color:#38bdf8;font-size:9px;'>{model_name}</b>", 
                 style="text;html=1;align=center;", x=12, y=6, w=90, h=32)

        # Port row
        ports_html = (
            "<div style='font-family:Arial,sans-serif; font-size:8px; color:#cbd5e1; text-align:left;'>"
            "<span style='color:#10b981;'>● WAN1 (MPLS)</span> &nbsp;|&nbsp; "
            "<span style='color:#10b981;'>● WAN2 (Internet VPN)</span> &nbsp;|&nbsp; "
            "<span style='color:#38bdf8;'>■ SFP+ FortiLink</span> &nbsp;|&nbsp; "
            "<span style='color:#fbbf24;'>● DMZ</span> &nbsp;|&nbsp; "
            "<span style='color:#94a3b8;'>Internal 1-16 (VLAN 10/20/30/40)</span>"
            "</div>"
        )
        add_cell(parent=bezel_id, value=ports_html, style="text;html=1;align=left;verticalAlign=middle;", x=110, y=4, w=w-150, h=36)

        # Specs description
        spec_text = (
            f"<div style='font-family:Arial,sans-serif; font-size:10px; color:#cbd5e1; line-height:1.4; text-align:left;'>"
            f"• <b>閘道 IP:</b> {ip}<br/>"
            f"• <b>連線服務:</b> {ports_info}"
            f"</div>"
        )
        add_cell(parent=app_id, value=spec_text, style="text;html=1;whiteSpace=wrap;spacingLeft=6;", x=10, y=82, w=w-20, h=h-90)

        return app_id

    # =========================================================================
    # REGION 1: 台北內湖總部核心機房 (Taipei Neihu HQ Data Center)
    # =========================================================================
    hq_container_style = (
        "swimlane;html=1;whiteSpace=wrap;collapsible=0;recursiveResize=0;"
        "fillColor=#090d16;strokeColor=#3b82f6;strokeWidth=2.5;rounded=1;shadow=1;"
        "fontFamily=Arial;fontColor=#93c5fd;fontSize=16;fontStyle=1;startSize=36;"
        "swimlaneFillColor=#060911;"
    )
    hq_title = "台北內湖總部核心機房 (Taipei Neihu HQ Data Center) ｜ IP 網段: 192.168.0.0/24 & 10.10.0.0/16"
    hq_id, _ = add_cell(value=hq_title, style=hq_container_style, x=60, y=140, w=2200, h=1520)

    # HQ Core Security & Switching: FortiGate 200F & Dell S5248F Switch
    fg200f_id, _ = add_cell(parent=hq_id, value="", style="", vertex="0", x=0, y=0, w=0, h=0)
    fg200f_id = draw_network_appliance(
        parent=hq_id, x=20, y=50, w=1060, h=140,
        model_name="FortiGate 200F", role_name="HQ Core NGFW / SD-WAN Controller",
        ip="WAN1: 210.65.x.x (MPLS 100M) | WAN2: 61.220.x.x (FTTB) | LAN: 192.168.0.254",
        ports_info="IPsec VPN (IKEv2 UDP 500/4500, ESP 50) ↔ 越南 RDV / 柬埔寨 RDG / AWS VPC；HTTPS 443 SSL-VPN；BGP 179"
    )

    s5248_id = draw_network_appliance(
        parent=hq_id, x=1100, y=50, w=1070, h=140,
        model_name="Dell PowerSwitch S5248F-ON", role_name="25GbE ToR Core Switch (Dual L2/L3 VLT)",
        ip="Mgmt IP: 10.10.99.1 (VLAN 99 Out-of-band)",
        ports_info="48x 25GbE SFP28 + 4x 100GbE QSFP28 Uplink；支援 RoCE v2 RDMA、iSCSI 低延遲 Jumbo Frame 9000、VLT 雙機高可用"
    )

    # HQ Server 1: RSI-SRV-HQ01 (2U Dell PowerEdge R760)
    srv_hq01_id = draw_realistic_server(
        parent=hq_id, x=20, y=210, w=1060, h=420,
        model_name="Dell PowerEdge R760 [RSI-SRV-HQ01]", form_factor="2U", serial="DELL-R760-TW01-NVME",
        hw_spec={
            "cpu": "2x Intel Xeon Gold 6430 (64核/128緒, 2.1GHz~3.4GHz, 60MB L3 Cache)",
            "ram": "256GB ECC DDR5-4800 (8x 32GB, 八通道架構)",
            "disk": "8x 1.92TB Enterprise NVMe PCIe 4.0 SSD (PERC H755 Front RAID 10, 7.6TB 有效空間)",
            "nic": "4x 10GbE SFP+ (Intel E810) + 2x 1GbE RJ45",
            "oob": "iDRAC9 Enterprise (Dedicated Port, 192.168.0.101)"
        },
        hypervisor={"name": "VMware ESXi 8.0 Enterprise Plus (Clustered with HQ02)", "ip": "192.168.0.21"},
        vms_pods=[
            {
                "name": "RDSMP2", "type": "VM", "ip": "192.168.0.22",
                "os": "Windows Server 2022 Standard", "resources": "16 vCPU / 64GB RAM",
                "services": [
                    {"proto": "TCP", "port": "80 / 443", "name": "IIS Web (SAM 打樣系統)", "desc": "服飾樣品打樣作業核心"},
                    {"proto": "TCP", "port": "1433", "name": "MS SQL Server (SAM 本地庫)", "desc": "樣品專案與歷史料表庫"},
                    {"proto": "TCP", "port": "445", "name": "SMB / CIFS 檔案共享", "desc": "版單 CAD/PDF 儲存"},
                    {"proto": "TCP", "port": "8000-8020", "name": "13 支同步批次排程服務", "desc": "跨國主檔定時同步器"}
                ]
            },
            {
                "name": "RDSMP1", "type": "VM", "ip": "192.168.0.23",
                "os": "Windows Server 2022 Standard", "resources": "16 vCPU / 64GB RAM",
                "services": [
                    {"proto": "TCP", "port": "8012", "name": "IIS Application Request Routing", "desc": "反向代理 & SSL 卸載"},
                    {"proto": "TCP", "port": "5000", "name": ".NET 8 CQS 微服務閘道", "desc": "採購 / 物料高併發查詢"},
                    {"proto": "TCP", "port": "9100", "name": "Prometheus Node Exporter", "desc": "主機與 VM 資源監控"},
                    {"proto": "TCP", "port": "3389", "name": "RDP 安全跳板登入", "desc": "管理維運通訊"}
                ]
            }
        ]
    )

    # HQ Server 2: RSI-SRV-HQ02 (2U Dell PowerEdge R760)
    srv_hq02_id = draw_realistic_server(
        parent=hq_id, x=1100, y=210, w=1070, h=420,
        model_name="Dell PowerEdge R760 [RSI-SRV-HQ02]", form_factor="2U", serial="DELL-R760-TW02-NVME",
        hw_spec={
            "cpu": "2x Intel Xeon Gold 6430 (64核/128緒, 2.1GHz)",
            "ram": "256GB ECC DDR5-4800 (8x 32GB)",
            "disk": "8x 1.92TB Enterprise NVMe PCIe 4.0 SSD (PERC H755 Front RAID 10, 7.6TB 有效空間)",
            "nic": "4x 10GbE SFP+ (Intel E810) + 2x 1GbE RJ45",
            "oob": "iDRAC9 Enterprise (Dedicated Port, 192.168.0.102)"
        },
        hypervisor={"name": "VMware ESXi 8.0 Enterprise Plus (HA / DRS Enabled)", "ip": "192.168.0.25"},
        vms_pods=[
            {
                "name": "RSI-D365-AOS01", "type": "VM", "ip": "192.168.0.30",
                "os": "Windows Server 2022 Datacenter", "resources": "24 vCPU / 96GB RAM",
                "services": [
                    {"proto": "TCP", "port": "8101", "name": "Dynamics 365 AOS 服務實例 1", "desc": "ERP 交易業務邏輯核心"},
                    {"proto": "TCP", "port": "8201", "name": "Dynamics 365 AOS 服務實例 2", "desc": "高負載工單批次計算引擎"},
                    {"proto": "TCP", "port": "8088", "name": "D365 OData REST API", "desc": "提供對外系統安全資料交換"},
                    {"proto": "TCP", "port": "443", "name": "WCF 內部安全通訊端點", "desc": "加密跨模組呼叫"}
                ]
            },
            {
                "name": "RSI-INT-GW01", "type": "VM", "ip": "192.168.0.35",
                "os": "Ubuntu 22.04 LTS", "resources": "8 vCPU / 32GB RAM",
                "services": [
                    {"proto": "TCP", "port": "5672", "name": "RabbitMQ AMQP 消息中繼代理", "desc": "跨國排程事件廣播"},
                    {"proto": "TCP", "port": "15672", "name": "RabbitMQ Web 管理控制台", "desc": "隊列長度與消費者監控"},
                    {"proto": "TCP", "port": "6379", "name": "Redis 7.0 分散式快取叢集", "desc": "料號/物料規格熱點快取"},
                    {"proto": "TCP", "port": "8080", "name": "Celery Worker 異步任務分派", "desc": "全球報表異步生成引擎"}
                ]
            }
        ]
    )

    # HQ Server 3: RSI-SRV-HQ03 (2U Dell PowerEdge R760 - Baremetal Database Cluster)
    srv_hq03_id = draw_realistic_server(
        parent=hq_id, x=20, y=650, w=1060, h=410,
        model_name="Dell PowerEdge R760 [RSI-SRV-HQ03 - 裸機資料庫主機]", form_factor="2U", serial="DELL-R760-TW03-SQLDB",
        hw_spec={
            "cpu": "2x Intel Xeon Gold 6430 (64核/128緒, 2.1GHz~3.4GHz)",
            "ram": "512GB ECC DDR5-4800 (16x 32GB 高頻寬記憶體)",
            "disk": "10x 3.84TB SAS 12Gbps Enterprise SSD (RAID 10, 19.2TB 本機高速日誌空間)",
            "nic": "2x 25GbE SFP28 (RDMA / RoCE 低延遲) + 4x 10GbE SFP+",
            "oob": "iDRAC9 Enterprise (Dedicated Port, 192.168.0.103)"
        },
        hypervisor={"name": "Baremetal Windows Server 2022 Datacenter (WSFC 故障轉移叢集)", "ip": "192.168.0.10"},
        vms_pods=[
            {
                "name": "rsiaxdb1 (SQL 主實例)", "type": "Baremetal", "ip": "192.168.0.10",
                "os": "Windows Server 2022 Datacenter WSFC", "resources": "64 Cores / 512GB RAM (全裸機算力)",
                "services": [
                    {"proto": "TCP", "port": "1433", "name": "MS SQL Server 2022 Enterprise", "desc": "Dynamics 365 核心營運庫 AXDB"},
                    {"proto": "TCP", "port": "5022", "name": "SQL AlwaysOn Availability Group", "desc": "高可用即時同步複製"},
                    {"proto": "TCP", "port": "1434", "name": "SQL Browser & Dedicated Admin DAC", "desc": "資料庫診斷連線"},
                    {"proto": "TCP", "port": "3260", "name": "iSCSI MPIO Initiator (掛載 SAN)", "desc": "掛載 Unity 480XT 儲存陣列 LUN"}
                ]
            }
        ]
    )

    # HQ Server 4: RSI-SRV-HQ04 (1U Dell PowerEdge R660 - Kubernetes Master/Worker Node)
    srv_hq04_id = draw_realistic_server(
        parent=hq_id, x=1100, y=650, w=1070, h=410,
        model_name="Dell PowerEdge R660 [RSI-SRV-HQ04 - Kubernetes 核心節點]", form_factor="1U", serial="DELL-R660-TW04-K8S",
        hw_spec={
            "cpu": "2x Intel Xeon Silver 4410Y (24核/48緒, 2.0GHz, 低功耗高效能)",
            "ram": "128GB ECC DDR5-4800 (4x 32GB)",
            "disk": "4x 1.92TB Enterprise NVMe SSD (RAID 1 OS + RAID 1 Container Storage)",
            "nic": "4x 10GbE SFP+ (Intel X710) + 2x 1GbE RJ45",
            "oob": "iDRAC9 Enterprise (Dedicated Port, 192.168.0.104)"
        },
        hypervisor={"name": "Kubernetes v1.28 Control Plane & Worker Node (Ubuntu 22.04 LTS)", "ip": "192.168.0.50"},
        vms_pods=[
            {
                "name": "K8s Ingress & API Gateway", "type": "k8s", "ip": "192.168.0.51",
                "os": "Envoy / Cilium eBPF CNI", "resources": "8 vCPU / 32GB RAM",
                "services": [
                    {"proto": "TCP", "port": "6443", "name": "Kubernetes API Server", "desc": "K8s 叢集主控通訊與管理"},
                    {"proto": "TCP", "port": "80 / 443", "name": "Envoy Ingress Gateway", "desc": "微服務統一入口反向代理"},
                    {"proto": "TCP", "port": "2379-2380", "name": "etcd 分散式狀態資料庫", "desc": "叢集元資料持久化"}
                ]
            },
            {
                "name": "K8s Monitoring & Observability", "type": "k8s", "ip": "192.168.0.52",
                "os": "Prometheus + Grafana Stack", "resources": "8 vCPU / 32GB RAM",
                "services": [
                    {"proto": "TCP", "port": "9090", "name": "Prometheus TSDB 時序監控庫", "desc": "全球主機/VM 指標抓取"},
                    {"proto": "TCP", "port": "3000", "name": "Grafana 全球監控戰情看板", "desc": "維運與各廠看板視覺化"},
                    {"proto": "TCP", "port": "24224", "name": "Fluentbit 跨國統一日誌收集", "desc": "收集各站點邊緣記錄"}
                ]
            }
        ]
    )

    # HQ SAN Storage: Dell Unity 480XT All-Flash SAN
    san_hq_id = draw_san_storage(
        parent=hq_id, x=20, y=1080, w=2150, h=410,
        model_name="Dell Unity 480XT All-Flash SAN Storage", serial="DELL-UNITY-480XT-HQSAN",
        hw_spec={},
        targets=[
            {"lun": "01", "name": "LUN_D365_DATA (AXDB 主資料檔)", "size": "30TB", "client": "RSI-SRV-HQ03 (rsiaxdb1)", "desc": "極致 0.3ms 延遲 NVMe Flash 池"},
            {"lun": "02", "name": "LUN_D365_LOG (SQL 交易日誌)", "size": "10TB", "client": "RSI-SRV-HQ03 (rsiaxdb1)", "desc": "RAID 10 鏡像高速寫入池"},
            {"lun": "03", "name": "LUN_ESXI_VMFS01 (虛擬機主資料存放區)", "size": "25TB", "client": "RSI-SRV-HQ01 / HQ02", "desc": "ESXi 8.0 叢集共享 VMFS 6"},
            {"lun": "04", "name": "LUN_BACKUP_SNAPSHOT (快照備份存放區)", "size": "15TB", "client": "Veeam / RSI-INT-GW01", "desc": "每小時無感硬體快照"}
        ]
    )

    # =========================================================================
    # REGION 2: 越南同奈廠 (Vietnam Dong Nai RDV Plant Edge DC)
    # =========================================================================
    rdv_container_style = (
        "swimlane;html=1;whiteSpace=wrap;collapsible=0;recursiveResize=0;"
        "fillColor=#090d16;strokeColor=#10b981;strokeWidth=2;rounded=1;shadow=1;"
        "fontFamily=Arial;fontColor=#6ee7b7;fontSize=15;fontStyle=1;startSize=34;"
        "swimlaneFillColor=#060a0f;"
    )
    rdv_title = "越南同奈廠 (Vietnam RDV Plant Edge DC) ｜ 內網網段: 172.16.10.0/24"
    rdv_id, _ = add_cell(value=rdv_title, style=rdv_container_style, x=2320, y=140, w=1400, h=660)

    # RDV Firewall
    fg80f_id = draw_network_appliance(
        parent=rdv_id, x=20, y=45, w=1360, h=130,
        model_name="FortiGate 80F", role_name="RDV Edge Firewall & SD-WAN",
        ip="WAN1: 113.161.x.x (MPLS 100M) | WAN2: 14.162.x.x (VNPT FTTB) | LAN: 172.16.10.254",
        ports_info="IPsec VPN (UDP 500/4500) ↔ 台北 HQ Core 200F；SD-WAN 智慧線路品質偵測與動態容錯移轉"
    )

    # RDV Server 1: RDV-EDGE-SRV01 (1U Dell PowerEdge R650xs)
    srv_rdv01_id = draw_realistic_server(
        parent=rdv_id, x=20, y=190, w=1360, h=440,
        model_name="Dell PowerEdge R650xs [RDV-EDGE-SRV01 - 越南邊緣主機]", form_factor="1U", serial="DELL-R650XS-VN01-EDGE",
        hw_spec={
            "cpu": "1x Intel Xeon Silver 4314 (16核/32緒, 2.4GHz~3.4GHz)",
            "ram": "64GB ECC DDR4-3200 (4x 16GB)",
            "disk": "2x 960GB NVMe SSD (RAID 1 OS) + 2x 2.4TB SAS 10K (RAID 1 本地離線暫存資料庫)",
            "nic": "2x 10GbE SFP+ + 4x 1GbE RJ45",
            "oob": "iDRAC9 Enterprise (Dedicated Port, 172.16.10.100)"
        },
        hypervisor={"name": "K3s Edge Kubernetes Cluster on Ubuntu 22.04 LTS (輕量容器邊緣架構)", "ip": "172.16.10.10"},
        vms_pods=[
            {
                "name": "RDV-MES-EDGE (製造邊緣收發)", "type": "pod", "ip": "172.16.10.11",
                "os": "Alpine Linux Container", "resources": "8 vCPU / 24GB RAM",
                "services": [
                    {"proto": "TCP", "port": "1883", "name": "Eclipse Mosquitto (MQTT 代理)", "desc": "自動化裁床/吊掛機數據採集"},
                    {"proto": "TCP", "port": "8080", "name": "MES Edge Data Collector", "desc": "現場產線工單即時過站處理"},
                    {"proto": "TCP", "port": "5432", "name": "PostgreSQL 15 Local Cache", "desc": "跨國斷網時 72 小時離線暫存庫"},
                    {"proto": "TCP", "port": "80", "name": "現場工位看板 Web 服務", "desc": "提供產線大電視與平板儀表板"}
                ]
            },
            {
                "name": "RDV-AGENT-PROXY (同步中繼代理)", "type": "pod", "ip": "172.16.10.12",
                "os": "Alpine Linux Container", "resources": "4 vCPU / 16GB RAM",
                "services": [
                    {"proto": "TCP", "port": "50051", "name": "gRPC 邊緣高速通訊同步器", "desc": "壓縮增量回傳台北總部 D365"},
                    {"proto": "TCP", "port": "9100", "name": "Node Exporter 產線指標代理", "desc": "回傳總部 Prometheus 9090"}
                ]
            }
        ]
    )

    # =========================================================================
    # REGION 3: 柬埔寨柴楨廠 (Cambodia Svay Rieng RDG Plant Edge DC)
    # =========================================================================
    rdg_container_style = (
        "swimlane;html=1;whiteSpace=wrap;collapsible=0;recursiveResize=0;"
        "fillColor=#090d16;strokeColor=#f59e0b;strokeWidth=2;rounded=1;shadow=1;"
        "fontFamily=Arial;fontColor=#fcd34d;fontSize=15;fontStyle=1;startSize=34;"
        "swimlaneFillColor=#060a0f;"
    )
    rdg_title = "柬埔寨柴楨廠 (Cambodia RDG Plant Edge DC) ｜ 內網網段: 172.16.20.0/24"
    rdg_id, _ = add_cell(value=rdg_title, style=rdg_container_style, x=2320, y=830, w=1400, h=660)

    # RDG Firewall
    fg60f_id = draw_network_appliance(
        parent=rdg_id, x=20, y=45, w=1360, h=130,
        model_name="FortiGate 60F", role_name="RDG Edge Firewall & SD-WAN",
        ip="WAN1: 114.119.x.x (MPLS 50M) | WAN2: 124.248.x.x (Metfone 4G/FTTH) | LAN: 172.16.20.254",
        ports_info="IPsec VPN (UDP 500/4500) ↔ 台北 HQ Core 200F；自動切換 4G LTE 備援線路"
    )

    # RDG Server 1: RDG-EDGE-SRV01 (1U Dell PowerEdge R650xs)
    srv_rdg01_id = draw_realistic_server(
        parent=rdg_id, x=20, y=190, w=1360, h=440,
        model_name="Dell PowerEdge R650xs [RDG-EDGE-SRV01 - 柬埔寨邊緣主機]", form_factor="1U", serial="DELL-R650XS-KH01-EDGE",
        hw_spec={
            "cpu": "1x Intel Xeon Silver 4314 (16核/32緒, 2.4GHz)",
            "ram": "64GB ECC DDR4-3200 (4x 16GB)",
            "disk": "2x 960GB NVMe SSD (RAID 1 OS) + 2x 2.4TB SAS 10K (RAID 1 本地離線暫存庫)",
            "nic": "2x 10GbE SFP+ + 4x 1GbE RJ45",
            "oob": "iDRAC9 Enterprise (Dedicated Port, 172.16.20.100)"
        },
        hypervisor={"name": "K3s Edge Kubernetes Cluster on Ubuntu 22.04 LTS (輕量容器邊緣架構)", "ip": "172.16.20.10"},
        vms_pods=[
            {
                "name": "RDG-SEW-EDGE (車縫產線邊緣節點)", "type": "pod", "ip": "172.16.20.11",
                "os": "Alpine Linux Container", "resources": "8 vCPU / 24GB RAM",
                "services": [
                    {"proto": "TCP", "port": "1883", "name": "MQTT IoT Broker (車縫機聯網)", "desc": "即時監聽車縫計數傳感器"},
                    {"proto": "TCP", "port": "8080", "name": "RDG MES Workstation Gateway", "desc": "現場工票條碼掃描與驗證"},
                    {"proto": "TCP", "port": "5432", "name": "PostgreSQL 15 Local Cache", "desc": "柴楨廠斷網 72 小時離線暫存庫"},
                    {"proto": "TCP", "port": "80", "name": "產線效率即時電視牆 Dashboard", "desc": "呈現各生產線達成率與工時"}
                ]
            },
            {
                "name": "RDG-DATA-SYNC (數據定時同步器)", "type": "pod", "ip": "172.16.20.12",
                "os": "Alpine Linux Container", "resources": "4 vCPU / 16GB RAM",
                "services": [
                    {"proto": "TCP", "port": "50051", "name": "gRPC 邊緣數據壓縮傳輸服務", "desc": "專線閒置時段同步工單數據至 HQ"},
                    {"proto": "TCP", "port": "9100", "name": "Node Exporter 產線指標代理", "desc": "回傳總部 Prometheus 9090"}
                ]
            }
        ]
    )

    # =========================================================================
    # REGION 4: AWS 雲端混合算力 (AWS Asia-Pacific VPC - ap-east-1 香港)
    # =========================================================================
    aws_container_style = (
        "swimlane;html=1;whiteSpace=wrap;collapsible=0;recursiveResize=0;"
        "fillColor=#090d16;strokeColor=#f97316;strokeWidth=2;rounded=1;shadow=1;"
        "fontFamily=Arial;fontColor=#fdba74;fontSize=15;fontStyle=1;startSize=34;"
        "swimlaneFillColor=#060a0f;"
    )
    aws_title = "AWS 雲端混合運算節點 (AWS VPC - ap-east-1 香港) ｜ VPC CIDR: 10.200.0.0/16"
    aws_id, _ = add_cell(value=aws_title, style=aws_container_style, x=60, y=1690, w=3660, h=460)

    # AWS Transit Gateway / Virtual Private Gateway
    aws_vgw_id = draw_network_appliance(
        parent=aws_id, x=20, y=50, w=1060, h=130,
        model_name="AWS Virtual Private Gateway (VGW)", role_name="Site-to-Site IPsec VPN Gateway",
        ip="Tunnel 1: 52.82.x.x / Tunnel 2: 52.83.x.x (Active/Active BGP 179)",
        ports_info="雙路 IPsec VPN (UDP 500/4500) ↔ 台北 HQ Core FortiGate 200F；Direct Connect 備援就緒"
    )

    # AWS Cloud Server: AWS-GPU-INF01 (EC2 g5.xlarge GPU Instance)
    srv_aws01_id = draw_realistic_server(
        parent=aws_id, x=1100, y=50, w=2520, h=380,
        model_name="AWS EC2 g5.xlarge [AWS-GPU-INF01 - 雲端 AI 視覺打樣與跨國翻譯節點]", form_factor="1U", serial="AWS-NITRO-G5-XLARGE",
        hw_spec={
            "cpu": "4 vCPU (AMD EPYC 7R32, 3.3GHz 高效能運算核心)",
            "ram": "16GB DDR4 High-Speed Cloud RAM",
            "disk": "250GB gp3 NVMe Cloud SSD (3,000 IOPS / 125 MB/s 吞吐量)",
            "nic": "Up to 10 Gbps AWS Enhanced Networking (ENA)",
            "oob": "AWS Nitro System Security Enclave / AWS Systems Manager (SSM)"
        },
        hypervisor={"name": "AWS Nitro Hypervisor (Containerd / Docker 24.0 on Amazon Linux 2023)", "ip": "10.200.1.50"},
        vms_pods=[
            {
                "name": "AI 視覺打樣辨識推論容器 (AI Vision Sampling Engine)", "type": "pod", "ip": "10.200.1.51",
                "os": "PyTorch 2.1 + CUDA 12.1 + NVIDIA A10G (24GB VRAM)", "resources": "NVIDIA A10G Tensor Core GPU / 2 vCPU / 8GB RAM",
                "services": [
                    {"proto": "TCP", "port": "8000", "name": "FastAPI AI 視覺特徵比對服務", "desc": "樣品成衣車縫線瑕疵與紋理匹配推論"},
                    {"proto": "TCP", "port": "8501", "name": "Triton Inference Server", "desc": "跨國打樣 3D 視覺即時運算"},
                    {"proto": "TCP", "port": "443", "name": "HTTPS 加密推論端點", "desc": "僅允許台北 HQ RDSMP2 (192.168.0.22) 呼叫"}
                ]
            },
            {
                "name": "跨國工藝術語神經網絡翻譯引擎 (RSI Neural Translation)", "type": "pod", "ip": "10.200.1.52",
                "os": "HuggingFace Transformers + ONNX Runtime", "resources": "2 vCPU / 8GB RAM",
                "services": [
                    {"proto": "TCP", "port": "8080", "name": "REST API 術語翻譯微服務", "desc": "繁中 ↔ 越語 ↔ 高棉語工藝辭典即時互譯"},
                    {"proto": "TCP", "port": "9100", "name": "Prometheus Node Exporter", "desc": "推播 GPU/CPU 指標至總部 9090"}
                ]
            }
        ]
    )

    # =========================================================================
    # GLOBAL CONNECTIVITY LINKS (MPLS, IPsec VPN, SAN Fabric, High Speed LAN)
    # =========================================================================
    # 1. MPLS 專線雙軌: HQ Core FW <---> RDV FG80F
    add_edge(
        source_id=fg200f_id, target_id=fg80f_id,
        label="【MPLS 100Mbps 專線主通道】(台北 HQ ↔ 越南 RDV 延遲 < 35ms)",
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f43f5e;strokeWidth=3;fontColor=#fda4af;fontSize=10;dashed=1;",
        points=[(1100, 100), (2280, 100), (2280, 210), (2320, 210)]
    )

    # 2. IPsec VPN 備援通道: HQ Core FW <---> RDV FG80F
    add_edge(
        source_id=fg200f_id, target_id=fg80f_id,
        label="【IPsec VPN 備援通道 (IKEv2 / UDP 500, 4500)】",
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#38bdf8;strokeWidth=2.5;fontColor=#7dd3fc;fontSize=10;",
        points=[(1080, 130), (2260, 130), (2260, 240), (2320, 240)]
    )

    # 3. MPLS 專線: HQ Core FW <---> RDG FG60F
    add_edge(
        source_id=fg200f_id, target_id=fg60f_id,
        label="【MPLS 50Mbps 專線主通道】(台北 HQ ↔ 柬埔寨 RDG 延遲 < 45ms)",
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f43f5e;strokeWidth=3;fontColor=#fda4af;fontSize=10;dashed=1;",
        points=[(1060, 150), (2240, 150), (2240, 900), (2320, 900)]
    )

    # 4. IPsec VPN 備援: HQ Core FW <---> RDG FG60F
    add_edge(
        source_id=fg200f_id, target_id=fg60f_id,
        label="【IPsec VPN 備援通道 (IKEv2 / 4G LTE 備援)】",
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#38bdf8;strokeWidth=2.5;fontColor=#7dd3fc;fontSize=10;",
        points=[(1040, 170), (2220, 170), (2220, 930), (2320, 930)]
    )

    # 5. AWS Site-to-Site VPN: HQ Core FW <---> AWS VGW
    add_edge(
        source_id=fg200f_id, target_id=aws_vgw_id,
        label="【AWS Site-to-Site IPsec VPN (雙 Tunnel Active/Active BGP 179)】(台北 HQ ↔ AWS 香港 ap-east-1 延遲 < 22ms)",
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f97316;strokeWidth=3;fontColor=#fdba74;fontSize=10;",
        points=[(500, 190), (500, 1690)]
    )

    # 6. SAN Fabric: RSI-SRV-HQ03 (Baremetal SQL) <---> Dell Unity 480XT SAN
    add_edge(
        source_id=srv_hq03_id, target_id=san_hq_id,
        label="【雙路徑 10GbE iSCSI MPIO 高速存取 (Port 3260, Jumbo Frame 9000)】",
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#a855f7;strokeWidth=3;fontColor=#d8b4fe;fontSize=10;",
        points=[(550, 1060), (550, 1080)]
    )

    # 7. SAN Fabric: ESXi Cluster (HQ01/HQ02) <---> Dell Unity 480XT SAN
    add_edge(
        source_id=srv_hq01_id, target_id=san_hq_id,
        label="【VMFS 6 叢集共享資料庫掛載 (iSCSI Port 3260)】",
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#a855f7;strokeWidth=2;fontColor=#d8b4fe;fontSize=10;",
        points=[(300, 630), (300, 1080)]
    )

    # 8. 25GbE ToR Core Interconnect: S5248 Switch <---> Servers
    add_edge(
        source_id=s5248_id, target_id=srv_hq03_id,
        label="【2x 25GbE RoCE v2 RDMA 資料庫高速直連】",
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#10b981;strokeWidth=2.5;fontColor=#6ee7b7;fontSize=10;",
        points=[(1600, 190), (1600, 620), (1080, 720)]
    )

    # Generate XML string
    xml_str = ET.tostring(root, encoding="utf-8", method="xml").decode("utf-8")
    with open("/Users/howard/.hermes/cache/scratch/rsi_hardware_deployment.drawio", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str)

    print("Successfully generated /Users/howard/.hermes/cache/scratch/rsi_hardware_deployment.drawio")

if __name__ == "__main__":
    build_diagram()
