"""
NL Team Trends - Interactive Dashboard
Run: pip install streamlit plotly pandas numpy seaborn
Then: streamlit run app.py
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="NL Team Trends Dashboard", layout="wide")
st.title("National League Team Trends Dashboard")
st.markdown("Explore historical NL franchise performance from 1876 to 2025.")

@st.cache_data
def load_data():
    all_time = pd.read_csv("data/nl_all_time_records.csv")
    pennants = pd.read_csv("data/nl_pennant_winners_recent.csv")
    trends = pd.read_csv("data/nl_championship_trends.csv")
    records = pd.read_csv("data/nl_notable_records.csv")
    return all_time, pennants, trends, records

all_time, pennants, trends, records = load_data()

st.header("All-Time Franchise Winning Percentage")
fig1 = px.bar(all_time.sort_values("win_pct", ascending=True),
              x="win_pct", y="franchise", color="division",
              title="NL Win% by Franchise (through 2025)",
              labels={"win_pct": "Winning %", "franchise": "Franchise"})
st.plotly_chart(fig1, use_container_width=True)

st.header("World Series Titles")
ws_data = all_time[all_time["ws_titles"] > 0].sort_values("ws_titles", ascending=True)
fig2 = px.bar(ws_data, x="ws_titles", y="franchise", color="division",
              title="NL World Series Championships",
              labels={"ws_titles": "WS Titles", "franchise": "Franchise"})
st.plotly_chart(fig2, use_container_width=True)

st.header("Championship Trends by Era")
st.table(trends)

st.header("NL Pennant Winners (1995-2025)")
fig3 = px.bar(pennants.sort_values("year"),
              x="year", y="win_pct", color="ws_result",
              title="Pennant Winners & WS Results",
              labels={"win_pct": "Win %", "year": "Season"})
st.plotly_chart(fig3, use_container_width=True)

st.header("Notable NL Records")
st.table(records)
