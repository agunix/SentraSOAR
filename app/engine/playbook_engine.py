from datetime import datetime
from app.storage.memory_db import db

def block_ip(ip):
    # simulation (real world: firewall / cloud API)
    return f"IP {ip} blocked"

def create_incident(alert):
    incident = {
        "id": db.counter,
        "title": alert.name,
        "severity": alert.severity,
        "source_ip": alert.source_ip,
        "created_at": datetime.utcnow().isoformat(),
        "status": "open"
    }

    db.incidents.append(incident)
    db.counter += 1

    return incident


def run_playbook(alert):

    actions = []

    # ACTION 1: block IP
    actions.append(block_ip(alert.source_ip))

    # ACTION 2: create incident
    incident = create_incident(alert)

    return {
        "actions_executed": actions,
        "incident": incident
    }