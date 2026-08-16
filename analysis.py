import pandas as pd

def analyze_csv(df: pd.DataFrame) -> dict:
    summary = {}
    summary["shape"] = df.shape
    summary["columns"] = list(df.columns)
    summary["dtypes"] = df.dtypes.astype(str).to_dict()
    summary["missing_values"] = df.isnull().sum().to_dict()

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] > 0:
        summary["describe"] = numeric_df.describe().to_dict()
    else:
        summary["describe"] = {}

    if numeric_df.shape[1] >= 2:
        summary["correlations"] = numeric_df.corr().round(2).to_dict()
    else:
        summary["correlations"] = {}

    outliers = {}
    for col in numeric_df.columns:
        q1, q3 = numeric_df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        count = ((numeric_df[col] < lower) | (numeric_df[col] > upper)).sum()
        outliers[col] = int(count)
    summary["outlier_counts"] = outliers

    return summary