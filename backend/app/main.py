from fastapi import FastAPI


from app.api.routes import router

app = FastAPI(
    title="SEYA API",
    version="0.1.0",
    description="Backend API for SEYA",
)

app.include_router(router)