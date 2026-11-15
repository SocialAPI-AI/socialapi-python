from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.private_reply_request import PrivateReplyRequest
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
    post_id: str,
    comment_id: str,
    *,
    body: PrivateReplyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/comments/{post_id}/{comment_id}/private-reply".format(
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

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

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
    body: PrivateReplyRequest,
) -> Response[ErrorResponse | SuccessResponse]:
    """Send a private reply to a commenter

     Sends a direct message to the author of a comment. Only supported on Instagram and Facebook. Meta
    allows one private reply per comment, within 7 days of the comment; a second attempt or an expired
    window returns HTTP 400 with error code platform.instagram.private_reply_ineligible or
    platform.facebook.private_reply_ineligible. When the comment is already known to be ineligible, the
    error carries blocked_locally true and a reason of already_replied, platform_refused or
    window_expired. When blocked_locally is true, or the reply was text only, the 400 is final. When the
    platform refuses a reply that carried buttons or an attachment, the refusal can come from that
    content: send it once more as text only. Set buttons (1 to 3) to send the reply as a button template
    with text as its body; a tap on a postback button arrives as a dm.postback event. Set attachment
    instead of text to send one image, video, audio or file: a private reply is a single message, so it
    carries either text (with optional buttons) or one attachment, never both. You cannot message the
    commenter again until they respond; once they do, the conversation continues within the standard
    24-hour messaging window. Check the can_private_reply capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (PrivateReplyRequest):

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
    body: PrivateReplyRequest,
) -> ErrorResponse | SuccessResponse | None:
    """Send a private reply to a commenter

     Sends a direct message to the author of a comment. Only supported on Instagram and Facebook. Meta
    allows one private reply per comment, within 7 days of the comment; a second attempt or an expired
    window returns HTTP 400 with error code platform.instagram.private_reply_ineligible or
    platform.facebook.private_reply_ineligible. When the comment is already known to be ineligible, the
    error carries blocked_locally true and a reason of already_replied, platform_refused or
    window_expired. When blocked_locally is true, or the reply was text only, the 400 is final. When the
    platform refuses a reply that carried buttons or an attachment, the refusal can come from that
    content: send it once more as text only. Set buttons (1 to 3) to send the reply as a button template
    with text as its body; a tap on a postback button arrives as a dm.postback event. Set attachment
    instead of text to send one image, video, audio or file: a private reply is a single message, so it
    carries either text (with optional buttons) or one attachment, never both. You cannot message the
    commenter again until they respond; once they do, the conversation continues within the standard
    24-hour messaging window. Check the can_private_reply capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (PrivateReplyRequest):

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
    body: PrivateReplyRequest,
) -> Response[ErrorResponse | SuccessResponse]:
    """Send a private reply to a commenter

     Sends a direct message to the author of a comment. Only supported on Instagram and Facebook. Meta
    allows one private reply per comment, within 7 days of the comment; a second attempt or an expired
    window returns HTTP 400 with error code platform.instagram.private_reply_ineligible or
    platform.facebook.private_reply_ineligible. When the comment is already known to be ineligible, the
    error carries blocked_locally true and a reason of already_replied, platform_refused or
    window_expired. When blocked_locally is true, or the reply was text only, the 400 is final. When the
    platform refuses a reply that carried buttons or an attachment, the refusal can come from that
    content: send it once more as text only. Set buttons (1 to 3) to send the reply as a button template
    with text as its body; a tap on a postback button arrives as a dm.postback event. Set attachment
    instead of text to send one image, video, audio or file: a private reply is a single message, so it
    carries either text (with optional buttons) or one attachment, never both. You cannot message the
    commenter again until they respond; once they do, the conversation continues within the standard
    24-hour messaging window. Check the can_private_reply capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (PrivateReplyRequest):

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
    body: PrivateReplyRequest,
) -> ErrorResponse | SuccessResponse | None:
    """Send a private reply to a commenter

     Sends a direct message to the author of a comment. Only supported on Instagram and Facebook. Meta
    allows one private reply per comment, within 7 days of the comment; a second attempt or an expired
    window returns HTTP 400 with error code platform.instagram.private_reply_ineligible or
    platform.facebook.private_reply_ineligible. When the comment is already known to be ineligible, the
    error carries blocked_locally true and a reason of already_replied, platform_refused or
    window_expired. When blocked_locally is true, or the reply was text only, the 400 is final. When the
    platform refuses a reply that carried buttons or an attachment, the refusal can come from that
    content: send it once more as text only. Set buttons (1 to 3) to send the reply as a button template
    with text as its body; a tap on a postback button arrives as a dm.postback event. Set attachment
    instead of text to send one image, video, audio or file: a private reply is a single message, so it
    carries either text (with optional buttons) or one attachment, never both. You cannot message the
    commenter again until they respond; once they do, the conversation continues within the standard
    24-hour messaging window. Check the can_private_reply capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (PrivateReplyRequest):

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
