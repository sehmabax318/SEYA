from fastapi import FastAPI

app = FastAPI(
    title="SEYA API",
    version="0.1.0",
    description="Backend API for SEYA"
)


@app.get("/")
def home():
    return {
        "assistant": "SEYA",
        "status": "online",
        "version": "0.1.0"
    }