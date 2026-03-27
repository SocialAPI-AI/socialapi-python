from __future__ import annotations

from socialapi.models.accounts import ConnectOAuthResponse, OAuthExchangeResponse

from .conftest import BASE_URL

ACCOUNT_JSON = {
    "id": "acc_ig_001",
    "platform": "instagram",
    "name": "Test Instagram",
    "username": "testinsta",
    "brand_id": "brand_001",
}


def test_list_accounts(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.accounts.list()
    assert len(page.data) == 1
    assert page.data[0].id == "acc_ig_001"
    assert page.data[0].platform == "instagram"
    assert page.data[0].username == "testinsta"


def test_connect_account(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/connect",
        json={
            "auth_url": "https://instagram.com/oauth/authorize?client_id=...",
            "state": "random_state_123",
            "message": "Redirect user to auth_url",
        },
    )
    result = client.accounts.connect(platform="instagram", metadata={"redirect_uri": "https://app.local/callback"})
    assert isinstance(result, ConnectOAuthResponse)
    assert result.auth_url.startswith("https://instagram.com")
    assert result.state == "random_state_123"


def test_exchange_oauth(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/exchange",
        json={
            "data": [
                {"account_id": "acc_ig_001", "platform": "instagram", "username": "testinsta"},
            ],
            "count": 1,
        },
    )
    result = client.accounts.exchange_oauth(
        platform="instagram",
        code="auth_code_abc",
        metadata={"redirect_uri": "https://app.local/callback", "state": "random_state_123"},
    )
    assert isinstance(result, OAuthExchangeResponse)
    assert result.accounts is not None
    assert len(result.accounts) == 1
    assert result.accounts[0].username == "testinsta"


def test_disconnect_account(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001",
        status_code=204,
    )
    # Should not raise
    client.accounts.disconnect("acc_ig_001")


def test_list_accounts_with_brand_id(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts?brand_id=brand_001",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.accounts.list(brand_id="brand_001")
    assert len(page.data) == 1


def test_connect_account_direct(httpx_mock, client) -> None:
    """Test direct-auth connect that returns ConnectAccountResponse."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/connect",
        json={"account_id": "acc_api_001", "platform": "google", "username": "mybiz"},
    )
    from socialapi.models.accounts import ConnectAccountResponse

    result = client.accounts.connect(platform="google")
    assert isinstance(result, ConnectAccountResponse)
    assert result.account_id == "acc_api_001"


def test_connect_account_with_brand_id(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/connect",
        json={
            "auth_url": "https://example.com/oauth",
            "state": "st_123",
            "message": "Redirect user",
        },
    )
    result = client.accounts.connect(
        platform="instagram", brand_id="brand_001", metadata={"redirect_uri": "https://app.local/callback"}
    )
    assert isinstance(result, ConnectOAuthResponse)

    import json

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["brand_id"] == "brand_001"
    assert body["metadata"]["redirect_uri"] == "https://app.local/callback"


def test_exchange_oauth_single_account(httpx_mock, client) -> None:
    """Single account response (no data wrapper) backward compatibility."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/exchange",
        json={"account_id": "acc_tiktok_001", "platform": "tiktok", "username": "myuser"},
    )
    result = client.accounts.exchange_oauth(
        platform="tiktok",
        code="code_xyz",
        metadata={"redirect_uri": "https://app.local/callback", "state": "s1"},
    )
    assert isinstance(result, OAuthExchangeResponse)
    assert len(result.accounts) == 1
    assert result.accounts[0].platform == "tiktok"


async def test_list_accounts_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.accounts.list()
    assert len(page.data) == 1
    assert page.data[0].platform == "instagram"


async def test_list_accounts_async_with_brand_id(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts?brand_id=brand_001",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.accounts.list(brand_id="brand_001")
    assert len(page.data) == 1


async def test_connect_account_async_oauth(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/connect",
        json={"auth_url": "https://example.com/oauth", "state": "st_async", "message": "Redirect"},
    )
    result = await async_client.accounts.connect(platform="instagram")
    assert isinstance(result, ConnectOAuthResponse)
    assert result.state == "st_async"


async def test_connect_account_async_direct(httpx_mock, async_client) -> None:
    from socialapi.models.accounts import ConnectAccountResponse

    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/connect",
        json={"account_id": "acc_g_001", "platform": "google", "username": "mybiz"},
    )
    result = await async_client.accounts.connect(platform="google", brand_id="b1", metadata={"key": "val"})
    assert isinstance(result, ConnectAccountResponse)


async def test_exchange_oauth_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/exchange",
        json={
            "data": [{"account_id": "acc_fb_001", "platform": "facebook", "username": "fbpage"}],
            "count": 1,
        },
    )
    result = await async_client.accounts.exchange_oauth(
        platform="facebook",
        code="code_fb",
        metadata={"redirect_uri": "https://app.local/cb", "state": "s2"},
    )
    assert len(result.accounts) == 1
    assert result.accounts[0].platform == "facebook"


async def test_exchange_oauth_async_single(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/oauth/exchange",
        json={"account_id": "acc_t_001", "platform": "threads", "username": "mythread"},
    )
    result = await async_client.accounts.exchange_oauth(
        platform="threads",
        code="code_t",
        metadata={"redirect_uri": "https://app.local/cb", "state": "s3"},
    )
    assert len(result.accounts) == 1


async def test_disconnect_account_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001",
        status_code=204,
    )
    await async_client.accounts.disconnect("acc_ig_001")
