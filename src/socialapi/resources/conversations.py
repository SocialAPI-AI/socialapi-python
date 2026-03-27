from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.conversations import (
    Conversation,
    Message,
    SendMessageResponse,
)

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


class Conversations:
    """Manage DM conversations in the unified inbox (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        status: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Conversation]:
        """List DM conversations.

        Args:
            account_id: Filter by connected account.
            platform: Filter by platform.
            status: Filter by conversation status (``"active"`` or ``"archived"``).
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of conversations.

        Raises:
            AuthenticationError: If the API key is invalid.
            BadRequestError: If query parameters are invalid.
        """
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if status is not None:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            "/v1/inbox/conversations",
            params=params,
            model=Conversation,
            timeout=timeout,
        )

    def get(
        self,
        conversation_id: str,
        *,
        timeout: float | None = None,
    ) -> Conversation:
        """Get a single conversation by ID.

        Args:
            conversation_id: The conversation ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            The conversation details.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get(f"/v1/inbox/conversations/{conversation_id}", timeout=timeout)
        return Conversation.model_validate(data.get("data", data))

    def update(
        self,
        conversation_id: str,
        *,
        status: str,
        timeout: float | None = None,
    ) -> Conversation:
        """Update a conversation (e.g. archive it).

        Args:
            conversation_id: The conversation ID.
            status: New status (``"active"`` or ``"archived"``).
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated conversation.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._patch(
            f"/v1/inbox/conversations/{conversation_id}",
            json={"status": status},
            timeout=timeout,
        )
        if isinstance(data, dict) and "data" in data:
            return Conversation.model_validate(data["data"])
        # API returns {"success": true} — re-fetch the conversation
        return self.get(conversation_id, timeout=timeout)

    def list_messages(
        self,
        conversation_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Message]:
        """List messages in a conversation.

        Args:
            conversation_id: The conversation ID.
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of messages.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            f"/v1/inbox/conversations/{conversation_id}/messages",
            params=params,
            model=Message,
            timeout=timeout,
        )

    def send_message(
        self,
        conversation_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> SendMessageResponse:
        """Send a message in a conversation.

        Args:
            conversation_id: The conversation ID.
            account_id: The connected account ID to send from.
            text: Message text content.
            timeout: Override the client-level timeout for this request.

        Returns:
            The send result with the new message ID.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._post(
            f"/v1/inbox/conversations/{conversation_id}/messages",
            json={"account_id": account_id, "text": text},
            timeout=timeout,
        )
        return SendMessageResponse.model_validate(data)

    def mark_as_read(
        self,
        conversation_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Mark a conversation as read.

        Args:
            conversation_id: The conversation ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._post(
            f"/v1/inbox/conversations/{conversation_id}/read",
            timeout=timeout,
        )


class AsyncConversations:
    """Manage DM conversations in the unified inbox (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        status: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[Conversation]:
        """List DM conversations.

        Args:
            account_id: Filter by connected account.
            platform: Filter by platform.
            status: Filter by conversation status (``"active"`` or ``"archived"``).
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of conversations.

        Raises:
            AuthenticationError: If the API key is invalid.
            BadRequestError: If query parameters are invalid.
        """
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if status is not None:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            "/v1/inbox/conversations",
            params=params,
            model=Conversation,
            timeout=timeout,
        )

    async def get(
        self,
        conversation_id: str,
        *,
        timeout: float | None = None,
    ) -> Conversation:
        """Get a single conversation by ID.

        Args:
            conversation_id: The conversation ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            The conversation details.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get(f"/v1/inbox/conversations/{conversation_id}", timeout=timeout)
        return Conversation.model_validate(data.get("data", data))

    async def update(
        self,
        conversation_id: str,
        *,
        status: str,
        timeout: float | None = None,
    ) -> Conversation:
        """Update a conversation (e.g. archive it).

        Args:
            conversation_id: The conversation ID.
            status: New status (``"active"`` or ``"archived"``).
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated conversation.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._patch(
            f"/v1/inbox/conversations/{conversation_id}",
            json={"status": status},
            timeout=timeout,
        )
        if isinstance(data, dict) and "data" in data:
            return Conversation.model_validate(data["data"])
        return await self.get(conversation_id, timeout=timeout)

    async def list_messages(
        self,
        conversation_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[Message]:
        """List messages in a conversation.

        Args:
            conversation_id: The conversation ID.
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of messages.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            f"/v1/inbox/conversations/{conversation_id}/messages",
            params=params,
            model=Message,
            timeout=timeout,
        )

    async def send_message(
        self,
        conversation_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> SendMessageResponse:
        """Send a message in a conversation.

        Args:
            conversation_id: The conversation ID.
            account_id: The connected account ID to send from.
            text: Message text content.
            timeout: Override the client-level timeout for this request.

        Returns:
            The send result with the new message ID.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._post(
            f"/v1/inbox/conversations/{conversation_id}/messages",
            json={"account_id": account_id, "text": text},
            timeout=timeout,
        )
        return SendMessageResponse.model_validate(data)

    async def mark_as_read(
        self,
        conversation_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Mark a conversation as read.

        Args:
            conversation_id: The conversation ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the conversation does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._post(
            f"/v1/inbox/conversations/{conversation_id}/read",
            timeout=timeout,
        )
