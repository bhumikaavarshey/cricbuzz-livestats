import streamlit as st
from database import run_query

st.title("📊 Player Statistics")

df = run_query("SELECT * FROM players")

team = st.selectbox(
    "Select Team",
    ["All"] + sorted(df["team"].unique().tolist())
)

role = st.selectbox(
    "Select Role",
    ["All"] + sorted(df["role"].unique().tolist())
)

if team != "All":
    df = df[df["team"] == team]

if role != "All":
    df = df[df["role"] == role]

st.subheader("Player Performance")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
