# 信源全球 2027 蜂巢計畫｜技術規格與架構評估專案報告
## Duke 11/12 交付之集團三大 API 清單與 RD_SAMPLE 示範範本深度剖析與落地處方

* **專案計畫**：信源全球 2027 蜂巢計畫 (Project Hive 2027)
* **計畫主持人**：周文津 副總
* **執行負責人 / 外部資訊顧問**：Howard Liao Ph.D.
* **記錄整理 / 研發資訊主管**：Duke Chen
* **發布日期**：2026 年 11 月 12 日
* **機密等級**：內部機密（RESTRICTED）
* **文檔編號**：RSI-HIVE-20261112-DUKE-API-SPEC-V1

---

## 一、執行摘要與標竿定位 (Executive Summary)

研發資訊主管 Duke 於 2026 年 11 月 12 日正式交付了信源內部兩份關鍵技術資產清冊：
1. **集團三大 API 清單 (`API-List`)**：完整盤點了 D365 C# 外掛 API、D365 C# 80 Operations (Custom Service)、CQS 品質服務以及 13 項 Windows 排程作業。
2. **樣品管理系統示範範本 (`RD_SAMPLE-v0-1`)**：依據周文津副總「統一使用 draw.io（.drawio 格式）」的最高指導原則，完成了包含系統卡、draw.io 雙頁圖、21 條跨系統串接拓撲矩陣（I01～I21）與 Windows 排程清查。

**顧問評估結論**：
Duke所建立的 `RD_SAMPLE` 規格具備極高成熟度與條理性，正式核定為集團 2027 蜂巢計畫各廠區（總部、越南 RDV、柬埔寨 RDG、印尼）系統盤點的**「金牌示範標竿（Gold Standard）」**。本報告針對交付內容進行架構、資安與營運韌性之深度評鑑，並提出四項具備高落地性的工程處方。

---

## 二、集團三大 API 體系深度解構與體檢

### 1. D365 C# 外掛 API (Report API & Local API)

* **技術棧**：C# (.NET Framework 4.8 / ASP.NET Web API 2)
* **部署主機**：`192.168.0.95` (實體伺服器)
  * **Report API**：UAT: `http://192.168.0.95:8082/swagger` ｜ Prod: `http://192.168.0.95:8085` (無 Swagger)
  * **Local API**：UAT: `http://192.168.0.95:8081/swagger` ｜ Prod: `http://192.168.0.95:80` (無 Swagger)
* **核心資料模型**：所有請求均繼承 `RqtBaseForm`：
  * `SalesId`, `StyleNo`, `ContractNo`, `ContractGroup`, `PurchId`, `ItemId`, `VendId`, `CustId`, `_key`, `BuyKeys`, `ContractNos`, `BatchNos`, `DataAreaId`, `UserName`
* **業務涵蓋範疇**：
  * **馬克（Marker）**：成衣主布用量計算與排料。
  * **PCT**：研發款式代號（Product Development Style Number）。
  * **WIP / F單（Forecast）**：成衣在製品與預測訂單。
  * **SML**：洗標供應商數據同步。
  * **Order Form**：包材訂購單系列（EDD042, 198, 199, 204 等）。
  * **異動類別**：MRP 採購運算、GRN 收貨、MZ 調撥、MS 領用、TR 轉倉、MI 發料、MRI 退料。
* **關鍵架構與資安升級節點**：
  * 🚨 **全無認證機制 (Zero Authentication)**：目前連線至該主機之 80 與 8085 端口無需任何 Token 或憑證，內網任何工作站皆可呼叫。
  * ⚠️ **檔案傳輸模式**：報表 API 僅回傳「內部檔案下載 URL 字串」，而非二進位資料流（Binary Stream），強烈依賴後端內部靜態伺服器之連通性。

### 2. D365 C# Custom Service (80 Operations)

* **技術棧**：Microsoft Dynamics 365 Finance & Operations C# Custom Service
* **管理模型**：`JCOM_WebServices`、`RSI_WebServices`
* **規模現況**：共計 **31 個 Service**、**80 個 Operation**
* **呼叫協定**：
  * Endpoint: `POST https://<D365_URL>/api/services/<ServiceGroup>/<Service>/<Operation>`
  * 鑑權方式：強制採用 **Azure AD Bearer Token**（呼叫端必須於 Microsoft Entra ID 註冊授權 Client ID & Secret）。
* **標準回傳格式 (`RSI_RT`)**：
  ```json
  {
    "IsValid": "Y",
    "Msg": "操作成功",
    "TotalCount": 128,
    "DataList": [ ... ]
  }
  ```
* **自動化文檔工具**：Duke 撰寫之 `Generate-ApiDoc.ps1` 可自動剖析 C# 元數據並導出 OpenAPI/Swagger JSON。

### 3. CQS 品質管控系統 API

