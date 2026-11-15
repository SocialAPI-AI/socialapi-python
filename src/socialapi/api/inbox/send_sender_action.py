from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.sender_action_request import SenderActionRequest
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
    conversation_id: str,
    *,
    body: SenderActionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/conversations/{conversation_id}/sender-action".format(
            conversation_id=quote(str(conversation_id), safe=""),
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

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 501:
        response_501 = ErrorResponse.from_dict(response.json())

        return response_501

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

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
    conversation_id: str,
    *,
    client: AuthenticatedClient,
    body: SenderActionRequest,
) -> Response[ErrorResponse | SuccessResponse]:
    """Show typing or mark seen

     Shows the other participant a typing indicator, or marks their messages as seen, without sending a
    message. Free: no interaction credit is used.

    Supported on Instagram, Facebook Messenger and WhatsApp. On Instagram and Messenger the typing
    indicator clears after 20 seconds or when you send a message. On WhatsApp, typing_on also marks the
    contact's latest message as read, clears after 25 seconds or when you reply, and needs at least one
    message from the contact. WhatsApp has no typing_off and returns 400. Marking a message seen on
    WhatsApp also marks every earlier message in the chat as read.

    Args:
        conversation_id (str):
        body (SenderActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SuccessResponse]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conversation_id: str,
    *,
    client: AuthenticatedClient,
    body: SenderActionRequest,
) -> ErrorResponse | SuccessResponse | None:
    """Show typing or mark seen

     Shows the other participant a typing indicator, or marks their messages as seen, without sending a
    message. Free: no interaction credit is used.

    Supported on Instagram, Facebook Messenger and WhatsApp. On Instagram and Messenger the typing
    indicator clears after 20 seconds or when you send a message. On WhatsApp, typing_on also marks the
    contact's latest message as read, clears after 25 seconds or when you reply, and needs at least one
    message from the contact. WhatsApp has no typing_off and returns 400. Marking a message seen on
    WhatsApp also marks every earlier message in the chat as read.

    Args:
        conversation_id (str):
        body (SenderActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SuccessResponse
    """

    return sync_detailed(
        conversation_id=conversation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    conversation_id: str,
    *,
    client: AuthenticatedClient,
    body: SenderActionRequest,
) -> Response[ErrorResponse | SuccessResponse]:
    """Show typing or mark seen

     Shows the other participant a typing indicator, or marks their messages as seen, without sending a
    message. Free: no interaction credit is used.

    Supported on Instagram, Facebook Messenger and WhatsApp. On Instagram and Messenger the typing
    indicator clears after 20 seconds or when you send a message. On WhatsApp, typing_on also marks the
    contact's latest message as read, clears after 25 seconds or when you reply, and needs at least one
    message from the contact. WhatsApp has no typing_off and returns 400. Marking a message seen on
    WhatsApp also marks every earlier message in the chat as read.

    Args:
        conversation_id (str):
        body (SenderActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SuccessResponse]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conversation_id: str,
    *,
    client: AuthenticatedClient,
    body: SenderActionRequest,
) -> ErrorResponse | SuccessResponse | None:
    """Show typing or mark seen

     Shows the other participant a typing indicator, or marks their messages as seen, without sending a
    message. Free: no interaction credit is used.

    Supported on Instagram, Facebook Messenger and WhatsApp. On Instagram and Messenger the typing
    indicator clears after 20 seconds or when you send a message. On WhatsApp, typing_on also marks the
    contact's latest message as read, clears after 25 seconds or when you reply, and needs at least one
    message from the contact. WhatsApp has no typing_off and returns 400. Marking a message seen on
    WhatsApp also marks every earlier message in the chat as read.

    Args:
        conversation_id (str):
        body (SenderActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SuccessResponse
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            body=body,
        )
    ).parsed
