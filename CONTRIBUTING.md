# Contributing

The client in `src/socialapi` is generated, so a change to it belongs in the API's OpenAPI spec, not here. Open an issue describing the problem instead.

Changes to the hand-written parts (`extras/`, `templates/`, `tests/`, `scripts/`, the workflow) are welcome. To check them locally:

```bash
bash scripts/generate.sh
uv run --with pytest --with-editable . pytest -q
```
