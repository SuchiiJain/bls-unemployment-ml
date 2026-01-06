import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="U.S. Unemployment Forecast Dashboard",
    layout="wide"
)

# -----------------------
# Load Data
# -----------------------
@st.cache_data
def load_data():
    hist = pd.read_csv("data/processed/unemployment_rate.csv")
    hist["date"] = pd.to_datetime(hist["date"])
    
    try:
        forecast = pd.read_csv("data/processed/12_month_forecast.csv")
    except FileNotFoundError:
        forecast = None
        
    return hist, forecast

df, forecast_df = load_data()

# -----------------------
# Header
# -----------------------
st.title("📊 U.S. Unemployment Rate Dashboard")
st.markdown(
    """
    **Data Source:** U.S. Bureau of Labor Statistics (BLS)  
    **Purpose:** Analyze historical unemployment trends and visualize model-based forecasts.
    """
)

# -----------------------
# Sidebar Filters
# -----------------------
st.sidebar.header("Filters")

min_year = df["date"].dt.year.min()
max_year = df["date"].dt.year.max()

year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

filtered_df = df[
    (df["date"].dt.year >= year_range[0]) &
    (df["date"].dt.year <= year_range[1])
]

# -----------------------
# KPI Metrics
# -----------------------
latest_rate = df.iloc[-1]["unemployment_rate"]
avg_rate = filtered_df["unemployment_rate"].mean()
max_rate = filtered_df["unemployment_rate"].max()

col1, col2, col3 = st.columns(3)

col1.metric("Latest Unemployment Rate (%)", f"{latest_rate:.2f}")
col2.metric("Average Rate (Selected Period)", f"{avg_rate:.2f}")
col3.metric("Peak Rate (Selected Period)", f"{max_rate:.2f}")

# -----------------------
# Trend Chart
# -----------------------
st.subheader("📈 Unemployment Rate Over Time")

fig, ax = plt.subplots()
ax.plot(filtered_df["date"], filtered_df["unemployment_rate"])
ax.set_xlabel("Year")
ax.set_ylabel("Unemployment Rate (%)")
ax.set_title("Historical U.S. Unemployment Rate")

st.pyplot(fig)

# -----------------------
# Forecast Section
# -----------------------
st.subheader("🔮 12-Month Forecast")

if forecast_df is not None:
    st.markdown(
        """
        The forecast below is generated using a Random Forest model trained on
        lagged and rolling unemployment features.
        """
    )

    forecast_df["month_ahead"] = forecast_df["month_ahead"].astype(int)

    fig2, ax2 = plt.subplots()
    ax2.plot(
        forecast_df["month_ahead"],
        forecast_df["predicted_unemployment_rate"],
        marker="o"
    )
    ax2.set_xlabel("Months Ahead")
    ax2.set_ylabel("Predicted Unemployment Rate (%)")
    ax2.set_title("12-Month Unemployment Forecast")

    st.pyplot(fig2)

    st.dataframe(forecast_df)
else:
    st.warning("Forecast data not found. Run the modeling notebook to generate forecasts.")

# -----------------------
# Insights Section
# -----------------------
st.subheader("📌 Key Insights")

st.markdown(
    """
    - Unemployment shows strong spikes during economic downturns
    - Lagged unemployment values are the strongest predictors
    - Rolling averages help smooth short-term volatility
    - Ensemble models outperform linear baselines
    """
)

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.markdown(
    "Built with Python, Streamlit, and official BLS data for analytics and forecasting."
)
