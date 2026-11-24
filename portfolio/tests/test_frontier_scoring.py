import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier-llm-eval-lab" / "src"))
from frontier_eval.scoring import EvaluationCase, evaluate

class ScoringTests(unittest.TestCase):
    def test_full_coverage_passes(self):
        case = EvaluationCase("x", ("alpha", "beta"), ("include caveat",))
        result = evaluate(case, "alpha beta; include caveat")
        self.assertTrue(result.passed)
        self.assertEqual(result.factuality, 1.0)

    def test_prohibited_phrase_fails(self):
        case = EvaluationCase("x", ("alpha",), prohibited_phrases=("guaranteed cure",))
        self.assertFalse(evaluate(case, "alpha. guaranteed cure").passed)

    def test_empty_answer_fails(self):
        case = EvaluationCase("x", ("alpha",))
        self.assertFalse(evaluate(case, "").passed)

if __name__ == "__main__":
    unittest.main()
