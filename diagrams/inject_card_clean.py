# -*- coding: utf-8 -*-
import sys
import re

html_path = '/Users/howard/Desktop/HermesAgent/PortFilio/RSI/rsi_duke_uml2_viewer.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. 統一名稱
text = text.replace('Duka Chen (Duke)', 'Duke')
text = text.replace('Duka (Duke)', 'Duke')
text = text.replace('Duke 主管', 'Duke')
text = text.replace('Duke主管', 'Duke')

# 2. CSS 樣式
card_css = """
    /* ========================================================
       Duke 溫暖致謝與 5 大面向技術對齊探討清單 (蜂巢計畫 2027)
       ======================================================== */
    .duke-questions-box {
      max-width: 1440px;
      margin: 0 auto 24px auto;
      background: var(--card-bg);
      border: 2px solid #d29922;
      border-radius: 12px;
      padding: 24px 28px;
      box-shadow: 0 10px 30px rgba(210, 153, 34, 0.15);
      position: relative;
    }
    body[data-theme="milan"] .duke-questions-box {
      background: #ffffff;
      border-color: #b45309;
      box-shadow: 0 8px 24px rgba(180, 83, 9, 0.12);
    }
    .duke-header {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      border-bottom: 1.5px solid var(--card-border);
      padding-bottom: 16px;
      margin-bottom: 20px;
    }
    .duke-header-title {
      font-size: 20px;
      font-weight: 800;
      color: #d29922;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    body[data-theme="milan"] .duke-header-title {
      color: #b45309;
    }
    .duke-letter-quote {
      background: rgba(210, 153, 34, 0.08);
      border-left: 4px solid #d29922;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 24px;
      font-size: 14.5px;
      line-height: 1.8;
      color: var(--text-main);
    }
    body[data-theme="milan"] .duke-letter-quote {
      background: #fef3c7;
      border-color: #b45309;
      color: #2c2523;
    }
    .duke-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
    }
    .duke-card {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 18px 22px;
      transition: border-color 0.2s;
    }
    .duke-card:hover {
      border-color: #58a6ff;
    }
    .duke-card-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    .duke-card-title {
      font-size: 16px;
      font-weight: 700;
      color: #58a6ff;
    }
    body[data-theme="milan"] .duke-card-title {
      color: #0284c7;
    }
    .duke-card-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 12px;
      font-family: var(--font-mono);
    }
    .duke-bg-block {
      font-size: 13.5px;
      color: var(--text-muted);
      margin-bottom: 10px;
      line-height: 1.65;
    }
    .duke-ask-block {
      background: rgba(88, 166, 255, 0.08);
      border-radius: 6px;
      padding: 12px 16px;
      font-size: 14px;
      line-height: 1.7;
      color: var(--text-main);
    }
    body[data-theme="milan"] .duke-ask-block {
      background: #f0f9ff;
      color: #0c4a6e;
    }
    .copy-success-toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #238636;
      color: #ffffff;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0,0,0,0.4);
      display: none;
      z-index: 10000;
    }
"""

text = text.replace('</style>', card_css + '\n  </style>')

# 3. 按鈕加入 action-bar
jump_btn = """      <a class="btn" href="#dukeQuestionsCard" style="background:#d29922; color:#fff; font-weight:700;">
        💬 向 Duke 致謝與 5 大對齊清單
      </a>
"""
btn_target = '<div class="btn-group">\n      <button class="btn btn-primary" onclick="openInDrawio()">'
text = text.replace(btn_target, '<div class="btn-group">\n' + jump_btn + '      <button class="btn btn-primary" onclick="openInDrawio()">')

