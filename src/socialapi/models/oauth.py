from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class _OAuthRedirectURIBase(_Bound):
    """Shared fields for OAuthRedirectURI / AsyncOAuthRedirectURI."""

    id: str
    uri: str
    label: str | None = None
    created_at: datetime | None = None


class OAuthRedirectURI(_OAuthRedirectURIBase):
    """A whitelisted OAuth redirect URI (sync)."""

    def delete(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._delete(f"/v1/oauth/redirect-uris/{self.id}", timeout=timeout)


class AsyncOAuthRedirectURI(_OAuthRedirectURIBase):
    """A whitelisted OAuth redirect URI (async)."""

    async def delete(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(f"/v1/oauth/redirect-uris/{self.id}", timeout=timeout)


class CreateRedirectURIRequest(BaseModel):
    """Request body for ``POST /v1/oauth/redirect-uris``."""

    model_config = ConfigDict(populate_by_name=True)

    uri: str
    label: str | None = None
