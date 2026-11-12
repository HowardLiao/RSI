# -*- coding: utf-8 -*-
import os

svg_path = "/Users/howard/.hermes/cache/scratch/rsi_hardware_deployment.svg"

# Let's generate a high-resolution SVG diagram (width 2600, height 1750)
svg = []
svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2600 1750" width="100%" height="100%" style="background:#090d16; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;">')

# Definitions & Filters
svg.append('''<defs>
  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
    <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.6"/>
  </filter>
  <linearGradient id="chassisGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#243044"/>
    <stop offset="50%" stop-color="#161f2e"/>
    <stop offset="100%" stop-color="#0f172a"/>
  </linearGradient>
  <linearGradient id="sanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#2a1f4e"/>
    <stop offset="100%" stop-color="#110d24"/>
  </linearGradient>
  <linearGradient id="bayGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#334155"/>
    <stop offset="100%" stop-color="#1e293b"/>
  </linearGradient>
  <linearGradient id="earGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#94a3b8"/>
    <stop offset="50%" stop-color="#64748b"/>
    <stop offset="100%" stop-color="#475569"/>
  </linearGradient>
  <pattern id="hexGrid" width="16" height="16" patternUnits="userSpaceOnUse">
    <path d="M 8 0 L 16 4.5 L 16 11.5 L 8 16 L 0 11.5 L 0 4.5 Z" fill="none" stroke="#1e293b" stroke-width="0.8"/>
  </pattern>
</defs>''')

# Background subtle grid
svg.append('<rect width="2600" height="1750" fill="url(#hexGrid)" opacity="0.4"/>')

# Diagram Header Banner
svg.append('''
<g transform="translate(40, 30)">
  <rect width="2520" height="72" rx="12" fill="#111827" stroke="#3b82f6" stroke-width="2" filter="url(#shadow)"/>
  <text x="30" y="38" fill="#f8fafc" font-size="22" font-weight="bold" letter-spacing="1">
    信源全球（RSI Group）Project Hive 全球混合雲實體硬體部署架構圖 (UML 2.0 Hardware Deployment)
  </text>
  <text x="30" y="58" fill="#94a3b8" font-size="12">
    核心節點：台北內湖總部 ｜ 越南同奈廠 (RDV) ｜ 柬埔寨柴楨廠 (RDG) ｜ AWS 雲端混合算力 ｜ 跨國 MPLS + IPsec VPN 雙軌備援拓撲
  </text>
  <!-- Legend inside banner -->
  <g transform="translate(1680, 20)">
    <circle cx="10" cy="14" r="5" fill="#10b981"/>
    <text x="22" y="18" fill="#cbd5e1" font-size="11">正常運作 / Link Active</text>
    <circle cx="160" cy="14" r="5" fill="#3b82f6"/>
    <text x="172" y="18" fill="#cbd5e1" font-size="11">System ID / iDRAC</text>
    <line x1="300" y1="14" x2="330" y2="14" stroke="#f43f5e" stroke-width="3" stroke-dasharray="4 3"/>
    <text x="338" y="18" fill="#fda4af" font-size="11">MPLS 專線</text>
    <line x1="430" y1="14" x2="460" y2="14" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="468" y="18" fill="#7dd3fc" font-size="11">IPsec VPN</text>
    <line x1="560" y1="14" x2="590" y2="14" stroke="#a855f7" stroke-width="2.5"/>
    <text x="598" y="18" fill="#d8b4fe" font-size="11">10G iSCSI SAN</text>
    <line x1="710" y1="14" x2="740" y2="14" stroke="#10b981" stroke-width="2.5"/>
    <text x="748" y="18" fill="#6ee7b7" font-size="11">25GbE RoCE</text>
  </g>
</g>
''')

# Helper: Draw Realistic 2U or 1U Rack Chassis
def draw_chassis_svg(x, y, w, h, u_type, model_badge, serial, drive_count, drive_label, drive_color="#10b981"):
    res = []
    # Outer Bezel
    res.append(f'<g transform="translate({x}, {y})">')
    res.append(f'<rect width="{w}" height="{h}" rx="6" fill="url(#chassisGrad)" stroke="#475569" stroke-width="2" filter="url(#shadow)"/>')
    
    # Left Ear
    res.append(f'<rect x="0" y="0" width="16" height="{h}" rx="2" fill="url(#earGrad)" stroke="#334155"/>')
    res.append(f'<circle cx="8" cy="10" r="3.5" fill="#0f172a" stroke="#1e293b"/>')
    res.append(f'<circle cx="8" cy="{h-10}" r="3.5" fill="#0f172a" stroke="#1e293b"/>')
    
    # Right Ear
    res.append(f'<rect x="{w-16}" y="0" width="16" height="{h}" rx="2" fill="url(#earGrad)" stroke="#334155"/>')
    res.append(f'<circle cx="{w-8}" cy="10" r="3.5" fill="#0f172a" stroke="#1e293b"/>')
    res.append(f'<circle cx="{w-8}" cy="{h-10}" r="3.5" fill="#0f172a" stroke="#1e293b"/>')
    
    # Control Panel
    ctrl_w = 64
    res.append(f'<rect x="22" y="6" width="{ctrl_w}" height="{h-12}" rx="3" fill="#0a0e17" stroke="#334155"/>')
    # Status LEDs
    res.append(f'<circle cx="34" cy="16" r="3" fill="#10b981" filter="drop-shadow(0 0 4px #10b981)"/>') # Power
    res.append(f'<circle cx="48" cy="16" r="3" fill="#3b82f6" filter="drop-shadow(0 0 4px #3b82f6)"/>') # ID
    res.append(f'<circle cx="62" cy="16" r="3" fill="#f59e0b"/>') # Activity
    # Badges
    res.append(f'<text x="54" y="{h-18}" fill="#f8fafc" font-size="8" font-weight="900" text-anchor="middle">DELL</text>')
    res.append(f'<text x="54" y="{h-8}" fill="#94a3b8" font-size="7" text-anchor="middle">{model_badge}</text>')
    
    # Drive Bays
    start_bx = 94
    avail_w = w - 94 - 170
    bay_w = int(avail_w / drive_count) - 4
    bay_h = h - 14
    for i in range(drive_count):
        bx = start_bx + i * (bay_w + 4)
        res.append(f'<rect x="{bx}" y="7" width="{bay_w}" height="{bay_h}" rx="3" fill="url(#bayGrad)" stroke="#475569" stroke-width="1"/>')
        # Latch
        res.append(f'<rect x="{bx+3}" y="{7+bay_h-8}" width="{bay_w-6}" height="5" rx="1.5" fill="#1e293b" stroke="#0f172a"/>')
        # Drive LED
        res.append(f'<circle cx="{bx+6}" cy="13" r="2" fill="{drive_color}"/>')
        res.append(f'<circle cx="{bx+13}" cy="13" r="2" fill="#0284c7"/>')
        # Text
        res.append(f'<text x="{bx + bay_w/2}" y="{7+bay_h/2+1}" fill="#cbd5e1" font-size="7" font-weight="bold" text-anchor="middle">{drive_label}</text>')
        res.append(f'<text x="{bx + bay_w/2}" y="{7+bay_h/2+9}" fill="#64748b" font-size="6" text-anchor="middle">BAY {i}</text>')

    # Rear/Right I/O & Dual PSUs
    rio_x = w - 165
    rio_w = 145
    res.append(f'<rect x="{rio_x}" y="6" width="{rio_w}" height="{h-12}" rx="3" fill="#0a0e17" stroke="#334155"/>')
    res.append(f'<text x="{rio_x+8}" y="19" fill="#38bdf8" font-size="8" font-weight="bold">PSU 1 &amp; 2: 1400W AC ●●</text>')
    res.append(f'<text x="{rio_x+8}" y="31" fill="#34d399" font-size="8" font-weight="bold">NIC: 4x 10G SFP+ / 2x 25G</text>')
    res.append(f'<text x="{rio_x+8}" y="{h-12}" fill="#fbbf24" font-size="7">iDRAC9 Ent. [{serial}]</text>')

    res.append('</g>')
    return "".join(res)

