from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_request import CreateWebhookRequest
from ...models.create_webhook_response import CreateWebhookResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWebhookRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CreateWebhookResponse | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = CreateWebhookResponse.from_dict(response.json())

        return response_201

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
) -> Response[CreateWebhookResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookRequest,
) -> Response[CreateWebhookResponse | ErrorResponse]:
    """Create webhook endpoint

     Registers a new webhook endpoint and performs a live reachability ping. If the endpoint is
    unreachable or returns an unexpected response, the request fails with 400
    (webhook_verification_failed). The generated secret is returned once - store it securely.

    Args:
        body (CreateWebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResponse | ErrorResponse]
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
    body: CreateWebhookRequest,
) -> CreateWebhookResponse | ErrorResponse | None:
    """Create webhook endpoint

     Registers a new webhook endpoint and performs a live reachability ping. If the endpoint is
    unreachable or returns an unexpected response, the request fails with 400
    (webhook_verification_failed). The generated secret is returned once - store it securely.

    Args:
        body (CreateWebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookRequest,
) -> Response[CreateWebhookResponse | ErrorResponse]:
    """Create webhook endpoint

     Registers a new webhook endpoint and performs a live reachability ping. If the endpoint is
    unreachable or returns an unexpected response, the request fails with 400
    (webhook_verification_failed). The generated secret is returned once - store it securely.

    Args:
        body (CreateWebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookRequest,
) -> CreateWebhookResponse | ErrorResponse | None:
    """Create webhook endpoint

     Registers a new webhook endpoint and performs a live reachability ping. If the endpoint is
    unreachable or returns an unexpected response, the request fails with 400
    (webhook_verification_failed). The generated secret is returned once - store it securely.

    Args:
        body (CreateWebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
