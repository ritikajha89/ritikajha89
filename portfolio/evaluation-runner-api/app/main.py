"""Typed API scaffold for evaluation job submission and status tracking."""
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="LLM Evaluation Runner API", version="0.1.0")

class JobState(str, Enum):
    queued = "queued"
    running = "running"
    completed = "completed"
    failed = "failed"

class JobRequest(BaseModel):
    suite: str = Field(min_length=1, max_length=120)
    model_id: str = Field(min_length=1, max_length=200)
    dataset_version: str = Field(min_length=1, max_length=80)
    cases: list[dict] = Field(min_length=1, max_length=500)

class JobRecord(BaseModel):
    job_id: str
    state: JobState
    created_at: datetime
    suite: str
    model_id: str
    dataset_version: str
    case_count: int

_jobs: dict[str, JobRecord] = {}

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

@app.post("/jobs", response_model=JobRecord, status_code=202)
def create_job(request: JobRequest) -> JobRecord:
    job = JobRecord(job_id=str(uuid4()), state=JobState.queued,
                    created_at=datetime.now(timezone.utc), suite=request.suite,
                    model_id=request.model_id, dataset_version=request.dataset_version,
                    case_count=len(request.cases))
    _jobs[job.job_id] = job
    return job

@app.get("/jobs/{job_id}", response_model=JobRecord)
def get_job(job_id: str) -> JobRecord:
    job = _jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")
    return job
