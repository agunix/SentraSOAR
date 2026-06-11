RULES = [
    {
        "name": "SSH Brute Force",
        "condition": lambda e: e.event_type == "login" and e.status == "failed",
        "threshold": 3
    }
]