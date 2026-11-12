#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
依據 Duka (Duke) 2026-11-12 交付之真實規格（API List 與 RD_SAMPLE 示範範本）
全量生成 UML 2 全部 14 張架構圖資之 draw.io 多頁 XML 檔與線上檢視入口。
依使用者指示：全部 D365 服務為 C# 撰寫（非 X++）。
"""

import os
import html
import base64
import urllib.parse
import xml.etree.ElementTree as ET

# Duke's Official Color Palette
C_BLUE_FILL   = "#d0e1fd"
C_BLUE_LINE   = "#1d63ed"
C_YELLOW_FILL = "#fff2cc"
C_YELLOW_LINE = "#d6b656"
C_GREEN_FILL  = "#d5e8d4"
C_GREEN_LINE  = "#82b366"
C_PURPLE_FILL = "#e1d5e7"
C_PURPLE_LINE = "#9673a6"
C_ORANGE_FILL = "#ffe6cc"
C_ORANGE_LINE = "#d79b00"
C_RED_FILL    = "#f8cecc"
C_RED_LINE    = "#b85450"
C_GRAY_FILL   = "#f5f5f5"
C_GRAY_LINE   = "#666666"

class DrawioDiagramBuilder:
    def __init__(self, diag_id, diag_name, width=1600, height=1100):
        self.diag_id = diag_id
        self.diag_name = diag_name
        self.width = width
        self.height = height
        self.cells = []
        self.cell_id_counter = 2
        # Root cells
        self.cells.append('<mxCell id="0"/>')
        self.cells.append('<mxCell id="1" parent="0"/>')

    def add_node(self, text, x, y, w, h, style):
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        escaped_val = html.escape(text).replace("\n", "&#xa;")
        cell_xml = f'<mxCell id="{cid}" value="{escaped_val}" style="{style}" vertex="1" parent="1">'
        cell_xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        cell_xml += '</mxCell>'
        self.cells.append(cell_xml)
        return cid

    def add_edge(self, text, source_id, target_id, style):
        cid = str(self.cell_id_counter)
        self.cell_id_counter += 1
        escaped_val = html.escape(text).replace("\n", "&#xa;")
        cell_xml = f'<mxCell id="{cid}" value="{escaped_val}" style="{style}" edge="1" parent="1" source="{source_id}" target="{target_id}">'
        cell_xml += '<mxGeometry relative="1" as="geometry"/>'
        cell_xml += '</mxCell>'
        self.cells.append(cell_xml)
        return cid

    def to_xml(self):
        body = "".join(self.cells)
        return f'<diagram id="{self.diag_id}" name="{html.escape(self.diag_name)}"><mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.width}" pageHeight="{self.height}" math="0" shadow="0"><root>{body}</root></mxGraphModel></diagram>'


def create_all_14_diagrams():
    diagrams = []

    # =========================================================================
    # 01. Class Diagram (類別圖)
    # =========================================================================
    d01 = DrawioDiagramBuilder("d01_class", "01. Class Diagram (類別圖)")
    title01 = d01.add_node("【UML 2 類別圖】RD_SAMPLE 與 D365 C# 服務領域物件模型\n(依 Duke 交付規格：全面以 C# 實作，繼承 RqtBaseForm 與 RSI_RT 規範)", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    # RqtBaseForm (Abstract Base Class)
    c_rqt = d01.add_node(
        "&lt;&lt;abstract&gt;&gt;&#xa;RqtBaseForm (C# Core Model)&#xa;--&#xa;"
        "+ SalesId : string [SO編號]&#xa;"
        "+ StyleNo : string [款號]&#xa;"
        "+ ContractNo : string [合同編號]&#xa;"
        "+ ContractGroup : string [合同群組]&#xa;"
        "+ PurchId : string [PO編號]&#xa;"
        "+ ItemId : string [物料編號]&#xa;"
        "+ VendId : string [供應商編號]&#xa;"
        "+ CustId : string [客戶編號]&#xa;"
        "+ _key : string [Buy Name]&#xa;"
        "+ BuyKeys : List&lt;long&gt; [RecId清單]&#xa;"
        "+ ContractNos : List&lt;string&gt;&#xa;"
        "+ BatchNos : List&lt;string&gt;&#xa;"
        "+ DataAreaId : string [公司代碼, 預設RSI]&#xa;"
        "+ UserName : string [匯出人帳號]&#xa;--&#xa;"
        "+ Validate() : bool&#xa;"
        "+ ToParameterDictionary() : IDictionary",
        50, 100, 280, 310,
        f"swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontSize=11;"
    )

    # ReportRequest (C# 外掛 Report API)
    c_rpt = d01.add_node(
        "D365ReportServiceRequest&#xa;--&#xa;"
        "+ ReportType : EnumReport&#xa;"
        "+ MarkerLayoutId : string [馬克圖ID]&#xa;"
        "+ OutputFormat : string [PDF/Excel]&#xa;--&#xa;"
        "+ GenerateReportAsync() : Task&lt;string&gt; [下載URL]&#xa;"
        "+ ExportMarkPlan() : string",
        50, 460, 280, 150,
        f"swimlane;fontStyle=1;align=center;verticalAlign=top;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontSize=11;"
    )

    # RSI_RT (C# Return Envelope)
    c_rt = d01.add_node(
        "RSI_RT&lt;T&gt; (C# 統一回應封裝)&#xa;--&#xa;"
        "+ IsValid : bool [是否成功]&#xa;"
        "+ Msg : string [錯誤或回傳訊息]&#xa;"
        "+ TotalCount : int [資料總筆數]&#xa;"
        "+ DataList : List&lt;T&gt; [業務實體集合]&#xa;--&#xa;"
        "+ Success(data : List&lt;T&gt;) : RSI_RT&lt;T&gt;&#xa;"
        "+ Failure(errorMsg : string) : RSI_RT&lt;T&gt;",
        380, 100, 280, 180,
        f"swimlane;fontStyle=1;align=center;verticalAlign=top;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontSize=11;"
    )

    # D365 C# Custom Service
    c_csharp_svc = d01.add_node(
        "&lt;&lt;service&gt;&gt;&#xa;D365CSharpServices (31 Service / 80 Ops)&#xa;--&#xa;"
        "+ JCOM_WebServices : Module&#xa;"
        "+ RSI_WebServices : Module&#xa;"
        "- _tokenProvider : IAzureAdTokenProvider&#xa;--&#xa;"
        "+ GetStyleBom(styleNo : string) : RSI_RT&lt;BomItem&gt;&#xa;"
        "+ QueryInventory(itemId : string) : RSI_RT&lt;Stock&gt;&#xa;"
        "+ SyncPurchOrder(purchId : string) : RSI_RT&lt;PO&gt;&#xa;"
        "+ Execute80OperationsAsync() : Task",
        380, 320, 280, 180,
        f"swimlane;fontStyle=1;align=center;verticalAlign=top;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontSize=11;"
    )

    # RD_SAMPLE MoHeader
    c_mo = d01.add_node(
        "MoHeader (樣品單主檔 - SAM DB)&#xa;--&#xa;"
        "+ MoNo : string [PK, 樣品單號]&#xa;"
        "+ StyleNo : string [FK, 款號]&#xa;"
        "+ Season : string [季節代碼]&#xa;"
        "+ CustomerId : string [客戶編號]&#xa;"
        "+ TechPackVersion : string [TP版本]&#xa;"
        "+ TargetFactory : string [RSV/RSG]&#xa;"
        "+ Status : EnumMoStatus&#xa;"
        "+ CreatedDate : DateTime&#xa;--&#xa;"
        "+ CreateMo() : bool&#xa;"
        "+ DispatchToFactory(facCode : string) : void",
        710, 100, 270, 210,
        f"swimlane;fontStyle=1;align=center;verticalAlign=top;fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};fontSize=11;"
    )

    # RD_SAMPLE MoDetail
    c_modetail = d01.add_node(
        "MoDetail (樣品單明細 - SAM DB)&#xa;--&#xa;"
        "+ DetailId : long [PK]&#xa;"
        "+ MoNo : string [FK]&#xa;"
        "+ ColorCode : string [顏色代碼]&#xa;"
        "+ SizeCode : string [尺碼代碼]&#xa;"
        "+ OrderQty : int [打樣數量]&#xa;"
        "+ CutQty : int [裁剪數量]&#xa;"
        "+ SewnQty : int [車縫完成量]&#xa;--&#xa;"
        "+ UpdateSewnProgress(qty : int) : void",
        710, 350, 270, 180,
        f"swimlane;fontStyle=1;align=center;verticalAlign=top;fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};fontSize=11;"
    )

    # DataAccess (ADO.NET Direct SQL)
    c_dal = d01.add_node(
        "&lt;&lt;utility&gt;&gt;&#xa;DataAccess (自寫 ADO.NET 直下SQL)&#xa;--&#xa;"
        "- _connectionString : string [sa帳號明碼]&#xa;"
        "+ SqlOccurrencesCount : int = 1490 [SAM庫]&#xa;"
        "+ AxDbQueryCount : int = 23 [AXDB庫]&#xa;--&#xa;"
        "+ ExecuteQuery(sql : string) : DataTable&#xa;"
        "+ ExecuteNonQuery(sql : string) : int&#xa;"
        "+ OpenConnection() : SqlConnection",
        1030, 100, 260, 180,
        f"swimlane;fontStyle=1;align=center;verticalAlign=top;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontSize=11;"
    )

    # Python TechPack Parser
    c_py = d01.add_node(
        "&lt;&lt;external CLI&gt;&gt;&#xa;PythonTechPackParser (I04)&#xa;--&#xa;"
        "+ ScriptPath : string = 'techpack_cli.py'&#xa;"
        "+ SupportedFormats : List&lt;string&gt; [PDF, AI]&#xa;--&#xa;"
        "+ ParsePdf(pdfPath : string) : JsonSchema&#xa;"
        "+ ExtractMeasurements() : DataTable",
        1030, 330, 260, 150,
        f"swimlane;fontStyle=1;align=center;verticalAlign=top;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontSize=11;"
    )

    # Edges for Class Diagram
    d01.add_edge("inherits", c_rpt, c_rqt, "endArrow=block;endFill=0;dashed=0;strokeColor=#666;")
    d01.add_edge("returns RSI_RT", c_csharp_svc, c_rt, "endArrow=open;dashed=1;strokeColor=#666;")
    d01.add_edge("1..*", c_mo, c_modetail, "endArrow=diamond;endFill=1;strokeColor=#333;headLabel=1..*;")
    d01.add_edge("1,490 處直接 SQL", c_mo, c_dal, "endArrow=classic;dashed=1;strokeColor=#d79b00;labelBackgroundColor=#fff;")
    d01.add_edge("I04 解析產出", c_py, c_mo, "endArrow=classic;strokeColor=#1d63ed;")
    diagrams.append(d01)

    # =========================================================================
    # 02. Component Diagram (元件圖)
    # =========================================================================
    d02 = DrawioDiagramBuilder("d02_component", "02. Component Diagram (元件圖)")
    d02.add_node("【UML 2 元件圖】RD_SAMPLE 系統組成、核心元件與微服務邊界拓撲", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    comp_web = d02.add_node("&lt;&lt;component&gt;&gt;&#xa;RD_Sample.Web&#xa;(ASP.NET WebForms 4.8 / IIS)", 60, 120, 240, 100, f"shape=component;align=left;spacingLeft=36;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    comp_batch = d02.add_node("&lt;&lt;component&gt;&gt;&#xa;RD_Batch.Console&#xa;(Windows 工作排程 13 任務)", 60, 280, 240, 100, f"shape=component;align=left;spacingLeft=36;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    comp_dal = d02.add_node("&lt;&lt;component&gt;&gt;&#xa;DataAccess.Core&#xa;(自寫 ADO.NET 直下 SQL)", 380, 190, 220, 90, f"shape=component;align=left;spacingLeft=36;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    comp_py = d02.add_node("&lt;&lt;component&gt;&gt;&#xa;TechPack Parser&#xa;(Python 獨立程序 I04)", 60, 430, 240, 80, f"shape=component;align=left;spacingLeft=36;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    
    comp_d365 = d02.add_node("&lt;&lt;component&gt;&gt;&#xa;D365 C# Integration Services&#xa;(Report.Service :8085 / 80 Ops)", 680, 100, 260, 100, f"shape=component;align=left;spacingLeft=36;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;")
    comp_cqs = d02.add_node("&lt;&lt;component&gt;&gt;&#xa;CQS 品管服務&#xa;(.NET 8 Core / ARR Proxy :8012)", 680, 240, 260, 90, f"shape=component;align=left;spacingLeft=36;fillColor={C_GREEN_FILL};strokeColor={C_GREEN_LINE};fontStyle=1;")
    comp_yarp = d02.add_node("&lt;&lt;component&gt;&gt;&#xa;[處方推薦] YARP API Gateway&#xa;(在地端零信任防護閘道)", 680, 380, 260, 90, f"shape=component;align=left;spacingLeft=36;fillColor={C_RED_FILL};strokeColor={C_RED_LINE};fontStyle=1;")
    
    comp_db_sam = d02.add_node("&lt;&lt;database&gt;&gt;&#xa;SAM 主資料庫&#xa;(SQL Server 1433)", 1020, 180, 180, 90, f"shape=cylinder;fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};fontStyle=1;")
    comp_db_ax = d02.add_node("&lt;&lt;database&gt;&gt;&#xa;rsiaxdb1 (AXDB)&#xa;(D365 營運主庫)", 1020, 320, 180, 90, f"shape=cylinder;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;")

    d02.add_edge("調用", comp_web, comp_dal, "endArrow=open;strokeColor=#1d63ed;")
    d02.add_edge("調用 (13 項排程)", comp_batch, comp_dal, "endArrow=open;strokeColor=#1d63ed;dashed=1;")
    d02.add_edge("I04 本地程序呼叫", comp_web, comp_py, "endArrow=open;strokeColor=#333;")
    d02.add_edge("I02: 1490 SQL", comp_dal, comp_db_sam, "endArrow=open;strokeColor=#d6b656;fontStyle=1;")
    d02.add_edge("I07: 23 SQL", comp_dal, comp_db_ax, "endArrow=open;strokeColor=#b85450;fontStyle=1;")
    d02.add_edge("I08: Bearer Token (C#)", comp_web, comp_d365, "endArrow=open;strokeColor=#9673a6;")
    d02.add_edge("I13: HTTP REST", comp_web, comp_cqs, "endArrow=open;strokeColor=#82b366;")
    d02.add_edge("資安收攏轉發", comp_yarp, comp_d365, "endArrow=open;strokeColor=#b85450;dashed=1;")
    diagrams.append(d02)

    # =========================================================================
    # 03. Deployment Diagram (部署圖)
    # =========================================================================
    d03 = DrawioDiagramBuilder("d03_deploy", "03. Deployment Diagram (部署圖)")
    d03.add_node("【UML 2 部署圖】全集團實體伺服器、網路節點、專線與雲端拓撲 (依 Duke 節點表)", 40, 20, 1200, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")

    # RDSMP2 正式機
    node_smp2 = d03.add_node(
        "&lt;&lt;device&gt;&gt;&#xa;RDSMP2 正式伺服器 (192.168.0.22)&#xa;--&#xa;"
        "• IIS 443/80 (rdsample.rsiapparel.com)&#xa;"
        "• SQL Server 2019 (1433) [SAM, PDFTAG, IEPortal, CQS]&#xa;"
        "• Windows 排程 D:\\EXP (13 項核心批次)&#xa;"
        "• 網路芳鄰 SMB 445 (hrm, web_backup)&#xa;"
        "• 實體儲存 E:\\RD_SAMPLE (樣品工藝圖檔)",
        50, 100, 350, 220,
        f"swimlane;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=11;align=center;"
    )

    # RDSMP1 測試機
    node_smp1 = d03.add_node(
        "&lt;&lt;device&gt;&gt;&#xa;RDSMP1 測試伺服器 (192.168.0.23)&#xa;--&#xa;"
        "• IIS 80 (test-rdsample.rsiapparel.com)&#xa;"
        "• SQL Server 1433 (SAM 正式副本、PDFTAG)&#xa;"
        "• CQS 品質微服務 (Port 8012 / 8011)&#xa;"
        "• FindImage 影像比對服務 (Port 8081)&#xa;"
        "• GitLab Runner (CI/CD 自動化 MSBuild)",
        50, 360, 350, 200,
        f"swimlane;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=11;align=center;"
    )

    # D365 外掛主機 RSIMDW1
    node_mdw1 = d03.add_node(
        "&lt;&lt;device&gt;&gt;&#xa;RSIMDW1 (192.168.0.95)&#xa;--&#xa;"
        "• D365.Report.Service (:8085 / :8082 UAT)&#xa;"
        "• Local.WebApi (:80 / :8081 UAT)&#xa;"
        "• D365_Prod 唯讀庫 (SQL 1433)&#xa;"
        "• Auth Token 服務 [全無驗證需收攏]",
        450, 100, 330, 180,
        f"swimlane;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;fontSize=11;align=center;"
    )

    # D365 核心叢集
    node_d365_core = d03.add_node(
        "&lt;&lt;device cluster&gt;&gt;&#xa;D365 AOS (192.168.0.124～.126)&#xa;+ rsiaxdb1 (192.168.0.131)&#xa;--&#xa;"
        "• D365 Core ERP (C# 80 Operations)&#xa;"
        "• AXDB 營運主資料庫 (SQL 1433)&#xa;"
        "• Entra ID Bearer 授權保護",
        450, 320, 330, 160,
        f"swimlane;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;fontSize=11;align=center;"
    )

    # 廠區節點 (越柬)
    node_factory = d03.add_node(
        "&lt;&lt;factory nodes via DYXnet 跨國專線&gt;&gt;&#xa;--&#xa;"
        "• 越南 RDV 廠區 DB (192.168.185.123:1433)&#xa;"
        "• 柬埔寨 RDG 廠區 DB (192.168.193.65:1433)&#xa;"
        "• [已停用] 桃園 TY DB (192.168.5.123)",
        830, 100, 340, 150,
        f"swimlane;fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};fontStyle=1;fontSize=11;align=center;"
    )

    # 外部雲端
    node_cloud = d03.add_node(
        "&lt;&lt;public cloud / external&gt;&gt;&#xa;AWS EC2 &amp; Group Mail&#xa;--&#xa;"
        "• AWS AI 推論服務 (98.84.29.205:8000 HTTP)&#xa;"
        "• AWS 跨國翻譯服務 (98.93.175.234:80 HTTP)&#xa;"
        "• 集團 SMTP 郵件主機 (192.168.8.64:587)",
        830, 300, 340, 150,
        f"swimlane;fillColor={C_RED_FILL};strokeColor={C_RED_LINE};fontStyle=1;fontSize=11;align=center;"
    )

    # Edges
    d03.add_edge("I05: 每30分鐘專線 TDS 1433 直連", node_smp2, node_factory, "strokeColor=#d79b00;fontStyle=1;strokeWidth=2;")
    d03.add_edge("I08/I09: 讀取 D365_Prod", node_smp2, node_mdw1, "strokeColor=#9673a6;")
    d03.add_edge("I07: 23 處 Direct SQL", node_smp2, node_d365_core, "strokeColor=#b85450;strokeWidth=2;dashed=1;")
    d03.add_edge("I16/I17: HTTP API 調用", node_smp2, node_cloud, "strokeColor=#b85450;")
    d03.add_edge("I21: CI/CD robocopy 部署", node_smp1, node_smp2, "strokeColor=#1d63ed;dashed=1;")
    diagrams.append(d03)

    # =========================================================================
    # 04. Package Diagram (套件圖)
    # =========================================================================
    d04 = DrawioDiagramBuilder("d04_package", "04. Package Diagram (套件圖)")
    d04.add_node("【UML 2 套件圖】集團軟體命名空間、分層模組架構與依賴關係 (依 Duke 程式組成)", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    pkg_pres = d04.add_node("package RSI.RDSample.Presentation\n--\n+ WebForms Pages (.aspx)\n+ jQuery & Knockout ViewModels\n+ jqxGrid Data Grids", 60, 120, 260, 140, f"shape=folder;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;tabPosition=left;tabWidth=140;")
    pkg_bll = d04.add_node("package RSI.RDSample.BusinessLogic\n--\n+ SampleOrderManager\n+ TechPackIngestionService\n+ SmvEstimationEngine\n+ CrossBorderSyncOrchestrator", 380, 120, 260, 140, f"shape=folder;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;tabPosition=left;tabWidth=140;")
    pkg_dal = d04.add_node("package RSI.Core.DataAccess\n--\n+ SqlServerDirectAccessor\n+ OracleDbDriver\n+ DbConnectionPoolManager", 700, 120, 260, 140, f"shape=folder;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;tabPosition=left;tabWidth=140;")
    
    pkg_batch = d04.add_node("package RSI.RDSample.RD_Batch\n--\n+ NotificationDispatcher\n+ FactorySyncExecutor\n+ ErpMasterSyncScheduler\n+ FitSopCalculator", 60, 320, 260, 140, f"shape=folder;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;tabPosition=left;tabWidth=140;")
    pkg_d365 = d04.add_node("package RSI.D365.Services (C#)\n--\n+ JCOM_WebServices (C#)\n+ RSI_WebServices (C#)\n+ D365.Report.Service\n+ Local.WebApi", 380, 320, 260, 140, f"shape=folder;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;tabPosition=left;tabWidth=140;")
    pkg_cqs = d04.add_node("package RSI.Quality.CQS (.NET 8)\n--\n+ InspectionController\n+ QualityAuditService\n+ ArrReverseProxyConfig", 700, 320, 260, 140, f"shape=folder;fillColor={C_GREEN_FILL};strokeColor={C_GREEN_LINE};fontStyle=1;tabPosition=left;tabWidth=140;")

    d04.add_edge("depends on", pkg_pres, pkg_bll, "endArrow=open;dashed=1;strokeColor=#1d63ed;")
    d04.add_edge("depends on", pkg_bll, pkg_dal, "endArrow=open;dashed=1;strokeColor=#1d63ed;")
    d04.add_edge("depends on", pkg_batch, pkg_dal, "endArrow=open;dashed=1;strokeColor=#1d63ed;")
    d04.add_edge("invokes C# APIs", pkg_bll, pkg_d365, "endArrow=open;dashed=1;strokeColor=#9673a6;")
    d04.add_edge("integrates", pkg_bll, pkg_cqs, "endArrow=open;dashed=1;strokeColor=#82b366;")
    diagrams.append(d04)

    # =========================================================================
    # 05. Object Diagram (物件圖 - 執行時期快照)
    # =========================================================================
    d05 = DrawioDiagramBuilder("d05_object", "05. Object Diagram (物件圖)")
    d05.add_node("【UML 2 物件圖】RD_SAMPLE 運行時期真實單據、執行個體快照 (Instance Snapshot)", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    obj_mo = d05.add_node("<u>activeMo : MoHeader</u>\n--\nMoNo = \"MO-202611-0089\"\nStyleNo = \"ST-NIK-902\"\nSeason = \"2027SS\"\nCustomerId = \"CUST-NIKE-01\"\nTargetFactory = \"RSV\"\nStatus = SewingInProgress", 60, 120, 250, 150, f"fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};fontStyle=0;align=center;")
    obj_item1 = d05.add_node("<u>itemBlackL : MoDetail</u>\n--\nDetailId = 10402\nColorCode = \"BLK-01\"\nSizeCode = \"L\"\nOrderQty = 30\nSewnQty = 25", 60, 320, 250, 130, f"fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};align=center;")
    obj_rqt = d05.add_node("<u>exportRqt : RqtBaseForm</u>\n--\nSalesId = \"SO-2026-8812\"\nStyleNo = \"ST-NIK-902\"\nDataAreaId = \"RSV\"\nUserName = \"duka.chen\"\nBuyKeys = [90812, 90815]", 380, 120, 260, 140, f"fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};align=center;")
    obj_resp = d05.add_node("<u>d365Rt : RSI_RT</u>\n--\nIsValid = true\nMsg = \"SUCCESS\"\nTotalCount = 1\nDataList = [\"http://192.168.0.95:8085/dl/mk902.pdf\"]", 380, 320, 260, 130, f"fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};align=center;")
    obj_batch = d05.add_node("<u>rsvSyncTask : ScheduledTask</u>\n--\nTaskName = \"Sync_RSV.bat\"\nExecTime = \"14:30:00\"\nTargetIP = \"192.168.185.123:1433\"\nLastStatus = \"Success\"\nDuration = \"4.2s\"", 700, 120, 260, 140, f"fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};align=center;")

    d05.add_edge("contains", obj_mo, obj_item1, "strokeColor=#333;endArrow=none;")
    d05.add_edge("associated with", obj_mo, obj_rqt, "strokeColor=#9673a6;endArrow=none;dashed=1;")
    d05.add_edge("yields", obj_rqt, obj_resp, "strokeColor=#9673a6;endArrow=none;")
    d05.add_edge("syncs Mo", obj_batch, obj_mo, "strokeColor=#d79b00;endArrow=none;dashed=1;")
    diagrams.append(d05)

    # =========================================================================
    # 06. Composite Structure Diagram (複合結構圖)
    # =========================================================================
    d06 = DrawioDiagramBuilder("d06_composite", "06. Composite Structure Diagram (複合結構圖)")
    d06.add_node("【UML 2 複合結構圖】RD_SAMPLE 內部微結構、通訊埠 (Ports) 與內部組件裝配", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    box_host = d06.add_node("RD_Sample_Host_Environment (RDSMP2)", 80, 100, 800, 450, f"swimlane;fillColor=#f8f9fa;strokeColor=#495057;fontStyle=1;")
    part_web = d06.add_node("webApp : ASP.NET Runtime", 140, 160, 220, 90, f"fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};")
    part_batch = d06.add_node("batchRunner : BatchProcess", 140, 310, 220, 90, f"fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};")
    part_dal = d06.add_node("dalBridge : DataAccessBridge", 440, 230, 220, 100, f"fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};")
    
    # Ports on the boundary
    port1 = d06.add_node("p1: Port&#xa;HTTPS 443", 60, 180, 50, 40, "fillColor=#fff;strokeColor=#000;fontSize=9;")
    port2 = d06.add_node("p2: Port&#xa;TDS 1433", 860, 260, 50, 40, "fillColor=#fff;strokeColor=#000;fontSize=9;")
    port3 = d06.add_node("p3: Port&#xa;REST :8085", 860, 160, 50, 40, "fillColor=#fff;strokeColor=#000;fontSize=9;")

    d06.add_edge("", port1, part_web, "endArrow=none;strokeColor=#333;")
    d06.add_edge("", part_web, part_dal, "endArrow=none;strokeColor=#333;")
    d06.add_edge("", part_batch, part_dal, "endArrow=none;strokeColor=#333;")
    d06.add_edge("", part_dal, port2, "endArrow=none;strokeColor=#333;")
    d06.add_edge("", part_web, port3, "endArrow=none;strokeColor=#333;")
    diagrams.append(d06)

    # =========================================================================
    # 07. Profile Diagram (輪廓圖 / 剖面圖)
    # =========================================================================
    d07 = DrawioDiagramBuilder("d07_profile", "07. Profile Diagram (輪廓圖)")
    d07.add_node("【UML 2 輪廓圖】蜂巢計畫領域專用擴充 Stereotypes 剖面定義", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    st_csharp = d07.add_node("&lt;&lt;stereotype&gt;&gt;&#xa;CSharpService&#xa;--&#xa;+ framework: \".NET 4.8\" | \".NET 8\"&#xa;+ operationsCount: int&#xa;+ authType: \"None\" | \"Bearer\"", 60, 120, 240, 130, f"fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;")
    st_sql = d07.add_node("&lt;&lt;stereotype&gt;&gt;&#xa;DirectSQL&#xa;--&#xa;+ occurrences: int&#xa;+ isSaAccount: bool = true&#xa;+ targetDatabase: string", 350, 120, 240, 130, f"fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};fontStyle=1;")
    st_cross = d07.add_node("&lt;&lt;stereotype&gt;&gt;&#xa;CrossBorderRPC&#xa;--&#xa;+ provider: \"DYXnet\"&#xa;+ protocol: \"TDS 1433\"&#xa;+ offlineToleranceHours: int = 72", 640, 120, 240, 130, f"fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};fontStyle=1;")
    st_batch = d07.add_node("&lt;&lt;stereotype&gt;&gt;&#xa;BatchSchedule&#xa;--&#xa;+ frequency: string&#xa;+ scriptPath: string&#xa;+ sendsNotification: bool", 930, 120, 240, 130, f"fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    
    meta_comp = d07.add_node("&lt;&lt;metaclass&gt;&gt;&#xa;Component", 200, 320, 160, 70, "fillColor=#e0e0e0;strokeColor=#666;fontStyle=1;")
    meta_conn = d07.add_node("&lt;&lt;metaclass&gt;&gt;&#xa;Connector", 500, 320, 160, 70, "fillColor=#e0e0e0;strokeColor=#666;fontStyle=1;")
    meta_oper = d07.add_node("&lt;&lt;metaclass&gt;&gt;&#xa;Operation", 800, 320, 160, 70, "fillColor=#e0e0e0;strokeColor=#666;fontStyle=1;")

    d07.add_edge("&lt;&lt;extend&gt;&gt;", st_csharp, meta_comp, "endArrow=block;endFill=1;strokeColor=#666;")
    d07.add_edge("&lt;&lt;extend&gt;&gt;", st_sql, meta_conn, "endArrow=block;endFill=1;strokeColor=#666;")
    d07.add_edge("&lt;&lt;extend&gt;&gt;", st_cross, meta_conn, "endArrow=block;endFill=1;strokeColor=#666;")
    d07.add_edge("&lt;&lt;extend&gt;&gt;", st_batch, meta_oper, "endArrow=block;endFill=1;strokeColor=#666;")
    diagrams.append(d07)

    # =========================================================================
    # 08. Use Case Diagram (使用案例圖)
    # =========================================================================
    d08 = DrawioDiagramBuilder("d08_usecase", "08. Use Case Diagram (使用案例圖)")
    d08.add_node("【UML 2 使用案例圖】研發打樣、跨國廠區車縫、ERP對齊與排程作業邊界", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    actor_rd = d08.add_node("總部打樣設計師&#xa;(HQ Designer)", 60, 160, 100, 120, "shape=actor;fillColor=#fff;strokeColor=#333;fontStyle=1;")
    actor_fac = d08.add_node("海外廠區生管&#xa;(RSV / RSG)", 60, 380, 100, 120, "shape=actor;fillColor=#fff;strokeColor=#333;fontStyle=1;")
    actor_sched = d08.add_node("Windows工作排程器&#xa;(Task Scheduler)", 1000, 160, 110, 120, "shape=actor;fillColor=#fff;strokeColor=#333;fontStyle=1;")
    actor_d365 = d08.add_node("D365 ERP (C#)&#xa;(Core Services)", 1000, 380, 110, 120, "shape=actor;fillColor=#fff;strokeColor=#333;fontStyle=1;")

    uc_mono = d08.add_node("UC01: 建立樣品單 (MoNo)", 300, 120, 220, 60, f"ellipse;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};")
    uc_tp = d08.add_node("UC02: Python 解析 TechPack", 300, 200, 220, 60, f"ellipse;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};")
    uc_sync = d08.add_node("UC03: 跨國專線 30 分鐘同步", 580, 140, 230, 60, f"ellipse;fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};")
    uc_sew = d08.add_node("UC04: 廠區車縫進度與回報", 300, 360, 220, 60, f"ellipse;fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};")
    uc_erp = d08.add_node("UC05: 每日 23:01 物料/顏色主檔同步", 580, 320, 240, 60, f"ellipse;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};")
    uc_mail = d08.add_node("UC06: 每 5 分鐘催辦通知信", 580, 230, 220, 60, f"ellipse;fillColor={C_RED_FILL};strokeColor={C_RED_LINE};")

    d08.add_edge("", actor_rd, uc_mono, "endArrow=none;strokeColor=#333;")
    d08.add_edge("", actor_rd, uc_tp, "endArrow=none;strokeColor=#333;")
    d08.add_edge("", actor_fac, uc_sew, "endArrow=none;strokeColor=#333;")
    d08.add_edge("", actor_sched, uc_sync, "endArrow=none;strokeColor=#333;")
    d08.add_edge("", actor_sched, uc_erp, "endArrow=none;strokeColor=#333;")
    d08.add_edge("", actor_sched, uc_mail, "endArrow=none;strokeColor=#333;")
    d08.add_edge("&lt;&lt;include&gt;&gt;", uc_sync, uc_sew, "endArrow=open;dashed=1;strokeColor=#d79b00;")
    d08.add_edge("&lt;&lt;invokes C#&gt;&gt;", uc_erp, actor_d365, "endArrow=open;dashed=1;strokeColor=#9673a6;")
    diagrams.append(d08)

    # =========================================================================
    # 09. Activity Diagram (活動圖)
    # =========================================================================
    d09 = DrawioDiagramBuilder("d09_activity", "09. Activity Diagram (活動圖)")
    d09.add_node("【UML 2 活動圖】樣品開單至出貨跨國協同泳道業務流程 (Swimlanes)", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    # Swimlane columns
    lane_hq = d09.add_node("總部研發 (HQ RD)", 60, 100, 260, 480, "swimlane;fillColor=#fafafa;strokeColor=#999;fontStyle=1;")
    lane_sch = d09.add_node("Windows 排程 (RD_Batch)", 320, 100, 260, 480, "swimlane;fillColor=#fafafa;strokeColor=#999;fontStyle=1;")
    lane_fac = d09.add_node("廠區生管 (RSV / RSG)", 580, 100, 260, 480, "swimlane;fillColor=#fafafa;strokeColor=#999;fontStyle=1;")
    lane_erp = d09.add_node("D365 ERP (C# Services)", 840, 100, 260, 480, "swimlane;fillColor=#fafafa;strokeColor=#999;fontStyle=1;")

    act_start = d09.add_node("", 175, 140, 30, 30, "ellipse;fillColor=#000;strokeColor=#000;")
    act_up = d09.add_node("上傳客戶 TechPack PDF", 110, 190, 160, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};")
    act_parse = d09.add_node("Python 解析工藝 BOM&#xa;直寫 SAM 庫 (sa帳號)", 110, 270, 160, 60, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};")
    act_erp_v = d09.add_node("驗證款號與物料資訊&#xa;(C# 80 Ops / OData)", 890, 270, 160, 60, f"rounded=1;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};")
    act_sync = d09.add_node("Sync_RSV.bat (每30分)&#xa;專線直推海外廠 SQL", 370, 360, 160, 60, f"rounded=1;fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};")
    act_sew = d09.add_node("排產車縫打樣&#xa;&amp; 錄入車縫報表", 630, 360, 160, 60, f"rounded=1;fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};")
    act_cqs = d09.add_node("CQS 品質檢驗放行", 630, 450, 160, 50, f"rounded=1;fillColor={C_GREEN_FILL};strokeColor={C_GREEN_LINE};")
    act_end = d09.add_node("", 695, 530, 30, 30, "ellipse;shape=endState;fillColor=#000;strokeColor=#000;")

    d09.add_edge("", act_start, act_up, "strokeColor=#333;")
    d09.add_edge("", act_up, act_parse, "strokeColor=#333;")
    d09.add_edge("I08 調用 C#", act_parse, act_erp_v, "strokeColor=#9673a6;strokeWidth=1;")
    d09.add_edge("放行", act_erp_v, act_sync, "strokeColor=#9673a6;")
    d09.add_edge("I05 專線寫庫", act_sync, act_sew, "strokeColor=#d79b00;strokeWidth=2;")
    d09.add_edge("", act_sew, act_cqs, "strokeColor=#333;")
    d09.add_edge("", act_cqs, act_end, "strokeColor=#333;")
    diagrams.append(d09)

    # =========================================================================
    # 10. State Machine Diagram (狀態機圖)
    # =========================================================================
    d10 = DrawioDiagramBuilder("d10_statemachine", "10. State Machine Diagram (狀態機圖)")
    d10.add_node("【UML 2 狀態機圖】樣品單 (MoNo) 完整生命週期狀態轉移模型", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    st_init = d10.add_node("", 60, 170, 30, 30, "ellipse;fillColor=#000;strokeColor=#000;")
    st_draft = d10.add_node("Draft&#xa;(草稿建立)", 140, 155, 120, 60, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    st_parsed = d10.add_node("TechPackParsed&#xa;(解析入庫完成)", 320, 155, 140, 60, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    st_synced = d10.add_node("SyncedToFactory&#xa;(專線同步至廠區)", 520, 155, 150, 60, f"rounded=1;fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};fontStyle=1;")
    st_sewing = d10.add_node("SewingInProgress&#xa;(廠區車縫排產中)", 730, 155, 150, 60, f"rounded=1;fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};fontStyle=1;")
    st_qc = d10.add_node("QC_Inspection&#xa;(品質檢驗錄入)", 730, 280, 150, 60, f"rounded=1;fillColor={C_GREEN_FILL};strokeColor={C_GREEN_LINE};fontStyle=1;")
    st_approved = d10.add_node("SampleApproved&#xa;(檢驗合格審批)", 520, 280, 150, 60, f"rounded=1;fillColor={C_GREEN_FILL};strokeColor={C_GREEN_LINE};fontStyle=1;")
    st_shipped = d10.add_node("Shipped&#xa;(出貨結案)", 320, 280, 140, 60, f"rounded=1;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;")
    st_final = d10.add_node("", 185, 295, 30, 30, "ellipse;shape=endState;fillColor=#000;strokeColor=#000;")

    d10.add_edge("MoNo 下單", st_init, st_draft, "strokeColor=#333;")
    d10.add_edge("I04 Python 抽取", st_draft, st_parsed, "strokeColor=#1d63ed;")
    d10.add_edge("I05 Sync_RSV.bat", st_parsed, st_synced, "strokeColor=#d79b00;")
    d10.add_edge("開裁車縫", st_synced, st_sewing, "strokeColor=#333;")
    d10.add_edge("車縫完成", st_sewing, st_qc, "strokeColor=#333;")
    d10.add_edge("CQS 放行通過", st_qc, st_approved, "strokeColor=#82b366;")
    d10.add_edge("報關交付", st_approved, st_shipped, "strokeColor=#333;")
    d10.add_edge("存檔封裝", st_shipped, st_final, "strokeColor=#333;")
    diagrams.append(d10)

    # =========================================================================
    # 11. Sequence Diagram (循序圖)
    # =========================================================================
    d11 = DrawioDiagramBuilder("d11_sequence", "11. Sequence Diagram (循序圖)")
    d11.add_node("【UML 2 循序圖】樣品開單、Python 解析、C# 服務調用與跨國排程同步時序", 40, 20, 1200, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    # Participants
    p_user = d11.add_node("設計師: Designer", 60, 100, 140, 40, "fillColor=#fff;strokeColor=#333;fontStyle=1;")
    p_web = d11.add_node("RDSMP2: WebForms", 240, 100, 150, 40, f"fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    p_py = d11.add_node("I04: Python Parser", 430, 100, 150, 40, f"fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    p_sam = d11.add_node("SAM DB (1433)", 620, 100, 140, 40, f"fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};fontStyle=1;")
    p_csharp = d11.add_node("D365 C# Svc (:8085)", 800, 100, 160, 40, f"fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;")
    p_rsv = d11.add_node("RDV 越南 DB (1433)", 1000, 100, 160, 40, f"fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};fontStyle=1;")

    # Lifeline bars
    l_user = d11.add_node("", 125, 140, 10, 420, "fillColor=#fff;strokeColor=#666;")
    l_web = d11.add_node("", 310, 140, 10, 420, "fillColor=#fff;strokeColor=#666;")
    l_py = d11.add_node("", 500, 140, 10, 420, "fillColor=#fff;strokeColor=#666;")
    l_sam = d11.add_node("", 685, 140, 10, 420, "fillColor=#fff;strokeColor=#666;")
    l_csharp = d11.add_node("", 875, 140, 10, 420, "fillColor=#fff;strokeColor=#666;")
    l_rsv = d11.add_node("", 1075, 140, 10, 420, "fillColor=#fff;strokeColor=#666;")

    # Interactions
    d11.add_edge("1. 上傳 TechPack PDF", l_user, l_web, "strokeColor=#333;endArrow=block;")
    d11.add_edge("2. 呼叫 CLI parse", l_web, l_py, "strokeColor=#1d63ed;endArrow=block;")
    d11.add_edge("3. 回傳工藝 JSON", l_py, l_web, "strokeColor=#1d63ed;dashed=1;endArrow=open;")
    d11.add_edge("4. ADO.NET 直下 SQL 寫庫", l_web, l_sam, "strokeColor=#d6b656;endArrow=block;")
    d11.add_edge("5. 調用 C# Report API (RqtBaseForm)", l_web, l_csharp, "strokeColor=#9673a6;endArrow=block;")
    d11.add_edge("6. 回傳下載 URL (無驗證)", l_csharp, l_web, "strokeColor=#9673a6;dashed=1;endArrow=open;")
    d11.add_edge("7. Sync_RSV.bat 排程 (每30分)", l_sam, l_rsv, "strokeColor=#d79b00;strokeWidth=2;endArrow=block;")
    diagrams.append(d11)

    # =========================================================================
    # 12. Communication Diagram (溝通圖 / 協作圖)
    # =========================================================================
    d12 = DrawioDiagramBuilder("d12_comm", "12. Communication Diagram (溝通圖)")
    d12.add_node("【UML 2 溝通圖】排程批次、資料存取與跨國資料庫拓撲協同鏈路", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    node_b = d12.add_node("<u>1: RD_Batch.Console</u>&#xa;(Windows工作排程器)", 450, 120, 200, 80, f"fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    node_s = d12.add_node("<u>2: SAM_Database</u>&#xa;(正式機 192.168.0.22)", 120, 280, 200, 80, f"fillColor={C_YELLOW_FILL};strokeColor={C_YELLOW_LINE};fontStyle=1;")
    node_e = d12.add_node("<u>3: D365 C# Services</u>&#xa;(外掛主機 192.168.0.95)", 450, 420, 200, 80, f"fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;")
    node_f = d12.add_node("<u>4: Factory_RSV_DB</u>&#xa;(越南 192.168.185.123)", 780, 280, 200, 80, f"fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};fontStyle=1;")

    d12.add_edge("1.1: 掃描待派工單\n1.2: 提取最新顏色物料", node_b, node_s, "strokeColor=#333;endArrow=none;")
    d12.add_edge("1.3: 每30分鐘 TDS 1433 寫入", node_b, node_f, "strokeColor=#d79b00;endArrow=none;strokeWidth=2;")
    d12.add_edge("1.4: 每日 23:01 同步 C# 主檔", node_b, node_e, "strokeColor=#9673a6;endArrow=none;")
    d12.add_edge("2.1: Linked Server MERGE", node_f, node_s, "strokeColor=#b85450;endArrow=none;dashed=1;")
    diagrams.append(d12)

    # =========================================================================
    # 13. Interaction Overview Diagram (互動概觀圖)
    # =========================================================================
    d13 = DrawioDiagramBuilder("d13_interact", "13. Interaction Overview Diagram (互動概觀圖)")
    d13.add_node("【UML 2 互動概觀圖】研發打樣高階控制流與嵌套循序作業全景", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    sd_init = d13.add_node("sd 樣品單初始與 TechPack 提取\n--\nref(SD_TechPack_Ingest)", 100, 120, 260, 100, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    sd_csharp = d13.add_node("sd D365 C# 規格與庫存驗證\n--\nref(SD_D365_CSharp_Verify)", 440, 120, 260, 100, f"rounded=1;fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;")
    sd_sync = d13.add_node("sd 跨國專線工單排程推送\n--\nref(SD_Factory_Sync_Batch)", 780, 120, 260, 100, f"rounded=1;fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};fontStyle=1;")
    sd_cqs = d13.add_node("sd 廠區車縫與 CQS 品檢回報\n--\nref(SD_CQS_Quality_Audit)", 780, 280, 260, 100, f"rounded=1;fillColor={C_GREEN_FILL};strokeColor={C_GREEN_LINE};fontStyle=1;")
    sd_report = d13.add_node("sd 每日車縫日報結算 (06:01)\n--\nref(SD_Daily_Sewn_Report)", 440, 280, 260, 100, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")

    d13.add_edge("BOM 提取成功", sd_init, sd_csharp, "strokeColor=#333;endArrow=block;")
    d13.add_edge("ERP 驗證無誤", sd_csharp, sd_sync, "strokeColor=#333;endArrow=block;")
    d13.add_edge("廠區接單", sd_sync, sd_cqs, "strokeColor=#333;endArrow=block;")
    d13.add_edge("每日匯總", sd_cqs, sd_report, "strokeColor=#333;endArrow=block;")
    diagrams.append(d13)

    # =========================================================================
    # 14. Timing Diagram (計時圖 / 時序圖)
    # =========================================================================
    d14 = DrawioDiagramBuilder("d14_timing", "14. Timing Diagram (計時圖)")
    d14.add_node("【UML 2 計時圖】13 項 Windows 排程工作時間軸與海纜延遲 SLA 狀態波形", 40, 20, 1100, 50, f"rounded=1;fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;fontSize=14;align=left;spacingLeft=15;")
    
    t_line1 = d14.add_node("SendNotification.bat&#xa;[每 5 分鐘輪詢]&#xa;Idle | Running", 60, 110, 220, 70, f"fillColor={C_RED_FILL};strokeColor={C_RED_LINE};fontStyle=1;")
    t_wave1 = d14.add_node("▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█▄█ (24小時全天不間斷)", 300, 110, 780, 70, "fillColor=#fff;strokeColor=#666;fontFamily=monospace;fontSize=12;align=center;")

    t_line2 = d14.add_node("Sync_RSV / RSG.bat&#xa;[每 30 分鐘跨國專線]&#xa;Active | Sleep (23-06)", 60, 200, 220, 70, f"fillColor={C_ORANGE_FILL};strokeColor={C_ORANGE_LINE};fontStyle=1;")
    t_wave2 = d14.add_node("████████████████████████████████████░░░░░░░░░░ (06:00~23:00 執行，深夜休眠)", 300, 200, 780, 70, "fillColor=#fff;strokeColor=#666;fontFamily=monospace;fontSize=12;align=center;")

    t_line3 = d14.add_node("ERP 夜間批次 (C#)&#xa;23:01 顏色 / 23:15 對照&#xa;23:19 新料 / 23:31 變更", 60, 290, 220, 80, f"fillColor={C_PURPLE_FILL};strokeColor={C_PURPLE_LINE};fontStyle=1;")
    t_wave3 = d14.add_node("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░[23:01][23:15][23:19][23:31] 高頻批次窗口", 300, 290, 780, 80, "fillColor=#fff;strokeColor=#666;fontFamily=monospace;fontSize=12;align=center;")

    t_line4 = d14.add_node("DYXnet 跨國專線狀態&#xa;正常 (Online)&#xa;斷網自律 (Offline)", 60, 390, 220, 80, f"fillColor={C_BLUE_FILL};strokeColor={C_BLUE_LINE};fontStyle=1;")
    t_wave4 = d14.add_node("══════════════════════ [海纜中斷事件] ── [48~72小時在地自律運轉] ──> [復原對齊]", 300, 390, 780, 80, "fillColor=#fff;strokeColor=#666;fontFamily=monospace;fontSize=12;align=center;fontStyle=1;")
    diagrams.append(d14)

    return diagrams


def build_multipage_drawio_file(output_path):
    diagrams = create_all_14_diagrams()
    xml_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_header += '<mxfile host="Electron" modified="2026-11-12T16:00:00.000Z" agent="Howard Agent" version="21.0.0" type="device">\n'
    diagrams_xml = "\n".join([d.to_xml() for d in diagrams])
    xml_footer = '\n</mxfile>'
    
    full_content = xml_header + diagrams_xml + xml_footer
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    print(f"[OK] Generated multi-page draw.io file with 14 diagrams: {output_path} ({len(full_content)} bytes)")
    return full_content


if __name__ == "__main__":
    base_dir = "/Users/howard/Desktop/HermesAgent/PortFilio/RSI"
    drawio_path = os.path.join(base_dir, "RSI_DUKE_UML2_ALL_DIAGRAMS.drawio")
    drawio_xml_path = os.path.join(base_dir, "RSI_DUKE_UML2_ALL_DIAGRAMS.drawio.xml")
    content = build_multipage_drawio_file(drawio_path)
    with open(drawio_xml_path, 'w', encoding='utf-8') as f:
        f.write(content)
