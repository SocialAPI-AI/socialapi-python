from __future__ import annotations

from .conftest import BASE_URL

MEDIA_ITEM_JSON = {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "filename": "photo.jpg",
    "content_type": "image/jpeg",
    "size_bytes": 2048576,
    "status": "ready",
    "url": "https://s3.example.com/media/photo.jpg",
    "created_at": "2026-03-20T09:00:00Z",
}


def test_list_media(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media",
        json={"data": [MEDIA_ITEM_JSON], "count": 1},
    )
    items = client.media.list()
    assert len(items) == 1
    assert items[0].filename == "photo.jpg"
    assert items[0].size_bytes == 2048576


def test_get_upload_url(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/upload-url?media_type=image%2Fjpeg&filename=photo.jpg",
        json={
            "media_id": "media_001",
            "upload_url": "https://storage.example.com/presigned/abc123",
            "expires_at": "2026-03-20T11:00:00Z",
        },
    )
    result = client.media.get_upload_url(media_type="image/jpeg", filename="photo.jpg")
    assert result.media_id == "media_001"


def test_verify_media(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/media_001/verify",
        status_code=204,
    )
    client.media.verify("media_001")


def test_delete_media(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/media_001",
        status_code=204,
    )
    client.media.delete("media_001")


def test_get_storage_usage(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/storage",
        json={"used_bytes": 52428800, "limit_bytes": 104857600, "count": 12},
    )
    usage = client.media.get_storage_usage()
    assert usage.used_bytes == 52428800
    assert usage.limit_bytes == 104857600
    assert usage.count == 12


async def test_list_media_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media",
        json={"data": [MEDIA_ITEM_JSON], "count": 1},
    )
    items = await async_client.media.list()
    assert len(items) == 1
    assert items[0].filename == "photo.jpg"


async def test_get_storage_usage_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/storage",
        json={"used_bytes": 100, "limit_bytes": -1, "count": 1},
    )
    usage = await async_client.media.get_storage_usage()
    assert usage.limit_bytes == -1


async def test_delete_media_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/media_001",
        status_code=204,
    )
    await async_client.media.delete("media_001")
