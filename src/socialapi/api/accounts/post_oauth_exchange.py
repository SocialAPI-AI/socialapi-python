from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_connect_account_response import ApiEndpointsConnectAccountResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_exchange_request import ApiEndpointsExchangeRequest
from ...models.api_endpoints_pending_connection_response import ApiEndpointsPendingConnectionResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ApiEndpointsExchangeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/oauth/exchange",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsPendingConnectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = ApiEndpointsConnectAccountResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsExchangeRequest,
) -> Response[ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse]:
    """Exchange OAuth code

     Exchanges an OAuth authorization code for a connected social account. Use this when
    you handle the OAuth callback on your own server (proxy flow). For a single account
    the response is a flat ConnectAccountResponse (HTTP 201). When a single OAuth flow
    connects multiple accounts (e.g. Facebook Pages) the response is OAuthCallbackResponse.

    Args:
        body (ApiEndpointsExchangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse]
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
    body: ApiEndpointsExchangeRequest,
) -> ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse | None:
    """Exchange OAuth code

     Exchanges an OAuth authorization code for a connected social account. Use this when
    you handle the OAuth callback on your own server (proxy flow). For a single account
    the response is a flat ConnectAccountResponse (HTTP 201). When a single OAuth flow
    connects multiple accounts (e.g. Facebook Pages) the response is OAuthCallbackResponse.

    Args:
        body (ApiEndpointsExchangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsExchangeRequest,
) -> Response[ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse]:
    """Exchange OAuth code

     Exchanges an OAuth authorization code for a connected social account. Use this when
    you handle the OAuth callback on your own server (proxy flow). For a single account
    the response is a flat ConnectAccountResponse (HTTP 201). When a single OAuth flow
    connects multiple accounts (e.g. Facebook Pages) the response is OAuthCallbackResponse.

    Args:
        body (ApiEndpointsExchangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsExchangeRequest,
) -> ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse | None:
    """Exchange OAuth code

     Exchanges an OAuth authorization code for a connected social account. Use this when
    you handle the OAuth callback on your own server (proxy flow). For a single account
    the response is a flat ConnectAccountResponse (HTTP 201). When a single OAuth flow
    connects multiple accounts (e.g. Facebook Pages) the response is OAuthCallbackResponse.

    Args:
        body (ApiEndpointsExchangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsConnectAccountResponse | ApiEndpointsErrorResponse | ApiEndpointsPendingConnectionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
