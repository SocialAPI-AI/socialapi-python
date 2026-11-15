from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.whats_app_create_template_request import WhatsAppCreateTemplateRequest
from ...models.whats_app_template_create_response import WhatsAppTemplateCreateResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: WhatsAppCreateTemplateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/whatsapp/accounts/{account_id}/templates".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | WhatsAppTemplateCreateResponse | None:
    if response.status_code == 201:
        response_201 = WhatsAppTemplateCreateResponse.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | WhatsAppTemplateCreateResponse]:
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
    body: WhatsAppCreateTemplateRequest,
) -> Response[ErrorResponse | WhatsAppTemplateCreateResponse]:
    """Create a message template

     Submits a new message template to the WhatsApp Business Account (WABA) for review. The request body
    is the raw WhatsApp Cloud API template payload (name, category, language, components). New templates
    start in PENDING status; Meta reviews them and the status transitions to APPROVED or REJECTED
    asynchronously.

    Args:
        account_id (str):
        body (WhatsAppCreateTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WhatsAppTemplateCreateResponse]
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
    body: WhatsAppCreateTemplateRequest,
) -> ErrorResponse | WhatsAppTemplateCreateResponse | None:
    """Create a message template

     Submits a new message template to the WhatsApp Business Account (WABA) for review. The request body
    is the raw WhatsApp Cloud API template payload (name, category, language, components). New templates
    start in PENDING status; Meta reviews them and the status transitions to APPROVED or REJECTED
    asynchronously.

    Args:
        account_id (str):
        body (WhatsAppCreateTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WhatsAppTemplateCreateResponse
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
    body: WhatsAppCreateTemplateRequest,
) -> Response[ErrorResponse | WhatsAppTemplateCreateResponse]:
    """Create a message template

     Submits a new message template to the WhatsApp Business Account (WABA) for review. The request body
    is the raw WhatsApp Cloud API template payload (name, category, language, components). New templates
    start in PENDING status; Meta reviews them and the status transitions to APPROVED or REJECTED
    asynchronously.

    Args:
        account_id (str):
        body (WhatsAppCreateTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WhatsAppTemplateCreateResponse]
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
    body: WhatsAppCreateTemplateRequest,
) -> ErrorResponse | WhatsAppTemplateCreateResponse | None:
    """Create a message template

     Submits a new message template to the WhatsApp Business Account (WABA) for review. The request body
    is the raw WhatsApp Cloud API template payload (name, category, language, components). New templates
    start in PENDING status; Meta reviews them and the status transitions to APPROVED or REJECTED
    asynchronously.

    Args:
        account_id (str):
        body (WhatsAppCreateTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WhatsAppTemplateCreateResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
