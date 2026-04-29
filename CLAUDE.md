# SocialAPI Python SDK -- Claude Code Context

## What this is

Official Python client library for the [SocialAPI.ai](https://social-api.ai) REST API. Provides typed, ergonomic access to the unified social media inbox -- comments, DMs, reviews, mentions, publishing, and account management across Instagram, Facebook, Threads, TikTok, Google Business Profile, and LinkedIn.

**Package:** `socialapi` | **Python >= 3.10** | **License:** MIT

---

## Commands

All commands are defined in the `Makefile`. Use them as the single source of truth.

```bash
# Install (editable, with dev deps)
make install                  # pip install -e ".[dev]"

# Test
make test                     # pytest
pytest tests/test_accounts.py # single module
pytest -k "test_list"         # by name pattern
pytest --cov=socialapi        # with coverage

# Lint
make lint                     # ruff check .

# Format
make format                   # ruff format .

# Type check
make typecheck                # pyright src/

# Full quality gate (CI equivalent)
make check                    # ruff check + format --check + pyright + pytest

# Publish (tag-triggered PyPI release)
make publish v=0.1.0          # bumps _version.py, commits, tags, pushes
```

---

## Source layout

The SDK uses the **src layout** with `hatch` as the build backend. All source lives under `src/socialapi/`.

```
src/socialapi/
  __init__.py               <-- public surface: SocialAPI, AsyncSocialAPI, models, exceptions
  _version.py               <-- single version string (__version__ = "X.Y.Z")
  _client.py                <-- SocialAPI (sync) and AsyncSocialAPI (async) client classes
  _base_client.py           <-- shared HTTP logic, retry, error mapping, auth header injection
  _bound.py                 <-- _Bound base class + UnboundModelError / MissingContextError
  _exceptions.py            <-- exception hierarchy (SocialAPIError tree)
  _pagination.py            <-- CursorPage iterator and async iterator for cursor-based pagination
  _constants.py             <-- default base URL, user agent, timeouts, enums (Platform, ...)
  _config.py                <-- ClientConfig dataclass (immutable per-client settings)
  py.typed                  <-- PEP 561 marker (empty file, signals typed package)
  models/
    __init__.py
    accounts.py             <-- Account/AsyncAccount, Page/AsyncPage, CreatorInfo, Connect/OAuth*
    brands.py               <-- Brand/AsyncBrand
    comments.py             <-- InboxComment/AsyncInboxComment, CommentedPost/AsyncCommentedPost,
                                CommentCapabilities, ReplyToCommentResponse
    conversations.py        <-- Conversation/AsyncConversation, Message, SendMessageResponse
    exports.py              <-- Export/AsyncExport, ExportVideo, CreateExportRequest
    invites.py              <-- Invite/AsyncInvite, InviteListItem/AsyncInviteListItem
    keys.py                 <-- APIKey/AsyncAPIKey, CreateKeyResponse
    media.py                <-- MediaItem/AsyncMediaItem, StorageUsage
    mentions.py             <-- Mention, MentionAuthor, MentionContent, MentionMedia (data only)
    oauth.py                <-- OAuthRedirectURI/AsyncOAuthRedirectURI, CreateRedirectURIRequest
    posts.py                <-- Post/AsyncPost, PostTarget, PostMetrics, ValidationResult
    publishing.py           <-- Create/Update/Validate/Import request bodies, MediaUploadURL
    reviews.py              <-- Review/AsyncReview, ReplyToReviewResponse
    usage.py                <-- UsageResponse, AccountLimits (data only)
    users.py                <-- User (data only)
    webhooks.py             <-- Webhook/AsyncWebhook, CreateWebhookResponse
  resources/
    __init__.py
    accounts.py             <-- Accounts, AsyncAccounts
    brands.py               <-- Brands, AsyncBrands
    comments.py             <-- Comments, AsyncComments
    conversations.py        <-- Conversations, AsyncConversations
    exports.py              <-- Exports, AsyncExports
    invites.py              <-- Invites, AsyncInvites
    keys.py                 <-- Keys, AsyncKeys
    media.py                <-- Media, AsyncMedia
    mentions.py             <-- Mentions, AsyncMentions
    oauth.py                <-- OAuth, AsyncOAuth (redirect-uri whitelist management)
    posts.py                <-- Posts, AsyncPosts
    publishing.py           <-- Publishing, AsyncPublishing
    reviews.py              <-- Reviews, AsyncReviews
    usage.py                <-- Usage, AsyncUsage
    users.py                <-- Users, AsyncUsers
    webhooks.py             <-- Webhooks, AsyncWebhooks
tests/
  conftest.py               <-- shared fixtures (httpx_mock, client, async_client)
  test_accounts.py
  test_bound_models.py      <-- coverage for active-record action methods + ctx propagation
  test_brands.py
  test_client.py
  test_comments.py
  test_conversations.py
  test_exceptions.py
  test_exports.py
  test_invites.py
  test_keys.py
  test_media.py
  test_mentions.py
  test_oauth.py
  test_pagination.py
  test_posts.py
  test_publishing.py
  test_retry.py
  test_reviews.py
  test_usage.py
  test_users.py
  test_webhooks.py
```

### Naming rules

- **Filenames:** `snake_case.py`. Prefix internal/private modules with `_` (e.g. `_client.py`, `_base_client.py`).
- **Classes:** `PascalCase`. Resource classes match their REST noun (e.g. `Accounts`, `AsyncAccounts`).
- **Methods:** `snake_case`. Match the REST verb semantics (e.g. `list`, `create`, `get`, `update`, `delete`, `reply`, `hide`, `unhide`).
- **Constants:** `UPPER_SNAKE_CASE`.
- **Models:** `PascalCase` Pydantic `BaseModel` subclasses. Field names use `snake_case` matching the API JSON keys exactly.
- **Async-parallel models:** action-bearing models have a sync class (`InboxComment`, `Post`, `Conversation`, ...) and an `Async`-prefixed twin (`AsyncInboxComment`, `AsyncPost`, `AsyncConversation`). Both inherit shared fields from a private `_<Name>Base` class. Async resources return the `Async*` variant. Pure data models (`Message`, `Mention`, `User`, `Usage*`, `*Request`/`*Response` envelopes) are single classes — no `Async*` twin needed.

---

## Architecture decisions

### HTTP client: httpx

Use `httpx` for both sync (`httpx.Client`) and async (`httpx.AsyncClient`) transports. Do not use `requests` or `aiohttp`. httpx provides a unified API surface, HTTP/2 support, and is the standard for modern Python SDKs (OpenAI, Anthropic, Stripe all use it).

### Data models: Pydantic v2

All request parameters and response objects are Pydantic `BaseModel` subclasses with strict field types. Use `model_validate` for response parsing (not `parse_obj`). Leverage Pydantic v2 features: `model_config`, `field_validator`, `ConfigDict(populate_by_name=True)`.

### Dual sync + async clients

Expose two top-level client classes:

```python
from socialapi import SocialAPI, AsyncSocialAPI

# Sync
client = SocialAPI(api_key="sapi_key_...")
accounts = client.accounts.list()

# Async
async_client = AsyncSocialAPI(api_key="sapi_key_...")
accounts = await async_client.accounts.list()
```

Both clients expose identical resource properties with identical method signatures. The sync client wraps `httpx.Client`; the async client wraps `httpx.AsyncClient`.

### Resource-based client pattern

Each API domain is a resource class attached as a property on the client. Resource classes receive the base client (which holds the httpx transport, auth, base URL) and delegate HTTP calls to it.

```python
class Accounts:
    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(self, *, brand_id: str | None = None) -> CursorPage[Account]:
        params: dict[str, Any] = {}
        if brand_id is not None:
            params["brand_id"] = brand_id
        return self._client._get_paginated("/v1/accounts", params=params, model=Account)
```

There is one sync resource class and one async resource class per API domain. They live in the same file (e.g. `resources/accounts.py` contains both `Accounts` and `AsyncAccounts`).

### Active-record action methods (`_Bound` infrastructure)

Models returned by resource calls are bound to the client that produced them, so users can call action methods directly on the object instead of always going through the resource:

```python
post = client.comments.list_posts(account_id="acc_1").data[0]
for comment in post.list_comments():
    comment.hide()              # uses comment._client + comment._ctx["account_id"]
    comment.reply(text="Hi!")
```

Mechanics:

- `_bound._Bound` is a `BaseModel` subclass with two `PrivateAttr` fields: `_client` (the `BaseSyncClient` or `BaseAsyncClient`) and `_ctx: dict[str, Any]` (contextual IDs the model itself doesn't always carry, e.g. `account_id` on a `Comment`).
- Action-bearing domain models inherit from `_Bound` via a shared `_<Name>Base` (e.g. `_InboxCommentBase`); the sync and async leaves only override action methods.
- Resources call `_client._get_paginated(..., bind_ctx={...})` for list endpoints and `obj._bind(client, ctx)` for single-result endpoints. Pagination threads `bind_ctx` through `next_page()` so auto-fetched pages also bind.
- Inside an action method: `client = self._client_or_raise_sync()` (or `_async`); `account_id = self._ctx_value("account_id")`. These raise `UnboundModelError` / `MissingContextError` with a helpful message that points users back to the resource API.
- Models built via `Model.model_validate(json)` from raw JSON (no client) have `_client=None` and remain pure data — the user can still inspect fields, just not act.

The resource API is preserved for every endpoint and is the fallback when an unbound or partially-contextualized model is in hand.

### Cursor-based pagination

List endpoints return cursor-paginated results. Provide a `CursorPage[T]` generic type that:

1. Holds `data: list[T]`, `has_more: bool`, `next_cursor: str | None`.
2. Implements `__iter__` (sync) and `__aiter__` (async) for auto-pagination.
3. Exposes `.has_next_page()` and `.next_page()` / `await .next_page()` for manual control.

```python
# Auto-paginate all pages
for post in client.posts.list(status="published"):
    print(post.id)

# Manual pagination
page = client.posts.list(status="published", limit=10)
while page.has_next_page():
    page = page.next_page()
```

---

## Type safety requirements

- **pyright strict mode** is mandatory. The `pyproject.toml` sets `typeCheckingMode = "strict"`.
- **py.typed marker** (`src/socialapi/py.typed`) must exist as an empty file per PEP 561.
- All public functions, methods, and class attributes must have explicit type annotations. No `Any` in public signatures unless truly unavoidable (e.g. platform-specific metadata dicts).
- Use `from __future__ import annotations` in every file for PEP 604 union syntax (`str | None` instead of `Optional[str]`).
- Run `pyright --verifytypes socialapi` periodically to check type completeness for downstream consumers.

---

## Error handling

### Exception hierarchy

```
SocialAPIError (base)
  APIStatusError (HTTP 4xx/5xx from the API)
    BadRequestError          (400)
    AuthenticationError      (401)
    ForbiddenError           (403)
    NotFoundError            (404)
    ConflictError            (409)
    StorageQuotaExceededError (413)
    RateLimitError           (429)
    InternalServerError      (500)
    NotSupportedError        (501)
  APIConnectionError         (network failure, DNS, timeout)
    APITimeoutError          (request timed out)
  UnboundModelError          (action method called on a model with no _client)
  MissingContextError        (bound action needs a _ctx key that wasn't seeded)
```

### APIStatusError attributes

Every `APIStatusError` carries:

| Attribute | Type | Description |
|---|---|---|
| `status_code` | `int` | HTTP status code |
| `message` | `str` | Human-readable error from `error` JSON field |
| `code` | `str \| None` | Machine-readable code from `code` JSON field |
| `response` | `httpx.Response` | Raw httpx response for inspection |
| `body` | `dict[str, Any] \| None` | Parsed JSON body if available |

### Mapping from API error codes

| API `code` | HTTP | SDK Exception |
|---|---|---|
| `missing_metadata` | 400 | `BadRequestError` |
| `unsupported_platform` | 400 | `BadRequestError` |
| `unauthorized` | 401 | `AuthenticationError` |
| `invalid_token` | 401 | `AuthenticationError` |
| `invalid_credentials` | 401 | `AuthenticationError` |
| `account_not_found` | 404 | `NotFoundError` |
| `not_found` | 404 | `NotFoundError` |
| `account_already_linked` | 409 | `ConflictError` |
| `storage_quota_exceeded` | 413 | `StorageQuotaExceededError` |
| `rate_limit_exceeded` | 429 | `RateLimitError` |
| `platform_rate_limit` | 429 | `RateLimitError` |
| `not_supported` | 501 | `NotSupportedError` |
| *(none)* | 500 | `InternalServerError` |

### Usage pattern

```python
from socialapi import SocialAPI
from socialapi._exceptions import RateLimitError, NotSupportedError

client = SocialAPI(api_key="sapi_key_...")

try:
    reviews = client.reviews.list(account_id="acc_...")
except NotSupportedError:
    print("This platform does not support reviews")
except RateLimitError as e:
    print(f"Rate limited: {e.message} (code={e.code})")
```

---

## Testing patterns

### Framework

- **pytest** as the test runner.
- **pytest-asyncio** with `asyncio_mode = "auto"` for async tests (no `@pytest.mark.asyncio` needed).
- **pytest-httpx** for mocking httpx requests at the transport layer.
- **pytest-cov** for coverage reporting.

### Fixtures (conftest.py)

```python
import pytest
from socialapi import SocialAPI, AsyncSocialAPI

@pytest.fixture
def client(httpx_mock) -> SocialAPI:
    """Sync client wired to httpx_mock transport."""
    return SocialAPI(api_key="sapi_key_test", base_url="https://api.test.local")

@pytest.fixture
def async_client(httpx_mock) -> AsyncSocialAPI:
    """Async client wired to httpx_mock transport."""
    return AsyncSocialAPI(api_key="sapi_key_test", base_url="https://api.test.local")
```

### Test structure

Each test file corresponds to one resource module. Every public method on both sync and async resource classes must have at least one test. Test names follow `test_<resource>_<method>[_<scenario>]`.

```python
def test_accounts_list(httpx_mock, client):
    httpx_mock.add_response(
        url="https://api.test.local/v1/accounts",
        json={"data": [{"id": "acc_1", "platform": "instagram", ...}], "count": 1},
    )
    accounts = client.accounts.list()
    assert len(accounts) == 1
    assert accounts[0].platform == "instagram"


async def test_accounts_list_async(httpx_mock, async_client):
    httpx_mock.add_response(
        url="https://api.test.local/v1/accounts",
        json={"data": [], "count": 0},
    )
    accounts = await async_client.accounts.list()
    assert accounts == []
```

### What to test

- Response parsing into Pydantic models (happy path).
- Error mapping (mock a 401 response, assert `AuthenticationError` is raised with correct `code`).
- Pagination iteration (mock two pages, assert auto-pagination yields all items).
- Query parameter construction (assert the URL/params sent by httpx match expectations).
- Request body serialization for POST/PATCH/PUT/DELETE endpoints.
- Bound action methods (sync + async): both that they call the right URL/body and that calling them on an unbound model raises `UnboundModelError`. `test_bound_models.py` is the canonical home for these.
- Context propagation: when a parent (e.g. `CommentedPost`) calls `list_comments()`, child models must inherit `account_id` and `inbox_post_id` in their `_ctx` so subsequent action methods work without extra args.

### What NOT to test

- The SocialAPI server itself. The SDK tests mock all HTTP calls.
- httpx internals or Pydantic validation internals.

---

## Public API surface

The SDK exposes **only** the public API endpoints. The source of truth is the MCP tools in `core/api/mcp/tools_*.go`. The following table maps API domains to SDK resource classes and their methods.

### Endpoint scope rules (MANDATORY)

**NEVER** create modules for: `billing`, `provision`, `whitelist`, `media_library`, `search`, `subscriptions`, `plans`, `payments`. Even if the OpenAPI spec lists them (e.g. `/search`), they are out of scope for this SDK.

**ONLY** create modules for the resources listed below. The OpenAPI spec at `docs/api-reference/openapi.json` (in the SocAPI core repo) is the canonical source of truth for endpoint shape and schema; when in doubt, match it.

### Resource map

Resource methods (`client.<resource>.<method>`) and the active-record bound methods (`obj.<method>()`) are equivalent — the bound version just infers IDs from the object and its seeded `_ctx`.

| Resource class | REST endpoints | SDK resource methods | Bound action methods |
|---|---|---|---|
| **Accounts** | `GET /v1/accounts` | `list(brand_id?)` | — |
| | `POST /v1/accounts/connect` | `connect(platform, brand_id?, metadata?)` | — |
| | `POST /v1/oauth/exchange` | `exchange_oauth(platform, code, metadata)` | — |
| | `DELETE /v1/accounts/:id` | `disconnect(account_id)` | `Account.disconnect()` |
| | `GET /v1/accounts/:id/creator-info` | `get_creator_info(account_id)` | `Account.get_creator_info()` |
| | `GET /v1/accounts/:id/pages` | `list_pages(account_id)` | `Account.list_pages()` |
| | `PATCH /v1/accounts/:id/pages/:pageId` | `update_page(account_id, page_id, ...)` | `Page.update(...)` |
| | `POST /v1/accounts/:id/export` | `export(account_id, ...)` | `Account.export(...)` |
| | `GET /v1/accounts/:id/limits` | `get_limits(account_id)` | `Account.get_limits()` |
| **Brands** | `GET /v1/brands` | `list()` | — |
| | `POST /v1/brands` | `create(name)` | — |
| | `PATCH /v1/brands/:id` | `update(brand_id, name)` | `Brand.update(name)` |
| | `DELETE /v1/brands/:id` | `delete(brand_id)` | `Brand.delete()` |
| **Comments** | `GET /v1/inbox/comments` | `list_posts(account_id?, platform?, min_comments?, since?, ...)` | — |
| | `GET /v1/inbox/comments/:postId` | `list(inbox_post_id, account_id, ...)` | `CommentedPost.list_comments()` |
| | `POST /v1/inbox/comments/:postId` | `reply(post_id, account_id, text, comment_id?)` | `InboxComment.reply(text)`, `CommentedPost.reply(text)` |
| | `GET /v1/inbox/comments/:p/:c/replies` | `list_replies(post_id, comment_id, account_id, ...)` | `InboxComment.list_replies()` |
| | `DELETE /v1/inbox/comments/:p/:c` | `delete(post_id, comment_id, account_id)` | `InboxComment.delete()` |
| | `POST .../hide` | `hide(post_id, comment_id, account_id)` | `InboxComment.hide()` |
| | `DELETE .../hide` | `unhide(post_id, comment_id, account_id)` | `InboxComment.unhide()` |
| | `POST .../like` | `like(post_id, comment_id, account_id)` | `InboxComment.like()` |
| | `DELETE .../like` | `unlike(post_id, comment_id, account_id)` | `InboxComment.unlike()` |
| | `POST .../private-reply` | `private_reply(post_id, comment_id, account_id, text)` | `InboxComment.private_reply(text)` |
| **Conversations** | `GET /v1/inbox/conversations` | `list(account_id?, platform?, status?, ...)` | — |
| | `GET /v1/inbox/conversations/:id` | `get(conversation_id)` | — |
| | `PATCH /v1/inbox/conversations/:id` | `update(conversation_id, status)` | `Conversation.update(status)` |
| | `GET .../messages` | `list_messages(conversation_id, ...)` | `Conversation.list_messages()` |
| | `POST .../messages` | `send_message(conversation_id, account_id, text)` | `Conversation.send_message(text)` |
| | `POST .../read` | `mark_as_read(conversation_id)` | `Conversation.mark_as_read()` |
| **Exports** | `GET /v1/exports` | `list(status?)` | — |
| | `GET /v1/exports/:id` | `get(export_id)` | `Export.refresh()` |
| | `GET /exports/:id/videos` | `list_videos(export_id)` | `Export.list_videos()` |
| **Invites** | `GET /v1/invites` | `list(brand_id)` | — |
| | `POST /v1/invites` | `create(brand_id, platform, expires_in_days)` | — |
| | `DELETE /v1/invites/:id` | `revoke(invite_id)` | `Invite.revoke()`, `InviteListItem.revoke()` |
| **Keys** | `GET /v1/keys` | `list()` | — |
| | `POST /v1/keys` | `create(name)` | — |
| | `DELETE /v1/keys/:id` | `revoke(key_id)` | `APIKey.revoke()` |
| **Media** | `GET /v1/media` | `list(limit?, cursor?)` | — |
| | `GET /v1/media/upload-url` | `get_upload_url(media_type, filename)` | — |
| | `POST /v1/media/:id/verify` | `verify(media_id)` | `MediaItem.verify()` |
| | `GET /v1/media/storage` | `get_storage_usage()` | — |
| | `DELETE /v1/media/:id` | `delete(media_id)` | `MediaItem.delete()` |
| **Mentions** | `GET /v1/accounts/:id/mentions` | `list(account_id, since?, limit?, cursor?)` | — |
| **OAuth** | `GET /v1/oauth/redirect-uris` | `list_redirect_uris()` | — |
| | `POST /v1/oauth/redirect-uris` | `create_redirect_uri(uri, label?)` | — |
| | `DELETE /v1/oauth/redirect-uris/:id` | `delete_redirect_uri(uri_id)` | `OAuthRedirectURI.delete()` |
| **Posts** | `GET /v1/posts` | `list(account_ids?, status?, platform?, ...)` | — |
| | `GET /v1/posts/:pid` | `get(post_id)` | — |
| | `DELETE /v1/posts/:pid` | `delete(post_id)` | `Post.delete()` |
| | `POST /v1/posts/:pid/retry` | `retry(post_id)` | `Post.retry()` |
| | `POST /v1/posts/:pid/unpublish` | `unpublish(post_id, account_id?)` | `Post.unpublish(account_id?)` |
| | `GET /v1/posts/:pid/metrics` | `get_metrics(post_id)` | `Post.get_metrics()` |
| **Publishing** | `POST /v1/posts` | `create(text, targets?, scheduled_at?, ...)` | — |
| | `PATCH /v1/posts/:pid` | `update(post_id, text?, targets?, ...)` | `Post.update(...)` |
| | `GET /v1/posts/validate` | `get_constraints()` | — |
| | `POST /v1/posts/validate` | `validate(text, platforms?, account_ids?, ...)` | — |
| | `POST /v1/posts/import` | `import_posts(file, dry_run?)` | — |
| | `GET /v1/media/upload-url` | `get_upload_url(media_type, filename)` | — |
| | `POST /v1/media/:id/verify` | `verify_upload(media_id)` | — |
| **Reviews** | `GET /v1/inbox/reviews` | `list(account_id?, platform?, ...)` | — |
| | `POST /v1/inbox/reviews/:id/reply` | `reply(review_id, account_id, text)` | `Review.reply(text)` |
| | `PUT /v1/inbox/reviews/:id/reply` | `update_reply(review_id, account_id, text)` | `Review.update_reply(text)` |
| | `DELETE /v1/inbox/reviews/:id/reply` | `delete_reply(review_id, account_id)` | `Review.delete_reply()` |
| **Usage** | `GET /v1/usage` | `get()` | — |
| | `GET /v1/accounts/:id/limits` | `get_account_limits(account_id)` | — *(see `Account.get_limits()`)* |
| **Users** | `GET /v1/users/me` | `get_me()` | — |
| | `PATCH /v1/users/me` | `update_me(onboarding?)` | — |
| | `DELETE /v1/users/me` | `delete_me()` | — |
| **Webhooks** | `GET /v1/webhooks` | `list()` | — |
| | `POST /v1/webhooks` | `create(url, events)` | — |
| | `PATCH /v1/webhooks/:id` | `update(webhook_id, url?, events?, is_active?)` | `Webhook.update(...)` |
| | `DELETE /v1/webhooks/:id` | `delete(webhook_id)` | `Webhook.delete()` |

### Webhook signature verification utility

Expose a standalone helper (not tied to a client instance) for verifying inbound webhook signatures:

```python
from socialapi.webhooks import verify_signature

is_valid = verify_signature(
    secret="whsec_...",
    payload=request.body,
    signature=request.headers["X-SocialAPI-Signature"],
)
```

This uses HMAC-SHA256 with constant-time comparison (`hmac.compare_digest`).

---

## API conventions

### Authentication

All requests send `Authorization: Bearer <api_key>`. The `api_key` is passed to the client constructor and injected by `_base_client.py` into every request.

```python
client = SocialAPI(api_key="sapi_key_...")

# Or from environment variable
client = SocialAPI()  # reads SOCIALAPI_API_KEY env var
```

### Base URL

Default: `https://api.social-api.ai`. Override via constructor:

```python
client = SocialAPI(api_key="...", base_url="http://localhost:3000")
```

### Timeouts

Default timeout: 30 seconds. Override via constructor:

```python
client = SocialAPI(api_key="...", timeout=60.0)
```

### Retries

Implement automatic retries with exponential backoff for:

- Network errors (`APIConnectionError`)
- HTTP 429 (rate limited) -- respect `Retry-After` header if present
- HTTP 500+ (server errors)

Default: 2 retries (3 total attempts). Override via constructor:

```python
client = SocialAPI(api_key="...", max_retries=0)  # disable retries
```

### User agent

Send `User-Agent: socialapi-python/<version>` on every request.

### Pagination parameters

List methods accept `limit: int | None = None` and `cursor: str | None = None`. These map to `?limit=` and `?cursor=` query parameters. Default limit is server-controlled (25). Max 100.

---

## Supported platforms

The API supports these social media platforms. The SDK does not need platform-specific logic -- it passes platform strings through to the API.

| Platform | Key | Capabilities |
|---|---|---|
| Instagram | `instagram` | Posts, comments, DMs, mentions |
| Facebook | `facebook` | Posts, comments, DMs (Messenger) |
| Threads | `threads` | Posts, comments |
| TikTok | `tiktok` | Posts, comments |
| Google Business | `google` | Posts, reviews |
| LinkedIn | `linkedin` | Posts, comments |

---

## CI/CD

### GitHub Actions

Two workflows exist in `.github/workflows/`:

- **ci.yml** -- Runs on push/PR to main. Matrix: Python 3.10, 3.11, 3.12, 3.13. Steps: install, ruff check, ruff format --check, pyright, pytest with coverage.
- **publish.yml** -- Triggered by `v*` tags. Builds with `python -m build`, publishes to PyPI via trusted publisher (OIDC, no API token needed).

### Release process

1. Update version in `src/socialapi/_version.py`.
2. `make publish v=X.Y.Z` -- commits version bump, creates git tag, pushes both.
3. GitHub Actions builds and publishes to PyPI automatically.

---

## Versioning

- Follow [Semantic Versioning 2.0](https://semver.org/).
- Single version source: `src/socialapi/_version.py` with `__version__ = "X.Y.Z"`.
- Hatch reads version dynamically from this file (`[tool.hatch.version] path`).
- Pre-1.0: breaking changes bump minor (0.2.0 -> 0.3.0). Post-1.0: breaking changes bump major.

---

## Code quality standards

### Ruff configuration (from pyproject.toml)

- Target: Python 3.10
- Line length: 120
- Enabled rule sets: `E`, `W`, `F`, `I`, `N`, `UP`, `B`, `SIM`, `TCH`, `RUF`
- isort: `known-first-party = ["socialapi"]`

### Style rules

- Use `from __future__ import annotations` in every file.
- Prefer keyword-only arguments for SDK methods (use `*` separator).
- All public methods must have Google-style docstrings with Args, Returns, and Raises sections.
- Use `TypeAlias` for complex type aliases.
- No mutable default arguments. Use `None` + internal construction.
- Avoid star imports. Explicit imports only.

### Docstring format

```python
def list(
    self,
    *,
    brand_id: str | None = None,
) -> list[Account]:
    """List all connected social media accounts.

    Args:
        brand_id: Optional brand ID to filter accounts by.

    Returns:
        A list of connected accounts.

    Raises:
        AuthenticationError: If the API key is invalid.
    """
```

---

## Dependencies

### Runtime (required)

| Package | Min version | Purpose |
|---|---|---|
| `httpx` | >= 0.27.0 | HTTP client (sync + async) |
| `pydantic` | >= 2.0.0 | Response/request model validation |

### Dev (optional `[dev]` extra)

| Package | Min version | Purpose |
|---|---|---|
| `pytest` | >= 8.0 | Test runner |
| `pytest-asyncio` | >= 0.24 | Async test support |
| `pytest-httpx` | >= 0.30 | httpx request mocking |
| `pytest-cov` | >= 5.0 | Coverage reporting |
| `ruff` | >= 0.8 | Linting + formatting |
| `pyright` | >= 1.1 | Static type checking |
| `build` | >= 1.0 | Package building |

---

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `SOCIALAPI_API_KEY` | No | Default API key (used when no `api_key` is passed to constructor) |
| `SOCIALAPI_BASE_URL` | No | Override base URL (default: `https://api.social-api.ai`) |
