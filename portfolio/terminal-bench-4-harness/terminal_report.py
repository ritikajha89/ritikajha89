"""Normalize a user-exported JSON task result list into transparent metrics.

Expected input: [{"task_id": str, "status": "passed|failed|timeout"}, ...]
This deliberately does not parse or fabricate official leaderboard records.
"""
import json
import sys
from collections import Counter
from pathlib import Path

VALID = {"passed", "failed", "timeout"}


def summarize(rows: list[dict]) -> dict:
    if not rows:
        raise ValueError("at least one task result is required")
    ids = [row.get("task_id") for row in rows]
    if any(not item for item in ids) or len(ids) != len(set(ids)):
        raise ValueError("task_id values must be present and unique")
    statuses = [row.get("status") for row in rows]
    if any(status not in VALID for status in statuses):
        raise ValueError(f"status must be one of {sorted(VALID)}")
    counts = Counter(statuses)
    total = len(rows)
    return {"total": total, "passed": counts["passed"], "failed": counts["failed"],
            "timeouts": counts["timeout"], "success_rate": counts["passed"] / total}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python terminal_report.py results.json")
    rows = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(summarize(rows), indent=2))

if __name__ == "__main__":
    main()
