# LLM Climate Risk 2026

Replication repository for the following manuscript:

> **Evaluating the scientific rigour of climate scenario analysis: LLM-assisted evidence from New Zealand's mandatory disclosures**
> Quyen Nguyen, Florent Aden-Antoniow, Nicholas A. Cradock-Henry, Jack Drummond,  Rob Buxton, Ani Barr
> *Version: June 2026*

---

## Overview

This repository covers four main workflows:

1. Download of New Zealand climate statements from the CRE search hub
2. Exploratory analysis of the final sample
3. Preliminary data analysis of climate risk disclosures using NLP
4. Analysis of agentic RAG LLM-assisted results

For the full implementation of the agentic RAG pipeline, see: https://github.com/florentaden/agent-climate-disclosure

---

## Repository Structure

```
LLM_climaterisk_2026/
├── README.md
├── LICENSE
├── config.yaml                                   # All paths and settings (edit base_dir here)
│
├── 00_scripts/                                   # Analysis notebooks (run in order)
│   ├── config_loader.py                          # Reads config.yaml; imported by all notebooks
│   ├── 0-scrapping_disclosure.ipynb              # Scrape PDFs from CRE search hub
│   ├── 1-explatorary_analysis.ipynb              # Exploratory analysis of the sample
│   ├── 2-nlp_analysis.ipynb                      # NLP-based disclosure analysis
│   ├── 3-rag_result.ipynb                        # LLM-assisted extraction (RAG)
│   └── 4-rag_benchmark.ipynb                     # Benchmarking RAG outputs
│
├── 01_pdfs_2026/                                 # Downloaded disclosure PDFs
│
├── 02_full_rag_results/                          # LLM extraction outputs (one JSON per company-year)
│
├── 03_benchmark_rag_results/                     # Ground-truth comparison (13 JSON files)
│
├── 04_interim_results/                           # Reference & mapping tables
│   ├── Included_PDF_only.csv
│   ├── List_of_selected_PDF_forLLManalysis.csv
│   ├── List_of_climate_scenarios_RAG_renamed.csv
│   └── List_of_mapped_models.csv
│
└── 05_final_results/                             # Output figures and tables
```
## Background: Climate-Related Disclosures in New Zealand

In recognition of the ongoing impact of climate change, the New Zealand Government introduced a mandatory requirement for large entities to prepare and lodge annual climate-related disclosures. These entities are called **Climate Reporting Entities (CREs)** under the Financial Markets Conduct Act 2013.

CREs must lodge climate statements or exemption notices with the Registrar of Financial Service Providers within 4 months of their balance date. Entities with a 31 December 2023 balance date were the first to file, with statements due by 30 April 2024.

**CRE search hub:** https://crd-app.companiesoffice.govt.nz/dashboard/

**NZ Climate Standard (NZCS 1):** https://www.xrb.govt.nz/standards/climate-related-disclosures/aotearoa-new-zealand-climate-standards/aotearoa-new-zealand-climate-standard-1/

Around 200 New Zealand entities (CREs) are required to report, including large banks, insurers, management schemes and public listed issuers. These CRE must meet a threshold of reporting (e.g. >1 billion in AUM or >NZ$60 million in market cap, refer to the paper).

---

## Analysis Versions
- **Number of CREs:** 173 unique CREs as of 4 May 2026. 
- **Final sample:** 227 companies as of May 2026, covering two fiscal periods FY24/25 and FY23/24. Exploratory analysis and RAG analysis is conducted for this sample of 227 companies
- **Ground-truth sample:** comparison for 13 companies in FY23/24
  
---

## External Data

**Raw PDF files:** `https://drive.google.com/drive/folders/1ZEM4f6etkYN_Tn6AS2uynkCWAflSQmf_?usp=drive_link`

The PDFs are New Zealand climate-related disclosure statements lodged by Climate Reporting Entities (CREs) with the Registrar of Financial Service Providers.


---

## Configuration

All paths and model settings are stored in [`config.yaml`](config.yaml). Before running any notebook, update `base_dir` to match your local environment — everything else is derived from it automatically.

Before running webscraping, makesure you download the equivalent chrome driver and update `chromedriver`.

```yaml
paths:
  base_dir: "C:/Users/YourName/path/to/19_LLM_ClimateRisk2026"  # ← change this only
  repo_dir: "{base_dir}/4-Github2026_LLM/LLM_climaterisk_2026"  # derived automatically

  # Repo folders
  pdf_folder:           "{repo_dir}/01_pdfs_2026"
  rag_results_dir:      "{repo_dir}/02_full_rag_results"
  benchmark_output_dir: "{repo_dir}/03_benchmark_rag_results"
  fig_folder:           "{repo_dir}/05_final_results"

  # External data
  scraping_dir: "{base_dir}/3-Webscrapping & PDF disclosure"
  chromedriver: "{base_dir}/4-Github2026_LLM/chromedriver-win64/chromedriver.exe"

model:
  name:       "claude-sonnet-4-6"
  max_tokens: 8192
```

Each notebook loads config at the top via:
```python
from config_loader import load_config
cfg = load_config()
```

---

## Notebooks 

| Script | Description |
|--------|-------------|
| `0-scrapping_disclosure.ipynb` | Scrapes all disclosure statements and saves to `pdfs_2026/` |
| `1-explatorary_analysis.ipynb` | Exploratory analysis for 198 companies (May 2026, period 2024–2025) |
| `2-nlp_analysis.ipynb` | Preliminary NLP-based analysis of climate risk disclosures |
| `3-rag_result.ipynb` | LLM-assisted extraction of structured answers from PDFs |
| `4-rag_benchmark.ipynb` | Benchmarking and result analysis of LLM outputs |



---

