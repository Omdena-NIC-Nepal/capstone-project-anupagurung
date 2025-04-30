import streamlit as st
import pandas as pd
import numpy as np
from data_utils import load_datasets
from Visualizations import (
    plot_temperature_trend,
    plot_precipitation_trend,
    plot_station_distribution
)
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("📊 Climate Data Exploration")

    try:
        daily, stations, rainfall, temps = load_datasets()
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return

    with st.sidebar:
        district = st.selectbox("Select District", sorted(daily["District"].dropna().unique()))

    st.subheader(f"📈 Climate Trends for {district}")
    st.plotly_chart(plot_temperature_trend(daily, district), use_container_width=True)
    st.plotly_chart(plot_precipitation_trend(daily, district), use_container_width=True)

    st.subheader("🗺️ Meteorological Station Distribution")
    st.plotly_chart(plot_station_distribution(stations), use_container_width=True)

    # ➕ Additional Visualizations
    st.subheader("🌦️ Temperature vs Precipitation Over Time")
    district_data = daily[daily["District"] == district]
    fig1 = px.line(district_data, x="Date", y=["Temp_2m", "Precip"], labels={"value": "Measurement", "variable": "Metric"})
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📅 Monthly Average Temperature Heatmap")
    daily["Date"] = pd.to_datetime(daily["Date"])
    daily["Month"] = daily["Date"].dt.month
    temp_heatmap = daily[daily["District"] == district].groupby(["Year", "Month"])["Temp_2m"].mean().unstack()
    fig2, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(temp_heatmap, cmap="YlGnBu", ax=ax)
    st.pyplot(fig2)

    st.subheader("☔ Total Rainfall by District (Bar Chart)")
    rainfall_sum = daily.groupby("District")["Precip"].sum().sort_values(ascending=False)
    fig3 = px.bar(rainfall_sum, title="Total Precipitation by District", labels={"value": "Precipitation", "index": "District"})
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("📊 Annual Temperature Comparison (Line)")
    if "Year" not in daily.columns:
        daily["Year"] = pd.to_datetime(daily["Date"]).dt.year
    annual_temp = daily.groupby(["District", "Year"])["Temp_2m"].mean().reset_index()
    fig4 = px.line(annual_temp[annual_temp["District"] == district], x="Year", y="Temp_2m", title="Annual Avg Temperature")
    st.plotly_chart(fig4, use_container_width=True)
