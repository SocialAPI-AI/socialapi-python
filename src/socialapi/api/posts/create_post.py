from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_post_request import CreatePostRequest
from ...models.error_response import ErrorResponse
from ...models.post_response import PostResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreatePostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/posts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | PostResponse | None:
    if response.status_code == 201:
        response_201 = PostResponse.from_dict(response.json())

        return response_201

    if response.status_code == 207:
        response_207 = PostResponse.from_dict(response.json())

        return response_207

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = PostResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | PostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreatePostRequest,
) -> Response[ErrorResponse | PostResponse]:
    """Create or schedule a post

     Creates a post for one or more connected accounts. Set `publish_now: true` to publish
    immediately: the post is accepted with status `publishing` and delivery runs in the
    background (so slow reel/video uploads do not block the request). The terminal status
    (`published`, `partial`, or `failed`) arrives via the `post.published`/`post.partial`/
    `post.failed` webhooks and by polling GET /posts/{post_id}. Set `scheduled_at` to queue the
    post for future publication. With neither flag the post is saved as a draft (this is the
    default, even when targets are provided); publish it later with POST /posts/{post_id}/publish.
    Set `stagger` to publish the targets one after another, separated by a random delay between
    `min_seconds` and `max_seconds`, instead of all at once; the post is then returned with status
    `scheduled`.
    Set `queue_id` instead of `scheduled_at` to schedule the post at the earliest free time of a Queue;
    the time is in `scheduled_at` on the response.
    Consumes 1 post credit when the post is published or scheduled; saving a draft is free.

    Args:
        body (CreatePostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreatePostRequest,
) -> ErrorResponse | PostResponse | None:
    """Create or schedule a post

     Creates a post for one or more connected accounts. Set `publish_now: true` to publish
    immediately: the post is accepted with status `publishing` and delivery runs in the
    background (so slow reel/video uploads do not block the request). The terminal status
    (`published`, `partial`, or `failed`) arrives via the `post.published`/`post.partial`/
    `post.failed` webhooks and by polling GET /posts/{post_id}. Set `scheduled_at` to queue the
    post for future publication. With neither flag the post is saved as a draft (this is the
    default, even when targets are provided); publish it later with POST /posts/{post_id}/publish.
    Set `stagger` to publish the targets one after another, separated by a random delay between
    `min_seconds` and `max_seconds`, instead of all at once; the post is then returned with status
    `scheduled`.
    Set `queue_id` instead of `scheduled_at` to schedule the post at the earliest free time of a Queue;
    the time is in `scheduled_at` on the response.
    Consumes 1 post credit when the post is published or scheduled; saving a draft is free.

    Args:
        body (CreatePostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreatePostRequest,
) -> Response[ErrorResponse | PostResponse]:
    """Create or schedule a post

     Creates a post for one or more connected accounts. Set `publish_now: true` to publish
    immediately: the post is accepted with status `publishing` and delivery runs in the
    background (so slow reel/video uploads do not block the request). The terminal status
    (`published`, `partial`, or `failed`) arrives via the `post.published`/`post.partial`/
    `post.failed` webhooks and by polling GET /posts/{post_id}. Set `scheduled_at` to queue the
    post for future publication. With neither flag the post is saved as a draft (this is the
    default, even when targets are provided); publish it later with POST /posts/{post_id}/publish.
    Set `stagger` to publish the targets one after another, separated by a random delay between
    `min_seconds` and `max_seconds`, instead of all at once; the post is then returned with status
    `scheduled`.
    Set `queue_id` instead of `scheduled_at` to schedule the post at the earliest free time of a Queue;
    the time is in `scheduled_at` on the response.
    Consumes 1 post credit when the post is published or scheduled; saving a draft is free.

    Args:
        body (CreatePostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreatePostRequest,
) -> ErrorResponse | PostResponse | None:
    """Create or schedule a post

     Creates a post for one or more connected accounts. Set `publish_now: true` to publish
    immediately: the post is accepted with status `publishing` and delivery runs in the
    background (so slow reel/video uploads do not block the request). The terminal status
    (`published`, `partial`, or `failed`) arrives via the `post.published`/`post.partial`/
    `post.failed` webhooks and by polling GET /posts/{post_id}. Set `scheduled_at` to queue the
    post for future publication. With neither flag the post is saved as a draft (this is the
    default, even when targets are provided); publish it later with POST /posts/{post_id}/publish.
    Set `stagger` to publish the targets one after another, separated by a random delay between
    `min_seconds` and `max_seconds`, instead of all at once; the post is then returned with status
    `scheduled`.
    Set `queue_id` instead of `scheduled_at` to schedule the post at the earliest free time of a Queue;
    the time is in `scheduled_at` on the response.
    Consumes 1 post credit when the post is published or scheduled; saving a draft is free.

    Args:
        body (CreatePostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
