from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_whats_app_send_template_request import ApiEndpointsWhatsAppSendTemplateRequest
from ...models.api_endpoints_whats_app_send_template_response import ApiEndpointsWhatsAppSendTemplateResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ApiEndpointsWhatsAppSendTemplateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/whatsapp/accounts/{id}/send-template".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsWhatsAppSendTemplateResponse.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse]:
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
    body: ApiEndpointsWhatsAppSendTemplateRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse]:
    """Send a template message

     Sends an approved WhatsApp template message to a recipient phone number. Template messages can be
    sent outside the 24-hour customer service window. The template must already be APPROVED on the WABA,
    and the language code must match an approved variant. Component parameter order must match the
    template's placeholders. The response includes message_id, the SocialAPI message ID for the send,
    which matches the id field on the dm.status.* webhooks for this message.

    Args:
        id (str):
        body (ApiEndpointsWhatsAppSendTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse]
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
    body: ApiEndpointsWhatsAppSendTemplateRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse | None:
    """Send a template message

     Sends an approved WhatsApp template message to a recipient phone number. Template messages can be
    sent outside the 24-hour customer service window. The template must already be APPROVED on the WABA,
    and the language code must match an approved variant. Component parameter order must match the
    template's placeholders. The response includes message_id, the SocialAPI message ID for the send,
    which matches the id field on the dm.status.* webhooks for this message.

    Args:
        id (str):
        body (ApiEndpointsWhatsAppSendTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse
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
    body: ApiEndpointsWhatsAppSendTemplateRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse]:
    """Send a template message

     Sends an approved WhatsApp template message to a recipient phone number. Template messages can be
    sent outside the 24-hour customer service window. The template must already be APPROVED on the WABA,
    and the language code must match an approved variant. Component parameter order must match the
    template's placeholders. The response includes message_id, the SocialAPI message ID for the send,
    which matches the id field on the dm.status.* webhooks for this message.

    Args:
        id (str):
        body (ApiEndpointsWhatsAppSendTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse]
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
    body: ApiEndpointsWhatsAppSendTemplateRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse | None:
    """Send a template message

     Sends an approved WhatsApp template message to a recipient phone number. Template messages can be
    sent outside the 24-hour customer service window. The template must already be APPROVED on the WABA,
    and the language code must match an approved variant. Component parameter order must match the
    template's placeholders. The response includes message_id, the SocialAPI message ID for the send,
    which matches the id field on the dm.status.* webhooks for this message.

    Args:
        id (str):
        body (ApiEndpointsWhatsAppSendTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsWhatsAppSendTemplateResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
