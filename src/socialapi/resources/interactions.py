"""Interactions resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from socialapi.models.interactions import ReplyResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Interactions:
    """Synchronous interactions resource.

    Provides methods for replying to interactions (comments, reviews, mentions).
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def reply(
        self,
        account_id: str,
        interaction_id: str,
        text: str,
        *,
        private: bool = False,
    ) -> ReplyResponse:
        """Reply to an interaction.

        Args:
            account_id: The connected account ID.
            interaction_id: The interaction ID to reply to.
            text: The reply text content.
            private: Whether the reply should be private (DM). Defaults to False.

        Returns:
            A ReplyResponse with the created reply details.

        Raises:
            NotFoundError: If the account or interaction is not found.
            NotSupportedError: If the platform does not support replies.
            RateLimitError: If the monthly interaction limit is exceeded.
        """
        return self._client._post(
            f"/v1/accounts/{account_id}/interactions/{interaction_id}/reply",
            json_data={"text": text, "private": private},
            response_model=ReplyResponse,
        )


class AsyncInteractions:
    """Asynchronous interactions resource.

    Provides methods for replying to interactions (comments, reviews, mentions).
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def reply(
        self,
        account_id: str,
        interaction_id: str,
        text: str,
        *,
        private: bool = False,
    ) -> ReplyResponse:
        """Reply to an interaction.

        Args:
            account_id: The connected account ID.
            interaction_id: The interaction ID to reply to.
            text: The reply text content.
            private: Whether the reply should be private (DM). Defaults to False.

        Returns:
            A ReplyResponse with the created reply details.

        Raises:
            NotFoundError: If the account or interaction is not found.
            NotSupportedError: If the platform does not support replies.
            RateLimitError: If the monthly interaction limit is exceeded.
        """
        return await self._client._post(
            f"/v1/accounts/{account_id}/interactions/{interaction_id}/reply",
            json_data={"text": text, "private": private},
            response_model=ReplyResponse,
        )
