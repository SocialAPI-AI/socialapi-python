# Contributing to socialapi-python

Thank you for considering contributing to the SocialAPI Python SDK.

## Development Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/social-api-ai/socialapi-python.git
   cd socialapi-python
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -e ".[dev]"
   ```

## Running Tests

```bash
# All tests
pytest

# Single file
pytest tests/test_accounts.py

# Single test
pytest tests/test_accounts.py -k "test_list"

# With coverage
pytest --cov=socialapi
```

## Linting and Formatting

```bash
# Lint
ruff check .

# Auto-fix lint issues
ruff check . --fix

# Format
ruff format .

# Format check (CI mode)
ruff format . --check
```

## Type Checking

```bash
pyright
```

## Pre-Commit Checklist

Run all quality checks before committing:

```bash
ruff check . && ruff format . --check && pyright && pytest
```

All four must pass before a pull request can be merged.

## Pull Request Guidelines

1. **Branch from `main`** and open your PR against `main`.
2. **Keep changes focused** -- one feature or fix per PR.
3. **Add tests** for any new functionality.
4. **Update docstrings** using Google-style format.
5. **Add type annotations** to all public functions and methods.
6. **Ensure all checks pass** (lint, format, type check, tests).
7. **Update CHANGELOG.md** with a summary of your changes under the `[Unreleased]` section.

## Code Style

- Follow PEP 8 naming conventions.
- Use `X | None` union syntax (PEP 604), not `Optional[X]`.
- Use built-in generics (`list[T]`, `dict[K, V]`), not `typing.List` / `typing.Dict`.
- Prefix private modules with `_`.
- Use keyword-only arguments (after `*`) for all optional parameters.
- Write Google-style docstrings with `Args`, `Returns`, and `Raises` sections.

## Questions?

Open an issue or reach out at contact@social-api.ai.
