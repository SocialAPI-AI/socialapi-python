from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_migration_response import ApiEndpointsMigrationResponse
from ...models.api_endpoints_start_migration_request import ApiEndpointsStartMigrationRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ApiEndpointsStartMigrationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/migrations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse | None:
    if response.status_code == 201:
        response_201 = ApiEndpointsMigrationResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsStartMigrationRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse]:
    """Start a migration

     Starts a migration from another provider with an API key from your account there, and returns the
    first assessment of your accounts. Calling it again replaces the key. You must accept the current
    authorisation text: send its `version` from `GET /v1/migrations/{provider}`. Dashboard sessions
    only; API keys get 403.

    Args:
        body (ApiEndpointsStartMigrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse]
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
    body: ApiEndpointsStartMigrationRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse | None:
    """Start a migration

     Starts a migration from another provider with an API key from your account there, and returns the
    first assessment of your accounts. Calling it again replaces the key. You must accept the current
    authorisation text: send its `version` from `GET /v1/migrations/{provider}`. Dashboard sessions
    only; API keys get 403.

    Args:
        body (ApiEndpointsStartMigrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsStartMigrationRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse]:
    """Start a migration

     Starts a migration from another provider with an API key from your account there, and returns the
    first assessment of your accounts. Calling it again replaces the key. You must accept the current
    authorisation text: send its `version` from `GET /v1/migrations/{provider}`. Dashboard sessions
    only; API keys get 403.

    Args:
        body (ApiEndpointsStartMigrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsStartMigrationRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse | None:
    """Start a migration

     Starts a migration from another provider with an API key from your account there, and returns the
    first assessment of your accounts. Calling it again replaces the key. You must accept the current
    authorisation text: send its `version` from `GET /v1/migrations/{provider}`. Dashboard sessions
    only; API keys get 403.

    Args:
        body (ApiEndpointsStartMigrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsMigrationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
