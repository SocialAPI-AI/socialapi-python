from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_delivery_list_response import ApiEndpointsDeliveryListResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    status: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["status"] = status

    params["event_type"] = event_type

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhooks/{id}/deliveries".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsDeliveryListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse]:
    """List webhook deliveries

     Returns recent delivery attempts for a webhook endpoint. Optionally filter by status (success,
    failed, pending) or event_type. Cursor-paginated.

    Args:
        id (str):
        status (str | Unset):
        event_type (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        event_type=event_type,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse | None:
    """List webhook deliveries

     Returns recent delivery attempts for a webhook endpoint. Optionally filter by status (success,
    failed, pending) or event_type. Cursor-paginated.

    Args:
        id (str):
        status (str | Unset):
        event_type (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        status=status,
        event_type=event_type,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse]:
    """List webhook deliveries

     Returns recent delivery attempts for a webhook endpoint. Optionally filter by status (success,
    failed, pending) or event_type. Cursor-paginated.

    Args:
        id (str):
        status (str | Unset):
        event_type (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        event_type=event_type,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse | None:
    """List webhook deliveries

     Returns recent delivery attempts for a webhook endpoint. Optionally filter by status (success,
    failed, pending) or event_type. Cursor-paginated.

    Args:
        id (str):
        status (str | Unset):
        event_type (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsDeliveryListResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            status=status,
            event_type=event_type,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