* **技術棧**：.NET 8 / ASP.NET Core Web API
* **部署主機**：
  * 測試環境：`http://192.168.0.23:8011`
  * 正式環境：`http://192.168.0.22:8011`
  * 拓撲結構：前端站台（8012）由 IIS ARR (Application Request Routing) 反向代理轉發至後端 8011 服務。
* **特性分析**：多數 API 於 Query String 或 Header 強制帶入 `userId` 做業務級別存取控管；Swagger 於正式機亦保持開啟，需進行權限收斂。

---

## 三、RD_SAMPLE (SOFT-00) 示範範本 21 條介面拓撲全覽

Duke 以研發樣品管理系統為標竿，梳理出 21 條跨系統串接拓撲矩陣：

| 介面代號 | 整合端點系統 | 傳輸協定 / 端口 | 驗證與機制現況 | 架構評估與關鍵升級節點 |
| :--- | :--- | :--- | :--- | :--- |
| **I01** | 使用者前端瀏覽器 | HTTPS 443 | Windows 帳號密碼 | 內網日常操作，體驗正常 |
| **I02** | SAM 研發樣品資料庫 | TDS 1433 | SQL Auth (sa/專用帳號) | **約 1,490 處直接 SQL 存取**，耦合度極高 |
| **I03** | PDFTAG 資料庫 | TDS 1433 | SQL Auth | 樣品標籤圖資管理 |
| **I04** | TechPack 解析程序 | Local Process | 本機 Python CLI 呼叫 | 本機相依性高，未來宜容器化為微服務 |
| **I05** | **跨國廠區資料庫 (越南/柬埔寨)** | **DYXnet 專線 TDS 1433** | SQL Auth | 🚨 **每 30 分鐘總部專線直連寫入海外 SQL**，專線抖動即引發排單死鎖 |
| **I06** | **廠區反向同步總部** | **SQL Linked Server** | SQL Linked Server | 🚨 **跨國 MERGE 同步**，海纜延遲將拖垮總部資料庫鎖定機制 |
| **I07** | **D365 AXDB 營運主庫** | **TDS 1433 (直接 SQL)** | SQL Auth | 🚨 **程式內 23 處直接 SQL 查詢 ERP 主庫**，欠缺讀寫分離 |
| **I08** | D365 OData / Custom API | HTTPS 443 | Azure AD Bearer Token | 標準微服務呼叫，符合現代化規範 |
| **I09** | D365_Prod 唯讀副本 | TDS 1433 | SQL Auth | 報表產出直接讀庫 |
| **I10** | D365 舊 SOAP 服務 | HTTP 80 / SOAP | Basic Auth | 歷史遺留介面，建議逐步淘汰 |
| **I11** | 舊 MSC2003 系統 | TDS 1433 | SQL Auth | **已停用**，待正式排程下線封存 |
| **I12** | MES IEPortal (工時系統) | HTTPS 443 | API Key | 樣品標準工時 (SMV) 資料同步 |
| **I13** | CQS 系統整合 | TDS 1433 + HTTP | DB Direct + ARR Proxy | 樣品檢驗報告與品質異常追蹤 |
| **I14** | BPM 簽核流程系統 | SOAP 80 + SMB 445 | Service Auth + 檔案共享 | 樣品放行與簽核單據交換 |
| **I15** | FindImage 影像比對 | HTTP REST | API Key | 樣品圖片向量特徵比對 |
| **I16** | AWS EC2 AI 樣品推論 | HTTP 8000 (IP 訪問) | Token 鑑權 | 樣品材料自動化識別模型 |
| **I17** | LLM 跨國語言翻譯 | HTTP (IP 訪問) | Bearer Token | 工藝單英越柬多語系翻譯服務 |
| **I18** | 企業 SMTP 郵件通知 | SMTP 587 | TLS / SMTP 認證 | 任務指派與逾期警示信（每 5 分鐘輪詢） |
| **I19** | HRM 人資打卡系統 | SMB 445 (CSV) | 網芳帳密 | 請假資料批次檔案同步 |
| **I20** | 本機檔案儲存 | Local File I/O | Windows ACL | 工藝圖與樣品紙樣暫存檔 |
| **I21** | GitLab CI/CD 自動發布 | SMB 445 (robocopy) | Domain 帳號 | **MSBuild 編譯後網芳覆蓋至正式機**，缺乏藍綠發布防護 |

---

## 四、Windows 排程器 13 項重要定時任務清查