# =============================================================================
# REGION 1: 台北內湖總部 (HQ Data Center)
# =============================================================================
svg.append('''
<g transform="translate(40, 130)">
  <!-- Container Box -->
  <rect width="1580" height="1140" rx="10" fill="#0c1322" stroke="#3b82f6" stroke-width="2" filter="url(#shadow)"/>
  <rect width="1580" height="36" rx="10" fill="#1e293b"/>
  <text x="20" y="24" fill="#60a5fa" font-size="15" font-weight="bold">
    🏢 台北內湖總部核心機房 (Taipei Neihu HQ Data Center) ｜ IP 網段: 192.168.0.0/24 &amp; 10.10.0.0/16
  </text>
''')

# HQ Appliances: FortiGate 200F & Dell Switch S5248F
svg.append('''
  <!-- FortiGate 200F Core Firewall -->
  <g transform="translate(20, 50)">
    <rect width="750" height="76" rx="6" fill="#111827" stroke="#0284c7" stroke-width="1.5"/>
    <text x="16" y="24" fill="#38bdf8" font-size="12" font-weight="bold">«Core NGFW» FortiGate 200F (HQ SD-WAN Gateway)</text>
    <text x="16" y="44" fill="#cbd5e1" font-size="10">WAN1: 210.65.x.x (MPLS 100M) ｜ WAN2: 61.220.x.x (FTTB) ｜ LAN: 192.168.0.254</text>
    <text x="16" y="62" fill="#94a3b8" font-size="9">IPsec VPN (IKEv2 UDP 500/4500) ↔ 越南 RDV / 柬埔寨 RDG / AWS VPC ｜ BGP 179</text>
  </g>

  <!-- Dell PowerSwitch S5248F 25G Switch -->
  <g transform="translate(800, 50)">
    <rect width="760" height="76" rx="6" fill="#111827" stroke="#0284c7" stroke-width="1.5"/>
    <text x="16" y="24" fill="#38bdf8" font-size="12" font-weight="bold">«ToR Core Switch» Dell PowerSwitch S5248F-ON (25GbE VLT)</text>
    <text x="16" y="44" fill="#cbd5e1" font-size="10">48x 25GbE SFP28 + 4x 100GbE QSFP28 Uplink ｜ Mgmt IP: 10.10.99.1</text>
    <text x="16" y="62" fill="#94a3b8" font-size="9">支援 RoCE v2 RDMA 雙機高速直連、iSCSI 低延遲 Jumbo Frame 9000、VLAN 10/20/30/40</text>
  </g>
''')

# Server 1: RSI-SRV-HQ01 (Dell R760 2U)
svg.append(draw_chassis_svg(20, 140, 750, 74, "2U", "R760", "TW01", 8, "NVMe", "#10b981"))
svg.append('''
  <g transform="translate(20, 218)">
    <rect width="750" height="230" rx="6" fill="#131e33" stroke="#334155"/>
    <!-- Specs Banner -->
    <rect x="10" y="8" width="730" height="46" rx="4" fill="#1e293b"/>
    <text x="20" y="26" fill="#38bdf8" font-size="10" font-weight="bold">【硬體規格】RSI-SRV-HQ01 ｜ VMware ESXi 8.0 (192.168.0.21)</text>
    <text x="20" y="42" fill="#cbd5e1" font-size="9">CPU: 2x Xeon Gold 6430 (64核/128緒) ｜ RAM: 256GB ECC DDR5 ｜ Disk: 8x 1.92TB NVMe RAID10 (7.6TB)</text>
    
    <!-- VM 1: RDSMP2 -->
    <g transform="translate(10, 60)">
      <rect width="360" height="158" rx="4" fill="#0f2118" stroke="#10b981" stroke-width="1.2"/>
      <rect width="360" height="24" rx="4" fill="#064e3b"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«VM» RDSMP2 (192.168.0.22) ｜ 16 vCPU / 64GB</text>
      <text x="10" y="42" fill="#67e8f9" font-size="9" font-weight="bold">• TCP 80/443: <tspan fill="#f8fafc">IIS Web SAM 打樣系統</tspan></text>
      <text x="10" y="60" fill="#67e8f9" font-size="9" font-weight="bold">• TCP 1433: <tspan fill="#f8fafc">MS SQL Server (SAM 本地樣品庫)</tspan></text>
      <text x="10" y="78" fill="#67e8f9" font-size="9" font-weight="bold">• TCP 445: <tspan fill="#f8fafc">SMB/CIFS 打樣版單 CAD/PDF 儲存</tspan></text>
      <text x="10" y="96" fill="#67e8f9" font-size="9" font-weight="bold">• TCP 8000-8020: <tspan fill="#f8fafc">13 支同步批次排程服務</tspan></text>
      <text x="10" y="114" fill="#94a3b8" font-size="8">OS: Windows Server 2022 Std ｜ 核心服飾樣品庫與主檔</text>
    </g>

    <!-- VM 2: RDSMP1 -->
    <g transform="translate(380, 60)">
      <rect width="360" height="158" rx="4" fill="#1c1917" stroke="#f59e0b" stroke-width="1.2"/>
      <rect width="360" height="24" rx="4" fill="#78350f"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«VM» RDSMP1 (192.168.0.23) ｜ 16 vCPU / 64GB</text>
      <text x="10" y="42" fill="#fcd34d" font-size="9" font-weight="bold">• TCP 8012: <tspan fill="#f8fafc">IIS ARR 反向代理 &amp; SSL 卸載</tspan></text>
      <text x="10" y="60" fill="#fcd34d" font-size="9" font-weight="bold">• TCP 5000: <tspan fill="#f8fafc">.NET 8 CQS 微服務閘道</tspan></text>
      <text x="10" y="78" fill="#fcd34d" font-size="9" font-weight="bold">• TCP 9100: <tspan fill="#f8fafc">Prometheus Node Exporter 監控</tspan></text>
      <text x="10" y="96" fill="#fcd34d" font-size="9" font-weight="bold">• TCP 3389: <tspan fill="#f8fafc">RDP 安全跳板登入維運</tspan></text>
      <text x="10" y="114" fill="#94a3b8" font-size="8">OS: Windows Server 2022 Std ｜ 物料採購高併發查詢</text>
    </g>
  </g>
''')

