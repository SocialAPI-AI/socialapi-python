"""Feedback resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.shared import SuccessResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Feedback:
    """Synchronous feedback resource.

    Provides methods for sending feedback to the SocialAPI team.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def send(self, message: str, *, email: str | None = None) -> SuccessResponse:
        """Send feedback to the SocialAPI team.

        Args:
            message: The feedback message text.
            email: Optional contact email for follow-up.

        Returns:
            A SuccessResponse indicating the feedback was received.

        Raises:
            ValidationError: If the message is empty.
        """
        body: dict[str, Any] = {"message": message}
        if email is not None:
            body["email"] = email
        return self._client._post("/v1/feedback", json_data=body, response_model=SuccessResponse)


class AsyncFeedback:
    """Asynchronous feedback resource.

    Provides methods for sending feedback to the SocialAPI team.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def send(self, message: str, *, email: str | None = None) -> SuccessResponse:
        """Send feedback to the SocialAPI team.

        Args:
            message: The feedback message text.
            email: Optional contact email for follow-up.

        Returns:
            A SuccessResponse indicating the feedback was received.

        Raises:
            ValidationError: If the message is empty.
        """
        body: dict[str, Any] = {"message": message}
        if email is not None:
            body["email"] = email
        return await self._client._post("/v1/feedback", json_data=body, response_model=SuccessResponse)
