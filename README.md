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

Requires Python 3.11+.

## Quick Start

```python
from socialapi import SocialAPI

client = SocialAPI(api_key="sapi_key_...")

# List connected accounts
for account in client.accounts.list():
    print(f"{account.platform}: {account.name}")

# Reply to a comment
client.comments.reply("ip_123", account_id="acc_ig_001", text="Thanks for the feedback!")

# Publish a post to multiple platforms
post = client.publishing.create(
    text="Hello from the API!",
    targets=[
        {"account_id": "acc_ig_001"},
        {"account_id": "acc_fb_002"},
    ],
)
```

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
        accounts = await client.accounts.list()
        async for account in accounts:
            print(account.name)

asyncio.run(main())
```

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

# List comments on a specific post
comments = client.comments.list("ip_123", account_id="acc_ig_001")

# Reply to a comment (threaded)
client.comments.reply("ip_123", account_id="acc_ig_001", text="Thanks!", comment_id="cmt_456")

# Moderate
client.comments.hide("ip_123", "cmt_456", account_id="acc_ig_001")
client.comments.like("ip_123", "cmt_456", account_id="acc_ig_001")
client.comments.delete("ip_123", "cmt_456", account_id="acc_ig_001")
```

### Direct Messages

```python
# List conversations
conversations = client.conversations.list(platform="instagram")

# Read messages in a thread
messages = client.conversations.list_messages("conv_001")

# Reply
client.conversations.send_message("conv_001", account_id="acc_ig_001", text="Hi there!")
client.conversations.mark_as_read("conv_001")
```

### Reviews

```python
# List reviews across Google Business Profile
reviews = client.reviews.list(platform="google")

# Reply to a review
client.reviews.reply("rev_789", account_id="acc_goog_001", text="Thank you for the kind words!")
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

### Events

```python
# List recent events (post publishes, account connections, etc.)
response = client.events.list(category="post", limit=10)
for event in response.events:
    print(f"{event.action}: {event.summary}")
```

### Webhooks

```python
# Subscribe to events
webhook = client.webhooks.create(
    url="https://example.com/webhook",
    events=["comment.received", "dm.received"],
)
print(f"Secret: {webhook.secret}")  # shown only once

# Update
client.webhooks.update(webhook.id, is_active=False)
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