# Server 2: RSI-SRV-HQ02 (Dell R760 2U)
svg.append(draw_chassis_svg(800, 140, 760, 74, "2U", "R760", "TW02", 8, "NVMe", "#10b981"))
svg.append('''
  <g transform="translate(800, 218)">
    <rect width="760" height="230" rx="6" fill="#131e33" stroke="#334155"/>
    <!-- Specs Banner -->
    <rect x="10" y="8" width="740" height="46" rx="4" fill="#1e293b"/>
    <text x="20" y="26" fill="#38bdf8" font-size="10" font-weight="bold">【硬體規格】RSI-SRV-HQ02 ｜ VMware ESXi 8.0 (192.168.0.25)</text>
    <text x="20" y="42" fill="#cbd5e1" font-size="9">CPU: 2x Xeon Gold 6430 (64核/128緒) ｜ RAM: 256GB ECC DDR5 ｜ Disk: 8x 1.92TB NVMe RAID10</text>
    
    <!-- VM 1: RSI-D365-AOS01 -->
    <g transform="translate(10, 60)">
      <rect width="365" height="158" rx="4" fill="#1c1917" stroke="#f59e0b" stroke-width="1.2"/>
      <rect width="365" height="24" rx="4" fill="#78350f"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«VM» RSI-D365-AOS01 (192.168.0.30) ｜ 24 vCPU / 96GB</text>
      <text x="10" y="42" fill="#fcd34d" font-size="9" font-weight="bold">• TCP 8101: <tspan fill="#f8fafc">Dynamics 365 AOS 交易服務實例 1</tspan></text>
      <text x="10" y="60" fill="#fcd34d" font-size="9" font-weight="bold">• TCP 8201: <tspan fill="#f8fafc">Dynamics 365 AOS 批次計算實例 2</tspan></text>
      <text x="10" y="78" fill="#fcd34d" font-size="9" font-weight="bold">• TCP 8088: <tspan fill="#f8fafc">D365 OData REST API 資料交換</tspan></text>
      <text x="10" y="96" fill="#fcd34d" font-size="9" font-weight="bold">• TCP 443: <tspan fill="#f8fafc">WCF 加密通訊端點</tspan></text>
      <text x="10" y="114" fill="#94a3b8" font-size="8">OS: Windows Server 2022 DC ｜ 跨國 ERP 交易核心</text>
    </g>

    <!-- VM 2: RSI-INT-GW01 -->
    <g transform="translate(385, 60)">
      <rect width="365" height="158" rx="4" fill="#0f172a" stroke="#3b82f6" stroke-width="1.2"/>
      <rect width="365" height="24" rx="4" fill="#1e3a8a"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«VM» RSI-INT-GW01 (192.168.0.35) ｜ 8 vCPU / 32GB</text>
      <text x="10" y="42" fill="#60a5fa" font-size="9" font-weight="bold">• TCP 5672/15672: <tspan fill="#f8fafc">RabbitMQ AMQP 消息中繼代理</tspan></text>
      <text x="10" y="60" fill="#60a5fa" font-size="9" font-weight="bold">• TCP 6379: <tspan fill="#f8fafc">Redis 7.0 分散式快取叢集</tspan></text>
      <text x="10" y="78" fill="#60a5fa" font-size="9" font-weight="bold">• TCP 8080: <tspan fill="#f8fafc">Celery 異步排程任務分派引擎</tspan></text>
      <text x="10" y="96" fill="#60a5fa" font-size="9" font-weight="bold">• TCP 9100: <tspan fill="#f8fafc">Node Exporter 系統指標採集</tspan></text>
      <text x="10" y="114" fill="#94a3b8" font-size="8">OS: Ubuntu 22.04 LTS ｜ 跨國排程事件廣播中台</text>
    </g>
  </g>
''')

