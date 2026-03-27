.PHONY: install test lint format typecheck check publish

install:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

typecheck:
	pyright src/

check:
	ruff check . && ruff format . --check && pyright src/ && pytest

publish:
	@if [ -z "$(v)" ]; then echo "Usage: make publish v=0.0.2"; exit 1; fi
	@echo "Publishing v$(v)..."
	sed -i 's/__version__ = ".*"/__version__ = "$(v)"/' src/socialapi/_version.py
	git add src/socialapi/_version.py
	git commit -m "release v$(v)"
	git tag "v$(v)"
	git push origin main "v$(v)"
