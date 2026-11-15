from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_connect_account_response import ApiEndpointsConnectAccountResponse
from ...models.api_endpoints_connect_o_auth_response import ApiEndpointsConnectOAuthResponse
from ...models.api_endpoints_connect_request import ApiEndpointsConnectRequest
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ApiEndpointsConnectRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/connect",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 201:
        response_201 = ApiEndpointsConnectAccountResponse.from_dict(response.json())

        return response_201

    if response.status_code == 202:
        response_202 = ApiEndpointsConnectOAuthResponse.from_dict(response.json())

        return response_202

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
) -> Response[ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsConnectRequest,
) -> Response[ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse]:
    """Connect a social account

     Initiates account connection. For OAuth2 platforms returns an auth_url to redirect the user to.
    For apikey/credentials platforms stores the credentials immediately and returns account_id.
    For WhatsApp, open auth_url to run Meta's signup. When the WhatsApp Business account holds several
    numbers, the redirect to your redirect_uri carries status=selection_required and a connection_id:
    list the numbers with GET /v1/accounts/pending/{connection_id} and pick one with POST
    /v1/accounts/pending/{connection_id}/select.
    Set the top-level redirect_uri field when connecting WhatsApp so the result reaches a page you
    control.

    Args:
        body (ApiEndpointsConnectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse]
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
    body: ApiEndpointsConnectRequest,
) -> ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse | None:
    """Connect a social account

     Initiates account connection. For OAuth2 platforms returns an auth_url to redirect the user to.
    For apikey/credentials platforms stores the credentials immediately and returns account_id.
    For WhatsApp, open auth_url to run Meta's signup. When the WhatsApp Business account holds several
    numbers, the redirect to your redirect_uri carries status=selection_required and a connection_id:
    list the numbers with GET /v1/accounts/pending/{connection_id} and pick one with POST
    /v1/accounts/pending/{connection_id}/select.
    Set the top-level redirect_uri field when connecting WhatsApp so the result reaches a page you
    control.

    Args:
        body (ApiEndpointsConnectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsConnectRequest,
) -> Response[ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse]:
    """Connect a social account

     Initiates account connection. For OAuth2 platforms returns an auth_url to redirect the user to.
    For apikey/credentials platforms stores the credentials immediately and returns account_id.
    For WhatsApp, open auth_url to run Meta's signup. When the WhatsApp Business account holds several
    numbers, the redirect to your redirect_uri carries status=selection_required and a connection_id:
    list the numbers with GET /v1/accounts/pending/{connection_id} and pick one with POST
    /v1/accounts/pending/{connection_id}/select.
    Set the top-level redirect_uri field when connecting WhatsApp so the result reaches a page you
    control.

    Args:
        body (ApiEndpointsConnectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsConnectRequest,
) -> ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse | None:
    """Connect a social account

     Initiates account connection. For OAuth2 platforms returns an auth_url to redirect the user to.
    For apikey/credentials platforms stores the credentials immediately and returns account_id.
    For WhatsApp, open auth_url to run Meta's signup. When the WhatsApp Business account holds several
    numbers, the redirect to your redirect_uri carries status=selection_required and a connection_id:
    list the numbers with GET /v1/accounts/pending/{connection_id} and pick one with POST
    /v1/accounts/pending/{connection_id}/select.
    Set the top-level redirect_uri field when connecting WhatsApp so the result reaches a page you
    control.

    Args:
        body (ApiEndpointsConnectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsConnectAccountResponse | ApiEndpointsConnectOAuthResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
