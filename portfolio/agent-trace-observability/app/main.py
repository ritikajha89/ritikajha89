"""Minimal trace ingestion and summary API."""
from datetime import datetime, timezone
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, model_validator

app = FastAPI(title="Agent Trace Observability", version="0.1.0")

class Span(BaseModel):
    span_id: str = Field(min_length=1, max_length=100)
    parent_span_id: str | None = None
    operation: str = Field(min_length=1, max_length=200)
    started_at: datetime
    ended_at: datetime
    status: str = Field(pattern="^(ok|error)$")

    @model_validator(mode="after")
    def validate_times(self):
        if self.ended_at < self.started_at:
            raise ValueError("ended_at must not precede started_at")
        return self

class TraceIn(BaseModel):
    trace_id: str = Field(min_length=1, max_length=100)
    spans: list[Span] = Field(min_length=1, max_length=2000)

    @model_validator(mode="after")
    def validate_graph(self):
        ids = [span.span_id for span in self.spans]
        if len(ids) != len(set(ids)):
            raise ValueError("span_id values must be unique within a trace")
        known = set(ids)
        if any(span.parent_span_id and span.parent_span_id not in known for span in self.spans):
            raise ValueError("parent_span_id must reference a span in this trace")
        return self

_store: dict[str, TraceIn] = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/traces", status_code=202)
def ingest_trace(trace: TraceIn):
    _store[trace.trace_id] = trace
    durations = [(s.ended_at - s.started_at).total_seconds() for s in trace.spans]
    errors = sum(s.status == "error" for s in trace.spans)
    return {"trace_id": trace.trace_id, "span_count": len(trace.spans),
            "error_count": errors, "total_span_seconds": round(sum(durations), 6)}

@app.get("/traces/{trace_id}")
def get_trace(trace_id: str):
    trace = _store.get(trace_id)
    if trace is None:
        raise HTTPException(status_code=404, detail="trace not found")
    return trace
