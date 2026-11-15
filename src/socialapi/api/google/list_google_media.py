from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.google_media_list_response import GoogleMediaListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    contributed: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["contributed"] = contributed

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/accounts/{account_id}/media".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GoogleMediaListResponse | None:
    if response.status_code == 200:
        response_200 = GoogleMediaListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GoogleMediaListResponse]:
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
    contributed: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | GoogleMediaListResponse]:
    """List a Google Business Profile location's media

     Lists the photos and videos on a location's public profile: its logo, cover, interior shots, and so
    on. This is profile media, not the media attached to a post. Set contributed=true to read the
    separate, read-only gallery of photos customers submitted; those items carry an attribution block
    that Google requires you to display as provided, unaltered.

    Args:
        account_id (str):
        contributed (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleMediaListResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        contributed=contributed,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    contributed: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | GoogleMediaListResponse | None:
    """List a Google Business Profile location's media

     Lists the photos and videos on a location's public profile: its logo, cover, interior shots, and so
    on. This is profile media, not the media attached to a post. Set contributed=true to read the
    separate, read-only gallery of photos customers submitted; those items carry an attribution block
    that Google requires you to display as provided, unaltered.

    Args:
        account_id (str):
        contributed (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleMediaListResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        contributed=contributed,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    contributed: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | GoogleMediaListResponse]:
    """List a Google Business Profile location's media

     Lists the photos and videos on a location's public profile: its logo, cover, interior shots, and so
    on. This is profile media, not the media attached to a post. Set contributed=true to read the
    separate, read-only gallery of photos customers submitted; those items carry an attribution block
    that Google requires you to display as provided, unaltered.

    Args:
        account_id (str):
        contributed (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleMediaListResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        contributed=contributed,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    contributed: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | GoogleMediaListResponse | None:
    """List a Google Business Profile location's media

     Lists the photos and videos on a location's public profile: its logo, cover, interior shots, and so
    on. This is profile media, not the media attached to a post. Set contributed=true to read the
    separate, read-only gallery of photos customers submitted; those items carry an attribution block
    that Google requires you to display as provided, unaltered.

    Args:
        account_id (str):
        contributed (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleMediaListResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            contributed=contributed,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
