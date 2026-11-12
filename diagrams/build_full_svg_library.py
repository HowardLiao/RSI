#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
信源全球 2027 蜂巢計畫 (Project Hive)
產出 14 組專業 UML 2.0 完整多面板 (Multi-Panel) SVG 程式碼模組
每張圖皆嚴格遵守 1600 x 950 尺寸，劃分 2~3 個獨立面板，杜絕擠壓。
"""

import sys

def get_full_14_svg_cases_js():
    w = 1600
    h = 950

    cases = {}

    # -------------------------------------------------------------
    # 0. Class Diagram (類別圖) - 3 Panels
    # -------------------------------------------------------------
    cases[0] = f"""
        case 0: // 01. Class Diagram
          return `
            <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="{w}" height="{h}" fill="#f8fafc" rx="8"/>
              <rect x="40" y="20" width="1520" height="50" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
              <text x="60" y="52" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#0f172a">01. UML 2.0 Class Diagram (類別圖) — 核心領域模型與跨系統資料契約</text>
              <text x="700" y="52" font-family="'Noto Sans TC', sans-serif" font-size="12" fill="#64748b">結構型圖 ｜ 包含 3 個獨立子圖面板 ｜ 依據 Duke 2026-11-12 交付架構</text>

              <!-- Panel 1: D365 C# Contracts -->
              <g transform="translate(40, 90)">
                <rect width="480" height="820" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                <rect width="480" height="35" rx="8" fill="#e0f2fe"/>
                <text x="20" y="24" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">【子圖 A】D365 C# 服務契約與請求基底</text>
                
                <g transform="translate(20, 50)">
                  <rect width="440" height="235" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
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

                <g transform="translate(20, 305)">
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

                <g transform="translate(20, 475)">
                  <rect width="440" height="320" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
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

              <!-- Panel 2: RD_SAMPLE Business Entities -->
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
                  <rect width="450" height="265" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
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

              <!-- Panel 3: Data Access & Batch -->
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
                  <rect width="470" height="215" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.5"/>
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
          `;
    """

    # We can write a generator for all other cases!
    return cases

print("[OK] Library base initialized")