# Server 3: RSI-SRV-HQ03 (Dell R760 2U Baremetal Database)
svg.append(draw_chassis_svg(20, 460, 750, 74, "2U", "R760 DB", "TW03", 8, "SAS SSD", "#f59e0b"))
svg.append('''
  <g transform="translate(20, 538)">
    <rect width="750" height="220" rx="6" fill="#131e33" stroke="#334155"/>
    <!-- Specs Banner -->
    <rect x="10" y="8" width="730" height="46" rx="4" fill="#1e293b"/>
    <text x="20" y="26" fill="#f59e0b" font-size="10" font-weight="bold">【裸機資料庫規格】RSI-SRV-HQ03 ｜ WSFC 裸機叢集 (192.168.0.10)</text>
    <text x="20" y="42" fill="#cbd5e1" font-size="9">CPU: 2x Xeon Gold 6430 (64核/128緒) ｜ RAM: 512GB ECC DDR5 ｜ Disk: 10x 3.84TB SAS SSD RAID10 (19.2TB)</text>
    
    <!-- Baremetal Instance -->
    <g transform="translate(10, 60)">
      <rect width="730" height="150" rx="4" fill="#1c1409" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="730" height="26" rx="4" fill="#78350f"/>
      <text x="14" y="18" fill="#fef08a" font-size="11" font-weight="bold">«Baremetal» rsiaxdb1 (MS SQL Server 2022 Enterprise AlwaysOn 核心營運庫)</text>
      
      <g transform="translate(14, 36)">
        <text x="0" y="16" fill="#fde047" font-size="10" font-weight="bold">• TCP 1433: <tspan fill="#f8fafc">MS SQL Server 2022 Enterprise 監聽埠 (Dynamics 365 AXDB 營運主庫)</tspan></text>
        <text x="0" y="34" fill="#fde047" font-size="10" font-weight="bold">• TCP 5022: <tspan fill="#f8fafc">SQL Server AlwaysOn Availability Group 高可用同步複寫端點</tspan></text>
        <text x="0" y="52" fill="#fde047" font-size="10" font-weight="bold">• TCP 1434: <tspan fill="#f8fafc">SQL Browser &amp; Dedicated Admin Connection (DAC 專用管理診斷埠)</tspan></text>
        <text x="0" y="70" fill="#fde047" font-size="10" font-weight="bold">• TCP 3260: <tspan fill="#f8fafc">iSCSI MPIO Initiator 多重路徑高速掛載 Dell Unity 480XT SAN 儲存陣列</tspan></text>
        <text x="0" y="90" fill="#94a3b8" font-size="9">OS: Windows Server 2022 Datacenter (WSFC 雙機鏡像) ｜ 2x 25GbE RoCE v2 RDMA 網路直連</text>
      </g>
    </g>
  </g>
''')

# Server 4: RSI-SRV-HQ04 (Dell R660 1U K8s Node)
svg.append(draw_chassis_svg(800, 460, 760, 56, "1U", "R660 K8s", "TW04", 6, "NVMe", "#10b981"))
svg.append('''
  <g transform="translate(800, 520)">
    <rect width="760" height="238" rx="6" fill="#131e33" stroke="#334155"/>
    <!-- Specs Banner -->
    <rect x="10" y="8" width="740" height="46" rx="4" fill="#1e293b"/>
    <text x="20" y="26" fill="#10b981" font-size="10" font-weight="bold">【K8s 節點規格】RSI-SRV-HQ04 ｜ Kubernetes v1.28 Master/Worker (192.168.0.50)</text>
    <text x="20" y="42" fill="#cbd5e1" font-size="9">CPU: 2x Xeon Silver 4410Y (24核/48緒) ｜ RAM: 128GB ECC DDR5 ｜ Disk: 4x 1.92TB NVMe RAID1</text>
    
    <!-- Pod 1 -->
    <g transform="translate(10, 60)">
      <rect width="365" height="166" rx="4" fill="#062820" stroke="#10b981" stroke-width="1.2"/>
      <rect width="365" height="24" rx="4" fill="#064e3b"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«Pod» Ingress &amp; API Gateway (192.168.0.51)</text>
      <text x="10" y="42" fill="#4ade80" font-size="9" font-weight="bold">• TCP 6443: <tspan fill="#f8fafc">Kubernetes API Server 主控埠</tspan></text>
      <text x="10" y="60" fill="#4ade80" font-size="9" font-weight="bold">• TCP 80/443: <tspan fill="#f8fafc">Envoy Ingress Gateway 反向代理</tspan></text>
      <text x="10" y="78" fill="#4ade80" font-size="9" font-weight="bold">• TCP 2379-2380: <tspan fill="#f8fafc">etcd 叢集狀態持久化儲存</tspan></text>
      <text x="10" y="96" fill="#94a3b8" font-size="8">8 vCPU / 32GB ｜ Cilium eBPF 高性能網路</text>
    </g>

    <!-- Pod 2 -->
    <g transform="translate(385, 60)">
      <rect width="365" height="166" rx="4" fill="#062820" stroke="#10b981" stroke-width="1.2"/>
      <rect width="365" height="24" rx="4" fill="#064e3b"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«Pod» Observability Stack (192.168.0.52)</text>
      <text x="10" y="42" fill="#4ade80" font-size="9" font-weight="bold">• TCP 9090: <tspan fill="#f8fafc">Prometheus TSDB 全球時序監控</tspan></text>
      <text x="10" y="60" fill="#4ade80" font-size="9" font-weight="bold">• TCP 3000: <tspan fill="#f8fafc">Grafana 跨國維運與產線戰情看板</tspan></text>
      <text x="10" y="78" fill="#4ade80" font-size="9" font-weight="bold">• TCP 24224: <tspan fill="#f8fafc">Fluentbit 跨國統一日誌採集代理</tspan></text>
      <text x="10" y="96" fill="#94a3b8" font-size="8">8 vCPU / 32GB ｜ 收集台北/越南/柬埔寨指標</text>
    </g>
  </g>
''')

# SAN Storage: Dell Unity 480XT All-Flash SAN
svg.append('''
  <!-- SAN Storage Section -->
  <g transform="translate(20, 770)">
    <rect width="1540" height="350" rx="8" fill="#110e24" stroke="#818cf8" stroke-width="2"/>
    <rect width="1540" height="32" rx="8" fill="#1e1b4b"/>
    <text x="20" y="22" fill="#c7d2fe" font-size="14" font-weight="bold">
      «SAN Storage» Dell Unity 480XT All-Flash 全快閃儲存陣列 (80TB 淨可用容量) ｜ S/N: DELL-UNITY-480XT-HQSAN
    </text>

    <!-- Physical SAN Chassis -->
    <g transform="translate(20, 44)">
      <rect width="1500" height="74" rx="6" fill="url(#sanGrad)" stroke="#6366f1" stroke-width="2"/>
      <!-- Ears -->
      <rect x="0" y="0" width="16" height="74" rx="2" fill="url(#earGrad)" stroke="#4338ca"/>
      <circle cx="8" cy="12" r="3.5" fill="#0f172a"/>
      <circle cx="8" cy="62" r="3.5" fill="#0f172a"/>
      <rect x="1484" y="0" width="16" height="74" rx="2" fill="url(#earGrad)" stroke="#4338ca"/>
      <circle cx="1492" cy="12" r="3.5" fill="#0f172a"/>
      <circle cx="1492" cy="62" r="3.5" fill="#0f172a"/>
      <!-- Badge -->
      <rect x="24" y="6" width="90" height="62" rx="4" fill="#0f0c24" stroke="#4338ca"/>
      <text x="69" y="32" fill="#a5b4fc" font-size="10" font-weight="900" text-anchor="middle">DELL EMC</text>
      <text x="69" y="48" fill="#818cf8" font-size="8" text-anchor="middle">Unity 480XT</text>
      <!-- Drive Slots (18 bays visual) -->
''')

