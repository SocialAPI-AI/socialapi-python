from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.sync_youtube_videos_response_200 import SyncYoutubeVideosResponse200
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/youtube/accounts/{account_id}/sync".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | SyncYoutubeVideosResponse200 | None:
    if response.status_code == 200:
        response_200 = SyncYoutubeVideosResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 501:
        response_501 = ErrorResponse.from_dict(response.json())

        return response_501

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | SyncYoutubeVideosResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | SyncYoutubeVideosResponse200]:
    """Re-sync a YouTube account's videos

     Starts a sync of the account's videos and returns once it is started. Poll GET
    /accounts/{account_id}/sync until state leaves "syncing", then read the posts. Shares the cooldown
    and the daily sync limit of POST /accounts/{account_id}/sync.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SyncYoutubeVideosResponse200]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | SyncYoutubeVideosResponse200 | None:
    """Re-sync a YouTube account's videos

     Starts a sync of the account's videos and returns once it is started. Poll GET
    /accounts/{account_id}/sync until state leaves "syncing", then read the posts. Shares the cooldown
    and the daily sync limit of POST /accounts/{account_id}/sync.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SyncYoutubeVideosResponse200
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | SyncYoutubeVideosResponse200]:
    """Re-sync a YouTube account's videos

     Starts a sync of the account's videos and returns once it is started. Poll GET
    /accounts/{account_id}/sync until state leaves "syncing", then read the posts. Shares the cooldown
    and the daily sync limit of POST /accounts/{account_id}/sync.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SyncYoutubeVideosResponse200]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | SyncYoutubeVideosResponse200 | None:
    """Re-sync a YouTube account's videos

     Starts a sync of the account's videos and returns once it is started. Poll GET
    /accounts/{account_id}/sync until state leaves "syncing", then read the posts. Shares the cooldown
    and the daily sync limit of POST /accounts/{account_id}/sync.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SyncYoutubeVideosResponse200
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
