from __future__ import annotations

from .conftest import BASE_URL

INVITE_JSON = {
    "id": "inv_001",
    "platform": "facebook",
    "token": "a55755cf75f73b56deb3dfe0c993fd36fc4c2bfa7",
    "url": "https://api.social-api.ai/invite/a55755cf...",
    "expires_at": "2026-04-03T12:00:00Z",
}

INVITE_LIST_ITEM_JSON = {
    **INVITE_JSON,
    "is_active": True,
    "created_at": "2026-03-27T12:00:00Z",
}


def test_create_invite(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/invites",
        json=INVITE_JSON,
    )
    invite = client.invites.create(brand_id="b_001", platform="facebook", expires_in_days=7)
    assert invite.id == "inv_001"
    assert invite.platform == "facebook"
    assert invite.token.startswith("a55755")


def test_list_invites(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/invites?brand_id=b_001",
        json={"data": [INVITE_LIST_ITEM_JSON], "count": 1},
    )
    invites = client.invites.list("b_001")
    assert len(invites) == 1
    assert invites[0].is_active is True


def test_revoke_invite(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/invites/inv_001",
        status_code=204,
    )
    client.invites.revoke("inv_001")


async def test_create_invite_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/invites",
        json=INVITE_JSON,
    )
    invite = await async_client.invites.create(brand_id="b_001", platform="facebook")
    assert invite.id == "inv_001"


async def test_list_invites_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/invites?brand_id=b_001",
        json={"data": [INVITE_LIST_ITEM_JSON], "count": 1},
    )
    invites = await async_client.invites.list("b_001")
    assert len(invites) == 1


async def test_revoke_invite_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/invites/inv_001",
        status_code=204,
    )
    await async_client.invites.revoke("inv_001")
