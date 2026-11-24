# LLM Red-Team and Safety Benchmark

A compact, versioned evaluation set for probing model behavior under adversarial and safety-sensitive prompts. The project is designed for controlled evaluation, not for generating harmful instructions.

## Coverage
- Prompt-injection attempts against quoted or retrieved content
- Requests to reveal secrets or hidden system instructions
- Unsupported factual assertions and citation fabrication
- Overconfident responses under uncertainty
- Inconsistent refusals across semantically equivalent prompts
- Safe handling of benign requests that resemble risky ones

## Protocol
Each test case includes an ID, risk category, prompt, expected behavior, severity, and reviewer notes. Run candidate models in an isolated evaluation environment, store raw outputs securely, and have trained reviewers adjudicate ambiguous cases. Report per-category rates and confidence intervals, not just one aggregate safety score.

## Ethics and limitations
Use synthetic secrets and non-operational examples. Do not test against real users or production systems without authorization. Automated string checks are screening signals, not a complete safety judgment.

## Status
Initial benchmark specification; dataset expansion and human-label calibration are future work.
