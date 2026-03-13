from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import sqlite3
import os
from datetime import datetime

app = FastAPI()

@app.get("/api/jobs")
def get_jobs():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM jobs ORDER BY data_publicacao DESC")
    jobs = c.fetchall()
    conn.close()
    
    jobs_list = []
    for job in jobs:
        jobs_list.append({
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
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM jobs")
    total_jobs = c.fetchone()[0]
    conn.close()
    
    # Verificar último log
    last_log = "Nenhuma execução ainda"
    if os.path.exists('logs/system.log'):
        with open('logs/system.log', 'r') as f:
            lines = f.readlines()
            if lines:
                last_log = lines[-1].strip()
    
    return {
        "total_vagas": total_jobs,
        "banco_dados": "jobs.db",
        "ultimo_log": last_log,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/")
def read_root():
    return FileResponse("dashboard.html")