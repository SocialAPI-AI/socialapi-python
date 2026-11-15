from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_exports_list_response import ApiEndpointsExportsListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsExportsListResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse]:
    """List analytics exports

     Returns the 50 most recent export jobs for the authenticated user. Optionally filter by status.

    Args:
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse]
    """

    kwargs = _get_kwargs(
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse | None:
    """List analytics exports

     Returns the 50 most recent export jobs for the authenticated user. Optionally filter by status.

    Args:
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse
    """

    return sync_detailed(
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse]:
    """List analytics exports

     Returns the 50 most recent export jobs for the authenticated user. Optionally filter by status.

    Args:
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse]
    """

    kwargs = _get_kwargs(
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse | None:
    """List analytics exports

     Returns the 50 most recent export jobs for the authenticated user. Optionally filter by status.

    Args:
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsExportsListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
        )
    ).parsed
