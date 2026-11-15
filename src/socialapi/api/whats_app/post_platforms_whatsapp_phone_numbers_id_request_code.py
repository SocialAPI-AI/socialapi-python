from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_whats_app_request_code_request import ApiEndpointsWhatsAppRequestCodeRequest
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ApiEndpointsWhatsAppRequestCodeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/whatsapp/phone-numbers/{id}/request-code".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ApiEndpointsErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ApiEndpointsErrorResponse]:
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
    body: ApiEndpointsWhatsAppRequestCodeRequest,
) -> Response[Any | ApiEndpointsErrorResponse]:
    """Request a phone number verification code

     Asks WhatsApp to send a one-time verification code to the phone number via SMS or voice call. The
    code is delivered to the underlying phone line, not to the API caller; follow up with verify-code
    once the user receives it. Step 1 of the phone-number registration flow (request-code, verify-code,
    register). A number that stays on the WhatsApp Business app is already verified and is refused with
    409 whatsapp.business_app_number.

    Args:
        id (str):
        body (ApiEndpointsWhatsAppRequestCodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiEndpointsErrorResponse]
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
    body: ApiEndpointsWhatsAppRequestCodeRequest,
) -> Any | ApiEndpointsErrorResponse | None:
    """Request a phone number verification code

     Asks WhatsApp to send a one-time verification code to the phone number via SMS or voice call. The
    code is delivered to the underlying phone line, not to the API caller; follow up with verify-code
    once the user receives it. Step 1 of the phone-number registration flow (request-code, verify-code,
    register). A number that stays on the WhatsApp Business app is already verified and is refused with
    409 whatsapp.business_app_number.

    Args:
        id (str):
        body (ApiEndpointsWhatsAppRequestCodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiEndpointsErrorResponse
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
    body: ApiEndpointsWhatsAppRequestCodeRequest,
) -> Response[Any | ApiEndpointsErrorResponse]:
    """Request a phone number verification code

     Asks WhatsApp to send a one-time verification code to the phone number via SMS or voice call. The
    code is delivered to the underlying phone line, not to the API caller; follow up with verify-code
    once the user receives it. Step 1 of the phone-number registration flow (request-code, verify-code,
    register). A number that stays on the WhatsApp Business app is already verified and is refused with
    409 whatsapp.business_app_number.

    Args:
        id (str):
        body (ApiEndpointsWhatsAppRequestCodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiEndpointsErrorResponse]
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
    body: ApiEndpointsWhatsAppRequestCodeRequest,
) -> Any | ApiEndpointsErrorResponse | None:
    """Request a phone number verification code

     Asks WhatsApp to send a one-time verification code to the phone number via SMS or voice call. The
    code is delivered to the underlying phone line, not to the API caller; follow up with verify-code
    once the user receives it. Step 1 of the phone-number registration flow (request-code, verify-code,
    register). A number that stays on the WhatsApp Business app is already verified and is refused with
    409 whatsapp.business_app_number.

    Args:
        id (str):
        body (ApiEndpointsWhatsAppRequestCodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
