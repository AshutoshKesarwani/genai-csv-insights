import streamlit as st
import pandas as pd
from analysis import analyze_csv
from insights import generate_insights

st.set_page_config(page_title="AI CSV Insights", layout="wide")
st.title("📊 Auto-Insight Generator")
st.write("Upload a CSV and get an AI-generated business summary.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview")
    st.dataframe(df.head())

    if st.button("Generate Insights"):
        with st.spinner("Analyzing data..."):
            summary = analyze_csv(df)
            insights = generate_insights(summary)

        st.subheader("AI-Generated Insights")
        st.write(insights)

        with st.expander("View raw statistical summary"):
            st.json(summary)