# mini SAS bays
for di in range(20):
    dx = 125 + di * 56
    svg.append(f'''
      <g transform="translate({dx}, 6)">
        <rect width="52" height="62" rx="3" fill="#1e1b4b" stroke="#4338ca" stroke-width="1"/>
        <rect x="3" y="52" width="46" height="5" rx="1.5" fill="#312e81"/>
        <circle cx="8" cy="10" r="2" fill="#10b981"/>
        <text x="26" y="24" fill="#c7d2fe" font-size="7" font-weight="bold" text-anchor="middle">SAS SSD</text>
        <text x="26" y="36" fill="#818cf8" font-size="6" text-anchor="middle">#{di+1}</text>
      </g>
    ''')

svg.append('''
      <!-- Dual SP Controller Ports -->
      <g transform="translate(1260, 6)">
        <rect width="216" height="62" rx="4" fill="#0f0c24" stroke="#6366f1"/>
        <text x="10" y="20" fill="#a5b4fc" font-size="9" font-weight="bold">Dual SP-A / SP-B (Active/Active)</text>
        <text x="10" y="36" fill="#38bdf8" font-size="8">8x 10GbE SFP+ iSCSI (Port 3260)</text>
        <text x="10" y="50" fill="#a855f7" font-size="8">4x 16Gbps FC ｜ 0.3ms 極低延遲</text>
      </g>
    </g>

    <!-- Specs & LUN Mapping Box -->
    <g transform="translate(20, 126)">
      <rect width="1500" height="204" rx="6" fill="#18133b" stroke="#4338ca"/>
      <text x="16" y="24" fill="#c7d2fe" font-size="11" font-weight="bold">
        【全快閃儲存池 LUN 掛載拓撲與傳輸通道】25x 3.84TB SAS 12G Enterprise SSD (RAID 6 動態硬碟池 80TB 淨可用)
      </text>

      <!-- 4 LUN Cards -->
      <g transform="translate(16, 36)">
        <!-- LUN 1 -->
        <g transform="translate(0, 0)">
          <rect width="350" height="150" rx="4" fill="#241b52" stroke="#818cf8" stroke-width="1.2"/>
          <text x="12" y="22" fill="#f8fafc" font-size="11" font-weight="bold">LUN #01: LUN_D365_DATA (30TB)</text>
          <text x="12" y="44" fill="#cbd5e1" font-size="9">掛載主機: <tspan fill="#f59e0b" font-weight="bold">RSI-SRV-HQ03 (rsiaxdb1)</tspan></text>
          <text x="12" y="64" fill="#cbd5e1" font-size="9">傳輸協定: iSCSI MPIO (Port 3260, Jumbo Frame 9000)</text>
          <text x="12" y="84" fill="#cbd5e1" font-size="9">用途: Dynamics 365 核心營運庫 AXDB.mdf 資料檔</text>
          <text x="12" y="104" fill="#34d399" font-size="9">效能指標: 45,000 IOPS / 0.3ms 存取延遲</text>
        </g>
        <!-- LUN 2 -->
        <g transform="translate(370, 0)">
          <rect width="350" height="150" rx="4" fill="#241b52" stroke="#818cf8" stroke-width="1.2"/>
          <text x="12" y="22" fill="#f8fafc" font-size="11" font-weight="bold">LUN #02: LUN_D365_LOG (10TB)</text>
          <text x="12" y="44" fill="#cbd5e1" font-size="9">掛載主機: <tspan fill="#f59e0b" font-weight="bold">RSI-SRV-HQ03 (rsiaxdb1)</tspan></text>
          <text x="12" y="64" fill="#cbd5e1" font-size="9">傳輸協定: iSCSI MPIO (Port 3260, 雙路容錯)</text>
          <text x="12" y="84" fill="#cbd5e1" font-size="9">用途: MS SQL 交易日誌檔 AXDB_log.ldf 高速寫入</text>
          <text x="12" y="104" fill="#34d399" font-size="9">效能指標: RAID 10 鏡像模式寫入加速</text>
        </g>
        <!-- LUN 3 -->
        <g transform="translate(740, 0)">
          <rect width="350" height="150" rx="4" fill="#241b52" stroke="#818cf8" stroke-width="1.2"/>
          <text x="12" y="22" fill="#f8fafc" font-size="11" font-weight="bold">LUN #03: LUN_ESXI_VMFS01 (25TB)</text>
          <text x="12" y="44" fill="#cbd5e1" font-size="9">掛載主機: <tspan fill="#38bdf8" font-weight="bold">RSI-SRV-HQ01 / HQ02 叢集</tspan></text>
          <text x="12" y="64" fill="#cbd5e1" font-size="9">傳輸協定: iSCSI VMFS 6 叢集共享檔案系統</text>
          <text x="12" y="84" fill="#cbd5e1" font-size="9">用途: 虛擬機 VMDK 映像檔與快照集中儲存</text>
          <text x="12" y="104" fill="#34d399" font-size="9">功能: 支援 VMware vMotion / DRS 瞬態熱遷移</text>
        </g>
        <!-- LUN 4 -->
        <g transform="translate(1110, 0)">
          <rect width="350" height="150" rx="4" fill="#241b52" stroke="#818cf8" stroke-width="1.2"/>
          <text x="12" y="22" fill="#f8fafc" font-size="11" font-weight="bold">LUN #04: LUN_BACKUP_SNAP (15TB)</text>
          <text x="12" y="44" fill="#cbd5e1" font-size="9">掛載主機: <tspan fill="#a855f7" font-weight="bold">Veeam Backup / RSI-INT-GW01</tspan></text>
          <text x="12" y="64" fill="#cbd5e1" font-size="9">傳輸協定: iSCSI / NFS 雙協定共享</text>
          <text x="12" y="84" fill="#cbd5e1" font-size="9">用途: 硬體級儲存無感快照與跨國增量備份存放</text>
          <text x="12" y="104" fill="#34d399" font-size="9">策略: RPO &lt; 15 mins, RTO &lt; 30 mins</text>
        </g>
      </g>
    </g>
  </g>
</g>
''')

