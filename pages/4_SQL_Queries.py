import streamlit as st
from database import run_query

st.title("🔍 SQL Query Interface")

queries = {
    "Top 10 Run Scorers":
        "SELECT name, team, runs FROM players ORDER BY runs DESC LIMIT 10;",

    "Top Wicket Takers":
        "SELECT name, team, wickets FROM players ORDER BY wickets DESC LIMIT 10;",

    "Players Above 500 Runs":
        "SELECT name, team, runs FROM players WHERE runs > 500 ORDER BY runs DESC;",

    "Team Total Runs":
        "SELECT team, SUM(runs) AS total_runs FROM players GROUP BY team ORDER BY total_runs DESC;",

    "Team Total Wickets":
        "SELECT team, SUM(wickets) AS total_wickets FROM players GROUP BY team ORDER BY total_wickets DESC;",

    "Average Runs By Team":
        "SELECT team, ROUND(AVG(runs),2) AS average_runs FROM players GROUP BY team;",

    "All Rounders":
        "SELECT name, team, runs, wickets FROM players WHERE role='All-rounder';",

    "High Strike Rate":
        "SELECT name, team, strike_rate FROM players WHERE strike_rate > 140 ORDER BY strike_rate DESC;",

    "Best Batting Average":
        "SELECT name, team, batting_average FROM players ORDER BY batting_average DESC LIMIT 10;",

    "Players With Runs And Wickets":
        "SELECT name, team, runs, wickets FROM players WHERE runs > 300 AND wickets > 5;",

    "Match Winners":
        "SELECT winner, COUNT(*) AS wins FROM matches GROUP BY winner ORDER BY wins DESC;",

    "All Matches":
        "SELECT * FROM matches ORDER BY match_date DESC;",

    "Player Ranking":
        "SELECT name, team, runs, RANK() OVER (ORDER BY runs DESC) AS ranking FROM players;",

    "Role Distribution":
        "SELECT role, COUNT(*) AS players FROM players GROUP BY role;",

    "Team Player Count":
        "SELECT team, COUNT(*) AS players FROM players GROUP BY team;"
}

choice = st.selectbox(
    "Select a SQL Query",
    list(queries.keys())
)

st.code(queries[choice], language="sql")

if st.button("▶ Run Query", type="primary"):

    result = run_query(queries[choice])

    st.subheader("Query Result")

    st.dataframe(
        result,
        use_container_width=True,
        hide_index=True
    )

st.divider()

st.subheader("Custom SQL Query")

custom_query = st.text_area(
    "Enter your SELECT query",
    placeholder="SELECT * FROM players;"
)

if st.button("Execute Custom Query"):

    if custom_query.strip().lower().startswith("select"):

        try:
            result = run_query(custom_query)

            st.dataframe(
                result,
                use_container_width=True,
                hide_index=True
            )

        except Exception as e:
            st.error(str(e))

    else:
        st.error("Only SELECT queries are allowed.")
