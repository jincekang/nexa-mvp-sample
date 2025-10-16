import sqlite3
import json
from pathlib import Path
import random

DB_PATH = Path(__file__).resolve().parents[2] / "db.sqlite3"

class TaskService:
    def __init__(self):
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, payload TEXT, status TEXT)"
            )
            conn.commit()

    def create_task(self, type_: str, payload: dict):
        status = "mocked"
        if type_ == "optimize_agenda":
            payload["route_suggestion"] = {
                "distance_km": round(random.uniform(1.0, 15.0), 2),
                "rating_factor": round(random.uniform(0.7, 1.0), 2),
            }
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO tasks (type, payload, status) VALUES (?, ?, ?)",
                (type_, json.dumps(payload), status),
            )
            conn.commit()
            task_id = cur.lastrowid
        return {"id": task_id, "status": status}

    def get_task(self, task_id: int):
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, type, payload, status FROM tasks WHERE id=?", (task_id,))
            row = cur.fetchone()
            if not row:
                return None
            return {
                "id": row[0],
                "type": row[1],
                "payload": json.loads(row[2]),
                "status": row[3],
            }
