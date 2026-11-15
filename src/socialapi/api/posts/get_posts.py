from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_posts_list_response import ApiEndpointsPostsListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_ids: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    hidden: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_ids"] = account_ids

    params["brand_id"] = brand_id

    params["status"] = status

    params["platform"] = platform

    params["page_id"] = page_id

    params["from"] = from_

    params["to"] = to

    params["search"] = search

    params["sort"] = sort

    params["cursor"] = cursor

    params["limit"] = limit

    params["hidden"] = hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/posts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsPostsListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_ids: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    hidden: bool | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse]:
    """List all posts

     Returns posts with rich filtering and cursor pagination. Supports filtering by status, platform,
    account_ids, date range, and text search.

    Args:
        account_ids (str | Unset):
        brand_id (str | Unset):
        status (str | Unset):
        platform (str | Unset):
        page_id (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        search (str | Unset):
        sort (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):
        hidden (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse]
    """

    kwargs = _get_kwargs(
        account_ids=account_ids,
        brand_id=brand_id,
        status=status,
        platform=platform,
        page_id=page_id,
        from_=from_,
        to=to,
        search=search,
        sort=sort,
        cursor=cursor,
        limit=limit,
        hidden=hidden,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_ids: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    hidden: bool | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse | None:
    """List all posts

     Returns posts with rich filtering and cursor pagination. Supports filtering by status, platform,
    account_ids, date range, and text search.

    Args:
        account_ids (str | Unset):
        brand_id (str | Unset):
        status (str | Unset):
        platform (str | Unset):
        page_id (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        search (str | Unset):
        sort (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):
        hidden (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse
    """

    return sync_detailed(
        client=client,
        account_ids=account_ids,
        brand_id=brand_id,
        status=status,
        platform=platform,
        page_id=page_id,
        from_=from_,
        to=to,
        search=search,
        sort=sort,
        cursor=cursor,
        limit=limit,
        hidden=hidden,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_ids: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    hidden: bool | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse]:
    """List all posts

     Returns posts with rich filtering and cursor pagination. Supports filtering by status, platform,
    account_ids, date range, and text search.

    Args:
        account_ids (str | Unset):
        brand_id (str | Unset):
        status (str | Unset):
        platform (str | Unset):
        page_id (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        search (str | Unset):
        sort (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):
        hidden (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse]
    """

    kwargs = _get_kwargs(
        account_ids=account_ids,
        brand_id=brand_id,
        status=status,
        platform=platform,
        page_id=page_id,
        from_=from_,
        to=to,
        search=search,
        sort=sort,
        cursor=cursor,
        limit=limit,
        hidden=hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_ids: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    hidden: bool | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse | None:
    """List all posts

     Returns posts with rich filtering and cursor pagination. Supports filtering by status, platform,
    account_ids, date range, and text search.

    Args:
        account_ids (str | Unset):
        brand_id (str | Unset):
        status (str | Unset):
        platform (str | Unset):
        page_id (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        search (str | Unset):
        sort (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):
        hidden (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsPostsListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_ids=account_ids,
            brand_id=brand_id,
            status=status,
            platform=platform,
            page_id=page_id,
            from_=from_,
            to=to,
            search=search,
            sort=sort,
            cursor=cursor,
            limit=limit,
            hidden=hidden,
        )
    ).parsed
