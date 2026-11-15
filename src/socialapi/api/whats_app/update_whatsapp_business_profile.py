from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.whats_app_update_business_profile_request import WhatsAppUpdateBusinessProfileRequest
from ...types import Response


def _get_kwargs(
    phone_number_id: str,
    *,
    body: WhatsAppUpdateBusinessProfileRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/platforms/whatsapp/phone-numbers/{phone_number_id}/business-profile".format(
            phone_number_id=quote(str(phone_number_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | ErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[Any | ErrorResponse]:
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
    body: WhatsAppUpdateBusinessProfileRequest,
) -> Response[Any | ErrorResponse]:
    """Update a WhatsApp Business Profile

     Updates one or more fields of the public business profile (about, address, description, email,
    websites, vertical, profile_picture_handle). Only provided fields are changed. The profile picture
    itself is changed by passing a profile_picture_handle obtained from the Resumable Upload API;
    profile_picture_url is read-only.

    Args:
        phone_number_id (str):
        body (WhatsAppUpdateBusinessProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        phone_number_id=phone_number_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    phone_number_id: str,
    *,
    client: AuthenticatedClient,
    body: WhatsAppUpdateBusinessProfileRequest,
) -> Any | ErrorResponse | None:
    """Update a WhatsApp Business Profile

     Updates one or more fields of the public business profile (about, address, description, email,
    websites, vertical, profile_picture_handle). Only provided fields are changed. The profile picture
    itself is changed by passing a profile_picture_handle obtained from the Resumable Upload API;
    profile_picture_url is read-only.

    Args:
        phone_number_id (str):
        body (WhatsAppUpdateBusinessProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        phone_number_id=phone_number_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    phone_number_id: str,
    *,
    client: AuthenticatedClient,
    body: WhatsAppUpdateBusinessProfileRequest,
) -> Response[Any | ErrorResponse]:
    """Update a WhatsApp Business Profile

     Updates one or more fields of the public business profile (about, address, description, email,
    websites, vertical, profile_picture_handle). Only provided fields are changed. The profile picture
    itself is changed by passing a profile_picture_handle obtained from the Resumable Upload API;
    profile_picture_url is read-only.

    Args:
        phone_number_id (str):
        body (WhatsAppUpdateBusinessProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        phone_number_id=phone_number_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    phone_number_id: str,
    *,
    client: AuthenticatedClient,
    body: WhatsAppUpdateBusinessProfileRequest,
) -> Any | ErrorResponse | None:
    """Update a WhatsApp Business Profile

     Updates one or more fields of the public business profile (about, address, description, email,
    websites, vertical, profile_picture_handle). Only provided fields are changed. The profile picture
    itself is changed by passing a profile_picture_handle obtained from the Resumable Upload API;
    profile_picture_url is read-only.

    Args:
        phone_number_id (str):
        body (WhatsAppUpdateBusinessProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            phone_number_id=phone_number_id,
            client=client,
            body=body,
        )
    ).parsed
