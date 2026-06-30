# LLM Climate Risk 2026

Replication repository for the following manuscript:

> Nguyen, Q., Aden-Antoniow, F., Cradock-Henry, N. A., Drummond, J., Buxton, R., & Barr, A. (2026). *Evaluating the scientific rigour of climate scenario analysis: LLM-assisted evidence from New Zealand's mandatory disclosures* [Working paper].

---
## Background: Climate-Related Disclosures in New Zealand

In recognition of the ongoing impact of climate change, the New Zealand Government introduced a mandatory requirement, namely **NZ Climate Standard (NZCS 1, 2, 3)[https://www.xrb.govt.nz/standards/climate-related-disclosures/aotearoa-new-zealand-climate-standards/aotearoa-new-zealand-climate-standard-1/]** for large entities to prepare and lodge annual climate-related disclosures. These entities are called **Climate Reporting Entities (CREs)** under the Financial Markets Conduct Act 2013. 

Around 200 CREs are required to report, including large banks, insurers, management schemes and public listed issuers. These CRE must meet a threshold of reporting (e.g. >1 billion in AUM or >NZ$60 million in market cap, refer to the paper). CREs must lodge climate statements or exemption notices with the **CRE search hub[https://crd-app.companiesoffice.govt.nz/dashboard/]** within 4 months of their balance date. 

This notebook explores the scientific rigour of these disclosures in the first two iterations (FY24/25 and FY23/24).

---

## Overview

This repository covers five main workflows:

1. Download of New Zealand climate statements from the CRE search hub
2. Exploratory analysis of the final sample
3. Preliminary data analysis of climate risk disclosures using NLP
4. Analysis of agentic RAG results
5. Benchmark RAG results with groundtruth

**Important!** The repository does not cover the full implementation of the agentic RAG pipeline. For the full implementation of the agentic RAG pipeline, see: https://github.com/florentaden/agent-climate-disclosure

---

## Notebooks 

<table>
<tr><th width="40%">Script</th><th>Description</th></tr>
<tr><td><code>0-scrapping_disclosure.ipynb</code></td><td>Download of New Zealand climate statements from the CRE search hub and save to <code>01_pdfs_2026/</code></td></tr>
<tr><td><code>1-sample_analysis.ipynb</code></td><td>Exploratory analysis for the final sample 227 statements (May 2026, period 2024–2025)</td></tr>
<tr><td><code>2-nlp_analysis.ipynb</code></td><td>Preliminary NLP-based analysis of climate risk disclosures</td></tr>
<tr><td><code>3-rag_result.ipynb</code></td><td>Analysis of agentic RAG results from structured answers from PDFs</td></tr>
<tr><td><code>4-rag_benchmark.ipynb</code></td><td>Benchmarking and result analysis of RAG outputs vs groundtruth</td></tr>
</table>


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
│   ├── 1-sample_analysis.ipynb                   # Exploratory analysis of the sample
│   ├── 2-nlp_analysis.ipynb                      # NLP-based disclosure analysis
│   ├── 3-rag_result.ipynb                        # LLM-assisted extraction (RAG)
│   └── 4-rag_benchmark.ipynb                     # Benchmarking RAG outputs
│
├── 01_pdfs_2026/                                 # Downloaded disclosure PDFs
│
├── 02_full_rag_results/                          # LLM extraction outputs (one JSON per company-year for 227 sample files)
│
├── 03_benchmark_rag_results/                     # Ground-truth comparison (one JSON per company-year for 13 sample files)
│
├── 04_interim_results/                           # Reference & mapping tables 
│   ├── Explatorary_Analysis_2026.xlsx
│   ├── Included_PDF_only.csv
│   ├── List_of_all_PDF_for_normal_companies.csv
│   ├── List_of_all_disclosures_as_of_2026_mapped.csv
│   ├── List_of_climate_scenarios_RAG_renamed.csv
│   ├── List_of_mapped_models.csv
│   ├── List_of_selected_PDF_forLLManalysis.csv
│   ├── List_of_unmatched_model.csv
│   └── webscraping/
│       ├── List_of_all_disclosures_as_of_2026.csv
│       ├── List_of_investment_scheme_sub-entities_2026.csv
│       ├── List_of_reporting_firms_2026.csv
│       ├── List_of_reporting_firms_2026_detailed.csv
│       └── List_of_reporting_firms_2026_withlink.csv
│
└── 05_final_results/                             # Output figures and tables
```
---

## Analysis Versions
- **Number of hyperlink:** 744 hyperlink to climate reports as of 4 May 2026, including both normal CREs and investment managers. 
- **Number of CREs:** 173 unique CREs as of 4 May 2026. 
- **Final sample:** 227 companies as of May 2026, covering two fiscal periods FY24/25 and FY23/24. 
- **Ground-truth sample:** comparison for 13 companies in FY23/24
  
---

## Data
The main datasets covered in this analysis included:
- `04_interim_results\webscraping\List_of_all_disclosures_as_of_2026.csv`: This is the master hyperlink to download all climate disclosures (744 hyperlinks). These links would be reviewed manually and filtered to arrive at the final sample (227 company-year pairs). 
  
- `04_interim_results\List_of_selected_PDF_forLLManalysis.csv`: This is the master file that includes the final sample, such as company name and industries (the final sample is 227 company-year pairs after excluding 7 files that are not actually climate disclosure). 
  
- `02_full_rag_results`: Include the agentic RAG results for the final sample in the analysis (227 results), resulting from running the raw PDF files through the agentic RAG. These results are included for replication pursposes as the agentic RAG may produce different results on different settings. 
  
- `03_benchmark_rag_results`: Include the agentic RAG results for the verification sample in the analysis (13 results), resulting from running the raw PDF files through the agentic RAG.These results are included for replication pursposes as the agentic RAG may produce different results on different settings. 

<!-- **Raw PDF files:** `https://drive.google.com/drive/folders/1ZEM4f6etkYN_Tn6AS2uynkCWAflSQmf_?usp=drive_link` [uploading]

The PDFs are New Zealand climate-related disclosure statements lodged by Climate Reporting Entities (CREs) with the Registrar of Financial Service Providers. -->


---

## Configuration

All paths and model settings are stored in [`config.yaml`](config.yaml). Before running any notebook, update `base_dir` to match your local environment — everything else is derived from it automatically.

Before running webscraping, makesure you download the equivalent chrome driver and update `chromedriver`.

Each notebook loads config at the top via:
```python
from config_loader import load_config
cfg = load_config()
```






