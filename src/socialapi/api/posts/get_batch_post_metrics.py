from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.posts_metrics_response import PostsMetricsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    post_ids: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["post_ids"] = post_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/posts/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | PostsMetricsResponse | None:
    if response.status_code == 200:
        response_200 = PostsMetricsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | PostsMetricsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    post_ids: str,
) -> Response[ErrorResponse | PostsMetricsResponse]:
    """Get metrics for several posts

     Fetches engagement metrics for up to 20 published posts in one call. Each ID can be a SocialAPI post
    ID or a platform post ID. Duplicate IDs are returned once.
    Each item has the same targets as GET /v1/posts/{post_id}/metrics. A post that cannot be read (not
    found, or a platform post ID that matches several posts) gets an `error` on its item instead of
    failing the request.

    Args:
        post_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostsMetricsResponse]
    """

    kwargs = _get_kwargs(
        post_ids=post_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    post_ids: str,
) -> ErrorResponse | PostsMetricsResponse | None:
    """Get metrics for several posts

     Fetches engagement metrics for up to 20 published posts in one call. Each ID can be a SocialAPI post
    ID or a platform post ID. Duplicate IDs are returned once.
    Each item has the same targets as GET /v1/posts/{post_id}/metrics. A post that cannot be read (not
    found, or a platform post ID that matches several posts) gets an `error` on its item instead of
    failing the request.

    Args:
        post_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostsMetricsResponse
    """

    return sync_detailed(
        client=client,
        post_ids=post_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    post_ids: str,
) -> Response[ErrorResponse | PostsMetricsResponse]:
    """Get metrics for several posts

     Fetches engagement metrics for up to 20 published posts in one call. Each ID can be a SocialAPI post
    ID or a platform post ID. Duplicate IDs are returned once.
    Each item has the same targets as GET /v1/posts/{post_id}/metrics. A post that cannot be read (not
    found, or a platform post ID that matches several posts) gets an `error` on its item instead of
    failing the request.

    Args:
        post_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostsMetricsResponse]
    """

    kwargs = _get_kwargs(
        post_ids=post_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    post_ids: str,
) -> ErrorResponse | PostsMetricsResponse | None:
    """Get metrics for several posts

     Fetches engagement metrics for up to 20 published posts in one call. Each ID can be a SocialAPI post
    ID or a platform post ID. Duplicate IDs are returned once.
    Each item has the same targets as GET /v1/posts/{post_id}/metrics. A post that cannot be read (not
    found, or a platform post ID that matches several posts) gets an `error` on its item instead of
    failing the request.

    Args:
        post_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostsMetricsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            post_ids=post_ids,
        )
    ).parsed
