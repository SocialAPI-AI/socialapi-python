from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_private_reply_request import ApiEndpointsPrivateReplyRequest
from ...models.api_endpoints_success_response import ApiEndpointsSuccessResponse
from ...types import Response


def _get_kwargs(
    post_id: str,
    comment_id: str,
    *,
    body: ApiEndpointsPrivateReplyRequest,
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
    body: ApiEndpointsPrivateReplyRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Send a private reply to a commenter

     Sends a direct message to the author of a comment. Only supported on Instagram and Facebook. Meta
    allows one private reply per comment, within 7 days of the comment; a second attempt or an expired
    window returns HTTP 400 with error code platform.instagram.private_reply_ineligible or
    platform.facebook.private_reply_ineligible. Once a comment has spent its one reply, or the comment
    is older than 7 days, further attempts are refused and do not count against your outbound message
    rate; the error carries a reason of already_replied, platform_refused or window_expired. The 400 is
    terminal: retrying it will never succeed. Set buttons (1 to 3) to send the reply as a button
    template with text as its body; a tap on a postback button arrives as a dm.postback event. Set
    attachment instead of text to send one image, video, audio or file: a private reply is a single
    message, so it carries either text (with optional buttons) or one attachment, never both. You cannot
    message the commenter again until they respond; once they do, the conversation continues within the
    standard 24-hour messaging window. Check the can_private_reply capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (ApiEndpointsPrivateReplyRequest):

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
    body: ApiEndpointsPrivateReplyRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Send a private reply to a commenter

     Sends a direct message to the author of a comment. Only supported on Instagram and Facebook. Meta
    allows one private reply per comment, within 7 days of the comment; a second attempt or an expired
    window returns HTTP 400 with error code platform.instagram.private_reply_ineligible or
    platform.facebook.private_reply_ineligible. Once a comment has spent its one reply, or the comment
    is older than 7 days, further attempts are refused and do not count against your outbound message
    rate; the error carries a reason of already_replied, platform_refused or window_expired. The 400 is
    terminal: retrying it will never succeed. Set buttons (1 to 3) to send the reply as a button
    template with text as its body; a tap on a postback button arrives as a dm.postback event. Set
    attachment instead of text to send one image, video, audio or file: a private reply is a single
    message, so it carries either text (with optional buttons) or one attachment, never both. You cannot
    message the commenter again until they respond; once they do, the conversation continues within the
    standard 24-hour messaging window. Check the can_private_reply capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (ApiEndpointsPrivateReplyRequest):

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
    body: ApiEndpointsPrivateReplyRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Send a private reply to a commenter

     Sends a direct message to the author of a comment. Only supported on Instagram and Facebook. Meta
    allows one private reply per comment, within 7 days of the comment; a second attempt or an expired
    window returns HTTP 400 with error code platform.instagram.private_reply_ineligible or
    platform.facebook.private_reply_ineligible. Once a comment has spent its one reply, or the comment
    is older than 7 days, further attempts are refused and do not count against your outbound message
    rate; the error carries a reason of already_replied, platform_refused or window_expired. The 400 is
    terminal: retrying it will never succeed. Set buttons (1 to 3) to send the reply as a button
    template with text as its body; a tap on a postback button arrives as a dm.postback event. Set
    attachment instead of text to send one image, video, audio or file: a private reply is a single
    message, so it carries either text (with optional buttons) or one attachment, never both. You cannot
    message the commenter again until they respond; once they do, the conversation continues within the
    standard 24-hour messaging window. Check the can_private_reply capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (ApiEndpointsPrivateReplyRequest):

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
    body: ApiEndpointsPrivateReplyRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Send a private reply to a commenter

     Sends a direct message to the author of a comment. Only supported on Instagram and Facebook. Meta
    allows one private reply per comment, within 7 days of the comment; a second attempt or an expired
    window returns HTTP 400 with error code platform.instagram.private_reply_ineligible or
    platform.facebook.private_reply_ineligible. Once a comment has spent its one reply, or the comment
    is older than 7 days, further attempts are refused and do not count against your outbound message
    rate; the error carries a reason of already_replied, platform_refused or window_expired. The 400 is
    terminal: retrying it will never succeed. Set buttons (1 to 3) to send the reply as a button
    template with text as its body; a tap on a postback button arrives as a dm.postback event. Set
    attachment instead of text to send one image, video, audio or file: a private reply is a single
    message, so it carries either text (with optional buttons) or one attachment, never both. You cannot
    message the commenter again until they respond; once they do, the conversation continues within the
    standard 24-hour messaging window. Check the can_private_reply capability flag.

    Args:
        post_id (str):
        comment_id (str):
        body (ApiEndpointsPrivateReplyRequest):

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
