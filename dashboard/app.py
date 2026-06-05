import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    page_icon="🏪",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🏪 Store Intelligence Dashboard")

st.caption(
    "Real-time retail analytics for customer movement, occupancy, dwell time, and zone transitions"
)

# --------------------------------------------------
# Fetch Metrics
# --------------------------------------------------

try:
    response = requests.get(
        "http://127.0.0.1:8000/metrics"
    )

    metrics = response.json()

    st.success(
    f"Store ID: {metrics['store_id']} | Backend Connected"
)

except Exception:

    st.error("Backend Not Running")

    st.stop()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Entries",
        metrics["total_entries"]
    )

with col2:
    st.metric(
        "🚪 Total Exits",
        metrics["total_exits"]
    )

with col3:
    st.metric(
        "📈 Peak Occupancy",
        metrics["peak_occupancy"]
    )

with col4:
    st.metric(
        "🏬 Final Occupancy",
        metrics["final_occupancy"]
    )

# --------------------------------------------------
# Dwell Time Chart
# --------------------------------------------------

st.divider()

st.subheader("Average Dwell Time by Zone")

dwell_data = metrics["avg_dwell_time"]

dwell_df = pd.DataFrame(
    {
        "Zone": list(dwell_data.keys()),
        "Average Dwell Time": list(dwell_data.values())
    }
)

fig = px.bar(
    dwell_df,
    x="Zone",
    y="Average Dwell Time",
    title="Average Dwell Time",
    labels={
        "Average Dwell Time": "Seconds"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# Zone Transition Chart
# --------------------------------------------------

st.divider()

st.subheader("Zone Transition Distribution")

transition_data = metrics["zone_transitions"]

transition_df = pd.DataFrame(
    {
        "Transition": list(
            transition_data.keys()
        ),
        "Count": list(
            transition_data.values()
        )
    }
)

fig2 = px.pie(
    transition_df,
    names="Transition",
    values="Count",
    hole=0.4,
    title="Zone Transition Share"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

st.caption(
    "Store Intelligence Platform | Computer Vision Analytics Dashboard | Built with FastAPI, Streamlit, YOLOv8 and ByteTrack"
)
