from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.reply_to_comment_success_response import ReplyToCommentSuccessResponse
from ...models.reply_to_mention_body import ReplyToMentionBody
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ReplyToMentionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{account_id}/mentions/reply".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | ReplyToCommentSuccessResponse | None:
    if response.status_code == 200:
        response_200 = ReplyToCommentSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 501:
        response_501 = ErrorResponse.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | ReplyToCommentSuccessResponse]:
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
    body: ReplyToMentionBody,
) -> Response[ErrorResponse | ReplyToCommentSuccessResponse]:
    """Reply to a mention

     Replies, as a public comment, to a mention of the connected account, including on a third-party post
    where the normal comment-reply endpoint is not permitted. Provide media_id (the media/post the
    mention is on); set comment_id only when the mention was in a comment (omit it to reply to a mention
    in the post caption). Supported on Instagram, Facebook, Threads and Bluesky. Consumes 1 interaction
    credit.

    Args:
        account_id (str):
        body (ReplyToMentionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ReplyToCommentSuccessResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ReplyToMentionBody,
) -> ErrorResponse | ReplyToCommentSuccessResponse | None:
    """Reply to a mention

     Replies, as a public comment, to a mention of the connected account, including on a third-party post
    where the normal comment-reply endpoint is not permitted. Provide media_id (the media/post the
    mention is on); set comment_id only when the mention was in a comment (omit it to reply to a mention
    in the post caption). Supported on Instagram, Facebook, Threads and Bluesky. Consumes 1 interaction
    credit.

    Args:
        account_id (str):
        body (ReplyToMentionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ReplyToCommentSuccessResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ReplyToMentionBody,
) -> Response[ErrorResponse | ReplyToCommentSuccessResponse]:
    """Reply to a mention

     Replies, as a public comment, to a mention of the connected account, including on a third-party post
    where the normal comment-reply endpoint is not permitted. Provide media_id (the media/post the
    mention is on); set comment_id only when the mention was in a comment (omit it to reply to a mention
    in the post caption). Supported on Instagram, Facebook, Threads and Bluesky. Consumes 1 interaction
    credit.

    Args:
        account_id (str):
        body (ReplyToMentionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ReplyToCommentSuccessResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ReplyToMentionBody,
) -> ErrorResponse | ReplyToCommentSuccessResponse | None:
    """Reply to a mention

     Replies, as a public comment, to a mention of the connected account, including on a third-party post
    where the normal comment-reply endpoint is not permitted. Provide media_id (the media/post the
    mention is on); set comment_id only when the mention was in a comment (omit it to reply to a mention
    in the post caption). Supported on Instagram, Facebook, Threads and Bluesky. Consumes 1 interaction
    credit.

    Args:
        account_id (str):
        body (ReplyToMentionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ReplyToCommentSuccessResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
