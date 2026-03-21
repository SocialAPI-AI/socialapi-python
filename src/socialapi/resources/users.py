"""Users resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from socialapi.models.shared import OKResponse
from socialapi.models.users import User

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Users:
    """Synchronous users resource.

    Provides methods for retrieving, updating, and deleting the current user.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def me(self) -> User:
        """Get the authenticated user's profile.

        Returns:
            The authenticated User.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return self._client._get("/v1/users/me", response_model=User)

    def update(self, *, onboarding: bool) -> User:
        """Update the authenticated user's profile.

        Args:
            onboarding: Whether the user has completed onboarding.

        Returns:
            The updated User.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return self._client._patch("/v1/users/me", json_data={"onboarding": onboarding}, response_model=User)

    def delete(self) -> OKResponse:
        """Delete the authenticated user's account.

        Returns:
            An OKResponse indicating the account was deleted.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return self._client._delete("/v1/users/me", response_model=OKResponse)


class AsyncUsers:
    """Asynchronous users resource.

    Provides methods for retrieving, updating, and deleting the current user.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def me(self) -> User:
        """Get the authenticated user's profile.

        Returns:
            The authenticated User.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return await self._client._get("/v1/users/me", response_model=User)

    async def update(self, *, onboarding: bool) -> User:
        """Update the authenticated user's profile.

        Args:
            onboarding: Whether the user has completed onboarding.

        Returns:
            The updated User.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return await self._client._patch("/v1/users/me", json_data={"onboarding": onboarding}, response_model=User)

    async def delete(self) -> OKResponse:
        """Delete the authenticated user's account.

        Returns:
            An OKResponse indicating the account was deleted.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return await self._client._delete("/v1/users/me", response_model=OKResponse)
