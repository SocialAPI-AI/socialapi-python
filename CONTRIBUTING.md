# Contributing to SocialAPI Python SDK

Thanks for your interest in contributing! This guide covers everything you need to get started.

## Prerequisites

- Python 3.11+
- Git

## Setup

1. Fork and clone the repo:

```bash
git clone https://github.com/SocialAPI-AI/socialapi-python.git
cd socialapi-python
```

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

3. Install in editable mode with dev dependencies:

```bash
make install
# or: pip install -e ".[dev]"
```

## Development Workflow

### Running Checks

```bash
make check     # lint + format check + type check + tests (same as CI)
```

Or run individually:

```bash
make lint       # ruff check .
make format     # ruff format . (auto-fix)
make typecheck  # pyright src/ (strict mode)
make test       # pytest
```

### Writing Code

- Source lives in `src/socialapi/`, tests in `tests/`.
- Follow PEP 8 naming: `snake_case` for functions/variables, `PascalCase` for classes.
- Every file starts with `from __future__ import annotations`.
- All public functions and classes need Google-style docstrings.
- Type everything -- pyright runs in strict mode with zero tolerance.
- Use `ruff` for linting and formatting (config is in `pyproject.toml`).

### Project Structure

```
src/socialapi/
  _client.py          # SocialAPI and AsyncSocialAPI clients
  _base_client.py     # HTTP layer (retry, auth, error handling)
  _exceptions.py      # Exception hierarchy
  _pagination.py      # CursorPage / AsyncCursorPage
  _constants.py       # Typed enums (Platform, PostStatus, etc.)
  models/             # Pydantic request/response models
  resources/           # Resource classes (accounts, comments, posts, etc.)
```

### Adding a New Resource

If the SocialAPI adds new endpoints:

1. Create models in `src/socialapi/models/<resource>.py`
2. Create sync + async resource classes in `src/socialapi/resources/<resource>.py`
3. Register the resource as a property on `SocialAPI` and `AsyncSocialAPI` in `_client.py`
4. Export models from `models/__init__.py` and `__init__.py`
5. Write tests in `tests/test_<resource>.py`

### Adding a New Method to an Existing Resource

1. Add the method to both the sync and async class in `resources/<resource>.py`
2. Add request/response models in `models/<resource>.py` if needed
3. Add tests covering the new method (both sync and at least one async test)

## Testing

Tests use [pytest](https://docs.pytest.org/) with [pytest-httpx](https://github.com/Colin-b/pytest_httpx) for HTTP mocking.

```bash
# Run all tests
make test

# Run a single file
pytest tests/test_accounts.py

# Run by name pattern
pytest -k "test_list"

# With coverage
pytest --cov=socialapi --cov-report=term-missing
```

### Writing Tests

- Mock HTTP responses with `httpx_mock.add_response()` -- never make real API calls.
- Test both sync and async variants for every resource method.
- Verify the correct URL, HTTP method, and response parsing.
- Use realistic mock data, not empty strings.

Example:

```python
def test_list_accounts(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url="https://test.social-api.ai/v1/accounts",
        json={"data": [{"id": "acc_001", "platform": "instagram", "account_name": "mypage"}]},
    )
    page = client.accounts.list()
    assert len(page) == 1
    assert page.data[0].platform == "instagram"
```

## Pull Request Guidelines

1. **Branch from `main`** -- create a feature branch like `feat/add-analytics-resource` or `fix/pagination-edge-case`.
2. **Run `make check`** before pushing -- CI runs the same checks, so catching issues locally saves time.
3. **Keep PRs focused** -- one feature or fix per PR. Small PRs get reviewed faster.
4. **Write a clear description** -- explain what changed and why. Link to relevant issues.
5. **Add tests** -- new code needs tests. Bug fixes need a test that would have caught the bug.

## Code of Conduct

Be respectful and constructive. We're all here to build something useful.

## Questions?

Open an issue on [GitHub](https://github.com/SocialAPI-AI/socialapi-python/issues) or reach out at contact@social-api.ai.
