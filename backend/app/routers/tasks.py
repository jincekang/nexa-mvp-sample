from fastapi import APIRouter, HTTPException
from app.services.task_service import TaskService
from pydantic import BaseModel

router = APIRouter()
service = TaskService()

class TaskRequest(BaseModel):
    type: str
    payload: dict

@router.post("/")
async def create_task(req: TaskRequest):
    task = service.create_task(req.type, req.payload)
    return {"id": task["id"], "status": task["status"]}

@router.get("/{task_id}")
async def get_task(task_id: int):
    task = service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
