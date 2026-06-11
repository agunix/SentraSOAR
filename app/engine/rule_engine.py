from collections import defaultdict
from app.rules.rules import RULES
from app.storage.memory_db import db
from app.models.alert import Alert
from app.engine.playbook_engine import run_playbook

# simple brute-force tracker
failed_logins = defaultdict(int)

def process_event(event):

    triggered_alerts = []

    for rule in RULES:

        if rule["condition"](event):

            failed_logins[event.source_ip] += 1

            if failed_logins[event.source_ip] >= rule["threshold"]:

                alert = Alert(
                    name=rule["name"],
                    severity="high",
                    source_ip=event.source_ip,
                    details={"count": failed_logins[event.source_ip]}
                )

                db.alerts.append(alert.dict())

                incident = run_playbook(alert)

                triggered_alerts.append({
                    "alert": alert.dict(),
                    "incident": incident
                })

                failed_logins[event.source_ip] = 0

    return {
        "status": "processed",
        "alerts_generated": triggered_alerts
    }