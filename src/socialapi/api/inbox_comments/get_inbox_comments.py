from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_commented_posts_list_response import ApiEndpointsCommentedPostsListResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    min_comments: int | Unset = UNSET,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["brand_id"] = brand_id

    params["platform"] = platform

    params["min_comments"] = min_comments

    params["since"] = since

    params["sort_by"] = sort_by

    params["sort_order"] = sort_order

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/inbox/comments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsCommentedPostsListResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    min_comments: int | Unset = UNSET,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse]:
    """List commented posts

     Returns the connected accounts' posts with their comment counts, newest published first. Add
    min_comments=1 to keep only posts that have comments. Filter by account, brand, platform, minimum
    comment count, and publish date. Uses cursor-based pagination.

    Args:
        account_id (str | Unset):
        brand_id (str | Unset):
        platform (str | Unset):
        min_comments (int | Unset):
        since (str | Unset):
        sort_by (str | Unset):
        sort_order (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        brand_id=brand_id,
        platform=platform,
        min_comments=min_comments,
        since=since,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    min_comments: int | Unset = UNSET,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse | None:
    """List commented posts

     Returns the connected accounts' posts with their comment counts, newest published first. Add
    min_comments=1 to keep only posts that have comments. Filter by account, brand, platform, minimum
    comment count, and publish date. Uses cursor-based pagination.

    Args:
        account_id (str | Unset):
        brand_id (str | Unset):
        platform (str | Unset):
        min_comments (int | Unset):
        since (str | Unset):
        sort_by (str | Unset):
        sort_order (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        brand_id=brand_id,
        platform=platform,
        min_comments=min_comments,
        since=since,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    min_comments: int | Unset = UNSET,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse]:
    """List commented posts

     Returns the connected accounts' posts with their comment counts, newest published first. Add
    min_comments=1 to keep only posts that have comments. Filter by account, brand, platform, minimum
    comment count, and publish date. Uses cursor-based pagination.

    Args:
        account_id (str | Unset):
        brand_id (str | Unset):
        platform (str | Unset):
        min_comments (int | Unset):
        since (str | Unset):
        sort_by (str | Unset):
        sort_order (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        brand_id=brand_id,
        platform=platform,
        min_comments=min_comments,
        since=since,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    min_comments: int | Unset = UNSET,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse | None:
    """List commented posts

     Returns the connected accounts' posts with their comment counts, newest published first. Add
    min_comments=1 to keep only posts that have comments. Filter by account, brand, platform, minimum
    comment count, and publish date. Uses cursor-based pagination.

    Args:
        account_id (str | Unset):
        brand_id (str | Unset):
        platform (str | Unset):
        min_comments (int | Unset):
        since (str | Unset):
        sort_by (str | Unset):
        sort_order (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCommentedPostsListResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            brand_id=brand_id,
            platform=platform,
            min_comments=min_comments,
            since=since,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
