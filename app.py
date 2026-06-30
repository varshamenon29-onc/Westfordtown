import streamlit as st
import pandas as pd

st.set_page_config(page_title="Westford 2050 Energy Hub", layout="wide")

st.title("Westford 2050: AI-Powered Community Energy Hub")
st.write("A simple simulator showing how AI can manage clean energy, batteries, and community demand.")

data = pd.read_csv("data/sample_energy_data.csv")

st.subheader("Energy Forecast")
st.line_chart(
    data,
    x="hour",
    y=["solar_kw", "wind_kw", "town_demand_kw", "data_center_kw"]
)

battery = st.slider("Battery Level (%)", 0, 100, 65)
emergency = st.checkbox("Emergency Mode")

latest = data.iloc[-1]

renewable_power = latest["solar_kw"] + latest["wind_kw"]
total_demand = latest["town_demand_kw"] + latest["data_center_kw"]

st.subheader("Current Energy Snapshot")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Solar Power", f"{latest['solar_kw']} kW")
col2.metric("Wind Power", f"{latest['wind_kw']} kW")
col3.metric("Town Demand", f"{latest['town_demand_kw']} kW")
col4.metric("Data Center Demand", f"{latest['data_center_kw']} kW")

st.subheader("AI Decision")

if emergency:
    decision = "Emergency Mode: prioritize police, fire, schools, medical services, and shelters."
elif renewable_power >= total_demand:
    decision = "Use clean energy now and store extra power in the battery."
elif battery > 40:
    decision = "Use battery support and reduce grid electricity."
else:
    decision = "Use grid power and delay non-urgent computing tasks."

st.success(decision)

st.subheader("Estimated Impact")
col5, col6, col7 = st.columns(3)

col5.metric("Carbon Savings", "38%")
col6.metric("Cost Savings", "$4.8M/year")
col7.metric("Heat Reused", "Up to 90%")
