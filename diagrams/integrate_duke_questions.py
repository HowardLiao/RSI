#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 1. 處理 rsi_duke_uml2_viewer.html
with open('/Users/howard/Desktop/HermesAgent/PortFilio/RSI/rsi_duke_uml2_viewer.html', 'r', encoding='utf-8') as f:
    viewer_html = f.read()

# 替換 "Duke 主管" / "Duka (Duke) 主管"
viewer_html = viewer_html.replace('Duka (Duke) 主管', 'Duke')
viewer_html = viewer_html.replace('Duka Chen (Duke) 主管', 'Duka Chen (Duke)')

# 新增樣式與組件
duke_card_style = """
    /* Duke 提問卡片樣式 */
    .duke-questions-drawer {
      background: rgba(22, 27, 34, 0.95);
      border: 1.5px solid #d29922;
      border-radius: 12px;
      margin: 20px 40px;
      padding: 24px 28px;
      box-shadow: 0 12px 36px rgba(0,0,0,0.4);
      display: block;
      transition: all 0.3s ease;
    }
    [data-theme="milan"] .duke-questions-drawer {
      background: #ffffff;
      border-color: #d97706;
      box-shadow: 0 10px 30px rgba(180, 83, 9, 0.12);
    }
    .duke-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 14px;
      margin-bottom: 16px;
    }
    .duke-title {
      font-size: 18px;
      font-weight: 700;
      color: var(--accent);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .duke-q-item {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border);
      border-left: 4px solid #38bdf8;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 14px;
    }
    [data-theme="milan"] .duke-q-item {
      background: #fdfbf7;
      border-color: #e2ddd5;
      border-left-color: #0284c7;
    }
    .duke-q-title {
      font-weight: 700;
      font-size: 15px;
      color: #38bdf8;
      margin-bottom: 8px;
    }
    [data-theme="milan"] .duke-q-title {
      color: #0284c7;
    }
    .duke-bg-text {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 8px;
      line-height: 1.6;
    }
    .duke-ask-text {
      font-size: 14px;
      color: var(--text-main);
      background: rgba(56, 189, 248, 0.08);
      border-radius: 6px;
      padding: 10px 14px;
      line-height: 1.6;
    }
    [data-theme="milan"] .duke-ask-text {
      background: #f0f9ff;
    }
    .copy-toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #10b981;
      color: #ffffff;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 600;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
      display: none;
      z-index: 9999;
    }
"""

