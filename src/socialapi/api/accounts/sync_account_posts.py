from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_posts_sync_response import AccountPostsSyncResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{account_id}/sync".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AccountPostsSyncResponse | ErrorResponse | None:
    if response.status_code == 202:
        response_202 = AccountPostsSyncResponse.from_dict(response.json())

        return response_202

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
) -> Response[AccountPostsSyncResponse | ErrorResponse]:
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
) -> Response[AccountPostsSyncResponse | ErrorResponse]:
    """Start a sync of a connected account's posts

     Refreshes one connected account's posts: new posts appear, engagement counts update, and Instagram
    and Facebook media links in platform_media are renewed. Instagram covers up to the 500 most recent
    posts, Facebook up to the 500 most recent per Page; other platforms cover up to the 25 most recent.
    Returns immediately: poll GET /accounts/{account_id}/sync until state leaves "syncing", then read
    the posts. A sync already running for the account is returned as-is. Each account can start a sync
    once every 15 minutes, and each day your plan allows 10 syncs per brand it includes (Enterprise is
    unlimited); the count resets at midnight UTC.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountPostsSyncResponse | ErrorResponse]
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
) -> AccountPostsSyncResponse | ErrorResponse | None:
    """Start a sync of a connected account's posts

     Refreshes one connected account's posts: new posts appear, engagement counts update, and Instagram
    and Facebook media links in platform_media are renewed. Instagram covers up to the 500 most recent
    posts, Facebook up to the 500 most recent per Page; other platforms cover up to the 25 most recent.
    Returns immediately: poll GET /accounts/{account_id}/sync until state leaves "syncing", then read
    the posts. A sync already running for the account is returned as-is. Each account can start a sync
    once every 15 minutes, and each day your plan allows 10 syncs per brand it includes (Enterprise is
    unlimited); the count resets at midnight UTC.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountPostsSyncResponse | ErrorResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AccountPostsSyncResponse | ErrorResponse]:
    """Start a sync of a connected account's posts

     Refreshes one connected account's posts: new posts appear, engagement counts update, and Instagram
    and Facebook media links in platform_media are renewed. Instagram covers up to the 500 most recent
    posts, Facebook up to the 500 most recent per Page; other platforms cover up to the 25 most recent.
    Returns immediately: poll GET /accounts/{account_id}/sync until state leaves "syncing", then read
    the posts. A sync already running for the account is returned as-is. Each account can start a sync
    once every 15 minutes, and each day your plan allows 10 syncs per brand it includes (Enterprise is
    unlimited); the count resets at midnight UTC.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountPostsSyncResponse | ErrorResponse]
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
) -> AccountPostsSyncResponse | ErrorResponse | None:
    """Start a sync of a connected account's posts

     Refreshes one connected account's posts: new posts appear, engagement counts update, and Instagram
    and Facebook media links in platform_media are renewed. Instagram covers up to the 500 most recent
    posts, Facebook up to the 500 most recent per Page; other platforms cover up to the 25 most recent.
    Returns immediately: poll GET /accounts/{account_id}/sync until state leaves "syncing", then read
    the posts. A sync already running for the account is returned as-is. Each account can start a sync
    once every 15 minutes, and each day your plan allows 10 syncs per brand it includes (Enterprise is
    unlimited); the count resets at midnight UTC.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountPostsSyncResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
