from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from socialapi.models.youtube import YouTubeChannelSummary

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient

# Allowed values for the moderate_comment ``status`` parameter.
# Mirrors ``youtubeModerationStatus`` in ``youtube_comments.go``.
YouTubeModerationStatus = Literal["published", "held_for_review", "rejected"]


class YouTube:
    """YouTube-specific platform operations (sync).

    Covers ``/v1/platforms/youtube/*`` endpoints for channel summaries,
    account sync, video edits, and comment moderation/editing.
    """

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def get_channel_summary(
        self,
        account_id: str,
        *,
        timeout: float | None = None,
    ) -> YouTubeChannelSummary:
        """Get YouTube channel-level statistics for a connected account.

        Args:
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            A ``YouTubeChannelSummary`` with title, handle, thumbnail URL,
            subscriber count, view count, and video count.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get(
            f"/v1/platforms/youtube/accounts/{account_id}/summary",
            timeout=timeout,
        )
        return YouTubeChannelSummary.model_validate(data)

    def sync_account(
        self,
        account_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Re-sync a YouTube account's videos.

        Args:
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            None on success.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account.
            AuthenticationError: If the API key is invalid.
        """
        self._client._post(
            f"/v1/platforms/youtube/accounts/{account_id}/sync",
            timeout=timeout,
        )
        return None

    def update_video(
        self,
        account_id: str,
        video_id: str,
        *,
        title: str | None = None,
        description: str | None = None,
        visibility: str | None = None,
        timeout: float | None = None,
    ) -> None:
        """Edit a published YouTube video.

        Only the fields provided (non-None) are included in the request body,
        matching the ``UpdateYouTubeVideoRequest`` partial-update semantics.

        Args:
            account_id: The connected account ID.
            video_id: The YouTube video ID to edit.
            title: New title for the video.
            description: New description for the video.
            visibility: New visibility (``public``, ``unlisted``, or
                ``private``).
            timeout: Override the client-level timeout for this request.

        Returns:
            None on success.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {}
        if title is not None:
            body["title"] = title
        if description is not None:
            body["description"] = description
        if visibility is not None:
            body["visibility"] = visibility

        self._client._patch(
            f"/v1/platforms/youtube/accounts/{account_id}/videos/{video_id}",
            json=body,
            timeout=timeout,
        )
        return None

    def edit_comment(
        self,
        comment_id: str,
        *,
        account_id: str,
        post_id: str,
        text: str,
        timeout: float | None = None,
    ) -> None:
        """Edit the text of one of the connected account's own YouTube comments.

        Only the comment author (the connected account) can edit the comment.

        Args:
            comment_id: The YouTube comment ID.
            account_id: The connected account ID (required to resolve the
                channel that owns the comment).
            post_id: The post ID (required to resolve the channel).
            text: The new comment text.
            timeout: Override the client-level timeout for this request.

        Returns:
            None on success.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account, or the
                connector does not support editing comments.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {
            "account_id": account_id,
            "post_id": post_id,
            "text": text,
        }
        self._client._patch(
            f"/v1/platforms/youtube/comments/{comment_id}",
            json=body,
            timeout=timeout,
        )
        return None

    def moderate_comment(
        self,
        comment_id: str,
        *,
        account_id: str,
        post_id: str,
        status: YouTubeModerationStatus,
        ban_author: bool | None = None,
        timeout: float | None = None,
    ) -> None:
        """Set the moderation status of a YouTube comment.

        Allowed values for ``status``: ``published``, ``held_for_review``,
        ``rejected``. ``ban_author`` is only valid with ``status="rejected"``.

        Args:
            comment_id: The YouTube comment ID.
            account_id: The connected account ID.
            post_id: The post ID (required to resolve the channel).
            status: The moderation status to set. One of ``published``,
                ``held_for_review``, or ``rejected``.
            ban_author: Ban the comment author. Only valid with
                ``status="rejected"``.
            timeout: Override the client-level timeout for this request.

        Returns:
            None on success.

        Raises:
            BadRequestError: If the status is invalid or ban_author is used
                without status=rejected.
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account, or the
                connector does not support comment moderation.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {
            "account_id": account_id,
            "post_id": post_id,
            "status": status,
        }
        if ban_author is not None:
            body["ban_author"] = ban_author

        self._client._post(
            f"/v1/platforms/youtube/comments/{comment_id}/moderate",
            json=body,
            timeout=timeout,
        )
        return None


class AsyncYouTube:
    """YouTube-specific platform operations (async).

    Covers ``/v1/platforms/youtube/*`` endpoints for channel summaries,
    account sync, video edits, and comment moderation/editing.
    """

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def get_channel_summary(
        self,
        account_id: str,
        *,
        timeout: float | None = None,
    ) -> YouTubeChannelSummary:
        """Get YouTube channel-level statistics for a connected account.

        Args:
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            A ``YouTubeChannelSummary`` with title, handle, thumbnail URL,
            subscriber count, view count, and video count.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get(
            f"/v1/platforms/youtube/accounts/{account_id}/summary",
            timeout=timeout,
        )
        return YouTubeChannelSummary.model_validate(data)

    async def sync_account(
        self,
        account_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Re-sync a YouTube account's videos.

        Args:
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            None on success.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._post(
            f"/v1/platforms/youtube/accounts/{account_id}/sync",
            timeout=timeout,
        )
        return None

    async def update_video(
        self,
        account_id: str,
        video_id: str,
        *,
        title: str | None = None,
        description: str | None = None,
        visibility: str | None = None,
        timeout: float | None = None,
    ) -> None:
        """Edit a published YouTube video.

        Only the fields provided (non-None) are included in the request body,
        matching the ``UpdateYouTubeVideoRequest`` partial-update semantics.

        Args:
            account_id: The connected account ID.
            video_id: The YouTube video ID to edit.
            title: New title for the video.
            description: New description for the video.
            visibility: New visibility (``public``, ``unlisted``, or
                ``private``).
            timeout: Override the client-level timeout for this request.

        Returns:
            None on success.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {}
        if title is not None:
            body["title"] = title
        if description is not None:
            body["description"] = description
        if visibility is not None:
            body["visibility"] = visibility

        await self._client._patch(
            f"/v1/platforms/youtube/accounts/{account_id}/videos/{video_id}",
            json=body,
            timeout=timeout,
        )
        return None

    async def edit_comment(
        self,
        comment_id: str,
        *,
        account_id: str,
        post_id: str,
        text: str,
        timeout: float | None = None,
    ) -> None:
        """Edit the text of one of the connected account's own YouTube comments.

        Only the comment author (the connected account) can edit the comment.

        Args:
            comment_id: The YouTube comment ID.
            account_id: The connected account ID (required to resolve the
                channel that owns the comment).
            post_id: The post ID (required to resolve the channel).
            text: The new comment text.
            timeout: Override the client-level timeout for this request.

        Returns:
            None on success.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account, or the
                connector does not support editing comments.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {
            "account_id": account_id,
            "post_id": post_id,
            "text": text,
        }
        await self._client._patch(
            f"/v1/platforms/youtube/comments/{comment_id}",
            json=body,
            timeout=timeout,
        )
        return None

    async def moderate_comment(
        self,
        comment_id: str,
        *,
        account_id: str,
        post_id: str,
        status: YouTubeModerationStatus,
        ban_author: bool | None = None,
        timeout: float | None = None,
    ) -> None:
        """Set the moderation status of a YouTube comment.

        Allowed values for ``status``: ``published``, ``held_for_review``,
        ``rejected``. ``ban_author`` is only valid with ``status="rejected"``.

        Args:
            comment_id: The YouTube comment ID.
            account_id: The connected account ID.
            post_id: The post ID (required to resolve the channel).
            status: The moderation status to set. One of ``published``,
                ``held_for_review``, or ``rejected``.
            ban_author: Ban the comment author. Only valid with
                ``status="rejected"``.
            timeout: Override the client-level timeout for this request.

        Returns:
            None on success.

        Raises:
            BadRequestError: If the status is invalid or ban_author is used
                without status=rejected.
            NotFoundError: If the account does not exist.
            NotSupportedError: If the account is not a YouTube account, or the
                connector does not support comment moderation.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {
            "account_id": account_id,
            "post_id": post_id,
            "status": status,
        }
        if ban_author is not None:
            body["ban_author"] = ban_author

        await self._client._post(
            f"/v1/platforms/youtube/comments/{comment_id}/moderate",
            json=body,
            timeout=timeout,
        )
        return None
