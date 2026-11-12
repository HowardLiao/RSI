#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
產出完整 14 組專業 UML 2.0 原生多面板 (Multi-Panel) SVG 模組
包含 Case 3 到 Case 13，每張圖皆劃分 2~3 個獨立面板，尺寸統一為 1600 x 950。
"""

def get_case_3(w, h):
    # Package Diagram (3 Panels)
    return f"""
        case 3: // 04. Package Diagram
          return `
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">04. UML 2.0 Package Diagram (套件圖) — 模組依賴與分層邊界</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 3 個獨立子圖面板 ｜ 總部核心套件、D365 C# 整合套件、海外自律邊緣套件</text>

              <!-- Panel 1: Taipei HQ Core Packages -->
              <g transform="translate(40, 90)">
                <rect width="480" height="820" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
                <rect width="480" height="35" rx="8" fill="#fef3c7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#b45309">【子圖 A】台北總部地端核心套件 (Taipei Core Packages)</text>

                <!-- Pkg 1 -->
                <g transform="translate(20, 50)">
                  <path d="M 0 15 L 0 0 L 120 0 L 135 15 L 440 15 L 440 160 L 0 160 Z" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#b45309">RD_Sample.Web</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">&lt;&lt;package&gt;&gt; RD_Sample.Web</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ WebForms.Controllers (.aspx / .cs)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ SampleDataModels (MoHeader, MoDetail)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">+ DirectSqlHelpers (1,490 處 SAM 直連 SQL)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">+ AxDbViewQueries (23 處跨庫直查 AXDB)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">部署於 RDSMP2 (192.168.0.22) IIS 10.0</text>
                </g>

                <!-- Pkg 2 -->
                <g transform="translate(20, 230)">
                  <path d="M 0 15 L 0 0 L 140 0 L 155 15 L 440 15 L 440 160 L 0 160 Z" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#15803d">CQS.QualityService</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;package&gt;&gt; CQS.QualityService</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ QualityInspectionContracts (DTO 模型)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ KestrelControllers (.NET 8 WebApi)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">+ ArrProxyReverseGateway (Port :8012 轉發 :8011)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ MetricCollector (車縫瑕疵分析儀)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">部署於 RDSMP1 (192.168.0.23)</text>
                </g>

                <!-- Pkg 3 -->
                <g transform="translate(20, 410)">
                  <path d="M 0 15 L 0 0 L 130 0 L 145 15 L 440 15 L 440 160 L 0 160 Z" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#6d28d9">TechPack.Parser</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#6d28d9">&lt;&lt;package&gt;&gt; TechPack.Parser.Cli</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ PythonCliWrapper (Process.Start 封裝)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ PdfBOMExtractor (Python 3 文本正則萃取)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ JsonOutputParser (結構化裁片物料轉換)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#6d28d9" font-weight="bold">+ FindImageServiceClient (Port :8081 特徵匹配)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">執行於 RDSMP2 本地環境 (D:\\EXP 共享目錄)</text>
                </g>

                <!-- Dependencies -->
                <g transform="translate(20, 590)">
                  <rect width="440" height="200" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
                  <text x="15" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#475569">套件依賴與邊界規則 (Dependencies)</text>
                  <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">1. RD_Sample.Web ──「use」──&gt; TechPack.Parser.Cli</text>
                  <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">2. RD_Sample.Web ──「access」──&gt; CQS.QualityService</text>
                  <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c">3. 依賴痛點：WebForms 與資料庫緊密耦合 (無 Repository 層)</text>
                  <text x="15" y="110" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">4. 蜂巢改善：規劃導入 Mediator 模式隔絕 Direct SQL</text>
                  <text x="15" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">所有套件均經由內網 1Gbps 專用交換機連通</text>
                </g>
              </g>

              <!-- Panel 2: D365 C# Integration Packages -->
              <g transform="translate(540, 90)">
                <rect width="490" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="490" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 B】D365 C# 整合套件群 (D365 Middleware)</text>

                <!-- Pkg 4 -->
                <g transform="translate(20, 50)">
                  <path d="M 0 15 L 0 0 L 150 0 L 165 15 L 450 15 L 450 170 L 0 170 Z" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#b91c1c">D365.ReportService</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b91c1c">&lt;&lt;package&gt;&gt; D365.ReportService</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ ExternalReportPlugin (C# 外掛模組)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ ExcelStreamingEngine (12 支報表產出匯出)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">+ NoAuthPolicyHandler (內部信任無驗證通道)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ RqtBaseFormBinder (請求物件轉換器)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">執行節點: RSIMDW1 (:8085 正式 / :8082 測試)</text>
                </g>

                <!-- Pkg 5 -->
                <g transform="translate(20, 240)">
                  <path d="M 0 15 L 0 0 L 140 0 L 155 15 L 450 15 L 450 170 L 0 170 Z" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#0369a1">D365.LocalWebApi</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0369a1">&lt;&lt;package&gt;&gt; D365.LocalWebApi</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ JCOM_WebServices (15 個業務模組)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ RSI_WebServices (16 個供應鏈模組)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">+ AzureAdBearerAuthFilter (JWT 認證過濾器)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#0369a1">+ OperationDispatchTable (80 項 Operations 路由)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">執行節點: RSIMDW1 (:80 正式 / :8081 測試)</text>
                </g>

                <!-- Pkg 6 -->
                <g transform="translate(20, 430)">
                  <path d="M 0 15 L 0 0 L 140 0 L 155 15 L 450 15 L 450 170 L 0 170 Z" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#7e22ce">D365.AXDB.Views</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#7e22ce">&lt;&lt;package&gt;&gt; D365.AXDB.Views</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ VendPurchOrderView (全球採購單查詢視圖)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ InventItemMasterView (料件規格主檔視圖)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#7e22ce" font-weight="bold">+ ReadOnlyCrossDbSchemas (23 個跨庫唯讀視圖)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ AlwaysOnReplicaListener (可用性群組唯讀節點)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">宿主資料庫: rsiaxdb1 (192.168.0.131:1433)</text>
                </g>

                <!-- Integration Note -->
                <g transform="translate(20, 620)">
                  <rect width="450" height="170" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
                  <text x="15" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#475569">D365 整合邊界說明</text>
                  <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• Report.Service 與 Local.WebApi 均為 100% C# 實作</text>
                  <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">• 所有 80 項 Operations 統一由 RqtBaseForm 與 RSI_RT 包裝</text>
                  <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c">• Report.Service 缺乏認證，由 2027 蜂巢 YARP 進行代理補強</text>
                  <text x="15" y="110" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">封裝架構清晰，為未來微服務拆分提供穩健基礎</text>
                </g>
              </g>

              <!-- Panel 3: Factory Edge Packages -->
              <g transform="translate(1050, 90)">
                <rect width="510" height="820" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
                <rect width="510" height="35" rx="8" fill="#dcfce7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#15803d">【子圖 C】DYXnet 跨國專線與海外自律套件 (Factory Edge)</text>

                <!-- Pkg 7 -->
                <g transform="translate(20, 50)">
                  <path d="M 0 15 L 0 0 L 150 0 L 165 15 L 470 15 L 470 170 L 0 170 Z" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#c2410c">WinBatch.Schedulers</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">&lt;&lt;package&gt;&gt; WinBatch.Schedulers</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ HighFreqTasks (SendNotification.bat 5分鐘)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ CrossBorderSyncTasks (Sync_RSV.bat, Sync_RSG.bat)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#c2410c" font-weight="bold">+ NightlyArchiveTasks (Export_Sam.bat, Daily_Sewn)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ BatchTaskWatcher (執行狀態監視與日誌輪替)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">執行宿主: RDSMP2 Windows 工作排程器 (D:\\EXP)</text>
                </g>

                <!-- Pkg 8 -->
                <g transform="translate(20, 240)">
                  <path d="M 0 15 L 0 0 L 140 0 L 155 15 L 470 15 L 470 170 L 0 170 Z" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#15803d">Factory.EdgeSync</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;package&gt;&gt; Factory.EdgeSync</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ RsvSyncListener (越南廠 192.168.185.123 接收端)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ RsgSyncListener (柬埔寨廠 192.168.193.65 接收端)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">+ DyxnetTdsChannel (跨國專線 TCP 1433 資料通道)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ DifferentialDataMerger (差集增量合併模組)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">運作週期: 每 30 分鐘自動同步一次</text>
                </g>

                <!-- Pkg 9 -->
                <g transform="translate(20, 430)">
                  <path d="M 0 15 L 0 0 L 160 0 L 175 15 L 470 15 L 470 170 L 0 170 Z" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="15" y="12" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#15803d">Offline.ResilienceBuffer</text>
                  <text x="20" y="40" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;package&gt;&gt; Offline.ResilienceBuffer</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ SQLiteLocalQueueStore (嵌入式 SQLite WAL 暫存)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">+ AutonomousProductionEngine (48~72hr 離線運轉模組)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ AutoReplayCoordinator (專線復原循序重放引擎)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">+ ConflictResolver (版本號與樂觀鎖例外對帳器)</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">部署於各廠區邊緣伺服器 (0 元開源架構平替)</text>
                </g>

                <!-- Resilience Note -->
                <g transform="translate(20, 620)">
                  <rect width="470" height="170" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
                  <text x="15" y="25" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#475569">廠區自律連續性架構價值</text>
                  <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">1. 專線斷網時自動接管車縫與檢驗資料落盤</text>
                  <text x="15" y="70" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">2. 現場作業員與平板端機 100% 無感，持續打樣作業</text>
                  <text x="15" y="90" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#334155">3. 網路恢復後自動重播佇列，資料零丟失</text>
                  <text x="15" y="110" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">徹底消除因海外海纜中斷造成的產線停工風險</text>
                </g>
              </g>
            </svg>
          `;
    """

def get_case_4(w, h):
    # Object Diagram (2 Panels)
    return f"""
        case 4: // 05. Object Diagram
          return `
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">05. UML 2.0 Object Diagram (物件圖) — 執行時期實例狀態與記憶體快照</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 2 個獨立子圖面板 ｜ 總部機房營運實例群、海外廠區離線自律實例群</text>

              <!-- Panel 1: Taipei HQ Runtime Instances -->
              <g transform="translate(40, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 A】台北總部機房營運物件實例 (Taipei HQ Runtime Instances)</text>

                <!-- Instance 1 -->
                <g transform="translate(25, 50)">
                  <rect width="330" height="170" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <rect width="330" height="28" fill="#0284c7"/>
                  <text x="165" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle" text-decoration="underline">rdsmp2_server : WinServer2019</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">ipv4 = "192.168.0.22"</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">status = "Operational"</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">cpuUsage = "14.2%"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">ramUsage = "38.5 GB / 64 GB"</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">activeJobs = 13 (Windows Scheduler)</text>
                  <text x="15" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">expStoragePath = "D:\\EXP"</text>
                </g>

                <!-- Instance 2 -->
                <g transform="translate(385, 50)">
                  <rect width="330" height="170" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect width="330" height="28" fill="#d97706"/>
                  <text x="165" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle" text-decoration="underline">sample_web : IIS_Site</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">siteName = "RD_SAMPLE"</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">port = 443 / 80</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">appPool = "Clr4Integrated"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c" font-weight="bold">directSqlRefs = 1490</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c" font-weight="bold">axDbViewRefs = 23</text>
                  <text x="15" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">activeSessions = 42</text>
                </g>

                <!-- Instance 3 -->
                <g transform="translate(25, 240)">
                  <rect width="330" height="170" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect width="330" height="28" fill="#16a34a"/>
                  <text x="165" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle" text-decoration="underline">arr_proxy : IIS_ARR</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">listenPort = 8012</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">targetBackend = "192.168.0.23:8011"</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">proxyState = "Forwarding"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">activeHttpSockets = 18</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">targetService = "CQS.KestrelCore"</text>
                  <text x="15" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">runNode = "RDSMP1 (192.168.0.23)"</text>
                </g>

                <!-- Instance 4 -->
                <g transform="translate(385, 240)">
                  <rect width="330" height="170" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect width="330" height="28" fill="#16a34a"/>
                  <text x="165" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle" text-decoration="underline">cqs_svc : DotNet8Kestrel</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">listenPort = 8011 (Localhost)</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">framework = ".NET 8 Core"</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">threadPoolThreads = 64</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">inspectedSamplesToday = 318</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">defectDetectedRate = "2.1%"</text>
                  <text x="15" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">dbState = "Healthy (SAM_DB Pool)"</text>
                </g>

                <!-- Instance 5 -->
                <g transform="translate(25, 430)">
                  <rect width="330" height="170" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
                  <rect width="330" height="28" fill="#dc2626"/>
                  <text x="165" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle" text-decoration="underline">report_svc : D365Plugin</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">node = "RSIMDW1 (192.168.0.95)"</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">listenPort = 8085 (Prod)</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c" font-weight="bold">authMechanism = "None (No Auth)"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">excelReportsSupported = 12</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">baseRequestContract = "RqtBaseForm"</text>
                  <text x="15" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">targetReplacement = "YARP Bearer Gateway"</text>
                </g>

                <!-- Instance 6 -->
                <g transform="translate(385, 430)">
                  <rect width="330" height="170" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <rect width="330" height="28" fill="#9333ea"/>
                  <text x="165" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle" text-decoration="underline">axdb_cluster : SqlAlwaysOn</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">clusterIp = "192.168.0.131:1433"</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">aosNodes = [".124", ".125", ".126"]</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#7e22ce">syncMode = "Synchronous Commit"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">openConnections = 142</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">crossDbViewsActive = 23</text>
                  <text x="15" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">readOnlyRouting = "Enabled"</text>
                </g>

                <!-- Instance 7 -->
                <g transform="translate(25, 620)">
                  <rect width="690" height="170" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
                  <text x="20" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0f172a" text-decoration="underline">coordinator : BatchScheduleCoordinator</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">activeJobs: [ "SendNotification.bat (5m)", "Sync_RSV.bat (30m)", "Sync_RSG.bat (30m)", "Export_Sam.bat (23:01)", "Daily_Sewn.bat (23:31)" ]</text>
                  <text x="20" y="80" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">lastGlobalSyncTimestamp = "2026-11-12 21:30:00 CST" ｜ dyxnetPulseStatus = "Optimal (Ping 42ms)"</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">failoverFallback = "Local SQLite Transaction Buffer Activated on Socket Timeout &gt; 5000ms"</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">總部物件實例均處於高可用正常運行狀態，監控指標齊全。</text>
                </g>
              </g>

              <!-- Panel 2: Overseas Factory Offline Autonomous Instances -->
              <g transform="translate(820, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#ffedd5"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#c2410c">【子圖 B】海外廠區離線自律物件實例 (Factory Edge Instances)</text>

                <!-- Factory RSV -->
                <g transform="translate(25, 50)">
                  <rect width="690" height="240" rx="4" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
                  <rect width="690" height="28" fill="#ea580c"/>
                  <text x="345" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle" text-decoration="underline">rsv_edge_node : IndustrialEdgeServer</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">siteLocation = "Vietnam Dong Nai Factory (RDV)"</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">ipv4 = "192.168.185.123" ｜ sqlPort = 1433 (RSV_SAMPLE)</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">connectedTablets = 45 units (Line Operator Tablets)</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d" font-weight="bold">linkStatus = "Online_Synchronized (DYXnet MPLS 45ms)"</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">lastBatchReceived = "Sync_RSV.bat (21:30 CST, 84 records synced)"</text>
                  <text x="20" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">embeddedBuffer = "SQLite3 WAL (Local C:\\EdgeData\\rsv_buffer.db)"</text>
                  <text x="20" y="170" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">queuedPendingTransactions = 0 (All Synced)</text>
                  <text x="20" y="190" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">maxAutonomousHours = 72 hours</text>
                  <text x="20" y="210" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">越南廠產線連線正常，打樣料件與工單即時鏡像中。</text>
                </g>

                <!-- Factory RSG (Simulating Link Failure Resilience) -->
                <g transform="translate(25, 310)">
                  <rect width="690" height="260" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
                  <rect width="690" height="28" fill="#dc2626"/>
                  <text x="345" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle" text-decoration="underline">rsg_edge_node : IndustrialEdgeServer [SIMULATING AIR-GAPPED]</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">siteLocation = "Cambodia Svay Rieng Factory (RDG)"</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">ipv4 = "192.168.193.65" ｜ sqlPort = 1433 (RSG_SAMPLE)</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">connectedTablets = 30 units (Line Operator Tablets)</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c" font-weight="bold">linkStatus = "AirGapped_Autonomous (DYXnet Link Severed)"</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c">offlineDuration = "14 Hours 35 Minutes"</text>
                  <text x="20" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d" font-weight="bold">embeddedBuffer = "SQLite3 WAL Active (Writing Local Logs)"</text>
                  <text x="20" y="170" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309" font-weight="bold">bufferedTransactions = 184 txs (Sewing Records &amp; Quality Checks)</text>
                  <text x="20" y="190" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">lineOperationImpact = "0% (Zero Downtime, Sewing Continues Normally)"</text>
                  <text x="20" y="210" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">autoReplayDaemon = "Polling DYXnet TDS Port every 60s..."</text>
                  <text x="20" y="230" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">模擬展示柬埔寨廠於專線中斷時，自律緩衝機制作動之真實物件狀態。</text>
                </g>

                <!-- Link Component Object -->
                <g transform="translate(25, 590)">
                  <rect width="690" height="200" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
                  <text x="20" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0f172a" text-decoration="underline">dyxnet_channel : MplsVpnTrunk</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">服務商: 第一線 (DYXnet) 跨國企業專線 ｜ 協議: TCP 1433 TDS 資料流直開</text>
                  <text x="20" y="80" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">台北 - 越南延遲: 42ms (穩定) ｜ 台北 - 柬埔寨延遲: 斷線重試中 (離線緩衝隔離)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">物件關聯性驗證：rsv_edge_node ── dyxnet_channel ── rdsmp2_server</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">所有實例屬性與運算狀態均與實體部署規格完全吻合。</text>
                </g>
              </g>
            </svg>
          `;
    """

print("[OK] Cases 3 and 4 defined")
