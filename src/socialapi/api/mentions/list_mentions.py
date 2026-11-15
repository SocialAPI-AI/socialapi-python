from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.mentions_list_response import MentionsListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["since"] = since

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/mentions".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | MentionsListResponse | None:
    if response.status_code == 200:
        response_200 = MentionsListResponse.from_dict(response.json())

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

    if response.status_code == 501:
        response_501 = ErrorResponse.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | MentionsListResponse]:
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
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | MentionsListResponse]:
    """List brand mentions

     Fetches posts where your brand account was mentioned or tagged. Results are sorted newest-first.
    Returns 501 for platforms that do not support mention tracking. On Instagram this returns only media
    your account was tagged in: @mentions written inside a post caption or inside a comment are never
    included, because Meta exposes no endpoint to poll them, and they are not currently delivered as
    mention.received webhooks either. On Threads, an account connected before 2026-10-17 gets an
    authorization error until it is reconnected.

    Args:
        account_id (str):
        since (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MentionsListResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        since=since,
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
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | MentionsListResponse | None:
    """List brand mentions

     Fetches posts where your brand account was mentioned or tagged. Results are sorted newest-first.
    Returns 501 for platforms that do not support mention tracking. On Instagram this returns only media
    your account was tagged in: @mentions written inside a post caption or inside a comment are never
    included, because Meta exposes no endpoint to poll them, and they are not currently delivered as
    mention.received webhooks either. On Threads, an account connected before 2026-10-17 gets an
    authorization error until it is reconnected.

    Args:
        account_id (str):
        since (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MentionsListResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        since=since,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | MentionsListResponse]:
    """List brand mentions

     Fetches posts where your brand account was mentioned or tagged. Results are sorted newest-first.
    Returns 501 for platforms that do not support mention tracking. On Instagram this returns only media
    your account was tagged in: @mentions written inside a post caption or inside a comment are never
    included, because Meta exposes no endpoint to poll them, and they are not currently delivered as
    mention.received webhooks either. On Threads, an account connected before 2026-10-17 gets an
    authorization error until it is reconnected.

    Args:
        account_id (str):
        since (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MentionsListResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        since=since,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | MentionsListResponse | None:
    """List brand mentions

     Fetches posts where your brand account was mentioned or tagged. Results are sorted newest-first.
    Returns 501 for platforms that do not support mention tracking. On Instagram this returns only media
    your account was tagged in: @mentions written inside a post caption or inside a comment are never
    included, because Meta exposes no endpoint to poll them, and they are not currently delivered as
    mention.received webhooks either. On Threads, an account connected before 2026-10-17 gets an
    authorization error until it is reconnected.

    Args:
        account_id (str):
        since (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MentionsListResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            since=since,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