# =============================================================================
# REGION 2: 越南同奈廠 (Vietnam RDV Plant Edge DC)
# =============================================================================
svg.append('''
<g transform="translate(1660, 130)">
  <rect width="900" height="550" rx="10" fill="#0c1322" stroke="#10b981" stroke-width="2" filter="url(#shadow)"/>
  <rect width="900" height="36" rx="10" fill="#064e3b"/>
  <text x="20" y="24" fill="#a7f3d0" font-size="15" font-weight="bold">
    🏭 越南同奈廠 (Vietnam RDV Plant Edge DC) ｜ 內網網段: 172.16.10.0/24
  </text>
  
  <!-- FortiGate 80F -->
  <g transform="translate(20, 48)">
    <rect width="860" height="66" rx="6" fill="#111827" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="24" fill="#34d399" font-size="11" font-weight="bold">«Edge Firewall» FortiGate 80F (RDV SD-WAN Gateway)</text>
    <text x="16" y="42" fill="#cbd5e1" font-size="9">WAN1: 113.161.x.x (MPLS 100M) ｜ WAN2: 14.162.x.x (VNPT FTTB) ｜ LAN: 172.16.10.254</text>
    <text x="16" y="56" fill="#94a3b8" font-size="8">IPsec VPN (UDP 500/4500) ↔ 台北 HQ Core 200F ｜ SD-WAN 毫秒級自動線路容錯</text>
  </g>
''')

# RDV Server Chassis: RDV-EDGE-SRV01 (Dell R650xs 1U)
svg.append(draw_chassis_svg(20, 126, 860, 56, "1U", "R650xs", "VN01", 6, "SAS/SSD", "#10b981"))
svg.append('''
  <!-- RDV Software Stack -->
  <g transform="translate(20, 190)">
    <rect width="860" height="340" rx="6" fill="#131e33" stroke="#334155"/>
    <rect x="10" y="8" width="840" height="42" rx="4" fill="#1e293b"/>
    <text x="20" y="24" fill="#34d399" font-size="10" font-weight="bold">【硬體規格】RDV-EDGE-SRV01 ｜ K3s Edge Kubernetes (172.16.10.10)</text>
    <text x="20" y="38" fill="#cbd5e1" font-size="9">CPU: 1x Xeon Silver 4314 (16核/32緒) ｜ RAM: 64GB ECC DDR4 ｜ Disk: 2x 960GB NVMe + 2x 2.4TB SAS</text>

    <!-- Pod 1 -->
    <g transform="translate(10, 56)">
      <rect width="410" height="268" rx="4" fill="#062820" stroke="#10b981" stroke-width="1.2"/>
      <rect width="410" height="24" rx="4" fill="#064e3b"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«Pod» RDV-MES-EDGE (製造邊緣節點 172.16.10.11)</text>
      <g transform="translate(10, 34)">
        <text x="0" y="16" fill="#4ade80" font-size="9" font-weight="bold">• TCP 1883: <tspan fill="#f8fafc">Eclipse Mosquitto (MQTT 物聯網代理)</tspan></text>
        <text x="12" y="30" fill="#94a3b8" font-size="8">採集自動化裁床、吊掛機與車縫感測即時數據</text>
        
        <text x="0" y="52" fill="#4ade80" font-size="9" font-weight="bold">• TCP 8080: <tspan fill="#f8fafc">MES Edge Collector (工單過站引擎)</tspan></text>
        <text x="12" y="66" fill="#94a3b8" font-size="8">產線條碼掃描、工序驗證與良率即時計算</text>

        <text x="0" y="88" fill="#4ade80" font-size="9" font-weight="bold">• TCP 5432: <tspan fill="#f8fafc">PostgreSQL 15 Local Cache (離線緩衝庫)</tspan></text>
        <text x="12" y="102" fill="#94a3b8" font-size="8">跨國專線斷線時支援 72 小時全廠無感離線運作</text>

        <text x="0" y="124" fill="#4ade80" font-size="9" font-weight="bold">• TCP 80: <tspan fill="#f8fafc">現場工位看板 Web 服務 (產線大螢幕)</tspan></text>
        <text x="12" y="138" fill="#94a3b8" font-size="8">提供車間現場平板與電視牆即時效率展示</text>
      </g>
    </g>

    <!-- Pod 2 -->
    <g transform="translate(430, 56)">
      <rect width="420" height="268" rx="4" fill="#062820" stroke="#10b981" stroke-width="1.2"/>
      <rect width="420" height="24" rx="4" fill="#064e3b"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«Pod» RDV-AGENT-PROXY (跨國同步代理 172.16.10.12)</text>
      <g transform="translate(10, 34)">
        <text x="0" y="16" fill="#4ade80" font-size="9" font-weight="bold">• TCP 50051: <tspan fill="#f8fafc">gRPC 邊緣增量同步器 (回傳總部 D365)</tspan></text>
        <text x="12" y="30" fill="#94a3b8" font-size="8">專利微差量同步協議，專線頻寬佔用降低 85%</text>

        <text x="0" y="52" fill="#4ade80" font-size="9" font-weight="bold">• TCP 9100: <tspan fill="#f8fafc">Node Exporter 系統指標採集代理</tspan></text>
        <text x="12" y="66" fill="#94a3b8" font-size="8">定期回推 CPU/RAM/儲存負載至總部 Prometheus</text>

        <text x="0" y="88" fill="#4ade80" font-size="9" font-weight="bold">• TCP 22: <tspan fill="#f8fafc">SSH 安全管理通道 (僅限跳板機)</tspan></text>
        <text x="12" y="102" fill="#94a3b8" font-size="8">金鑰登入，禁用密碼與 Root 遠端登入</text>
      </g>
    </g>
  </g>
</g>
''')