duke_card_html = """
  <!-- Duke 協同提問與架構對齊專區 -->
  <div id="dukeQuestionsCard" class="duke-questions-drawer">
    <div class="duke-header-row">
      <div class="duke-title">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        向 Duke 溫暖致謝與 5 大面向技術對齊探討清單（蜂巢計畫 2027）
      </div>
      <div style="display: flex; gap: 10px;">
        <button class="btn btn-primary" onclick="copyDukeLetter()" style="padding: 6px 14px; font-size: 13px;">
          📋 一鍵複製完整信函
        </button>
        <button class="btn btn-secondary" onclick="toggleDukeCard()" style="padding: 6px 12px; font-size: 13px;">
          隱藏 / 展開
        </button>
      </div>
    </div>

    <div id="dukeContentBody">
      <div style="background: rgba(210, 153, 34, 0.1); border-left: 4px solid #d29922; padding: 12px 18px; border-radius: 6px; margin-bottom: 18px; font-size: 14px; line-height: 1.6;">
        <strong>致謝信函內文摘錄：</strong><br>
        「Duke 您好，辛苦了！非常感謝您在 11/12 如此高效率且條理分明地盤點並交付了集團核心的 API List 與 RD_SAMPLE-v0-1 完整規格！這份技術資產梳理得非常清晰，不僅將複雜的跨系統介面（21 條拓撲）與 13 項核心排程完整透明化，更為我們推進周副總主持的『2027 蜂巢計畫（Project Hive）』奠定了極為扎實、可靠的工程基石。為了協助團隊在後續落地『在地端 48~72 小時斷網自律運轉』與『0 元開源平替架構』時更加平穩順暢，並最大程度降低對您與開發團隊日常維運的負擔，我們在深入研讀這兩份寶貴資料後，整理出以下 5 個面向的協同確認與探討點，想請教並聆聽您的實務經驗與建議：」
      </div>

      <div class="duke-q-item">
        <div class="duke-q-title">1. D365 C# 外掛 API 的邊界防護與 Gateway 平滑收攏</div>
        <div class="duke-bg-text"><strong>現況背景：</strong>清冊中清楚標記了主機 192.168.0.95 上的 Report API（:8085 / :8082）與 Local API（:80 / :8081），主要供各系統取得報表下載 URL 與成衣業務資料（馬克、PCT、WIP 等），目前採取內部信任（無驗證）模式。</div>
        <div class="duke-ask-text"><strong>想請教 Duke：</strong><br>
        • 目前呼叫這兩組 API 的主要來源端（如 RD_SAMPLE 站台、現場特定工作站或批次程式），在底層網路上是否已有既定的 IP 白名單或網段限制？<br>
        • 未來若由在地端輕量 API Gateway（如開源 YARP）在前端統籌掛載 JWT/Token 鑑權做為資安防護閘道，現有呼叫端在配合改帶 Authorization Header 方面，哪一種推進節奏對團隊來說最為平穩（例如：維持既有端口不變、由 Gateway 對外開新路由並設置平行過渡期）？</div>
      </div>

      <div class="duke-q-item">
        <div class="duke-q-title">2. 跨國專線同步與廠區「48～72 小時斷網自律」落地銜接</div>
        <div class="duke-bg-text"><strong>現況背景：</strong>Sync_RSV.bat 與 Sync_RSG.bat 每 30 分鐘透過 DYXnet 專線直連越柬廠區 SQL Server（1433）同步工單與日報資料，維繫了跨國打樣與生產節奏。</div>
        <div class="duke-ask-text"><strong>想請教 Duke：</strong><br>
        • 依據過往經驗，當遇上海纜檢修或跨國專線瞬斷時，海外廠端若無法即時回寫，目前同仁的排解方式主要依賴重跑排程，或是有人工批次對齊的機制？是否有遇過主鍵衝突或時間戳鎖定需要手動處理的情形？<br>
        • 若我們在廠區邊緣端（Local Edge）導入離線暫存隊列，讓越南與柬埔寨在海纜斷線時仍可自律開單、打樣與填報達 72 小時，待專線復原後全自動非同步對齊，生管與打樣現場最核心、最不能中斷的關鍵欄位會建議優先鎖定哪些？</div>
      </div>

      <div class="duke-q-item">
        <div class="duke-q-title">3. RD_SAMPLE 資料庫存取與 AXDB 正式庫連線收斂</div>
        <div class="duke-bg-text"><strong>現況背景：</strong>RD_SAMPLE 內部包含 1,490 處存取 SAM 資料庫的 SQL，並有 23 處跨庫直連 AXDB 營運主庫（192.168.0.131）進行資料讀取。</div>
        <div class="duke-ask-text"><strong>想請教 Duke：</strong><br>
        • 這 23 處直讀 AXDB 的查詢需求（例如料號基本檔、訂單狀態），是否有部分在您梳理的「D365 C# 80 Operations」中已具備對應的 API 服務可供直接調用？<br>
        • 針對高頻查詢部分，若未來透過夜間批次先將 AXDB 所需的唯讀視圖（Read-Only View）鏡像至地端暫存庫，解除直接對 AXDB 的連線依賴，這樣的架構調整是否符合團隊對資料即時性的預期？</div>
      </div>

      <div class="duke-q-item">
        <div class="duke-q-title">4. 13 項核心排程之運作觀測與維運儀表體驗</div>
        <div class="duke-bg-text"><strong>現況背景：</strong>SendNotification.bat 具備 5 分鐘高頻輪詢機制，且夜間 23:01 起有密集的顏色、物料主檔同步排程，是維持集團營運神經中樞的功臣。</div>
        <div class="duke-ask-text"><strong>想請教 Duke：</strong><br>
        • 目前這些排程若在半夜遇到網路逾時或執行例外，內部現行的監控機制是透過文字 Log 巡檢，還是已串接特定的通訊軟體 / 郵件告警？<br>
        • 未來若規劃一個輕量、視覺化的地端任務儀表板（可直接線上查看各排程心跳狀態、執行成功率與一鍵手動補跑），您與團隊在維運習慣上，最希望在儀表板首頁看到哪些即時指標？</div>
      </div>

      <div class="duke-q-item">
        <div class="duke-q-title">5. CQS 品質微服務 (.NET 8) 現代化架構經驗借鏡</div>
        <div class="duke-bg-text"><strong>現況背景：</strong>CQS 已成功建構於 .NET 8 現代化微服務框架上，並由 IIS ARR（8012 轉發至 8011）負責負載調度，架構十分先進！</div>
        <div class="duke-ask-text"><strong>想請教 Duke：</strong><br>
        • CQS 的升級經驗非常適合作為其他系統現代化的示範標竿！想請教目前 IIS ARR 在實際承載高頻品質審核請求時的效能與記憶體表現如何？<br>
        • 正式機環境上的 Swagger 頁面，團隊目前是否有預定的排程做內部權限隔離，或是未來可直接收納至統一的開發者門戶中統一管理？</div>
      </div>
      
      <div style="font-size: 13px; color: var(--text-muted); text-align: right; margin-top: 8px;">
        ※ 再次感謝 Duke 與研發團隊的扎實梳理，以上問題旨在協助後續架構對齊時能最大程度保護現有程式碼、零衝擊產線營運，期待與 Duke 共同推進計畫！
      </div>
    </div>
  </div>

  <div id="copyToast" class="copy-toast">✓ 信函內容已複製到剪貼簿！</div>
"""

