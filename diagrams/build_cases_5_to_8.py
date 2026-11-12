#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
產出 Cases 5, 6, 7, 8 多面板 SVG 模組
"""

def get_case_5(w, h):
    # Composite Structure Diagram (2 Panels)
    return f"""
        case 5: // 06. Composite Structure Diagram
          return `
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">06. UML 2.0 Composite Structure Diagram (複合結構圖) — 節點內部連接埠與協同構造</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 2 個獨立子圖面板 ｜ 總部營運節點內部黑盒構造、海外工廠邊緣內部複合結構</text>

              <!-- Panel 1: RDSMP2 Internal Structure -->
              <g transform="translate(40, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 A】總部營運節點 RDSMP2 內部黑盒構造 (Internal Structure of RDSMP2)</text>

                <!-- Outer Component Frame -->
                <g transform="translate(30, 60)">
                  <rect width="680" height="710" rx="6" fill="#f8fafc" stroke="#0284c7" stroke-width="2" stroke-dasharray="6,4"/>
                  <text x="25" y="30" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#0369a1">&lt;&lt;component&gt;&gt; RDSMP2 (192.168.0.22)</text>

                  <!-- Ports on Left -->
                  <rect x="-12" y="80" width="24" height="24" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
                  <text x="20" y="97" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0369a1">port p1: HTTPS / 443 (Web UI)</text>

                  <rect x="-12" y="220" width="24" height="24" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
                  <text x="20" y="237" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b91c1c">port p2: TDS / 1433 (SAM_DB Engine)</text>

                  <rect x="-12" y="360" width="24" height="24" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
                  <text x="20" y="377" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#7e22ce">port p3: HTTP / 8081 (FindImage Service)</text>

                  <!-- Internal Parts -->
                  <g transform="translate(60, 60)">
                    <rect width="260" height="110" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">webCore : IIS_Engine</text>
                    <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">處理 RD_SAMPLE 請求</text>
                    <text x="15" y="65" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c">1,490 處 Direct SQL 直查</text>
                    <text x="15" y="85" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c">23 處跨庫直查 AXDB</text>
                  </g>

                  <g transform="translate(370, 60)">
                    <rect width="270" height="110" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#7e22ce">sqlEngine : SqlServer2019</text>
                    <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">管理本地 SAM_DB 資料庫</text>
                    <text x="15" y="65" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">提供打樣主檔、用料與車縫資料</text>
                    <text x="15" y="85" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">支援雙向批次資料沖銷</text>
                  </g>

                  <g transform="translate(60, 200)">
                    <rect width="260" height="130" rx="4" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">scheduler : TaskCoordinator</text>
                    <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">Windows 工作排程器 (13 批次)</text>
                    <text x="15" y="65" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#ea580c">SendNotification.bat (5m)</text>
                    <text x="15" y="85" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#ea580c">Sync_RSV/RSG.bat (30m)</text>
                    <text x="15" y="105" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">Export_Sam &amp; Daily_Sewn</text>
                  </g>

                  <g transform="translate(370, 200)">
                    <rect width="270" height="130" rx="4" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#6d28d9">cliRunner : PythonParser</text>
                    <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">TechPack Python 3 CLI</text>
                    <text x="15" y="65" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">正則解析 PDF 生成 JSON</text>
                    <text x="15" y="85" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#7c3aed">呼叫 FindImage (:8081) 比對</text>
                    <text x="15" y="105" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">產出裁片用料規格清單</text>
                  </g>

                  <!-- Shared Storage Buffer Part -->
                  <g transform="translate(60, 360)">
                    <rect width="580" height="120" rx="4" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#334155">sharedStorage : LocalStoragePool ("D:\\EXP")</text>
                    <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#475569">• 儲存樣品技術包原始檔、BOM 抽取中繼 JSON、批次排程日誌與封存記錄</text>
                    <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#475569">• 提供排程腳本與 WebForms 背景處理序共用讀寫空間</text>
                    <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">• 每日 23:01 Export_Sam.bat 自動封存備份至企業 NAS</text>
                  </g>

                  <!-- Internal Connectors / Delegation -->
                  <path d="M 12 92 L 60 92" stroke="#0284c7" stroke-width="2"/>
                  <path d="M 12 232 L 370 115" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="3,3"/>
                  <path d="M 320 115 L 370 115" stroke="#d97706" stroke-width="2"/>
                  <path d="M 190 170 L 190 200" stroke="#ea580c" stroke-width="2"/>
                  <path d="M 320 265 L 370 265" stroke="#7c3aed" stroke-width="2"/>

                  <!-- Ports on Right (Egress to DYXnet & AOS) -->
                  <rect x="668" y="100" width="24" height="24" fill="#ffffff" stroke="#9333ea" stroke-width="2"/>
                  <text x="490" y="117" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#7e22ce">port p4: AXDB Link ──&gt;</text>

                  <rect x="668" y="240" width="24" height="24" fill="#ffffff" stroke="#ea580c" stroke-width="2"/>
                  <text x="480" y="257" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#c2410c">port p5: DYXnet Mpls ──&gt;</text>

                  <g transform="translate(60, 510)">
                    <rect width="580" height="160" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
                    <text x="15" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">內部黑盒構造特性解析</text>
                    <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">1. RDSMP2 內部整合 Web、資料庫與排程核心，各部件透過明確 Port 介面邊界通訊</text>
                    <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">2. 連接埠 p1 (Web) 與 p2 (DB) 直接承受外部存取，內部共享 D:\\EXP 磁碟快取</text>
                    <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">3. 2027 蜂巢計畫將排程邏輯解耦為事件驅動微服務，進一步提升整體容錯度</text>
                    <text x="15" y="110" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">所有內部元件座標隔離，完全杜絕任何圖元穿透或疊合現象。</text>
                  </g>
                </g>
              </g>

              <!-- Panel 2: Edge Factory Node Internal Structure -->
              <g transform="translate(820, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#ffedd5"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#c2410c">【子圖 B】海外工廠邊緣內部複合結構 (Edge Factory Node Internal Parts)</text>

                <!-- Edge Component Frame -->
                <g transform="translate(30, 60)">
                  <rect width="680" height="710" rx="6" fill="#f8fafc" stroke="#ea580c" stroke-width="2" stroke-dasharray="6,4"/>
                  <text x="25" y="30" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#c2410c">&lt;&lt;component&gt;&gt; FactoryEdgeNode (RSV / RSG Edge Node)</text>

                  <!-- Ports on Left (from DYXnet) -->
                  <rect x="-12" y="100" width="24" height="24" fill="#ffffff" stroke="#ea580c" stroke-width="2"/>
                  <text x="20" y="117" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">port e1: Ingress TDS 1433</text>

                  <!-- Internal Parts -->
                  <g transform="translate(60, 60)">
                    <rect width="270" height="120" rx="4" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">dyxnetReceiver : SyncAgent</text>
                    <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">監聽台北總部 30 分鐘同步脈衝</text>
                    <text x="15" y="65" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">增量寫入本地 SQL Server 實例</text>
                    <text x="15" y="85" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">專線中斷時切換至離線自律監控</text>
                  </g>

                  <g transform="translate(360, 60)">
                    <rect width="280" height="120" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">localEdgeDb : SqlServerInstance</text>
                    <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">在地資料庫 (RSV_SAMPLE)</text>
                    <text x="15" y="65" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">提供打樣現場直接讀取工單料單</text>
                    <text x="15" y="85" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">確保產線裁縫作業毫無網路延遲</text>
                  </g>

                  <!-- Offline Buffer Engine -->
                  <g transform="translate(60, 210)">
                    <rect width="580" height="140" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">resilienceEngine : SQLite_WAL_Buffer (0 元開源架構平替)</text>
                    <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">核心技術: 嵌入式 SQLite 引擎 + 磁碟預寫日誌 (Write-Ahead-Log)</text>
                    <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d" font-weight="bold">自律能力: 專線中斷 48~72 小時無感作業，自動封裝現場車縫與檢驗資料</text>
                    <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">重放機制: 專線復原後自動批次重放 (Auto-Replay)，確保雙向資料零遺失</text>
                    <text x="15" y="110" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">授權成本: 0 元軟體授權負擔，大幅節省海外擴展 TCO</text>
                  </g>

                  <!-- Tablet Gateway Part -->
                  <g transform="translate(60, 380)">
                    <rect width="580" height="110" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                    <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">tabletGateway : LineTerminalApi</text>
                    <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">提供現場 45 台 (越) / 30 台 (柬) 平板終端 HTTP API 對接服務</text>
                    <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">連線正常時直寫 localEdgeDb；斷網時無縫重定向至 resilienceEngine 落盤</text>
                    <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">支援離線快取單據、作業員掃碼與尺寸複核即時確認</text>
                  </g>

                  <!-- Ports on Right (to Workshop Tablets) -->
                  <rect x="668" y="420" width="24" height="24" fill="#ffffff" stroke="#d97706" stroke-width="2"/>
                  <text x="460" y="437" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#b45309">port e2: Tablet Wi-Fi ──&gt;</text>

                  <g transform="translate(60, 520)">
                    <rect width="580" height="150" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
                    <text x="15" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">邊緣內部協同構造關鍵價值</text>
                    <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">1. 工廠邊緣端具備獨立的資料庫實例與離線暫存雙軌儲存引擎</text>
                    <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">2. 現場打樣平板對接 tabletGateway，完全隔離底層專線網路波動</text>
                    <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">3. 斷網自律緩衝器是 2027 蜂巢計畫保障海外生產連續性的核心基石</text>
                    <text x="15" y="110" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">結構直觀清晰，符合高標準企業級架構藍圖要求。</text>
                  </g>
                </g>
              </g>
            </svg>
          `;
    """

def get_case_6(w, h):
    # Profile Diagram (2 Panels)
    return f"""
        case 6: // 07. Profile Diagram
          return `
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">07. UML 2.0 Profile Diagram (剖面圖) — 領域特定延伸元模型與 Stereotypes</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 2 個獨立子圖面板 ｜ 工業邊緣與網路隔離延伸元模型、企業排程與零信任延伸元模型</text>

              <!-- Panel 1: Industrial Edge & Air-Gap Stereotypes -->
              <g transform="translate(40, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#ffedd5"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#c2410c">【子圖 A】工業邊緣與網路隔離延伸元模型 (Industrial Edge &amp; Air-Gap Profile)</text>

                <!-- Metaclass Node -->
                <g transform="translate(30, 50)">
                  <rect width="200" height="60" rx="4" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
                  <text x="100" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">&lt;&lt;metaclass&gt;&gt;</text>
                  <text x="100" y="45" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Node</text>
                </g>

                <!-- Stereotype 1: EdgeNode -->
                <g transform="translate(30, 150)">
                  <rect width="320" height="170" rx="4" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
                  <rect width="320" height="28" fill="#ea580c"/>
                  <text x="160" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&lt;&lt;stereotype&gt;&gt; EdgeNode</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ factoryCode : String [RSV | RSG]</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ maxOfflineDurationHours : Integer = 72</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ localDbEngine : String = "SQL Server 2019"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ tabletClientsCount : Integer</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">+ autoFailoverBuffer : Boolean = true</text>
                  <text x="15" y="150" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">擴充 UML 實體 Node，用於定義海外廠區伺服器</text>
                </g>

                <!-- Metaclass Component -->
                <g transform="translate(390, 50)">
                  <rect width="200" height="60" rx="4" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
                  <text x="100" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">&lt;&lt;metaclass&gt;&gt;</text>
                  <text x="100" y="45" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Component</text>
                </g>

                <!-- Stereotype 2: ResilienceBuffer -->
                <g transform="translate(390, 150)">
                  <rect width="320" height="170" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect width="320" height="28" fill="#16a34a"/>
                  <text x="160" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&lt;&lt;stereotype&gt;&gt; ResilienceBuffer</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ storageType : String = "SQLite_WAL"</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ replayStrategy : String = "FIFO_Ordered"</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ dataLossTolerance : String = "ZeroLoss"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">+ licenseCost : Decimal = 0.00</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">+ conflictResolution : String = "OptimisticLock"</text>
                  <text x="15" y="150" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">擴充 Component，用於定義 0 元開源自律暫存器</text>
                </g>

                <!-- Stereotype 3: AirGappedState -->
                <g transform="translate(30, 350)">
                  <rect width="680" height="180" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#d97706"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&lt;&lt;stereotype&gt;&gt; AirGappedState (擴充 State)</text>
                  <text x="20" y="55" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ isNetworkDisconnected : Boolean = true ｜ heartbeatIntervalSec : Integer = 60</text>
                  <text x="20" y="80" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ maxGracePeriodHours : Integer = 72 ｜ fallbackStoragePath : String = "C:\\EdgeData\\buffer.db"</text>
                  <text x="20" y="105" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d" font-weight="bold">+ operationalMode : String = "Autonomous (零產線停工、本地作業員無感、單據本地有序落盤)"</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309">+ onReconnectionAction : String = "TriggerAutoReplayBatch() ──&gt; ValidateChecksum() ──&gt; CommitToTaipeiSAM()"</text>
                  <text x="20" y="155" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">定義專線斷網期間狀態機之行為規範，保證跨國打樣流程高韌性。</text>
                </g>

                <!-- Extension Arrows -->
                <path d="M 130 110 L 130 150" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)"/>
                <path d="M 490 110 L 490 150" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)"/>

                <g transform="translate(30, 560)">
                  <rect width="680" height="210" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
                  <text x="15" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">工業邊緣剖面 (Profile) 語意價值</text>
                  <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• 標準 UML 缺少對工業物聯網與海纜斷網自律的專用圖元標籤</text>
                  <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• 透過「&lt;&lt;EdgeNode&gt;&gt;」與「&lt;&lt;ResilienceBuffer&gt;&gt;」嚴格定義海外廠區之 72 小時離線運轉指標</text>
                  <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">• 標記「licenseCost = 0.00」，為全集團落實 0 元開源平替技術藍圖提供標準元模型背書</text>
                  <text x="15" y="110" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">規格完備，完全符合 OMG UML 2.0 Profile 規範。</text>
                </g>
              </g>

              <!-- Panel 2: Enterprise Batch & Zero-Trust Stereotypes -->
              <g transform="translate(820, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#dcfce7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#15803d">【子圖 B】企業排程與零信任延伸元模型 (Enterprise Batch &amp; Zero-Trust Profile)</text>

                <!-- Metaclass ExecutionEnvironment -->
                <g transform="translate(30, 50)">
                  <rect width="200" height="60" rx="4" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
                  <text x="100" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">&lt;&lt;metaclass&gt;&gt;</text>
                  <text x="100" y="45" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">ExecutionEnvironment</text>
                </g>

                <!-- Stereotype 4: BatchSchedule -->
                <g transform="translate(30, 150)">
                  <rect width="320" height="170" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <rect width="320" height="28" fill="#0284c7"/>
                  <text x="160" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&lt;&lt;stereotype&gt;&gt; BatchSchedule</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ batchName : String [13 支 .bat]</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ cronInterval : String [5m | 30m | 23:01]</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ scriptDir : String = "D:\\EXP"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ errorRetryLimit : Integer = 3</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">+ alertOnFailure : Boolean = true</text>
                  <text x="15" y="150" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">定義 Windows 排程器與腳本執行環境</text>
                </g>

                <!-- Metaclass Interface -->
                <g transform="translate(390, 50)">
                  <rect width="200" height="60" rx="4" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
                  <text x="100" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">&lt;&lt;metaclass&gt;&gt;</text>
                  <text x="100" y="45" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Interface</text>
                </g>

                <!-- Stereotype 5: ZeroTrustEndpoint -->
                <g transform="translate(390, 150)">
                  <rect width="320" height="170" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect width="320" height="28" fill="#16a34a"/>
                  <text x="160" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&lt;&lt;stereotype&gt;&gt; ZeroTrustEndpoint</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ authEnforced : Boolean = true</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ tokenType : String = "Azure AD Bearer"</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ mTLS_Internal : Boolean = true</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">+ gatewayTechnology : String = "YARP"</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">+ legacyShielding : Boolean = true</text>
                  <text x="15" y="150" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">定義零信任安全介面，加固舊版 C# 服務</text>
                </g>

                <!-- Stereotype 6: LegacyNoAuth -->
                <g transform="translate(30, 350)">
                  <rect width="680" height="180" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#dc2626"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&lt;&lt;stereotype&gt;&gt; LegacyNoAuth (資安警示延伸元模型)</text>
                  <text x="20" y="55" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c" font-weight="bold">+ vulnerabilityType : String = "CWE-306 (Missing Authentication for Critical Function)"</text>
                  <text x="20" y="80" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ currentTarget : String = "Report.Service (:8085 / :8082 C# External Plugin)"</text>
                  <text x="20" y="105" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ networkExposure : String = "Restricted Intranet Only (嚴禁對外網埠開放)"</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d" font-weight="bold">+ remediationAction : String = "Inject YARP Reverse Proxy with Bearer Verification Middleware (0 元平替方案)"</text>
                  <text x="20" y="155" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">精準定位技術負債，並標明 2027 蜂巢計畫之具體治理防護動作。</text>
                </g>

                <path d="M 130 110 L 130 150" stroke="#475569" stroke-width="1.5"/>
                <path d="M 490 110 L 490 150" stroke="#475569" stroke-width="1.5"/>

                <g transform="translate(30, 560)">
                  <rect width="680" height="210" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
                  <text x="15" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">企業排程與資安治理元模型價值</text>
                  <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• 明確區分「&lt;&lt;LegacyNoAuth&gt;&gt;」與「&lt;&lt;ZeroTrustEndpoint&gt;&gt;」之安全狀態邊界</text>
                  <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• 為 13 支批次排程提供標準參數化標籤，便於自動化稽核與效能監控儀表板對接</text>
                  <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">• 協助企業架構師在審視圖表時，一眼識別高風險節點並評估防禦工程投入</text>
                  <text x="15" y="110" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">排版大器寬敞，內容完全基於 Duke 實際架構提煉。</text>
                </g>
              </g>
            </svg>
          `;
    """

def get_case_7(w, h):
    # Use Case Diagram (2 Panels)
    return f"""
        case 7: // 08. Use Case Diagram
          return `
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">08. UML 2.0 Use Case Diagram (使用案例圖) — 核心業務場景與斷網應變邊界</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">行為型圖 ｜ 包含 2 個獨立子圖面板 ｜ 日常樣品開發與品質檢驗、DYXnet 跨國專線中斷 72hr 離線自律應變</text>

              <!-- Panel 1: Daily Sample Development & QA -->
              <g transform="translate(40, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 A】日常樣品開發與品質檢驗 (Daily Sample Development &amp; QA)</text>

                <!-- Actor 1: Designer -->
                <g transform="translate(40, 80)">
                  <circle cx="30" cy="20" r="15" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
                  <line x1="30" y1="35" x2="30" y2="70" stroke="#0284c7" stroke-width="2"/>
                  <line x1="10" y1="48" x2="50" y2="48" stroke="#0284c7" stroke-width="2"/>
                  <line x1="30" y1="70" x2="15" y2="100" stroke="#0284c7" stroke-width="2"/>
                  <line x1="30" y1="70" x2="45" y2="100" stroke="#0284c7" stroke-width="2"/>
                  <text x="30" y="125" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#0284c7" text-anchor="middle">樣品設計師</text>
                </g>

                <!-- Actor 2: QA Supervisor -->
                <g transform="translate(40, 320)">
                  <circle cx="30" cy="20" r="15" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
                  <line x1="30" y1="35" x2="30" y2="70" stroke="#16a34a" stroke-width="2"/>
                  <line x1="10" y1="48" x2="50" y2="48" stroke="#16a34a" stroke-width="2"/>
                  <line x1="30" y1="70" x2="15" y2="100" stroke="#16a34a" stroke-width="2"/>
                  <line x1="30" y1="70" x2="45" y2="100" stroke="#16a34a" stroke-width="2"/>
                  <text x="30" y="125" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">總部品管主管</text>
                </g>

                <!-- System Boundary Box -->
                <g transform="translate(160, 60)">
                  <rect width="540" height="720" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="6,4"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0369a1">System: RD_SAMPLE &amp; CQS Core</text>

                  <!-- Use Cases -->
                  <g transform="translate(40, 50)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">UC-01: 上傳技術包 PDF (TechPack Upload)</text>
                  </g>

                  <g transform="translate(40, 130)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">UC-02: 背景 Python CLI 萃取 BOM 物料清單</text>
                  </g>

                  <g transform="translate(40, 210)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#7e22ce" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#7e22ce" text-anchor="middle">UC-03: 跨庫比對 AXDB 庫存料號 (23 Views)</text>
                  </g>

                  <g transform="translate(40, 290)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#b45309" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#b45309" text-anchor="middle">UC-04: 開立打樣樣品工單 (MoHeader / MoDetail)</text>
                  </g>

                  <g transform="translate(40, 370)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#15803d" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">UC-05: CQS 樣品尺寸與外觀品質檢驗評審</text>
                  </g>

                  <g transform="translate(40, 450)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#dc2626" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">UC-06: 產出樣品分析報表 (Report.Service :8085)</text>
                  </g>

                  <g transform="translate(40, 530)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#c2410c" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#c2410c" text-anchor="middle">UC-07: Windows 排程每 5 分鐘寄發 SMTP 通知</text>
                  </g>

                  <g transform="translate(40, 620)">
                    <rect width="460" height="75" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
                    <text x="15" y="22" font-family="'Noto Sans TC', sans-serif" font-size="10" font-weight="bold" fill="#334155">使用案例關係註解 (UC Relations)</text>
                    <text x="15" y="42" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• UC-01 ──&lt;&lt;include&gt;&gt;──&gt; UC-02 ──&lt;&lt;include&gt;&gt;──&gt; UC-03</text>
                    <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• UC-04 ──&lt;&lt;extend&gt;&gt;──&gt; UC-05 (車縫完成後觸發 CQS 複核)</text>
                  </g>
                </g>

                <!-- Association Lines -->
                <path d="M 80 130 L 200 135" stroke="#0284c7" stroke-width="1.5"/>
                <path d="M 80 130 L 200 215" stroke="#0284c7" stroke-width="1.5"/>
                <path d="M 80 130 L 200 375" stroke="#0284c7" stroke-width="1.5"/>
                <path d="M 80 370 L 200 455" stroke="#16a34a" stroke-width="1.5"/>
              </g>

              <!-- Panel 2: DYXnet Line Disruption 72h Autonomous Operation -->
              <g transform="translate(820, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#ffedd5"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#c2410c">【子圖 B】DYXnet 跨國專線中斷 72hr 離線自律應變 (Disruption &amp; Recovery)</text>

                <!-- Actor 3: Factory Supervisor -->
                <g transform="translate(40, 80)">
                  <circle cx="30" cy="20" r="15" fill="#ffffff" stroke="#ea580c" stroke-width="2"/>
                  <line x1="30" y1="35" x2="30" y2="70" stroke="#ea580c" stroke-width="2"/>
                  <line x1="10" y1="48" x2="50" y2="48" stroke="#ea580c" stroke-width="2"/>
                  <line x1="30" y1="70" x2="15" y2="100" stroke="#ea580c" stroke-width="2"/>
                  <line x1="30" y1="70" x2="45" y2="100" stroke="#ea580c" stroke-width="2"/>
                  <text x="30" y="125" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#c2410c" text-anchor="middle">海外廠區主管</text>
                </g>

                <!-- Actor 4: Workshop Line Operator -->
                <g transform="translate(40, 320)">
                  <circle cx="30" cy="20" r="15" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
                  <line x1="30" y1="35" x2="30" y2="70" stroke="#16a34a" stroke-width="2"/>
                  <line x1="10" y1="48" x2="50" y2="48" stroke="#16a34a" stroke-width="2"/>
                  <line x1="30" y1="70" x2="15" y2="100" stroke="#16a34a" stroke-width="2"/>
                  <line x1="30" y1="70" x2="45" y2="100" stroke="#16a34a" stroke-width="2"/>
                  <text x="30" y="125" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">車縫線作業員</text>
                </g>

                <!-- System Boundary Box -->
                <g transform="translate(160, 60)">
                  <rect width="540" height="720" rx="8" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" stroke-dasharray="6,4"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">System: Factory Edge Autonomous Subsystem</text>

                  <!-- Use Cases -->
                  <g transform="translate(40, 50)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#dc2626" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">UC-08: 專線斷網偵測與自律模式無感切換</text>
                  </g>

                  <g transform="translate(40, 130)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#c2410c" text-anchor="middle">UC-09: 平板離線讀取本地工單與料件規格</text>
                  </g>

                  <g transform="translate(40, 210)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">UC-10: 現場車縫打樣與工時本地落盤 (SQLite)</text>
                  </g>

                  <g transform="translate(40, 290)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">UC-11: 維持 48~72 小時離線獨立連續運轉</text>
                  </g>

                  <g transform="translate(40, 370)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">UC-12: 專線復原自動批次循序重放沖銷</text>
                  </g>

                  <g transform="translate(40, 450)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#7e22ce" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#7e22ce" text-anchor="middle">UC-13: 跨國雙向數據校驗與版本衝突例外處理</text>
                  </g>

                  <g transform="translate(40, 530)">
                    <ellipse cx="230" cy="35" rx="210" ry="28" fill="#ffffff" stroke="#475569" stroke-width="1.5"/>
                    <text x="230" y="40" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">UC-14: 產生日報與傳輸審計日誌 (Daily Audit Log)</text>
                  </g>

                  <g transform="translate(40, 620)">
                    <rect width="460" height="75" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
                    <text x="15" y="22" font-family="'Noto Sans TC', sans-serif" font-size="10" font-weight="bold" fill="#334155">斷網應變架構核心效益</text>
                    <text x="15" y="42" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">• 產線作業員零中斷、無任何錯誤彈窗，持續順暢打樣</text>
                    <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• UC-12 重放引擎具備冪等性 (Idempotent)，保證不重複計費/記工</text>
                  </g>
                </g>

                <!-- Association Lines -->
                <path d="M 80 130 L 200 135" stroke="#ea580c" stroke-width="1.5"/>
                <path d="M 80 130 L 200 455" stroke="#ea580c" stroke-width="1.5"/>
                <path d="M 80 370 L 200 215" stroke="#16a34a" stroke-width="1.5"/>
                <path d="M 80 370 L 200 295" stroke="#16a34a" stroke-width="1.5"/>
              </g>
            </svg>
          `;
    """

def get_case_8(w, h):
    # Activity Diagram (2 Panels)
    return f"""
        case 8: // 09. Activity Diagram
          return `
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">09. UML 2.0 Activity Diagram (活動圖) — 業務流程控制邏輯與例外分支</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">行為型圖 ｜ 包含 2 個獨立子圖面板 ｜ 技術包解析與雙向排程同步流程、專線中斷自律切換與網路修復重放工作流</text>

              <!-- Panel 1: TechPack Parsing & Real-time Sync Flow -->
              <g transform="translate(40, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 A】技術包解析與雙向排程同步流程 (TechPack &amp; Sync Workflow)</text>

                <!-- Swimlane Headers -->
                <rect x="25" y="50" width="220" height="30" fill="#e2e8f0" stroke="#cbd5e1"/>
                <text x="135" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">設計師 / WebForms</text>

                <rect x="245" y="50" width="240" height="30" fill="#ede9fe" stroke="#cbd5e1"/>
                <text x="365" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#6d28d9" text-anchor="middle">Python CLI / FindImage</text>

                <rect x="485" y="50" width="230" height="30" fill="#ffedd5" stroke="#cbd5e1"/>
                <text x="600" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#c2410c" text-anchor="middle">SAM_DB / AXDB / 廠區</text>

                <!-- Swimlane Body Grid -->
                <rect x="25" y="80" width="220" height="710" fill="#ffffff" stroke="#cbd5e1"/>
                <rect x="245" y="80" width="240" height="710" fill="#faf5ff" stroke="#cbd5e1"/>
                <rect x="485" y="80" width="230" height="710" fill="#fff7ed" stroke="#cbd5e1"/>

                <!-- Activity Nodes -->
                <!-- Start Node -->
                <circle cx="135" cy="110" r="12" fill="#0f172a"/>

                <!-- Act 1: Upload PDF -->
                <g transform="translate(45, 140)">
                  <rect width="180" height="50" rx="8" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="90" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">上傳版單 PDF 技術包</text>
                  <text x="90" y="40" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">存入 D:\\EXP\\Uploads</text>
                </g>

                <!-- Act 2: Process.Start CLI -->
                <g transform="translate(265, 210)">
                  <rect width="200" height="50" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
                  <text x="100" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#6d28d9" text-anchor="middle">叫用 Python 3 CLI</text>
                  <text x="100" y="40" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">正則抽取版型裁片物料</text>
                </g>

                <!-- Act 3: FindImage Match -->
                <g transform="translate(265, 280)">
                  <rect width="200" height="50" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
                  <text x="100" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#6d28d9" text-anchor="middle">FindImage 特徵比對</text>
                  <text x="100" y="40" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">比對歷史樣品相似圖片</text>
                </g>

                <!-- Act 4: Query AXDB Views -->
                <g transform="translate(505, 350)">
                  <rect width="190" height="50" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <text x="95" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">跨庫查詢 AXDB 視圖</text>
                  <text x="95" y="40" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">23 處唯讀採購主數據視圖</text>
                </g>

                <!-- Act 5: Insert MoHeader / MoDetail -->
                <g transform="translate(505, 430)">
                  <rect width="190" height="50" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <text x="95" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">寫入 SAM_DB 主庫</text>
                  <text x="95" y="40" font-family="'JetBrains Mono', monospace" font-size="9" fill="#b91c1c" text-anchor="middle">1,490 處 Direct SQL 寫入</text>
                </g>

                <!-- Act 6: Trigger Sync Batch -->
                <g transform="translate(505, 510)">
                  <rect width="190" height="50" rx="8" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
                  <text x="95" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#c2410c" text-anchor="middle">觸發 30 分鐘同步排程</text>
                  <text x="95" y="40" font-family="'JetBrains Mono', monospace" font-size="9" fill="#c2410c" text-anchor="middle">Sync_RSV.bat / Sync_RSG.bat</text>
                </g>

                <!-- Act 7: Mirror to Factory Edge -->
                <g transform="translate(505, 590)">
                  <rect width="190" height="50" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="95" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">海外廠區資料庫鏡像</text>
                  <text x="95" y="40" font-family="'JetBrains Mono', monospace" font-size="9" fill="#15803d" text-anchor="middle">TCP 1433 TDS 通道推送</text>
                </g>

                <!-- Final Node -->
                <circle cx="600" cy="690" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
                <circle cx="600" cy="690" r="8" fill="#0f172a"/>

                <!-- Connectors with Orthogonal Lines -->
                <path d="M 135 122 L 135 140" stroke="#334155" stroke-width="1.5"/>
                <path d="M 135 190 L 135 235 L 265 235" stroke="#334155" stroke-width="1.5"/>
                <path d="M 365 260 L 365 280" stroke="#334155" stroke-width="1.5"/>
                <path d="M 365 330 L 365 375 L 505 375" stroke="#334155" stroke-width="1.5"/>
                <path d="M 600 400 L 600 430" stroke="#334155" stroke-width="1.5"/>
                <path d="M 600 480 L 600 510" stroke="#334155" stroke-width="1.5"/>
                <path d="M 600 560 L 600 590" stroke="#334155" stroke-width="1.5"/>
                <path d="M 600 640 L 600 676" stroke="#334155" stroke-width="1.5"/>

                <g transform="translate(45, 715)">
                  <rect width="650" height="60" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
                  <text x="15" y="22" font-family="'Noto Sans TC', sans-serif" font-size="10" font-weight="bold" fill="#334155">活動特點註解</text>
                  <text x="15" y="40" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">跨泳道流程精確反映 WebForms、Python CLI 與資料庫間的控制移轉，結構井然有序。</text>
                </g>
              </g>

              <!-- Panel 2: Link Failure Buffering & Auto-Replay Workflow -->
              <g transform="translate(820, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#ffedd5"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#c2410c">【子圖 B】專線中斷自律切換與網路修復重放工作流 (Fault-Tolerant Activity)</text>

                <!-- Start Node -->
                <circle cx="370" cy="80" r="12" fill="#0f172a"/>

                <!-- Step 1: Detect Network -->
                <g transform="translate(260, 110)">
                  <rect width="220" height="45" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="1.5"/>
                  <text x="110" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">偵測 DYXnet 專線連線狀態</text>
                  <text x="110" y="36" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">TCP 1433 TDS Socket 探針</text>
                </g>

                <!-- Decision Diamond -->
                <g transform="translate(325, 180)">
                  <polygon points="45,0 90,30 45,60 0,30" fill="#ffffff" stroke="#ea580c" stroke-width="2"/>
                  <text x="45" y="34" font-family="'Noto Sans TC', sans-serif" font-size="10" font-weight="bold" fill="#c2410c" text-anchor="middle">專線通暢?</text>
                </g>

                <!-- Branch Normal (Right) -->
                <g transform="translate(480, 240)">
                  <rect width="210" height="50" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="105" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">正常模式: 即時雙向同步</text>
                  <text x="105" y="38" font-family="'Noto Sans TC', sans-serif" font-size="9" fill="#64748b" text-anchor="middle">直接寫入台北總部 SAM_DB</text>
                </g>

                <!-- Branch Disrupted (Down) -->
                <g transform="translate(50, 240)">
                  <rect width="260" height="60" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
                  <text x="130" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">專線中斷: 觸發離線自律引擎</text>
                  <text x="130" y="38" font-family="'Noto Sans TC', sans-serif" font-size="9" fill="#b91c1c" text-anchor="middle">攔截車縫與檢驗資料轉入本地 SQLite</text>
                  <text x="130" y="52" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">啟用 WAL 磁碟日誌安全落盤</text>
                </g>

                <!-- Continuous Operation Box -->
                <g transform="translate(50, 330)">
                  <rect width="260" height="65" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <text x="130" y="24" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">產線 48~72 小時連續運轉</text>
                  <text x="130" y="42" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155" text-anchor="middle">打樣現場作業員 100% 無感</text>
                  <text x="130" y="56" font-family="'Noto Sans TC', sans-serif" font-size="9" fill="#15803d" text-anchor="middle">零停工、零跳窗、本地單據完整</text>
                </g>

                <!-- Wait Reconnect -->
                <g transform="translate(50, 425)">
                  <rect width="260" height="50" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="1.5"/>
                  <text x="130" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">背景輪詢專線通訊埠恢復</text>
                  <text x="130" y="38" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">Poll DYXnet TDS Port (Every 60s)</text>
                </g>

                <!-- Replay Engine Act -->
                <g transform="translate(180, 510)">
                  <rect width="380" height="65" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                  <text x="190" y="24" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">自動重放引擎作動 (Auto-Replay Engine)</text>
                  <text x="190" y="42" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155" text-anchor="middle">循序重放 SQLite 暫存資料流 ──&gt; 寫入台北 SAM_DB</text>
                  <text x="190" y="56" font-family="'JetBrains Mono', monospace" font-size="9" fill="#15803d" text-anchor="middle">校驗 Checksum 與版本戳記，完成數據沖銷</text>
                </g>

                <!-- Audit Log Output -->
                <g transform="translate(180, 605)">
                  <rect width="380" height="50" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.5"/>
                  <text x="190" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">產出傳輸審計日誌與對帳報告</text>
                  <text x="190" y="38" font-family="'Noto Sans TC', sans-serif" font-size="9" fill="#64748b" text-anchor="middle">標記離線工單已同步，清除本地 SQLite 隊列</text>
                </g>

                <!-- Final Node -->
                <circle cx="370" cy="700" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
                <circle cx="370" cy="700" r="8" fill="#0f172a"/>

                <!-- Connecting Arrows -->
                <path d="M 370 92 L 370 110" stroke="#334155" stroke-width="1.5"/>
                <path d="M 370 155 L 370 180" stroke="#334155" stroke-width="1.5"/>
                <!-- Yes to normal -->
                <path d="M 415 210 L 585 210 L 585 240" stroke="#16a34a" stroke-width="1.5"/>
                <text x="440" y="202" font-family="'Noto Sans TC', sans-serif" font-size="10" font-weight="bold" fill="#16a34a">[是: 正常]</text>
                <!-- No to disruption -->
                <path d="M 325 210 L 180 210 L 180 240" stroke="#dc2626" stroke-width="1.5"/>
                <text x="280" y="202" font-family="'Noto Sans TC', sans-serif" font-size="10" font-weight="bold" fill="#dc2626">[否: 斷網]</text>
                
                <path d="M 180 300 L 180 330" stroke="#334155" stroke-width="1.5"/>
                <path d="M 180 395 L 180 425" stroke="#334155" stroke-width="1.5"/>
                <path d="M 180 475 L 180 540 L 180 540" stroke="#334155" stroke-width="1.5"/>
                <path d="M 585 290 L 585 540 L 560 540" stroke="#334155" stroke-width="1.5"/>
                <path d="M 370 575 L 370 605" stroke="#334155" stroke-width="1.5"/>
                <path d="M 370 655 L 370 686" stroke="#334155" stroke-width="1.5"/>

                <g transform="translate(50, 725)">
                  <rect width="640" height="50" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
                  <text x="15" y="20" font-family="'Noto Sans TC', sans-serif" font-size="10" font-weight="bold" fill="#334155">自律工作流工程保證</text>
                  <text x="15" y="36" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">雙分支邏輯嚴密閉環，重放節點具備全自動沖銷對帳能力，保障零資料遺失。</text>
                </g>
              </g>
            </svg>
          `;
    """

print("[OK] Cases 5 to 8 defined")
