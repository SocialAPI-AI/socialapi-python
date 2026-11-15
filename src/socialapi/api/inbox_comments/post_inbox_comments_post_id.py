from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_reply_to_comment_success_response import ApiEndpointsReplyToCommentSuccessResponse
from ...models.post_inbox_comments_post_id_body import PostInboxCommentsPostIdBody
from ...types import Response


def _get_kwargs(
    post_id: str,
    *,
    body: PostInboxCommentsPostIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/comments/{post_id}".format(
            post_id=quote(str(post_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsReplyToCommentSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    post_id: str,
    *,
    client: AuthenticatedClient,
    body: PostInboxCommentsPostIdBody,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse]:
    """Reply to a comment

     Posts a reply on the platform. If comment_id is provided, replies to that specific comment (threaded
    reply); otherwise replies to the post itself (top-level comment). Consumes 1 interaction credit.

    Args:
        post_id (str):
        body (PostInboxCommentsPostIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: str,
    *,
    client: AuthenticatedClient,
    body: PostInboxCommentsPostIdBody,
) -> ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse | None:
    """Reply to a comment

     Posts a reply on the platform. If comment_id is provided, replies to that specific comment (threaded
    reply); otherwise replies to the post itself (top-level comment). Consumes 1 interaction credit.

    Args:
        post_id (str):
        body (PostInboxCommentsPostIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: AuthenticatedClient,
    body: PostInboxCommentsPostIdBody,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse]:
    """Reply to a comment

     Posts a reply on the platform. If comment_id is provided, replies to that specific comment (threaded
    reply); otherwise replies to the post itself (top-level comment). Consumes 1 interaction credit.

    Args:
        post_id (str):
        body (PostInboxCommentsPostIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    *,
    client: AuthenticatedClient,
    body: PostInboxCommentsPostIdBody,
) -> ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse | None:
    """Reply to a comment

     Posts a reply on the platform. If comment_id is provided, replies to that specific comment (threaded
    reply); otherwise replies to the post itself (top-level comment). Consumes 1 interaction credit.

    Args:
        post_id (str):
        body (PostInboxCommentsPostIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsReplyToCommentSuccessResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
            body=body,
        )
    ).parsed
