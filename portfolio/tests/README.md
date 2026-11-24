# Portfolio tests

Run the dependency-free unit tests from the repository root:

```bash
python -m unittest discover -s portfolio/tests -v
```

These tests cover the transparent rubric scorer and the Terminal-Bench result normalizer. They do not execute Harbor, contact model APIs, or establish benchmark performance.