duke_js = """
    function toggleDukeCard() {
      const body = document.getElementById('dukeContentBody');
      if (body.style.display === 'none') {
        body.style.display = 'block';
      } else {
        body.style.display = 'none';
      }
    }

    const DUKE_FULL_LETTER = `Duke 您好，辛苦了！

非常感謝您在 11/12 如此高效率且條理分明地盤點並交付了集團核心的 API List 與 RD_SAMPLE-v0-1 完整規格！這份技術資產梳理得非常清晰，不僅將複雜的跨系統介面（21 條拓撲）與 13 項核心排程完整透明化，更為我們推進周副總主持的「2027 蜂巢計畫（Project Hive）」奠定了極為扎實、可靠的工程基石。

為了協助團隊在後續落地「在地端 48~72 小時斷網自律運轉」與「0 元開源平替架構」時更加平穩順暢，並最大程度降低對您與開發團隊日常維運的負擔，我們在深入研讀這兩份寶貴資料後，整理出以下 5 個面向的協同確認與探討點。想請教並聆聽您的實務經驗與建議：

1. D365 C# 外掛 API 的邊界防護與 Gateway 平滑收攏
現況背景：
清冊中清楚標記了主機 192.168.0.95 上的 Report API（:8085 / :8082）與 Local API（:80 / :8081），主要供各系統取得報表下載 URL 與成衣業務資料（馬克、PCT、WIP 等），目前採取內部信任（無驗證）模式。
想請教 Duke：
目前呼叫這兩組 API 的主要來源端（如 RD_SAMPLE 站台、現場特定工作站或批次程式），在底層網路上是否已有既定的 IP 白名單或網段限制？
未來若由在地端輕量 API Gateway（如開源 YARP）在前端統籌掛載 JWT/Token 鑑權做為資安防護閘道，現有呼叫端在配合改帶 Authorization Header 方面，哪一種推進節奏對團隊來說最為平穩（例如：維持既有端口不變、由 Gateway 對外開新路由並設置平行過渡期）？

2. 跨國專線同步與廠區「48～72 小時斷網自律」落地銜接
現況背景：
Sync_RSV.bat 與 Sync_RSG.bat 每 30 分鐘透過 DYXnet 專線直連越柬廠區 SQL Server（1433）同步工單與日報資料，維繫了跨國打樣與生產節奏。
想請教 Duke：
依據過往經驗，當遇上海纜檢修或跨國專線瞬斷時，海外廠端若無法即時回寫，目前同仁的排解方式主要依賴重跑排程，或是有人工批次對齊的機制？是否有遇過主鍵衝突或時間戳鎖定需要手動處理的情形？
若我們在廠區邊緣端（Local Edge）導入離線暫存隊列，讓越南與柬埔寨在海纜斷線時仍可自律開單、打樣與填報達 72 小時，待專線復原後全自動非同步對齊，生管與打樣現場最核心、最不能中斷的關鍵欄位會建議優先鎖定哪些？

3. RD_SAMPLE 資料庫存取與 AXDB 正式庫連線收斂
現況背景：
RD_SAMPLE 內部包含 1,490 處存取 SAM 資料庫的 SQL，並有 23 處跨庫直連 AXDB 營運主庫（192.168.0.131）進行資料讀取。
想請教 Duke：
這 23 處直讀 AXDB 的查詢需求（例如料號基本檔、訂單狀態），是否有部分在您梳理的「D365 C# 80 Operations」中已具備對應的 API 服務可供直接調用？
針對高頻查詢部分，若未來透過夜間批次先將 AXDB 所需的唯讀視圖（Read-Only View）鏡像至地端暫存庫，解除直接對 AXDB 的連線依賴，這樣的架構調整是否符合團隊對資料即時性的預期？

4. 13 項核心排程之運作觀測與維運儀表體驗
現況背景：
SendNotification.bat 具備 5 分鐘高頻輪詢機制，且夜間 23:01 起有密集的顏色、物料主檔同步排程，是維持集團營運神經中樞的功臣。
想請教 Duke：
目前這些排程若在半夜遇到網路逾時或執行例外，內部現行的監控機制是透過文字 Log 巡檢，還是已串接特定的通訊軟體 / 郵件告警？
未來若規劃一個輕量、視覺化的地端任務儀表板（可直接線上查看各排程心跳狀態、執行成功率與一鍵手動補跑），您與團隊在維運習慣上，最希望在儀表板首頁看到哪些即時指標？

5. CQS 品質微服務 (.NET 8) 現代化架構經驗借鏡
現況背景：
CQS 已成功建構於 .NET 8 現代化微服務框架上，並由 IIS ARR（8012 轉發至 8011）負責負載調度，架構十分先進！
想請教 Duke：
CQS 的升級經驗非常適合作為其他系統現代化的示範標竿！想請教目前 IIS ARR 在實際承載高頻品質審核請求時的效能與記憶體表現如何？
正式機環境上的 Swagger 頁面，團隊目前是否有預定的排程做內部權限隔離，或是未來可直接收納至統一的開發者門戶中統一管理？

再次感謝 Duke 與研發團隊的扎實梳理，以上問題旨在協助後續架構對齊時能最大程度保護現有程式碼、零衝擊產線營運，期待與 Duke 共同推進計畫！`;

    function copyDukeLetter() {
      navigator.clipboard.writeText(DUKE_FULL_LETTER).then(() => {
        const toast = document.getElementById('copyToast');
        toast.style.display = 'block';
        setTimeout(() => {
          toast.style.display = 'none';
        }, 2500);
      });
    }
"""

