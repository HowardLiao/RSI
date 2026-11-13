# 信源全球 2027 蜂巢計畫｜技術規格與架構評估專案報告
## Duke 11/12 交付之集團三大核心系統 (RD_SAMPLE、D365、CQS) 與 API 全量清冊深度剖析與落地處方

* **專案計畫**：信源全球 2027 蜂巢計畫 (Project Hive 2027)
* **計畫主持人**：周文津 副總
* **執行負責人 / 外部資訊顧問**：Howard Liao Ph.D.
* **記錄整理 / 研發資訊主管**：Duke Chen
* **發布日期**：2026 年 11 月 12 日（2026 年 11 月 13 日完整審核增訂）
* **機密等級**：內部機密（RESTRICTED）
* **文檔編號**：RSI-HIVE-20261112-DUKE-API-SPEC-V2

---

## 一、執行摘要與標竿定位 (Executive Summary)

研發資訊主管 Duke 於 2026 年 11 月 12 日正式提交並確認了信源集團內部核心三大系統之架構與串接盤點資料（對應 RSI 1109 會議決議第一項）：
1. **`RD_SAMPLE` 樣品管理系統（雛型 v0.1）**：包含系統卡、draw.io 雙頁圖、21 條跨系統串接拓撲矩陣（I01～I21）、Windows 排程器 13 項重要定時任務清查及 7 大架構資安風險。
2. **`D365 F&O (ERP)` 核心系統（雛型 v0.1）**：涵蓋地端 LBD 部署拓撲、21 條跨系統串接拓撲矩陣（D01～D21）、海外 8 廠 WMS 資料庫 IP 矩陣、14 個 Service Group / 31 個 Service / 80 個 Operation 之 X++ Custom Service，以及 RSIMDW1 上的 C# 外掛中介層（50 支 API）。
3. **`CQS` 報價成本系統（雛型 v0.1）**：涵蓋 Vue 3 + .NET 8 ASP.NET Core 架構、13 條跨系統串接拓撲矩陣（C01～C13）、177 支 CQS API、5 大批次作業（含致命之 C08 直接寫入生產庫 AXDB 議題）及 IIS ARR 反向代理拓撲。
4. **`API List` 全量清冊**：整合 D365 C# 外掛 API（Report API、Local API）、共用資料模型 `RqtBaseForm`（14 個共用欄位）、X++ Custom Service 規範（Azure AD Bearer Token 驗證）與共用回傳格式 `RSI_RT`。

**顧問評估結論**：
Duke 所主導之三大系統盤點展現了卓越的工程紀律與深度，全量 55 條串接拓撲（I01～I21, D01～D21, C01～C13）與 13 項排程任務已全面確認，正式定調為信源集團各廠區系統盤點的**「金牌示範標竿（Gold Standard）」**。本報告依據全量規格進行深度評鑑，提出 4 大工程落地處方，並列出向 Duke 溫暖致謝與 5 大技術對齊議題。

---

## 二、模組一：RD_SAMPLE 樣品管理系統（雛型 v0.1）深度解構

### 1. 系統基本資料卡 (SOFT-00)
* **系統代號**：RD_SAMPLE (SOFT-00)
* **系統名稱**：樣品管理系統（打樣／研發流程）
* **技術棧**：前端 ASP.NET WebForms (.NET 4.8) + Knockout.js / jqxGrid；後端自寫 DataAccess (ADO.NET 直連 SQL)；Tech Pack 解析器採用 Python。
* **部署主機**：
  * 正式機：`RDSMP2` (192.168.0.22)
  * 測試機：`RDSMP1` (192.168.0.23)
* **版控與 CI/CD**：GitLab `rd/rd_sample`；Runner 位於 RDSMP1，dev 分支部署測試、master 分支部署正式（msbuild + robocopy）。

