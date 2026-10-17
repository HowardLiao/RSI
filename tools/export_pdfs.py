#!/usr/bin/env python3
"""Re-export the download-center PDFs from their source HTML pages.

Each PDF in Hive/download_center.html is a headless-Chrome print of one site
page. Run this after editing any of those pages so the PDFs stay in step:

    python3 tools/export_pdfs.py            # all
    python3 tools/export_pdfs.py togaf      # only targets whose PDF name contains "togaf"
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# PDF (relative to site root) -> source HTML page (relative to site root)
TARGETS = {
    "Hive/RSI_2027_蜂巢計畫實施藍圖_Project_Hive.pdf": "Hive/index.html",
    "RSI_CEO戰略營運計畫_2027.pdf": "ceo_strategic_plan.html",
    "Hive/RSI_TOGAF企業架構與API品質標準規範書.pdf": "Hive/togaf_api_quality_standards.html",
    "Hive/RSI_邊界WAAP與旁路API安全雙軌聯防架構報告.pdf": "Hive/waap_api_security_architecture.html",
    "Hive/RSI_三大雲端體系_API與DataLake架構層級運作圖資.pdf": "Hive/cloud_platforms_deepdive_architecture.html",
    "Hive/RSI_API_Platform與DataLake工具選型評估_GCP_AWS_OpenSource.pdf": "Hive/platform_tools_comparison_matrix.html",
    "Hive/RSI_API_Platform與DataLake雙核心架構報告.pdf": "Hive/platforms_architecture_showcase.html",
    "Hive/RSI_API_Platform_架構圖與時序圖.pdf": "Hive/api_platform_drawio.html",
    "Hive/RSI_DataLake_ETL_ELT_架構圖與時序圖.pdf": "Hive/datalake_etl_elt_drawio.html",
    "Hive/RSI_內部IT_技術職能問卷與缺口分析報告.pdf": "Hive/it_skills_8domains_assessment.html",
    "Hive/RSI_內部工程師高階技術職能深度盤點評鑑表.pdf": "Hive/engineer_skills_inventory.html",
    "Hive/RSI_資訊基礎設施與系統6大領域盤點表.pdf": "Hive/it_infrastructure_inventory.html",
    "Hive/RSI_內部工程師6大領域分項盤點表.pdf": "Hive/modular_skills_inventory.html",
    "Hive/RSI_Group_會議紀錄_2026-10-16.pdf": "Hive/RSI_Group_會議紀錄_2026-10-16.html",
}


# Tabbed pages hide every panel except the active one (display:none), so a plain
# print only captured the first tab. Print a temporary copy with all panels shown,
# each panel starting on a new page, and nothing clipped by scroll containers.
PRINT_ALL = """<style id="print-all-panels">
@media print {
  .panel, .diagram-panel, .subform-panel { display: block !important; opacity: 1 !important;
    transform: none !important; animation: none !important; visibility: visible !important; }
  :is(.panel, .diagram-panel, .subform-panel) ~ :is(.panel, .diagram-panel, .subform-panel) { break-before: page; }
  .tab-btn, .module-nav-tabs, .tab-nav, .tabs-nav { display: none !important; }
  .table-wrap, .table-container, .scroll-x, pre, .code-block { overflow: visible !important; max-height: none !important; }
  .rsi-music { display: none !important; }
}
</style>"""


def export(pdf: str, html: str) -> None:
    page = ROOT / html
    tmp = page.with_name(".print_tmp_" + page.name)
    text = page.read_text(encoding="utf-8")
    tmp.write_text(text.replace("</head>", PRINT_ALL + "\n</head>", 1), encoding="utf-8")
    out = ROOT / pdf
    try:
        subprocess.run(
            [
                CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                "--hide-scrollbars", "--run-all-compositor-stages-before-draw",
                "--virtual-time-budget=15000", f"--print-to-pdf={out}", tmp.as_uri(),
            ],
            check=True, capture_output=True,
        )
    finally:
        tmp.unlink(missing_ok=True)
    print(f"{out.stat().st_size / 1e6:6.2f} MB  {pdf}  <-  {html}")


if __name__ == "__main__":
    pick = [a.lower() for a in sys.argv[1:]]
    for pdf, html in TARGETS.items():
        if not pick or any(p in pdf.lower() for p in pick):
            export(pdf, html)
