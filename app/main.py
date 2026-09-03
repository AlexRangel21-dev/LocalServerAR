from fastapi import FastAPI
from routers.health import router as health_router

app = FastAPI(
    title="Tools API",
    version="1.0.0"
)

app.include_router(health_router)