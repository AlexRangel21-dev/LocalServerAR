from fastapi import FastAPI

from routers.health import router as health_router
from routers.auth import router as auth_router

app = FastAPI(
    title="Tools API",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(auth_router)