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
│
├── scripts/                                      # Analysis notebooks (run in order)
│   ├── 0-scrapping_climate_risk_disclosure.ipynb # Scrape PDFs from CRE search hub
│   ├── 1-explatorary_analysis.ipynb              # Exploratory analysis of the sample
│   ├── 2-nlp_analysis.ipynb                      # NLP-based disclosure analysis
│   ├── 3-rag_result.ipynb                        # LLM-assisted extraction (RAG)
│   └── 4-rag_benchmark.ipynb                     # Benchmarking RAG outputs
│
├── full_rag_results/                             # LLM extraction outputs (234 JSON files)
│   └── {COMPANY}_{YEAR}.json                    # One file per company-year
│
├── benchmark_rag_results/                        # Ground-truth comparison (13 JSON files)
│   └── {COMPANY}_{YEAR}.json                    # Manually validated subset
│
└── interim_results/                              # Reference & mapping tables
    ├── Included_PDF_only.csv                     # Final PDF sample list
    ├── List_of_selected_PDF_forLLManalysis.csv   # PDFs selected for LLM analysis
    ├── List_of_climate_scenarios_RAG_renamed.csv # Scenario name mapping
    └── List_of_mapped_models.csv                 # Climate model name mapping
```
---

## Analysis Versions
- **Final Sample:** 227 companies as of May 2026, covering two fiscal periods FY24/25 and FY23/24. 
- Exploratory analysis for 227 companies
- LLM analysis for 227 companies
- Ground-truth comparison for 13 companies in FY23/24
  
---

## External Data

**Raw PDF files:** `` *(link to be updated)*

The PDFs are New Zealand climate-related disclosure statements lodged by Climate Reporting Entities (CREs) with the Registrar of Financial Service Providers.


---

## Scripts

| Script | Description |
|--------|-------------|
| `0-scrapping_disclosure.ipynb` | Scrapes all disclosure statements and saves to `pdfs_2026/` |
| `1-explatorary_analysis.ipynb` | Exploratory analysis for 198 companies (May 2026, period 2024–2025) |
| `2-nlp_analysis.ipynb` | Preliminary NLP-based analysis of climate risk disclosures |
| `3-rag_result.ipynb` | LLM-assisted extraction of structured answers from PDFs |
| `4-rag_benchmark.ipynb` | Benchmarking and result analysis of LLM outputs |



---

## Background: Climate-Related Disclosures in New Zealand

In recognition of the ongoing impact of climate change, the New Zealand Government introduced a mandatory requirement for large entities to prepare and lodge annual climate-related disclosures. These entities are called **Climate Reporting Entities (CREs)** under the Financial Markets Conduct Act 2013.

CREs must lodge climate statements or exemption notices with the Registrar of Financial Service Providers within 4 months of their balance date. Entities with a 31 December 2023 balance date were the first to file, with statements due by 30 April 2024.

**CRE search hub:** https://crd-app.companiesoffice.govt.nz/dashboard/

**NZ Climate Standard (NZCS 1):** https://www.xrb.govt.nz/standards/climate-related-disclosures/aotearoa-new-zealand-climate-standards/aotearoa-new-zealand-climate-standard-1/

### Which entities are CREs?

Around 200 New Zealand entities are required to report, including:

- **Large registered banks, credit unions, and building societies** — total assets > $1 billion
- **Large managers of registered investment schemes** — total assets under management > $1 billion
- **Large licensed insurers** — total assets > $1 billion or annual gross premium income > $250 million
- **Large listed issuers of quoted equity or debt securities** — equity issuers with market value > $60 million; debt issuers with face value of quoted debt > $60 million (growth market issuers excluded)

Thresholds are calculated at the balance date of the two preceding accounting periods and adjusted periodically for CPI movements.
