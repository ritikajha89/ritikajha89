# Frontier LLM Evaluation Lab

A reproducible, provider-neutral evaluation harness for comparing language models on structured tasks. The initial implementation focuses on deterministic rubric scoring, evidence capture, pairwise comparison, and machine-readable reports.

## Evaluation dimensions
- Instruction adherence and task completion
- Factuality against supplied reference facts
- Completeness against required elements
- Groundedness: whether claims have supporting evidence in the response
- Safety flags supplied by a human reviewer or an external classifier

## Run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m frontier_eval.cli examples/sample.json
```

The scorer is intentionally deterministic and does not pretend to be a universal judge model. It provides transparent baseline metrics; model-based judging should be added as a separately versioned evaluator and calibrated against human labels.

## Methodology
Every run should record the dataset version, evaluator version, model/provider identifier, decoding parameters, timestamp, and raw response. Do not compare scores across changed rubrics without reporting the rubric version. Never publish benchmark claims without preserving the evaluated sample and run metadata.

## Status
Initial local baseline. No frontier-model leaderboard result is claimed.
