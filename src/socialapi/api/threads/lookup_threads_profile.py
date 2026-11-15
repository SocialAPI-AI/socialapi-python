from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.threads_profile_response import ThreadsProfileResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    account_id: str,
    username: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/threads/profile-lookup",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | ThreadsProfileResponse | None:
    if response.status_code == 200:
        response_200 = ThreadsProfileResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | ThreadsProfileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str,
    username: str,
) -> Response[ErrorResponse | ThreadsProfileResponse]:
    """Look up a public Threads profile (beta)

     Beta. Resolves a public Threads profile by exact username and returns its public metrics. Requires
    the threads_profile_discovery Threads permission, which is pending Meta App Review, so calls may
    return an upstream authorization error for accounts outside the app's tester roster until that
    permission is granted. Matching is exact, with no fuzzy or prefix search. Only profiles with 100 or
    more followers are discoverable, anything else returns 404. The upstream budget is 1000 lookups per
    user per rolling 24 hours.

    Args:
        account_id (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ThreadsProfileResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: str,
    username: str,
) -> ErrorResponse | ThreadsProfileResponse | None:
    """Look up a public Threads profile (beta)

     Beta. Resolves a public Threads profile by exact username and returns its public metrics. Requires
    the threads_profile_discovery Threads permission, which is pending Meta App Review, so calls may
    return an upstream authorization error for accounts outside the app's tester roster until that
    permission is granted. Matching is exact, with no fuzzy or prefix search. Only profiles with 100 or
    more followers are discoverable, anything else returns 404. The upstream budget is 1000 lookups per
    user per rolling 24 hours.

    Args:
        account_id (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ThreadsProfileResponse
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str,
    username: str,
) -> Response[ErrorResponse | ThreadsProfileResponse]:
    """Look up a public Threads profile (beta)

     Beta. Resolves a public Threads profile by exact username and returns its public metrics. Requires
    the threads_profile_discovery Threads permission, which is pending Meta App Review, so calls may
    return an upstream authorization error for accounts outside the app's tester roster until that
    permission is granted. Matching is exact, with no fuzzy or prefix search. Only profiles with 100 or
    more followers are discoverable, anything else returns 404. The upstream budget is 1000 lookups per
    user per rolling 24 hours.

    Args:
        account_id (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ThreadsProfileResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str,
    username: str,
) -> ErrorResponse | ThreadsProfileResponse | None:
    """Look up a public Threads profile (beta)

     Beta. Resolves a public Threads profile by exact username and returns its public metrics. Requires
    the threads_profile_discovery Threads permission, which is pending Meta App Review, so calls may
    return an upstream authorization error for accounts outside the app's tester roster until that
    permission is granted. Matching is exact, with no fuzzy or prefix search. Only profiles with 100 or
    more followers are discoverable, anything else returns 404. The upstream budget is 1000 lookups per
    user per rolling 24 hours.

    Args:
        account_id (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ThreadsProfileResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            username=username,
        )
    ).parsed
