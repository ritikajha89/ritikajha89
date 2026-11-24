"""Deterministic rubric scoring with explicit, auditable criteria."""
from dataclasses import asdict, dataclass
from typing import Iterable


@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    required_facts: tuple[str, ...]
    required_elements: tuple[str, ...] = ()
    prohibited_phrases: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvaluationResult:
    case_id: str
    factuality: float
    completeness: float
    prohibited_phrase_hits: tuple[str, ...]
    passed: bool

    def to_dict(self) -> dict:
        return asdict(self)


def _coverage(expected: Iterable[str], answer: str) -> float:
    items = tuple(expected)
    if not items:
        return 1.0
    normalized = answer.casefold()
    return sum(term.casefold() in normalized for term in items) / len(items)


def evaluate(case: EvaluationCase, answer: str) -> EvaluationResult:
    """Score lexical evidence coverage; this is not semantic truth verification."""
    if not answer.strip():
        return EvaluationResult(case.case_id, 0.0, 0.0, (), False)
    factuality = _coverage(case.required_facts, answer)
    completeness = _coverage(case.required_elements, answer)
    hits = tuple(p for p in case.prohibited_phrases if p.casefold() in answer.casefold())
    return EvaluationResult(case.case_id, factuality, completeness, hits,
                            factuality == 1.0 and completeness == 1.0 and not hits)
