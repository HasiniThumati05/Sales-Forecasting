import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Sales Forecasting Dashboard")
st.write("Machine Learning & Time Series Forecasting Project")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_sales.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="mixed"
    )

    return df

sales = load_data()

# -----------------------------
# Dataset Preview
# -----------------------------
st.header("Dataset Preview")
st.dataframe(sales.head())

# -----------------------------
# Monthly Sales Trend
# -----------------------------
st.header("Monthly Sales Trend")

monthly_sales = (
    sales.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
    .sum()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(
    monthly_sales["Order Date"],
    monthly_sales["Sales"],
    marker="o"
)
ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
st.pyplot(fig)

# -----------------------------
# Category-wise Sales
# -----------------------------
st.header("Category-wise Sales")

category_sales = sales.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots()

category_sales.plot(
    kind="bar",
    ax=ax,
    color=["skyblue","orange","green"]
)

ax.set_ylabel("Sales")
st.pyplot(fig)

# -----------------------------
# Region-wise Sales
# -----------------------------
st.header("Region-wise Sales")

region_sales = sales.groupby("Region")["Sales"].sum()

fig, ax = plt.subplots()

region_sales.plot(
    kind="bar",
    ax=ax,
    color="purple"
)

ax.set_ylabel("Sales")
st.pyplot(fig)

# -----------------------------
# Model Comparison
# -----------------------------
st.header("Forecasting Model Comparison")

comparison = pd.DataFrame({
    "Model":["SARIMA","Prophet","XGBoost"],
    "MAE":[18031.40,20250.79,13915.32],
    "RMSE":[19009.18,22318.41,18893.85],
    "MAPE":[18.97,21.86,13.29]
})

st.dataframe(comparison)

st.success("🏆 Best Model: XGBoost")

# -----------------------------
# Business Insights
# -----------------------------
st.header("Business Insights")

st.markdown("""
- 📈 Technology category showed strong sales growth.
- 🌍 West region recorded the highest sales.
- 🚨 Isolation Forest detected unusual sales spikes.
- 👥 K-Means identified three customer segments.
- 🏆 XGBoost achieved the best forecasting accuracy.
""")

st.success("Project Completed Successfully ✅")