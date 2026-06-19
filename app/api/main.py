from fastapi import FastAPI

app = FastAPI()


@app.get("/alerts")
def alerts():
    return [
        {
            "id": 1,
            "severity": "high",
            "source": "test",
            "message": "Test alert"
        }
    ]


@app.get("/incidents")
def incidents():
    return [
        {
            "id": 1,
            "status": "open",
            "title": "Test incident"
        }
    ]