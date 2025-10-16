# Backend – Nexa Test 1 Validation

## Description
FastAPI backend for creating and retrieving tasks. Includes mock route optimization.

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints
- `POST /tasks` → Create a task
- `GET /tasks/{id}` → Retrieve task by ID
