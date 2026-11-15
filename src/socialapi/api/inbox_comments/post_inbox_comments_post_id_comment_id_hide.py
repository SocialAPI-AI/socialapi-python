from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_success_response import ApiEndpointsSuccessResponse
from ...models.post_inbox_comments_post_id_comment_id_hide_body import PostInboxCommentsPostIdCommentIdHideBody
from ...types import Response


def _get_kwargs(
    post_id: str,
    comment_id: str,
    *,
    body: PostInboxCommentsPostIdCommentIdHideBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/comments/{post_id}/{comment_id}/hide".format(
            post_id=quote(str(post_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    post_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    body: PostInboxCommentsPostIdCommentIdHideBody,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Hide a comment

     Hides a comment on the platform so it is not visible to the public, and marks it hidden in the
    inbox. Supported on Instagram, Facebook, Threads (replies from other accounts), X (replies to the
    account's own posts), YouTube, Bluesky (replies in threads the account started), and TikTok (default
    connection, not a creator connection; comments written by other people). Check the can_hide
    capability flag. On Threads, an account connected before 2026-10-17 gets an authorization error
    until it is reconnected.

    Args:
        post_id (str):
        comment_id (str):
        body (PostInboxCommentsPostIdCommentIdHideBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        comment_id=comment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    body: PostInboxCommentsPostIdCommentIdHideBody,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Hide a comment

     Hides a comment on the platform so it is not visible to the public, and marks it hidden in the
    inbox. Supported on Instagram, Facebook, Threads (replies from other accounts), X (replies to the
    account's own posts), YouTube, Bluesky (replies in threads the account started), and TikTok (default
    connection, not a creator connection; comments written by other people). Check the can_hide
    capability flag. On Threads, an account connected before 2026-10-17 gets an authorization error
    until it is reconnected.

    Args:
        post_id (str):
        comment_id (str):
        body (PostInboxCommentsPostIdCommentIdHideBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return sync_detailed(
        post_id=post_id,
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    body: PostInboxCommentsPostIdCommentIdHideBody,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Hide a comment

     Hides a comment on the platform so it is not visible to the public, and marks it hidden in the
    inbox. Supported on Instagram, Facebook, Threads (replies from other accounts), X (replies to the
    account's own posts), YouTube, Bluesky (replies in threads the account started), and TikTok (default
    connection, not a creator connection; comments written by other people). Check the can_hide
    capability flag. On Threads, an account connected before 2026-10-17 gets an authorization error
    until it is reconnected.

    Args:
        post_id (str):
        comment_id (str):
        body (PostInboxCommentsPostIdCommentIdHideBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    body: PostInboxCommentsPostIdCommentIdHideBody,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Hide a comment

     Hides a comment on the platform so it is not visible to the public, and marks it hidden in the
    inbox. Supported on Instagram, Facebook, Threads (replies from other accounts), X (replies to the
    account's own posts), YouTube, Bluesky (replies in threads the account started), and TikTok (default
    connection, not a creator connection; comments written by other people). Check the can_hide
    capability flag. On Threads, an account connected before 2026-10-17 gets an authorization error
    until it is reconnected.

    Args:
        post_id (str):
        comment_id (str):
        body (PostInboxCommentsPostIdCommentIdHideBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
