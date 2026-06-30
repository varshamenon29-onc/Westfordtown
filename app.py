import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Westford 2050 Energy Hub",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: 800;
    color: #0b2e63;
}
.subtitle {
    font-size: 20px;
    color: #2e7d32;
    font-weight: 600;
}
.card {
    padding: 20px;
    border-radius: 14px;
    background-color: #f6fbf7;
    border: 1px solid #d7eadb;
}
.metric-label {
    font-size: 16px;
    color: #555;
}
.metric-value {
    font-size: 30px;
    font-weight: 800;
    color: #0b2e63;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------

data = pd.DataFrame({
    "hour": ["6 AM", "9 AM", "12 PM", "3 PM", "6 PM", "9 PM"],
    "solar_kw": [100, 600, 1100, 900, 300, 0],
    "wind_kw": [220, 180, 150, 200, 260, 300],
    "town_demand_kw": [1200, 1700, 1900, 2100, 2300, 1800],
    "data_center_kw": [500, 700, 900, 850, 950, 700]
})

latest = data.iloc[-1]

# ---------------- SIDEBAR ----------------

st.sidebar.title("🌱 Westford 2050")
st.sidebar.markdown("### AI-Powered Community Energy Hub")
st.sidebar.write("Smarter energy. Stronger community. Sustainable future.")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "AI Decisions", "Community Impact", "Project Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Mission: Use AI to balance clean energy, battery storage, data demand, and community needs."
)

# ---------------- HEADER ----------------

st.markdown('<div class="big-title">Westford 2050: AI-Powered Community Energy Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Reliable. Affordable. Equitable. Sustainable.</div>', unsafe_allow_html=True)
st.write("A simple simulator showing how AI can manage clean energy, batteries, data centers, and community demand.")

# ---------------- CONTROLS ----------------

battery = st.slider("Battery Level (%)", 0, 100, 65)
emergency = st.checkbox("Emergency Mode")

renewable_power = latest["solar_kw"] + latest["wind_kw"]
total_demand = latest["town_demand_kw"] + latest["data_center_kw"]

if emergency:
    decision = "🚨 Emergency Mode: prioritize police, fire, schools, medical services, and shelters."
elif renewable_power >= total_demand:
    decision = "✅ Use clean energy now and store extra power in the battery."
elif battery > 40:
    decision = "🔋 Use battery support and reduce grid electricity."
else:
    decision = "⚡ Use grid power and delay non-urgent computing tasks."

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.subheader("Current Energy Snapshot")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("### ☀️ Solar Power")
        st.metric("Available", f"{latest['solar_kw']} kW")

    with col2:
        st.markdown("### 🌬️ Wind Power")
        st.metric("Available", f"{latest['wind_kw']} kW")

    with col3:
        st.markdown("### 🔋 Battery")
        st.metric("Stored", f"{battery}%")
        st.progress(battery)

    with col4:
        st.markdown("### 🏢 Data Center")
        st.metric("Demand", f"{latest['data_center_kw']} kW")

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:
        st.subheader("Energy Forecast Today")
        chart_data = data.set_index("hour")
        st.line_chart(chart_data[["solar_kw", "wind_kw", "town_demand_kw", "data_center_kw"]])

    with right:
        st.subheader("AI Decision")
        st.success(decision)

        st.markdown("### Estimated Impact")
        st.metric("Carbon Savings", "38%")
        st.metric("Cost Savings", "$4.8M/year")
        st.metric("Heat Reused", "Up to 90%")

    st.markdown("---")

    st.subheader("Energy Mix Right Now")

    energy_mix = pd.DataFrame({
        "Source": ["Solar", "Wind", "Battery", "Grid"],
        "Power": [latest["solar_kw"], latest["wind_kw"], 200, 120]
    })

    fig = px.pie(
        energy_mix,
        names="Source",
        values="Power",
        hole=0.45,
        title="Current Energy Sources"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- AI DECISIONS ----------------

elif page == "AI Decisions":

    st.subheader("How the AI Thinks")

    st.write("The AI looks at multiple signals and makes the best energy decision every few minutes.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Data Inputs
        - 🌦️ Weather forecast
        - ☀️ Solar production
        - 🌬️ Wind production
        - 🔋 Battery level
        - ⚡ Electricity price
        - 🏘️ Town demand
        - 🏢 Data center demand
        - 🚨 Emergency alerts
        """)

    with col2:
        st.markdown("""
        ### AI Decisions
        - Use clean energy first
        - Store extra energy
        - Use batteries during high demand
        - Delay non-urgent computing
        - Prioritize emergency services
        - Reduce costs and emissions
        """)

    st.info(decision)

    st.subheader("Decision Simulator")

    if emergency:
        st.error("Emergency services are prioritized.")
    elif battery < 25:
        st.warning("Battery is low. AI will save battery for emergencies.")
    elif battery > 70:
        st.success("Battery is strong. AI can use stored power to reduce grid demand.")
    else:
        st.info("Battery is moderate. AI balances renewable energy, battery, and grid power.")

# ---------------- COMMUNITY IMPACT ----------------

elif page == "Community Impact":

    st.subheader("Who Benefits?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🏫 Schools
        - Reliable technology
        - Lower energy costs
        - Cleaner power
        """)

        st.markdown("""
        ### 🏠 Homes
        - Lower bills
        - More reliable grid
        - Cleaner community
        """)

    with col2:
        st.markdown("""
        ### 🚒 Public Safety
        - Backup energy during storms
        - Priority power for police and fire
        - Stronger emergency response
        """)

        st.markdown("""
        ### 🏢 Businesses
        - Reliable computing
        - Lower operating costs
        - Green innovation jobs
        """)

    with col3:
        st.markdown("""
        ### 🌱 Environment
        - Lower emissions
        - Less wasted heat
        - More renewable energy
        """)

        st.markdown("""
        ### 🚗 EV Drivers
        - Cleaner charging
        - More chargers
        - Smarter energy timing
        """)

    st.markdown("---")

    st.subheader("Heat Recycling Idea")

    st.success(
        "Waste heat from the data center could help warm schools, greenhouses, senior centers, community pools, or sidewalks in winter."
    )

# ---------------- PROJECT SUMMARY ----------------

elif page == "Project Summary":

    st.subheader("Project Summary")

    st.markdown("""
    ## Problem
    By 2050, communities will need more electricity because of AI, cloud computing, electric vehicles, homes, schools, and businesses.

    ## Solution
    Build an AI-powered community energy hub that connects renewable energy, battery storage, a small data center, heat recycling, and emergency backup power.

    ## Why It Matters
    This creates a system that is:
    - Reliable
    - Affordable
    - Equitable
    - Sustainable

    ## What This App Shows
    This simulator demonstrates how AI can make energy decisions using solar power, wind power, battery level, town demand, and data center demand.
    """)

    st.markdown("### Final Pitch Line")
    st.success("If it works in Westford, it can work in every town.")
