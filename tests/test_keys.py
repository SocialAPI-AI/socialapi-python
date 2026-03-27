from __future__ import annotations

from .conftest import BASE_URL

KEY_JSON = {
    "id": "key_001",
    "name": "Production Key",
    "preview": "sapi_",
    "is_active": True,
    "last_used_at": "2026-03-20T15:00:00Z",
    "created_at": "2026-03-01T10:00:00Z",
}


def test_list_keys(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/keys",
        json={"data": [KEY_JSON]},
    )
    keys = client.keys.list()
    assert len(keys) == 1
    assert keys[0].id == "key_001"
    assert keys[0].name == "Production Key"
    assert keys[0].is_active is True


def test_create_key(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/keys",
        json={
            "id": "key_002",
            "name": "Staging Key",
            "raw_key": "sapi_key_0123456789abcdef",
            "message": "Save this key -- it will not be shown again.",
        },
    )
    result = client.keys.create(name="Staging Key")
    assert result.id == "key_002"
    assert result.raw_key == "sapi_key_0123456789abcdef"

    import json

    request = httpx_mock.get_requests()[0]
    body = json.loads(request.content)
    assert body["name"] == "Staging Key"


def test_revoke_key(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/keys/key_001",
        status_code=204,
    )
    client.keys.revoke("key_001")


async def test_list_keys_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/keys",
        json={"data": [KEY_JSON]},
    )
    keys = await async_client.keys.list()
    assert len(keys) == 1
    assert keys[0].name == "Production Key"


async def test_create_key_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/keys",
        json={
            "id": "key_async_001",
            "name": "Async Key",
            "raw_key": "sapi_key_async_abc123",
            "message": "Save this key -- it will not be shown again.",
        },
    )
    result = await async_client.keys.create(name="Async Key")
    assert result.id == "key_async_001"
    assert result.raw_key == "sapi_key_async_abc123"


async def test_revoke_key_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/keys/key_001",
        status_code=204,
    )
    await async_client.keys.revoke("key_001")
