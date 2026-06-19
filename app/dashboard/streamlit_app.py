import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
from app.dashboard.api_client import get_alerts, get_incidents

st.set_page_config(page_title="SOC Dashboard", layout="wide")

st.title("🛡️ SOAR SOC Dashboard (MVP)")

# Auto refresh toggle
#auto_refresh = st.sidebar.checkbox("Auto Refresh (5s)", value=True)
autorefresh = st.sidebar.checkbox("Auto Refresh (5s)", value=True)
if autorefresh:
    st_autorefresh(interval=5000, key="refresh")

# Load data
alerts = get_alerts()
incidents = get_incidents()

# Convert to DataFrame
alerts_df = pd.DataFrame(alerts)
incidents_df = pd.DataFrame(incidents)

# =========================
# 📊 METRICS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Total Alerts", len(alerts_df))
col2.metric("Total Incidents", len(incidents_df))

high_sev = len(alerts_df[alerts_df["severity"] == "high"]) if not alerts_df.empty else 0
col3.metric("High Severity Alerts", high_sev)

st.divider()

# =========================
# 🚨 ALERTS SECTION
# =========================
st.subheader("🚨 Alerts")

if not alerts_df.empty:
    st.dataframe(alerts_df, use_container_width=True)

    st.bar_chart(alerts_df["severity"].value_counts())
else:
    st.info("No alerts generated yet.")

st.divider()

# =========================
# 📁 INCIDENTS SECTION
# =========================
st.subheader("📁 Incidents")

if not incidents_df.empty:
    st.dataframe(incidents_df, use_container_width=True)

    # filter by IP
    ips = incidents_df["source_ip"].unique().tolist()
    selected_ip = st.selectbox("Filter by Source IP", ["All"] + ips)

    if selected_ip != "All":
        filtered = incidents_df[incidents_df["source_ip"] == selected_ip]
        st.write(filtered)

else:
    st.info("No incidents created yet.")

st.divider()

# =========================
# 🔍 QUICK ANALYTICS
# =========================
st.subheader("📈 Threat Overview")

if not alerts_df.empty:
    st.write("Top Source IPs causing alerts:")
    st.bar_chart(alerts_df["source_ip"].value_counts())

st.caption("SOAR MVP Dashboard - SOC Simulation Mode")