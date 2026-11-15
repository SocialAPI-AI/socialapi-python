from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_sender_action_request import ApiEndpointsSenderActionRequest
from ...models.api_endpoints_success_response import ApiEndpointsSuccessResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ApiEndpointsSenderActionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/conversations/{id}/sender-action".format(
            id=quote(str(id), safe=""),
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

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

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
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsSenderActionRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Show typing or mark seen

     Shows the other participant a typing indicator, or marks their messages as seen, without sending a
    message. Free: no interaction credit is used.

    Supported on Instagram, Facebook Messenger and WhatsApp. On Instagram and Messenger the typing
    indicator clears after 20 seconds or when you send a message. On WhatsApp, typing_on also marks the
    contact's latest message as read, clears after 25 seconds or when you reply, and needs at least one
    message from the contact. WhatsApp has no typing_off and returns 400. Marking a message seen on
    WhatsApp also marks every earlier message in the chat as read.

    Args:
        id (str):
        body (ApiEndpointsSenderActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsSenderActionRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Show typing or mark seen

     Shows the other participant a typing indicator, or marks their messages as seen, without sending a
    message. Free: no interaction credit is used.

    Supported on Instagram, Facebook Messenger and WhatsApp. On Instagram and Messenger the typing
    indicator clears after 20 seconds or when you send a message. On WhatsApp, typing_on also marks the
    contact's latest message as read, clears after 25 seconds or when you reply, and needs at least one
    message from the contact. WhatsApp has no typing_off and returns 400. Marking a message seen on
    WhatsApp also marks every earlier message in the chat as read.

    Args:
        id (str):
        body (ApiEndpointsSenderActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsSenderActionRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Show typing or mark seen

     Shows the other participant a typing indicator, or marks their messages as seen, without sending a
    message. Free: no interaction credit is used.

    Supported on Instagram, Facebook Messenger and WhatsApp. On Instagram and Messenger the typing
    indicator clears after 20 seconds or when you send a message. On WhatsApp, typing_on also marks the
    contact's latest message as read, clears after 25 seconds or when you reply, and needs at least one
    message from the contact. WhatsApp has no typing_off and returns 400. Marking a message seen on
    WhatsApp also marks every earlier message in the chat as read.

    Args:
        id (str):
        body (ApiEndpointsSenderActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsSenderActionRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Show typing or mark seen

     Shows the other participant a typing indicator, or marks their messages as seen, without sending a
    message. Free: no interaction credit is used.

    Supported on Instagram, Facebook Messenger and WhatsApp. On Instagram and Messenger the typing
    indicator clears after 20 seconds or when you send a message. On WhatsApp, typing_on also marks the
    contact's latest message as read, clears after 25 seconds or when you reply, and needs at least one
    message from the contact. WhatsApp has no typing_off and returns 400. Marking a message seen on
    WhatsApp also marks every earlier message in the chat as read.

    Args:
        id (str):
        body (ApiEndpointsSenderActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
