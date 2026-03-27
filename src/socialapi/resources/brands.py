from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.brands import Brand

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Brands:
    """Manage brands (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        timeout: float | None = None,
    ) -> list[Brand]:
        """List all brands for the current user.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of brands with account counts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get("/v1/brands", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [Brand.model_validate(item) for item in raw_items]

    def create(
        self,
        *,
        name: str,
        timeout: float | None = None,
    ) -> Brand:
        """Create a new brand.

        Args:
            name: Brand name.
            timeout: Override the client-level timeout for this request.

        Returns:
            The created brand.

        Raises:
            BadRequestError: If the name is missing or invalid.
            ForbiddenError: If the brand limit has been reached.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._post("/v1/brands", json={"name": name}, timeout=timeout)
        return Brand.model_validate(data)

    def update(
        self,
        brand_id: str,
        *,
        name: str,
        timeout: float | None = None,
    ) -> Brand:
        """Rename a brand.

        Args:
            brand_id: The brand ID.
            name: New brand name.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated brand.

        Raises:
            NotFoundError: If the brand does not exist.
            BadRequestError: If the name is missing or invalid.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._patch(f"/v1/brands/{brand_id}", json={"name": name}, timeout=timeout)
        return Brand.model_validate(data)

    def delete(
        self,
        brand_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Delete a brand and disconnect all its accounts.

        Args:
            brand_id: The brand ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the brand does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._delete(f"/v1/brands/{brand_id}", timeout=timeout)


class AsyncBrands:
    """Manage brands (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        timeout: float | None = None,
    ) -> list[Brand]:
        """List all brands for the current user.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of brands with account counts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/brands", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [Brand.model_validate(item) for item in raw_items]

    async def create(
        self,
        *,
        name: str,
        timeout: float | None = None,
    ) -> Brand:
        """Create a new brand.

        Args:
            name: Brand name.
            timeout: Override the client-level timeout for this request.

        Returns:
            The created brand.

        Raises:
            BadRequestError: If the name is missing or invalid.
            ForbiddenError: If the brand limit has been reached.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._post("/v1/brands", json={"name": name}, timeout=timeout)
        return Brand.model_validate(data)

    async def update(
        self,
        brand_id: str,
        *,
        name: str,
        timeout: float | None = None,
    ) -> Brand:
        """Rename a brand.

        Args:
            brand_id: The brand ID.
            name: New brand name.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated brand.

        Raises:
            NotFoundError: If the brand does not exist.
            BadRequestError: If the name is missing or invalid.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._patch(f"/v1/brands/{brand_id}", json={"name": name}, timeout=timeout)
        return Brand.model_validate(data)

    async def delete(
        self,
        brand_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Delete a brand and disconnect all its accounts.

        Args:
            brand_id: The brand ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the brand does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(f"/v1/brands/{brand_id}", timeout=timeout)
