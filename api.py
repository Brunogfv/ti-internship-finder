import json
import sqlite3
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import FileResponse
from config import DB_PATH, BASE_DIR

STATUS_PATH = BASE_DIR / 'last_run.json'
app = FastAPI(title="TI Internship Finder API")


@app.get("/api/jobs")
def get_jobs(search: str = ""):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if search:
        c.execute("SELECT * FROM jobs WHERE titulo LIKE ? OR empresa LIKE ? OR localizacao LIKE ? ORDER BY data_publicacao DESC",
                  (f"%{search}%", f"%{search}%", f"%{search}%"))
    else:
        c.execute("SELECT * FROM jobs ORDER BY data_publicacao DESC")
    rows = c.fetchall()
    conn.close()

    jobs_list = []
    for job in rows:
        jobs_list.append({
            "id": job[0],
            "titulo": job[1],
            "empresa": job[2],
            "localizacao": job[3],
            "tipo": job[4],
            "link": job[5],
            "data_publicacao": job[6],
            "descricao_resumida": job[7]
        })
    return {"total": len(jobs_list), "jobs": jobs_list}


@app.get("/api/status")
def get_status():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM jobs")
    total_jobs = c.fetchone()[0]
    c.execute("SELECT data_publicacao FROM jobs ORDER BY data_publicacao DESC LIMIT 1")
    row = c.fetchone()
    ultima_data = row[0] if row else None
    conn.close()

    ultima_execucao = "Nenhuma execução ainda"
    novas_vagas = 0
    try:
        with open(STATUS_PATH) as f:
            data = json.load(f)
            ultima_execucao = data.get('ultima_execucao', ultima_execucao)
            novas_vagas = data.get('novas_vagas', 0)
    except Exception:
        pass

    return {
        "total_vagas": total_jobs,
        "ultima_data_vaga": ultima_data,
        "ultima_execucao": ultima_execucao,
        "novas_vagas": novas_vagas,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/")
def read_root():
    return FileResponse(str(BASE_DIR / "dashboard.html"))