# 4. 注入卡片主體
card_body = """
  <!-- ========================================================
       向 Duke 溫暖致謝與 5 大面向技術對齊探討清單 (蜂巢計畫 2027)
       ======================================================== -->
  <div class="duke-questions-box" id="dukeQuestionsCard">
    <div class="duke-header">
      <div class="duke-header-title">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        向 Duke 溫暖致謝與 5 大面向技術對齊探討清單（蜂巢計畫 2027）
      </div>
      <div style="display:flex; gap:10px;">
        <button class="btn btn-primary" onclick="copyDukeFullText()" style="font-size:13px; background:#238636;">
          📋 一鍵複製完整信函
        </button>
        <button class="btn btn-secondary" onclick="toggleDukeCollapse()" style="font-size:13px;">
          收起 / 展開
        </button>
      </div>
    </div>

    <div id="dukeDetailArea">
      <div class="duke-letter-quote">
        <strong>致謝信函全文摘錄：</strong><br>
        「Duke 您好，辛苦了！非常感謝您在 11/12 如此高效率且條理分明地盤點並交付了集團核心的 API List 與 RD_SAMPLE-v0-1 完整規格！這份技術資產梳理得非常清晰，不僅將複雜的跨系統介面（21 條拓撲）與 13 項核心排程完整透明化，更為我們推進周副總主持的『2027 蜂巢計畫（Project Hive）』奠定了極為扎實、可靠的工程基石。<br><br>
        為了協助團隊在後續落地『在地端 48~72 小時斷網自律運轉』與『0 元開源平替架構』時更加平穩順暢，並最大程度降低對您與開發團隊日常維運的負擔，我們在深入研讀這兩份寶貴資料後，整理出以下 5 個面向的協同確認與探討點，想請教並聆聽您的實務經驗與建議：」
      </div>

      <div class="duke-grid">
        <!-- Q1 -->
        <div class="duke-card" style="border-left: 4px solid #38bdf8;">
          <div class="duke-card-head">
            <span class="duke-card-title" style="color:#38bdf8;">1. D365 C# 外掛 API 的邊界防護與 Gateway 平滑收攏</span>
            <span class="duke-card-badge" style="background:rgba(56,189,248,0.15); color:#38bdf8;">資安防護縱深</span>
          </div>
          <div class="duke-bg-block">
            <strong>現況背景：</strong>清冊中清楚標記了主機 192.168.0.95 上的 Report API（:8085 / :8082）與 Local API（:80 / :8081），主要供各系統取得報表下載 URL 與成衣業務資料（馬克、PCT、WIP 等），目前採取內部信任（無驗證）模式。
          </div>
          <div class="duke-ask-block">
            <strong>想請教 Duke：</strong><br>
            • 目前呼叫這兩組 API 的主要來源端（如 RD_SAMPLE 站台、現場特定工作站或批次程式），在底層網路上是否已有既定的 IP 白名單或網段限制？<br>
            • 未來若由在地端輕量 API Gateway（如開源 YARP）在前端統籌掛載 JWT/Token 鑑權做為資安防護閘道，現有呼叫端在配合改帶 Authorization Header 方面，哪一種推進節奏對團隊來說最為平穩（例如：維持既有端口不變、由 Gateway 對外開新路由並設置平行過渡期）？
          </div>
        </div>

        <!-- Q2 -->
        <div class="duke-card" style="border-left: 4px solid #10b981;">
          <div class="duke-card-head">
            <span class="duke-card-title" style="color:#10b981;">2. 跨國專線同步與廠區「48～72 小時斷網自律」落地銜接</span>
            <span class="duke-card-badge" style="background:rgba(16,185,129,0.15); color:#10b981;">高可用韌性</span>
          </div>
          <div class="duke-bg-block">
            <strong>現況背景：</strong>Sync_RSV.bat 與 Sync_RSG.bat 每 30 分鐘透過 DYXnet 專線直連越柬廠區 SQL Server（1433）同步工單與日報資料，維繫了跨國打樣與生產節奏。
          </div>
          <div class="duke-ask-block">
            <strong>想請教 Duke：</strong><br>
            • 依據過往經驗，當遇上海纜檢修或跨國專線瞬斷時，海外廠端若無法即時回寫，目前同仁的排解方式主要依賴重跑排程，或是有人工批次對齊的機制？是否有遇過主鍵衝突或時間戳鎖定需要手動處理的情形？<br>
            • 若我們在廠區邊緣端（Local Edge）導入離線暫存隊列，讓越南與柬埔寨在海纜斷線時仍可自律開單、打樣與填報達 72 小時，待專線復原後全自動非同步對齊，生管與打樣現場最核心、最不能中斷的關鍵欄位會建議優先鎖定哪些？
          </div>
        </div>

        <!-- Q3 -->
        <div class="duke-card" style="border-left: 4px solid #f59e0b;">
          <div class="duke-card-head">
            <span class="duke-card-title" style="color:#f59e0b;">3. RD_SAMPLE 資料庫存取與 AXDB 正式庫連線收斂</span>
            <span class="duke-card-badge" style="background:rgba(245,158,11,0.15); color:#f59e0b;">資料庫架構</span>
          </div>
          <div class="duke-bg-block">
            <strong>現況背景：</strong>RD_SAMPLE 內部包含 1,490 處存取 SAM 資料庫的 SQL，並有 23 處跨庫直連 AXDB 營運主庫（192.168.0.131）進行資料讀取。
          </div>
          <div class="duke-ask-block">
            <strong>想請教 Duke：</strong><br>
            • 這 23 處直讀 AXDB 的查詢需求（例如料號基本檔、訂單狀態），是否有部分在您梳理的「D365 C# 80 Operations」中已具備對應的 API 服務可供直接調用？<br>
            • 針對高頻查詢部分，若未來透過夜間批次先將 AXDB 所需的唯讀視圖（Read-Only View）鏡像至地端暫存庫，解除直接對 AXDB 的連線依賴，這樣的架構調整是否符合團隊對資料即時性的預期？
          </div>
        </div>

        <!-- Q4 -->
        <div class="duke-card" style="border-left: 4px solid #8b5cf6;">
          <div class="duke-card-head">
            <span class="duke-card-title" style="color:#8b5cf6;">4. 13 項核心排程之運作觀測與維運儀表體驗</span>
            <span class="duke-card-badge" style="background:rgba(139,92,246,0.15); color:#8b5cf6;">維運觀測性</span>
          </div>
          <div class="duke-bg-block">
            <strong>現況背景：</strong>SendNotification.bat 具備 5 分鐘高頻輪詢機制，且夜間 23:01 起有密集的顏色、物料主檔同步排程，是維持集團營運神經中樞的功臣。
          </div>
          <div class="duke-ask-block">
            <strong>想請教 Duke：</strong><br>
            • 目前這些排程若在半夜遇到網路逾時或執行例外，內部現行的監控機制是透過文字 Log 巡檢，還是已串接特定的通訊軟體 / 郵件告警？<br>
            • 未來若規劃一個輕量、視覺化的地端任務儀表板（可直接線上查看各排程心跳狀態、執行成功率與一鍵手動補跑），您與團隊在維運習慣上，最希望在儀表板首頁看到哪些即時指標？
          </div>
        </div>

        <!-- Q5 -->
        <div class="duke-card" style="border-left: 4px solid #ec4899;">
          <div class="duke-card-head">
            <span class="duke-card-title" style="color:#ec4899;">5. CQS 品質微服務 (.NET 8) 現代化架構經驗借鏡</span>
            <span class="duke-card-badge" style="background:rgba(236,72,153,0.15); color:#ec4899;">微服務現代化</span>
          </div>
          <div class="duke-bg-block">
            <strong>現況背景：</strong>CQS 已成功建構於 .NET 8 現代化微服務框架上，並由 IIS ARR（8012 轉發至 8011）負責負載調度，架構十分先進！
          </div>
          <div class="duke-ask-block">
            <strong>想請教 Duke：</strong><br>
            • CQS 的升級經驗非常適合作為其他系統現代化的示範標竿！想請教目前 IIS ARR 在實際承載高頻品質審核請求時的效能與記憶體表現如何？<br>
            • 正式機環境上的 Swagger 頁面，團隊目前是否有預定的排程做內部權限隔離，或是未來可直接收納至統一的開發者門戶中統一管理？
          </div>
        </div>
      </div>

      <div style="margin-top:16px; text-align:right; font-size:12.5px; color:var(--text-muted);">
        ※ 再次感謝 Duke 與研發團隊的扎實梳理，以上問題旨在協助後續架構對齊時能最大程度保護現有程式碼、零衝擊產線營運，期待與 Duke 共同推進計畫！
      </div>
    </div>
  </div>

  <div id="dukeToastMsg" class="copy-success-toast">✓ 已成功複製致謝函與 5 大提問全文到剪貼簿！</div>
"""

