import requests
from app.dashboard.config import API_BASE

def get_alerts():
    response = requests.get(
        f"{API_BASE}/alerts"
    )

    response.raise_for_status()

    return response.json()



def get_incidents():
    response = requests.get(
        f"{API_BASE}/incidents"
    )

    response.raise_for_status()

    return response.json()