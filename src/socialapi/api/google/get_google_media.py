from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.google_media_item import GoogleMediaItem
from ...types import Response


def _get_kwargs(
    account_id: str,
    media_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/accounts/{account_id}/media/{media_id}".format(
            account_id=quote(str(account_id), safe=""),
            media_id=quote(str(media_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GoogleMediaItem | None:
    if response.status_code == 200:
        response_200 = GoogleMediaItem.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | GoogleMediaItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | GoogleMediaItem]:
    """Get one Google Business Profile media item

     Returns one photo or video from a location's profile. mediaId accepts either the bare id or the full
    Google resource name returned by the list endpoint.

    Args:
        account_id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleMediaItem]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        media_id=media_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | GoogleMediaItem | None:
    """Get one Google Business Profile media item

     Returns one photo or video from a location's profile. mediaId accepts either the bare id or the full
    Google resource name returned by the list endpoint.

    Args:
        account_id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleMediaItem
    """

    return sync_detailed(
        account_id=account_id,
        media_id=media_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | GoogleMediaItem]:
    """Get one Google Business Profile media item

     Returns one photo or video from a location's profile. mediaId accepts either the bare id or the full
    Google resource name returned by the list endpoint.

    Args:
        account_id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleMediaItem]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        media_id=media_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | GoogleMediaItem | None:
    """Get one Google Business Profile media item

     Returns one photo or video from a location's profile. mediaId accepts either the bare id or the full
    Google resource name returned by the list endpoint.

    Args:
        account_id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleMediaItem
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            media_id=media_id,
            client=client,
        )
    ).parsed