### 2. 21 條跨系統串接拓撲矩陣 (I01～I21 全覽)
| 編號 | 對象系統 | 方向 | 串接方式／協定 | 端點（正式） | 觸發 | 用途說明 | 依據 |
|---|---|---|---|---|---|---|---|
| I01 | 使用者瀏覽器 | ← | HTTPS 443 | `rdsample.rsiapparel.com` (192.168.0.22) | 即時 | 系統操作與打樣維護 | Web.config |
| I02 | 本地 SQL Server | → | TDS 1433 (ADO.NET) | RDSMP2 (192.168.0.22) / RD_SAMPLE | 即時 | 樣品業務主庫讀寫 | 連線字串 |
| I03 | PDFTAG 資料庫 | → | 同 SQL 執行個體跨庫查詢 | RDSMP2 / PDFTAG | 即時 | Tech Pack 結構化資料比對 | 程式碼查詢 |
| I04 | CQS 資料庫 | → | 同 SQL 執行個體跨庫查詢 | RDSMP2 / CQS | 即時 | 報價用量與成本查詢 | 程式碼查詢 |
| I05 | 越南廠區 RDV 庫 | → | TDS 1433 (專線直連) | 192.168.185.123 / RDV_SAMPLE | 排程 30分 | 越南打樣進度同步 (Sync_RSV.bat) | 排程腳本 |
| I06 | 柬埔寨廠區 RDG 庫 | → | TDS 1433 (專線直連) | 192.168.193.65 / RDG_SAMPLE | 排程 30分 | 柬埔寨打樣進度同步 (Sync_RSG.bat) | 排程腳本 |
| I07 | D365 AXDB 主庫 | → | TDS 1433 直讀 (sa 帳號) | RSIAXDB1 (192.168.0.131) / AXDB | 即時+排程 | 23 處直讀物料、顏色、客戶主檔 | GetDatabase("AX") |
| I08 | D365 C# Local.WebApi | → | HTTP 80 | RSIMDW1 (192.168.0.95) / Auth | 即時 | 代為取得 D365 Bearer Token | AX_token 設定 |
| I09 | D365 X++ Custom Service | → | HTTPS 443 (Bearer) | AOS / api/services/JCOM_* | 即時 | 拋轉日記帳、採購與物料異動 | ERP_API_Model.cs |
| I10 | D365 ERP (反向呼叫) | ← | SOAP ASMX | RDSMP2 / SAM/WEBSERVICE/RdsmpService.asmx | ERP 觸發 | RequestBOM, 同步主檔資料 | ASMX 原始碼 |
| I11 | UOF BPM 簽核系統 | → | SOAP over HTTPS | bpm.rsiapparel.com (192.168.8.226) | 即時 | 樣品核准流程簽核 | BPMService.cs |
| I12 | UOF BPM 資料庫 | → | TDS 1433 直讀 | 192.168.8.226 / UOF | 即時 | 簽核狀態與歷程查詢 | 連線字串 |
| I13 | 郵件伺服器 | → | SMTP 25 | 192.168.0.35 (RSIMBX1) | 排程/即時 | 發送打樣通知信 (SendNotification.bat) | MailHelper.cs |
| I14 | AWS AI 規格推論服務 | → | HTTP 8000 | 98.84.29.205:8000 / inference | 即時 | Tech Pack 智慧版型推論 | 呼叫端程式碼 |
| I15 | AWS 翻譯服務 | → | HTTP 80 | 98.93.175.234:80 / translate | 即時 | 規格說明中越英多語系翻譯 | 呼叫端程式碼 |
| I16 | 檔案共用伺服器 | → | SMB 445 | \192.168.0.22\Storage | 即時 | 樣品圖檔、PDF Tech Pack 存放 | 路徑設定 |
| I17 | 舊版圖檔伺服器 | → | HTTP 8081 | 192.168.0.23:8081 (依賴測試機!) | 即時 | 舊款樣品照片檢視 (FindImage) | 程式碼硬編碼 |
| I18 | AD 網域控制站 | → | LDAP 389 | 192.168.0.10 (RSIAD1) | 即時 | 人員帳號密碼 Windows 驗證 | Membership |
| I19 | GitLab CI Runner | ← | SMB 445 (robocopy) | GitLab (192.168.10.134) -> RDSMP2 | push CI | 程式碼編譯部署覆蓋 | gitlab-ci.yml |
| I20 | 舊版 MSC DB (已停用) | → | TDS 1433 | 192.168.3.120 / MSC2003 | — | 停用殘留連線 (部分報表殘留) | Web.config |
| I21 | 舊版 MES DB (停用查核) | → | TDS 1433 | 192.168.0.125 / MES_OLD | — | 停用殘留連線 | Web.config |