# 注入 CSS
viewer_html = viewer_html.replace('</style>', duke_card_style + '\n</style>')

# 注入 HTML 卡片在 action-bar 之後
action_bar_pos = viewer_html.find('</div>\n\n  <div class="tabs-container">')
if action_bar_pos != -1:
    viewer_html = viewer_html[:action_bar_pos+6] + '\n' + duke_card_html + '\n' + viewer_html[action_bar_pos+6:]
else:
    # 備選位置
    viewer_html = viewer_html.replace('<div class="tabs-container">', duke_card_html + '\n<div class="tabs-container">')

# 注入 JS
viewer_html = viewer_html.replace('function switchTab(index) {', duke_js + '\n    function switchTab(index) {')

with open('/Users/howard/Desktop/HermesAgent/PortFilio/RSI/rsi_duke_uml2_viewer.html', 'w', encoding='utf-8') as f:
    f.write(viewer_html)

print("[SUCCESS] Updated rsi_duke_uml2_viewer.html with Duke alignment card!")


# 2. 處理 duke_api_evaluation_report.html
with open('/Users/howard/Desktop/HermesAgent/PortFilio/RSI/duke_api_evaluation_report.html', 'r', encoding='utf-8') as f:
    report_html = f.read()

report_html = report_html.replace('Duka 主管', 'Duke')
report_html = report_html.replace('Duka Chen (Duke) 主管', 'Duka Chen (Duke)')

