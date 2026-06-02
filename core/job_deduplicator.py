import hashlib
from typing import Any


def deduplicate_jobs(jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for job in jobs:
        job_id = hashlib.md5(job['link'].encode()).hexdigest()
        if job_id not in seen:
            seen.add(job_id)
            unique.append(job)
    return unique