# =============================================================================
# REGION 3: 柬埔寨柴楨廠 (Cambodia RDG Plant Edge DC)
# =============================================================================
svg.append('''
<g transform="translate(1660, 710)">
  <rect width="900" height="560" rx="10" fill="#0c1322" stroke="#f59e0b" stroke-width="2" filter="url(#shadow)"/>
  <rect width="900" height="36" rx="10" fill="#78350f"/>
  <text x="20" y="24" fill="#fde68a" font-size="15" font-weight="bold">
    🏭 柬埔寨柴楨廠 (Cambodia RDG Plant Edge DC) ｜ 內網網段: 172.16.20.0/24
  </text>
  
  <!-- FortiGate 60F -->
  <g transform="translate(20, 48)">
    <rect width="860" height="66" rx="6" fill="#111827" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="24" fill="#fcd34d" font-size="11" font-weight="bold">«Edge Firewall» FortiGate 60F (RDG SD-WAN Gateway)</text>
    <text x="16" y="42" fill="#cbd5e1" font-size="9">WAN1: 114.119.x.x (MPLS 50M) ｜ WAN2: 124.248.x.x (Metfone 4G/FTTH) ｜ LAN: 172.16.20.254</text>
    <text x="16" y="56" fill="#94a3b8" font-size="8">IPsec VPN (UDP 500/4500) ↔ 台北 HQ Core 200F ｜ 4G LTE 自動無感熱備援</text>
  </g>
''')

# RDG Server Chassis: RDG-EDGE-SRV01 (Dell R650xs 1U)
svg.append(draw_chassis_svg(20, 126, 860, 56, "1U", "R650xs", "KH01", 6, "SAS/SSD", "#f59e0b"))
svg.append('''
  <!-- RDG Software Stack -->
  <g transform="translate(20, 190)">
    <rect width="860" height="350" rx="6" fill="#131e33" stroke="#334155"/>
    <rect x="10" y="8" width="840" height="42" rx="4" fill="#1e293b"/>
    <text x="20" y="24" fill="#fcd34d" font-size="10" font-weight="bold">【硬體規格】RDG-EDGE-SRV01 ｜ K3s Edge Kubernetes (172.16.20.10)</text>
    <text x="20" y="38" fill="#cbd5e1" font-size="9">CPU: 1x Xeon Silver 4314 (16核/32緒) ｜ RAM: 64GB ECC DDR4 ｜ Disk: 2x 960GB NVMe + 2x 2.4TB SAS</text>

    <!-- Pod 1 -->
    <g transform="translate(10, 56)">
      <rect width="410" height="278" rx="4" fill="#1c1409" stroke="#f59e0b" stroke-width="1.2"/>
      <rect width="410" height="24" rx="4" fill="#78350f"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«Pod» RDG-SEW-EDGE (車縫產線邊緣 172.16.20.11)</text>
      <g transform="translate(10, 34)">
        <text x="0" y="16" fill="#fde047" font-size="9" font-weight="bold">• TCP 1883: <tspan fill="#f8fafc">MQTT IoT Broker (車縫機聯網代理)</tspan></text>
        <text x="12" y="30" fill="#94a3b8" font-size="8">柴楨廠車縫機台轉速、計數與斷線傳感器監聽</text>

        <text x="0" y="52" fill="#fde047" font-size="9" font-weight="bold">• TCP 8080: <tspan fill="#f8fafc">RDG MES Workstation Gateway</tspan></text>
        <text x="12" y="66" fill="#94a3b8" font-size="8">成衣工票過站條碼掃描與即時檢驗反饋</text>

        <text x="0" y="88" fill="#fde047" font-size="9" font-weight="bold">• TCP 5432: <tspan fill="#f8fafc">PostgreSQL 15 Local Cache (離線緩衝庫)</tspan></text>
        <text x="12" y="102" fill="#94a3b8" font-size="8">柴楨廠區 72 小時本機交易與物料數據暫存</text>

        <text x="0" y="124" fill="#fde047" font-size="9" font-weight="bold">• TCP 80: <tspan fill="#f8fafc">產線效率即時電視牆 Dashboard</tspan></text>
        <text x="12" y="138" fill="#94a3b8" font-size="8">呈現車縫線各組目標達成率與工時監控</text>
      </g>
    </g>

    <!-- Pod 2 -->
    <g transform="translate(430, 56)">
      <rect width="420" height="278" rx="4" fill="#1c1409" stroke="#f59e0b" stroke-width="1.2"/>
      <rect width="420" height="24" rx="4" fill="#78350f"/>
      <text x="10" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«Pod» RDG-DATA-SYNC (跨國同步代理 172.16.20.12)</text>
      <g transform="translate(10, 34)">
        <text x="0" y="16" fill="#fde047" font-size="9" font-weight="bold">• TCP 50051: <tspan fill="#f8fafc">gRPC 邊緣高速通訊同步器</tspan></text>
        <text x="12" y="30" fill="#94a3b8" font-size="8">夜間與離峰時段批量回傳產能報表至總部</text>

        <text x="0" y="52" fill="#fde047" font-size="9" font-weight="bold">• TCP 9100: <tspan fill="#f8fafc">Node Exporter 產線指標代理</tspan></text>
        <text x="12" y="66" fill="#94a3b8" font-size="8">回傳硬體與邊緣容器指標至總部 Prometheus</text>

        <text x="0" y="88" fill="#fde047" font-size="9" font-weight="bold">• TCP 22: <tspan fill="#f8fafc">SSH 管理通道 (堡壘機憑證存取)</tspan></text>
        <text x="12" y="102" fill="#94a3b8" font-size="8">嚴格隔離，禁止外部直接存取</text>
      </g>
    </g>
  </g>
</g>
''')

# =============================================================================
# REGION 4: AWS 雲端混合算力 (AWS Asia-Pacific VPC - ap-east-1 香港)
# =============================================================================
svg.append('''
<g transform="translate(40, 1300)">
  <rect width="2520" height="390" rx="10" fill="#0c1322" stroke="#f97316" stroke-width="2" filter="url(#shadow)"/>
  <rect width="2520" height="36" rx="10" fill="#7c2d12"/>
  <text x="20" y="24" fill="#fdba74" font-size="15" font-weight="bold">
    ☁️ AWS 雲端混合運算節點 (AWS VPC - ap-east-1 香港) ｜ VPC CIDR: 10.200.0.0/16
  </text>

  <!-- AWS VGW -->
  <g transform="translate(20, 50)">
    <rect width="680" height="74" rx="6" fill="#111827" stroke="#f97316" stroke-width="1.2"/>
    <text x="16" y="24" fill="#fb923c" font-size="11" font-weight="bold">«VPN Gateway» AWS Virtual Private Gateway (VGW)</text>
    <text x="16" y="42" fill="#cbd5e1" font-size="9">雙通道 Active/Active Site-to-Site IPsec VPN ｜ Tunnel 1: 52.82.x.x / Tunnel 2: 52.83.x.x</text>
    <text x="16" y="58" fill="#94a3b8" font-size="8">BGP ASN: 65000 ↔ 64512 (Port 179) ｜ 台北 HQ ↔ AWS 香港 ap-east-1 (延遲 &lt; 22ms)</text>
  </g>
''')

