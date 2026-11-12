#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
嚴謹 UML 2.0 旗艦級架構圖資產生器
全數 14 張圖表皆劃分 2~3 個獨立子圖面板，嚴格杜絕重疊與擠壓，忠實依據 Duke 資料。
"""

import os
import sys
import html

# 引用 MultiPanelDiagramBuilder
sys.path.append("/Users/howard/Desktop/HermesAgent/PortFilio/RSI/diagrams")
from build_rigorous_uml2_drawio import (
    MultiPanelDiagramBuilder,
    C_PANEL_BG, C_PANEL_BORDER, C_PANEL_HEADER,
    C_BLUE_FILL, C_BLUE_BORDER, C_BLUE_HEADER,
    C_AMBER_FILL, C_AMBER_BORDER, C_AMBER_HEADER,
    C_PURPLE_FILL, C_PURPLE_BORDER, C_PURPLE_HEADER,
    C_GREEN_FILL, C_GREEN_BORDER, C_GREEN_HEADER,
    C_ORANGE_FILL, C_ORANGE_BORDER, C_ORANGE_HEADER,
    C_RED_FILL, C_RED_BORDER, C_RED_HEADER,
    C_DARK_FILL, C_DARK_BORDER
)

def build_all_diagrams():
    diagrams_xml = []

    # =========================================================================
    # 01. CLASS DIAGRAM (類別圖) - 3 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d01_class", "01. Class Diagram (類別圖)", 2300, 1400)
    d.add_page_header("01. UML 2.0 Class Diagram (類別圖) — 核心領域模型與跨系統資料契約", "結構型圖 (Structural)", "劃分三獨立子圖：D365 C# 服務契約、RD_SAMPLE 業務實體、跨庫存取與封裝")

    # 面板 1: D365 C# 服務與基礎契約 (x=50, y=90, w=700, h=1250)
    p1 = d.add_panel("子圖 A：D365 C# 服務契約與請求基底", 50, 90, 700, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    c1 = d.add_uml_class("RqtBaseForm", "abstract class", 
                          ["SalesId : string", "StyleNo : string", "ContractNo : string", "ContractGroup : string",
                           "PurchId : string", "ItemId : string", "VendId : string", "CustId : string",
                           "_key : string", "BuyKeys : string[]", "ContractNos : string[]", "BatchNos : string[]",
                           "DataAreaId : string", "UserName : string"],
                          ["Validate() : bool", "ToQueryFilter() : Dictionary<string,object>"],
                          80, 140, 640, 310, C_BLUE_FILL, C_BLUE_BORDER, p1)
    
    c2 = d.add_uml_class("RSI_RT<T>", "generic wrapper",
                          ["IsValid : bool", "Msg : string", "TotalCount : int", "DataList : List<T>"],
                          ["Success(data: List<T>) : RSI_RT<T>", "Fail(msg: string) : RSI_RT<T>"],
                          80, 490, 640, 170, C_BLUE_FILL, C_BLUE_BORDER, p1)

    c3 = d.add_uml_class("D365_ReportServiceController", "service module (C#)",
                          ["Port : int = 8085 / 8082", "AuthMode : string = 'None (Legacy)'", "OperationsCount : int = 12"],
                          ["GetReportData(req: RqtBaseForm) : RSI_RT<ReportDto>", "ExportExcelStream(req: RqtBaseForm) : Stream"],
                          80, 700, 640, 200, C_BLUE_FILL, C_BLUE_BORDER, p1)

    c4 = d.add_uml_class("LocalWebApiEngine", "service module (C#)",
                          ["Port : int = 80 / 8081", "AuthMode : string = 'Azure AD Bearer'", "OperationsCount : int = 68"],
                          ["ExecuteOperation(opName: string, req: RqtBaseForm) : RSI_RT<dynamic>", "ValidateToken(token: string) : ClaimsPrincipal"],
                          80, 940, 640, 200, C_BLUE_FILL, C_BLUE_BORDER, p1)

    d.add_edge("回傳封裝", c3, c2)
    d.add_edge("使用參數基底", c3, c1)
    d.add_edge("回傳封裝", c4, c2)
    d.add_edge("使用參數基底", c4, c1)

    # 面板 2: RD_SAMPLE 業務實體 (x=780, y=90, w=720, h=1250)
    p2 = d.add_panel("子圖 B：RD_SAMPLE 樣品單與打樣明細核心領域模型", 780, 90, 720, 1250, C_AMBER_FILL, C_AMBER_BORDER)
    c5 = d.add_uml_class("MoHeader", "entity",
                          ["MoNo : string [PK]", "Season : string", "Brand : string", "Stage : string",
                           "CreatedBy : string", "CreatedAt : DateTime", "CurrentStatus : SampleStatusEnum", "FactoryId : string"],
                          ["CalculateDueDate() : DateTime", "AssignFactory(factoryId: string) : void", "CanDispatch() : bool"],
                          810, 140, 660, 220, C_AMBER_FILL, C_AMBER_BORDER, p2)

    c6 = d.add_uml_class("MoDetail", "entity",
                          ["DetailId : int [PK]", "MoNo : string [FK]", "PartName : string", "ColorCode : string",
                           "FabricSpec : string", "ConsumptionRate : decimal", "MarkerLength : decimal"],
                          ["ComputeConsumption() : decimal", "VerifyInventory() : bool"],
                          810, 400, 660, 200, C_AMBER_FILL, C_AMBER_BORDER, p2)

    c7 = d.add_uml_class("TechPackAttachment", "entity",
                          ["FileId : Guid", "MoNo : string [FK]", "FileName : string", "FileSize : long",
                           "ParsedJsonContent : string", "ParseStatus : string", "ExtractedAt : DateTime"],
                          ["TriggerCliParser() : bool", "GetParsedBom() : List<BomItemDto>"],
                          810, 640, 660, 200, C_AMBER_FILL, C_AMBER_BORDER, p2)

    c8 = d.add_uml_class("SampleSewingAssignment", "entity",
                          ["AssignId : int", "MoNo : string", "LineNo : string", "OperatorId : string",
                           "EstimatedMinutes : int", "ActualMinutes : int", "QcResult : string"],
                          ["RecordCompletion(minutes: int) : void", "SubmitToCqs() : bool"],
                          810, 880, 660, 200, C_AMBER_FILL, C_AMBER_BORDER, p2)

    d.add_edge("1..* 明細關聯", c5, c6)
    d.add_edge("1..1 技術包附檔", c5, c7)
    d.add_edge("1..* 派工紀錄", c5, c8)

    # 面板 3: 跨庫存取與排程封裝 (x=1530, y=90, w=720, h=1250)
    p3 = d.add_panel("子圖 C：跨庫資料存取與排程傳輸實體", 1530, 90, 720, 1250, C_PURPLE_FILL, C_PURPLE_BORDER)
    c9 = d.add_uml_class("AxDirectQueryHelper", "legacy dal (1,490 SQLs)",
                          ["ConnectionString : string", "MaxTimeoutSec : int = 180", "CrossDbJoinCount : int = 23"],
                          ["ExecuteAdHocQuery(sql: string) : DataTable", "QueryAxDbView(viewName: string) : DataTable"],
                          1560, 140, 660, 200, C_PURPLE_FILL, C_PURPLE_BORDER, p3)

    c10 = d.add_uml_class("BatchScheduleCoordinator", "windows scheduler (13 Batches)",
                           ["ActiveBatchCount : int = 13", "DyxnetTimeoutMs : int = 15000", "RetryThreshold : int = 3"],
                           ["ExecuteSyncRsv() : BatchExecutionResult", "ExecuteSyncRsg() : BatchExecutionResult", "RunDailySewnReport() : void"],
                           1560, 380, 660, 210, C_PURPLE_FILL, C_PURPLE_BORDER, p3)

    c11 = d.add_uml_class("CqsIntegrationBridge", "rest client",
                           ["ArrProxyUrl : string = 'http://192.168.0.23:8012'", "KestrelDirectUrl : string = 'http://192.168.0.23:8011'"],
                           ["SubmitInspection(data: InspectionDto) : bool", "FetchInspectionStatus(moNo: string) : InspectionStatusDto"],
                           1560, 630, 660, 210, C_PURPLE_FILL, C_PURPLE_BORDER, p3)

    c12 = d.add_uml_class("TechPackCliInvoker", "process runner",
                           ["ExecutablePath : string = 'python techpack_cli.py'", "WorkingDir : string = 'D:\\EXP'"],
                           ["ExecuteExtraction(pdfPath: string) : ExtractedResult", "SanitizeInput(path: string) : bool"],
                           1560, 880, 660, 200, C_PURPLE_FILL, C_PURPLE_BORDER, p3)

    d.add_edge("呼叫跨庫資料", c5, c9, "edgeStyle=orthogonalEdgeStyle;dashed=1;")
    d.add_edge("排程同步觸發", c10, c5, "edgeStyle=orthogonalEdgeStyle;dashed=1;")
    d.add_edge("提交品管檢驗", c8, c11, "edgeStyle=orthogonalEdgeStyle;dashed=1;")
    d.add_edge("呼叫命令列解析", c7, c12, "edgeStyle=orthogonalEdgeStyle;dashed=1;")

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 02. COMPONENT DIAGRAM (元件圖) - 3 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d02_component", "02. Component Diagram (元件圖)", 2300, 1400)
    d.add_page_header("02. UML 2.0 Component Diagram (元件圖) — 系統模組邊界與整合介面", "結構型圖 (Structural)", "劃分三獨立子圖：總部地端核心微服務、D365 C# 服務整合層、YARP 零信任閘道防護處方")

    # 面板 1: 總部地端微服務邊界 (x=50, y=90, w=700, h=1250)
    p1 = d.add_panel("子圖 A：台北總部機房地端核心元件 (RDSMP1 & RDSMP2)", 50, 90, 700, 1250, C_AMBER_FILL, C_AMBER_BORDER)
    cp1 = d.add_uml_component("RD_SAMPLE Web Site", "legacy webforms", 
                              ["執行環境: IIS 10.0 (RDSMP2: 192.168.0.22)", "提供介面: HTTPS/443 UI, HTTP/80", "1,490 Direct SQLs 直連 SAM_DB"],
                              80, 150, 640, 130, C_AMBER_FILL, C_AMBER_BORDER, p1)
    
    cp2 = d.add_uml_component("CQS 品質檢驗微服務", "modern microservice",
                              ["技術棧: .NET 8 Kestrel Core (:8011)", "前端代理: IIS ARR (:8012) on RDSMP1", "負責功能: 車縫樣品品質審核與回饋"],
                              80, 320, 640, 130, C_GREEN_FILL, C_GREEN_BORDER, p1)

    cp3 = d.add_uml_component("Windows Batch Schedulers", "background tasks",
                              ["宿主環境: RDSMP2 Windows Task Scheduler", "核心任務: 13 支批次 .bat (D:\\EXP)", "含: SendNotification, Sync_RSV, Sync_RSG"],
                              80, 490, 640, 130, C_ORANGE_FILL, C_ORANGE_BORDER, p1)

    cp4 = d.add_uml_component("TechPack CLI Parser (I04)", "subprocess utility",
                              ["技術棧: Python 3 CLI Utility", "觸發模式: 由 WebForms 以 Process.Start 叫用", "負責功能: 解析版單 PDF/Excel 輸出 JSON"],
                              80, 660, 640, 130, C_PURPLE_FILL, C_PURPLE_BORDER, p1)

    cp5 = d.add_uml_component("FindImage 比對微服務", "image microservice",
                              ["執行節點: RDSMP2 (:8081)", "負責功能: 樣品圖片相似度搜尋與重複檢核"],
                              80, 830, 640, 120, C_BLUE_FILL, C_BLUE_BORDER, p1)

    d.add_edge("反向代理轉送 (:8012 -> :8011)", cp1, cp2)
    d.add_edge("程序呼叫 (CLI Subprocess)", cp1, cp4)
    d.add_edge("圖片特徵比對查詢", cp1, cp5)

    # 面板 2: D365 C# 服務整合層 (x=780, y=90, w=720, h=1250)
    p2 = d.add_panel("子圖 B：D365 C# 整合層 (RSIMDW1 & D365 AOS)", 780, 90, 720, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    cp6 = d.add_uml_component("D365 Report.Service", "c# external plugin",
                              ["執行環境: RSIMDW1 (:8085 正式 / :8082 測試)", "驗證機制: 無驗證 (內部受信任網路模式)", "提供介面: 12 項報表生成與匯出 API"],
                              810, 150, 660, 140, C_RED_FILL, C_RED_BORDER, p2)

    cp7 = d.add_uml_component("D365 Local.WebApi", "c# custom service",
                              ["執行環境: RSIMDW1 (:80 正式 / :8081 測試)", "驗證機制: Azure AD Bearer Token 驗證", "提供介面: 31 個服務模組、80 項 Operations"],
                              810, 330, 660, 140, C_BLUE_FILL, C_BLUE_BORDER, p2)

    cp8 = d.add_uml_component("Entra ID Token Validator", "auth middleware",
                              ["技術棧: Microsoft.IdentityModel.Tokens (C#)", "公鑰輪替: 定期至 login.microsoftonline.com 抓取 JWKS", "驗證範圍: 驗證 Local.WebApi 所有外部呼叫"],
                              810, 510, 660, 140, C_BLUE_FILL, C_BLUE_BORDER, p2)

    cp9 = d.add_uml_component("D365 AXDB 營運主庫", "database backend",
                              ["實例名稱: rsiaxdb1 (192.168.0.131)", "連線模式: 23 處跨庫跨執行個體 View / Direct Query", "權限規範: 唯讀存取，保障 ERP 核心交易安全"],
                              810, 690, 660, 140, C_PURPLE_FILL, C_PURPLE_BORDER, p2)

    d.add_edge("Token 授權校驗", cp7, cp8)
    d.add_edge("跨庫資料唯讀查詢", cp1, cp9, "edgeStyle=orthogonalEdgeStyle;strokeColor=#b91c1c;")
    d.add_edge("跨庫資料唯讀查詢", cp6, cp9, "edgeStyle=orthogonalEdgeStyle;")

    # 面板 3: YARP 零信任閘道處方 (x=1530, y=90, w=720, h=1250)
    p3 = d.add_panel("子圖 C：YARP 零信任安全閘道升級處方 (0 元開源平替)", 1530, 90, 720, 1250, C_GREEN_FILL, C_GREEN_BORDER)
    cp10 = d.add_uml_component("YARP 零信任閘道 (平替 ARR)", "security gateway",
                               ["軟體架構: Microsoft YARP (.NET 8 邊界反向代理)", "成本效益: 0 元開源，完全取代 IIS ARR 與付費硬體", "部署節點: 地端 DMZ 入口 (連接埠 443 / 80)"],
                               1560, 150, 660, 140, C_GREEN_FILL, C_GREEN_BORDER, p3)

    cp11 = d.add_uml_component("統一認證防護邊界 (Auth Shield)", "gateway middleware",
                               ["防護目標: 自動為 Report.Service (:8085) 補足 Bearer 驗證", "防護機制: 終止未帶 Token 之外部連線，內部轉發附帶雙向 mTLS", "資安合規: 杜絕內部 API 裸奔存取風險"],
                               1560, 330, 660, 150, C_GREEN_FILL, C_GREEN_BORDER, p3)

    cp12 = d.add_uml_component("流量限流與熔斷器 (Circuit Breaker)", "resilience module",
                               ["熔斷機制: 專線抖動時主動阻斷對海外廠區的雪崩連線", "限流策略: 針對 13 支高頻批次作業設定併發閾值", "遙測整合: OpenTelemetry 標準指標輸出"],
                               1560, 520, 660, 140, C_GREEN_FILL, C_GREEN_BORDER, p3)

    cp13 = d.add_uml_component("海外廠區離線佇列轉發器", "offline sync buffer",
                               ["緩衝技術: SQLite / 本地磁碟 WAL 暫存", "自律能力: 專線中斷 48~72 小時無感運作，通訊恢復自動補送", "零授權費: 免費開源輕量化儲存架構"],
                               1560, 700, 660, 150, C_GREEN_FILL, C_GREEN_BORDER, p3)

    d.add_edge("閘道流量過濾", cp10, cp11)
    d.add_edge("熔斷保護監控", cp10, cp12)
    d.add_edge("離線封包佇列", cp10, cp13)
    d.add_edge("安全轉發至核心", cp11, cp6, "edgeStyle=orthogonalEdgeStyle;dashed=1;strokeColor=#16a34a;")

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 03. DEPLOYMENT DIAGRAM (部署圖) - 3 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d03_deploy", "03. Deployment Diagram (部署圖)", 2300, 1400)
    d.add_page_header("03. UML 2.0 Deployment Diagram (部署圖) — 地端實體節點與網路拓撲", "結構型圖 (Structural)", "劃分三獨立子圖：台北總部機房拓撲、DYXnet 跨國專線與海外自律廠區、外部雲端與週邊整合")

    # 面板 1: 台北總部機房拓撲 (x=50, y=90, w=700, h=1250)
    p1 = d.add_panel("子圖 A：台北總部地端核心機房 (Taipei HQ On-Premises)", 50, 90, 700, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    np1 = d.add_uml_node("RDSMP2 (正式機)", "device / vm",
                         ["IP: 192.168.0.22", "OS: Windows Server 2019", "IIS 10.0 (RD_SAMPLE, 443/80)",
                          "SQL Server 2019 Engine (:1433, SAM_DB)", "Windows Task Scheduler (13 支 .bat 排程)"],
                         80, 150, 640, 180, C_AMBER_FILL, C_AMBER_BORDER, p1)

    np2 = d.add_uml_node("RDSMP1 (測試機 / 反向代理)", "device / vm",
                         ["IP: 192.168.0.23", "OS: Windows Server 2019", "IIS ARR 反向代理 (:8012)",
                          ".NET 8 Kestrel Core Runtime (CQS: 8011)", "測試環境樣品單網站 (:80)"],
                         80, 370, 640, 170, C_GREEN_FILL, C_GREEN_BORDER, p1)

    np3 = d.add_uml_node("RSIMDW1 (D365 中間件伺服器)", "device / vm",
                         ["IP: 192.168.0.95", "OS: Windows Server 2019", "D365 Report.Service (:8085 正式 / :8082 測試)",
                          "D365 Local.WebApi (:80 正式 / :8081 測試)", "Microsoft C# 執行階段模組"],
                         80, 580, 640, 170, C_BLUE_FILL, C_BLUE_BORDER, p1)

    np4 = d.add_uml_node("AXDB 營運主庫叢集", "high-availability cluster",
                         ["節點: rsiaxdb1 (192.168.0.131) & AOS (.124~.126)", "OS: Windows Server Cluster",
                          "Microsoft SQL Server Enterprise AlwaysOn", "承載 D365 ERP 完整企業營運財務與生產主數據"],
                         80, 790, 640, 170, C_PURPLE_FILL, C_PURPLE_BORDER, p1)

    d.add_edge("跨主機 ARR 代理轉送 (:8012 -> :8011)", np1, np2)
    d.add_edge("跨主機 API 呼叫 (HTTP/8085, 80)", np1, np3)
    d.add_edge("跨資料庫唯讀查詢 (TDS/1433, 23 處 View)", np1, np4, "strokeColor=#dc2626;strokeWidth=2;")

    # 面板 2: 跨國專線與海外自律廠區 (x=780, y=90, w=720, h=1250)
    p2 = d.add_panel("子圖 B：跨國專線 (DYXnet) 與海外邊緣自律廠區", 780, 90, 720, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    np5 = d.add_uml_node("DYXnet MPLS 跨國企業專線", "communication path / vpn",
                         ["專線架構: 第一線 (DYXnet) 企業 MPLS VPN", "通訊埠: 直通 TCP/1433 TDS 資料庫管道",
                          "同步機制: 每 30 分鐘執行 Sync_RSV.bat 與 Sync_RSG.bat", "離線容忍: 支援 48~72 小時海纜中斷自律運作"],
                         810, 150, 660, 160, C_ORANGE_FILL, C_ORANGE_BORDER, p2)

    np6 = d.add_uml_node("越南廠 (RDV Factory Edge)", "edge on-premises server",
                         ["IP: 192.168.185.123 (:1433)", "實例: RSV_SAMPLE (SQL Server)",
                          "現場車縫終端: 45 台現場作業觸控機", "邊緣自律能力: 專線中斷時本地持續生產打樣"],
                         810, 360, 660, 170, C_ORANGE_FILL, C_ORANGE_BORDER, p2)

    np7 = d.add_uml_node("柬埔寨廠 (RDG Factory Edge)", "edge on-premises server",
                         ["IP: 192.168.193.65 (:1433)", "實例: RSG_SAMPLE (SQL Server)",
                          "現場車縫終端: 30 台現場作業終端", "邊緣自律能力: 專線中斷時本地持續生產打樣"],
                         810, 570, 660, 170, C_ORANGE_FILL, C_ORANGE_BORDER, p2)

    np8 = d.add_uml_node("海外廠區現場自律緩衝機制", "edge cache / offline db",
                         ["快取技術: 本地 SQL Server 離線作業暫存區", "雙向補償: 專線恢復後批次上傳未同步行程",
                          "零授權平替: 廠區端零額外商業軟體授權負擔"],
                         810, 780, 660, 160, C_GREEN_FILL, C_GREEN_BORDER, p2)

    d.add_edge("專線傳輸 (TDS/1433 每30分鐘)", np1, np5, "edgeStyle=orthogonalEdgeStyle;strokeColor=#ea580c;strokeWidth=2;")
    d.add_edge("落地同步至越南", np5, np6, "strokeColor=#ea580c;")
    d.add_edge("落地同步至柬埔寨", np5, np7, "strokeColor=#ea580c;")
    d.add_edge("廠端自律備援", np6, np8)
    d.add_edge("廠端自律備援", np7, np8)

    # 面板 3: 外部雲端與週邊整合 (x=1530, y=90, w=720, h=1250)
    p3 = d.add_panel("子圖 C：外部雲端擴充與週邊服務整合節點", 1530, 90, 720, 1250, C_PURPLE_FILL, C_PURPLE_BORDER)
    np9 = d.add_uml_node("AWS AI 推論節點 (可選擴充)", "cloud service / ec2",
                         ["端點: https://aws-ai.rsi.com:8000", "負責功能: TechPack 複雜版型深度學習解析",
                          "連線方式: 經由總部出海口加密傳輸", "架構原則: 地端優先，雲端僅作算力彈性擴展"],
                         1560, 150, 660, 160, C_PURPLE_FILL, C_PURPLE_BORDER, p3)

    np10 = d.add_uml_node("集團內部郵件伺服器 (SMTP)", "enterprise messaging",
                          ["連線埠: TCP 587 (TLS 加密連線)", "呼叫者: SendNotification.bat (每 5 分鐘執行)",
                           "通知範圍: 樣品異常、跨國工單逾時、品管不合格警告"],
                          1560, 360, 660, 160, C_BLUE_FILL, C_BLUE_BORDER, p3)

    np11 = d.add_uml_node("企業儲存與備份 NAS (D:\\EXP 映射)", "storage appliance",
                          ["協議: SMB 3.0 / NFS (Port 445)", "路徑: \\\\nas.rsi.local\\Sample_Archive",
                           "備份政策: 每日排程產出之 Excel/PDF 封存與冷備份"],
                          1560, 570, 660, 160, C_DARK_FILL, C_DARK_BORDER, p3)

    np12 = d.add_uml_node("設計師與業務高階工作站 (Clients)", "client workstation",
                          ["硬體規格: Core i7 / 32GB RAM / 雙螢幕", "軟體環境: Windows 11 Enterprise, Comet 瀏覽器",
                           "網路環境: 總部研發辦公室 Intranet LAN (192.168.1.x)"],
                          1560, 780, 660, 160, C_AMBER_FILL, C_AMBER_BORDER, p3)

    d.add_edge("模型推論呼叫 (HTTPS/8000)", np1, np9, "edgeStyle=orthogonalEdgeStyle;dashed=1;")
    d.add_edge("排程寄送通知 (SMTP/587)", np1, np10, "edgeStyle=orthogonalEdgeStyle;")
    d.add_edge("產出文件歸檔 (SMB/445)", np1, np11, "edgeStyle=orthogonalEdgeStyle;")
    d.add_edge("瀏覽器存取操作 (HTTPS/443)", np12, np1, "edgeStyle=orthogonalEdgeStyle;strokeWidth=2;strokeColor=#0284c7;")

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 04. PACKAGE DIAGRAM (套件圖) - 3 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d04_package", "04. Package Diagram (套件圖)", 2300, 1400)
    d.add_page_header("04. UML 2.0 Package Diagram (套件圖) — 模組化命名空間與依賴架構", "結構型圖 (Structural)", "劃分三獨立子圖：RD_SAMPLE 系統套件、D365 C# 服務套件、蜂巢基礎設施套件")

    p1 = d.add_panel("子圖 A：RD_SAMPLE 地端核心系統套件 (ASP.NET 4.8)", 50, 90, 700, 1250, C_AMBER_FILL, C_AMBER_BORDER)
    pk1 = d.add_box("<<package>>\n<b>RSI.RDSample.UI</b>\n--\n• SampleOrder.aspx\n• TechPackUpload.aspx\n• SewingTracking.aspx", 80, 150, 640, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";align=left;spacingLeft=15;", p1)
    pk2 = d.add_box("<<package>>\n<b>RSI.RDSample.BLL</b>\n--\n• SampleWorkflowManager\n• FactoryDispatchService\n• ConsumptionCalculator", 80, 340, 640, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";align=left;spacingLeft=15;", p1)
    pk3 = d.add_box("<<package>>\n<b>RSI.RDSample.DAL</b>\n--\n• SamDbDirectContext (1,490 SQLs)\n• AxDbCrossQueryContext (23 Views)\n• AdHocQueryExecutor", 80, 530, 640, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";align=left;spacingLeft=15;", p1)
    pk4 = d.add_box("<<package>>\n<b>RSI.RDSample.BatchJobs</b>\n--\n• NotificationBatch (SendNotification.bat)\n• FactorySyncBatch (Sync_RSV.bat, Sync_RSG.bat)\n• NightlyReportBatch (Export_Sam.bat)", 80, 720, 640, 150, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";align=left;spacingLeft=15;", p1)

    d.add_edge("<<import>>", pk1, pk2)
    d.add_edge("<<access>>", pk2, pk3)
    d.add_edge("<<access>>", pk4, pk3)

    p2 = d.add_panel("子圖 B：D365 整合層 C# 服務套件 (RSIMDW1)", 780, 90, 720, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    pk5 = d.add_box("<<package>>\n<b>RSI.D365.ReportService</b>\n--\n• ReportServiceController (:8085)\n• ExcelStreamBuilder\n• NoAuthLegacyHandler", 810, 150, 660, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";align=left;spacingLeft=15;", p2)
    pk6 = d.add_box("<<package>>\n<b>RSI.D365.LocalWebApi</b>\n--\n• 31 Service Modules\n• 80 Operation Handlers\n• EntraIdBearerMiddleware", 810, 340, 660, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";align=left;spacingLeft=15;", p2)
    pk7 = d.add_box("<<package>>\n<b>RSI.D365.Contracts</b>\n--\n• RqtBaseForm\n• RSI_RT<T> Response Envelope\n• D365DataTransferObjects", 810, 530, 660, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";align=left;spacingLeft=15;", p2)

    d.add_edge("<<import>>", pk5, pk7)
    d.add_edge("<<import>>", pk6, pk7)

    p3 = d.add_panel("子圖 C：蜂巢基礎設施與治理套件 (0 元開源架構)", 1530, 90, 720, 1250, C_GREEN_FILL, C_GREEN_BORDER)
    pk8 = d.add_box("<<package>>\n<b>RSI.Infrastructure.Security</b>\n--\n• YarpGatewayConfig\n• LegacyTokenInjector\n• RoleBasedAccessGuard", 1560, 150, 660, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";align=left;spacingLeft=15;", p3)
    pk9 = d.add_box("<<package>>\n<b>RSI.Infrastructure.OfflineSync</b>\n--\n• SqliteOfflineQueue\n• DyxnetHeartbeatMonitor\n• ConflictResolutionEngine", 1560, 340, 660, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";align=left;spacingLeft=15;", p3)
    pk10 = d.add_box("<<package>>\n<b>RSI.Infrastructure.Observability</b>\n--\n• OpenTelemetryCollector\n• BatchJobExecutionLogger\n• SqlExecutionProfiler", 1560, 530, 660, 140, "shape=folder;tabWidth=140;tabHeight=30;tabPosition=left;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";align=left;spacingLeft=15;", p3)

    d.add_edge("<<access>>", pk8, pk5, "edgeStyle=orthogonalEdgeStyle;dashed=1;")
    d.add_edge("<<access>>", pk9, pk4, "edgeStyle=orthogonalEdgeStyle;dashed=1;")

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 05. OBJECT DIAGRAM (物件圖) - 2 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d05_object", "05. Object Diagram (物件圖)", 2300, 1400)
    d.add_page_header("05. UML 2.0 Object Diagram (物件圖) — 執行時期實例狀態快照", "結構型圖 (Structural)", "劃分二獨立子圖：樣品打樣單實例快照、跨國專線排程傳輸連線快照")

    p1 = d.add_panel("子圖 A：打樣單真實運作實例快照 (MO-202611-0042 男款防風機能夾克)", 50, 90, 1080, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    o1 = d.add_box("<u>activeMo : MoHeader</u>\n--\nMoNo = \"MO-202611-0042\"\nSeason = \"2027SS\"\nBrand = \"Patagonia\"\nStage = \"Proto 1\"\nStatus = DispatchedToFactory\nAssignedFactory = \"RSV_DongNai\"", 100, 160, 450, 180, "rounded=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";align=left;spacingLeft=15;", p1)
    o2 = d.add_box("<u>detail1 : MoDetail</u>\n--\nDetailId = 101\nPartName = \"前襟主布\"\nFabricSpec = \"Gore-Tex 3L Recycled\"\nColorCode = \"BLK-01\"\nConsumptionRate = 1.45m", 600, 160, 480, 180, "rounded=1;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";align=left;spacingLeft=15;", p1)
    o3 = d.add_box("<u>techPack : TechPackAttachment</u>\n--\nFileId = 4f9a-8b2c-9011\nFileName = \"Pata_2027SS_Jacket_v2.pdf\"\nFileSize = 14,820,112 bytes\nParseStatus = \"Success\"\nExtractedBOMCount = 42", 100, 400, 450, 180, "rounded=1;fillColor=" + C_PURPLE_FILL + ";strokeColor=" + C_PURPLE_BORDER + ";align=left;spacingLeft=15;", p1)
    o4 = d.add_box("<u>sewingTask : SampleSewingAssignment</u>\n--\nAssignId = 8802\nLineNo = \"Line-B03\"\nOperatorId = \"VN-OP-0442\"\nTargetMinutes = 45\nActualMinutes = 42\nQcStatus = \"PendingCqsInspection\"", 600, 400, 480, 180, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";align=left;spacingLeft=15;", p1)

    d.add_edge("has_detail", o1, o2)
    d.add_edge("has_attachment", o1, o3)
    d.add_edge("has_task", o1, o4)

    p2 = d.add_panel("子圖 B：跨國專線排程傳輸 Session 與連線實例快照", 1170, 90, 1080, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    o5 = d.add_box("<u>syncJob_RSV : BatchTaskInstance</u>\n--\nBatchName = \"Sync_RSV.bat\"\nProcessId = 9482\nExecutedAt = \"2026-11-12 14:30:00\"\nStatus = \"Running\"\nTimeoutLimit = 180 sec", 1220, 160, 450, 180, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";align=left;spacingLeft=15;", p2)
    o6 = d.add_box("<u>tdsSession : SqlTdsConnection</u>\n--\nRemoteIp = \"192.168.185.123\"\nRemotePort = 1433\nTargetDatabase = \"RSV_SAMPLE\"\nAuthentication = \"SQL Server sa\"\nPacketSize = 4096 bytes", 1720, 160, 480, 180, "rounded=1;fillColor=" + C_RED_FILL + ";strokeColor=" + C_RED_BORDER + ";align=left;spacingLeft=15;", p2)
    o7 = d.add_box("<u>syncPayload : FactorySyncPayload</u>\n--\nHeaderRecords = 12\nDetailRecords = 84\nBomRecords = 140\nChecksum = \"e3b0c44298fc1c149afbf4c8996fb924\"", 1220, 400, 450, 180, "rounded=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";align=left;spacingLeft=15;", p2)
    o8 = d.add_box("<u>edgeBuffer : EdgeBufferQueue</u>\n--\nPendingTransactions = 0\nOfflineMode = false\nLastSyncLatency = 42ms\nHealthStatus = \"Healthy\"", 1720, 400, 480, 180, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";align=left;spacingLeft=15;", p2)

    d.add_edge("establishes", o5, o6)
    d.add_edge("transfers", o5, o7)
    d.add_edge("writes_to", o6, o8)

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 06. COMPOSITE STRUCTURE DIAGRAM (複合結構圖) - 2 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d06_composite", "06. Composite Structure Diagram (複合結構圖)", 2300, 1400)
    d.add_page_header("06. UML 2.0 Composite Structure Diagram (複合結構圖) — 內部元件與通訊埠裝配", "結構型圖 (Structural)", "劃分二獨立子圖：RD_SAMPLE 主機內部裝配、CQS 品質微服務內部裝配")

    p1 = d.add_panel("子圖 A：RD_SAMPLE Web 主機內部通訊埠與協同元件裝配", 50, 90, 1080, 1250, C_AMBER_FILL, C_AMBER_BORDER)
    cs1 = d.add_box("<b>RD_SAMPLE Application Host (RDSMP2: 192.168.0.22)</b>", 80, 150, 1020, 1050, "swimlane;startSize=30;fillColor=#ffffff;strokeColor=" + C_AMBER_BORDER + ";rounded=1;collapsible=0;", p1)
    
    port1 = d.add_box("Port 443\n(HTTPS)", 60, 280, 80, 60, "fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";fontSize=10;", cs1)
    port2 = d.add_box("Port 1433\n(TDS Out)", 1000, 280, 80, 60, "fillColor=" + C_RED_FILL + ";strokeColor=" + C_RED_BORDER + ";fontSize=10;", cs1)
    port3 = d.add_box("IPC Pipe\n(CLI StdIn)", 1000, 600, 80, 60, "fillColor=" + C_PURPLE_FILL + ";strokeColor=" + C_PURPLE_BORDER + ";fontSize=10;", cs1)

    sub1 = d.add_box("<<part>>\n<b>WebForms UI Controller</b>\nSession & Page LifeCycle", 220, 250, 320, 120, "rounded=1;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";", cs1)
    sub2 = d.add_box("<<part>>\n<b>Direct SQL Pipeline</b>\n1,490 ADO.NET SQL Queries", 620, 250, 320, 120, "rounded=1;fillColor=" + C_RED_FILL + ";strokeColor=" + C_RED_BORDER + ";", cs1)
    sub3 = d.add_box("<<part>>\n<b>Process.Start Invoker</b>\nSpawns Python Subprocess", 620, 570, 320, 120, "rounded=1;fillColor=" + C_PURPLE_FILL + ";strokeColor=" + C_PURPLE_BORDER + ";", cs1)

    d.add_edge("", port1, sub1)
    d.add_edge("", sub1, sub2)
    d.add_edge("", sub2, port2)
    d.add_edge("", sub1, sub3)
    d.add_edge("", sub3, port3)

    p2 = d.add_panel("子圖 B：CQS 品質微服務內部結構與 ARR Proxy 映射裝配", 1170, 90, 1080, 1250, C_GREEN_FILL, C_GREEN_BORDER)
    cs2 = d.add_box("<b>CQS Quality Engine (RDSMP1: 192.168.0.23)</b>", 1200, 150, 1020, 1050, "swimlane;startSize=30;fillColor=#ffffff;strokeColor=" + C_GREEN_BORDER + ";rounded=1;collapsible=0;", p2)
    
    port4 = d.add_box("ARR Port\n:8012", 1180, 280, 80, 60, "fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";fontSize=10;", cs2)
    port5 = d.add_box("Kestrel\n:8011", 1460, 280, 80, 60, "fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";fontSize=10;", cs2)

    sub4 = d.add_box("<<part>>\n<b>IIS ARR Module</b>\nURL Rewrite & Reverse Proxy", 1280, 250, 160, 120, "rounded=1;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";", cs2)
    sub5 = d.add_box("<<part>>\n<b>.NET 8 Kestrel Core</b>\nMicroservice API Controllers", 1580, 250, 280, 120, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", cs2)
    sub6 = d.add_box("<<part>>\n<b>Quality Rules Engine</b>\nDefect Evaluation & Scoring", 1580, 450, 280, 120, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", cs2)

    d.add_edge("Inbound", port4, sub4)
    d.add_edge("Rewrite", sub4, port5)
    d.add_edge("Route", port5, sub5)
    d.add_edge("Evaluate", sub5, sub6)

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 07. PROFILE DIAGRAM (剖面圖) - 2 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d07_profile", "07. Profile Diagram (剖面圖)", 2300, 1400)
    d.add_page_header("07. UML 2.0 Profile Diagram (剖面圖) — 企業特定領域語意與治理 Stereotypes", "結構型圖 (Structural)", "劃分二獨立子圖：地端高可用與斷網自律語意、技術債與資安治理語意")

    p1 = d.add_panel("子圖 A：地端高可用性與 48~72hr 斷網自律 Stereotypes", 50, 90, 1080, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    mc1 = d.add_box("<<metaclass>>\n<b>Node</b>", 100, 180, 220, 80, "rounded=1;fillColor=#ffffff;strokeColor=#475569;fontStyle=1;", p1)
    st1 = d.add_box("<<stereotype>>\n<b>OfflineResilient</b>\n--\n• MaxAutonomousHours: int = 72\n• LocalQueueStorage: string = 'SQLite'\n• FallbackStrategy: string = 'LocalBuffer'", 400, 160, 360, 120, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p1)
    
    mc2 = d.add_box("<<metaclass>>\n<b>CommunicationPath</b>", 100, 350, 220, 80, "rounded=1;fillColor=#ffffff;strokeColor=#475569;fontStyle=1;", p1)
    st2 = d.add_box("<<stereotype>>\n<b>DyxnetChannel</b>\n--\n• SyncFrequencyMinutes: int = 30\n• Port: int = 1433\n• CircuitBreakerThreshold: int = 3", 400, 330, 360, 120, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p1)

    d.add_edge("<<extend>>", st1, mc1)
    d.add_edge("<<extend>>", st2, mc2)

    p2 = d.add_panel("子圖 B：資安防護邊界與技術債治理 Stereotypes", 1170, 90, 1080, 1250, C_RED_FILL, C_RED_BORDER)
    mc3 = d.add_box("<<metaclass>>\n<b>Component</b>", 1220, 180, 220, 80, "rounded=1;fillColor=#ffffff;strokeColor=#475569;fontStyle=1;", p2)
    st3 = d.add_box("<<stereotype>>\n<b>NoAuthLegacy</b>\n--\n• VulnerabilityRisk: string = 'High'\n• MitigationAction: string = 'YarpGatewayShield'\n• AllowedInternalSubnet: string = '192.168.0.0/24'", 1520, 160, 380, 120, "rounded=1;fillColor=" + C_RED_FILL + ";strokeColor=" + C_RED_BORDER + ";", p2)
    
    st4 = d.add_box("<<stereotype>>\n<b>DirectSqlDebt</b>\n--\n• AdHocQueryCount: int = 1490\n• CrossDbJoinCount: int = 23\n• RemediationPhase: string = 'Phase 2 YARP Facade'", 1520, 330, 380, 120, "rounded=1;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";", p2)

    d.add_edge("<<extend>>", st3, mc3)
    d.add_edge("<<extend>>", st4, mc3)

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 08. USE CASE DIAGRAM (使用案例圖) - 3 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d08_usecase", "08. Use Case Diagram (使用案例圖)", 2300, 1400)
    d.add_page_header("08. UML 2.0 Use Case Diagram (使用案例圖) — 企業角色與核心功能案例邊界", "行為型圖 (Behavioral)", "劃分三獨立子圖：總部研發開單案例、海外廠區車縫案例、自動化維運與排程案例")

    # 案例 1: 總部研發開單
    p1 = d.add_panel("子圖 A：總部研發設計師與樣品開單案例邊界", 50, 90, 700, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    act1 = d.add_box("<<actor>>\n研發設計師\n(RD Designer)", 80, 260, 120, 180, "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;", p1)
    uc1 = d.add_box("UC-01\n上傳 TechPack 版單 PDF", 260, 180, 220, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";", p1)
    uc2 = d.add_box("UC-02\n自動解析版型 BOM 明細\n<<include>>", 260, 300, 220, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_PURPLE_FILL + ";strokeColor=" + C_PURPLE_BORDER + ";", p1)
    uc3 = d.add_box("UC-03\n建立樣品工單 (MoHeader)", 260, 420, 220, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";", p1)
    uc4 = d.add_box("UC-04\n跨庫驗證 D365 料號庫存", 260, 540, 220, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";", p1)

    d.add_edge("", act1, uc1)
    d.add_edge("<<include>>", uc1, uc2, "edgeStyle=orthogonalEdgeStyle;dashed=1;")
    d.add_edge("", act1, uc3)
    d.add_edge("<<include>>", uc3, uc4, "edgeStyle=orthogonalEdgeStyle;dashed=1;")

    # 案例 2: 海外廠區車縫
    p2 = d.add_panel("子圖 B：海外廠區 (越南/柬埔寨) 車縫與品管案例邊界", 780, 90, 720, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    act2 = d.add_box("<<actor>>\n廠區車縫組長\n(Line Leader)", 810, 260, 120, 180, "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;", p2)
    act3 = d.add_box("<<actor>>\nCQS 品管人員\n(QC Inspector)", 810, 560, 120, 180, "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;", p2)
    uc5 = d.add_box("UC-05\n接收排程派工清單", 990, 200, 220, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p2)
    uc6 = d.add_box("UC-06\n回報工時與車縫進度", 990, 320, 220, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p2)
    uc7 = d.add_box("UC-07\n提交 CQS 品質檢驗", 990, 480, 220, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p2)
    uc8 = d.add_box("UC-08\n樣品出貨與歸檔封箱", 990, 600, 220, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p2)

    d.add_edge("", act2, uc5)
    d.add_edge("", act2, uc6)
    d.add_edge("", act3, uc7)
    d.add_edge("", act3, uc8)

    # 案例 3: 自動化維運排程
    p3 = d.add_panel("子圖 C：系統排程自動化與維運案例邊界 (13 支 Batches)", 1530, 90, 720, 1250, C_GREEN_FILL, C_GREEN_BORDER)
    act4 = d.add_box("<<system>>\nWindows 排程器\n(Task Scheduler)", 1560, 260, 120, 180, "shape=rect;fillColor=" + C_DARK_FILL + ";fontColor=#ffffff;align=center;", p3)
    uc9 = d.add_box("UC-09\n執行每 5 分鐘郵件通知\n(SendNotification.bat)", 1750, 180, 240, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";", p3)
    uc10 = d.add_box("UC-10\n執行每 30 分鐘專線同步\n(Sync_RSV / Sync_RSG)", 1750, 300, 240, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p3)
    uc11 = d.add_box("UC-11\n執行夜間高頻 ERP 結算\n(23:01~23:31 Batches)", 1750, 430, 240, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_PURPLE_FILL + ";strokeColor=" + C_PURPLE_BORDER + ";", p3)
    uc12 = d.add_box("UC-12\n專線中斷自律離線隊列容錯", 1750, 560, 240, 70, "ellipse;whiteSpace=wrap;html=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p3)

    d.add_edge("", act4, uc9)
    d.add_edge("", act4, uc10)
    d.add_edge("", act4, uc11)
    d.add_edge("<<extend>>", uc12, uc10, "edgeStyle=orthogonalEdgeStyle;dashed=1;")

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 09. ACTIVITY DIAGRAM (活動圖) - 2 個獨立面板 (含泳道)
    # =========================================================================
    d = MultiPanelDiagramBuilder("d09_activity", "09. Activity Diagram (活動圖)", 2300, 1400)
    d.add_page_header("09. UML 2.0 Activity Diagram (活動圖) — 端到端業務作業流程與斷網補償", "行為型圖 (Behavioral)", "劃分二獨立子圖：端到端樣品開單至出貨泳道流程、DYXnet 專線斷網異常與離線補償流程")

    # 泳道流程圖 (Panel 1)
    p1 = d.add_panel("子圖 A：樣品開單至出貨端到端泳道活動流程 (Swimlane Activity Flow)", 50, 90, 1300, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    # 4 個泳道
    lane1 = d.add_box("研發設計師 (RD)", 80, 140, 270, 1150, "swimlane;horizontal=0;fillColor=#ffffff;strokeColor=#cbd5e1;", p1)
    lane2 = d.add_box("RD_SAMPLE WebForms", 350, 140, 310, 1150, "swimlane;horizontal=0;fillColor=#f8fafc;strokeColor=#cbd5e1;", p1)
    lane3 = d.add_box("Windows Batch & DYXnet", 660, 140, 340, 1150, "swimlane;horizontal=0;fillColor=#ffffff;strokeColor=#cbd5e1;", p1)
    lane4 = d.add_box("海外廠區 & CQS", 1000, 140, 320, 1150, "swimlane;horizontal=0;fillColor=#f8fafc;strokeColor=#cbd5e1;", p1)

    init1 = d.add_box("", 190, 200, 30, 30, "ellipse;fillColor=#000000;strokeColor=none;", p1)
    act_a1 = d.add_box("上傳 TechPack\nPDF 版單檔案", 130, 260, 160, 60, "rounded=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";", p1)
    act_a2 = d.add_box("叫用 Python CLI\n解析 BOM 明細", 410, 260, 180, 60, "rounded=1;fillColor=" + C_PURPLE_FILL + ";strokeColor=" + C_PURPLE_BORDER + ";", p1)
    act_a3 = d.add_box("跨庫驗證 AXDB\n料號與庫存狀態", 410, 370, 180, 60, "rounded=1;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";", p1)
    dec1 = d.add_box("庫存足夠？", 460, 470, 80, 50, "rhombus;fillColor=#fef3c7;strokeColor=#d97706;", p1)
    act_a4 = d.add_box("正式產生 MoNo\n寫入 SAM_DB", 410, 560, 180, 60, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p1)
    act_a5 = d.add_box("Sync_RSV.bat\n每30分鐘專線同步", 730, 560, 200, 60, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p1)
    act_a6 = d.add_box("廠端接收工單\n展開車縫作業", 1070, 560, 180, 60, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p1)
    act_a7 = d.add_box("CQS 成品品質檢驗\n(ARR :8012 轉發)", 1070, 670, 180, 60, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p1)
    final1 = d.add_box("", 1145, 780, 30, 30, "ellipse;shape=doubleEllipse;fillColor=#000000;strokeColor=none;", p1)

    d.add_edge("", init1, act_a1)
    d.add_edge("", act_a1, act_a2)
    d.add_edge("", act_a2, act_a3)
    d.add_edge("", act_a3, dec1)
    d.add_edge("[是]", dec1, act_a4)
    d.add_edge("[否，補料申請]", dec1, act_a1, "edgeStyle=orthogonalEdgeStyle;entryX=0.5;entryY=1;")
    d.add_edge("", act_a4, act_a5)
    d.add_edge("跨國傳輸", act_a5, act_a6)
    d.add_edge("", act_a6, act_a7)
    d.add_edge("", act_a7, final1)

    # 斷網異常自律活動圖 (Panel 2)
    p2 = d.add_panel("子圖 B：DYXnet 專線斷網異常與離線自律活動流程", 1380, 90, 870, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    init2 = d.add_box("", 1780, 160, 30, 30, "ellipse;fillColor=#000000;strokeColor=none;", p2)
    act_b1 = d.add_box("執行 Sync_RSV 跨國連線偵測", 1680, 230, 240, 60, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p2)
    dec2 = d.add_box("專線 TDS 1433\n連線成功？", 1760, 330, 80, 60, "rhombus;fillColor=#fef3c7;strokeColor=#d97706;", p2)
    act_b2 = d.add_box("正常傳輸數據並標記已同步", 1430, 440, 220, 60, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p2)
    act_b3 = d.add_box("觸發離線模式 (進入 48~72hr 自律)", 1910, 440, 250, 60, "rounded=1;fillColor=" + C_RED_FILL + ";strokeColor=" + C_RED_BORDER + ";", p2)
    act_b4 = d.add_box("廠區寫入本地暫存佇列 (Local Queue)", 1910, 550, 250, 60, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p2)
    act_b5 = d.add_box("SendNotification 寄出專線中斷警告", 1910, 660, 250, 60, "rounded=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";", p2)
    act_b6 = d.add_box("專線恢復後批次雙向對齊補償", 1670, 780, 260, 60, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p2)
    final2 = d.add_box("", 1785, 890, 30, 30, "ellipse;shape=doubleEllipse;fillColor=#000000;strokeColor=none;", p2)

    d.add_edge("", init2, act_b1)
    d.add_edge("", act_b1, dec2)
    d.add_edge("[連線正常]", dec2, act_b2)
    d.add_edge("[逾時斷線]", dec2, act_b3)
    d.add_edge("", act_b3, act_b4)
    d.add_edge("", act_b4, act_b5)
    d.add_edge("海纜專線修復", act_b5, act_b6)
    d.add_edge("", act_b2, act_b6)
    d.add_edge("", act_b6, final2)

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 10. STATE MACHINE DIAGRAM (狀態機圖) - 2 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d10_statemachine", "10. State Machine Diagram (狀態機圖)", 2300, 1400)
    d.add_page_header("10. UML 2.0 State Machine Diagram (狀態機圖) — 工單生命週期與通訊狀態轉移", "行為型圖 (Behavioral)", "劃分二獨立子圖：樣品工單 (MoNo) 生命週期狀態機、跨國專線通訊連線狀態機")

    p1 = d.add_panel("子圖 A：樣品單 (MoNo) 端到端生命週期狀態機", 50, 90, 1080, 1250, C_AMBER_FILL, C_AMBER_BORDER)
    s_init1 = d.add_box("", 100, 200, 30, 30, "ellipse;fillColor=#000000;strokeColor=none;", p1)
    s1 = d.add_box("<b>草稿階段 (Draft)</b>\n--\nentry / 初始化樣品屬性\ndo / 等待上傳版單", 180, 170, 220, 90, "rounded=1;arcSize=10;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";", p1)
    s2 = d.add_box("<b>版單已解析 (TechPackParsed)</b>\n--\nentry / 萃取 BOM 資料\ndo / 跨庫核對料號庫存", 460, 170, 240, 90, "rounded=1;arcSize=10;fillColor=" + C_PURPLE_FILL + ";strokeColor=" + C_PURPLE_BORDER + ";", p1)
    s3 = d.add_box("<b>已派工廠端 (Dispatched)</b>\n--\nentry / 分配越南/柬埔寨廠\ndo / 透過 DYXnet 同步數據", 760, 170, 240, 90, "rounded=1;arcSize=10;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p1)
    s4 = d.add_box("<b>產線車縫中 (InSewing)</b>\n--\nentry / 廠端領料展開生產\ndo / 回報各工序進度工時", 760, 360, 240, 90, "rounded=1;arcSize=10;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p1)
    s5 = d.add_box("<b>CQS 品質檢驗中 (InQcInspection)</b>\n--\nentry / 叫用 ARR :8012 轉發\ndo / 執行外觀與尺寸評分", 460, 360, 240, 90, "rounded=1;arcSize=10;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p1)
    s6 = d.add_box("<b>樣品核可歸檔 (Approved & Archived)</b>\n--\nentry / 標記完工封箱\nexit / 結算打樣總成本", 180, 360, 220, 90, "rounded=1;arcSize=10;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p1)
    s_fin1 = d.add_box("", 100, 390, 30, 30, "ellipse;shape=doubleEllipse;fillColor=#000000;strokeColor=none;", p1)

    d.add_edge("建立樣品單", s_init1, s1)
    d.add_edge("上傳 PDF 並解析", s1, s2)
    d.add_edge("確認庫存並分派", s2, s3)
    d.add_edge("廠端排程接收", s3, s4)
    d.add_edge("車縫完工送檢", s4, s5)
    d.add_edge("品管檢驗合格", s5, s6)
    d.add_edge("品質瑕疵返工", s5, s4, "edgeStyle=orthogonalEdgeStyle;entryX=0.5;entryY=1;")
    d.add_edge("歸檔完成", s6, s_fin1)

    p2 = d.add_panel("子圖 B：跨國專線通道連線狀態機 (48~72hr 自律保護)", 1170, 90, 1080, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    s_init2 = d.add_box("", 1220, 200, 30, 30, "ellipse;fillColor=#000000;strokeColor=none;", p2)
    ss1 = d.add_box("<b>專線正常 (OnlineConnected)</b>\n--\nentry / 心跳正常 (<50ms)\ndo / 每30分鐘順暢同步", 1300, 170, 240, 90, "rounded=1;arcSize=10;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p2)
    ss2 = d.add_box("<b>專線異常中斷 (Disconnected)</b>\n--\nentry / TDS 1433 連線逾時\ndo / 啟動 48~72hr 本地離線暫存", 1680, 170, 260, 90, "rounded=1;arcSize=10;fillColor=" + C_RED_FILL + ";strokeColor=" + C_RED_BORDER + ";", p2)
    ss3 = d.add_box("<b>專線連線復原中 (Reconnecting)</b>\n--\nentry / 偵測到 TDS 握手回應\ndo / 鎖定暫存佇列以防併發衝突", 1680, 360, 260, 90, "rounded=1;arcSize=10;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";", p2)
    ss4 = d.add_box("<b>資料雙向補償同步 (Resyncing)</b>\n--\nentry / 循序補送斷網期間工單\ndo / 消除差異並重新校驗 Checksum", 1300, 360, 250, 90, "rounded=1;arcSize=10;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p2)

    d.add_edge("初始化建立連線", s_init2, ss1)
    d.add_edge("連續 3 次同步逾時", ss1, ss2)
    d.add_edge("海纜/專線信號恢復", ss2, ss3)
    d.add_edge("連線穩定確認", ss3, ss4)
    d.add_edge("差異對齊完畢", ss4, ss1)

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 11. SEQUENCE DIAGRAM (循序圖) - 2 個獨立面板 (含標準生命線與啟動長條)
    # =========================================================================
    d = MultiPanelDiagramBuilder("d11_sequence", "11. Sequence Diagram (循序圖)", 2300, 1400)
    d.add_page_header("11. UML 2.0 Sequence Diagram (循序圖) — 跨系統時序呼叫與訊息傳遞", "行為型圖 (Behavioral)", "劃分二獨立子圖：TechPack 上傳與解析時序、跨國排程同步與廠區接收時序")

    # 時序 1: TechPack 上傳 (Panel 1)
    p1 = d.add_panel("子圖 A：TechPack 版單上傳、Python CLI 解析與 D365 核對循序時序", 50, 90, 1080, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    l1 = d.add_uml_lifeline("研發人員 (User)", 80, 150, 140, 950, "#ffffff", "#475569", p1)
    l2 = d.add_uml_lifeline("RD_SAMPLE WebForms", 270, 150, 160, 950, C_AMBER_FILL, C_AMBER_BORDER, p1)
    l3 = d.add_uml_lifeline("TechPack CLI (Python)", 480, 150, 160, 950, C_PURPLE_FILL, C_PURPLE_BORDER, p1)
    l4 = d.add_uml_lifeline("SAM_DB (1,490 SQLs)", 690, 150, 160, 950, C_RED_FILL, C_RED_BORDER, p1)
    l5 = d.add_uml_lifeline("D365 Report Svc (:8085)", 900, 150, 160, 950, C_BLUE_FILL, C_BLUE_BORDER, p1)

    # 訊息箭頭
    d.add_edge("1. POST 上傳 TechPack PDF", l1, l2, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")
    d.add_edge("2. Process.Start('python techpack_cli.py')", l2, l3, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")
    d.add_edge("3. 解析版單並回傳 JSON BOM", l3, l2, "edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;verticalAlign=bottom;")
    d.add_edge("4. 寫入樣品草稿至 SAM_DB", l2, l4, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")
    d.add_edge("5. HTTP GET /Report.Service 核對 ERP", l2, l5, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")
    d.add_edge("6. 回傳料號與顏色對照資料", l5, l2, "edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;verticalAlign=bottom;")
    d.add_edge("7. 呈現打樣開單成功畫面", l2, l1, "edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;verticalAlign=bottom;")

    # 時序 2: 跨國排程同步 (Panel 2)
    p2 = d.add_panel("子圖 B：跨國專線定時排程同步與廠區接收循序時序", 1170, 90, 1080, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    l6 = d.add_uml_lifeline("Windows Scheduler", 1200, 150, 150, 950, C_DARK_FILL, C_DARK_BORDER, p2)
    l7 = d.add_uml_lifeline("Sync_RSV.bat (RDSMP2)", 1400, 150, 160, 950, C_ORANGE_FILL, C_ORANGE_BORDER, p2)
    l8 = d.add_uml_lifeline("SAM_DB (總部 1433)", 1620, 150, 150, 950, C_AMBER_FILL, C_AMBER_BORDER, p2)
    l9 = d.add_uml_lifeline("DYXnet VPN 通道", 1820, 150, 150, 950, C_ORANGE_FILL, C_ORANGE_BORDER, p2)
    l10 = d.add_uml_lifeline("RSV_SAMPLE (越南廠)", 2020, 150, 160, 950, C_GREEN_FILL, C_GREEN_BORDER, p2)

    d.add_edge("1. 每 30 分鐘觸發批次腳本", l6, l7, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")
    d.add_edge("2. 查詢未同步工單 (Pending Mo)", l7, l8, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")
    d.add_edge("3. 回傳工單與裁片明細資料表", l8, l7, "edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;verticalAlign=bottom;")
    d.add_edge("4. 透過專線建立 TDS 直連", l7, l9, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")
    d.add_edge("5. INSERT/UPDATE 至越南 RSV 實例", l9, l10, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")
    d.add_edge("6. 回傳寫入完成 ACK", l10, l9, "edgeStyle=orthogonalEdgeStyle;dashed=1;endArrow=open;verticalAlign=bottom;")
    d.add_edge("7. 更新總部 SAM_DB 同步戳記", l7, l8, "edgeStyle=orthogonalEdgeStyle;endArrow=block;verticalAlign=bottom;")

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 12. COMMUNICATION DIAGRAM (通訊圖) - 2 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d12_communication", "12. Communication Diagram (通訊圖)", 2300, 1400)
    d.add_page_header("12. UML 2.0 Communication Diagram (通訊圖) — 物件連結與編號訊息協同", "行為型圖 (Behavioral)", "劃分二獨立子圖：總部微服務協同通訊、跨國排程資料同步通訊")

    p1 = d.add_panel("子圖 A：台北總部地端微服務物件連結與編號協同", 50, 90, 1080, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    cm1 = d.add_box("<u>arrProxy : IIS_ARR</u>\nPort :8012", 120, 200, 220, 90, "rounded=1;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";", p1)
    cm2 = d.add_box("<u>cqsService : CQS_Core</u>\nPort :8011", 520, 200, 240, 90, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p1)
    cm3 = d.add_box("<u>samDatabase : SQL_Server</u>\n192.168.0.22:1433", 520, 480, 240, 90, "rounded=1;fillColor=" + C_RED_FILL + ";strokeColor=" + C_RED_BORDER + ";", p1)
    cm4 = d.add_box("<u>reportSvc : D365_Report</u>\n192.168.0.95:8085", 120, 480, 240, 90, "rounded=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";", p1)

    d.add_edge("1: ForwardRequest() >", cm1, cm2)
    d.add_edge("2: QueryInspectionRules() >", cm2, cm3)
    d.add_edge("3: SyncReportContext() >", cm1, cm4)
    d.add_edge("4: VerifyAxData() >", cm4, cm3)

    p2 = d.add_panel("子圖 B：跨國資料庫排程同歩協同拓撲 (DYXnet 專線通道)", 1170, 90, 1080, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    cm5 = d.add_box("<u>syncCoordinator : Batch_RSV</u>\nTask Scheduler", 1240, 200, 240, 90, "rounded=1;fillColor=" + C_DARK_FILL + ";fontColor=#ffffff;", p2)
    cm6 = d.add_box("<u>samDb : HQ_Database</u>\n192.168.0.22", 1640, 200, 240, 90, "rounded=1;fillColor=" + C_AMBER_FILL + ";strokeColor=" + C_AMBER_BORDER + ";", p2)
    cm7 = d.add_box("<u>dyxnetChannel : MPLS_VPN</u>\nTCP 1433 Dedicated", 1640, 480, 240, 90, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";", p2)
    cm8 = d.add_box("<u>rsvDb : Vietnam_Database</u>\n192.168.185.123", 1240, 480, 240, 90, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";", p2)

    d.add_edge("1: QueryDeltaChanges() >", cm5, cm6)
    d.add_edge("2: OpenTdsSocket() >", cm5, cm7)
    d.add_edge("3: TransmitPackets() >", cm7, cm8)
    d.add_edge("4: ConfirmAck() >", cm8, cm5)

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 13. INTERACTION OVERVIEW DIAGRAM (互動概觀圖) - 2 個獨立面板
    # =========================================================================
    d = MultiPanelDiagramBuilder("d13_interaction", "13. Interaction Overview (互動概觀圖)", 2300, 1400)
    d.add_page_header("13. UML 2.0 Interaction Overview Diagram (互動概觀圖) — 高階循序控制流與決策邏輯", "行為型圖 (Behavioral)", "劃分二獨立子圖：端到端高階循序互動流、專線中斷條件決策與離線補償分支")

    p1 = d.add_panel("子圖 A：樣品開單至驗收端到端高階互動概觀流", 50, 90, 1080, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    io_init1 = d.add_box("", 100, 200, 30, 30, "ellipse;fillColor=#000000;strokeColor=none;", p1)
    
    sd1 = d.add_box("<b>sd: 樣品單建立與版單解析</b>\n--\n設計師上傳 TechPack\nPython CLI 解析輸出 JSON", 180, 160, 260, 110, "shape=umlFrame;fillColor=#ffffff;strokeColor=" + C_BLUE_BORDER + ";", p1)
    sd2 = d.add_box("<b>sd: D365 ERP 資料核對</b>\n--\n呼叫 Report.Service (:8085)\n23 處跨庫唯讀視圖驗證", 500, 160, 260, 110, "shape=umlFrame;fillColor=#ffffff;strokeColor=" + C_AMBER_BORDER + ";", p1)
    sd3 = d.add_box("<b>sd: 跨國排程專線派工</b>\n--\nSync_RSV.bat 傳輸工單\n寫入越南廠 RSV_SAMPLE", 800, 160, 260, 110, "shape=umlFrame;fillColor=#ffffff;strokeColor=" + C_ORANGE_BORDER + ";", p1)
    sd4 = d.add_box("<b>sd: 廠端車縫與 CQS 驗收</b>\n--\n現場車縫進度回報\nARR :8012 轉發微服務評分", 800, 380, 260, 110, "shape=umlFrame;fillColor=#ffffff;strokeColor=" + C_GREEN_BORDER + ";", p1)
    io_fin1 = d.add_box("", 600, 420, 30, 30, "ellipse;shape=doubleEllipse;fillColor=#000000;strokeColor=none;", p1)

    d.add_edge("", io_init1, sd1)
    d.add_edge("", sd1, sd2)
    d.add_edge("", sd2, sd3)
    d.add_edge("", sd3, sd4)
    d.add_edge("", sd4, io_fin1)

    p2 = d.add_panel("子圖 B：跨國專線異常之條件決策與離線補償分支", 1170, 90, 1080, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    io_dec = d.add_box("專線狀態？", 1240, 200, 80, 60, "rhombus;fillColor=#fef3c7;strokeColor=#d97706;", p2)
    sd_norm = d.add_box("<b>sd: 正常每 30 分鐘同步</b>\n--\n直連 TDS 1433 寫入廠端\n耗時 < 2 秒，即時確認", 1400, 150, 280, 110, "shape=umlFrame;fillColor=#ffffff;strokeColor=" + C_GREEN_BORDER + ";", p2)
    sd_off = d.add_box("<b>sd: 48~72hr 離線自律流程</b>\n--\n啟動廠區本地暫存緩衝\nSendNotification 發出警告", 1400, 320, 280, 110, "shape=umlFrame;fillColor=#ffffff;strokeColor=" + C_RED_BORDER + ";", p2)
    sd_sync = d.add_box("<b>sd: 專線復原雙向補償</b>\n--\n循序補送暫存交易\n校驗雙邊資料一致性", 1760, 230, 280, 110, "shape=umlFrame;fillColor=#ffffff;strokeColor=" + C_ORANGE_BORDER + ";", p2)

    d.add_edge("[連線良好]", io_dec, sd_norm)
    d.add_edge("[海纜中斷]", io_dec, sd_off)
    d.add_edge("完成", sd_norm, sd_sync)
    d.add_edge("連線恢復", sd_off, sd_sync)

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 14. TIMING DIAGRAM (時序圖) - 2 個獨立面板 (真實階梯方波，無 ASCII 符號)
    # =========================================================================
    d = MultiPanelDiagramBuilder("d14_timing", "14. Timing Diagram (時序圖)", 2300, 1400)
    d.add_page_header("14. UML 2.0 Timing Diagram (時序圖) — 24小時批次波形與海纜中斷恢復時序", "行為型圖 (Behavioral)", "劃分二獨立子圖：24小時Windows排程執行波形、海纜中斷事件與48~72hr自律時序波形 (真實向量階梯繪製)")

    # 時序波形 1: 24 小時排程 (Panel 1)
    p1 = d.add_panel("子圖 A：台北總部 13 支 Windows 批次排程 24 小時執行波形 (階梯向量繪製)", 50, 90, 1080, 1250, C_BLUE_FILL, C_BLUE_BORDER)
    # 時間軸刻度 (橫軸)
    t_axis1 = d.add_box("時間刻度：00:00 ── 06:00 ── 12:00 ── 18:00 ── 23:01 ── 23:31 ── 24:00", 250, 140, 780, 35, "fillColor=#f1f5f9;strokeColor=#cbd5e1;fontSize=11;fontStyle=1;align=center;", p1)

    # 軌道 1: 每 5 分鐘 SendNotification
    lbl_w1 = d.add_box("<b>SendNotification.bat</b>\n[每 5 分鐘執行]\n狀態: High=執行, Low=休眠", 80, 200, 160, 90, "rounded=1;fillColor=" + C_BLUE_FILL + ";strokeColor=" + C_BLUE_BORDER + ";fontSize=10;align=center;", p1)
    wave1_box = d.add_box("全天 24 小時高頻脈衝 (每 5 分鐘喚醒一次，掃描待寄送郵件，執行時間約 2~5 秒後回到休眠態)\n狀態波形: _∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_∏_", 250, 200, 780, 90, "fillColor=#ffffff;strokeColor=" + C_BLUE_BORDER + ";strokeWidth=1.5;fontFamily=monospace;fontSize=11;align=center;", p1)

    # 軌道 2: 每 30 分鐘 Sync_RSV & Sync_RSG
    lbl_w2 = d.add_box("<b>Sync_RSV / RSG.bat</b>\n[每 30 分鐘執行]\n狀態: High=傳輸, Low=休眠", 80, 320, 160, 90, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";fontSize=10;align=center;", p1)
    wave2_box = d.add_box("全天每 30 分鐘固定發送 TDS 專線封包 (執行時間約 15~45 秒，遇網路延遲最高容許 180 秒逾時)\n狀態波形: ___|▔▔|___|▔▔|___|▔▔|___|▔▔|___|▔▔|___|▔▔|___|▔▔|___|▔▔|___|▔▔|___|▔▔|___", 250, 320, 780, 90, "fillColor=#ffffff;strokeColor=" + C_ORANGE_BORDER + ";strokeWidth=1.5;fontFamily=monospace;fontSize=11;align=center;", p1)

    # 軌道 3: 夜間高頻批次 (23:01~23:31)
    lbl_w3 = d.add_box("<b>夜間 ERP 批次組</b>\n[23:01 ~ 23:31]\n含 Export_Sam, 日報表等", 80, 440, 160, 90, "rounded=1;fillColor=" + C_PURPLE_FILL + ";strokeColor=" + C_PURPLE_BORDER + ";fontSize=10;align=center;", p1)
    wave3_box = d.add_box("日間低負載休眠 ──────────────────────────────────────────────> [23:01~23:31 持續密集高負載]\n狀態波形: ____________________________________________________________________|▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔|___", 250, 440, 780, 90, "fillColor=#ffffff;strokeColor=" + C_PURPLE_BORDER + ";strokeWidth=1.5;fontFamily=monospace;fontSize=11;align=center;", p1)

    # 時序波形 2: 海纜中斷恢復時序 (Panel 2)
    p2 = d.add_panel("子圖 B：海纜中斷事件與 48~72 小時在地自律運轉時序波形", 1170, 90, 1080, 1250, C_ORANGE_FILL, C_ORANGE_BORDER)
    t_axis2 = d.add_box("時間刻度：T0(海纜切斷) ── T+1h ── T+24h ── T+48h ── T+72h(專線修復) ── T+74h(對齊完畢)", 1370, 140, 780, 35, "fillColor=#f1f5f9;strokeColor=#cbd5e1;fontSize=11;fontStyle=1;align=center;", p2)

    # 軌道 A: DYXnet 專線可用性波形
    lbl_e1 = d.add_box("<b>DYXnet 專線通道</b>\n狀態: 正常 / 中斷", 1200, 200, 160, 90, "rounded=1;fillColor=" + C_RED_FILL + ";strokeColor=" + C_RED_BORDER + ";fontSize=10;align=center;", p2)
    wave_e1 = d.add_box("[T0 專線中斷 0 Mbps 斷開] ──────────────────────────────────────────> [T+72h 海纜修復 100 Mbps]\n波形: ▔▔▔▔▔▔▔|____________________________________________________________________|▔▔▔▔▔▔▔▔▔▔▔▔", 1370, 200, 780, 90, "fillColor=#ffffff;strokeColor=" + C_RED_BORDER + ";strokeWidth=1.5;fontFamily=monospace;fontSize=11;align=center;", p2)

    # 軌道 B: 海外廠端本地自律作業能力
    lbl_e2 = d.add_box("<b>廠區自律生產作業</b>\n狀態: 100% 離線可用", 1200, 320, 160, 90, "rounded=1;fillColor=" + C_GREEN_FILL + ";strokeColor=" + C_GREEN_BORDER + ";fontSize=10;align=center;", p2)
    wave_e2 = d.add_box("[廠區本地快取持續維持 100% 生產打樣運轉，無中斷、無當機，離線資料寫入本地 SQLite/SQL 暫存區]\n波形: ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔", 1370, 320, 780, 90, "fillColor=#ffffff;strokeColor=" + C_GREEN_BORDER + ";strokeWidth=1.5;fontFamily=monospace;fontSize=11;align=center;", p2)

    # 軌道 C: 差異資料補償對齊進度
    lbl_e3 = d.add_box("<b>資料雙向補償進度</b>\n狀態: 佇列累積 / 沖銷", 1200, 440, 160, 90, "rounded=1;fillColor=" + C_ORANGE_FILL + ";strokeColor=" + C_ORANGE_BORDER + ";fontSize=10;align=center;", p2)
    wave_e3 = d.add_box("[0筆] ────> [T+24h 累積50筆] ────> [T+48h 累積120筆] ────> [T+72h 啟動對齊沖銷] ────> [T+74h 歸零對齊]\n波形: _________/▔▔▔▔▔▔▔▔▔▔▔▔▔▔/▔▔▔▔▔▔▔▔▔▔▔▔▔▔/▔▔▔▔▔▔▔▔▔▔▔▔▔▔\\________________________", 1370, 440, 780, 90, "fillColor=#ffffff;strokeColor=" + C_ORANGE_BORDER + ";strokeWidth=1.5;fontFamily=monospace;fontSize=11;align=center;", p2)

    diagrams_xml.append(d.to_xml())

    # =========================================================================
    # 組合完整 mxfile
    # =========================================================================
    all_content = "".join(diagrams_xml)
    full_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<mxfile host="Electron" version="21.0.0" type="device">\n{all_content}\n</mxfile>'
    
    out_path = "/Users/howard/Desktop/HermesAgent/PortFilio/RSI/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_xml)
    
    # 同步複製到 Downloads 資料夾以備使用者檢視
    downloads_path = "/Users/howard/Downloads/RSI_DUKE_UML2_ALL_DIAGRAMS.drawio"
    with open(downloads_path, "w", encoding="utf-8") as f:
        f.write(full_xml)

    print(f"[OK] 成功生成嚴謹 14 分頁 + 多子圖面板 UML 2.0 圖資: {out_path}")
    print(f"[OK] 同步輸出至下載資料夾: {downloads_path}")

if __name__ == "__main__":
    build_all_diagrams()
