/**
 * 信源全球 RSI Group · 2027 蜂巢計畫 (Project Hive)
 * 全站存取門禁審計日誌 Webhook 接收端 (Google Apps Script)
 * 
 * 部署指引：
 * 1. 在 Google 雲端硬碟建立一個新的 Google 試算表（命名為：信源全球_蜂巢計畫_全站存取稽核日誌）
 * 2. 點擊頂部選單「擴充功能」->「Apps Script」
 * 3. 刪除原有代碼，將本檔案全部內容複製貼上
 * 4. 點擊「部署」->「新部署」
 *    - 選擇類型：網頁應用程式 (Web app)
 *    - 說明：RSI Gatekeeper Audit Webhook
 *    - 執行身分：我 (Me - 您的 Google 帳號)
 *    - 誰可以存取：任何人 (Anyone)
 * 5. 複製產出的 Web App 網址（https://script.google.com/macros/s/.../exec）
 * 6. 提供該網址，系統將自動寫入 rsi-gatekeeper.js 並推播上線！
 */

function doPost(e) {
  try {
    var sheet = getOrCreateAuditSheet();
    var raw = e.postData ? e.postData.contents : "";
    if (!raw) {
      return responseJson({ status: "error", message: "Empty payload" });
    }
    
    var data = JSON.parse(raw);
    
    // 台北時區標準時間
    var nowTaipei = Utilities.formatDate(new Date(), "Asia/Taipei", "yyyy-MM-dd HH:mm:ss");
    
    // 新增一列完整紀錄 (含自動探測之 IP 與環境指紋)
    sheet.appendRow([
      nowTaipei,
      data.name || "未提供",
      data.company || "未提供",
      data.dept || "未提供",
      data.email || "未提供",
      data.purpose || "未提供",
      data.keyUsed || "無 (申請審核)",
      data.role || "訪客",
      data.status || "UNKNOWN",
      data.ip || "內網/未提供",
      data.location || "未知位置",
      data.isp || "未知電信",
      data.screenRes || "",
      data.referrer || "直接造訪",
      data.path || "/",
      data.userAgent || ""
    ]);
    
    // 格式化最新列的狀態顏色 (欄 9 驗證狀態)
    var lastRow = sheet.getLastRow();
    var statusCell = sheet.getRange(lastRow, 9);
    if (data.status === "VERIFIED_ACCESS") {
      statusCell.setBackground("#DCFCE7").setFontColor("#166534"); // 淺綠底深綠字
    } else if (data.status === "PENDING_APPROVAL") {
      statusCell.setBackground("#FEF3C7").setFontColor("#92400E"); // 琥珀黃底深棕字
    }
    
    return responseJson({ status: "success", row: lastRow, timestamp: nowTaipei });
  } catch (err) {
    return responseJson({ status: "error", message: err.toString() });
  }
}

// 支援 GET 請求以利健康檢查
function doGet(e) {
  return responseJson({
    status: "online",
    system: "RSI Group Gatekeeper Webhook Relay",
    project: "Project Hive 2027",
    timestamp: Utilities.formatDate(new Date(), "Asia/Taipei", "yyyy-MM-dd HH:mm:ss")
  });
}

// 輔助函式：取得或自動初始化米蘭風格稽核工作表
function getOrCreateAuditSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName("存取稽核紀錄");
  if (!sheet) {
    sheet = ss.insertSheet("存取稽核紀錄", 0);
    // 建立米蘭風格表頭 (16 欄全維度審查)
    var headers = [
      "存取時間 (台北)",
      "訪客姓名",
      "所屬廠區 / 機構",
      "部門與職稱",
      "官方 Email",
      "申請 / 查閱事由",
      "使用通行碼",
      "核定角色",
      "驗證狀態",
      "來源 IP 位址",
      "地理位置 (國家/城市)",
      "電信業者 (ISP)",
      "螢幕解析度",
      "來源網址",
      "訪問頁面",
      "瀏覽器與設備"
    ];
    sheet.appendRow(headers);
    
    // 樣式化表頭：米蘭莫蘭迪炭黑底 + 琥珀文字
    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#1A2530")
               .setFontColor("#F59E0B")
               .setFontWeight("bold")
               .setFontSize(11)
               .setHorizontalAlignment("center");
               
    sheet.setFrozenRows(1);
    
    // 設定最適欄寬
    sheet.setColumnWidth(1, 160); // 存取時間
    sheet.setColumnWidth(2, 110); // 姓名
    sheet.setColumnWidth(3, 140); // 廠區
    sheet.setColumnWidth(4, 150); // 部門與職稱
    sheet.setColumnWidth(5, 180); // Email
    sheet.setColumnWidth(6, 260); // 存取事由
    sheet.setColumnWidth(7, 120); // 通行碼
    sheet.setColumnWidth(8, 140); // 角色
    sheet.setColumnWidth(9, 130); // 驗證狀態
    sheet.setColumnWidth(10, 130); // 來源 IP
    sheet.setColumnWidth(11, 150); // 地理位置
    sheet.setColumnWidth(12, 160); // ISP
    sheet.setColumnWidth(13, 110); // 螢幕解析度
    sheet.setColumnWidth(14, 160); // 來源網址
    sheet.setColumnWidth(15, 160); // 頁面
    sheet.setColumnWidth(16, 220); // 設備
  }
  return sheet;
}

function responseJson(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
