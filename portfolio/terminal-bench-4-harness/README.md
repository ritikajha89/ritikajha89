# Terminal-Bench 4.0 Experiment Harness

A lightweight experiment wrapper and reporting scaffold for running the published Terminal-Bench 4.0 release with Harbor. This repository is an independent experiment client; it is not the official benchmark, leaderboard, or Harbor implementation.

## Prerequisites
- Python 3.10+
- Harbor installed and configured for the agent/provider you intend to test
- A container runtime supported by Harbor

## Run the official release
```bash
harbor run -d terminal-bench/terminal-bench@4.0.0
```

Use Harbor's documented output and preserve the raw run artifacts. The wrapper in this repository normalizes a supplied JSON result file into a compact summary; it does not invent task results or substitute for the official verifier.

## Reporting requirements
Record benchmark release, Harbor version, agent/model identifier, provider, run configuration, task count, successful tasks, failures, timeouts, and raw artifact location. Report cost and latency only when measured. Separate official benchmark runs from custom tasks and local smoke tests.

## References
- Terminal-Bench 4.0 release: https://www.tbench.ai/news/terminal-bench-4-0
- Official benchmark repository: https://github.com/harbor-framework/terminal-bench

## Status
Experiment scaffolding only. No official leaderboard score or completed benchmark run is claimed.
