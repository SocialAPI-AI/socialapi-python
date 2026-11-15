from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_post_response import ApiEndpointsPostResponse
from ...types import Response


def _get_kwargs(
    pid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/posts/{pid}/publish".format(
            pid=quote(str(pid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsPostResponse | None:
    if response.status_code == 201:
        response_201 = ApiEndpointsPostResponse.from_dict(response.json())

        return response_201

    if response.status_code == 207:
        response_207 = ApiEndpointsPostResponse.from_dict(response.json())

        return response_207

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ApiEndpointsPostResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsPostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsPostResponse]:
    """Publish a draft post now

     Publishes a post in `draft` or `scheduled` status immediately. The post is accepted
    with status `publishing` and delivery runs in the background (so slow reel/video uploads
    do not block the request); the terminal status arrives via the `post.published`/
    `post.partial`/`post.failed` webhooks and by polling GET /posts/{pid}. Use this to publish
    a post that was saved as a draft, or to publish a scheduled post ahead of its time.
    A post in a Queue publishes now and leaves the Queue.
    Consumes 1 post credit.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsPostResponse]
    """

    kwargs = _get_kwargs(
        pid=pid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsPostResponse | None:
    """Publish a draft post now

     Publishes a post in `draft` or `scheduled` status immediately. The post is accepted
    with status `publishing` and delivery runs in the background (so slow reel/video uploads
    do not block the request); the terminal status arrives via the `post.published`/
    `post.partial`/`post.failed` webhooks and by polling GET /posts/{pid}. Use this to publish
    a post that was saved as a draft, or to publish a scheduled post ahead of its time.
    A post in a Queue publishes now and leaves the Queue.
    Consumes 1 post credit.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsPostResponse
    """

    return sync_detailed(
        pid=pid,
        client=client,
    ).parsed


async def asyncio_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsPostResponse]:
    """Publish a draft post now

     Publishes a post in `draft` or `scheduled` status immediately. The post is accepted
    with status `publishing` and delivery runs in the background (so slow reel/video uploads
    do not block the request); the terminal status arrives via the `post.published`/
    `post.partial`/`post.failed` webhooks and by polling GET /posts/{pid}. Use this to publish
    a post that was saved as a draft, or to publish a scheduled post ahead of its time.
    A post in a Queue publishes now and leaves the Queue.
    Consumes 1 post credit.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsPostResponse]
    """

    kwargs = _get_kwargs(
        pid=pid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsPostResponse | None:
    """Publish a draft post now

     Publishes a post in `draft` or `scheduled` status immediately. The post is accepted
    with status `publishing` and delivery runs in the background (so slow reel/video uploads
    do not block the request); the terminal status arrives via the `post.published`/
    `post.partial`/`post.failed` webhooks and by polling GET /posts/{pid}. Use this to publish
    a post that was saved as a draft, or to publish a scheduled post ahead of its time.
    A post in a Queue publishes now and leaves the Queue.
    Consumes 1 post credit.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsPostResponse
    """

    return (
        await asyncio_detailed(
            pid=pid,
            client=client,
        )
    ).parsed
