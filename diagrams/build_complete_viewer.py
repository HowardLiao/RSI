#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

def get_svg(index):
    w = 1600
    h = 950

    if index == 0:
        return f"""
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">01. UML 2.0 Class Diagram (類別圖) — 核心領域模型與跨系統資料契約</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 3 個獨立子圖面板 ｜ 依據 Duke 2026-11-12 交付架構</text>

              <!-- Panel 1 -->
              <g transform="translate(40, 90)">
                <rect width="480" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="480" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 A】D365 C# 服務契約與請求基底</text>
                
                <g transform="translate(20, 50)">
                  <rect width="440" height="240" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <rect width="440" height="30" fill="#0284c7"/>
                  <text x="220" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&lt;&lt;abstract&gt;&gt; RqtBaseForm</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ SalesId, StyleNo, ContractNo, PurchId : string</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ ItemId, VendId, CustId, _key : string</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ BuyKeys : List&lt;long&gt;, ContractNos : List&lt;string&gt;</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ BatchNos : List&lt;string&gt;, DataAreaId : string = "RSI"</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ UserName : string</text>
                  <line x1="0" y1="145" x2="440" y2="145" stroke="#bae6fd" stroke-width="1"/>
                  <text x="15" y="165" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">+ Validate() : bool</text>
                  <text x="15" y="185" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">+ ToParameterDictionary() : Dictionary&lt;string, object&gt;</text>
                  <text x="15" y="205" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">+ GetSearchFilterExpression() : string</text>
                  <text x="15" y="225" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">// 31 個服務模組、80 項 Operations 統一繼承此基底</text>
                </g>

                <g transform="translate(20, 310)">
                  <rect width="440" height="150" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <rect width="440" height="30" fill="#0284c7"/>
                  <text x="220" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">RSI_RT&lt;T&gt; (C# 回應包裝)</text>
                  <text x="15" y="55" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ IsValid : bool [執行狀態]</text>
                  <text x="15" y="75" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ Msg : string [訊息提示]</text>
                  <text x="15" y="95" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ TotalCount : int [總記錄數]</text>
                  <text x="15" y="115" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ DataList : List&lt;T&gt; [泛型資料實體清單]</text>
                  <line x1="0" y1="125" x2="440" y2="125" stroke="#bae6fd" stroke-width="1"/>
                  <text x="15" y="140" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">+ Success(data: List&lt;T&gt;) / + Fail(msg: string)</text>
                </g>

                <g transform="translate(20, 480)">
                  <rect width="440" height="310" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <rect width="440" height="30" fill="#0284c7"/>
                  <text x="220" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">D365_C#_Controllers</text>
                  <text x="15" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#b91c1c">■ Report.Service (RSIMDW1 :8085 / :8082)</text>
                  <text x="25" y="75" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ GetReportData(req: RqtBaseForm) : RSI_RT&lt;ReportDto&gt;</text>
                  <text x="25" y="95" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ ExportExcel(req: RqtBaseForm) : FileStreamResult</text>
                  <text x="25" y="115" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c">[資安注意: 無驗證模式 / 內部網路信任模式]</text>
                  <line x1="10" y1="130" x2="430" y2="130" stroke="#bae6fd" stroke-width="1"/>
                  <text x="15" y="150" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#0369a1">■ Local.WebApi (RSIMDW1 :80 / :8081)</text>
                  <text x="25" y="170" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ JCOM_WebServices : 15 模組 (Azure AD Bearer)</text>
                  <text x="25" y="190" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ RSI_WebServices : 16 模組 (Azure AD Bearer)</text>
                  <text x="25" y="210" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ ExecuteOperation(op: string, req: RqtBaseForm)</text>
                  <text x="25" y="230" font-family="'JetBrains Mono', monospace" font-size="10" fill="#0369a1">+ ValidateToken(jwt: string) : ClaimsPrincipal</text>
                  <line x1="10" y1="245" x2="430" y2="245" stroke="#bae6fd" stroke-width="1"/>
                  <text x="15" y="265" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">架構特點：31 服務、80 Operations 全量 C# 實作</text>
                  <text x="15" y="285" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">所有參數皆繼承 RqtBaseForm，回傳封裝至 RSI_RT&lt;T&gt;</text>
                </g>
              </g>

              <!-- Panel 2 -->
              <g transform="translate(540, 90)">
                <rect width="490" height="820" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
                <rect width="490" height="35" rx="8" fill="#fef3c7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#b45309">【子圖 B】RD_SAMPLE 樣品單與打樣明細核心領域模型</text>
                
                <g transform="translate(20, 50)">
                  <rect width="450" height="230" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect width="450" height="30" fill="#d97706"/>
                  <text x="225" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">MoHeader (樣品單主檔)</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ MoNo : string [主鍵 PK, 例如: MO-202611-0042]</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ Season : string [季節, 2027SS], Brand : string</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ Stage : string [Proto 1 / Sales Sample]</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ TargetFactory : string [RSV 越南 / RSG 柬埔寨]</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ CurrentStatus : SampleStatusEnum</text>
                  <line x1="0" y1="145" x2="450" y2="145" stroke="#fde68a" stroke-width="1"/>
                  <text x="15" y="165" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309">+ CreateMo() : bool</text>
                  <text x="15" y="185" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309">+ AssignFactory(factoryCode: string) : void</text>
                  <text x="15" y="205" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309">+ DispatchToProductionQueue() : bool</text>
                </g>

                <g transform="translate(20, 300)">
                  <rect width="450" height="210" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect width="450" height="30" fill="#d97706"/>
                  <text x="225" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">MoDetail (樣品部位用料明細)</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ DetailId : int [PK], MoNo : string [FK]</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ PartName : string [前片/後片/袖口/拉鍊]</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ FabricSpec : string [材質規格規格碼]</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ ColorCode : string, ConsumptionRate : decimal</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ MarkerLength : decimal, WastagePercent : decimal</text>
                  <line x1="0" y1="145" x2="450" y2="145" stroke="#fde68a" stroke-width="1"/>
                  <text x="15" y="165" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309">+ CalculateTotalUsage() : decimal</text>
                  <text x="15" y="185" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309">+ CheckAxInventory() : bool (跨庫視圖查詢)</text>
                </g>

                <g transform="translate(20, 530)">
                  <rect width="450" height="260" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect width="450" height="30" fill="#d97706"/>
                  <text x="225" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">TechPackAttachment &amp; SewingTask</text>
                  <text x="15" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#0369a1">■ TechPackAttachment (版單技術包)</text>
                  <text x="25" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ FileId : Guid, MoNo : string [FK], FileName : string</text>
                  <text x="25" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ ParsedBOMJson : string, ParseStatus : string</text>
                  <text x="25" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309">+ InvokePythonCliParser() : ExtractedResult</text>
                  <line x1="10" y1="125" x2="440" y2="125" stroke="#fde68a" stroke-width="1"/>
                  <text x="15" y="145" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#15803d">■ SampleSewingAssignment (車縫工單)</text>
                  <text x="25" y="165" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ AssignId : int, LineNo : string, OperatorId : string</text>
                  <text x="25" y="185" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ TargetMinutes : int, ActualMinutes : int</text>
                  <text x="25" y="205" font-family="'JetBrains Mono', monospace" font-size="10" fill="#15803d">+ SubmitToCqsQualityReview() : bool</text>
                  <text x="15" y="235" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">關聯結構：MoHeader 1 ──* MoDetail ｜ 1 ── 1 TechPack</text>
                </g>
              </g>

              <!-- Panel 3 -->
              <g transform="translate(1050, 90)">
                <rect width="510" height="820" rx="8" fill="#ffffff" stroke="#9333ea" stroke-width="1.5"/>
                <rect width="510" height="35" rx="8" fill="#f3e8ff"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#7e22ce">【子圖 C】跨庫資料存取與排程傳輸實體</text>

                <g transform="translate(20, 50)">
                  <rect width="470" height="240" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <rect width="470" height="30" fill="#9333ea"/>
                  <text x="235" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AxDirectQueryHelper (ADO.NET)</text>
                  <text x="15" y="55" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c" font-weight="bold">! 1,490 處 Direct SQL 直查 SAM 本地庫</text>
                  <text x="15" y="75" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c" font-weight="bold">! 23 處 Direct SQL 跨庫查 AXDB 視圖</text>
                  <text x="15" y="95" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">- _samConnStr : "server=192.168.0.22;uid=sa;..."</text>
                  <text x="15" y="115" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">- _axdbConnStr : "server=192.168.0.131;uid=sa;..."</text>
                  <line x1="0" y1="130" x2="470" y2="130" stroke="#e9d5ff" stroke-width="1"/>
                  <text x="15" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#7e22ce">+ ExecuteAdHocSql(sql: string) : DataTable</text>
                  <text x="15" y="170" font-family="'JetBrains Mono', monospace" font-size="10" fill="#7e22ce">+ QueryAxDbView(viewName: string) : DataTable</text>
                  <text x="15" y="190" font-family="'JetBrains Mono', monospace" font-size="10" fill="#7e22ce">+ BatchExecuteCommands(sqls: List&lt;string&gt;) : int</text>
                  <text x="15" y="215" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c">[高架構負債：無 ORM，SQL 散落於 WebForms aspx.cs]</text>
                </g>

                <g transform="translate(20, 310)">
                  <rect width="470" height="250" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <rect width="470" height="30" fill="#9333ea"/>
                  <text x="235" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">BatchScheduleCoordinator (13 Batches)</text>
                  <text x="15" y="55" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ SendNotification_bat : 每 5 分鐘掃描寄發</text>
                  <text x="15" y="75" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ Sync_RSV_bat : 每 30 分鐘同步至越南廠</text>
                  <text x="15" y="95" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ Sync_RSG_bat : 每 30 分鐘同步至柬埔寨廠</text>
                  <text x="15" y="115" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ Export_Sam_bat : 每日 23:01 導出打樣資料</text>
                  <text x="15" y="135" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ Daily_Sewn_Report_bat : 每日 23:31 車縫日報</text>
                  <line x1="0" y1="150" x2="470" y2="150" stroke="#e9d5ff" stroke-width="1"/>
                  <text x="15" y="170" font-family="'JetBrains Mono', monospace" font-size="10" fill="#7e22ce">+ TriggerBatch(batchName: string) : ExitCode</text>
                  <text x="15" y="190" font-family="'JetBrains Mono', monospace" font-size="10" fill="#7e22ce">+ CheckDyxnetTdsSocket(ip: string) : bool</text>
                  <text x="15" y="210" font-family="'JetBrains Mono', monospace" font-size="10" fill="#7e22ce">+ BufferFailedTransactionsToSqlite() : void</text>
                  <text x="15" y="235" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">[離線韌性：專線中斷自動啟動 48~72hr 自律暫存]</text>
                </g>

                <g transform="translate(20, 580)">
                  <rect width="470" height="210" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <rect width="470" height="30" fill="#9333ea"/>
                  <text x="235" y="20" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CqsIntegrationBridge &amp; CLI Runner</text>
                  <text x="15" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#15803d">■ CQS (.NET 8 ARR 反向代理架構)</text>
                  <text x="25" y="75" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ ArrUrl: "http://192.168.0.23:8012" -&gt; Kestrel :8011</text>
                  <text x="25" y="95" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ SubmitInspectionReport(dto: CqsDto) : bool</text>
                  <line x1="10" y1="110" x2="460" y2="110" stroke="#e9d5ff" stroke-width="1"/>
                  <text x="15" y="130" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#7e22ce">■ Python TechPack Subprocess Runner</text>
                  <text x="25" y="150" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ RunTechPackCli(pdfPath: string) : JsonPayload</text>
                  <text x="25" y="170" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">+ WorkingDir: "D:\\EXP" ｜ 執行環境: Local Python 3</text>
                  <text x="15" y="195" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">全面支援 0 元開源架構，免授權負擔</text>
                </g>
              </g>
            </svg>
        """

    elif index == 1:
        return f"""
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">02. UML 2.0 Component Diagram (元件圖) — 系統模組邊界與整合介面</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 3 個獨立子圖面板 ｜ 總部地端核心微服務、D365 C# 整合層、YARP 零信任閘道</text>

              <!-- Panel 1 -->
              <g transform="translate(40, 90)">
                <rect width="480" height="820" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
                <rect width="480" height="35" rx="8" fill="#fef3c7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#b45309">【子圖 A】台北總部地端核心元件 (RDSMP1 &amp; RDSMP2)</text>
                
                <g transform="translate(20, 50)">
                  <rect width="440" height="130" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect x="400" y="10" width="25" height="15" fill="#fef3c7" stroke="#d97706"/>
                  <rect x="395" y="13" width="10" height="4" fill="#d97706"/>
                  <rect x="395" y="19" width="10" height="4" fill="#d97706"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">&lt;&lt;component&gt;&gt; RD_Sample.Web</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">環境: IIS 10.0 on RDSMP2 (192.168.0.22)</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">提供介面: HTTPS/443 Web UI, HTTP/80 WebForms</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">技術債: 1,490 處 Direct SQL 直連 SAM_DB</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">跨庫存取: 23 處 Direct SQL 直查 AXDB (192.168.0.131)</text>
                </g>

                <g transform="translate(20, 200)">
                  <rect width="440" height="130" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect x="400" y="10" width="25" height="15" fill="#dcfce7" stroke="#16a34a"/>
                  <rect x="395" y="13" width="10" height="4" fill="#16a34a"/>
                  <rect x="395" y="19" width="10" height="4" fill="#16a34a"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;component&gt;&gt; CQS 品質檢驗微服務</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">執行節點: RDSMP1 (192.168.0.23)</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">入口反向代理: IIS ARR (:8012) ──&gt; Kestrel (:8011)</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">微服務架構: .NET 8 Kestrel Core 高效能非同步微服務</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d">職責: 車縫工單樣品尺寸、外觀瑕疵評定與品質追蹤</text>
                </g>

                <g transform="translate(20, 350)">
                  <rect width="440" height="140" rx="4" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
                  <rect x="400" y="10" width="25" height="15" fill="#ffedd5" stroke="#ea580c"/>
                  <rect x="395" y="13" width="10" height="4" fill="#ea580c"/>
                  <rect x="395" y="19" width="10" height="4" fill="#ea580c"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">&lt;&lt;component&gt;&gt; Windows 批次排程 (13 Batches)</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">宿主環境: RDSMP2 Windows 工作排程器</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">高頻任務: SendNotification (5分), Sync_RSV/RSG (30分)</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">夜間任務: Export_Sam (23:01), Daily_Sewn_Report (23:31)</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#c2410c">執行路徑: D:\\EXP 腳本目錄與資料暫存槽</text>
                </g>

                <g transform="translate(20, 510)">
                  <rect width="440" height="140" rx="4" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
                  <rect x="400" y="10" width="25" height="15" fill="#ede9fe" stroke="#7c3aed"/>
                  <rect x="395" y="13" width="10" height="4" fill="#7c3aed"/>
                  <rect x="395" y="19" width="10" height="4" fill="#7c3aed"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#6d28d9">&lt;&lt;component&gt;&gt; TechPack CLI &amp; FindImage</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">TechPack Parser: Python 3 命令行實用程式 (I04)</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">叫用模式: WebForms 以 Process.Start 啟動 CLI 解析</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">FindImage: RDSMP2 (:8081) 圖片相似特徵比對微服務</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#6d28d9">輸出: 結構化 JSON BOM 與物料裁片清單</text>
                </g>
              </g>

              <!-- Panel 2 -->
              <g transform="translate(540, 90)">
                <rect width="490" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="490" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 B】D365 C# 整合層 (RSIMDW1 &amp; D365 AOS)</text>
                
                <g transform="translate(20, 50)">
                  <rect width="450" height="150" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
                  <rect x="410" y="10" width="25" height="15" fill="#fee2e2" stroke="#dc2626"/>
                  <rect x="405" y="13" width="10" height="4" fill="#dc2626"/>
                  <rect x="405" y="19" width="10" height="4" fill="#dc2626"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b91c1c">&lt;&lt;component&gt;&gt; D365 Report.Service</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">節點: RSIMDW1 (:8085 正式 / :8082 測試)</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">性質: D365 C# 外掛報表引擎 (C# External Plugin)</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">驗證模式: 無驗證 (No Auth, 受信任內網直連)</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">提供介面: 12 項報表產出、Excel 匯出串流</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">所有請求參數繼承 RqtBaseForm，回傳封裝為 RSI_RT</text>
                </g>

                <g transform="translate(20, 220)">
                  <rect width="450" height="150" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <rect x="410" y="10" width="25" height="15" fill="#e0f2fe" stroke="#0284c7"/>
                  <rect x="405" y="13" width="10" height="4" fill="#0284c7"/>
                  <rect x="405" y="19" width="10" height="4" fill="#0284c7"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0369a1">&lt;&lt;component&gt;&gt; D365 Local.WebApi</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">節點: RSIMDW1 (:80 正式 / :8081 測試)</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">架構模組: 31 個服務模組、80 項 Operations (全量 C#)</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">驗證機制: Azure AD Bearer Token 驗證保護</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">核心服務: JCOM_WebServices, RSI_WebServices</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">包含完整 JWT Bearer 授權解析與權限範圍校驗</text>
                </g>

                <g transform="translate(20, 390)">
                  <rect width="450" height="150" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <rect x="410" y="10" width="25" height="15" fill="#f3e8ff" stroke="#9333ea"/>
                  <rect x="405" y="13" width="10" height="4" fill="#9333ea"/>
                  <rect x="405" y="19" width="10" height="4" fill="#9333ea"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#7e22ce">&lt;&lt;database&gt;&gt; D365 AXDB 營運主庫</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">實例名稱: rsiaxdb1 (192.168.0.131)</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">集群節點: AOS 叢集 (.124, .125, .126)</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">存取模式: 23 處跨資料庫唯讀查詢 (Read-Only Views)</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#7e22ce">儲存標的: 全球採購單、BOM 主檔、財務主數據</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">安全防護: 跨庫查詢僅具備 SELECT 權限，保障交易完整性</text>
                </g>
              </g>

              <!-- Panel 3 -->
              <g transform="translate(1050, 90)">
                <rect width="510" height="820" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
                <rect width="510" height="35" rx="8" fill="#dcfce7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#15803d">【子圖 C】YARP 零信任閘道處方 (0 元開源架構平替)</text>

                <g transform="translate(20, 50)">
                  <rect width="470" height="150" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect x="430" y="10" width="25" height="15" fill="#dcfce7" stroke="#16a34a"/>
                  <rect x="425" y="13" width="10" height="4" fill="#16a34a"/>
                  <rect x="425" y="19" width="10" height="4" fill="#16a34a"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;gateway&gt;&gt; YARP 零信任邊界反向代理</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">軟體架構: Microsoft YARP (.NET 8 邊界反向代理)</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">成本效益: 0 元開源平替，完全取代付費 ARR 與硬體負載平衡</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">整合能力: 統一反向代理 CQS (:8011) 與 Report (:8085)</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">效能表現: 支援 HTTP/2, gRPC 與連線池複用</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">部署節點: 台北總部機房 DMZ 入口 (連接埠 443 / 80)</text>
                </g>

                <g transform="translate(20, 220)">
                  <rect width="470" height="150" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect x="430" y="10" width="25" height="15" fill="#dcfce7" stroke="#16a34a"/>
                  <rect x="425" y="13" width="10" height="4" fill="#16a34a"/>
                  <rect x="425" y="19" width="10" height="4" fill="#16a34a"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;middleware&gt;&gt; 認證護盾與熔斷限流模組</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">認證補強: 自動為 Report.Service (:8085) 補上 Bearer 檢核</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">安全邊界: 外部呼叫必須攜帶 Token，內部轉發附加雙向 mTLS</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">熔斷保護: 專線抖動時主動熔斷對海外廠區的阻塞連線</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d">限流保護: 針對 13 支批次作業提供平滑併發控制</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">全面防禦阻絕外部未經授權穿透至舊版 C# 服務</text>
                </g>

                <g transform="translate(20, 390)">
                  <rect width="470" height="150" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect x="430" y="10" width="25" height="15" fill="#dcfce7" stroke="#16a34a"/>
                  <rect x="425" y="13" width="10" height="4" fill="#16a34a"/>
                  <rect x="425" y="19" width="10" height="4" fill="#16a34a"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;buffer&gt;&gt; 海外廠區離線佇列轉發器</text>
                  <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">儲存技術: 廠區地端嵌入式 SQLite / 本地磁碟 WAL 暫存</text>
                  <text x="20" y="70" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">自律能力: 專線中斷 48~72 小時無感作業，恢復後自動補送</text>
                  <text x="20" y="90" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">資料沖銷: 專線恢復後循序重放交易日誌，確保數據一致</text>
                  <text x="20" y="110" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">零授權費: 免收廠端軟體 License，大幅降低海外營運 TCO</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">為 2027 蜂巢計畫海外廠區提供強韌生產連續性保護</text>
                </g>
              </g>
            </svg>
        """

    elif index == 2:
        return f"""
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">03. UML 2.0 Deployment Diagram (部署圖) — 地端實體節點與網路拓撲</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 3 個獨立子圖面板 ｜ 台北總部機房拓撲、DYXnet 跨國專線海外廠區、外部雲端整合</text>

              <!-- Panel 1 -->
              <g transform="translate(40, 90)">
                <rect width="480" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="480" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 A】台北總部地端核心機房 (Taipei HQ On-Premises)</text>
                
                <g transform="translate(20, 50)">
                  <rect width="440" height="170" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">&lt;&lt;device / vm&gt;&gt; RDSMP2 (正式營運機)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">實體 IP: 192.168.0.22 ｜ OS: Windows Server 2019</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">Web 站台: IIS 10.0 (RD_SAMPLE, HTTPS 443 / HTTP 80)</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">資料庫引擎: SQL Server 2019 (:1433, SAM_DB 本地實例)</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#ea580c" font-weight="bold">排程執行器: Windows Task Scheduler (13 支 .bat 排程作業)</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">微服務實例: FindImage.WebApi (Port :8081)</text>
                  <text x="20" y="155" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">磁碟配置: C:\\ (系統), D:\\EXP (樣品數據、批次排程與封存)</text>
                </g>

                <g transform="translate(20, 240)">
                  <rect width="440" height="150" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;device / vm&gt;&gt; RDSMP1 (測試機 / ARR 代理)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">實體 IP: 192.168.0.23 ｜ OS: Windows Server 2019</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">代理閘道: IIS ARR 反向代理模組 (Port :8012)</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">微服務節點: .NET 8 Kestrel Core Runtime (CQS: 8011)</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">測試站台: RD_SAMPLE 測試環境網站 (Port :80)</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">網路對接: 與 RDSMP2 位於相同 1Gbps 機房內網</text>
                </g>

                <g transform="translate(20, 410)">
                  <rect width="440" height="150" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0369a1">&lt;&lt;device / vm&gt;&gt; RSIMDW1 (D365 中間件伺服器)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">實體 IP: 192.168.0.95 ｜ OS: Windows Server 2019</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">報表服務: D365 Report.Service (:8085 正式 / :8082 測試)</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#0369a1" font-weight="bold">核心 API: D365 Local.WebApi (:80 正式 / :8081 測試)</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">軟體架構: Microsoft C# 執行階段模組 (31 模組 / 80 Ops)</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">認證規範: Local.WebApi 採用 Azure AD Bearer Token</text>
                </g>

                <g transform="translate(20, 580)">
                  <rect width="440" height="150" rx="6" fill="#faf5ff" stroke="#9333ea" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#7e22ce">&lt;&lt;cluster&gt;&gt; AXDB 營運主庫叢集 (D365 ERP)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">實例 IP: rsiaxdb1 (192.168.0.131) ｜ 埠號: TCP 1433</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">AOS 叢集節點: 192.168.0.124 ~ 192.168.0.126</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#7e22ce" font-weight="bold">高可用架構: SQL Server AlwaysOn 可用性群組</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">存取關係: RD_SAMPLE 共有 23 處 Direct SQL 跨庫讀取</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">主庫保護: 嚴格隔離寫入，僅授權唯讀視圖查詢</text>
                </g>
              </g>

              <!-- Panel 2 -->
              <g transform="translate(540, 90)">
                <rect width="490" height="820" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
                <rect width="490" height="35" rx="8" fill="#ffedd5"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#c2410c">【子圖 B】跨國專線 (DYXnet) 與海外邊緣自律廠區</text>
                
                <g transform="translate(20, 50)">
                  <rect width="450" height="160" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">&lt;&lt;mpls vpn&gt;&gt; 第一線 (DYXnet) 企業跨國專線</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">專線網路: 台北總部 &lt;──&gt; 越南同奈 &lt;──&gt; 柬埔寨柴楨</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">直通通訊埠: 直開 TCP 1433 TDS 資料庫傳輸通道</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#c2410c" font-weight="bold">同步排程: 每 30 分鐘自動執行 Sync_RSV.bat / Sync_RSG.bat</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">斷網自律要求: 廠區端具備 48~72 小時離線獨立運轉能力</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">海纜中斷時廠區作業零停頓，專線復原後自動批次補送對齊</text>
                </g>

                <g transform="translate(20, 230)">
                  <rect width="450" height="160" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">&lt;&lt;edge node&gt;&gt; 越南廠 (RDV Factory Edge)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">節點 IP: 192.168.185.123 ｜ 通訊埠: TCP 1433</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">在地實例: RSV_SAMPLE (SQL Server 地端實例)</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">現場終端: 45 台打樣車縫現場平板觸控端機</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">自律機制: 本地排程接收工單，產線直接自本地庫讀取料單</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">跨國連線中斷時，現場裁縫與品管不受絲毫影響</text>
                </g>

                <g transform="translate(20, 410)">
                  <rect width="450" height="160" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#c2410c">&lt;&lt;edge node&gt;&gt; 柬埔寨廠 (RDG Factory Edge)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">節點 IP: 192.168.193.65 ｜ 通訊埠: TCP 1433</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">在地實例: RSG_SAMPLE (SQL Server 地端實例)</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">現場終端: 30 台打樣車縫現場平板觸控端機</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">自律機制: 具備獨立 SQLite / 本地磁碟交易補償佇列</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">專線修復後批次同步當日車縫回報與工時記錄</text>
                </g>

                <g transform="translate(20, 590)">
                  <rect width="450" height="150" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">&lt;&lt;resilience buffer&gt;&gt; 廠區在地自律緩衝架構</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">快取技術: 零授權費開源 SQLite / 本地磁碟交易日誌</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">容錯指標: 容許海纜或專線中斷 48 ~ 72 小時</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">復原機制: 網路恢復後循序重放交易日誌，雙向一致校驗</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">保障全球供應鏈打樣交期零風險</text>
                </g>
              </g>

              <!-- Panel 3 -->
              <g transform="translate(1050, 90)">
                <rect width="510" height="820" rx="8" fill="#ffffff" stroke="#9333ea" stroke-width="1.5"/>
                <rect width="510" height="35" rx="8" fill="#f3e8ff"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#7e22ce">【子圖 C】外部雲端擴充與週邊服務整合節點</text>

                <g transform="translate(20, 50)">
                  <rect width="470" height="160" rx="6" fill="#faf5ff" stroke="#9333ea" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#7e22ce">&lt;&lt;cloud service&gt;&gt; AWS AI 推論節點 (彈性擴展)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">端點位址: https://aws-ai.rsi.com:8000 (HTTPS 加密)</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">整合功能: TechPack 複雜版型深度學習解析與向量檢索</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#7e22ce" font-weight="bold">架構方針: 地端優先 (On-Prem First)，雲端僅作輔助彈性算力</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">資安邊界: 僅傳輸去識別化向量特徵，無企業營業秘密外流</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">斷網保護: 雲端不可用時自動降級由本地 Python CLI 解析</text>
                </g>

                <g transform="translate(20, 230)">
                  <rect width="470" height="150" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0369a1">&lt;&lt;service&gt;&gt; 集團郵件伺服器 (SMTP Service)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">連線協定: TCP 587 (STARTTLS 加密傳輸)</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#0369a1" font-weight="bold">排程觸發: SendNotification.bat (每 5 分鐘高頻脈衝)</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">警報範疇: 樣品進度逾時、海外廠車縫品質異常、專線中斷警告</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">通知對象: 設計師、業務團隊、工廠廠長與品管主管</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">備援機制: 郵件發送失敗自動保留於本地佇列等待下回重試</text>
                </g>

                <g transform="translate(20, 400)">
                  <rect width="470" height="150" rx="6" fill="#f8fafc" stroke="#475569" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#1e293b">&lt;&lt;storage&gt;&gt; 企業儲存 NAS (D:\\EXP 映射槽)</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">存取協定: SMB 3.0 / NFS (Port 445)</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">路徑對應: \\\\nas.rsi.local\\Sample_Archive ──&gt; D:\\EXP</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#1e293b" font-weight="bold">備份作業: Export_Sam.bat (每日 23:01 自動匯出歸檔)</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">資料保留: 樣品 PDF、歷史 BOM、每日車縫日報長期封存</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">異地備援: 透過專屬儲存網路進行異地快照複製</text>
                </g>

                <g transform="translate(20, 570)">
                  <rect width="470" height="150" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
                  <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">&lt;&lt;workstation&gt;&gt; 設計師與業務終端工作站</text>
                  <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">硬體規格: Intel Core i7 / 32GB RAM / 雙螢幕工作站</text>
                  <text x="20" y="75" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">作業系統: Windows 11 Enterprise ｜ 瀏覽器: Comet 瀏覽器</text>
                  <text x="20" y="95" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b45309" font-weight="bold">網路連線: 總部研發 Intranet (HTTPS 443 存取 RD_SAMPLE)</text>
                  <text x="20" y="115" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">操作行為: 上傳版單 PDF、開立樣品工單、審核報表</text>
                  <text x="20" y="135" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#64748b">資安控管: 企業端點防護、嚴禁明碼下載敏感主數據</text>
                </g>
              </g>
            </svg>
        """

    elif index == 3:
        # Package Diagram (3 Panels)
        return f"""
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">04. UML 2.0 Package Diagram (套件圖) — 模組依賴與分層邊界</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 3 個獨立子圖面板 ｜ RD_SAMPLE 系統套件、D365 C# 服務套件、蜂巢基礎設施</text>

              <!-- Panel 1: RD_SAMPLE Packages -->
              <g transform="translate(40, 90)">
                <rect width="480" height="820" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
                <rect width="480" height="35" rx="8" fill="#fef3c7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#b45309">【子圖 A】RD_SAMPLE 系統分層套件</text>
                
                <g transform="translate(20, 50)">
                  <rect x="0" y="0" width="120" height="20" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#b45309">RSI.RDSample.UI</text>
                  <rect x="0" y="18" width="440" height="140" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">+ WebForms aspx / aspx.cs 頁面控制器</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• MoEntryForm.aspx (樣品單維護)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• TechPackUploadHandler.ashx (版單接收)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• SampleReportViewer.aspx (報表查閱)</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">! 緊密耦合: UI 層混雜大量 ADO.NET SQL 指令</text>
                </g>

                <g transform="translate(20, 230)">
                  <rect x="0" y="0" width="130" height="20" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#b45309">RSI.RDSample.BLL</text>
                  <rect x="0" y="18" width="440" height="140" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">+ 樣品業務規則與計算引擎</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• MoManager (工單流程狀態流轉)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• FabricConsumptionCalculator (裁片損耗試算)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• TechPackParserBridge (叫用 Python CLI I04)</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">依賴: RSI.RDSample.DAL, RSI.D365.Contracts</text>
                </g>

                <g transform="translate(20, 410)">
                  <rect x="0" y="0" width="130" height="20" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#b45309">RSI.RDSample.DAL</text>
                  <rect x="0" y="18" width="440" height="150" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">+ 資料存取套件 (ADO.NET Direct SQL)</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• SamDbAccessor (1,490 處 Direct SQL)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• AxDbCrossQueryAccessor (23 處跨庫 SQL 視圖)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• SqlTransactionScopeManager</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">! 痛點: 無 ORM 抽象，資料庫遷移摩擦力極高</text>
                </g>

                <g transform="translate(20, 600)">
                  <rect x="0" y="0" width="160" height="20" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#b45309">RSI.RDSample.BatchJobs</text>
                  <rect x="0" y="18" width="440" height="150" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b45309">+ Windows 批次排程實作 (D:\\EXP)</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• 13 支批次 .bat 作業腳本套件</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• Sync_RSV / Sync_RSG 跨國傳輸模組</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• Daily_Sewn_Report 匯總套件</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#ea580c">執行環境: Windows 內建排程器，每 5~30 分鐘自動觸發</text>
                </g>
              </g>

              <!-- Panel 2: D365 C# Packages -->
              <g transform="translate(540, 90)">
                <rect width="490" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="490" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 B】D365 C# 服務套件架構</text>
                
                <g transform="translate(20, 50)">
                  <rect x="0" y="0" width="160" height="20" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#0369a1">RSI.D365.ReportService</text>
                  <rect x="0" y="18" width="450" height="160" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b91c1c">+ D365 C# 外掛報表套件 (RSIMDW1 :8085)</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• 12 項打樣與 ERP 關聯報表生成器</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• ExcelStreamExporter (大數據串流輸出)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b91c1c" font-weight="bold">! 驗證層級: 無驗證模式 (No Auth Legacy)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• 請求參數型態: 繼承 RqtBaseForm</text>
                  <text x="20" y="145" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">對外暴露 HTTP REST API，直接回傳二進位資料串流</text>
                </g>

                <g transform="translate(20, 240)">
                  <rect x="0" y="0" width="150" height="20" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#0369a1">RSI.D365.LocalWebApi</text>
                  <rect x="0" y="18" width="450" height="170" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0369a1">+ D365 核心業務服務套件 (RSIMDW1 :80)</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• 31 個服務模組、80 項 Operations (全量 C# 實作)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• JCOM_WebServices (15 模組) ｜ RSI_WebServices (16 模組)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">! 驗證機制: Azure AD Bearer Token 安全校驗</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• 回應型態: 統一封裝為泛型 RSI_RT&lt;T&gt;</text>
                  <text x="20" y="150" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">包含完整的 JWT 權杖解析器與微服務路由表</text>
                </g>

                <g transform="translate(20, 440)">
                  <rect x="0" y="0" width="140" height="20" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#0369a1">RSI.D365.Contracts</text>
                  <rect x="0" y="18" width="450" height="150" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#0369a1">+ 跨系統通訊契約共享套件</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• RqtBaseForm (所有 C# API 請求抽象基底)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• RSI_RT&lt;T&gt; (標準化泛型回傳模型)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• CommonFilterDto, PagingParameterDto</text>
                  <text x="20" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">由 RD_SAMPLE 與 D365 微服務共同參照，保證通訊規格一致</text>
                </g>

                <g transform="translate(20, 620)">
                  <rect x="0" y="0" width="130" height="20" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#0369a1">RSI.CQS.Engine</text>
                  <rect x="0" y="18" width="450" height="140" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">+ CQS 品質檢驗引擎 (.NET 8 Kestrel Core)</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• 入口: IIS ARR (:8012) 反向代理至 Kestrel (:8011)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• QualityRuleEvaluator (成衣樣品公差評定)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• InspectionAuditLogger (品質審查軌跡追蹤)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#15803d">現代化微服務架構，支援非同步高併發處理</text>
                </g>
              </g>

              <!-- Panel 3: Hive Infrastructure -->
              <g transform="translate(1050, 90)">
                <rect width="510" height="820" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
                <rect width="510" height="35" rx="8" fill="#dcfce7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#15803d">【子圖 C】蜂巢計畫基礎設施與治理套件</text>

                <g transform="translate(20, 50)">
                  <rect x="0" y="0" width="180" height="20" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#15803d">RSI.Infrastructure.Security</text>
                  <rect x="0" y="18" width="470" height="170" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">+ YARP 零信任閘道與安全護盾套件</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• YarpReverseProxyModule (0元開源反向代理)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• TokenEnforcementFilter (為無驗證報表補上 Bearer)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• RateLimitingMiddleware (防禦 DoS 與併發阻塞)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">! 效益: 徹底防禦未經授權穿透，取代昂貴專用設備</text>
                  <text x="20" y="150" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">實現 0 元軟體授權之企業級資安防禦網</text>
                </g>

                <g transform="translate(20, 250)">
                  <rect x="0" y="0" width="190" height="20" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#15803d">RSI.Infrastructure.OfflineSync</text>
                  <rect x="0" y="18" width="470" height="170" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">+ 48~72 小時離線自律傳輸套件</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• EdgeTransactionQueue (廠區地端嵌入式 SQLite 暫存)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• DyxnetCircuitBreaker (專線中斷主動熔斷保護)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• TwoWayReconcileEngine (海纜復原後雙向差分對齊)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d" font-weight="bold">! 韌性保證: 越南與柬埔寨廠區斷網 3 天正常運轉</text>
                  <text x="20" y="150" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">徹底告別專線不穩引發產線停擺的營運風險</text>
                </g>

                <g transform="translate(20, 450)">
                  <rect x="0" y="0" width="190" height="20" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#15803d">RSI.Infrastructure.Observability</text>
                  <rect x="0" y="18" width="470" height="160" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#15803d">+ 全鏈路遙測與日誌可觀測套件</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• OpenTelemetryTracer (分佈式追蹤 CorrelationId)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• BatchExecutionWatcher (13 支排程超時監控)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• SmtpAlertDispatcher (異常秒級告警推播)</text>
                  <text x="20" y="125" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#64748b">統一總部與海外廠區日誌格式，達成全域可視化監控</text>
                </g>

                <g transform="translate(20, 640)">
                  <rect x="0" y="0" width="150" height="20" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
                  <text x="10" y="14" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#6d28d9">RSI.External.AiBridge</text>
                  <rect x="0" y="18" width="470" height="120" rx="4" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5"/>
                  <text x="20" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#6d28d9">+ 外部 AI 推論連接器 (AWS EC2 :8000)</text>
                  <text x="20" y="65" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• TechPackVectorExtractor (去識別化版型特徵提取)</text>
                  <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#334155">• FallbackToLocalCliHandler (雲端超時自動降級本地 CLI)</text>
                  <text x="20" y="105" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#7c3aed">兼顧前瞻雲端 AI 算力與地端極限容錯自律</text>
                </g>
              </g>
            </svg>
        """

    elif index == 4:
        # Object Diagram (2 Panels)
        return f"""
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">05. UML 2.0 Object Diagram (物件圖) — 執行期真實記憶體物件快照</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 2 個獨立子圖面板 ｜ 樣品單領域物件快照、跨國專線排程傳輸 Session 快照</text>

              <!-- Panel 1: Active Mo Domain Objects -->
              <g transform="translate(40, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#fef3c7"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#b45309">【子圖 A】打樣單執行期領域物件實例快照 (Snapshot: 2026-11-12 14:30)</text>

                <!-- Object 1: activeMo -->
                <g transform="translate(30, 50)">
                  <rect width="680" height="150" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#d97706"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">activeMo : MoHeader</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">MoNo = "MO-202611-0042"</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">Season = "2027SS" ｜ Brand = "Arc'teryx" ｜ StyleNo = "AT-JKT-8891"</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">Stage = "Proto 1" ｜ TargetFactory = "RSV" (越南同奈廠)</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#15803d" font-weight="bold">CurrentStatus = SampleStatusEnum.DispatchedToFactory</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">CreatedAt = 2026-11-12 10:15:32 ｜ CreatedBy = "designer.chen"</text>
                </g>

                <!-- Object 2: detailFront -->
                <g transform="translate(30, 220)">
                  <rect width="320" height="150" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect width="320" height="28" fill="#d97706"/>
                  <text x="160" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">detailFront : MoDetail</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">DetailId = 10101</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">MoNo = "MO-202611-0042"</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">PartName = "FrontPanel (前片)"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">FabricSpec = "GORETEX-3L-BK"</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">ConsumptionRate = 1.25m</text>
                </g>

                <!-- Object 3: detailBack -->
                <g transform="translate(390, 220)">
                  <rect width="320" height="150" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
                  <rect width="320" height="28" fill="#d97706"/>
                  <text x="160" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">detailBack : MoDetail</text>
                  <text x="15" y="50" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">DetailId = 10102</text>
                  <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">MoNo = "MO-202611-0042"</text>
                  <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">PartName = "BackPanel (後片)"</text>
                  <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">FabricSpec = "GORETEX-3L-BK"</text>
                  <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#334155">ConsumptionRate = 1.45m</text>
                </g>

                <!-- Object 4: techPack -->
                <g transform="translate(30, 390)">
                  <rect width="680" height="150" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#0284c7"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">techPack : TechPackAttachment</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">FileId = 4c9e8a01-9872-4b31-9f20-b3f94089c104</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">FileName = "ArcTeryx_2027SS_AT8891_SpecSheet.pdf"</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">FileSize = 14,821,902 bytes ｜ StoragePath = "D:\\EXP\\Uploads\\202611\\"</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#15803d" font-weight="bold">ParseStatus = "PARSED_SUCCESS_VIA_LOCAL_PYTHON_CLI"</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">ExtractedPartsCount = 28 ｜ ExtractedColors = 3 (Black, Olive, Slate)</text>
                </g>

                <!-- Object 5: sewTask -->
                <g transform="translate(30, 560)">
                  <rect width="680" height="150" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#16a34a"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">sewingTask : SampleSewingAssignment</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">AssignId = 88201 ｜ Factory = "RSV" ｜ LineNo = "SampleLine-02"</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">MasterOperator = "Nguyen Van A" ｜ PlannedDate = "2026-11-13"</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">TargetMinutes = 180 mins ｜ ActualMinutes = 175 mins</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#15803d" font-weight="bold">CqsQualityScore = 98.5 (Grade A - Released)</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">QualityEvaluatedAt = 2026-11-13 16:20:10 on RDSMP1 Kestrel Core</text>
                </g>

                <!-- Links -->
                <line x1="370" y1="200" x2="190" y2="220" stroke="#d97706" stroke-width="1.5"/>
                <line x1="370" y1="200" x2="550" y2="220" stroke="#d97706" stroke-width="1.5"/>
                <line x1="370" y1="200" x2="370" y2="390" stroke="#0284c7" stroke-width="1.5"/>
                <line x1="370" y1="540" x2="370" y2="560" stroke="#16a34a" stroke-width="1.5"/>
              </g>

              <!-- Panel 2: Cross-Border Session Snapshot -->
              <g transform="translate(820, 90)">
                <rect width="740" height="820" rx="8" fill="#ffffff" stroke="#9333ea" stroke-width="1.5"/>
                <rect width="740" height="35" rx="8" fill="#f3e8ff"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#7e22ce">【子圖 B】跨國排程傳輸與資料通道執行期快照</text>

                <!-- Object 6: syncJob_RSV -->
                <g transform="translate(30, 50)">
                  <rect width="680" height="150" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#9333ea"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">syncJob_RSV : BatchTaskInstance</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">TaskName = "Sync_RSV.bat" ｜ Host = "RDSMP2 (192.168.0.22)"</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">Schedule = "Every 30 Minutes" ｜ TriggeredBy = "TaskScheduler"</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">LastRunTime = 2026-11-12 14:00:01 ｜ Duration = 14.2 seconds</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#15803d" font-weight="bold">ExitCode = 0 (SUCCESS) ｜ ProcessedRecords = 42 MOs</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">LogOutput = "D:\\EXP\\Logs\\Sync_RSV_20261112_1400.log"</text>
                </g>

                <!-- Object 7: tdsSession -->
                <g transform="translate(30, 220)">
                  <rect width="680" height="150" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#9333ea"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">tdsSession : SqlTdsConnection</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">LocalEndpoint = "192.168.0.22:54210" ──&gt; DYXnet MPLS VPN</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">RemoteEndpoint = "192.168.185.123:1433" (RDV Factory SQL)</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">Protocol = "TDS 7.4 (Tabular Data Stream over TCP)"</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#15803d" font-weight="bold">ConnectionState = Open ｜ Latency = 42ms ｜ PacketLoss = 0%</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">ActiveTransaction = "TX_RSV_SYNC_BATCH_202611121400"</text>
                </g>

                <!-- Object 8: syncPayload -->
                <g transform="translate(30, 390)">
                  <rect width="680" height="150" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#9333ea"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">syncPayload : FactorySyncPayload</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">BatchId = "BATCH-RSV-20261112-140000"</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">ContainedOrders = ["MO-202611-0042", "MO-202611-0043", "MO-202611-0044"]</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">PayloadSize = 1,248,392 bytes (Compressed GZIP: 214KB)</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#15803d" font-weight="bold">IntegrityChecksum = "sha256:8f419c8b74..." (Verified on RDV)</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">AckReceivedAt = 2026-11-12 14:00:14 ｜ CommitStatus = Committed</text>
                </g>

                <!-- Object 9: edgeBuffer -->
                <g transform="translate(30, 560)">
                  <rect width="680" height="150" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
                  <rect width="680" height="28" fill="#16a34a"/>
                  <text x="340" y="19" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">edgeBuffer_RDV : EdgeBufferQueue</text>
                  <text x="20" y="50" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">Location = "RDV Vietnam Factory On-Prem Storage"</text>
                  <text x="20" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">StorageEngine = "SQLite 3 WAL Mode / Local Disk WAL"</text>
                  <text x="20" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#334155">PendingUpstreamTransactions = 0 (專線健康，實時直送)</text>
                  <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#15803d" font-weight="bold">AutonomousCapacityHours = 72 hours (容許斷網 3 天零停擺)</text>
                  <text x="20" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">HealthHeartbeat = "OK" ｜ LastCheck = 2026-11-12 14:29:55</text>
                </g>

                <!-- Links -->
                <line x1="370" y1="200" x2="370" y2="220" stroke="#9333ea" stroke-width="1.5"/>
                <line x1="370" y1="370" x2="370" y2="390" stroke="#9333ea" stroke-width="1.5"/>
                <line x1="370" y1="540" x2="370" y2="560" stroke="#16a34a" stroke-width="1.5"/>
              </g>
            </svg>
        """

    # We will generate Tabs 5 to 13 with the exact same rich, multi-panel SVG layout!
    # Let's write the remaining cases directly in Python!
    return ""

print("[OK] Loaded base get_svg")
