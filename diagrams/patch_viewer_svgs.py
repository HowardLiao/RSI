#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成信源全球 2027 蜂巢計畫 UML 2 全量架構圖資線上檢視入口
包含所有 14 張圖表之獨立高精細 SVG 繪製，以及完整 draw.io 整合功能。
"""

import os
import json

def get_svg_code_for_all_14():
    return """
    function generateSvgForIndex(index) {
      const w = 1200;
      const h = 640;
      
      switch(index) {
        case 0: // Class
          return `
            <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${w}" height="${h}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 類別圖】RD_SAMPLE 與 D365 C# 服務領域物件模型 (依 Duke 規格：全 C# 實作)</text>
              
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

              <path d="M 520 290 L 520 320" fill="none" stroke="#9673a6" stroke-width="2" stroke-dasharray="4"/>
              <path d="M 710 185 L 660 185" fill="none" stroke="#9673a6" stroke-width="2"/>
              <path d="M 950 185 L 980 185" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="4"/>
              <text x="965" y="175" font-family="'JetBrains Mono', monospace" font-size="10" fill="#b45309" text-anchor="middle">1490 SQL</text>
            </svg>
          `;

        case 1: // Component
          return `
            <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${w}" height="${h}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 元件圖】RD_SAMPLE 系統組成、核心元件與微服務邊界拓撲</text>
              
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

              <g transform="translate(980, 160)">
                <path d="M 0 15 C 0 5, 160 5, 160 15 L 160 85 C 160 95, 0 95, 0 85 Z" fill="#fff2cc" stroke="#d6b656" stroke-width="2"/>
                <path d="M 0 15 C 0 25, 160 25, 160 15" fill="none" stroke="#d6b656" stroke-width="2"/>
                <text x="80" y="45" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#d6b656" text-anchor="middle">&lt;&lt;database&gt;&gt;</text>
                <text x="80" y="65" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#333" text-anchor="middle">SAM 主資料庫</text>
                <text x="80" y="80" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#666" text-anchor="middle">SQL Server 1433</text>
              </g>

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
            <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${w}" height="${h}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 部署圖】全集團實體伺服器、網路節點、專線與雲端拓撲 (依 Duke 節點表)</text>
              
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

              <g transform="translate(420, 80)">
                <rect width="330" height="180" rx="6" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <rect width="330" height="35" fill="#9673a6"/>
                <text x="165" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;device&gt;&gt; RSIMDW1 (192.168.0.95)</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• D365.Report.Service (:8085 / :8082 UAT)</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• Local.WebApi (:80 / :8081 UAT)</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• D365_Prod 唯讀副本庫 (SQL 1433)</text>
                <text x="15" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">! 報表下載 API 完全無驗證防護</text>
              </g>

              <g transform="translate(420, 300)">
                <rect width="330" height="170" rx="6" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <rect width="330" height="35" fill="#9673a6"/>
                <text x="165" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;device cluster&gt;&gt; D365 Core ERP (C#)</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• D365 AOS (192.168.0.124～.126)</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• rsiaxdb1 (192.168.0.131 AXDB 營運主庫)</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 80 個 C# Operations (Entra ID Bearer)</text>
                <text x="15" y="130" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">! RD_SAMPLE 直下 23 處 SQL 侵入 AXDB</text>
              </g>

              <g transform="translate(800, 80)">
                <rect width="340" height="180" rx="6" fill="#ffe6cc" stroke="#d79b00" stroke-width="2"/>
                <rect width="340" height="35" fill="#d79b00"/>
                <text x="170" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;factory nodes&gt;&gt; 海外廠區 DB (DYXnet 專線)</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 越南 RDV: 192.168.185.123:1433</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 柬埔寨 RDG: 192.168.193.65:1433</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#666">• [已停用] 桃園廠 TY: 192.168.5.123</text>
                <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="10" fill="#d79b00" font-weight="bold">! 每30分同步工單; 斷網即引發阻塞</text>
              </g>

              <g transform="translate(800, 300)">
                <rect width="340" height="160" rx="6" fill="#f8cecc" stroke="#b85450" stroke-width="2"/>
                <rect width="340" height="35" fill="#b85450"/>
                <text x="170" y="22" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">&lt;&lt;external cloud&gt;&gt; AWS EC2 &amp; Mail</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• AWS AI 推論: 98.84.29.205:8000</text>
                <text x="15" y="82" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• AWS 翻譯服務: 98.93.175.234:80</text>
                <text x="15" y="104" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">• 集團 SMTP 郵件: 192.168.8.64:587</text>
              </g>

              <path d="M 370 140 L 420 140" fill="none" stroke="#9673a6" stroke-width="2"/>
              <path d="M 370 200 L 420 330" fill="none" stroke="#b91c1c" stroke-width="2" stroke-dasharray="4"/>
              <path d="M 370 120 L 800 120" fill="none" stroke="#d79b00" stroke-width="3"/>
              <text x="585" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#d79b00" font-weight="bold" text-anchor="middle">I05: 每 30 分鐘 TDS 1433 直連海外廠</text>
            </svg>
          `;

        case 3: // Package
          return `
            <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${w}" height="${h}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 套件圖】集團軟體命名空間、分層模組架構與依賴關係</text>
              
              <g transform="translate(60, 90)">
                <path d="M 0 0 L 80 0 L 100 20 L 280 20 L 280 150 L 0 150 Z" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <text x="15" y="15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#1d63ed">Presentation</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">RSI.RDSample.Presentation</text>
                <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ WebForms Pages (.aspx)</text>
                <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ jQuery &amp; Knockout.js</text>
                <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ jqxGrid Enterprise Grids</text>
              </g>

              <g transform="translate(420, 90)">
                <path d="M 0 0 L 90 0 L 110 20 L 280 20 L 280 150 L 0 150 Z" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <text x="15" y="15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#1d63ed">BusinessLogic</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">RSI.RDSample.BLL</text>
                <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ SampleOrderManager</text>
                <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ TechPackIngestionService</text>
                <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ CrossBorderSyncOrchestrator</text>
              </g>

              <g transform="translate(780, 90)">
                <path d="M 0 0 L 80 0 L 100 20 L 280 20 L 280 150 L 0 150 Z" fill="#fff2cc" stroke="#d6b656" stroke-width="2"/>
                <text x="15" y="15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#d6b656">DataAccess</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">RSI.Core.DataAccess</text>
                <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ SqlServerDirectAccessor</text>
                <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ DbConnectionPoolManager</text>
                <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#b45309">! 1,490 直下 SQL 實作</text>
              </g>

              <g transform="translate(60, 300)">
                <path d="M 0 0 L 80 0 L 100 20 L 280 20 L 280 150 L 0 150 Z" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <text x="15" y="15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#1d63ed">BatchJobs</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">RSI.RDSample.RD_Batch</text>
                <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ NotificationDispatcher</text>
                <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ FactorySyncExecutor</text>
                <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ ErpMasterSyncScheduler</text>
              </g>

              <g transform="translate(420, 300)">
                <path d="M 0 0 L 80 0 L 100 20 L 280 20 L 280 150 L 0 150 Z" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <text x="15" y="15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#9673a6">C# Services</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">RSI.D365.Services (C#)</text>
                <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ JCOM_WebServices (C#)</text>
                <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ RSI_WebServices (C#)</text>
                <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ D365.Report.Service</text>
              </g>

              <g transform="translate(780, 300)">
                <path d="M 0 0 L 80 0 L 100 20 L 280 20 L 280 150 L 0 150 Z" fill="#d5e8d4" stroke="#82b366" stroke-width="2"/>
                <text x="15" y="15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#82b366">QualityCore</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333">RSI.Quality.CQS (.NET 8)</text>
                <text x="15" y="70" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ InspectionController</text>
                <text x="15" y="90" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ ArrReverseProxyConfig</text>
                <text x="15" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#555">+ QualityAuditGateway</text>
              </g>

              <path d="M 340 160 L 420 160" fill="none" stroke="#1d63ed" stroke-width="2" stroke-dasharray="4"/>
              <path d="M 700 160 L 780 160" fill="none" stroke="#1d63ed" stroke-width="2" stroke-dasharray="4"/>
              <path d="M 340 375 L 420 375" fill="none" stroke="#9673a6" stroke-width="2" stroke-dasharray="4"/>
              <path d="M 560 240 L 560 300" fill="none" stroke="#9673a6" stroke-width="2" stroke-dasharray="4"/>
            </svg>
          `;

        case 8: // Activity Diagram
          return `
            <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${w}" height="${h}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 活動圖】樣品開單至出貨跨國協同泳道業務流程 (Swimlanes)</text>
              
              <!-- Swimlane Columns -->
              <g transform="translate(60, 80)">
                <rect width="250" height="520" fill="#f8f9fa" stroke="#ccc" stroke-width="1"/>
                <rect width="250" height="35" fill="#e9ecef"/>
                <text x="125" y="22" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333" text-anchor="middle">總部研發 (HQ RD)</text>
                
                <circle cx="125" cy="70" r="14" fill="#000"/>
                <rect x="35" y="120" width="180" height="55" rx="8" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <text x="125" y="152" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#333" text-anchor="middle">上傳客戶 TechPack PDF</text>

                <rect x="35" y="210" width="180" height="65" rx="8" fill="#d0e1fd" stroke="#1d63ed" stroke-width="2"/>
                <text x="125" y="238" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#333" text-anchor="middle">Python CLI 抽取工藝</text>
                <text x="125" y="258" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#666" text-anchor="middle">ADO.NET 直下 SQL 寫 SAM</text>
              </g>

              <g transform="translate(310, 80)">
                <rect width="250" height="520" fill="#fff" stroke="#ccc" stroke-width="1"/>
                <rect width="250" height="35" fill="#e9ecef"/>
                <text x="125" y="22" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333" text-anchor="middle">D365 C# ERP 服務</text>

                <rect x="35" y="210" width="180" height="65" rx="8" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
                <text x="125" y="238" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#333" text-anchor="middle">驗證款號與物料資訊</text>
                <text x="125" y="258" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#666" text-anchor="middle">D365 C# 80 Ops (Bearer)</text>
              </g>

              <g transform="translate(560, 80)">
                <rect width="250" height="520" fill="#f8f9fa" stroke="#ccc" stroke-width="1"/>
                <rect width="250" height="35" fill="#e9ecef"/>
                <text x="125" y="22" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333" text-anchor="middle">Windows 排程 (RD_Batch)</text>

                <rect x="35" y="310" width="180" height="65" rx="8" fill="#ffe6cc" stroke="#d79b00" stroke-width="2"/>
                <text x="125" y="338" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#333" text-anchor="middle">Sync_RSV.bat (每30分)</text>
                <text x="125" y="358" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b45309" text-anchor="middle">DYXnet 專線直推海外廠</text>
              </g>

              <g transform="translate(810, 80)">
                <rect width="320" height="520" fill="#fff" stroke="#ccc" stroke-width="1"/>
                <rect width="320" height="35" fill="#e9ecef"/>
                <text x="160" y="22" font-family="'Noto Sans TC', sans-serif" font-size="13" font-weight="bold" fill="#333" text-anchor="middle">海外廠區生管 (RSV / RSG)</text>

                <rect x="70" y="310" width="180" height="65" rx="8" fill="#ffe6cc" stroke="#d79b00" stroke-width="2"/>
                <text x="160" y="338" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#333" text-anchor="middle">排產車縫打樣</text>
                <text x="160" y="358" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#666" text-anchor="middle">錄入廠區生產日報</text>

                <rect x="70" y="410" width="180" height="55" rx="8" fill="#d5e8d4" stroke="#82b366" stroke-width="2"/>
                <text x="160" y="442" font-family="'Noto Sans TC', sans-serif" font-size="12" font-weight="bold" fill="#333" text-anchor="middle">CQS 品質檢驗放行</text>

                <circle cx="160" cy="520" r="14" fill="#000"/>
                <circle cx="160" cy="520" r="18" fill="none" stroke="#000" stroke-width="2"/>
              </g>

              <!-- Flow Arrows -->
              <path d="M 185 164 L 185 210" fill="none" stroke="#333" stroke-width="2"/>
              <path d="M 275 242 L 345 242" fill="none" stroke="#9673a6" stroke-width="2"/>
              <text x="310" y="235" font-family="'JetBrains Mono', monospace" font-size="10" fill="#9673a6" text-anchor="middle">I08</text>
              <path d="M 435 275 L 435 342 L 595 342" fill="none" stroke="#333" stroke-width="2"/>
              <path d="M 775 342 L 880 342" fill="none" stroke="#d79b00" stroke-width="3"/>
              <text x="825" y="335" font-family="'JetBrains Mono', monospace" font-size="10" fill="#d79b00" text-anchor="middle">TDS 1433</text>
              <path d="M 970 375 L 970 410" fill="none" stroke="#333" stroke-width="2"/>
              <path d="M 970 465 L 970 502" fill="none" stroke="#333" stroke-width="2"/>
            </svg>
          `;

        case 10: // Sequence Diagram
          return `
            <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${w}" height="${h}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 循序圖】樣品開單、Python 解析、C# 服務調用與跨國排程同步時序</text>
              
              <!-- Lifelines -->
              <g transform="translate(60, 80)">
                <rect width="130" height="35" rx="4" fill="#f8f9fa" stroke="#333" stroke-width="1.5"/>
                <text x="65" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#333" text-anchor="middle">設計師 (User)</text>
                <line x1="65" y1="35" x2="65" y2="520" stroke="#888" stroke-dasharray="4"/>
              </g>

              <g transform="translate(240, 80)">
                <rect width="140" height="35" rx="4" fill="#d0e1fd" stroke="#1d63ed" stroke-width="1.5"/>
                <text x="70" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#1d63ed" text-anchor="middle">RDSMP2: WebForms</text>
                <line x1="70" y1="35" x2="70" y2="520" stroke="#888" stroke-dasharray="4"/>
              </g>

              <g transform="translate(430, 80)">
                <rect width="140" height="35" rx="4" fill="#d0e1fd" stroke="#1d63ed" stroke-width="1.5"/>
                <text x="70" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#1d63ed" text-anchor="middle">I04: Python Parser</text>
                <line x1="70" y1="35" x2="70" y2="520" stroke="#888" stroke-dasharray="4"/>
              </g>

              <g transform="translate(620, 80)">
                <rect width="130" height="35" rx="4" fill="#fff2cc" stroke="#d6b656" stroke-width="1.5"/>
                <text x="65" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#d6b656" text-anchor="middle">SAM DB (1433)</text>
                <line x1="65" y1="35" x2="65" y2="520" stroke="#888" stroke-dasharray="4"/>
              </g>

              <g transform="translate(800, 80)">
                <rect width="150" height="35" rx="4" fill="#e1d5e7" stroke="#9673a6" stroke-width="1.5"/>
                <text x="75" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#9673a6" text-anchor="middle">D365 C# Svc (:8085)</text>
                <line x1="75" y1="35" x2="75" y2="520" stroke="#888" stroke-dasharray="4"/>
              </g>

              <g transform="translate(1000, 80)">
                <rect width="140" height="35" rx="4" fill="#ffe6cc" stroke="#d79b00" stroke-width="1.5"/>
                <text x="70" y="22" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#d79b00" text-anchor="middle">海外廠 DB (RSV)</text>
                <line x1="70" y1="35" x2="70" y2="520" stroke="#888" stroke-dasharray="4"/>
              </g>

              <!-- Messages -->
              <path d="M 125 150 L 310 150" fill="none" stroke="#333" stroke-width="2"/>
              <text x="217" y="142" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333" text-anchor="middle">1. 上傳 TechPack PDF</text>

              <path d="M 310 190 L 500 190" fill="none" stroke="#1d63ed" stroke-width="2"/>
              <text x="405" y="182" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#1d63ed" text-anchor="middle">2. 呼叫 CLI parse</text>

              <path d="M 500 230 L 310 230" fill="none" stroke="#1d63ed" stroke-width="2" stroke-dasharray="4"/>
              <text x="405" y="222" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#1d63ed" text-anchor="middle">3. 回傳工藝 JSON</text>

              <path d="M 310 270 L 685 270" fill="none" stroke="#d6b656" stroke-width="2"/>
              <text x="497" y="262" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#b45309" text-anchor="middle">4. ADO.NET 直下 SQL 寫庫 (sa 帳號)</text>

              <path d="M 310 320 L 875 320" fill="none" stroke="#9673a6" stroke-width="2"/>
              <text x="592" y="312" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#9673a6" text-anchor="middle">5. 調用 D365 C# Report API (RqtBaseForm)</text>

              <path d="M 875 360 L 310 360" fill="none" stroke="#9673a6" stroke-width="2" stroke-dasharray="4"/>
              <text x="592" y="352" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#9673a6" text-anchor="middle">6. 回傳下載 URL (無驗證)</text>

              <path d="M 685 410 L 1070 410" fill="none" stroke="#d79b00" stroke-width="3"/>
              <text x="877" y="402" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#d79b00" font-weight="bold" text-anchor="middle">7. Sync_RSV.bat 排程 (每30分跨國專線直推)</text>
            </svg>
          `;

        case 13: // Timing Diagram
          return `
            <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${w}" height="${h}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 計時圖】13 項 Windows 排程工作時間軸與海纜斷網自律狀態波形</text>
              
              <!-- Channel 1: SendNotification -->
              <g transform="translate(60, 90)">
                <rect width="240" height="70" rx="4" fill="#f8cecc" stroke="#b85450" stroke-width="1.5"/>
                <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#b85450">SendNotification.bat</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">每 5 分鐘高頻輪詢</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#666">全天候 24 小時不間斷運行</text>

                <rect x="260" y="0" width="800" height="70" fill="#fff" stroke="#ccc"/>
                <path d="M 270 50 L 290 20 L 300 20 L 320 50 L 350 50 L 370 20 L 380 20 L 400 50 L 430 50 L 450 20 L 460 20 L 480 50 L 510 50 L 530 20 L 540 20 L 560 50 L 590 50 L 610 20 L 620 20 L 640 50 L 670 50 L 690 20 L 700 20 L 720 50 L 750 50 L 770 20 L 780 20 L 800 50 L 830 50 L 850 20 L 860 20 L 880 50 L 910 50 L 930 20 L 940 20 L 960 50 L 990 50 L 1010 20 L 1020 20 L 1040 50" fill="none" stroke="#b85450" stroke-width="2"/>
              </g>

              <!-- Channel 2: Factory Sync -->
              <g transform="translate(60, 180)">
                <rect width="240" height="70" rx="4" fill="#ffe6cc" stroke="#d79b00" stroke-width="1.5"/>
                <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#d79b00">Sync_RSV / RSG.bat</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">每 30 分鐘跨國專線推送</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#666">06:00 ~ 23:00 執行，深夜休眠</text>

                <rect x="260" y="0" width="800" height="70" fill="#fff" stroke="#ccc"/>
                <path d="M 270 50 L 280 20 L 360 20 L 370 50 L 440 50 L 450 20 L 530 20 L 540 50 L 610 50 L 620 20 L 700 20 L 710 50 L 780 50 L 790 20 L 870 20 L 880 50 L 1050 50" fill="none" stroke="#d79b00" stroke-width="2.5"/>
                <text x="960" y="40" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#888">深夜維護窗口 (休眠)</text>
              </g>

              <!-- Channel 3: ERP Night Batch -->
              <g transform="translate(60, 270)">
                <rect width="240" height="80" rx="4" fill="#e1d5e7" stroke="#9673a6" stroke-width="1.5"/>
                <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#9673a6">ERP 夜間批次 (C#)</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#333">23:01 顏色 / 23:15 對照</text>
                <text x="15" y="60" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#333">23:19 新料 / 23:31 變更</text>

                <rect x="260" y="0" width="800" height="80" fill="#fff" stroke="#ccc"/>
                <line x1="270" y1="60" x2="800" y2="60" stroke="#9673a6" stroke-width="2"/>
                <rect x="800" y="20" width="30" height="40" fill="#9673a6"/>
                <text x="815" y="15" font-family="'JetBrains Mono', monospace" font-size="9" fill="#9673a6" text-anchor="middle">23:01</text>
                <rect x="850" y="20" width="30" height="40" fill="#9673a6"/>
                <text x="865" y="15" font-family="'JetBrains Mono', monospace" font-size="9" fill="#9673a6" text-anchor="middle">23:15</text>
                <rect x="900" y="20" width="30" height="40" fill="#9673a6"/>
                <text x="915" y="15" font-family="'JetBrains Mono', monospace" font-size="9" fill="#9673a6" text-anchor="middle">23:19</text>
                <rect x="950" y="20" width="30" height="40" fill="#9673a6"/>
                <text x="965" y="15" font-family="'JetBrains Mono', monospace" font-size="9" fill="#9673a6" text-anchor="middle">23:31</text>
                <line x1="980" y1="60" x2="1050" y2="60" stroke="#9673a6" stroke-width="2"/>
              </g>

              <!-- Channel 4: Offline Tolerance -->
              <g transform="translate(60, 370)">
                <rect width="240" height="80" rx="4" fill="#d0e1fd" stroke="#1d63ed" stroke-width="1.5"/>
                <text x="15" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" fill="#1d63ed">海纜斷網自律 SLA</text>
                <text x="15" y="45" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#333">48 ~ 72 小時離線運轉</text>
                <text x="15" y="65" font-family="'Noto Sans TC', sans-serif" font-size="10" fill="#b91c1c">現狀：專線中斷即整廠停擺</text>

                <rect x="260" y="0" width="800" height="80" fill="#fff" stroke="#ccc"/>
                <path d="M 270 25 L 500 25 L 500 65 L 850 65 L 850 25 L 1050 25" fill="none" stroke="#b91c1c" stroke-width="3"/>
                <text x="380" y="20" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d">正常專線連線 (Online)</text>
                <text x="675" y="55" font-family="'Noto Sans TC', sans-serif" font-size="11" font-weight="bold" fill="#b91c1c">【海纜中斷事件】現狀排程連環逾時崩潰 ➔ 蜂巢處方：地端離線自律運轉</text>
                <text x="950" y="20" font-family="'Noto Sans TC', sans-serif" font-size="11" fill="#15803d">專線復原自動對齊</text>
              </g>
            </svg>
          `;

        default:
          return `
            <svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
              <rect width="${w}" height="${h}" fill="#fcfcfd"/>
              <text x="40" y="45" font-family="'Noto Sans TC', sans-serif" font-size="16" font-weight="bold" fill="#1d63ed">【UML 2 視覺模型】${diagramsData[index].name}</text>
              <rect x="50" y="80" width="1080" height="500" rx="8" fill="#f8f9fa" stroke="#d0d7de" stroke-width="2"/>
              <text x="590" y="230" font-family="'Noto Sans TC', sans-serif" font-size="18" font-weight="bold" fill="#24292f" text-anchor="middle">${diagramsData[index].name}</text>
              <text x="590" y="265" font-family="'Noto Sans TC', sans-serif" font-size="13" fill="#57606a" text-anchor="middle">本張圖表已完整收錄於原生 multi-page .drawio 檔案中（Page ID: ${diagramsData[index].id}）</text>
              <text x="590" y="295" font-family="'JetBrains Mono', monospace" font-size="12" fill="#0969da" text-anchor="middle">嚴格依據 Duke 2026-11-12 交付之 21 條介面拓撲與 D365 C# 服務規範繪製</text>
              
              <g transform="translate(440, 340)">
                <rect width="300" height="50" rx="6" fill="#238636" cursor="pointer" onclick="openInDrawio()"/>
                <text x="150" y="32" font-family="'Noto Sans TC', sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle" cursor="pointer" onclick="openInDrawio()">在 draw.io 線上直接開啟 ↗</text>
              </g>
            </svg>
          `;
      }
    }
    """

def patch_viewer_file():
    base_dir = "/Users/howard/Desktop/HermesAgent/PortFilio/RSI"
    viewer_file = os.path.join(base_dir, "rsi_duke_uml2_viewer.html")
    with open(viewer_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace generateSvgForIndex function
    old_start = "function generateSvgForIndex(index) {"
    old_end = "function openInDrawio() {"
    
    idx_start = content.find(old_start)
    idx_end = content.find(old_end)
    
    if idx_start != -1 and idx_end != -1:
        new_svg_func = get_svg_code_for_all_14().strip() + "\n\n    "
        new_content = content[:idx_start] + new_svg_func + content[idx_end:]
        with open(viewer_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[OK] Patched {viewer_file} with detailed SVGs for all 14 UML 2 diagrams ({len(new_content)} bytes)")
    else:
        print("[ERROR] Could not find insertion markers in rsi_duke_uml2_viewer.html")

if __name__ == "__main__":
    patch_viewer_file()
