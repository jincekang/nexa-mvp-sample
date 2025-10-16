# Nexa Test 1 Validation

Combined FastAPI + Next.js monorepo demonstrating architecture clarity and modularity.

## Structure
- **backend/** → FastAPI service for task creation and retrieval.
- **frontend/** → Next.js interface to interact with the API.

## Run Instructions

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install next react react-dom
npm run dev
```

Access frontend via http://localhost:3000 and backend at http://localhost:8000
