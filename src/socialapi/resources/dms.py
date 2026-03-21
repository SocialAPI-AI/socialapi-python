"""Direct messages resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.interactions import DMThreadResponse, InteractionsListResponse, ReplyResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class DMs:
    """Synchronous DMs resource.

    Provides methods for listing DMs, sending messages, and retrieving threads.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def list(
        self,
        account_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> InteractionsListResponse:
        """List direct messages for a connected account.

        Args:
            account_id: The connected account ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            An InteractionsListResponse containing the DMs and count.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support DMs.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        if since is not None:
            params["since"] = since
        return self._client._get(
            f"/v1/accounts/{account_id}/dms",
            params=params,
            response_model=InteractionsListResponse,
        )

    def send(self, account_id: str, thread_id: str, text: str) -> ReplyResponse:
        """Send a direct message in a thread.

        Args:
            account_id: The connected account ID.
            thread_id: The DM thread ID.
            text: The message text content.

        Returns:
            A ReplyResponse with the sent message details.

        Raises:
            NotFoundError: If the account or thread is not found.
            NotSupportedError: If the platform does not support sending DMs.
        """
        return self._client._post(
            f"/v1/accounts/{account_id}/dms/{thread_id}/send",
            json_data={"text": text},
            response_model=ReplyResponse,
        )

    def thread(self, account_id: str, user_id: str) -> DMThreadResponse:
        """Get or create a DM thread with a specific user.

        Args:
            account_id: The connected account ID.
            user_id: The platform user ID to get or create a thread with.

        Returns:
            A DMThreadResponse containing the thread ID.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support DM threads.
        """
        return self._client._get(
            f"/v1/accounts/{account_id}/dms/thread",
            params={"user_id": user_id},
            response_model=DMThreadResponse,
        )


class AsyncDMs:
    """Asynchronous DMs resource.

    Provides methods for listing DMs, sending messages, and retrieving threads.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def list(
        self,
        account_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> InteractionsListResponse:
        """List direct messages for a connected account.

        Args:
            account_id: The connected account ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            An InteractionsListResponse containing the DMs and count.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support DMs.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        if since is not None:
            params["since"] = since
        return await self._client._get(
            f"/v1/accounts/{account_id}/dms",
            params=params,
            response_model=InteractionsListResponse,
        )

    async def send(self, account_id: str, thread_id: str, text: str) -> ReplyResponse:
        """Send a direct message in a thread.

        Args:
            account_id: The connected account ID.
            thread_id: The DM thread ID.
            text: The message text content.

        Returns:
            A ReplyResponse with the sent message details.

        Raises:
            NotFoundError: If the account or thread is not found.
            NotSupportedError: If the platform does not support sending DMs.
        """
        return await self._client._post(
            f"/v1/accounts/{account_id}/dms/{thread_id}/send",
            json_data={"text": text},
            response_model=ReplyResponse,
        )

    async def thread(self, account_id: str, user_id: str) -> DMThreadResponse:
        """Get or create a DM thread with a specific user.

        Args:
            account_id: The connected account ID.
            user_id: The platform user ID to get or create a thread with.

        Returns:
            A DMThreadResponse containing the thread ID.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support DM threads.
        """
        return await self._client._get(
            f"/v1/accounts/{account_id}/dms/thread",
            params={"user_id": user_id},
            response_model=DMThreadResponse,
        )
