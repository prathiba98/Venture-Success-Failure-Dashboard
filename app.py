import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Venture Success & Failure Dashboard",
    layout="wide"
)

st.title("Venture Success & Failure Dashboard")
st.markdown("An interactive analysis of global startup success, funding, survival trends, and industry risk.")

# -------------------------
# Load Data
# -------------------------
df = pd.read_csv("clean_startup_data.csv")
  
# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("Filters")

year_range = st.sidebar.slider(
    "Select Founded Year Range",
    int(df['founded_year'].min()),
    int(df['founded_year'].max()),
    (2000, int(df['founded_year'].max()))
)

industry_filter = st.sidebar.multiselect(
    "Select Industry",
    options=sorted(df['primary_category'].unique()),
    default=None
)

country_filter = st.sidebar.multiselect(
    "Select Country",
    options=sorted(df['country_code'].unique()),
    default=None
)

# Apply filters
filtered_df = df[
    (df['founded_year'] >= year_range[0]) &
    (df['founded_year'] <= year_range[1])
]

if industry_filter:
    filtered_df = filtered_df[filtered_df['primary_category'].isin(industry_filter)]

if country_filter:
    filtered_df = filtered_df[filtered_df['country_code'].isin(country_filter)]

# -------------------------
# KPI Section
# -------------------------
st.subheader("Key Metrics")

total_startups = len(filtered_df)
total_failed = filtered_df['failed'].sum()
failure_rate = (total_failed / total_startups) * 100 if total_startups > 0 else 0
avg_funding = filtered_df['funding_total_usd'].median()
avg_survival = filtered_df['startup_age_years'].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Startups", f"{total_startups:,}")
col2.metric("Failure Rate", f"{failure_rate:.2f}%")
col3.metric("Median Funding (USD)", f"${avg_funding:,.0f}")
col4.metric("Avg Survival Years", f"{avg_survival:.1f}")

# -------------------------
# Funding Distribution
# -------------------------
st.subheader("Funding Distribution (Log Scale)")

fig_funding = px.histogram(
    filtered_df,
    x=np.log1p(filtered_df['funding_total_usd']),
    nbins=40,
    labels={'x': 'Log Funding'}
)

st.plotly_chart(fig_funding, use_container_width=True)

# -------------------------
# Funding by Status
# -------------------------
st.subheader("Funding by Startup Status")

fig_status = px.box(
    filtered_df,
    x='status',
    y='funding_total_usd',
    log_y=True
)

st.plotly_chart(fig_status, use_container_width=True)

# -------------------------
# Industry Failure Rates
# -------------------------
st.subheader("Top Industries by Failure Rate")

industry_stats = (
    filtered_df.groupby('primary_category')
    .agg(
        total=('name', 'count'),
        failure_rate=('failed', 'mean')
    )
)

industry_stats = industry_stats[industry_stats['total'] >= 50]
top_failure = industry_stats.sort_values('failure_rate', ascending=False).head(10)

fig_industry = px.bar(
    top_failure.reset_index(),
    x='primary_category',
    y='failure_rate',
    labels={'primary_category': 'Industry', 'failure_rate': 'Failure Rate'}
)

st.plotly_chart(fig_industry, use_container_width=True)

# -------------------------
# Startup Formation Trend
# -------------------------
st.subheader("Startups Founded Per Year")

yearly = filtered_df['founded_year'].value_counts().sort_index()

fig_year = px.line(
    x=yearly.index,
    y=yearly.values,
    labels={'x': 'Year', 'y': 'Number of Startups'}
)

st.plotly_chart(fig_year, use_container_width=True)

# -------------------------
# Final Summary Section
# -------------------------
st.subheader("Key Insights Summary")

st.markdown("""
###  Ecosystem Overview
- Startup formation accelerated exponentially after 2000, reflecting the rise of the digital economy and venture capital expansion.
- The apparent recent decline may reflect incomplete reporting rather than actual slowdown.

###  Funding Dynamics
- Startup funding is highly right-skewed, with a small number of ventures capturing disproportionately large investments.
- Log transformation reveals a more structured funding distribution.
- IPO and acquired startups demonstrate significantly higher median funding compared to closed startups, indicating strong capital-performance linkage.

###  Survival Patterns
- Most startups cluster within early operational years, highlighting high ecosystem volatility.
- While higher funding shows a weak positive relationship with survival years, capital alone does not guarantee longevity.

###  Industry Risk Variation
- Failure rates vary across industries, with consumer-facing and promotion-driven sectors showing relatively higher failure proportions.
- Risk is not uniformly distributed across sectors, indicating structural sustainability differences between business models.

---

**Conclusion:**  
Startup success is influenced by funding intensity, industry structure, and ecosystem dynamics. While capital improves exit probability, long-term survival depends on multiple structural factors beyond funding alone.
""")
