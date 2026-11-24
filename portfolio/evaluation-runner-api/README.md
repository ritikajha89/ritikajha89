# LLM Evaluation Runner API

A backend service scaffold for registering evaluation jobs, validating payloads, and exposing job status through a typed FastAPI interface. The initial version uses an in-memory store for local development; replace it with PostgreSQL and a durable queue before production use.

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `/docs` for the OpenAPI interface. The service accepts evaluation metadata and task payloads; it does not call an LLM provider or claim to execute a benchmark in this scaffold.

## Production roadmap
PostgreSQL persistence, idempotency keys, worker queue, authentication/authorization, rate limiting, audit events, structured logs, and integration tests.
