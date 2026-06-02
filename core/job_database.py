import sqlite3
import hashlib
import csv
import os
from typing import Any
from config import DB_PATH, CSV_PATH


def create_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        empresa TEXT,
        localizacao TEXT,
        tipo TEXT,
        link TEXT UNIQUE,
        data_publicacao TEXT,
        descricao_resumida TEXT,
        hash TEXT UNIQUE
    )''')
    conn.commit()
    conn.close()


def save_jobs_to_db(jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    new_jobs: list[dict[str, Any]] = []
    for job in jobs:
        job_hash = hashlib.md5(job['link'].encode()).hexdigest()
        try:
            c.execute('''INSERT INTO jobs (titulo, empresa, localizacao, tipo, link, data_publicacao, descricao_resumida, hash)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                      (job['titulo'], job['empresa'], job['localizacao'], job['tipo'], job['link'], job['data_publicacao'], job['descricao_resumida'], job_hash))
            new_jobs.append(job)
        except sqlite3.IntegrityError:
            pass
    conn.commit()
    conn.close()
    return new_jobs


def export_to_csv(jobs: list[dict[str, Any]]) -> None:
    if not jobs:
        return
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['titulo', 'empresa', 'localizacao', 'tipo', 'link', 'data_publicacao', 'descricao_resumida']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists or os.path.getsize(CSV_PATH) == 0:
            writer.writeheader()
        for job in jobs:
            writer.writerow(job)
