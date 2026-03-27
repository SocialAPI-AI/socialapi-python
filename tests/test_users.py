from __future__ import annotations

from .conftest import BASE_URL

USER_JSON = {
    "id": "usr_001",
    "email": "dev@example.com",
    "plan": "starter",
    "onboarding": False,
    "avatar_url": "https://cdn.example.com/avatar.jpg",
    "beta_tester": True,
    "allowed_platforms": ["instagram", "facebook", "threads"],
}


def test_get_me(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        json=USER_JSON,
    )
    user = client.users.get_me()
    assert user.id == "usr_001"
    assert user.email == "dev@example.com"
    assert user.plan == "starter"
    assert user.beta_tester is True
    assert user.allowed_platforms == ["instagram", "facebook", "threads"]


def test_update_me(httpx_mock, client) -> None:
    updated = {**USER_JSON, "onboarding": True}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        json=updated,
    )
    user = client.users.update_me(onboarding=True)
    assert user.onboarding is True

    import json

    request = httpx_mock.get_requests()[0]
    body = json.loads(request.content)
    assert body["onboarding"] is True


def test_delete_me(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        status_code=204,
    )
    client.users.delete_me()


def test_update_me_with_all_fields(httpx_mock, client) -> None:
    updated = {**USER_JSON, "onboarding": False, "use_case": "saas", "referral": "twitter"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        json=updated,
    )
    user = client.users.update_me(onboarding=False, use_case="saas", referral="twitter")
    assert user.onboarding is False

    import json

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["onboarding"] is False
    assert body["use_case"] == "saas"
    assert body["referral"] == "twitter"


async def test_get_me_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        json=USER_JSON,
    )
    user = await async_client.users.get_me()
    assert user.id == "usr_001"
    assert user.email == "dev@example.com"


async def test_update_me_async(httpx_mock, async_client) -> None:
    updated = {**USER_JSON, "onboarding": True, "use_case": "agency"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        json=updated,
    )
    user = await async_client.users.update_me(onboarding=True, use_case="agency", referral="friend")
    assert user.onboarding is True


async def test_delete_me_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        status_code=204,
    )
    await async_client.users.delete_me()
