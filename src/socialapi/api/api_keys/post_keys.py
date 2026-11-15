from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_create_key_request import ApiEndpointsCreateKeyRequest
from ...models.api_endpoints_create_key_response import ApiEndpointsCreateKeyResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ApiEndpointsCreateKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 201:
        response_201 = ApiEndpointsCreateKeyResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateKeyRequest,
) -> Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]:
    """Create API key

     Generates a new API key for the authenticated user. Optionally restrict it to a set of scopes (see
    GET /keys/scopes) and/or brands. Empty scopes or brand_ids mean unrestricted.

    Args:
        body (ApiEndpointsCreateKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]
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
    body: ApiEndpointsCreateKeyRequest,
) -> ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse | None:
    """Create API key

     Generates a new API key for the authenticated user. Optionally restrict it to a set of scopes (see
    GET /keys/scopes) and/or brands. Empty scopes or brand_ids mean unrestricted.

    Args:
        body (ApiEndpointsCreateKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateKeyRequest,
) -> Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]:
    """Create API key

     Generates a new API key for the authenticated user. Optionally restrict it to a set of scopes (see
    GET /keys/scopes) and/or brands. Empty scopes or brand_ids mean unrestricted.

    Args:
        body (ApiEndpointsCreateKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateKeyRequest,
) -> ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse | None:
    """Create API key

     Generates a new API key for the authenticated user. Optionally restrict it to a set of scopes (see
    GET /keys/scopes) and/or brands. Empty scopes or brand_ids mean unrestricted.

    Args:
        body (ApiEndpointsCreateKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
