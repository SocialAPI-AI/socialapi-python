from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.like_comment_body import LikeCommentBody
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
    post_id: str,
    comment_id: str,
    *,
    body: LikeCommentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/comments/{post_id}/{comment_id}/like".format(
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
) -> ErrorResponse | SuccessResponse | None:
    if response.status_code == 200:
        response_200 = SuccessResponse.from_dict(response.json())

        return response_200

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

    if response.status_code == 501:
        response_501 = ErrorResponse.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | SuccessResponse]:
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
    body: LikeCommentBody,
) -> Response[ErrorResponse | SuccessResponse]:
    """Like a comment

     Likes a comment on the platform as the connected account. Supported on Facebook, LinkedIn (company
    Pages and member profiles), TikTok (default connection), and Instagram accounts connected with
    Facebook Login. Instagram accounts connected with Instagram Login cannot like comments. Check the
    can_like capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (LikeCommentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SuccessResponse]
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
    body: LikeCommentBody,
) -> ErrorResponse | SuccessResponse | None:
    """Like a comment

     Likes a comment on the platform as the connected account. Supported on Facebook, LinkedIn (company
    Pages and member profiles), TikTok (default connection), and Instagram accounts connected with
    Facebook Login. Instagram accounts connected with Instagram Login cannot like comments. Check the
    can_like capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (LikeCommentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SuccessResponse
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
    body: LikeCommentBody,
) -> Response[ErrorResponse | SuccessResponse]:
    """Like a comment

     Likes a comment on the platform as the connected account. Supported on Facebook, LinkedIn (company
    Pages and member profiles), TikTok (default connection), and Instagram accounts connected with
    Facebook Login. Instagram accounts connected with Instagram Login cannot like comments. Check the
    can_like capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (LikeCommentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SuccessResponse]
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
    body: LikeCommentBody,
) -> ErrorResponse | SuccessResponse | None:
    """Like a comment

     Likes a comment on the platform as the connected account. Supported on Facebook, LinkedIn (company
    Pages and member profiles), TikTok (default connection), and Instagram accounts connected with
    Facebook Login. Instagram accounts connected with Instagram Login cannot like comments. Check the
    can_like capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (LikeCommentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SuccessResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
