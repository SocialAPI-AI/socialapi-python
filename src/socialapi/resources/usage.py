from __future__ import annotations

from typing import TYPE_CHECKING, cast

from socialapi.models.usage import AccountLimits, UsageResponse

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Usage:
    """Access billing usage and account limits (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def get(
        self,
        *,
        timeout: float | None = None,
    ) -> UsageResponse:
        """Get current billing period usage.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            Usage statistics for the current billing period.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get("/v1/usage", timeout=timeout)
        return UsageResponse.model_validate(data)

    def get_account_limits(
        self,
        account_id: str,
        *,
        timeout: float | None = None,
    ) -> AccountLimits:
        """Get platform-specific quota limits for a connected account.

        Args:
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            Platform-specific remaining quotas.

        Raises:
            NotFoundError: If the account does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get(f"/v1/accounts/{account_id}/limits", timeout=timeout)
        # API returns the limits dict directly (not wrapped in "data")
        if "limits" not in data:
            return AccountLimits(limits=cast("dict[str, int]", data))
        return AccountLimits.model_validate(data)


class AsyncUsage:
    """Access billing usage and account limits (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def get(
        self,
        *,
        timeout: float | None = None,
    ) -> UsageResponse:
        """Get current billing period usage.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            Usage statistics for the current billing period.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/usage", timeout=timeout)
        return UsageResponse.model_validate(data)

    async def get_account_limits(
        self,
        account_id: str,
        *,
        timeout: float | None = None,
    ) -> AccountLimits:
        """Get platform-specific quota limits for a connected account.

        Args:
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            Platform-specific remaining quotas.

        Raises:
            NotFoundError: If the account does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get(f"/v1/accounts/{account_id}/limits", timeout=timeout)
        if "limits" not in data:
            return AccountLimits(limits=cast("dict[str, int]", data))
        return AccountLimits.model_validate(data)
