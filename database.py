import sqlite3
import pandas as pd
DB_NAME="cricket.db"
def get_connection(): return sqlite3.connect(DB_NAME)
def create_tables():
    c=get_connection(); x=c.cursor()
    x.execute("CREATE TABLE IF NOT EXISTS teams(team_id INTEGER PRIMARY KEY AUTOINCREMENT,team_name TEXT UNIQUE,country TEXT)")
    x.execute("CREATE TABLE IF NOT EXISTS matches(match_id INTEGER PRIMARY KEY,team1 TEXT,team2 TEXT,venue TEXT,match_date TEXT,status TEXT,winner TEXT)")
    x.execute("CREATE TABLE IF NOT EXISTS players(player_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,team TEXT,role TEXT,matches INTEGER,runs INTEGER,wickets INTEGER,batting_average REAL,strike_rate REAL,economy REAL)")
    x.execute("CREATE TABLE IF NOT EXISTS batting_stats(batting_id INTEGER PRIMARY KEY AUTOINCREMENT,match_id INTEGER,player_id INTEGER,runs INTEGER,balls INTEGER,fours INTEGER,sixes INTEGER,strike_rate REAL)")
    x.execute("CREATE TABLE IF NOT EXISTS bowling_stats(bowling_id INTEGER PRIMARY KEY AUTOINCREMENT,match_id INTEGER,player_id INTEGER,overs REAL,runs_conceded INTEGER,wickets INTEGER,economy REAL)")
    c.commit(); c.close()
def seed_data():
    c=get_connection(); x=c.cursor()
    teams=[("India","India"),("Australia","Australia"),("England","England"),("Pakistan","Pakistan"),("South Africa","South Africa"),("New Zealand","New Zealand")]
    x.executemany("INSERT OR IGNORE INTO teams(team_name,country) VALUES(?,?)",teams)
    matches=[(1,"India","Australia","Wankhede Stadium","2026-09-01","India won","India"),(2,"England","Pakistan","Lord's","2026-09-02","England won","England"),(3,"South Africa","New Zealand","Cape Town","2026-09-03","South Africa won","South Africa"),(4,"India","England","Ahmedabad","2026-09-05","India won","India"),(5,"Pakistan","New Zealand","Lahore","2026-09-06","Pakistan won","Pakistan"),(6,"Australia","South Africa","Sydney","2026-09-07","Australia won","Australia")]
    x.executemany("INSERT OR IGNORE INTO matches VALUES(?,?,?,?,?,?,?)",matches)
    players=[("Virat Kohli","India","Batsman",12,642,0,53.5,138.2,0),("Rohit Sharma","India","Batsman",12,581,0,48.42,142.5,0),("Jasprit Bumrah","India","Bowler",12,48,25,16,105.2,6.42),("Hardik Pandya","India","All-rounder",12,384,14,38.4,151.7,7.82),("Shubman Gill","India","Batsman",11,492,0,44.73,131.4,0),("Steve Smith","Australia","Batsman",12,598,1,49.83,129.8,0),("Travis Head","Australia","Batsman",12,625,0,52.08,148.6,0),("Pat Cummins","Australia","Bowler",12,71,22,17.75,112.6,6.85),("Mitchell Starc","Australia","Bowler",11,54,24,18,110.2,6.51),("Joe Root","England","Batsman",12,615,2,51.25,127.5,0),("Jos Buttler","England","Wicketkeeper",12,545,0,45.42,146.3,0),("Jofra Archer","England","Bowler",10,38,21,19,108.6,6.72),("Babar Azam","Pakistan","Batsman",12,573,0,47.75,133.8,0),("Mohammad Rizwan","Pakistan","Wicketkeeper",12,488,0,40.67,128.4,0),("Shaheen Afridi","Pakistan","Bowler",12,41,23,20.5,109.3,6.95),("Kagiso Rabada","South Africa","Bowler",11,35,26,17.5,104.2,6.31),("Quinton de Kock","South Africa","Wicketkeeper",11,512,0,46.55,139.1,0),("Aiden Markram","South Africa","All-rounder",11,421,11,42.1,134.7,7.21),("Kane Williamson","New Zealand","Batsman",10,475,0,47.5,121.5,0),("Trent Boult","New Zealand","Bowler",10,29,20,14.5,102.1,6.78)]
    x.executemany("INSERT OR IGNORE INTO players(name,team,role,matches,runs,wickets,batting_average,strike_rate,economy) VALUES(?,?,?,?,?,?,?,?,?)",players)
    c.commit(); c.close()
def run_query(q):
    c=get_connection()
    try:return pd.read_sql_query(q,c)
    finally:c.close()
def execute_query(q,p=()):
    c=get_connection()
    try:c.execute(q,p);c.commit();return True
    except:return False
    finally:c.close()
create_tables(); seed_data()
