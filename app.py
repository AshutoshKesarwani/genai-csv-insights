import streamlit as st
import pandas as pd
from analysis import analyze_csv
from insights import generate_insights

st.set_page_config(
    page_title="Auto-Insight Generator",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    h1 {
        font-weight: 700;
    }
    .stButton>button {
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Auto-Insight Generator")
st.caption("Upload a CSV and get an AI-generated business summary — powered by LLM inference.")
st.divider()

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", f"{df.shape[0]:,}")
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))
    
    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    if st.button("✨ Generate Insights", type="primary"):
        with st.spinner("Analyzing your data..."):
            summary = analyze_csv(df)
            insights = generate_insights(summary)

        st.divider()
        st.subheader("AI-Generated Insights")
        st.markdown(insights)

        with st.expander("View raw statistical summary"):
            st.json(summary)