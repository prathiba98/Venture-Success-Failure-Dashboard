#  Venture Success & Failure Dashboard
## streamlit app: https://venture-success-failure-dashboard-jewwfsaarzccd683by9fzv.streamlit.app/

An interactive Streamlit dashboard analyzing global startup success, funding patterns, survival trends, and industry-level failure risks.

This project explores how funding intensity, industry structure, and ecosystem evolution influence startup outcomes using 66,000+ global startup records.

---

##  Project Overview

The Venture Success & Failure Dashboard provides insights into:

- Startup formation trends over time  
- Funding distribution patterns  
- Funding differences across startup statuses  
- Industry-level failure rates  
- Survival dynamics across the ecosystem  

The dashboard transforms raw startup data into business-level insights using exploratory data analysis and interactive visualization.

---

##  Key Insights

###  Ecosystem Evolution
- Startup formation accelerated sharply after 2000, reflecting the rise of the digital economy and expansion of venture capital.
- Recent dips in startup counts may reflect incomplete reporting rather than structural decline.

###  Funding Dynamics
- Startup funding is highly right-skewed, with a small number of ventures capturing disproportionately large investments.
- Log transformation reveals a more structured funding distribution.
- IPO and acquired startups demonstrate significantly higher median funding compared to closed startups, suggesting strong capital-performance linkage.

###  Survival Patterns
- Most startups cluster within early operational years, highlighting high ecosystem volatility.
- While funding shows a weak positive relationship with survival duration, capital alone does not guarantee long-term sustainability.

###  Industry Risk Variation
- Failure rates vary across industries.
- Consumer-facing and promotion-driven sectors exhibit relatively higher failure proportions.
- Startup risk is not uniformly distributed and depends on structural characteristics of each industry.

---

##  Tech Stack

- Python  
- Pandas  
- NumPy  
- Plotly  
- Streamlit  

---

##  Data Preparation

The dataset was cleaned and transformed using:

- Funding value normalization  
- Date parsing and survival-year calculation  
- Failure classification (Closed = Failed)  
- Industry extraction from multi-category fields  
- Outlier handling  
- Null value treatment  

Feature engineering included:

- Startup Age (Years)  
- Failure Flag  
- Industry-Level Aggregations  

---

##  Dashboard Features

- Interactive year range filtering  
- Industry and country selection filters  
- KPI summary metrics  
- Log-scale funding distribution  
- Funding comparison by startup status  
- Industry failure rate comparison  
- Startup formation trend analysis  
- Integrated insight summary  

---


## Conclusion

Startup success is influenced by funding intensity, industry structure, and ecosystem maturity. While capital improves exit probability, sustainable success depends on multiple structural factors beyond funding alone.