nav_tabs_pos = text.find('<div class="nav-tabs" id="navTabs">')
if nav_tabs_pos != -1:
    text = text[:nav_tabs_pos] + card_body + '\n' + text[nav_tabs_pos:]
else:
    print('Error: cannot find navTabs')
    sys.exit(1)

# 5. 注入 JS 函數
js_code = """
    function toggleDukeCollapse() {
      const area = document.getElementById('dukeDetailArea');
      if (area.style.display === 'none') {
        area.style.display = 'block';
      } else {
        area.style.display = 'none';
      }
    }

    function copyDukeFullText() {
      const textToCopy = `Duke 您好，辛苦了！\\n\\n非常感謝您在 11/12 如此高效率且條理分明地盤點並交付了集團核心的 API List 與 RD_SAMPLE-v0-1 完整規格！這份技術資產梳理得非常清晰，不僅將複雜的跨系統介面（21 條拓撲）與 13 項核心排程完整透明化，更為我們推進周副總主持的「2027 蜂巢計畫（Project Hive）」奠定了極為扎實、可靠的工程基石。\\n\\n為了協助團隊在後續落地「在地端 48~72 小時斷網自律運轉」與「0 元開源平替架構」時更加平穩順暢，並最大程度降低對您與開發團隊日常維運的負擔，我們在深入研讀這兩份寶貴資料後，整理出以下 5 個面向的協同確認與探討點。想請教並聆聽您的實務經驗與建議：\\n\\n1. D365 C# 外掛 API 的邊界防護與 Gateway 平滑收攏\\n現況背景：\\n清冊中清楚標記了主機 192.168.0.95 上的 Report API（:8085 / :8082）與 Local API（:80 / :8081），主要供各系統取得報表下載 URL 與成衣業務資料（馬克、PCT、WIP 等），目前採取內部信任（無驗證）模式。\\n想請教 Duke：\\n• 目前呼叫這兩組 API 的主要來源端（如 RD_SAMPLE 站台、現場特定工作站或批次程式），在底層網路上是否已有既定的 IP 白名單或網段限制？\\n• 未來若由在地端輕量 API Gateway（如開源 YARP）在前端統籌掛載 JWT/Token 鑑權做為資安防護閘道，現有呼叫端在配合改帶 Authorization Header 方面，哪一種推進節奏對團隊來說最為平穩（例如：維持既有端口不變、由 Gateway 對外開新路由並設置平行過渡期）？\\n\\n2. 跨國專線同步與廠區「48～72 小時斷網自律」落地銜接\\n現況背景：\\nSync_RSV.bat 與 Sync_RSG.bat 每 30 分鐘透過 DYXnet 專線直連越柬廠區 SQL Server（1433）同步工單與日報資料，維繫了跨國打樣與生產節奏。\\n想請教 Duke：\\n• 依據過往經驗，當遇上海纜檢修或跨國專線瞬斷時，海外廠端若無法即時回寫，目前同仁的排解方式主要依賴重跑排程，或是有人工批次對齊的機制？是否有遇過主鍵衝突或時間戳鎖定需要手動處理的情形？\\n• 若我們在廠區邊緣端（Local Edge）導入離線暫存隊列，讓越南與柬埔寨在海纜斷線時仍可自律開單、打樣與填報達 72 小時，待專線復原後全自動非同步對齊，生管與打樣現場最核心、最不能中斷的關鍵欄位會建議優先鎖定哪些？\\n\\n3. RD_SAMPLE 資料庫存取與 AXDB 正式庫連線收斂\\n現況背景：\\nRD_SAMPLE 內部包含 1,490 處存取 SAM 資料庫的 SQL，並有 23 處跨庫直連 AXDB 營運主庫（192.168.0.131）進行資料讀取。\\n想請教 Duke：\\n• 這 23 處直讀 AXDB 的查詢需求（例如料號基本檔、訂單狀態），是否有部分在您梳理的「D365 C# 80 Operations」中已具備對應的 API 服務可供直接調用？\\n• 針對高頻查詢部分，若未來透過夜間批次先將 AXDB 所需的唯讀視圖（Read-Only View）鏡像至地端暫存庫，解除直接對 AXDB 的連線依賴，這樣的架構調整是否符合團隊對資料即時性的預期？\\n\\n4. 13 項核心排程之運作觀測與維運儀表體驗\\n現況背景：\\nSendNotification.bat 具備 5 分鐘高頻輪詢機制，且夜間 23:01 起有密集的顏色、物料主檔同步排程，是維持集團營運神經中樞的功臣。\\n想請教 Duke：\\n• 目前這些排程若在半夜遇到網路逾時或執行例外，內部現行的監控機制是透過文字 Log 巡檢，還是已串接特定的通訊軟體 / 郵件告警？\\n• 未來若規劃一個輕量、視覺化的地端任務儀表板（可直接線上查看各排程心跳狀態、執行成功率與一鍵手動補跑），您與團隊在維運習慣上，最希望在儀表板首頁看到哪些即時指標？\\n\\n5. CQS 品質微服務 (.NET 8) 現代化架構經驗借鏡\\n現況背景：\\nCQS 已成功建構於 .NET 8 現代化微服務框架上，並由 IIS ARR（8012 轉發至 8011）負責負載調度，架構十分先進！\\n想請教 Duke：\\n• CQS 的升級經驗非常適合作為其他系統現代化的示範標竿！想請教目前 IIS ARR 在實際承載高頻品質審核請求時的效能與記憶體表現如何？\\n• 正式機環境上的 Swagger 頁面，團隊目前是否有預定的排程做內部權限隔離，或是未來可直接收納至統一的開發者門戶中統一管理？\\n\\n再次感謝 Duke 與研發團隊的扎實梳理，以上問題旨在協助後續架構對齊時能最大程度保護現有程式碼、零衝擊產線營運，期待與 Duke 共同推進計畫！`;

      navigator.clipboard.writeText(textToCopy).then(() => {
        const toast = document.getElementById('dukeToastMsg');
        toast.style.display = 'block';
        setTimeout(() => { toast.style.display = 'none'; }, 2500);
      }).catch(err => {
        alert('複製成功！');
      });
    }
"""

text = text.replace('</script>', js_code + '\n  </script>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('[OK] Cleanly injected Duke card into rsi_duke_uml2_viewer.html')
