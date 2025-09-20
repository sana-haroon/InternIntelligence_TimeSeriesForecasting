import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
import matplotlib.pyplot as plt

st.title("🌦 Time Series Forecasting of Weather Data")

# ================= Upload CSV =================
uploaded_file = st.file_uploader("📂 Upload your weather CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["Date_Time"] = pd.to_datetime(df["Date_Time"], errors="coerce")
    df = df.dropna(subset=["Date_Time"])  # drop invalid dates

    # ================= Location & Target Selection =================
    location = st.selectbox("Choose Location", df["Location"].unique())
    target = st.selectbox("Choose Target Variable", ["Temperature_C", "Humidity_pct", "Precipitation_mm", "Wind_Speed_kmh"])

    # Filter by location
    df_loc = df[df["Location"] == location].copy()

    # 🛠 Fix duplicates → group by date
    df_loc = df_loc.groupby(df_loc["Date_Time"].dt.date).mean(numeric_only=True)
    df_loc.index = pd.to_datetime(df_loc.index)

    # Select target
    ts = df_loc[[target]].asfreq("D").interpolate()

    st.write(f"### 📊 Data Preview for {location} - {target}")
    st.line_chart(ts)

    # =============== ARIMA MODEL ===============
    st.subheader("🔮 ARIMA Forecast")
    try:
        model = ARIMA(ts, order=(5, 1, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=30)

        fig, ax = plt.subplots()
        ts.plot(ax=ax, label="Historical")
        forecast.plot(ax=ax, label="Forecast", color="red")
        ax.legend()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"ARIMA Error: {e}")

    # =============== PROPHET MODEL ===============
    st.subheader("🔮 Prophet Forecast")
    try:
        prophet_df = ts.reset_index()
        prophet_df.columns = ["ds", "y"]  # ✅ Fix Prophet column names

        model_p = Prophet()
        model_p.fit(prophet_df)

        future = model_p.make_future_dataframe(periods=30)
        forecast_p = model_p.predict(future)

        fig2 = model_p.plot(forecast_p)
        st.pyplot(fig2)
    except Exception as e:
        st.error(f"Prophet Error: {e}")

else:
    st.info("👆 Please upload a CSV file to start.")
