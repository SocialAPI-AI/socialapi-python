from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.social_api_ai_core_api_connectors_whatsapp_phone_number_status_response import (
    SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/whatsapp/phone-numbers/{id}/status".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse | None:
    if response.status_code == 200:
        response_200 = SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse]:
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
) -> Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse]:
    """Get phone number registration status

     Returns whether a phone number is verified and registered with WhatsApp Business, and whether it
    stays on the WhatsApp Business app (business_app). A number with registered true can send and
    receive messages. A business_app number is always verified and registered and skips the request-
    code, verify-code and register steps.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse | None:
    """Get phone number registration status

     Returns whether a phone number is verified and registered with WhatsApp Business, and whether it
    stays on the WhatsApp Business app (business_app). A number with registered true can send and
    receive messages. A business_app number is always verified and registered and skips the request-
    code, verify-code and register steps.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse]:
    """Get phone number registration status

     Returns whether a phone number is verified and registered with WhatsApp Business, and whether it
    stays on the WhatsApp Business app (business_app). A number with registered true can send and
    receive messages. A business_app number is always verified and registered and skips the request-
    code, verify-code and register steps.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse | None:
    """Get phone number registration status

     Returns whether a phone number is verified and registered with WhatsApp Business, and whether it
    stays on the WhatsApp Business app (business_app). A number with registered true can send and
    receive messages. A business_app number is always verified and registered and skips the request-
    code, verify-code and register steps.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
