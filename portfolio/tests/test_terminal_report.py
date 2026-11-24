import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "terminal-bench-4-harness" / "terminal_report.py"
spec = importlib.util.spec_from_file_location("terminal_report", MODULE)
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)

class TerminalReportTests(unittest.TestCase):
    def test_counts_statuses(self):
        result = report.summarize([
            {"task_id": "a", "status": "passed"},
            {"task_id": "b", "status": "failed"},
            {"task_id": "c", "status": "timeout"},
        ])
        self.assertEqual(result["passed"], 1)
        self.assertEqual(result["success_rate"], 1 / 3)

    def test_duplicate_ids_rejected(self):
        with self.assertRaises(ValueError):
            report.summarize([{"task_id": "a", "status": "passed"},
                              {"task_id": "a", "status": "failed"}])

if __name__ == "__main__":
    unittest.main()
