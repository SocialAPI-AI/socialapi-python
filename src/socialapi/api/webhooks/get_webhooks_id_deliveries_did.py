from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_delivery_detail_response import ApiEndpointsDeliveryDetailResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
    did: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhooks/{id}/deliveries/{did}".format(
            id=quote(str(id), safe=""),
            did=quote(str(did), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsDeliveryDetailResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    did: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse]:
    """Get webhook delivery

     Returns the full record of a single webhook delivery attempt, including request payload, response
    status, response body excerpt, and timing.

    Args:
        id (str):
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        did=did,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    did: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse | None:
    """Get webhook delivery

     Returns the full record of a single webhook delivery attempt, including request payload, response
    status, response body excerpt, and timing.

    Args:
        id (str):
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        id=id,
        did=did,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    did: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse]:
    """Get webhook delivery

     Returns the full record of a single webhook delivery attempt, including request payload, response
    status, response body excerpt, and timing.

    Args:
        id (str):
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        did=did,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    did: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse | None:
    """Get webhook delivery

     Returns the full record of a single webhook delivery attempt, including request payload, response
    status, response body excerpt, and timing.

    Args:
        id (str):
        did (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsDeliveryDetailResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            did=did,
            client=client,
        )
    ).parsed
