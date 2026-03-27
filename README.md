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

## Quick Start

```python
from socialapi import SocialAPI

client = SocialAPI(api_key="sapi_key_...")

# List connected accounts
for account in client.accounts.list():
    print(f"{account.platform}: {account.account_name}")

# Reply to a comment
client.comments.reply(post_id="ip_123", text="Thanks for the feedback!")

# Publish a post to multiple platforms
post = client.publishing.create(
    text="Hello from the API!",
    platforms=[{"platform": "instagram", "account_id": "acc_ig_001"}],
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
            print(account.account_name)

asyncio.run(main())
```

## Usage Examples

### Comments

```python
# List posts with comments
posts = client.comments.list_posts(platform="instagram")

# List comments on a specific post
comments = client.comments.list(post_id="ip_123")

# Moderate
client.comments.hide(post_id="ip_123", comment_id="cmt_456")
client.comments.like(post_id="ip_123", comment_id="cmt_456")
client.comments.delete(post_id="ip_123", comment_id="cmt_456")
```

### Direct Messages

```python
# List conversations
conversations = client.conversations.list(platform="instagram")

# Read messages in a thread
messages = client.conversations.list_messages(conversation_id="conv_001")

# Reply
client.conversations.send_message(conversation_id="conv_001", text="Hi there!")
client.conversations.mark_as_read(conversation_id="conv_001")
```

### Reviews

```python
# List reviews across Google Business Profile
reviews = client.reviews.list(platform="google")

# Reply to a review
client.reviews.reply(review_id="rev_789", text="Thank you for the kind words!")
```

### Publishing

```python
# Create and schedule a post
from datetime import datetime, timezone

post = client.publishing.create(
    text="Scheduled post!",
    platforms=[
        {"platform": "instagram", "account_id": "acc_ig_001"},
        {"platform": "facebook", "account_id": "acc_fb_002"},
    ],
    scheduled_at=datetime(2026, 4, 1, 12, 0, tzinfo=timezone.utc).isoformat(),
)

# Validate before publishing
result = client.publishing.validate(
    text="Check this post",
    platforms=["instagram"],
    account_ids=["acc_ig_001"],
)
if not result.valid:
    for issue in result.errors:
        print(f"{issue.platform}: {issue.message}")
```

### Webhooks

```python
# Subscribe to events
webhook = client.webhooks.create(
    url="https://example.com/webhook",
    events=["comment.received", "dm.received"],
)

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
    client.comments.reply(post_id="ip_123", text="Hello")
except AuthenticationError:
    print("Invalid API key")
except NotFoundError:
    print("Post not found")
except RateLimitError as e:
    print(f"Rate limited: retry after checking headers")
except SocialAPIError as e:
    print(f"API error {e.status_code}: {e.message}")
```

| HTTP Status | Exception | When |
|---|---|---|
| 400 | `BadRequestError` | Invalid parameters |
| 401 | `AuthenticationError` | Bad or missing API key |
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
post = client.posts.get(post_id="p_123", timeout=60.0)
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
