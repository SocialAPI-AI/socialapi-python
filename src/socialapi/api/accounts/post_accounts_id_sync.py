from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_account_posts_sync_response import ApiEndpointsAccountPostsSyncResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{id}/sync".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 202:
        response_202 = ApiEndpointsAccountPostsSyncResponse.from_dict(response.json())

        return response_202

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse]:
    """Start a sync of a connected account's posts

     Refreshes one connected account's posts: new posts appear, engagement counts update, and Instagram
    and Facebook media links in platform_media are renewed. Instagram covers up to the 500 most recent
    posts, Facebook up to the 500 most recent per Page; other platforms cover up to the 25 most recent.
    Returns immediately: poll GET /accounts/{id}/sync until state leaves "syncing", then read the posts.
    A sync already running for the account is returned as-is. Each account can start a sync once every
    15 minutes, and each day your plan allows 10 syncs per brand it includes (Enterprise is unlimited);
    the count resets at midnight UTC.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse | None:
    """Start a sync of a connected account's posts

     Refreshes one connected account's posts: new posts appear, engagement counts update, and Instagram
    and Facebook media links in platform_media are renewed. Instagram covers up to the 500 most recent
    posts, Facebook up to the 500 most recent per Page; other platforms cover up to the 25 most recent.
    Returns immediately: poll GET /accounts/{id}/sync until state leaves "syncing", then read the posts.
    A sync already running for the account is returned as-is. Each account can start a sync once every
    15 minutes, and each day your plan allows 10 syncs per brand it includes (Enterprise is unlimited);
    the count resets at midnight UTC.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse]:
    """Start a sync of a connected account's posts

     Refreshes one connected account's posts: new posts appear, engagement counts update, and Instagram
    and Facebook media links in platform_media are renewed. Instagram covers up to the 500 most recent
    posts, Facebook up to the 500 most recent per Page; other platforms cover up to the 25 most recent.
    Returns immediately: poll GET /accounts/{id}/sync until state leaves "syncing", then read the posts.
    A sync already running for the account is returned as-is. Each account can start a sync once every
    15 minutes, and each day your plan allows 10 syncs per brand it includes (Enterprise is unlimited);
    the count resets at midnight UTC.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse | None:
    """Start a sync of a connected account's posts

     Refreshes one connected account's posts: new posts appear, engagement counts update, and Instagram
    and Facebook media links in platform_media are renewed. Instagram covers up to the 500 most recent
    posts, Facebook up to the 500 most recent per Page; other platforms cover up to the 25 most recent.
    Returns immediately: poll GET /accounts/{id}/sync until state leaves "syncing", then read the posts.
    A sync already running for the account is returned as-is. Each account can start a sync once every
    15 minutes, and each day your plan allows 10 syncs per brand it includes (Enterprise is unlimited);
    the count resets at midnight UTC.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAccountPostsSyncResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
