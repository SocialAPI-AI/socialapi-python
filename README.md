# SocialAPI Python SDK

[![CI](https://github.com/SocialAPI-AI/socialapi-python/actions/workflows/ci.yml/badge.svg)](https://github.com/SocialAPI-AI/socialapi-python/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/socialapi.svg)](https://pypi.org/project/socialapi/)
[![Python](https://img.shields.io/pypi/pyversions/socialapi.svg)](https://pypi.org/project/socialapi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

The official Python client for the [SocialAPI](https://social-api.ai) REST API -- a unified inbox for comments, DMs, reviews, mentions, and publishing across Instagram, Facebook, Threads, TikTok, Google Business Profile, and LinkedIn.

## Installation

```bash
pip install socialapi
```

Requires Python 3.10+.

## Quick Start

```python
from socialapi import SocialAPI

client = SocialAPI(api_key="sapi_key_...")

# List connected accounts
for account in client.accounts.list():
    print(f"{account.platform}: {account.name}")

# Reply to a comment via the resource API
client.comments.reply("ip_123", account_id="acc_ig_001", text="Thanks for the feedback!")

# Or use the active-record API: each returned object is bound to the client
posts = client.comments.list_posts(account_id="acc_ig_001").data
last_post = posts[0]

for comment in last_post.list_comments():
    if "spam" in comment.text:
        comment.hide()
    else:
        comment.reply(text="Thanks!")

# Publish a post to multiple platforms
post = client.publishing.create(
    text="Hello from the API!",
    targets=[
        {"account_id": "acc_ig_001"},
        {"account_id": "acc_fb_002"},
    ],
)
```

### Two ways to call the API

Every list / get response returns models bound to the client, so action methods
work directly on the object — `comment.reply(...)`, `post.update(...)`,
`brand.delete()`. The resource API (`client.comments.reply(...)`) is still
available and equivalent. Pick whichever reads better for the call site.

```python
# Resource style — explicit, takes all IDs as arguments
client.comments.hide("ip_123", "cmt_456", account_id="acc_ig_001")

# Active-record style — IDs are inferred from the bound object
comment.hide()
```

Bound models built from raw JSON (`InboxComment.model_validate(payload)`)
have no client and will raise `UnboundModelError` if you try to call action
methods on them — fall back to the resource API in that case.

## Authentication

Pass your API key directly or set it as an environment variable:

```python
# Option 1: Constructor
client = SocialAPI(api_key="sapi_key_...")

# Option 2: Environment variable
#   export SOCIALAPI_API_KEY=sapi_key_...
client = SocialAPI()
```

You can generate API keys from the [SocialAPI dashboard](https://app.social-api.ai).

## Async Support

Every method has an async equivalent via `AsyncSocialAPI`:

```python
import asyncio
from socialapi import AsyncSocialAPI

async def main():
    async with AsyncSocialAPI(api_key="sapi_key_...") as client:
        async for comment in await client.conversations.list():
            await comment.send_message(text="hi")

asyncio.run(main())
```

Async resources return `Async*` model variants (`AsyncInboxComment`,
`AsyncPost`, `AsyncConversation`, …) whose action methods are awaitable.
Field shapes match the sync models exactly — the suffix only changes how the
methods dispatch.

## Usage Examples

### Brands

```python
# Create a brand to group accounts
brand = client.brands.create(name="Acme Corp")

# List all brands
for brand in client.brands.list():
    print(f"{brand.name} ({brand.accounts_count} accounts)")

# Update or delete
client.brands.update(brand.id, name="Acme Corporation")
client.brands.delete(brand.id)
```

### Comments

```python
# List posts with comments
posts = client.comments.list_posts(platform="instagram")

# Walk into a post's comments and act on them directly
for post in posts:
    for comment in post.list_comments():
        comment.reply(text="Thanks!")
        comment.like()
        # Threaded replies
        for reply in comment.list_replies():
            print(reply.text)

# Or stick with the resource API
client.comments.reply("ip_123", account_id="acc_ig_001", text="Thanks!", comment_id="cmt_456")
client.comments.hide("ip_123", "cmt_456", account_id="acc_ig_001")
client.comments.delete("ip_123", "cmt_456", account_id="acc_ig_001")
```

### Direct Messages

```python
# Walk into a conversation and reply on it directly
for conv in client.conversations.list(platform="instagram"):
    for message in conv.list_messages():
        print(f"{message.sender_name}: {message.text}")
    conv.send_message(text="Hi there!")
    conv.mark_as_read()
```

### Reviews

```python
# List reviews across Google Business Profile
for review in client.reviews.list(platform="google"):
    if review.rating >= 4:
        review.reply(text="Thank you!")
```

### Publishing

```python
from datetime import datetime, timezone

# Publish immediately
post = client.publishing.create(
    text="Check out our new product!",
    targets=[{"account_id": "acc_ig_001"}, {"account_id": "acc_fb_002"}],
)

# Schedule for later (pass a datetime directly)
post = client.publishing.create(
    text="Scheduled post!",
    targets=[{"account_id": "acc_ig_001"}],
    scheduled_at=datetime(2026, 4, 1, 12, 0, tzinfo=timezone.utc),
)

# Per-account text overrides
post = client.publishing.create(
    text="Default text",
    targets=[
        {"account_id": "acc_ig_001", "text": "Instagram-specific text"},
        {"account_id": "acc_li_002", "title": "LinkedIn Title", "visibility": "connections_only"},
    ],
)

# Validate before publishing
result = client.publishing.validate(text="Check this post", platforms=["instagram"])
if not result.valid:
    for issue in result.errors:
        print(f"{issue.platform}: {issue.message}")
```

### Media

```python
# Upload media for use in posts
upload = client.media.get_upload_url(media_type="image/jpeg", filename="photo.jpg")
# PUT the file to upload.upload_url, then verify:
client.media.verify(upload.media_id)

# List uploaded files
for item in client.media.list():
    print(f"{item.filename} ({item.size_bytes} bytes)")

# Check storage usage
usage = client.media.get_storage_usage()
print(f"Using {usage.used_bytes} of {usage.limit_bytes} bytes")
```

### Account Management

```python
# Inspect platform-specific creator settings (TikTok)
info = client.accounts.get_creator_info("acc_tt_001")
print(info.privacy_level_options, info.max_video_duration_sec)

# Manage Facebook Pages attached to an account
for page in client.accounts.list_pages("acc_fb_001"):
    if not page.is_default:
        page.update(is_default=True)

# Per-account platform quotas (e.g. Instagram posts_remaining)
limits = client.accounts.get_limits("acc_ig_001")
```

### Analytics Exports

```python
# Enqueue an export for a connected account (returns a bound Export)
export = client.accounts.export("acc_ig_001", include_transcript=True)

# Poll until done
while export.status not in ("completed", "failed"):
    export = export.refresh()

if export.status == "completed":
    print("Download:", export.download_url)
    for video in export.list_videos():
        print(video.url)

# Or list all recent jobs
for job in client.exports.list(status="completed"):
    print(job.id, job.completed_at)
```

### OAuth Redirect URIs

If you're building a multi-tenant app that redirects end-users through
SocialAPI's OAuth flow, you need to whitelist your callback URLs:

```python
# Whitelist a callback
uri = client.oauth.create_redirect_uri(
    uri="https://app.example.com/oauth/done",
    label="production",
)

# List and clean up
for u in client.oauth.list_redirect_uris():
    if "staging" in (u.label or ""):
        u.delete()
```

### Webhooks

```python
# Subscribe to events
webhook = client.webhooks.create(
    url="https://example.com/webhook",
    events=["comment.received", "dm.received"],
)
print(f"Secret: {webhook.secret}")  # shown only once

# Bound list returns objects you can act on directly
for hook in client.webhooks.list():
    if not hook.is_active:
        hook.delete()
```

## Pagination

List endpoints return a `CursorPage` that auto-paginates:

```python
# Iterate through all pages automatically
for post in client.posts.list(status="published"):
    print(post.text)

# Or control pagination manually
page = client.posts.list(limit=10)
print(f"Page has {len(page)} items, has_more={page.has_more}")
if page.has_more:
    next_page = page.next_page()
```

## Error Handling

The SDK raises typed exceptions mapped to API error codes:

```python
from socialapi import (
    SocialAPIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
)

try:
    client.comments.reply("ip_123", account_id="acc_001", text="Hello")
except AuthenticationError:
    print("Invalid API key")
except NotFoundError:
    print("Post not found")
except RateLimitError:
    print("Rate limited -- retry after backoff")
except SocialAPIError as e:
    print(f"API error {e.status_code}: {e.message}")
```

| HTTP Status | Exception | When |
|---|---|---|
| 400 | `BadRequestError` | Invalid parameters |
| 401 | `AuthenticationError` | Bad or missing API key |
| 403 | `ForbiddenError` | Permission denied |
| 404 | `NotFoundError` | Resource doesn't exist |
| 409 | `ConflictError` | Account already linked |
| 413 | `StorageQuotaExceededError` | Storage quota exceeded |
| 429 | `RateLimitError` | Rate limit hit |
| 500 | `InternalServerError` | Server error |
| 501 | `NotSupportedError` | Platform doesn't support this |

Network and timeout errors raise `APIConnectionError` and `APITimeoutError`.

When using the active-record API, `UnboundModelError` is raised if you call an
action method on a model that wasn't built by a client (e.g. one constructed
via `model_validate()`), and `MissingContextError` is raised if a required
contextual ID (like `account_id`) wasn't seeded — fall back to the resource
API in those cases.

## Configuration

```python
client = SocialAPI(
    api_key="sapi_key_...",
    base_url="https://api.social-api.ai",  # default
    timeout=30.0,                           # seconds, default
    max_retries=2,                          # default
    debug=False,                            # log raw HTTP requests/responses
)

# Per-request timeout override
post = client.posts.get("p_123", timeout=60.0)
```

The client automatically retries on 429 (rate limit) and 5xx errors with exponential backoff and jitter. The `Retry-After` header is respected when present.

## Resource Cleanup

Always close the client when done, or use it as a context manager:

```python
# Context manager (recommended)
with SocialAPI(api_key="...") as client:
    client.posts.list()

# Manual close
client = SocialAPI(api_key="...")
try:
    client.posts.list()
finally:
    client.close()
```

## Typed Enums

The SDK exports typed enums for API constants, enabling IDE autocomplete:

```python
from socialapi import Platform, PostStatus, WebhookEvent

# Use in filters
posts = client.posts.list(platform=Platform.INSTAGRAM, status=PostStatus.PUBLISHED)

# Use in webhook subscriptions
client.webhooks.create(url="...", events=[WebhookEvent.COMMENT_RECEIVED])
```

## API Reference

See the full API documentation at [docs.social-api.ai](https://docs.social-api.ai).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## License

MIT -- see [LICENSE](LICENSE) for details.