### 3. Windows 工作排程器 13 項重要任務明細
1. `SendNotification.bat`：每 5 分鐘執行，發送打樣逾期與簽核通知。
2. `Sync_RSV.bat`：每 30 分鐘執行，雙向同步越南廠打樣進度（程式內建 23:00–06:00 避峰）。
3. `Sync_RSG.bat`：每 30 分鐘執行，雙向同步柬埔寨廠打樣進度（程式內建 23:00–06:00 避峰）。
4. `DailySewnReport.bat`：週一至六 06:01 執行，匯總前日車縫樣品產能日報。
5. `SyncHRM.bat`：每日 10:45 執行，自人資系統同步員工組織與離在職名單。
6. `ScheduleSummary.bat`：週一至六 21:01 執行，計算當日打樣進度甘特排程統計。
7. `updateColorFromERP.bat`：每日 23:01 執行，自 D365 AXDB 同步標準顏色代碼。
8. `updateColorMappingFromERP.bat`：每日 23:15 執行，同步買主顏色映射主檔。
9. `InsertMaterialERP.bat`：每日 23:19 執行，將打樣新料號回拋 ERP 審核暫存檔。
10. `updateMaterialERP.bat`：每日 23:31 執行，自 D365 更新物料最新採購狀態與單價。
11. `SP_FITSOP_NT.bat`：每週日 20:00 執行，重算全廠試穿樣（Fit Sample）標準工時。
12. `DeleteRpaFile.bat`：每週日 02:07 執行，清理伺服器暫存 RPA 圖檔與 PDF 暫存。
13. `UpdateCustEstSMV.bat`：每半年（1/1、7/1）10:58 執行，更新客戶預估標準工時矩陣。

### 4. 7 大架構與資安盤點風險 (R1～R7)
* **R1 明碼帳密**：Web.config 與 bat 腳本內硬編碼資料庫帳密。
* **R2 全數 sa 權限連線**：跨庫查詢使用 sa 帳號，缺乏最小權限原則。
* **R3 正式機依賴測試機**：I17 舊圖檔介面正式機指向 `192.168.0.23:8081`（測試機），測試機若當機影響正式環境。
* **R4 AWS 公網未加密連線**：I14、I15 呼叫公有雲 AI 服務走未加密 HTTP 明文，存在中間人竊聽風險。
* **R5 跨國專線 TDS 1433 直連**：I05、I06 跨國直接以 TDS 協定同步資料，海纜延遲或斷線容易引發連線逾時。
* **R6 SQL 字串拼接**：歷史老舊程式碼存在 SQL 字串拼接寫法，具 SQL 隱碼風險。
* **R7 跨系統直讀 DB 與 MSC 殘留**：直讀 AXDB 造成 ERP 結構更動風險，且已停用 MSC 伺服器連線未徹底移除。

---

## 三、模組二：D365 F&O (ERP) 核心系統（雛型 v0.1）深度解構

### 1. 系統基本資料卡 (D365)
* **系統代號**：D365
* **系統名稱**：Microsoft Dynamics 365 Finance & Operations (ERP)
* **部署型態**：**地端部署（LBD, Local Business Data）**：Service Fabric 叢集＋SQL Server＋ADFS，全部位於台北總部機房。
* **系統負責單位**：ERP 組
* **預設公司別**：`DataAreaId = GRSI`
* **客製範圍**：
  * X++ model：`JCOM_WebServices`（顧問廠商 JCOM）、`RSI_WebServices`（自研）。
  * Custom Service：共 **14 個 Service Group、31 個 Service、80 個 Operation**。
* **外掛中介層**：C# (.NET Framework 4.8 / ASP.NET Web API 2)，部署於 `RSIMDW1 (192.168.0.95)`。
  * `Local.WebApi`（24 支 API）
  * `D365.Report.Service`（26 支報表 API）
  * `Local.Batch`（背景排程批次）
  * `ERP_WMS_inventory`（ERP 與 WMS 庫存對帳服務）
* **環境端點**：
  * 正式：`rsiax.rsiapparel.com`
  * 測試：`labax.rsiapparel.com` (LAB)
  * 開發：RSIAXDEV1～9 開發虛擬機
* **身分驗證**：走地端 ADFS（`d365ffoadfs.rsict.com.tw`）OAuth2；外掛提供 `/Auth` 代取 Bearer Token。
* **版控與 CI**：C# 外掛由 GitLab `d365/d365` 管理，Runner 在 RDSMP1，robocopy 至 `\\192.168.0.95\d$\D365`；X++ 由 RSIAXDBT1（192.168.0.130）建置經 LCS 套件發布。