# AWS Cloud Server: AWS-GPU-INF01 (EC2 g5.xlarge)
svg.append(draw_chassis_svg(730, 50, 1770, 74, "1U", "AWS G5", "NITRO", 16, "gp3 SSD", "#f97316"))
svg.append('''
  <!-- AWS Instance Software Stack -->
  <g transform="translate(20, 134)">
    <rect width="2480" height="236" rx="6" fill="#131e33" stroke="#334155"/>
    <rect x="10" y="8" width="2460" height="42" rx="4" fill="#1e293b"/>
    <text x="20" y="24" fill="#fb923c" font-size="10" font-weight="bold">【雲端執行個體規格】AWS-GPU-INF01 (EC2 g5.xlarge) ｜ Private IP: 10.200.1.50</text>
    <text x="20" y="38" fill="#cbd5e1" font-size="9">CPU: 4 vCPU (AMD EPYC 7R32) ｜ RAM: 16GB ｜ GPU: NVIDIA A10G (24GB VRAM) ｜ Disk: 250GB gp3 NVMe Cloud SSD ｜ Nitro Enclave</text>

    <!-- Container 1 -->
    <g transform="translate(10, 56)">
      <rect width="1215" height="168" rx="4" fill="#1c0f07" stroke="#f97316" stroke-width="1.2"/>
      <rect width="1215" height="24" rx="4" fill="#7c2d12"/>
      <text x="12" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«Container» AI 視覺打樣辨識推論容器 (AI Vision Sampling Engine 10.200.1.51)</text>
      <g transform="translate(14, 34)">
        <text x="0" y="16" fill="#fdba74" font-size="10" font-weight="bold">• TCP 8000 / 443: <tspan fill="#f8fafc">FastAPI AI 視覺特徵比對微服務 (成衣瑕疵辨識、車縫線平整度評分)</tspan></text>
        <text x="0" y="36" fill="#fdba74" font-size="10" font-weight="bold">• TCP 8501: <tspan fill="#f8fafc">Triton Inference Server (跨國打樣 3D 視覺即時神經網絡推論)</tspan></text>
        <text x="0" y="56" fill="#94a3b8" font-size="9">環境: PyTorch 2.1 + CUDA 12.1 + NVIDIA A10G (24GB VRAM) ｜ 僅放行台北總部打樣伺服器 RDSMP2 呼叫</text>
        <text x="0" y="74" fill="#34d399" font-size="9">效能指標: 單件打樣成衣 3D 紋理特徵提取 &lt; 850ms</text>
      </g>
    </g>

    <!-- Container 2 -->
    <g transform="translate(1245, 56)">
      <rect width="1225" height="168" rx="4" fill="#1c0f07" stroke="#f97316" stroke-width="1.2"/>
      <rect width="1225" height="24" rx="4" fill="#7c2d12"/>
      <text x="12" y="16" fill="#f8fafc" font-size="10" font-weight="bold">«Container» 跨國工藝術語神經網絡翻譯引擎 (RSI Neural Translation 10.200.1.52)</text>
      <g transform="translate(14, 34)">
        <text x="0" y="16" fill="#fdba74" font-size="10" font-weight="bold">• TCP 8080: <tspan fill="#f8fafc">REST API 術語翻譯微服務 (繁中 ↔ 越南語 ↔ 高棉語車縫專門術語)</tspan></text>
        <text x="0" y="36" fill="#fdba74" font-size="10" font-weight="bold">• TCP 9100: <tspan fill="#f8fafc">Prometheus Node Exporter (GPU/CPU 負載指標定期推播回總部 9090)</tspan></text>
        <text x="0" y="56" fill="#94a3b8" font-size="9">技術棧: HuggingFace Transformers + ONNX Runtime ｜ 自動整合 RSI 私有成衣辭典</text>
        <text x="0" y="74" fill="#34d399" font-size="9">可用性: 雙向無縫轉譯版單備註與車縫要求，跨廠溝通零障礙</text>
      </g>
    </g>
  </g>
</g>
''')

# =============================================================================
# GLOBAL CONNECTIVITY LINES OVERLAY
# =============================================================================
svg.append('''
<!-- Network Connecting Lines -->
<!-- 1. MPLS HQ to RDV (Red Dashed) -->
<path d="M 790 195 L 1640 195 L 1640 210 L 1680 210" fill="none" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6 4"/>
<text x="1215" y="188" fill="#fda4af" font-size="10" font-weight="bold" text-anchor="middle">MPLS 100M 專線主通道 (延遲 &lt; 35ms)</text>

<!-- 2. IPsec VPN HQ to RDV (Blue Solid) -->
<path d="M 790 205 L 1625 205 L 1625 225 L 1680 225" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
<text x="1215" y="220" fill="#7dd3fc" font-size="9" text-anchor="middle">IPsec VPN 備援 (UDP 500/4500)</text>

<!-- 3. MPLS HQ to RDG (Red Dashed) -->
<path d="M 790 215 L 1610 215 L 1610 790 L 1680 790" fill="none" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6 4"/>
<text x="1450" y="782" fill="#fda4af" font-size="10" font-weight="bold">MPLS 50M 專線主通道 (延遲 &lt; 45ms)</text>

<!-- 4. IPsec VPN HQ to RDG (Blue Solid) -->
<path d="M 790 225 L 1595 225 L 1595 805 L 1680 805" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
<text x="1450" y="818" fill="#7dd3fc" font-size="9">IPsec VPN 備援 (UDP 500/4500)</text>

<!-- 5. AWS VPN HQ to AWS (Orange Solid) -->
<path d="M 400 256 L 400 1350" fill="none" stroke="#f97316" stroke-width="3"/>
<rect x="250" y="760" width="300" height="40" rx="4" fill="#0f172a" stroke="#f97316"/>
<text x="400" y="778" fill="#fdba74" font-size="9" font-weight="bold" text-anchor="middle">AWS Site-to-Site VPN (雙通道 Active/Active)</text>
<text x="400" y="792" fill="#cbd5e1" font-size="8" text-anchor="middle">BGP Port 179 ｜ 延遲 &lt; 22ms 台北 ↔ 香港</text>
''')

svg.append('</svg>')

with open(svg_path, "w", encoding="utf-8") as f:
    f.write("".join(svg))

print("Successfully generated high-res SVG deployment diagram at:", svg_path)
