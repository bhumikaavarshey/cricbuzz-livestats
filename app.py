import streamlit as st
import plotly.express as px
from database import run_query
from api import get_live_matches
st.set_page_config(page_title="Cricbuzz LiveStats",page_icon="🏏",layout="wide")
st.title("🏏 Cricbuzz LiveStats")
st.caption("Real-Time Cricket Insights & SQL-Based Analytics")
if get_live_matches().get("demo_mode"): st.info("Demo mode: API key can be added in api.py for live API requests.")
p=run_query("SELECT * FROM players"); m=run_query("SELECT * FROM matches")
a,b,c,d=st.columns(4); a.metric("Matches",len(m)); b.metric("Players",len(p)); c.metric("Total Runs",f"{p.runs.sum():,}"); d.metric("Total Wickets",f"{p.wickets.sum():,}")
l,r=st.columns(2)
with l: st.plotly_chart(px.bar(p.nlargest(8,"runs"),x="runs",y="name",orientation="h",title="Top Run Scorers"),use_container_width=True)
with r: st.plotly_chart(px.bar(p.nlargest(8,"wickets"),x="wickets",y="name",orientation="h",title="Top Wicket Takers"),use_container_width=True)
st.subheader("Recent Matches"); st.dataframe(m,use_container_width=True,hide_index=True)
