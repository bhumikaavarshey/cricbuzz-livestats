import streamlit as st
import plotly.express as px
from database import run_query

st.title("📈 Statistics Visualizations")

players = run_query("SELECT * FROM players")

st.subheader("Top 10 Run Scorers")

top_runs = players.nlargest(10, "runs")

fig1 = px.bar(
    top_runs,
    x="name",
    y="runs",
    title="Top 10 Players by Runs"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Runs vs Strike Rate")

fig2 = px.scatter(
    players,
    x="strike_rate",
    y="runs",
    size="matches",
    color="role",
    hover_name="name",
    title="Runs vs Strike Rate"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Team Performance")

team_data = run_query("""
SELECT
    team,
    SUM(runs) AS total_runs,
    SUM(wickets) AS total_wickets
FROM players
GROUP BY team
ORDER BY total_runs DESC
""")

fig3 = px.bar(
    team_data,
    x="team",
    y=["total_runs", "total_wickets"],
    barmode="group",
    title="Team Performance"
)

st.plotly_chart(fig3, use_container_width=True)
