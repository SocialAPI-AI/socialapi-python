from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.whats_app_create_template_request import WhatsAppCreateTemplateRequest
from ...models.whats_app_validate_template_response import WhatsAppValidateTemplateResponse
from ...types import Response


def _get_kwargs(
    *,
    body: WhatsAppCreateTemplateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/whatsapp/templates/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | WhatsAppValidateTemplateResponse | None:
    if response.status_code == 200:
        response_200 = WhatsAppValidateTemplateResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | WhatsAppValidateTemplateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WhatsAppCreateTemplateRequest,
) -> Response[ErrorResponse | WhatsAppValidateTemplateResponse]:
    """Validate a message template

     Dry-run validation of a WhatsApp message template against the Cloud API rules (name format,
    component cardinality, header format, text limits, placeholder sequencing, button constraints).
    Returns errors for hard violations that WhatsApp would reject and warnings for best-practice issues.
    Performs no network call and does not submit the template.

    Args:
        body (WhatsAppCreateTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WhatsAppValidateTemplateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: WhatsAppCreateTemplateRequest,
) -> ErrorResponse | WhatsAppValidateTemplateResponse | None:
    """Validate a message template

     Dry-run validation of a WhatsApp message template against the Cloud API rules (name format,
    component cardinality, header format, text limits, placeholder sequencing, button constraints).
    Returns errors for hard violations that WhatsApp would reject and warnings for best-practice issues.
    Performs no network call and does not submit the template.

    Args:
        body (WhatsAppCreateTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WhatsAppValidateTemplateResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WhatsAppCreateTemplateRequest,
) -> Response[ErrorResponse | WhatsAppValidateTemplateResponse]:
    """Validate a message template

     Dry-run validation of a WhatsApp message template against the Cloud API rules (name format,
    component cardinality, header format, text limits, placeholder sequencing, button constraints).
    Returns errors for hard violations that WhatsApp would reject and warnings for best-practice issues.
    Performs no network call and does not submit the template.

    Args:
        body (WhatsAppCreateTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WhatsAppValidateTemplateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WhatsAppCreateTemplateRequest,
) -> ErrorResponse | WhatsAppValidateTemplateResponse | None:
    """Validate a message template

     Dry-run validation of a WhatsApp message template against the Cloud API rules (name format,
    component cardinality, header format, text limits, placeholder sequencing, button constraints).
    Returns errors for hard violations that WhatsApp would reject and warnings for best-practice issues.
    Performs no network call and does not submit the template.

    Args:
        body (WhatsAppCreateTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WhatsAppValidateTemplateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
