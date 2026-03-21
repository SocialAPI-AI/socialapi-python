"""Comments resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.interactions import InteractionsListResponse
from socialapi.models.shared import OKResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Comments:
    """Synchronous comments resource.

    Provides methods for listing comments, fetching replies,
    moderating comments, and toggling comments on posts.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def list(
        self,
        account_id: str,
        post_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> InteractionsListResponse:
        """List comments on a post.

        Args:
            account_id: The connected account ID.
            post_id: The platform post ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            An InteractionsListResponse containing the comments and count.

        Raises:
            NotFoundError: If the account or post is not found.
            NotSupportedError: If the platform does not support comments.
            RateLimitError: If the monthly resource limit is exceeded.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        if since is not None:
            params["since"] = since
        return self._client._get(
            f"/v1/accounts/{account_id}/posts/{post_id}/comments",
            params=params,
            response_model=InteractionsListResponse,
        )

    def replies(
        self,
        account_id: str,
        interaction_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> InteractionsListResponse:
        """List replies to a comment.

        Args:
            account_id: The connected account ID.
            interaction_id: The interaction (comment) ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            An InteractionsListResponse containing the replies and count.

        Raises:
            NotFoundError: If the account or interaction is not found.
            NotSupportedError: If the platform does not support comment replies.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        if since is not None:
            params["since"] = since
        return self._client._get(
            f"/v1/accounts/{account_id}/interactions/{interaction_id}/replies",
            params=params,
            response_model=InteractionsListResponse,
        )

    def moderate(self, account_id: str, interaction_id: str, action: str) -> OKResponse:
        """Moderate a comment (hide, unhide, delete, etc.).

        Args:
            account_id: The connected account ID.
            interaction_id: The interaction (comment) ID.
            action: The moderation action to perform (e.g. ``"hide"``, ``"delete"``).

        Returns:
            An OKResponse indicating the action was applied.

        Raises:
            NotFoundError: If the account or interaction is not found.
            NotSupportedError: If the platform does not support this moderation action.
        """
        return self._client._post(
            f"/v1/accounts/{account_id}/interactions/{interaction_id}/moderate",
            json_data={"action": action},
            response_model=OKResponse,
        )

    def toggle(self, account_id: str, post_id: str, enabled: bool) -> OKResponse:
        """Toggle comments on or off for a post.

        Args:
            account_id: The connected account ID.
            post_id: The platform post ID.
            enabled: Whether to enable or disable comments.

        Returns:
            An OKResponse indicating the toggle was applied.

        Raises:
            NotFoundError: If the account or post is not found.
            NotSupportedError: If the platform does not support toggling comments.
        """
        return self._client._post(
            f"/v1/accounts/{account_id}/posts/{post_id}/comments/toggle",
            json_data={"enabled": enabled},
            response_model=OKResponse,
        )


class AsyncComments:
    """Asynchronous comments resource.

    Provides methods for listing comments, fetching replies,
    moderating comments, and toggling comments on posts.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def list(
        self,
        account_id: str,
        post_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> InteractionsListResponse:
        """List comments on a post.

        Args:
            account_id: The connected account ID.
            post_id: The platform post ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            An InteractionsListResponse containing the comments and count.

        Raises:
            NotFoundError: If the account or post is not found.
            NotSupportedError: If the platform does not support comments.
            RateLimitError: If the monthly resource limit is exceeded.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        if since is not None:
            params["since"] = since
        return await self._client._get(
            f"/v1/accounts/{account_id}/posts/{post_id}/comments",
            params=params,
            response_model=InteractionsListResponse,
        )

    async def replies(
        self,
        account_id: str,
        interaction_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> InteractionsListResponse:
        """List replies to a comment.

        Args:
            account_id: The connected account ID.
            interaction_id: The interaction (comment) ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            An InteractionsListResponse containing the replies and count.

        Raises:
            NotFoundError: If the account or interaction is not found.
            NotSupportedError: If the platform does not support comment replies.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        if since is not None:
            params["since"] = since
        return await self._client._get(
            f"/v1/accounts/{account_id}/interactions/{interaction_id}/replies",
            params=params,
            response_model=InteractionsListResponse,
        )

    async def moderate(self, account_id: str, interaction_id: str, action: str) -> OKResponse:
        """Moderate a comment (hide, unhide, delete, etc.).

        Args:
            account_id: The connected account ID.
            interaction_id: The interaction (comment) ID.
            action: The moderation action to perform (e.g. ``"hide"``, ``"delete"``).

        Returns:
            An OKResponse indicating the action was applied.

        Raises:
            NotFoundError: If the account or interaction is not found.
            NotSupportedError: If the platform does not support this moderation action.
        """
        return await self._client._post(
            f"/v1/accounts/{account_id}/interactions/{interaction_id}/moderate",
            json_data={"action": action},
            response_model=OKResponse,
        )

    async def toggle(self, account_id: str, post_id: str, enabled: bool) -> OKResponse:
        """Toggle comments on or off for a post.

        Args:
            account_id: The connected account ID.
            post_id: The platform post ID.
            enabled: Whether to enable or disable comments.

        Returns:
            An OKResponse indicating the toggle was applied.

        Raises:
            NotFoundError: If the account or post is not found.
            NotSupportedError: If the platform does not support toggling comments.
        """
        return await self._client._post(
            f"/v1/accounts/{account_id}/posts/{post_id}/comments/toggle",
            json_data={"enabled": enabled},
            response_model=OKResponse,
        )