# 在導航欄加入 Tab 6 按鈕
nav_marker = '<button class="nav-tab" onclick="switchTab(\'tab-prescription\')">💡 四大工程處方</button>'
new_nav_btn = nav_marker + '\n      <button class="nav-tab" onclick="switchTab(\'tab-duke-questions\')">💬 向 Duke 協同提問 (5大落地點)</button>'
report_html = report_html.replace(nav_marker, new_nav_btn)

# 在內容區加入 Tab 6 頁面
tab_duke_content = """
    <!-- TAB 6: 向 Duke 協同提問與落地對齊清單 -->
    <div id="tab-duke-questions" class="tab-pane">
      <div class="content-card">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 16px; margin-bottom: 20px;">
          <div>
            <h2 style="font-size: 22px; color: var(--accent); margin-bottom: 6px;">💬 向 Duke 溫暖致謝與 5 大面向技術對齊探討清單</h2>
            <div style="color: var(--text-muted); font-size: 14px;">本清單依據 Duke 11/12 交付之 API List (21 條拓撲) 與 13 項排程規格精煉，用於平穩推進 48~72hr 在地自律與 0 元開源架構</div>
          </div>
          <button class="btn btn-primary" onclick="copyDukeLetterReport()" style="padding: 8px 16px; font-size: 14px;">
            📋 一鍵複製完整信函
          </button>
        </div>

        <div style="background: rgba(210, 153, 34, 0.1); border-left: 4px solid #d29922; padding: 16px 20px; border-radius: 8px; margin-bottom: 24px; font-size: 15px; line-height: 1.7;">
          <strong>致謝信函內文：</strong><br>
          「Duke 您好，辛苦了！非常感謝您在 11/12 如此高效率且條理分明地盤點並交付了集團核心的 API List 與 RD_SAMPLE-v0-1 完整規格！這份技術資產梳理得非常清晰，不僅將複雜的跨系統介面（21 條拓撲）與 13 項核心排程完整透明化，更為我們推進周副總主持的『2027 蜂巢計畫（Project Hive）』奠定了極為扎實、可靠的工程基石。為了協助團隊在後續落地『在地端 48~72 小時斷網自律運轉』與『0 元開源平替架構』時更加平穩順暢，並最大程度降低對您與開發團隊日常維運的負擔，我們在深入研讀這兩份寶貴資料後，整理出以下 5 個面向的協同確認與探討點，想請教並聆聽您的實務經驗與建議：」
        </div>

        <div class="prescription-card" style="border-left: 4px solid #38bdf8;">
          <div class="prescription-header">
            <span class="prescription-title" style="color: #38bdf8;">1. D365 C# 外掛 API 的邊界防護與 Gateway 平滑收攏</span>
            <span class="tag tag-primary">資安防護縱深</span>
          </div>
          <p style="margin-bottom: 10px; color: var(--text-muted);">
            <strong>【現況背景】</strong> 清冊中清楚標記了主機 192.168.0.95 上的 Report API（:8085 / :8082）與 Local API（:80 / :8081），主要供各系統取得報表下載 URL 與成衣業務資料（馬克、PCT、WIP 等），目前採取內部信任（無驗證）模式。
          </p>
          <p style="background: rgba(56, 189, 248, 0.08); padding: 12px 16px; border-radius: 6px; line-height: 1.6;">
            <strong>【想請教 Duke】</strong><br>
            • 目前呼叫這兩組 API 的主要來源端（如 RD_SAMPLE 站台、現場特定工作站或批次程式），在底層網路上是否已有既定的 IP 白名單或網段限制？<br>
            • 未來若由在地端輕量 API Gateway（如開源 YARP）在前端統籌掛載 JWT/Token 鑑權做為資安防護閘道，現有呼叫端在配合改帶 Authorization Header 方面，哪一種推進節奏對團隊來說最為平穩（例如：維持既有端口不變、由 Gateway 對外開新路由並設置平行過渡期）？
          </p>
        </div>

        <div class="prescription-card" style="border-left: 4px solid #10b981;">
          <div class="prescription-header">
            <span class="prescription-title" style="color: #10b981;">2. 跨國專線同步與廠區「48～72 小時斷網自律」落地銜接</span>
            <span class="tag tag-success">高可用韌性</span>
          </div>
          <p style="margin-bottom: 10px; color: var(--text-muted);">
            <strong>【現況背景】</strong> Sync_RSV.bat 與 Sync_RSG.bat 每 30 分鐘透過 DYXnet 專線直連越柬廠區 SQL Server（1433）同步工單與日報資料，維繫了跨國打樣與生產節奏。
          </p>
          <p style="background: rgba(16, 185, 129, 0.08); padding: 12px 16px; border-radius: 6px; line-height: 1.6;">
            <strong>【想請教 Duke】</strong><br>
            • 依據過往經驗，當遇上海纜檢修或跨國專線瞬斷時，海外廠端若無法即時回寫，目前同仁的排解方式主要依賴重跑排程，或是有人工批次對齊的機制？是否有遇過主鍵衝突或時間戳鎖定需要手動處理的情形？<br>
            • 若我們在廠區邊緣端（Local Edge）導入離線暫存隊列，讓越南與柬埔寨在海纜斷線時仍可自律開單、打樣與填報達 72 小時，待專線復原後全自動非同步對齊，生管與打樣現場最核心、最不能中斷的關鍵欄位會建議優先鎖定哪些？
          </p>
        </div>

        <div class="prescription-card" style="border-left: 4px solid #f59e0b;">
          <div class="prescription-header">
            <span class="prescription-title" style="color: #f59e0b;">3. RD_SAMPLE 資料庫存取與 AXDB 正式庫連線收斂</span>
            <span class="tag tag-warning">資料庫架構</span>
          </div>
          <p style="margin-bottom: 10px; color: var(--text-muted);">
            <strong>【現況背景】</strong> RD_SAMPLE 內部包含 1,490 處存取 SAM 資料庫的 SQL，並有 23 處跨庫直連 AXDB 營運主庫（192.168.0.131）進行資料讀取。
          </p>
          <p style="background: rgba(245, 158, 11, 0.08); padding: 12px 16px; border-radius: 6px; line-height: 1.6;">
            <strong>【想請教 Duke】</strong><br>
            • 這 23 處直讀 AXDB 的查詢需求（例如料號基本檔、訂單狀態），是否有部分在您梳理的「D365 C# 80 Operations」中已具備對應的 API 服務可供直接調用？<br>
            • 針對高頻查詢部分，若未來透過夜間批次先將 AXDB 所需的唯讀視圖（Read-Only View）鏡像至地端暫存庫，解除直接對 AXDB 的連線依賴，這樣的架構調整是否符合團隊對資料即時性的預期？
          </p>
        </div>

        <div class="prescription-card" style="border-left: 4px solid #8b5cf6;">
          <div class="prescription-header">
            <span class="prescription-title" style="color: #8b5cf6;">4. 13 項核心排程之運作觀測與維運儀表體驗</span>
            <span class="tag tag-purple">維運觀測性</span>
          </div>
          <p style="margin-bottom: 10px; color: var(--text-muted);">
            <strong>【現況背景】</strong> SendNotification.bat 具備 5 分鐘高頻輪詢機制，且夜間 23:01 起有密集的顏色、物料主檔同步排程，是維持集團營運神經中樞的功臣。
          </p>
          <p style="background: rgba(139, 92, 246, 0.08); padding: 12px 16px; border-radius: 6px; line-height: 1.6;">
            <strong>【想請教 Duke】</strong><br>
            • 目前這些排程若在半夜遇到網路逾時或執行例外，內部現行的監控機制是透過文字 Log 巡檢，還是已串接特定的通訊軟體 / 郵件告警？<br>
            • 未來若規劃一個輕量、視覺化的地端任務儀表板（可直接線上查看各排程心跳狀態、執行成功率與一鍵手動補跑），您與團隊在維運習慣上，最希望在儀表板首頁看到哪些即時指標？
          </p>
        </div>

        <div class="prescription-card" style="border-left: 4px solid #ec4899;">
          <div class="prescription-header">
            <span class="prescription-title" style="color: #ec4899;">5. CQS 品質微服務 (.NET 8) 現代化架構經驗借鏡</span>
            <span class="tag tag-red">微服務現代化</span>
          </div>
          <p style="margin-bottom: 10px; color: var(--text-muted);">
            <strong>【現況背景】</strong> CQS 已成功建構於 .NET 8 現代化微服務框架上，並由 IIS ARR（8012 轉發至 8011）負責負載調度，架構十分先進！
          </p>
          <p style="background: rgba(236, 72, 153, 0.08); padding: 12px 16px; border-radius: 6px; line-height: 1.6;">
            <strong>【想請教 Duke】</strong><br>
            • CQS 的升級經驗非常適合作為其他系統現代化的示範標竿！想請教目前 IIS ARR 在實際承載高頻品質審核請求時的效能與記憶體表現如何？<br>
            • 正式機環境上的 Swagger 頁面，團隊目前是否有預定的排程做內部權限隔離，或是未來可直接收納至統一的開發者門戶中統一管理？
          </p>
        </div>

        <div style="margin-top: 20px; text-align: right; font-size: 14px; color: var(--text-muted);">
          ※ 再次感謝 Duke 與研發團隊的扎實梳理，以上問題旨在協助後續架構對齊時能最大程度保護現有程式碼、零衝擊產線營運，期待與 Duke 共同推進計畫！
        </div>
      </div>
    </div>
"""

