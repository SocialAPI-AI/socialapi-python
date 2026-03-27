from __future__ import annotations

from .conftest import BASE_URL

BRAND_JSON = {
    "id": "b_001",
    "name": "Acme Corp",
    "accounts_count": 3,
    "created_at": "2026-03-14T09:00:00Z",
    "updated_at": "2026-03-14T09:00:00Z",
}


def test_list_brands(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands",
        json={"data": [BRAND_JSON], "count": 1},
    )
    brands = client.brands.list()
    assert len(brands) == 1
    assert brands[0].id == "b_001"
    assert brands[0].name == "Acme Corp"
    assert brands[0].accounts_count == 3


def test_create_brand(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands",
        json=BRAND_JSON,
    )
    brand = client.brands.create(name="Acme Corp")
    assert brand.id == "b_001"
    assert brand.name == "Acme Corp"


def test_update_brand(httpx_mock, client) -> None:
    updated = {**BRAND_JSON, "name": "Acme Corporation"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands/b_001",
        json=updated,
    )
    brand = client.brands.update("b_001", name="Acme Corporation")
    assert brand.name == "Acme Corporation"


def test_delete_brand(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands/b_001",
        status_code=204,
    )
    client.brands.delete("b_001")


async def test_list_brands_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands",
        json={"data": [BRAND_JSON], "count": 1},
    )
    brands = await async_client.brands.list()
    assert len(brands) == 1
    assert brands[0].name == "Acme Corp"


async def test_create_brand_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands",
        json=BRAND_JSON,
    )
    brand = await async_client.brands.create(name="Acme Corp")
    assert brand.id == "b_001"


async def test_delete_brand_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands/b_001",
        status_code=204,
    )
    await async_client.brands.delete("b_001")
