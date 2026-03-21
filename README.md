# SocialAPI Python SDK

[![PyPI version](https://img.shields.io/pypi/v/socialapi.svg)](https://pypi.org/project/socialapi/)
[![Python versions](https://img.shields.io/pypi/pyversions/socialapi.svg)](https://pypi.org/project/socialapi/)
[![CI](https://github.com/social-api-ai/socialapi-python/actions/workflows/ci.yml/badge.svg)](https://github.com/social-api-ai/socialapi-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

The official Python SDK for [SocialAPI](https://social-api.ai) -- a unified social media inbox API that reads and responds to comments, DMs, reviews, and mentions across Instagram, Facebook, Google Reviews, TikTok, YouTube, X/Twitter, Trustpilot, and LinkedIn through a single REST API.

## Installation

```bash
pip install socialapi
```

Requires Python 3.10 or later.

## Quick Start

### Synchronous

```python
from socialapi import SocialAPI

client = SocialAPI(api_key="sapi_key_...")

# List connected accounts
accounts = client.accounts.list()
for account in accounts.data:
    print(f"{account.platform}: {account.name}")

# List comments on a post
comments = client.comments.list("acc_123", "post_456")
for comment in comments.data:
    print(comment.content.text)

# Reply to a comment
reply = client.interactions.reply("acc_123", "sapi_cmt_abc", text="Thanks!")
```

### Asynchronous

```python
import asyncio
from socialapi import AsyncSocialAPI

async def main():
    async with AsyncSocialAPI(api_key="sapi_key_...") as client:
        accounts = await client.accounts.list()
        for account in accounts.data:
            print(f"{account.platform}: {account.name}")

asyncio.run(main())
```

## Authentication

Pass your API key directly or set the `SOCIALAPI_API_KEY` environment variable:

```python
# Explicit
client = SocialAPI(api_key="sapi_key_...")

# From environment variable
import os
os.environ["SOCIALAPI_API_KEY"] = "sapi_key_..."
client = SocialAPI()
```

API keys are created in the [SocialAPI dashboard](https://app.social-api.ai/keys) or via the API. The full key is shown once at creation -- store it securely.

## Usage Examples

### Managing Accounts

```python
# Connect a new account via OAuth
result = client.accounts.connect("instagram", metadata={"redirect_uri": "https://..."})

# Disconnect an account
client.accounts.disconnect("acc_123")
```

### Publishing Posts

```python
# Create a post across multiple accounts
post = client.posts.create(
    account_ids=["acc_123", "acc_456"],
    text="Hello from SocialAPI!",
)

# Schedule a post
post = client.posts.create(
    account_ids=["acc_123"],
    text="Scheduled post",
    scheduled_at="2026-04-01T12:00:00Z",
)
```

### Direct Messages

```python
# List DM threads
dms = client.dms.list("acc_123")

# Send a DM
client.dms.send("acc_123", thread_id="thread_789", text="Hello!")
```

### Media Upload

```python
# Upload media for use in posts
upload_info = client.media.upload_url(media_type="image", filename="photo.jpg")
# Upload to the presigned URL, then verify:
client.media.verify(media_id=upload_info.id)
```

## Error Handling

The SDK raises typed exceptions for all API errors:

```python
from socialapi import (
    SocialAPIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    PlanLimitError,
    PlatformRateLimitError,
    ValidationError,
    NotSupportedError,
)

try:
    client.comments.list("acc_123", "post_456")
except NotFoundError as e:
    print(f"Not found: {e.message} (code: {e.code})")
except PlanLimitError:
    print("Monthly limit exceeded -- upgrade your plan")
except PlatformRateLimitError:
    print("Platform rate limit hit -- will auto-retry")
except AuthenticationError:
    print("Invalid API key")
except SocialAPIError as e:
    print(f"API error {e.status_code}: {e.message}")
```

## Pagination

### Single Page

```python
response = client.comments.list("acc_123", "post_456", limit=10)
print(response.data)   # list of comments
print(response.count)  # total count
```

### Auto-Pagination

```python
# Synchronous -- iterates through all pages automatically
for comment in client.comments.list_auto("acc_123", "post_456"):
    print(comment.content.text)

# Asynchronous
async for comment in async_client.comments.list_auto("acc_123", "post_456"):
    print(comment.content.text)
```

## Configuration

```python
client = SocialAPI(
    api_key="sapi_key_...",
    base_url="https://api.social-api.ai",  # default
    timeout=30.0,                           # seconds, default
    max_retries=3,                          # default
)
```

### Context Manager

Both clients support context managers for proper resource cleanup:

```python
with SocialAPI(api_key="sapi_key_...") as client:
    accounts = client.accounts.list()

async with AsyncSocialAPI(api_key="sapi_key_...") as client:
    accounts = await client.accounts.list()
```

### Custom HTTP Client

For advanced use cases, inject your own httpx client:

```python
import httpx

http_client = httpx.Client(verify=False)  # custom SSL settings, proxies, etc.
client = SocialAPI(api_key="sapi_key_...", http_client=http_client)
```

## API Reference

For full endpoint documentation, visit [docs.social-api.ai](https://docs.social-api.ai).

### Resources

| Resource | Description |
|---|---|
| `client.accounts` | Manage connected social accounts |
| `client.posts` | Create, update, delete, and retry posts |
| `client.comments` | List and moderate comments |
| `client.interactions` | Reply to comments, reviews, and mentions |
| `client.dms` | List and send direct messages |
| `client.reviews` | List reviews |
| `client.mentions` | List mentions |
| `client.media` | Upload and manage media files |
| `client.usage` | Check usage statistics |
| `client.keys` | Manage API keys |
| `client.users` | Manage user profile |
| `client.webhooks` | Configure webhook endpoints |
| `client.billing` | Manage billing and subscriptions |
| `client.oauth` | OAuth token exchange |
| `client.search` | Search across accounts |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, testing, and PR guidelines.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
