# Agent Trace Observability Service

A backend-oriented trace ingestion scaffold for inspecting multi-step agent execution. It validates spans, preserves parent-child relationships, and calculates basic latency and tool-failure summaries.

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Post a trace to `POST /traces` with a trace ID and spans containing span ID, optional parent ID, operation name, start/end timestamps, and status. The current version is an in-memory prototype, not a production telemetry platform.

## Engineering concerns
Production deployment should add persistent storage, trace sampling, PII redaction, tenant isolation, retention controls, OpenTelemetry ingestion, and query indexes.
