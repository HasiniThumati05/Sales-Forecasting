# 📊 Sales Forecasting using Machine Learning & Time Series Analysis

## 📌 Project Overview

This project predicts future sales using historical sales data. It includes complete data preprocessing, exploratory data analysis (EDA), time series forecasting, anomaly detection, customer segmentation, and an interactive Streamlit dashboard.

---

## 🎯 Objectives

- Analyze historical sales trends
- Forecast future sales
- Detect sales anomalies
- Segment customers using K-Means
- Compare forecasting models
- Build an interactive dashboard

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost
- Streamlit

---

## 📂 Project Structure

```
SalesForecasting_Bhavani/
│
├── charts/
├── analysis.ipynb
├── app.py
├── cleaned_sales.csv
├── train.csv
├── vgsales.csv
├── requirements.txt
└── README.md
```

---

## 📊 Project Workflow

### Task 1
- Data Loading
- Data Cleaning
- Feature Engineering

### Task 2
- Exploratory Data Analysis
- Sales Trend Analysis
- Category Analysis
- Region Analysis

### Task 3
- Time Series Forecasting
- SARIMA Model
- Prophet Model
- XGBoost Model
- Model Comparison

### Task 4
- Category and Region Analysis

### Task 5
- Anomaly Detection

### Task 6
- Customer Segmentation using K-Means

### Task 7
- Streamlit Dashboard

---

## 📈 Models Used

- SARIMA
- Prophet
- XGBoost

---

## 📊 Model Performance

| Model | MAE | RMSE | MAPE |
|-------|------|-------|-------|
| SARIMA | 18031.40 | 19009.18 | 18.97% |
| Prophet | 20250.79 | 22318.41 | 21.86% |
| XGBoost | 13915.32 | 18893.85 | 13.29% |

### 🏆 Best Model

**XGBoost** achieved the lowest forecasting error and delivered the best overall performance.

---

## 📌 Business Insights

- Technology category generated the highest sales.
- West region recorded the maximum revenue.
- Sales showed clear seasonal patterns.
- Isolation Forest detected unusual sales spikes.
- K-Means identified three customer segments.
- XGBoost produced the most accurate forecasts.

---

## 🚀 How to Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
streamlit run app.py
```

---

## 📷 Dashboard

The dashboard includes

- Dataset Preview
- Monthly Sales Trend
- Category-wise Sales
- Region-wise Sales
- Model Comparison
- Business Insights

---

## 👩‍💻 Author

**Jana Surya Ganga Bhavani**

B.Tech Final Year (Information Technology)

Machine Learning & Data Science Enthusiast