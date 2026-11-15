# SocialAPI Python SDK

Official Python client for the [SocialAPI](https://social-api.ai) REST API. Requires Python 3.11 or newer.

```bash
pip install socialapi
```

```python
from socialapi import AuthenticatedClient
from socialapi.api.brands import get_brands

client = AuthenticatedClient(base_url="https://api.social-api.ai/v1", token="sapi_key_...")
brands = get_brands.sync(client=client)
```

Every endpoint is a module under `socialapi.api.<tag>` with `sync`, `sync_detailed`, `asyncio` and `asyncio_detailed` functions. The API reference is at [docs.social-api.ai](https://docs.social-api.ai).

## Verifying webhooks

```python
from socialapi.webhooks import verify_webhook

if not verify_webhook("whsec_...", raw_body, request.headers):
    return 401
```

Pass the raw request body, before JSON decoding. Deliveries older than 5 minutes are rejected.

## How this package is built

The code under `src/socialapi` is generated from the API's OpenAPI spec by [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). Do not edit it: every release regenerates it. Hand-written code lives in `extras/` (copied in by `scripts/generate.sh`) and `templates/`. Releases are fully automated by `.github/workflows/release.yml`, and versions follow semver from the spec diff.
