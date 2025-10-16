import { useState } from 'react';

export default function Home() {
  const [type, setType] = useState('default');
  const [payload, setPayload] = useState('{"example": "data"}');
  const [tasks, setTasks] = useState([]);

  const createTask = async () => {
    const res = await fetch('http://localhost:8000/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ type, payload: JSON.parse(payload) })
    });
    const data = await res.json();
    alert(`Task created with ID: ${data.id}`);
    fetchTask(data.id);
  };

  const fetchTask = async (id) => {
    const res = await fetch(`http://localhost:8000/tasks/${id}`);
    const data = await res.json();
    setTasks((prev) => [...prev, data]);
  };

  return (
    <main style={{ padding: 40, fontFamily: 'Arial' }}>
      <h1>Nexa Test 1 Validation</h1>
      <div style={{ marginBottom: 20 }}>
        <label>Type: </label>
        <input value={type} onChange={(e) => setType(e.target.value)} />
      </div>
      <div style={{ marginBottom: 20 }}>
        <label>Payload (JSON): </label>
        <textarea value={payload} onChange={(e) => setPayload(e.target.value)} rows="4" cols="50" />
      </div>
      <button onClick={createTask}>Create Task</button>

      <h2 style={{ marginTop: 40 }}>Task History</h2>
      <ul>
        {tasks.map((t) => (
          <li key={t.id}>
            <b>ID:</b> {t.id} | <b>Type:</b> {t.type} | <b>Status:</b> {t.status}
          </li>
        ))}
      </ul>
    </main>
  );
}
