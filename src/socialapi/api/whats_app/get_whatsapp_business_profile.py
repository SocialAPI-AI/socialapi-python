from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.whats_app_business_profile import WhatsAppBusinessProfile
from ...types import Response


def _get_kwargs(
    phone_number_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/whatsapp/phone-numbers/{phone_number_id}/business-profile".format(
            phone_number_id=quote(str(phone_number_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | WhatsAppBusinessProfile | None:
    if response.status_code == 200:
        response_200 = WhatsAppBusinessProfile.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | WhatsAppBusinessProfile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    phone_number_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | WhatsAppBusinessProfile]:
    """Get a WhatsApp Business Profile

     Returns the public business profile for a WhatsApp phone number, including about text, address,
    description, contact email, websites, and vertical. The profile is visible to customers in the
    WhatsApp chat header.

    Args:
        phone_number_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WhatsAppBusinessProfile]
    """

    kwargs = _get_kwargs(
        phone_number_id=phone_number_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    phone_number_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | WhatsAppBusinessProfile | None:
    """Get a WhatsApp Business Profile

     Returns the public business profile for a WhatsApp phone number, including about text, address,
    description, contact email, websites, and vertical. The profile is visible to customers in the
    WhatsApp chat header.

    Args:
        phone_number_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WhatsAppBusinessProfile
    """

    return sync_detailed(
        phone_number_id=phone_number_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    phone_number_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | WhatsAppBusinessProfile]:
    """Get a WhatsApp Business Profile

     Returns the public business profile for a WhatsApp phone number, including about text, address,
    description, contact email, websites, and vertical. The profile is visible to customers in the
    WhatsApp chat header.

    Args:
        phone_number_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WhatsAppBusinessProfile]
    """

    kwargs = _get_kwargs(
        phone_number_id=phone_number_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    phone_number_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | WhatsAppBusinessProfile | None:
    """Get a WhatsApp Business Profile

     Returns the public business profile for a WhatsApp phone number, including about text, address,
    description, contact email, websites, and vertical. The profile is visible to customers in the
    WhatsApp chat header.

    Args:
        phone_number_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WhatsAppBusinessProfile
    """

    return (
        await asyncio_detailed(
            phone_number_id=phone_number_id,
            client=client,
        )
    ).parsed
