# LLM_climaterisk_2026
This is the repo to update the data analysis of climate risk disclosure using LLM. 

### About Climate Related Disclosure 
In recognition of the ongoing impact that climate change has on New Zealand the Government introduced a requirement for large entities to prepare and lodge annual climate-related disclosures (climate statements). These entities are called Climate Reporting Entities (CREs) under the Financial Markets Conduct Act 2013.  

The aim of requiring CREs to consider and report on climate-related risks and opportunities is to encourage a transition to a low-emissions future.

CREs are required to lodge climate statements or exemption notices with the Registrar of Financial Service Providers within 4 months after the balance date of the entity. CREs with a balance date of 31 December 2023 will be the first to file their climate statements which are due by 30 April 2024.

The CRE search hub is this link: https://crd-app.companiesoffice.govt.nz/dashboard/

The link to the disclousre is: https://www.xrb.govt.nz/standards/climate-related-disclosures/aotearoa-new-zealand-climate-standards/aotearoa-new-zealand-climate-standard-1/ 

### Which entities are Climate Reporting Entities (CREs): 
Around 200 entities in New Zealand will be required to prepare and lodge climate statements or exemption notices. CREs are a subset of FMC reporting entities, and include: 
 - Large registered banks, credit unions, and building societies. Those with total assets of more than $1 billion. 
 - Large managers of registered investment schemes (other than restricted schemes). Those with greater than $1 billion in total assets under management. 
 - Large licensed insurers. Those with greater than $1 billion in total assets or annual gross premium income greater than $250 million. 
 - Large listed issuers of quoted equity securities or quoted debt securities. An equity issuer is large if the market price or fair value of all of its equity securities exceeds $60 million and a debt issuer is large if the face value of its quoted debt exceeds $60 million. Issuers listed on growth markets are excluded from the climate reporting entity definition. 
 
The thresholds for each entity are calculated as at the balance date of their 2 preceding accounting periods. These thresholds will be amended from time to time to reflect the movements in the consumers price index.

### Change in regulations
* 15 December 2022, the XRB issued Aotearoa New Zealand Climate Standards (NZ CS). 
* 1 January 2023, the Climate Standard come into effective. 
* 30 November 2023, the XRB conducted international alignment of climate reporting –and fidn that there is a high degree of interoperability between NZ CS and the TCFD recommendations and the ISSB standards
* 1 January 2024, CREs are required to prepare climate statements and lodge them on this register.  
* 27 October 2024, Mandatory assurance of Greenhouse Gas (GHG) emissions begins for reporting periods ending on or after this date
* 2024 - 2025: Initial "Climate Statements" are published by early adopters and mandatory entities.
* November 2024/2025: Amendments made to Adoption provisions (NZ CS 2), including extending provisions for Scope 3 GHG emissions to allow for better data quality.
* Future (2026/2028): Potential changes in 2025 may adjust thresholds for reporting entities (e.g., changing to \(NZD550\) million market cap, possibly dropping to \(NZD250\) million later)


### Analysis versions

* `pdfs_2024` The first analysis was conducted in June 2024 for 35 companies (including 30 companies reported as of 7 May 2024 and 5 extra banks from 2022-2023). 
* `pdfs_2026` The second analysis was conducted in May 2026 for 198 companies (across all target years in 2023-2026). This analysis now only includes a snapshot of 198 companies as of May 2026 for the period from 2024-2025. 

### Update of 2026 versions 

- Exploratory analysis for 198 companies as of May 2026 for the period from 2024 to 2025 
- LLM analysis for 198 companies within 2024-2025 
- Groundtruth comparison for 35 companies (17 companies with manual data) in 2024-2025 


### Scripts
- `0-scrapping_climate_risk_disclosure.ipynb' to scrap all disclosure statement and saved to 'pdfs_2026'
- `1-explatory_analysis.ipynb' to conduct exploratory analysis for 198 companies as of May 2026 for the period from 2024 to 2025 
