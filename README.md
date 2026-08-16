# 📊 AI CSV Insight Generator

Upload any CSV and get an AI-generated, plain-English business summary — trends, outliers, and actionable recommendations — powered by LLM inference.

🔗 **Live app:** https://genai-csv-insights-bjhfbcx7eqgv4rqmsnjwwc.streamlit.app

## How it works
1. Upload a CSV file
2. The app computes statistical summaries (distributions, correlations, outlier detection using IQR)
3. These stats are passed to an LLM (via Groq API, Llama 3.3) which generates a business-friendly summary and recommendations

## Tech stack
- Python, pandas (data analysis)
- Groq API (LLM inference)
- Streamlit (UI + deployment)

## Example use case
Tested on an SBA loan approvals dataset (~896K records) — generated insights on loan trends, borrower patterns, and risk indicators.