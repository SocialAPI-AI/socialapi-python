"""Tests for media resource."""

from __future__ import annotations

import httpx
import pytest

from socialapi import AsyncSocialAPI, SocialAPI


@pytest.fixture
def api_key() -> str:
    return "sapi_key_test_0123456789abcdef"


@pytest.fixture
def client(api_key: str) -> SocialAPI:
    return SocialAPI(api_key=api_key, base_url="https://api.social-api.ai")


@pytest.fixture
def async_client(api_key: str) -> AsyncSocialAPI:
    return AsyncSocialAPI(api_key=api_key, base_url="https://api.social-api.ai")


MEDIA_ID = "med_001"

MEDIA_ITEM_DATA = {
    "id": MEDIA_ID,
    "filename": "photo.png",
    "content_type": "image/png",
    "size_bytes": 102400,
    "status": "ready",
    "url": "https://cdn.social-api.ai/media/photo.png",
    "created_at": "2025-01-10T09:00:00Z",
}


def test_media_upload_url(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/media/upload-url",
            params={"media_type": "image/png", "filename": "photo.png"},
        ),
        json={
            "media_id": "med_new_001",
            "upload_url": "https://storage.example.com/upload?token=abc",
            "expires_at": "2025-01-15T10:00:00Z",
        },
    )
    result = client.media.upload_url("image/png", "photo.png")
    assert result.media_id == "med_new_001"
    assert "storage.example.com" in result.upload_url
    assert result.expires_at == "2025-01-15T10:00:00Z"


def test_media_verify(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/media/med_001/verify",
        method="POST",
        json={"success": True},
    )
    result = client.media.verify(MEDIA_ID)
    assert result.success is True


def test_media_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/media",
            params={"limit": "50"},
        ),
        json={"data": [MEDIA_ITEM_DATA], "count": 1, "cursor": None},
    )
    result = client.media.list()
    assert result.count == 1
    assert len(result.data) == 1
    assert result.data[0].id == MEDIA_ID
    assert result.data[0].filename == "photo.png"
    assert result.data[0].size_bytes == 102400


def test_media_delete(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/media/med_001",
        method="DELETE",
        status_code=204,
    )
    result = client.media.delete(MEDIA_ID)
    assert result is None


def test_media_storage(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/media/storage",
        json={"used_bytes": 5242880, "limit_bytes": 104857600, "count": 12},
    )
    result = client.media.storage()
    assert result.used_bytes == 5242880
    assert result.limit_bytes == 104857600
    assert result.count == 12


async def test_async_media_upload_url(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/media/upload-url",
            params={"media_type": "image/png", "filename": "photo.png"},
        ),
        json={
            "media_id": "med_new_001",
            "upload_url": "https://storage.example.com/upload?token=abc",
            "expires_at": "2025-01-15T10:00:00Z",
        },
    )
    result = await async_client.media.upload_url("image/png", "photo.png")
    assert result.media_id == "med_new_001"


async def test_async_media_delete(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/media/med_001",
        method="DELETE",
        status_code=204,
    )
    result = await async_client.media.delete(MEDIA_ID)
    assert result is None
