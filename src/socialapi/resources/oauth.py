from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.oauth import AsyncOAuthRedirectURI, OAuthRedirectURI

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class OAuth:
    """Manage OAuth redirect URI whitelist (sync).

    The OAuth code-exchange flow itself lives on ``client.accounts``
    (``connect()``, ``exchange_oauth()``); this resource manages the
    whitelist of allowed redirect URIs used during that flow.
    """

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list_redirect_uris(self, *, timeout: float | None = None) -> list[OAuthRedirectURI]:
        data = self._client._get("/v1/oauth/redirect-uris", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [OAuthRedirectURI.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    def create_redirect_uri(
        self,
        *,
        uri: str,
        label: str | None = None,
        timeout: float | None = None,
    ) -> OAuthRedirectURI:
        body: dict[str, Any] = {"uri": uri}
        if label is not None:
            body["label"] = label
        data = self._client._post("/v1/oauth/redirect-uris", json=body, timeout=timeout)
        result = OAuthRedirectURI.model_validate(data)
        result._bind(self._client)
        return result

    def delete_redirect_uri(self, uri_id: str, *, timeout: float | None = None) -> None:
        self._client._delete(f"/v1/oauth/redirect-uris/{uri_id}", timeout=timeout)


class AsyncOAuth:
    """Manage OAuth redirect URI whitelist (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list_redirect_uris(self, *, timeout: float | None = None) -> list[AsyncOAuthRedirectURI]:
        data = await self._client._get("/v1/oauth/redirect-uris", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncOAuthRedirectURI.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    async def create_redirect_uri(
        self,
        *,
        uri: str,
        label: str | None = None,
        timeout: float | None = None,
    ) -> AsyncOAuthRedirectURI:
        body: dict[str, Any] = {"uri": uri}
        if label is not None:
            body["label"] = label
        data = await self._client._post("/v1/oauth/redirect-uris", json=body, timeout=timeout)
        result = AsyncOAuthRedirectURI.model_validate(data)
        result._bind(self._client)
        return result

    async def delete_redirect_uri(self, uri_id: str, *, timeout: float | None = None) -> None:
        await self._client._delete(f"/v1/oauth/redirect-uris/{uri_id}", timeout=timeout)
