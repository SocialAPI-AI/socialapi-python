from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_storage_usage_response import ApiEndpointsStorageUsageResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/media/storage",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsStorageUsageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse]:
    """Get storage usage

     Returns total bytes used, the plan limit, and file count for the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse | None:
    """Get storage usage

     Returns total bytes used, the plan limit, and file count for the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse]:
    """Get storage usage

     Returns total bytes used, the plan limit, and file count for the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse | None:
    """Get storage usage

     Returns total bytes used, the plan limit, and file count for the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsStorageUsageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
