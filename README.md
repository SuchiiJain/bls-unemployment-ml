# U.S. Unemployment Forecasting using BLS Data

## Overview
This project analyzes and forecasts the U.S. unemployment rate using official data from the U.S. Bureau of Labor Statistics (BLS). The goal is to demonstrate an end-to-end analytics and machine learning workflow, from data ingestion via a public API to feature engineering, modeling, and evaluation.

The project is designed to reflect real-world analyst and ML workflows used in business, operations, and economic decision-making.

---

## Problem Statement
Accurately forecasting unemployment trends is critical for workforce planning, policy analysis, and economic risk assessment. This project builds forecasting models using historical unemployment data to identify patterns, seasonality, and macroeconomic shifts.

---

## Data Source
- U.S. Bureau of Labor Statistics (BLS) Public API  
- Dataset: Current Population Survey (CPS)  
- Series ID: LNS14000000 (U.S. Unemployment Rate, Monthly, Seasonally Adjusted)

---

## Tech Stack
- Python
- pandas, numpy
- scikit-learn
- statsmodels
- matplotlib, seaborn
- Jupyter Notebook
- Git / GitHub

---

## Project Structure

---

## Methodology
1. Pulled official labor market data using the BLS Public API
2. Cleaned and transformed raw time-series data
3. Performed exploratory data analysis (EDA)
4. Engineered lag, rolling average, and calendar features
5. Trained and evaluated multiple forecasting models
6. Compared performance using MAE

---

## Models Evaluated
- Naive Lag-Based Baseline
- Linear Regression
- Random Forest Regressor

The Random Forest model achieved the lowest error and best captured non-linear trends and seasonal patterns.

---

## Key Insights
- Unemployment exhibits strong recession-driven spikes and recovery cycles
- Lagged unemployment values are the strongest predictors
- Rolling averages improve model stability and performance
- Ensemble models outperform linear baselines on recent data

---

## Business Applications
- Workforce planning and hiring forecasts
- Economic risk monitoring
- Policy and labor market analysis
- Strategic planning and budgeting

---

## Future Improvements
- Incorporate CPI and wage data as additional features
- Extend forecasts to multi-step horizons
- Deploy interactive dashboard using Streamlit

Streamlit app link: https://bls-unemployment-ml-kwlfran5chhbehenhvv6wq.streamlit.app/
