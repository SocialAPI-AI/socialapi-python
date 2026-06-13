from __future__ import annotations

from socialapi._pagination import AsyncCursorPage, CursorPage
from socialapi.models.publishing import MediaUploadResponse

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


def test_list_media_returns_cursor_page(httpx_mock, client) -> None:
    """list() must return a CursorPage, not a bare list."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media",
        json={"data": [MEDIA_ITEM_JSON], "count": 1},
    )
    page = client.media.list()
    assert isinstance(page, CursorPage)
    assert len(page.data) == 1
    assert page.data[0].filename == "photo.jpg"
    assert page.data[0].size_bytes == 2048576


def test_list_media_pagination_cursor(httpx_mock, client) -> None:
    """list() propagates cursor from the response envelope."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media",
        json={"data": [MEDIA_ITEM_JSON], "count": 2, "cursor": "abc123"},
    )
    page = client.media.list()
    assert isinstance(page, CursorPage)
    assert page.next_cursor == "abc123"
    assert page.has_more is True


def test_list_media_no_cursor(httpx_mock, client) -> None:
    """list() without a cursor in the response has no next page."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media",
        json={"data": [MEDIA_ITEM_JSON], "count": 1},
    )
    page = client.media.list()
    assert page.next_cursor is None
    assert page.has_more is False


def test_list_media_with_params(httpx_mock, client) -> None:
    """limit and cursor query params are forwarded."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media?limit=5&cursor=tok",
        json={"data": [], "count": 0},
    )
    page = client.media.list(limit=5, cursor="tok")
    assert isinstance(page, CursorPage)
    assert len(page.data) == 0


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


def test_upload_multipart(httpx_mock, client) -> None:
    """upload() sends a multipart/form-data request with a 'file' field."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/upload",
        json={"media_id": "media_new_001"},
        status_code=201,
    )
    result = client.media.upload(content=b"fake image bytes", filename="photo.jpg")
    assert isinstance(result, MediaUploadResponse)
    assert result.media_id == "media_new_001"
    # Verify the request used multipart (content-type header includes multipart)
    request = httpx_mock.get_request()
    assert request is not None
    content_type = request.headers.get("content-type", "")
    assert "multipart/form-data" in content_type


def test_upload_multipart_with_content_type(httpx_mock, client) -> None:
    """upload() accepts an explicit content_type for the file part."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/upload",
        json={"media_id": "media_new_002"},
        status_code=201,
    )
    result = client.media.upload(
        content=b"fake image bytes",
        filename="photo.jpg",
        content_type="image/jpeg",
    )
    assert result.media_id == "media_new_002"


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


async def test_list_media_async_returns_cursor_page(httpx_mock, async_client) -> None:
    """Async list() must return an AsyncCursorPage."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media",
        json={"data": [MEDIA_ITEM_JSON], "count": 1},
    )
    page = await async_client.media.list()
    assert isinstance(page, AsyncCursorPage)
    assert len(page.data) == 1
    assert page.data[0].filename == "photo.jpg"


async def test_list_media_async_cursor_propagated(httpx_mock, async_client) -> None:
    """Async list() propagates cursor field."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media",
        json={"data": [MEDIA_ITEM_JSON], "count": 2, "cursor": "xyz"},
    )
    page = await async_client.media.list()
    assert page.next_cursor == "xyz"
    assert page.has_more is True


async def test_upload_multipart_async(httpx_mock, async_client) -> None:
    """Async upload() sends multipart/form-data."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/upload",
        json={"media_id": "media_async_001"},
        status_code=201,
    )
    result = await async_client.media.upload(content=b"async bytes", filename="img.png")
    assert isinstance(result, MediaUploadResponse)
    assert result.media_id == "media_async_001"
    request = httpx_mock.get_request()
    assert request is not None
    content_type = request.headers.get("content-type", "")
    assert "multipart/form-data" in content_type


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
