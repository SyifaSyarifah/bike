# Nama          : Syifa Syarifah
# Email         : m129d4kx1804@bangkit.academy
# Id Dicoding   : syifa_syarifah

# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
@st.cache
def load_data():
    data = pd.read_csv("dataset/day.csv")
    return data

# Sidebar
st.sidebar.title("Informasi:")
st.sidebar.text("Nama: Syifa Syarifah Nurul Yasin Mulyoadi")
st.sidebar.text("Email: m129d4kx1804@bangkit.academy")
st.sidebar.text("Id Dicoding   : syifa_syarifah")

# Load Data
data = load_data()

# Page Title
st.title("Bike Share Dashboard")

# Show Dataset
if st.checkbox("Tampilkan Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Summary Statistics
if st.checkbox("Tampilkan Statistik Ringkasan"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Visualizations
st.sidebar.title("Visualisasi Data")

# Season-wise Bike Share Count
season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
data["season_label"] = data["season"].map(season_mapping)
season_count = data.groupby("season_label")["cnt"].sum().reset_index()
fig_season_count = px.bar(season_count, x="season_label", y="cnt", title="Season-wise Bike Share Count")
st.plotly_chart(fig_season_count, use_container_width=True)

# Weather Situation-wise Bike Share Count
weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
fig_weather_count = px.bar(weather_count, x="weathersit", y="cnt", title="Weather Situation-wise Bike Share Count")
st.plotly_chart(fig_weather_count, use_container_width=True)

# Hourly Bike Share Count
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(hourly_count, x="hr", y="cnt", title="Hourly Bike Share Count")
st.plotly_chart(fig_hourly_count, use_container_width=True)

# Humidity vs. Bike Share Count
fig_humidity_chart = px.scatter(data, x="hum", y="cnt", title="Humidity vs. Bike Share Count")
st.plotly_chart(fig_humidity_chart, use_container_width=True)

# Wind Speed vs. Bike Share Count
fig_wind_speed_chart = px.scatter(data, x="windspeed", y="cnt", title="Wind Speed vs. Bike Share Count")
st.plotly_chart(fig_wind_speed_chart, use_container_width=True)

# Temperature vs. Bike Share Count
fig_temp_chart = px.scatter(data, x="temp", y="cnt", title="Temperature vs. Bike Share Count")
st.plotly_chart(fig_temp_chart, use_container_width=True)
