#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成信源全球 2027 蜂巢計畫 UML 2 全量架構圖資線上檢視入口
檔案：rsi_duke_uml2_viewer.html
"""

import os
import html
import json

def generate_viewer_html():
    base_dir = "/Users/howard/Desktop/HermesAgent/PortFilio/RSI"
    drawio_file = os.path.join(base_dir, "RSI_DUKE_UML2_ALL_DIAGRAMS.drawio")
    with open(drawio_file, "r", encoding="utf-8") as f:
        drawio_xml_content = f.read()

    # Pre-escape drawio XML for embedding into JS string
    json_drawio_xml = json.dumps(drawio_xml_content)

    html_code = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>信源全球 (RSI) 2027 蜂巢計畫 | UML 2.0 全套架構圖資 (Duke規格依據)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Noto+Sans+TC:wght@300;400;500;700;900&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0d1117;
      --card-bg: #161b22;
      --card-border: #30363d;
      --text-main: #f0f6fc;
      --text-muted: #8b949e;
      --accent: #58a6ff;
      --accent-glow: rgba(88, 166, 255, 0.2);
      --amber: #d29922;
      --amber-bg: rgba(210, 153, 34, 0.1);
      --green: #3fb950;
      --green-bg: rgba(63, 185, 80, 0.1);
      --purple: #bc8cff;
      --purple-bg: rgba(188, 140, 255, 0.1);
      --red: #f85149;
      --red-bg: rgba(248, 81, 73, 0.1);
      --font-sans: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    body[data-theme="milan"] {{
      --bg: #fbf9f5;
      --card-bg: #ffffff;
      --card-border: #e6dfd5;
      --text-main: #2c2523;
      --text-muted: #786c66;
      --accent: #b45309;
      --accent-glow: rgba(180, 83, 9, 0.15);
      --amber: #b45309;
      --amber-bg: #fef3c7;
      --green: #15803d;
      --green-bg: #dcfce7;
      --purple: #6b21a8;
      --purple-bg: #f3e8ff;
      --red: #b91c1c;
      --red-bg: #fee2e2;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: var(--bg);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      padding: 24px 32px;
      transition: background 0.25s ease, color 0.25s ease;
    }}

    .header-container {{
      max-width: 1440px;
      margin: 0 auto 24px auto;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 24px 32px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    }}

    .meta-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 12px;
    }}

    .tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      font-family: var(--font-mono);
      letter-spacing: 0.5px;
    }}

    .tag-blue {{ background: var(--accent-glow); color: var(--accent); border: 1px solid var(--accent); }}
    .tag-amber {{ background: var(--amber-bg); color: var(--amber); border: 1px solid var(--amber); }}
    .tag-purple {{ background: var(--purple-bg); color: var(--purple); border: 1px solid var(--purple); }}
    .tag-green {{ background: var(--green-bg); color: var(--green); border: 1px solid var(--green); }}
    .tag-red {{ background: var(--red-bg); color: var(--red); border: 1px solid var(--red); }}

    h1 {{
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: 14px;
      margin-bottom: 18px;
    }}

    .role-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
      padding-top: 14px;
      border-top: 1px solid var(--card-border);
    }}

    .role-card {{
      background: rgba(255,255,255,0.02);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .role-title {{
      font-size: 11px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }}

    .role-name {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
    }}

    .role-desc {{
      font-size: 11px;
      color: var(--text-muted);
    }}

    /* Action bar */
    .action-bar {{
      max-width: 1440px;
      margin: 0 auto 20px auto;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}

    .btn-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
      border: 1px solid transparent;
      font-family: var(--font-sans);
    }}

    .btn-primary {{
      background: #238636;
      color: #fff;
    }}
    .btn-primary:hover {{
      background: #2ea043;
    }}

    .btn-secondary {{
      background: var(--card-bg);
      border-color: var(--card-border);
      color: var(--text-main);
    }}
    .btn-secondary:hover {{
      border-color: var(--accent);
      color: var(--accent);
    }}

    .btn-amber {{
      background: var(--amber);
      color: #fff;
    }}
    .btn-amber:hover {{
      opacity: 0.9;
    }}

    /* Diagram Nav Tabs */
    .nav-tabs {{
      max-width: 1440px;
      margin: 0 auto 20px auto;
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      padding: 8px;
      border-radius: 10px;
    }}

    .nav-tab {{
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      border: 1px solid transparent;
      background: transparent;
      transition: all 0.15s ease;
      white-space: nowrap;
      font-family: var(--font-mono);
    }}

    .nav-tab:hover {{
      color: var(--text-main);
      background: rgba(255,255,255,0.04);
    }}

    .nav-tab.active {{
      color: var(--accent);
      background: var(--accent-glow);
      border-color: var(--accent);
    }}

    /* Main Diagram Container */
    .viewer-main {{
      max-width: 1440px;
      margin: 0 auto 30px auto;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 24px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }}

    .diagram-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--card-border);
    }}

    .diagram-title {{
      font-size: 20px;
      font-weight: 700;
    }}

    .diagram-badge {{
      font-size: 11px;
      font-family: var(--font-mono);
      padding: 4px 10px;
      border-radius: 12px;
      background: var(--purple-bg);
      color: var(--purple);
      border: 1px solid var(--purple);
    }}

    .diagram-frame {{
      width: 100%;
      min-height: 640px;
      background: #ffffff;
      border-radius: 8px;
      border: 1px solid var(--card-border);
      overflow: auto;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }}

    .diagram-desc {{
      margin-top: 18px;
      padding: 16px;
      border-radius: 8px;
      background: rgba(255,255,255,0.02);
      border: 1px solid var(--card-border);
      font-size: 13px;
      color: var(--text-muted);
    }}

    .diagram-desc strong {{
      color: var(--text-main);
    }}

    /* Spec section */
    .spec-section {{
      max-width: 1440px;
      margin: 40px auto;
    }}

    .section-title {{
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .spec-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 16px;
    }}

    .spec-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 16px;
    }}

    .spec-card h3 {{
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 8px;
      color: var(--accent);
    }}

    .spec-card ul {{
      padding-left: 20px;
      font-size: 12px;
      color: var(--text-muted);
    }}

    .spec-card li {{
      margin-bottom: 4px;
    }}

    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #238636;
      color: #fff;
      padding: 12px 20px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      display: none;
      z-index: 1000;
    }}

    svg {{
      max-width: 100%;
      height: auto;
    }}
  </style>
</head>
<body data-theme="dark">

  <div class="header-container">
    <div class="meta-tags">
      <span class="tag tag-blue">信源全球 (RSI) 2027 蜂巢計畫</span>
      <span class="tag tag-amber">依據 Duke 2026-11-12 真實交付規格</span>
      <span class="tag tag-purple">D365 C# 服務體系</span>
      <span class="tag tag-green">UML 2.0 完整 14 張圖資</span>
      <span class="tag tag-red">0 元開源平替 & 在地自律運轉</span>
    </div>

    <h1>信源全球 2027 蜂巢計畫 (Project Hive) UML 2.0 架構總覽圖冊</h1>
    <div class="subtitle">
      依據 Duka (Duke) 主管交付之真實 API List (三章 26 服務) 與 RD_SAMPLE-v0-1 示範範本 (21 條拓撲、1,490 處直接 SQL、13 項排程)，遵循 D365 C# 服務定義，產出符合 ISO/IEC 19505 之 UML 2.0 全量架構圖資。
    </div>

    <div class="role-grid">
      <div class="role-card">
        <span class="role-title">計劃主持人</span>
        <span class="role-name">周文津 副總</span>
        <span class="role-desc">全球資訊戰略方針、在地自律運轉與 0 授權費架構核定</span>
      </div>
      <div class="role-card">
        <span class="role-title">執行負責人</span>
        <span class="role-name">Howard Liao Ph.D.</span>
        <span class="role-desc">外部資訊顧問 ｜ UML 2 架構設計、API 治理與處方驗證實施</span>
      </div>
      <div class="role-card">
        <span class="role-title">記錄整理</span>
        <span class="role-name">Duka Chen (Duke) 主管</span>
        <span class="role-desc">研發資訊主管 ｜ 交付 RD_SAMPLE-v0-1 與集團真實 API 清單</span>
      </div>
    </div>
  </div>

  <div class="action-bar">
    <div class="btn-group">
      <button class="btn btn-primary" onclick="openInDrawio()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
        在 draw.io 線上編輯 / 查看 (.drawio)
      </button>

      <a class="btn btn-secondary" href="RSI_DUKE_UML2_ALL_DIAGRAMS.drawio" download="RSI_DUKE_UML2_ALL_DIAGRAMS.drawio">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        下載 .drawio 原始檔 (多頁原生檔)
      </a>

      <button class="btn btn-secondary" onclick="copyDrawioXml()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
        複製 draw.io XML 碼
      </button>

      <a class="btn btn-amber" href="duke_api_evaluation_report.html" target="_blank">
        檢視高階主管評估報告 HTML
      </a>
    </div>

    <div class="btn-group">
      <button class="btn btn-secondary" onclick="toggleTheme()">切換主題 (米蘭暖琥珀 / 曜石深黑)</button>
    </div>
  </div>

  <!-- Tab selector -->
  <div class="nav-tabs" id="navTabs">
    <!-- Populated by JS -->
  </div>

  <!-- Viewer -->
  <div class="viewer-main">
    <div class="diagram-header">
      <div>
        <div class="diagram-title" id="diagTitle">01. Class Diagram (類別圖)</div>
        <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;" id="diagSub">結構型圖資 Structure Diagram</div>
      </div>
      <div class="diagram-badge" id="diagBadge">ISO/IEC 19505 標準</div>
    </div>

    <div class="diagram-frame" id="diagramFrame">
      <!-- SVG rendering container -->
    </div>

    <div class="diagram-desc" id="diagDesc">
      <!-- Description updated dynamically -->
    </div>
  </div>

  <!-- Detailed Spec Breakdown according to Duke's deliverable -->
  <div class="spec-section">
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
      Duke 交付之關鍵架構與介面規範總成 (作為 UML 2 圖資之唯一標準)
    </div>

    <div class="spec-grid">
      <div class="spec-card">
        <h3>1. D365 C# 服務體系</h3>
        <ul>
          <li><strong>D365 C# 外掛 API:</strong> 運行於 <code>192.168.0.95</code> (.NET 4.8 / Web API 2)，包含 Report API (:8085 正式/:8082 UAT) 與 Local API (:80 正式/:8081 UAT)。</li>
          <li><strong>全無驗證風險:</strong> 外掛 API 完全無 Token/身份驗證，僅需提供參數即可下載 PDF/Excel，須透過 API Gateway 收攏。</li>
          <li><strong>D365 C# 80 Operations:</strong> 涵蓋 JCOM_WebServices、RSI_WebServices 等 31 個服務，採 Entra ID Bearer Token 授權，回傳統一結構 <code>RSI_RT&lt;T&gt;</code>。</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>2. CQS 品質微服務 (.NET 8 ARR)</h3>
        <ul>
          <li><strong>架構演進:</strong> CQS 採用最新 .NET 8 框架，正處於現代化過渡期。</li>
          <li><strong>IIS ARR 轉發:</strong> 正式機 <code>192.168.0.22:8011</code>，測試機 <code>192.168.0.23:8011</code>，由 IIS Application Request Routing (ARR) 在 Port 8012 進行反向代理。</li>
          <li><strong>平替方案:</strong> 建議以開源 YARP / Envoy 替換 Windows ARR，解除微軟專屬授權綁定。</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>3. RD_SAMPLE 示範範本核心問題</h3>
        <ul>
          <li><strong>1,490 處直接下 SQL:</strong> 自寫 ADO.NET 直下 SQL 語句，連線字串內含明碼 sa 帳號，缺乏 ORM 與參數化防護。</li>
          <li><strong>跨庫查詢 AXDB (23 處):</strong> 直連 rsiaxdb1 營運主庫，引發鎖表與效能爭用。</li>
          <li><strong>13 項 Windows 排程依賴:</strong> 包含每 5 分鐘通知輪詢、每 30 分鐘跨國專線 TDS 直寫 (Sync_RSV/RSG) 及每日 23:01 批次主檔同步。</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>4. 四大處方與 48~72 小時在地自律</h3>
        <ul>
          <li><strong>處方 1:</strong> 導入 YARP API Gateway 收攏無驗證外掛與 C# 80 Operations。</li>
          <li><strong>處方 2:</strong> 跨國資料庫直連改為 RabbitMQ 斷網自律離線訊息佇列。</li>
          <li><strong>處方 3:</strong> ADO.NET 重構為 Dapper + 預行編譯 SQL，拔除明碼 sa 帳號。</li>
          <li><strong>處方 4:</strong> Windows Task Scheduler 遷移至 Hangfire / KEDA 在地容器化排程。</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="toast" id="toast">已成功複製 draw.io XML 碼！可在 draw.io 中直接貼上！</div>

  <script>
    const DRAWIO_XML = {json_drawio_xml};

    const diagramsData = [
      {{
        id: "d01_class",
        name: "01. Class Diagram (類別圖)",
        category: "結構型圖 (Structure)",
        desc: "<strong>核心重點：</strong>展示 RD_SAMPLE 領域模型與 D365 C# 服務類別。所有 D365 外掛均繼承自 <code>RqtBaseForm</code> (包含 SalesId, StyleNo, BuyKeys, UserName 等欄位)；D365 C# 自研 80 Operations 回傳統一 <code>RSI_RT&lt;T&gt;</code> (IsValid, Msg, TotalCount, DataList)。同時揭示 DataAccess 類別中 1,490 處直接 SQL SAM 庫與 23 處 SQL AXDB 庫之結構綁定。"
      }},
      {{
        id: "d02_component",
        name: "02. Component Diagram (元件圖)",
        category: "結構型圖 (Structure)",
        desc: "<strong>核心重點：</strong>呈現 RD_Sample.Web、RD_Batch.Console、Python TechPack Parser、D365 C# Integration Services (Report API :8085 / 80 Ops)、CQS (.NET 8 ARR :8012) 以及處方推薦之 YARP Gateway 微服務邊界與依賴關聯。"
      }},
      {{
        id: "d03_deploy",
        name: "03. Deployment Diagram (部署圖)",
        category: "結構型圖 (Structure)",
        desc: "<strong>核心重點：</strong>全實體節點拓撲。正式伺服器 RDSMP2 (192.168.0.22)、測試伺服器 RDSMP1 (192.168.0.23)、D365 外掛主機 RSIMDW1 (192.168.0.95)、D365 核心叢集 (192.168.0.124~126 / 131 AXDB)、海外廠區 RDV (192.168.185.123:1433) 與 RDG (192.168.193.65:1433) 跨國專線直連，以及 AWS 外部推論服務。"
      }},
      {{
        id: "d04_package",
        name: "04. Package Diagram (套件圖)",
        category: "結構型圖 (Structure)",
        desc: "<strong>核心重點：</strong>展示集團軟體分層命名空間：Presentation (.aspx WebForms)、BusinessLogic (SampleOrderManager, SyncOrchestrator)、Core.DataAccess (SqlServerDirectAccessor)、RD_Batch (排程批次)、D365.Services (C# 服務包) 及 Quality.CQS (.NET 8 品管包)。"
      }},
      {{
        id: "d05_object",
        name: "05. Object Diagram (物件圖)",
        category: "結構型圖 (Structure)",
        desc: "<strong>核心重點：</strong>運行時期的真實物件快照實例。包含 activeMo: MoHeader (&#39;MO-202611-0089&#39;)、itemBlackL: MoDetail、exportRqt: RqtBaseForm (由 duka.chen 發起之打樣匯出)、d365Rt: RSI_RT (C# 回應實例) 及 rsvSyncTask: ScheduledTask 排程實例。"
      }},
      {{
        id: "d06_composite",
        name: "06. Composite Structure Diagram (複合結構圖)",
        category: "結構型圖 (Structure)",
        desc: "<strong>核心重點：</strong>展示 RDSMP2 執行環境之內部零件裝配與對外通訊埠 (Ports)：Port 1 (HTTPS 443 供外部瀏覽)、Port 2 (TDS 1433 供資料庫直連)、Port 3 (REST :8085 供 D365 C# 外掛報表介接)。"
      }},
      {{
        id: "d07_profile",
        name: "07. Profile Diagram (輪廓圖)",
        category: "結構型圖 (Structure)",
        desc: "<strong>核心重點：</strong>專為蜂巢計畫量身打造之領域 Stereotypes 定義，擴充自 UML 2 Metaclass：&lt;&lt;CSharpService&gt;&gt; (定義 .NET 版本與 Bearer 驗證)、&lt;&lt;DirectSQL&gt;&gt; (標註直下 SQL 次數與 sa 帳號)、&lt;&lt;CrossBorderRPC&gt;&gt; (標註 DYXnet 專線與斷網容忍度) 與 &lt;&lt;BatchSchedule&gt;&gt; (標註排程頻率)。"
      }},
      {{
        id: "d08_usecase",
        name: "08. Use Case Diagram (使用案例圖)",
        category: "行為型圖 (Behavior)",
        desc: "<strong>核心重點：</strong>總部打樣設計師、海外廠區生管 (RSV/RSG)、Windows 工作排程器與 D365 ERP (C# Services) 之間的業務案例邊界：UC01 建立樣品單、UC02 Python 解析工藝、UC03 跨國專線 30 分鐘同步、UC04 廠區車縫回報、UC05 每日 23:01 物料主檔同步。"
      }},
      {{
        id: "d09_activity",
        name: "09. Activity Diagram (活動圖)",
        category: "行為型圖 (Behavior)",
        desc: "<strong>核心重點：</strong>跨國四泳道協同業務流程 (Swimlanes)：總部研發 (上傳 TechPack -> Python 解析) -> D365 C# ERP (驗證物料與款號) -> Windows 排程 (Sync_RSV.bat 專線推送) -> 廠區生管 (排產車縫 -> CQS 品質檢驗放行)。"
      }},
      {{
        id: "d10_statemachine",
        name: "10. State Machine Diagram (狀態機圖)",
        category: "行為型圖 (Behavior)",
        desc: "<strong>核心重點：</strong>樣品單 (MoNo) 完整生命週期狀態轉移模型：Draft (草稿) -> TechPackParsed (解析入庫) -> SyncedToFactory (專線同步至廠區) -> SewingInProgress (排產車縫中) -> QC_Inspection (品管檢驗) -> SampleApproved (檢驗合格) -> Shipped (報關出貨)。"
      }},
      {{
        id: "d11_sequence",
        name: "11. Sequence Diagram (循序圖)",
        category: "互動型圖 (Interaction)",
        desc: "<strong>核心重點：</strong>精確時序呼叫鏈路：設計師上傳 TechPack -> WebForms 呼叫 Python CLI -> 直寫 SAM 庫 (ADO.NET) -> 呼叫 D365 C# Report API (繼承 RqtBaseForm) -> 回傳下載 URL (無驗證) -> 觸發 Sync_RSV.bat 專線推送至海外廠區。"
      }},
      {{
        id: "d12_comm",
        name: "12. Communication Diagram (溝通圖)",
        category: "互動型圖 (Interaction)",
        desc: "<strong>核心重點：</strong>強調節點間之協同通訊鏈路：RD_Batch.Console 作為中央樞紐，向 SAM 資料庫發送 1.1/1.2 查詢，向 Factory_RSV_DB 發送 1.3 跨國專線 30 分鐘寫入，向 D365 C# Services 發送 1.4 每日 23:01 主檔同步。"
      }},
      {{
        id: "d13_interact",
        name: "13. Interaction Overview Diagram (互動概觀圖)",
        category: "互動型圖 (Interaction)",
        desc: "<strong>核心重點：</strong>以高階活動控制流統整各循序作業片段 (sd)：sd_TechPack_Ingest (提取) -> sd_D365_CSharp_Verify (C# 規格驗證) -> sd_Factory_Sync_Batch (專線排程推送) -> sd_CQS_Quality_Audit (品檢回報) -> sd_Daily_Sewn_Report (每日車縫日報結算)。"
      }},
      {{
        id: "d14_timing",
        name: "14. Timing Diagram (計時圖)",
        category: "互動型圖 (Interaction)",
        desc: "<strong>核心重點：</strong>時間軸與波形分析。SendNotification.bat (每 5 分鐘高頻脈衝)、Sync_RSV/RSG.bat (每 30 分鐘，06:00~23:00 執行，深夜休眠)、ERP 夜間批次 (C#，23:01~23:31 密集批次窗口)，以及海纜斷網事件發生時之 48~72 小時在地自律運轉與復原對齊波形。"
      }}
    ];

    let currentTabIndex = 0;

    function renderTabs() {{
      const navTabs = document.getElementById("navTabs");
      navTabs.innerHTML = diagramsData.map((d, idx) => `
        <button class="nav-tab ${{idx === currentTabIndex ? 'active' : ''}}" onclick="switchTab(${{idx}})">
          ${{d.name.split(' ')[0]}} ${{d.name.split(' ')[1]}}
        </button>
      `).join('');
    }}

    function switchTab(index) {{
      currentTabIndex = index;
      renderTabs();
      updateDiagramView();
    }}

    function updateDiagramView() {{
      const data = diagramsData[currentTabIndex];
      document.getElementById("diagTitle").innerText = data.name;
      document.getElementById("diagSub").innerText = data.category;
      document.getElementById("diagDesc").innerHTML = data.desc;

      // Render high-clarity SVG for the active diagram
      const frame = document.getElementById("diagramFrame");
      frame.innerHTML = generateSvgForIndex(currentTabIndex);
    }}

    function generateSvgForIndex(index) {{
      const w = 1200;
      const h = 640;
      
      switch(index) {{
        case 0: // Class
          return `
            <svg width="100%" height="${{h}}" viewBox="0 0 ${{w}} ${{h}}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${{w}}" height="${{h}}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 類別圖】RD_SAMPLE 與 D365 C# 服務領域物件模型 (依 Duke 規格：全 C# 實作)</text>
              
              <!-- RqtBaseForm -->
              <g transform="translate(50, 80)">
                <rect width="280" height="310" rx="4" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <rect width="280" height="40" fill="#9673a6"/>
                <text x="140" y="18" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;abstract&gt;&gt; RqtBaseForm</text>
                <text x="140" y="32" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#f0e6f6" text-anchor="middle">C# Core Request Model</text>
                
                <text x="15" y="65" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ SalesId : string [SO編號]</text>
                <text x="15" y="85" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ StyleNo : string [款號]</text>
                <text x="15" y="105" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ ContractNo : string [合同編號]</text>
                <text x="15" y="125" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ PurchId : string [PO編號]</text>
                <text x="15" y="145" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ ItemId : string [物料編號]</text>
                <text x="15" y="165" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ VendId / CustId : string</text>
                <text x="15" y="185" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ BuyKeys : List&lt;long&gt; [RecId]</text>
                <text x="15" y="205" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ ContractNos : List&lt;string&gt;</text>
                <text x="15" y="225" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ DataAreaId : string = "RSI"</text>
                <text x="15" y="245" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ UserName : string [匯出人]</text>
                <line x1="0" y1="260" x2="280" y2="260" stroke="#9673a6" stroke-width="1"/>
                <text x="15" y="280" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ Validate() : bool</text>
                <text x="15" y="300" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ ToParameterDictionary()</text>
              </g>

              <!-- D365 C# Custom Services -->
              <g transform="translate(380, 80)">
                <rect width="280" height="210" rx="4" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <rect width="280" height="40" fill="#9673a6"/>
                <text x="140" y="18" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;service&gt;&gt; D365CSharpServices</text>
                <text x="140" y="32" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#f0e6f6" text-anchor="middle">31 Services / 80 Operations (全量C#)</text>
                
                <text x="15" y="65" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ JCOM_WebServices : Module</text>
                <text x="15" y="85" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ RSI_WebServices : Module</text>
                <text x="15" y="105" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">- _tokenProvider: EntraBearerToken</text>
                <line x1="0" y1="120" x2="280" y2="120" stroke="#9673a6" stroke-width="1"/>
                <text x="15" y="140" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ GetStyleBom() : RSI_RT&lt;Bom&gt;</text>
                <text x="15" y="160" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ QueryInventory() : RSI_RT&lt;Stock&gt;</text>
                <text x="15" y="180" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ SyncPurchOrder() : RSI_RT&lt;PO&gt;</text>
                <text x="15" y="200" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ Execute80OperationsAsync()</text>
              </g>

              <!-- RSI_RT Envelope -->
              <g transform="translate(380, 320)">
                <rect width="280" height="170" rx="4" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <rect width="280" height="35" fill="#9673a6"/>
                <text x="140" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">RSI_RT&lt;T&gt; (C# 回應封裝)</text>
                <text x="15" y="60" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ IsValid : bool [是否成功]</text>
                <text x="15" y="80" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ Msg : string [回傳訊息]</text>
                <text x="15" y="100" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ TotalCount : int [總筆數]</text>
                <text x="15" y="120" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ DataList : List&lt;T&gt; [實體清單]</text>
                <line x1="0" y1="135" x2="280" y2="135" stroke="#9673a6" stroke-width="1"/>
                <text x="15" y="155" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ Success() / + Failure()</text>
              </g>

              <!-- MoHeader & MoDetail -->
              <g transform="translate(710, 80)">
                <rect width="240" height="210" rx="4" fill="#fff2cc" stroke="#d6b656" stroke-width="2"/>
                <rect width="240" height="35" fill="#d6b656"/>
                <text x="120" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">MoHeader (樣品單主檔)</text>
                <text x="15" y="55" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ MoNo : string [PK]</text>
                <text x="15" y="75" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ StyleNo : string [FK]</text>
                <text x="15" y="95" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ Season : string</text>
                <text x="15" y="115" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ TargetFactory : RSV / RSG</text>
                <text x="15" y="135" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ Status : EnumMoStatus</text>
                <line x1="0" y1="150" x2="240" y2="150" stroke="#d6b656" stroke-width="1"/>
                <text x="15" y="175" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ CreateMo() : bool</text>
                <text x="15" y="195" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ DispatchToFactory()</text>
              </g>

              <!-- DataAccess Direct SQL -->
              <g transform="translate(980, 80)">
                <rect width="200" height="190" rx="4" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <rect width="200" height="35" fill="#1d63ed"/>
                <text x="100" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">DataAccess (ADO.NET)</text>
                <text x="15" y="55" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">- _connStr : sa 明碼</text>
                <text x="15" y="75" font-family="'JetBrains Mono', monospace" font-size="11" fill="#b45309" font-weight="bold">! 1490 SQL (SAM)</text>
                <text x="15" y="95" font-family="'JetBrains Mono', monospace" font-size="11" fill="#b91c1c" font-weight="bold">! 23 SQL (AXDB)</text>
                <line x1="0" y1="110" x2="200" y2="110" stroke="#1d63ed" stroke-width="1"/>
                <text x="15" y="135" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ ExecuteQuery()</text>
                <text x="15" y="155" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ ExecuteNonQuery()</text>
                <text x="15" y="175" font-family="'JetBrains Mono', monospace" font-size="11" fill="#333">+ OpenConnection()</text>
              </g>

              <!-- Connections -->
              <path d="M 520 290 L 520 320" fill="none" stroke="#9673a6" stroke-width="2" stroke-dasharray="4" marker-end="url(#arrow)"/>
              <path d="M 710 185 L 660 185" fill="none" stroke="#9673a6" stroke-width="2" marker-end="url(#arrow)"/>
              <path d="M 950 185 L 980 185" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="4"/>
              <text x="965" y="175" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309" text-anchor="middle">1490 SQL</text>
            </svg>
          `;

        case 1: // Component
          return `
            <svg width="100%" height="${{h}}" viewBox="0 0 ${{w}} ${{h}}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${{w}}" height="${{h}}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 元件圖】RD_SAMPLE 系統組成、核心元件與微服務邊界拓撲</text>
              
              <!-- Components -->
              <g transform="translate(60, 100)">
                <rect width="240" height="90" rx="6" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <text x="20" y="35" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#1d63ed">&lt;&lt;component&gt;&gt;</text>
                <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">RD_Sample.Web</text>
                <text x="20" y="72" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#666">ASP.NET WebForms 4.8 / IIS</text>
              </g>

              <g transform="translate(60, 240)">
                <rect width="240" height="90" rx="6" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <text x="20" y="35" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#1d63ed">&lt;&lt;component&gt;&gt;</text>
                <text x="20" y="55" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">RD_Batch.Console</text>
                <text x="20" y="72" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#666">Windows 排程器 (13 項核心任務)</text>
              </g>

              <g transform="translate(360, 170)">
                <rect width="220" height="80" rx="6" fill="#fff2cc" stroke="#d6b656" stroke-width="2"/>
                <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#d6b656">&lt;&lt;component&gt;&gt;</text>
                <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">DataAccess.Core</text>
                <text x="20" y="68" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#666">ADO.NET 直下 SQL 封裝</text>
              </g>

              <g transform="translate(640, 90)">
                <rect width="280" height="100" rx="6" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#9673a6">&lt;&lt;component&gt;&gt; (全量 C#)</text>
                <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">D365 C# Integration Services</text>
                <text x="20" y="68" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#666">Report (:8085) / 80 Ops (Bearer)</text>
                <text x="20" y="85" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c">⚠️ 無驗證需收攏至 API Gateway</text>
              </g>

              <g transform="translate(640, 230)">
                <rect width="280" height="90" rx="6" fill="#d5e8d4" stroke="#82b366" stroke-width="2"/>
                <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#82b366">&lt;&lt;component&gt;&gt;</text>
                <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">CQS 品管微服務</text>
                <text x="20" y="68" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#666">.NET 8 Core / IIS ARR (:8012)</text>
              </g>

              <g transform="translate(640, 360)">
                <rect width="280" height="90" rx="6" fill="#f8cecc" stroke="#b85450" stroke-width="2" stroke-dasharray="4"/>
                <text x="20" y="30" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b85450">&lt;&lt;處方推薦架構&gt;&gt;</text>
                <text x="20" y="50" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">YARP API Gateway (0元平替)</text>
                <text x="20" y="68" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#666">在地零信任統一認證閘道</text>
              </g>

              <!-- DBs -->
              <g transform="translate(980, 160)">
                <path d="M 0 15 C 0 5, 160 5, 160 15 L 160 85 C 160 95, 0 95, 0 85 Z" fill="#fff2cc" stroke="#d6b656" stroke-width="2"/>
                <path d="M 0 15 C 0 25, 160 25, 160 15" fill="none" stroke="#d6b656" stroke-width="2"/>
                <text x="80" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#d6b656" text-anchor="middle">&lt;&lt;database&gt;&gt;</text>
                <text x="80" y="65" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#333" text-anchor="middle">SAM 主資料庫</text>
                <text x="80" y="80" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#666" text-anchor="middle">SQL Server 1433</text>
              </g>

              <!-- Lines -->
              <path d="M 300 145 L 360 185" fill="none" stroke="#1d63ed" stroke-width="2"/>
              <path d="M 300 285 L 360 235" fill="none" stroke="#1d63ed" stroke-width="2" stroke-dasharray="3"/>
              <path d="M 580 210 L 980 210" fill="none" stroke="#d6b656" stroke-width="2"/>
              <text x="780" y="200" font-family="'JetBrains Mono', monospace" font-size="11" fill="#d6b656" text-anchor="middle">I02: 1,490 處直接 SQL</text>
              <path d="M 300 130 L 640 130" fill="none" stroke="#9673a6" stroke-width="2"/>
              <text x="470" y="120" font-family="'JetBrains Mono', monospace" font-size="11" fill="#9673a6" text-anchor="middle">I08: D365 C# API (無驗證)</text>
              <path d="M 300 160 L 640 270" fill="none" stroke="#82b366" stroke-width="2"/>
              <text x="470" y="250" font-family="'JetBrains Mono', monospace" font-size="11" fill="#82b366" text-anchor="middle">I13: HTTP REST</text>
            </svg>
          `;

        case 2: // Deployment
          return `
            <svg width="100%" height="${{h}}" viewBox="0 0 ${{w}} ${{h}}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${{w}}" height="${{h}}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 部署圖】全集團實體伺服器、網路節點、專線與雲端拓撲 (依 Duke 節點表)</text>
              
              <!-- RDSMP2 -->
              <g transform="translate(50, 80)">
                <rect width="320" height="230" rx="6" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <rect width="320" height="35" fill="#1d63ed"/>
                <text x="160" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;device&gt;&gt; RDSMP2 正式機 (192.168.0.22)</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• IIS 443/80 (rdsample.rsiapparel.com)</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• SQL Server 2019 (1433) [SAM, PDFTAG, CQS]</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• Windows 排程 D:\\EXP (13 項核心批次)</text>
                <text x="15" y="126" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• SMB 445 (hrm, web_backup 芳鄰備份)</text>
                <text x="15" y="148" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 實體路徑 E:\\RD_SAMPLE (樣品工藝圖檔)</text>
                <text x="15" y="180" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b91c1c" font-weight="bold">! 承受每30分跨國直連與夜間高頻鎖表風險</text>
              </g>

              <!-- RDSMP1 -->
              <g transform="translate(50, 340)">
                <rect width="320" height="200" rx="6" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <rect width="320" height="35" fill="#1d63ed"/>
                <text x="160" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;device&gt;&gt; RDSMP1 測試機 (192.168.0.23)</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• IIS 80 (test-rdsample.rsiapparel.com)</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• SQL 1433 (SAM 正式副本、PDFTAG)</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• CQS 品質服務 (:8012/:8011)</text>
                <text x="15" y="126" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• FindImage 影像比對 (:8081)</text>
                <text x="15" y="148" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• GitLab Runner (CI/CD 自動編譯)</text>
              </g>

              <!-- D365 RSIMDW1 -->
              <g transform="translate(420, 80)">
                <rect width="330" height="180" rx="6" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <rect width="330" height="35" fill="#9673a6"/>
                <text x="165" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;device&gt;&gt; RSIMDW1 (192.168.0.95)</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• D365.Report.Service (:8085 / :8082 UAT)</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• Local.WebApi (:80 / :8081 UAT)</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• D365_Prod 唯讀副本庫 (SQL 1433)</text>
                <text x="15" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">! 報表下載 API 完全無驗證防護</text>
              </g>

              <!-- D365 Core Cluster -->
              <g transform="translate(420, 300)">
                <rect width="330" height="170" rx="6" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <rect width="330" height="35" fill="#9673a6"/>
                <text x="165" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;device cluster&gt;&gt; D365 Core ERP (C#)</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• D365 AOS (192.168.0.124～.126)</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• rsiaxdb1 (192.168.0.131 AXDB 營運主庫)</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 80 個 C# Operations (Entra ID Bearer)</text>
                <text x="15" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">! RD_SAMPLE 直下 23 處 SQL 侵入 AXDB</text>
              </g>

              <!-- Factory Nodes -->
              <g transform="translate(800, 80)">
                <rect width="340" height="180" rx="6" fill="#ffe6cc" stroke="#d79b00" stroke-width="2"/>
                <rect width="340" height="35" fill="#d79b00"/>
                <text x="170" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;factory nodes&gt;&gt; 海外廠區 DB (DYXnet 專線)</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 越南 RDV: 192.168.185.123:1433</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 柬埔寨 RDG: 192.168.193.65:1433</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#666">• [已停用] 桃園廠 TY: 192.168.5.123</text>
                <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#d79b00" font-weight="bold">! 每30分同步工單; 斷網即引發阻塞</text>
              </g>

              <!-- Cloud -->
              <g transform="translate(800, 300)">
                <rect width="340" height="160" rx="6" fill="#f8cecc" stroke="#b85450" stroke-width="2"/>
                <rect width="340" height="35" fill="#b85450"/>
                <text x="170" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;external cloud&gt;&gt; AWS EC2 &amp; Mail</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• AWS AI 推論: 98.84.29.205:8000</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• AWS 翻譯服務: 98.93.175.234:80</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 集團 SMTP 郵件: 192.168.8.64:587</text>
              </g>

              <!-- Connections -->
              <path d="M 370 140 L 420 140" fill="none" stroke="#9673a6" stroke-width="2"/>
              <path d="M 370 200 L 420 330" fill="none" stroke="#b91c1c" stroke-width="2" stroke-dasharray="4"/>
              <path d="M 370 120 L 800 120" fill="none" stroke="#d79b00" stroke-width="3"/>
              <text x="585" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#d79b00" font-weight="bold" text-anchor="middle">I05: 每 30 分鐘 TDS 1433 直連海外廠</text>
            </svg>
          `;

        default:
          return `
            <svg width="100%" height="${{h}}" viewBox="0 0 ${{w}} ${{h}}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${{w}}" height="${{h}}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 視覺模型】${{diagramsData[index].name}}</text>
              <rect x="50" y="80" width="1080" height="500" rx="8" fill="#f8f9fa" stroke="#d0d7de" stroke-width="2"/>
              <text x="590" y="240" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#24292f" text-anchor="middle">${{diagramsData[index].name}}</text>
              <text x="590" y="270" font-family="'Noto Sans TC', sans-serif" font-size="13" fill="#57606a" text-anchor="middle">已全量納入多頁 draw.io 原生檔案 (RSI_DUKE_UML2_ALL_DIAGRAMS.drawio)</text>
              <text x="590" y="300" font-family="'JetBrains Mono', monospace" font-size="12" fill="#0969da" text-anchor="middle">點擊上方「在 draw.io 線上編輯 / 查看」即可無縫開啟並進行拖曳編輯</text>
              
              <g transform="translate(440, 340)">
                <rect width="300" height="50" rx="6" fill="#238636" cursor="pointer" onclick="openInDrawio()"/>
                <text x="150" y="32" font-family="'Noto Sans TC', sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle" cursor="pointer" onclick="openInDrawio()">在 draw.io 開啟本頁圖資 ↗</text>
              </g>
            </svg>
          `;
      }}
    }}

    function openInDrawio() {{
      // Opens draw.io with the XML loaded directly via data URL or diagrams.net lightbox
      const encodedXml = encodeURIComponent(DRAWIO_XML);
      const url = "https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank#R" + encodeURIComponent(DRAWIO_XML);
      window.open(url, "_blank");
    }}

    function copyDrawioXml() {{
      navigator.clipboard.writeText(DRAWIO_XML).then(() => {{
        const toast = document.getElementById("toast");
        toast.style.display = "block";
        setTimeout(() => {{
          toast.style.display = "none";
        }}, 3500);
      }}).catch(err => {{
        alert("複製失敗，請手動下載 .drawio 檔案");
      }});
    }}

    function toggleTheme() {{
      const body = document.body;
      const current = body.getAttribute("data-theme");
      body.setAttribute("data-theme", current === "dark" ? "milan" : "dark");
    }}

    // Init
    renderTabs();
    updateDiagramView();
  </script>
</body>
</html>
'''

    output_path = os.path.join(base_dir, "rsi_duke_uml2_viewer.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"[OK] Generated UML 2 Viewer HTML: {output_path} ({len(html_code)} bytes)")
    return output_path

if __name__ == "__main__":
    generate_viewer_html()
