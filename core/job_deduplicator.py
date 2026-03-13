def deduplicate_jobs(jobs):
    seen = set()
    unique = []
    for job in jobs:
        job_id = hash(job['link'])
        if job_id not in seen:
            seen.add(job_id)
            unique.append(job)
    return unique