正式機 `192.168.0.22` (路徑 `D:\EXP\`) 掛載之關鍵批次排程：
1. `SendNotification.bat`：**每 5 分鐘** 執行一次，負責 I02 與 I18 郵件通知與待辦派工。
2. `Sync_RSV.bat`：**每 30 分鐘** 執行一次，將總部樣品與工單資料推送至越南廠（I05）。
3. `Sync_RSG.bat`：**每 30 分鐘** 執行一次，將總部樣品與工單資料推送至柬埔寨廠（I05）。
4. `DailySewnReport.bat`：**週一至週六 06:01** 產出車縫日報。
5. `SyncHRM.bat`：**每天 10:45** 執行人資出勤與請假資料同步。
6. `ScheduleSummary.bat`：**週一至週六 21:01** 彙總當日排單與產能負載。
7. `updateColorFromERP.bat`：**每天 23:01** 從 ERP 同步最新顏色主檔。
8. `updateColorMappingFromERP.bat`：**每天 23:11** 同步買主顏色對照表。
9. `InsertMaterialERP.bat`：**每天 23:21** 同步 ERP 新增物料。
10. `updateMaterialERP.bat`：**每天 23:31** 同步 ERP 變更物料主檔。
11. `SP_FITSOP_NT.bat`：**每週日 20:00** 執行試身標準作業程序（Fit SOP）批次運算。
12. `DeleteRpaFile.bat`：**每週日 02:07** 清理自動化 RPA 暫存檔與歷史日誌。
13. `UpdateCustEstSMV.bat`：**每半年 (1/1, 7/1 10:58)** 依據歷史縫製工時校正客戶預估標準工時 (SMV)。

---

## 五、Howard Liao Ph.D. 首席架構師四大工程處方

基於信源全球 2027 蜂巢計畫的戰略目標（穩健營運韌性、地端開源自建、48～72 小時斷網自律），針對 Duke 揭示之架構現況，提出四大落地處方：

### 處方一（資安防禦）：以地端 YARP API Gateway 收攏無認證 C# 外掛
* **挑戰**：`192.168.0.95` 的 Report API 與 Local API 無驗證機制，修改底層 .NET 4.8 專案需耗費大量迴歸測試成本。
* **處方措施**：
  1. 於地端反向代理節點部署 **Microsoft YARP (.NET 8 輕量級開源閘道)**。
  2. 封鎖 `192.168.0.95` 對外部一般網段的直連端口（僅允許 Gateway IP 訪問）。
  3. 由 YARP 掛載 JWT 驗證、IP 白名單與 Rate Limiting 中介軟體。
  4. **效益**：零侵入舊系統程式碼、0 元軟體授權，24 小時內達成 100% 零信任安全收攏。

### 處方二（營運韌性）：解耦 I05/I06 跨國專線 TDS 1433 直連與 Linked Server
* **挑戰**：跨國專線直連與 Linked Server MERGE 同步在海纜不穩時，將造成長交易鎖定（Locking），甚至拖垮總部資料庫。
* **處方措施**：
  1. 廢止跨國資料庫直連 RPC 與 Linked Server。
  2. 改採 **「非同步 API 隊列 ＋ 本地端 SQLite / SQL Express 緩存」**。
  3. 總部將工單與排單異動寫入本地發布佇列；廠區 Agent 透過斷點續傳 Pull 機制抓取並落庫。
  4. **效益**：即使國際專線中斷 48～72 小時，廠區產線依然能正常讀取本地快取進行樣品製作，復網後自動 Reconciliation。

### 處方三（資料治理）：解耦 I07 程式內 23 處直接 SQL 讀取 ERP 主庫 (AXDB)
* **挑戰**：高頻直接下 SQL 查詢 ERP 主庫容易爭搶鎖（Lock Contention），且暴露底層實體 Table 結構。
* **處方措施**：
  1. 導入 CQRS 讀寫分離理念。
  2. 將物料、顏色、BOM 等主檔透過 D365 變更追蹤（Change Tracking）鏡像至地端 **StarRocks 高性能湖倉** 或唯讀副本。
  3. RD_SAMPLE 程式將 23 處 Direct SQL 遷移至只讀視圖（Read-only Views）或快取 API。
  4. **效益**：ERP 核心主庫負載降低 40% 以上，並避免業務報表鎖定生產交易。

### 處方四（制度推廣）：正式將 Duke `RD_SAMPLE` 定為全集團 Week 1 統一填報標準
* **挑戰**：海外廠區（越、柬、印）與總部其他部門系統眾多，盤點格式易各自為政。
* **處方措施**：
  1. PMO 以 Duke 之 `RD_SAMPLE` 為標竿，制定全集團 Week 1 統一範本。
  2. 強制要求各系統負責人必須繳交：
     * **draw.io 雙頁圖檔**（Page 1: 系統架構圖 / Page 2: 部署拓撲圖）。
     * **系統資產卡**（技術棧、依賴庫、資料庫直接 SQL 數量）。
     * **跨系統介面清冊 (I01～IN)**（包含協定、認證方式、頻率、斷網影響）。
     * **Windows 排程任務清查表**。
  3. 於 11/16 召開各廠區填報審查會，由架構委員會依此進行評鑑與統一納管。

---

## 六、規格簽核與記錄

* **計畫主持人**：周文津 副總
* **發布負責**：Howard Liao Ph.D.（外部資訊顧問）
* **記錄整理**：Duke 主管（研發資訊課）
* **收受與會商單位**：信源全球資訊中心、海外工廠資訊部（越南、柬埔寨、印尼）
