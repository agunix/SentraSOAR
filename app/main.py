from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="SOAR MVP Engine", version="1.0")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "SOAR MVP is running"}