### 2. 21 條跨系統串接拓撲矩陣 (D01～D21 全覽)
| 編號 | 對象系統 | 方向 | 串接方式／協定 | 端點（正式） | 觸發 | 用途說明 | 依據 |
|---|---|---|---|---|---|---|---|
| D01 | 使用者瀏覽器 | ← | HTTPS 443 (ADFS) | `rsiax.rsiapparel.com` (AOS x3 DNS輪詢) | 即時 | 總部與各廠日常 ERP 業務操作 | DNS |
| D02 | ADFS 認證伺服器 | → | OAuth2 / OpenID (HTTPS 443) | `d365ffoadfs.rsict.com.tw` (192.168.0.109) | 即時 | 使用者登入與服務權杖發行 | 外掛設定檔 |
| D03 | AXDB (D365 主庫) | → | TDS 1433 (鏡像高可用) | RSIAXDB1 .131 / RSIAXDB2 .132 | 即時 | D365 核心財務交易與業務資料 | 外掛設定檔 |
| D04 | SSRS / MR 報表 | → | 內部 Service Fabric 通訊 | RSIAXSRS1 .129; RSIAXMR1/MR2 .127~.128 | 即時 | 財務報表、發票與出貨單據產生 | ERP 組確認 |
| D05 | RD_SAMPLE 系統 | ← | HTTPS 443 (/api/services/...) | JCOM_ImportJournalServices 等 5 類服務 | 即時 | 物料入庫、日記帳、MS/PO 查詢 | rd_sample RouteFile |
| D06 | RD_SAMPLE 系統 | ← | HTTP 80 | Local.WebApi `GET /Auth` (RSIMDW1) | 即時 | 代取 D365 授權 Bearer Token | rd_sample AX_token |
| D07 | RD_SAMPLE 系統 | ← | TDS 1433 直讀 (帳號 wms) | AXDB (192.168.0.131) | 即時+排程 | 約 23 處直讀物料、顏色、客戶主檔 | rd_sample 原始碼 |
| D08 | 生產周邊 (MES/WMS/APS/QMS) | ← | HTTPS 443 (/api/services/...) | JCOM_MESToERPServices, JCOM_Production 等 | 即時/批次 | 生產工單、報工、領料、出貨拋轉 | Notion X++ 清單 |
| D09 | 外掛 Local.Batch | → | HTTPS 443 (/api/services/...) | AOS (RSI_Services/RSI_DailyBatch/*) | 排程 | 每日同步產地、目的地、款式、客戶、SMV | RouteFile.json |
| D10 | 外掛程式 (三支) | → | TDS 1433 直讀 (帳號 sa) | AXDB (192.168.0.131) | 即時+排程 | 報表與查詢直接讀取 D365 資料表 (約 22 處) | ConnectionStrings |
| D11 | ODS 操作資料庫 | → | TDS 1433 | 192.168.0.7 (RSIESB1) / ODS | 即時+排程 | 報表資料來源、物料與銷售控制 | Report API 設定 |
| D12 | MSC2003 (舊 ERP) | → | TDS 1433 (已停用) | 192.168.0.120 / MSC2003 | — | 歷史 MSC 版報表 (物料需求、採購) | Report API 設定 |
| D13 | 廠區 WMS 資料庫 (8 廠) | → | TDS 1433 (跨國專線, whuser) | 各海外廠 WMS 資料庫 (見下表) | 即時+排程 | 庫存報表、ERP 與 WMS 庫存差異比對 | ERP_WMS_inventory |
| D14 | RD_SAMPLE 資料庫 | → | TDS 1433 | RDSMP2 (192.168.0.22) / RD_SAMPLE | 即時 | Local.WebApi「RD 樣品」API (8 支) | Local.WebApi 設定 |
| D15 | RSIERP 資料庫 | → | TDS 1433 (EF) | 192.168.0.11 / RSIERP (殘留設定未呼叫) | — | 歷史系統殘留連線設定 | Local.Batch 設定 |
| D16 | 外掛自用資料庫 | → | TDS 1433 | RSIMDW1 / D365_Prod, D365_Uat | 即時 | Buyfile、參數設定、檔案匯出紀錄 | 外掛設定檔 |
| D17 | 報表檔案下載服務 | ← | HTTP 80 | `http://192.168.0.95/Storage/...` | 即時 | 報表 API 回傳之靜態檔案下載 URL | Report API 程式 |
| D18 | 集團郵件伺服器 | → | SMTP 587 | `mail.rsiapparel.com` | 排程 | 庫存差異通知、批次錯誤告警 (mis_erp@) | ERP_WMS_inventory |
| D19 | 報表 API 呼叫端 | ← | HTTP 8085 (Prod) / 8082 (UAT) | `D365.Report.Service` (RSIMDW1) | 即時 | EDD 報表匯出 (呼叫端為 D365 畫面) | Notion C# API 清單 |
| D20 | GitLab CI 部署 | ← | HTTP 拉碼 + SMB 445 robocopy | GitLab (192.168.10.134) -> RSIMDW1 | push CI | C# 外掛自動化建置與伺服器部署 | .gitlab-ci.yml |
| D21 | D365 ERP (主動反拋) | → | SOAP (ASMX) | RD_SAMPLE / SAM/WEBSERVICE/RdsmpService.asmx | ERP 觸發 | RequestBOM, 同步品項、顏色、客戶 | rd_sample I10 |

### 3. 海外廠區 8 廠 WMS 資料庫對照矩陣 (D13)
| 廠區代碼 | 廠區名稱／地點 | 資料庫主機 IP | 預設資料庫名稱 | 連線協定與帳號 |
|---|---|---|---|---|
| **RSA** | 總部廠區 A | `192.168.50.6` | `WareHousing` | TDS 1433 / whuser |
| **RSB** | 越南廠區 B | `192.168.33.11` | `WareHousing` | TDS 1433 / whuser |
| **TOP** | 越南 TOP 廠 | `192.168.33.124` | `WareHousing` | TDS 1433 / whuser |
| **RSG** | 柬埔寨 RSG 廠 | `192.168.168.6` | `WareHousing` | TDS 1433 / whuser |
| **RSK** | 柬埔寨 RSK 廠 | `192.168.60.9` | `WareHousing` | TDS 1433 / whuser |
| **RSV** | 越南 RSV 廠 | `192.168.97.8` | `WareHousing` | TDS 1433 / whuser |
| **SY** | 緬甸 SY 廠 | `192.168.180.34` | `WareHousing` | TDS 1433 / whuser |
| **RVT** | 越南 RVT 廠 | `192.168.113.34` | `WareHousing` | TDS 1433 / whuser |

### 4. X++ Custom Service 架構分類清單 (14 類 Service Group / 80 Operations)
| Service Group 群組名稱 | 包含 Service 數 | Operation 數 | 核心業務用途與主要呼叫端系統 |
|---|---|---|---|
| **JCOM_MatTransServices** | 4 (MS, MT, MAB, ADJ) | 16 | 物料各類異動（領料、調撥、調整）；主要由 RD_SAMPLE 與 WMS 呼叫 |
| **JCOM_SalesServices** | 3 | 8 | 款式主檔維護、外箱標籤裝箱、客戶發票處理 |
| **JCOM_ProductionServices** | 3 | 6 | 生產工單拋轉、現場報工、領料過帳；主要由 MES 呼叫 |
| **JCOM_SalesOrderToMES** | 3 | 4 | 銷售訂單 (SO) 拋轉 MES 製造現場排產 |
| **JCOM_MESToERPServices** | 1 | 1 | MES 製造現場工單完成與用料即時回拋 ERP |
| **JCOM_NonMPOPickingJournalService**| 1 | 3 | 非 MPO 生產領料日記帳維護 |
| **JCOM_ImportJournalServices** | 1 | 2 | 外部日記帳批次匯入；主要由 RD_SAMPLE 呼叫 |
| **JCOM_BomImportFromRDServices** | 1 | 2 | 自研發樣品系統匯入標準 BOM |
| **JCOM_LBServices** | 2 | 2 | 外部供應商裝箱單核對、採購單 (PO) 狀態即時查詢 |
| **JCOM_LDServices** | 1 | 1 | LD 實驗室打色與配方數據同步 |
| **JCOM_APSServices** | 1 | 1 | 高級排程系統物料毛淨需求運算介面 |
| **JCOM_PrepareMaterialService** | 1 | 1 | 生產前置備料指示與齊料檢驗 |
| **RSI_Services** | 8 (DailyBatch, Agent 等) | 30 | 自研外掛排程、Buyfile 買主檔、QMS 品管、異常工單管理 |
| **RSI_SynchronizeDataToRDSampleServices** | 1 | 3 | 核心品項 (Items)、顏色 (Colors)、客戶 (Customers) 同步至樣品系統 |

---

## 四、模組三：CQS 報價成本系統（雛型 v0.1）深度解構

### 1. 系統基本資料卡 (CQS)
* **系統代號**：CQS
* **系統名稱**：報價成本系統 (Cost Sheet)
* **業務定位**：物料主檔維護、產生／核准內外部報價單、報價歷程追蹤、報價用量回寫 ERP、實際用量成本差異分析。
* **技術棧**：
  * 前端：Vue 3 + Vite + TypeScript (現代化 SPA 單頁應用)
  * 後端：CQSService (.NET 8 / ASP.NET Core Web API, EF Core)
  * 批次：CQS_Batch (.NET 8 Console 批次執行檔)
* **API 規模現況**：共計 **177 支 API**：
  * CostSheet 報價核心：63 支
  * Material 物料維護：40 支
  * ERP 介接：12 支
  * 系統管理權限：34 支
  * 其他輔助功能：28 支
* **身分驗證**：IIS Windows 整合驗證（AD 帳號），登入後自動映射 CQS 系統使用者。
* **資料庫環境**：CQS 主庫；另跨庫查詢 PDFTAG、RD_SAMPLE (同 SQL 實例)，並直連 D365 AXDB。
* **主機環境**：正式 RDSMP2 (`192.168.0.22`) Web 8012 / API 8011；測試 RDSMP1 (`192.168.0.23`) Web 8012 / API 8011。
* **部署與版控風險**：GitLab `cqs/cqs`，**目前完全沒有 CI/CD 管道**，採人工手動複製覆蓋伺服器部署。

### 2. 13 條跨系統串接拓撲矩陣 (C01～C13 全覽)
| 編號 | 對象系統 | 方向 | 串接方式／協定 | 端點（正式） | 觸發 | 用途說明 | 依據 |
|---|---|---|---|---|---|---|---|
| C01 | 使用者瀏覽器 | ← | HTTP 8012 (Windows 驗證) | `http://192.168.0.22:8012` | 即時 | 報價人員維護報價單與成本試算 | BPM 設定 CQSUrl |
| C02 | CQSService API | 內部 | HTTP 8011 `/api/*` | `http://192.168.0.22:8011` | 即時 | 前端 SPA 呼叫後端 REST API | .env.production |
| C03 | CQS 專屬資料庫 | → | TDS 1433 (EF Core) | RDSMP2 / CQS | 即時+排程 | 報價核心業務資料持久化 | CQSDatabase |
| C04 | PDFTAG 資料庫 | → | TDS 1433 | RDSMP2 / PDFTAG | 即時 | 由 Tech Pack 自動產生報價料號對照 | PDFDatabase |
| C05 | RD_SAMPLE 資料庫 | → | 同 SQL 實例跨庫查詢 | RDSMP2 / RD_SAMPLE.dbo.* | 即時+排程 01:00 | 讀取物料、顏色、客戶與用碼量 | commonFunction.cs |
| C06 | D365 AXDB 主庫 | → | TDS 1433 直讀 (sa 帳號) | RSIAXDB1 (192.168.0.131) | 即時 | 查詢 ERP 料號、BOM 與實際發料 | ERPDatabase |
| C07 | D365 AXDB (Linked Server) | → | SQL Server Linked Server | `[RSIAXDB1].[AXDB]` | 即時 | 跨庫取系統標準 SMV 工時值 | costSheetFunction.cs |
| **C08**| **D365 AXDB (直接寫入!)** | → | **TDS 1433 直接 UPDATE** | `UPDATE BOM SET JCOM_BOMQTYQUOTE` | **操作即時觸發** | **報價用量直接回寫生產主 BOM** | **CQSUpdateERPBOMQtyQuote** |
| C09 | D365 外掛 Local.WebApi | → | HTTP 80 經 IIS ARR 轉發 | RSIMDW1 (192.168.0.95) /rd/MarkAndTrimInfo | 即時 | 取樣品馬克圖與副料用量資訊 | ARR 反向代理 |
| C10 | BPM 簽核系統 | → | SOAP over HTTPS | bpm.rsiapparel.com (192.168.8.226) | 即時 | 報價單送簽（依毛利率動態核決） | BPMService.cs |
| C11 | RD_SAMPLE 系統 | ← | HTTP 經 ARR 轉 8011 | 192.168.0.22:8012 /api/SysUser/CreateSysUser | 即時 | RD 建立帳號時同步建 CQS 帳號 | FND004ViewModel |
| C12 | 集團郵件伺服器 | → | SMTP 25 (帳號 Notify) | 192.168.0.35 (RSIMBX1) | 批次執行時 | 發送批次執行結果與異常通知 | MailSender.cs |
| C13 | RD_SAMPLE 網站 | → | 網頁超連結跳轉 | `https://rdsample.rsiapparel.com/SAM/STYLE/` | 即時 | 從報價單直接開樣品款式明細頁 | RDSampleWeb 設定 |

### 3. CQS_Batch 5 大批次作業詳細對照
* **執行主機**：RDSMP2 正式機 (`192.168.0.22`) `D:\CQSService\Batch\CQS_Batch.exe`。
1. **`RDSAMPLEInsertMaterial`** (RD_SAMPLE → CQS)：排程每日 01:00 執行，亦可由畫面手動點擊；將樣品新物料同步寫入 CQS 物料庫。
2. **`CQSUpdateERPBOMQtyQuote`** (CQS → **AXDB 直接寫入**)：**重大架構卡點**！由使用者在畫面審核時以 `Process.Start` 即時啟動，直接下 SQL UPDATE 覆寫 D365 生產庫中的 BOM 用量。
3. **`CQSCreateCABatch`** (AXDB → CQS)：使用者點擊成本分析時以 `Process.Start` 啟動，依 ERP 實際發料計算各色組實際用量與成本偏差。
4. **`TPInsertMaterial`** (PDFTAG → CQS)：**已停用**；早期將 Tech Pack 料號寫入物料主檔之批次。
5. **`ERPUpdateMaterial`** (AXDB → CQS)：**已停用**；早期更新 ERP 物料主檔之舊程式。

---

## 五、模組四：集團三大 API 清冊與標準化契約 (API List)

### 1. D365 C# 外掛 API 雙核心專案 (RSIMDW1 192.168.0.95)
* **`D365.Report.Service` (Report API)**：
  * UAT：`http://192.168.0.95:8082/swagger`（規格檔：`/swagger/docs/v1`）
  * Prod：`http://192.168.0.95:8085`（無 Swagger 介面）
  * 共 26 支報表匯出 API，回傳產生的靜態檔案下載 URL 字串。
* **`Local.WebApi` (Local API)**：
  * UAT：`http://192.168.0.95:8081/swagger`（規格檔：`/swagger/docs/v1`）
  * Prod：`http://192.168.0.95:80`（無 Swagger 介面）
  * 共 24 支業務 API（含 `/Auth` 代取 Bearer Token、RD 樣品 8 支 API、庫存同步等）。
* **共用 Request Model (`RqtBaseForm`)**：
  * 繼承欄位：`SalesId`, `StyleNo`, `ContractNo`, `ContractGroup`, `PurchId`, `ItemId`, `VendId`, `CustId`, `_key`, `BuyKeys`, `ContractNos`, `BatchNos`, `DataAreaId`, `UserName`。

### 2. D365 X++ Custom Service (80 Operations 呼叫契約)
* **呼叫格式**：一律 `POST https://<host>/api/services/<serviceGroup>/<service>/<operation>`，`Content-Type: application/json`。
* **身分驗證**：必須帶 Azure AD / ADFS Bearer Token（`Authorization: Bearer <token>`），呼叫端 App 必須於 Microsoft Entra 登記。
* **共用 Response Model (`RSI_RT`)**：
  ```json
  {
    "IsValid": true,
    "Msg": "Operation Succeeded",
    "TotalCount": 150,
    "DataList": [ { ... } ]
  }
  ```

---

## 六、Howard Liao Ph.D. 首席顧問四大工程處方

### 處方一：C08 直接寫入 AXDB 之「防腐層隔離與事件驅動重構」
* **問題根因**：CQS 報價系統直接下 SQL UPDATE 覆寫 D365 AXDB 主庫的 `BOM.JCOM_BOMQTYQUOTE`，跳過 ERP 商業邏輯驗證、審計軌跡與併發鎖定，一旦連線中斷或欄位驗證失敗將破壞 ERP 交易一致性。
* **工程解方**：
  1. 立即廢除 `UPDATE BOM` 直接連線，改由 D365 Custom Service 新增 `RSI_BOMQuoteUpdateService`。
  2. CQS 透過 API 發送報價審核事件，由 D365 內部 X++ 交易事務（ttsbegin / ttscommit）進行校驗回寫，確保 ERP 內部審計日誌完整。

### 處方二：三大跨系統拓撲（55 條連線）資安收斂與 API Gateway 落地
* **問題根因**：全案存在 21 (RD_SAMPLE) + 21 (D365) + 13 (CQS) = 55 條串接拓撲，其中多達 15 處直接以 sa 或 whuser 帳號透過 TDS 1433 直連跨國資料庫，且 C# 外掛 80/8085 端口全無認證。
* **工程解方**：
  1. 導入輕量級 API Gateway（Envoy / IIS ARR 強化），將所有 HTTP 端口統一收斂至 HTTPS 443，強制掛載 Entra ID / ADFS JWT 驗證。
  2. 跨國資料庫直連（如 8 廠 WMS、越南 RDV、柬埔寨 RDG）全面封裝為 RESTful API，禁止跨國 WAN 暴露 TDS 1433 端口。

### 處方三：海外 8 廠離線自律 (48-72 小時) 與非同步補償佇列
* **問題根因**：海外各廠區現場依賴總部連線，海纜中斷時容易導致打樣與現場生產停擺。
* **工程解方**：
  1. 各海外廠區本地部署 SQLite / 本地 SQL 快取，維護未來 72 小時所需之款式、物料與工單快照。
  2. 本地作業產生之異動寫入本地非同步佇列，待專線恢復後透過 idempotency key 自動增量回傳總部，確保「斷網不停產、復網不衝突」。

### 處方四：CQS 與 C# 外掛之 CI/CD 現代化標準化
* **問題根因**：CQS 系統目前完全無 CI，採人工覆蓋檔案；外掛雖有 GitLab Runner 但採 robocopy 覆蓋，缺乏自動化測試與回滾機制。
* **工程解方**：
  1. 為 `cqs/cqs` 建立 GitLab CI 腳本，結合 Docker 或 IIS Web Deploy 實現藍綠無中斷部署。
  2. 導入組態設定外部化（如 Azure Key Vault 或機密管理檔），杜絕程式碼與 Web.config 中殘留明碼帳密。

---

## 七、向 Duke 溫暖致謝與 5 大面向技術對齊探討清單

> **致 Duke 的技術致敬簡函**：  
> 「Duke 您好：非常感佩您與研發、ERP 團隊在 11/12 所整理交付的整套系統規格與串接矩陣！從 RD_SAMPLE 的 21 條拓撲、D365 的 21 條拓撲到 CQS 的 13 條連線與 177 支 API，資料極具系統性與工程穿透力，為蜂巢計畫 2027 奠定了最堅實的基準。為了讓後續架構升級更加平穩，顧問團隊在此列出 5 個技術焦點，期待與您溫暖對齊交流！」

1. **焦點一【C08 報價回寫 ERP 邊界仲裁】**：
   * 目前 CQS 的 `CQSUpdateERPBOMQtyQuote` 採直接 UPDATE D365 AXDB。評估是否在 2027 蜂巢計畫中，由 ERP 組開放專屬 X++ Custom Service 操作，讓報價用量回寫納入 D365 交易鎖定與審計日誌？
2. **焦點二【C# 外掛 API 驗證機制無縫升級】**：
   * 目前 RSIMDW1 上的 `Report.Service` (:8085) 與 `Local.WebApi` (:80) 無認證。是否可由外掛目前的 `/Auth` 端點延伸，全面加上 ADFS Bearer Token 檢核，防範內網未授權呼叫？
3. **焦點三【海外 8 廠 WMS 跨國 TDS 直連轉型】**：
   * 目前 `ERP_WMS_inventory` 透過專線跨國直連 8 廠 TDS 1433。未來是否規劃在海外廠區部署輕量微服務，將庫存比對改為每日增量 JSON 拋轉，降低專線抖動對總部排程的衝擊？
4. **焦點四【CQS 系統版控與 CI/CD 落地】**：
   * 盤點指出 CQS 前端 (Vue 3) 與後端 (.NET 8) 尚無 CI 自動化部署。顧問團隊可協助於 GitLab 配置建置腳本與 Runner，免除人工覆蓋伺服器檔案的營運風險。
5. **焦點五【正式機對測試機依賴之清理 (I17)】**：
   * 樣品系統 I17 圖檔檢視目前正式機硬編碼指向測試機 `192.168.0.23:8081`。建議安排工單將測試機舊圖檔遷移至正式儲存伺服器，消除此一單點脆弱性。
