import logging
import os
from typing import Any


def filter_jobs(jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    filtered: list[dict[str, Any]] = []
    keywords = ["estágio", "estagiário", "estagiaria", "programação", "desenvolvimento", "backend", "java", "python", "aprendiz", "ti", "tecnologia"]

    allow_presencial = os.getenv('ALLOW_PRESENCIAL', '1').lower() in ('1', 'true', 'yes')
    presencial_cidades = [c.strip().lower() for c in os.getenv('PRESENCIAL_CIDADES', 'garanhuns,recife,são paulo,rio de janeiro,belo horizonte,brasília').split(',') if c.strip()]

    for job in jobs:
        title = job.get('titulo', '').lower()
        desc = job.get('descricao_resumida', '').lower()
        tipo = job.get('tipo', '').lower()
        local = job.get('localizacao', '').lower()

        has_kw = any(kw in title or kw in desc for kw in keywords)
        is_remote = 'remoto' in tipo or 'híbrido' in tipo or 'hibrido' in tipo
        is_presencial = 'presencial' in tipo or tipo.strip() == ''

        cidade_ok = not local or any(cidade in local for cidade in presencial_cidades)

        if has_kw and (is_remote or (allow_presencial and is_presencial and cidade_ok)):
            filtered.append(job)

    logging.info(
        f"Filtro: {len(filtered)}/{len(jobs)} vagas mantidas (allow_presencial={allow_presencial}, cidades={presencial_cidades})"
    )
    return filtered
