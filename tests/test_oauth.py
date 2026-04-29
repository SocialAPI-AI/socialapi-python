from __future__ import annotations

from typing import TYPE_CHECKING

from .conftest import BASE_URL

if TYPE_CHECKING:
    from socialapi import AsyncSocialAPI, SocialAPI


URI_JSON = {
    "id": "ruri_001",
    "uri": "https://app.example.com/oauth/done",
    "label": "production",
    "created_at": "2026-04-10T12:00:00Z",
}


def test_oauth_list_redirect_uris(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/redirect-uris",
        json={"data": [URI_JSON], "count": 1},
    )
    uris = client.oauth.list_redirect_uris()
    assert len(uris) == 1
    assert uris[0].uri == "https://app.example.com/oauth/done"


def test_oauth_create_redirect_uri(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/redirect-uris",
        method="POST",
        status_code=201,
        json=URI_JSON,
    )
    created = client.oauth.create_redirect_uri(
        uri="https://app.example.com/oauth/done",
        label="production",
    )
    assert created.id == "ruri_001"


def test_oauth_delete_redirect_uri(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/redirect-uris/ruri_001",
        method="DELETE",
        status_code=204,
    )
    client.oauth.delete_redirect_uri("ruri_001")


def test_oauth_redirect_uri_delete_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/redirect-uris",
        json={"data": [URI_JSON], "count": 1},
    )
    uris = client.oauth.list_redirect_uris()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/redirect-uris/ruri_001",
        method="DELETE",
        status_code=204,
    )
    uris[0].delete()


async def test_oauth_list_redirect_uris_async(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/redirect-uris",
        json={"data": [URI_JSON], "count": 1},
    )
    uris = await async_client.oauth.list_redirect_uris()
    assert len(uris) == 1


async def test_oauth_redirect_uri_delete_via_bound_method_async(
    httpx_mock,
    async_client: AsyncSocialAPI,
) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/redirect-uris",
        json={"data": [URI_JSON], "count": 1},
    )
    uris = await async_client.oauth.list_redirect_uris()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/redirect-uris/ruri_001",
        method="DELETE",
        status_code=204,
    )
    await uris[0].delete()
