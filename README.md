# 信源全球 (RSI) · 2027 IT 營運計畫架構與全專案排程白皮書
> **總體戰略定位**：整合運用・智能營運 (Integration & Intelligent Operations)  
> **計劃主持人**：周文津 副總 (Executive Sponsor) ｜ **執行負責人**：Howard Liao Ph.D. (Lead Architect & C-Level Advisor)  
> **線上即時戰情白皮書**：[https://howardliao.github.io/RSI/](https://howardliao.github.io/RSI/)  
> **全年度 25 項專案甘特圖**：[https://howardliao.github.io/RSI/gantt_chart_2027.html](https://howardliao.github.io/RSI/gantt_chart_2027.html)  
> **組織職能與內外部資源配置**：[https://howardliao.github.io/RSI/organization_resources.html](https://howardliao.github.io/RSI/organization_resources.html)  
> **現有技術職能與資通設備盤點實施手冊**：[https://howardliao.github.io/RSI/inventory_discovery.html](https://howardliao.github.io/RSI/inventory_discovery.html)

---

## 🎯 2027 四大戰略投資主軸與二千萬級資本精算 (v6.0.0)

依據信源全球跨國製造版圖（台北營運總部 + 越南隆安/西寧、柬埔寨金邊、印尼中爪哇），以 **全集團 2,500 席知識工作者與現場幹部** 規模進行企業級完整配置：

* **Pillar I 數位底座年度基準總預算**：**$640,000 USD / 年 (約 NT$ 2,016 萬，基準二千萬規模)**
  * **55% Run (維運穩固)**：$352,000 USD (約 NT$ 1,109 萬) — 保障生產 100% 零中斷、CrowdStrike 24/7 MDR 全託管、Zerto 秒級災備。
  * **25% Grow (業務擴展)**：$160,000 USD (約 NT$ 504 萬) — 支援柬/印新廠交鑰匙複製、Databricks 30TB+ 湖倉與 MDM 擴展。
  * **20% Transform (智能轉型)**：$128,000 USD (約 NT$ 403 萬) — Agentic AI 落地、多語言技術手冊編譯與動態排線。
* **單件成衣數位成本 (DCPG)**：
  $$\text{DCPG} = \frac{\$640,000}{75,000,000 \text{ 件}} \approx \mathbf{\$0.0085 \text{ USD / 件 (約合 NT\$ 0.27 / 件，不到三毛錢！)}}$$

---

## 📅 2027 全年度 25 項專案甘特圖 (排開連假與封網期)

排程嚴格排除週休二日與跨國重大連續假日：
* **2月春節 / 越南 Tet 年假 (2/5~2/14)**：工廠全停工 10 天，實施 **系統封網 (Code Freeze)**，禁止核心生產變更。
* **3月印尼開齋節 (3/9~3/12)**、**4月中旬柬埔寨新年 (4/13~4/16)**：排開各廠產線停工期。
* **四季平準化推進節奏**：
  * **Q1 (1-3月) · 總部築底** (15 項啟動)：總部雙活 Kong 網關、Entra ID 分層 SSO、Zerto 秒級災備。
  * **Q2 (4-6月) · 隆安燈塔** (24 項攻堅)：Ready-to-Sew 4-Gate 產前門禁、72h 斷網離線自律、Flink PCD 缺料預警。
  * **Q3 (7-9月) · 柬印複製** (23 項推廣)：柬埔寨金邊與印尼中爪哇交鑰匙複製、Databricks 30TB 湖倉、Profisee MDM 主數據。
  * **Q4 (10-12月) · 集團驗收** (12 項收官)：Agentic AI 生管跟單、OR-Tools 動態線平衡人機排程、全集團 2,500 席驗收。

---

## 🏛️ 25 項企業級實戰工具選型矩陣

* **Pillar I 數位底座 (8項)**：Kong Enterprise, Microsoft Entra ID P2/F-SKU, HashiCorp Vault, Databricks Delta Lake, Profisee MDM, Portkey/LiteLLM, CrowdStrike Falcon Complete (24/7 MDR), Zerto CDP, Fortinet Secure SD-WAN (HA), 研華工業邊緣主機。
* **Pillar II 營運流程 (5項)**：Camunda 8, 供應鏈 Control Tower, Ready-to-Sew 4-Gate, GSDCost, Flowable BPM。
* **Pillar III 智能決策 (7項)**：Apache Flink CEP, Power BI, XGBoost/LightGBM, Google OR-Tools, LangGraph / Autogen, Qdrant + LlamaParse, Power Automate。
* **Pillar IV 智慧製造 (5項)**：Kepware OPC-UA + EMQX, NVIDIA vLLM + K3s, Moxa/研華邊緣網關 (Delta Sync), Impinj RFID, 貼合溫壓 IoT 監控。

---

## 🌐 國際化多語言支援 (6 國語言即時切換)

1. 🇹🇼 **繁體中文** (台北營運總部)
2. 🇬🇧 **English** (Global Brand Clients)
3. 🇯🇵 **日本語** (日系品牌品質規範)
4. 🇻🇳 **Tiếng Việt** (越南隆安旗艦示範廠)
5. 🇰🇭 **ភាសាខ្មែរ** (柬埔寨金邊針織運動廠，支援 Google Noto Sans Khmer 字型)
6. 🇮🇩 **Bahasa Indonesia** (印尼中爪哇無縫/熱壓新基地)

---
*版權聲明：本計畫與架構模型受 Howard Liao Ph.D. 專利保護與浮水印防偽管制，僅供信源全球內部戰略決策使用。*
