import requests
from app.dashboard.config import API_BASE

def get_alerts():
    return requests.get(f"{API_BASE}/alerts").json()

def get_incidents():
    return requests.get(f"{API_BASE}/incidents").json()