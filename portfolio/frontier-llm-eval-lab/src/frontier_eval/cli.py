"""Command-line entry point for JSONL/JSON case evaluation."""
import json
import sys
from pathlib import Path
from .scoring import EvaluationCase, evaluate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: frontier-eval path/to/sample.json")
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    case = EvaluationCase(
        case_id=payload["case_id"],
        required_facts=tuple(payload.get("required_facts", [])),
        required_elements=tuple(payload.get("required_elements", [])),
        prohibited_phrases=tuple(payload.get("prohibited_phrases", [])),
    )
    print(json.dumps(evaluate(case, payload.get("answer", "")).to_dict(), indent=2))

if __name__ == "__main__":
    main()
