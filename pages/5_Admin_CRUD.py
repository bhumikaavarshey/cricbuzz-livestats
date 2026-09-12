import streamlit as st
from database import run_query, execute_query

st.title("⚙️ Administrative CRUD Operations")

create_tab, read_tab, update_tab, delete_tab = st.tabs(
    ["Create", "Read", "Update", "Delete"]
)

# CREATE
with create_tab:

    st.subheader("Add New Player")

    with st.form("add_player"):

        name = st.text_input("Player Name")
        team = st.text_input("Team")

        role = st.selectbox(
            "Role",
            ["Batsman", "Bowler", "All-rounder", "Wicketkeeper"]
        )

        matches = st.number_input("Matches", min_value=0, value=0)
        runs = st.number_input("Runs", min_value=0, value=0)
        wickets = st.number_input("Wickets", min_value=0, value=0)

        submitted = st.form_submit_button("Add Player")

        if submitted:

            execute_query(
                """
                INSERT INTO players
                (name, team, role, matches, runs, wickets,
                 batting_average, strike_rate, economy)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (name, team, role, matches, runs, wickets, 0, 0, 0)
            )

            st.success("Player created successfully!")

# READ
with read_tab:

    st.subheader("All Player Records")

    players = run_query(
        "SELECT * FROM players ORDER BY runs DESC"
    )

    st.dataframe(
        players,
        use_container_width=True,
        hide_index=True
    )

# UPDATE
with update_tab:

    st.subheader("Update Player")

    players = run_query(
        "SELECT player_id, name, runs, wickets FROM players"
    )

    player_id = st.selectbox(
        "Select Player",
        players["player_id"].tolist(),
        format_func=lambda x:
            players.loc[
                players["player_id"] == x,
                "name"
            ].iloc[0]
    )

    selected = players[
        players["player_id"] == player_id
    ].iloc[0]

    new_runs = st.number_input(
        "Updated Runs",
        min_value=0,
        value=int(selected["runs"])
    )

    new_wickets = st.number_input(
        "Updated Wickets",
        min_value=0,
        value=int(selected["wickets"])
    )

    if st.button("Update Player"):

        execute_query(
            """
            UPDATE players
            SET runs = ?, wickets = ?
            WHERE player_id = ?
            """,
            (new_runs, new_wickets, player_id)
        )

        st.success("Player updated successfully!")

# DELETE
with delete_tab:

    st.subheader("Delete Player")

    players = run_query(
        "SELECT player_id, name FROM players"
    )

    player_id = st.selectbox(
        "Select Player To Delete",
        players["player_id"].tolist(),
        format_func=lambda x:
            players.loc[
                players["player_id"] == x,
                "name"
            ].iloc[0],
        key="delete_player"
    )

    if st.button("Delete Player"):

        execute_query(
            "DELETE FROM players WHERE player_id = ?",
            (player_id,)
        )

        st.success("Player deleted successfully!")
