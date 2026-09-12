import streamlit as st
from database import run_query
from api import get_live_matches

st.title("🏏 Live Matches & Scorecards")

api_data = get_live_matches()

if api_data.get("demo_mode"):
    st.warning(
        "Demo mode: add an API key in api.py to enable live API results."
    )

matches = run_query(
    "SELECT * FROM matches ORDER BY match_date DESC"
)

for _, match in matches.iterrows():

    with st.container(border=True):

        st.subheader(
            f"{match.team1} vs {match.team2}"
        )

        st.write(
            f"**Venue:** {match.venue}"
        )

        st.write(
            f"**Date:** {match.match_date}"
        )

        st.write(
            f"**Result:** {match.status}"
        )

        st.write(
            f"**Winner:** {match.winner}"
        )
