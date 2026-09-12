import requests
API_KEY=""
BASE_URL="https://cricbuzz-cricket.p.rapidapi.com"
def get_live_matches():
    if not API_KEY:return {"demo_mode":True}
    try:
        r=requests.get(BASE_URL+"/matches/v1/live",headers={"X-RapidAPI-Key":API_KEY,"X-RapidAPI-Host":"cricbuzz-cricket.p.rapidapi.com"},timeout=10)
        return r.json()
    except Exception as e:return {"error":str(e)}
