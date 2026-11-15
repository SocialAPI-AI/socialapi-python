from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.whats_app_verify_code_request import WhatsAppVerifyCodeRequest
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: WhatsAppVerifyCodeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/whatsapp/phone-numbers/{account_id}/verify-code".format(
            account_id=quote(str(account_id), safe=""),
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

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

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
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: WhatsAppVerifyCodeRequest,
) -> Response[Any | ErrorResponse]:
    """Verify a phone number with a code

     Submits the 6-digit code received via SMS or voice to prove ownership of the phone number. Once
    verified, the phone number can be registered with WhatsApp Business. Codes expire quickly; if
    verification fails, request a new code. A number that stays on the WhatsApp Business app is already
    verified and is refused with 409 whatsapp.business_app_number.

    Args:
        account_id (str):
        body (WhatsAppVerifyCodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
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
    body: WhatsAppVerifyCodeRequest,
) -> Any | ErrorResponse | None:
    """Verify a phone number with a code

     Submits the 6-digit code received via SMS or voice to prove ownership of the phone number. Once
    verified, the phone number can be registered with WhatsApp Business. Codes expire quickly; if
    verification fails, request a new code. A number that stays on the WhatsApp Business app is already
    verified and is refused with 409 whatsapp.business_app_number.

    Args:
        account_id (str):
        body (WhatsAppVerifyCodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
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
    body: WhatsAppVerifyCodeRequest,
) -> Response[Any | ErrorResponse]:
    """Verify a phone number with a code

     Submits the 6-digit code received via SMS or voice to prove ownership of the phone number. Once
    verified, the phone number can be registered with WhatsApp Business. Codes expire quickly; if
    verification fails, request a new code. A number that stays on the WhatsApp Business app is already
    verified and is refused with 409 whatsapp.business_app_number.

    Args:
        account_id (str):
        body (WhatsAppVerifyCodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
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
    body: WhatsAppVerifyCodeRequest,
) -> Any | ErrorResponse | None:
    """Verify a phone number with a code

     Submits the 6-digit code received via SMS or voice to prove ownership of the phone number. Once
    verified, the phone number can be registered with WhatsApp Business. Codes expire quickly; if
    verification fails, request a new code. A number that stays on the WhatsApp Business app is already
    verified and is refused with 409 whatsapp.business_app_number.

    Args:
        account_id (str):
        body (WhatsAppVerifyCodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