# 在 tab-prescription 結束後插入
tab_presc_end = report_html.find('</div>\n    </div>\n\n  </main>')
if tab_presc_end != -1:
    report_html = report_html[:tab_presc_end+11] + '\n' + tab_duke_content + report_html[tab_presc_end+11:]
else:
    report_html = report_html.replace('</main>', tab_duke_content + '\n</main>')

# 注入 JS 複製功能
report_js_copy = """
    function copyDukeLetterReport() {
      navigator.clipboard.writeText(`Duke 您好，辛苦了！\\n\\n非常感謝您在 11/12 如此高效率且條理分明地盤點並交付了集團核心的 API List 與 RD_SAMPLE-v0-1 完整規格！這份技術資產梳理得非常清晰，不僅將複雜的跨系統介面（21 條拓撲）與 13 項核心排程完整透明化，更為我們推進周副總主持的「2027 蜂巢計畫（Project Hive）」奠定了極為扎實、可靠的工程基石。\\n\\n為了協助團隊在後續落地「在地端 48~72 小時斷網自律運轉」與「0 元開源平替架構」時更加平穩順暢，並最大程度降低對您與開發團隊日常維運的負擔，我們在深入研讀這兩份寶貴資料後，整理出以下 5 個面向的協同確認與探討點。想請教並聆聽您的實務經驗與建議：\\n\\n1. D365 C# 外掛 API 的邊界防護與 Gateway 平滑收攏\\n現況背景：\\n清冊中清楚標記了主機 192.168.0.95 上的 Report API（:8085 / :8082）與 Local API（:80 / :8081），主要供各系統取得報表下載 URL 與成衣業務資料（馬克、PCT、WIP 等），目前採取內部信任（無驗證）模式。\\n想請教 Duke：\\n目前呼叫這兩組 API 的主要來源端（如 RD_SAMPLE 站台、現場特定工作站或批次程式），在底層網路上是否已有既定的 IP 白名單或網段限制？\\n未來若由在地端輕量 API Gateway（如開源 YARP）在前端統籌掛載 JWT/Token 鑑權做為資安防護閘道，現有呼叫端在配合改帶 Authorization Header 方面，哪一種推進節奏對團隊來說最為平穩（例如：維持既有端口不變、由 Gateway 對外開新路由並設置平行過渡期）？\\n\\n2. 跨國專線同步與廠區「48～72 小時斷網自律」落地銜接\\n現況背景：\\nSync_RSV.bat 與 Sync_RSG.bat 每 30 分鐘透過 DYXnet 專線直連越柬廠區 SQL Server（1433）同步工單與日報資料，維繫了跨國打樣與生產節奏。\\n想請教 Duke：\\n依據過往經驗，當遇上海纜檢修或跨國專線瞬斷時，海外廠端若無法即時回寫，目前同仁的排解方式主要依賴重跑排程，或是有人工批次對齊的機制？是否有遇過主鍵衝突或時間戳鎖定需要手動處理的情形？\\n若我們在廠區邊緣端（Local Edge）導入離線暫存隊列，讓越南與柬埔寨在海纜斷線時仍可自律開單、打樣與填報達 72 小時，待專線復原後全自動非同步對齊，生管與打樣現場最核心、最不能中斷的關鍵欄位會建議優先鎖定哪些？\\n\\n3. RD_SAMPLE 資料庫存取與 AXDB 正式庫連線收斂\\n現況背景：\\nRD_SAMPLE 內部包含 1,490 處存取 SAM 資料庫的 SQL，並有 23 處跨庫直連 AXDB 營運主庫（192.168.0.131）進行資料讀取。\\n想請教 Duke：\\n這 23 處直讀 AXDB 的查詢需求（例如料號基本檔、訂單狀態），是否有部分在您梳理的「D365 C# 80 Operations」中已具備對應的 API 服務可供直接調用？\\n針對高頻查詢部分，若未來透過夜間批次先將 AXDB 所需的唯讀視圖（Read-Only View）鏡像至地端暫存庫，解除直接對 AXDB 的連線依賴，這樣的架構調整是否符合團隊對資料即時性的預期？\\n\\n4. 13 項核心排程之運作觀測與維運儀表體驗\\n現況背景：\\nSendNotification.bat 具備 5 分鐘高頻輪詢機制，且夜間 23:01 起有密集的顏色、物料主檔同步排程，是維持集團營運神經中樞的功臣。\\n想請教 Duke：\\n目前這些排程若在半夜遇到網路逾時或執行例外，內部現行的監控機制是透過文字 Log 巡檢，還是已串接特定的通訊軟體 / 郵件告警？\\n未來若規劃一個輕量、視覺化的地端任務儀表板（可直接線上查看各排程心跳狀態、執行成功率與一鍵手動補跑），您與團隊在維運習慣上，最希望在儀表板首頁看到哪些即時指標？\\n\\n5. CQS 品質微服務 (.NET 8) 現代化架構經驗借鏡\\n現況背景：\\nCQS 已成功建構於 .NET 8 現代化微服務框架上，並由 IIS ARR（8012 轉發至 8011）負責負載調度，架構十分先進！\\n想請教 Duke：\\nCQS 的升級經驗非常適 coal 作為其他系統現代化的示範標竿！想請教目前 IIS ARR 在實際承載高頻品質審核請求時的效能與記憶體表現如何？\\n正式機環境上的 Swagger 頁面，團隊目前是否有預定的排程做內部權限隔離，或是未來可直接收納至統一的開發者門戶中統一管理？\\n\\n再次感謝 Duke 與研發團隊的扎實梳理，以上問題旨在協助後續架構對齊時能最大程度保護現有程式碼、零衝擊產線營運，期待與 Duke 共同推進計畫！`).then(() => {
        alert('✓ 信函內容已成功複製到剪貼簿！');
      });
    }
"""

report_html = report_html.replace('</script>', report_js_copy + '\n</script>')

with open('/Users/howard/Desktop/HermesAgent/PortFilio/RSI/duke_api_evaluation_report.html', 'w', encoding='utf-8') as f:
    f.write(report_html)

print("[SUCCESS] Updated duke_api_evaluation_report.html with Tab 6 Duke questions!")
