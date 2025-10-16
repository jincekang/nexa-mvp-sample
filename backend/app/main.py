from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(title="Nexa Test 1 Validation", version="1.0")

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
