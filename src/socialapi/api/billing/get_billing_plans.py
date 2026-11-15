from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_billing_plans_response import ApiEndpointsBillingPlansResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/billing/plans",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsBillingPlansResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse]:
    """List plans

     Returns every subscription tier with prices and resource limits, ordered from cheapest to most
    expensive. Each tier is priced in USD and in EUR. -1 means unlimited for limits and custom pricing
    for prices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse | None:
    """List plans

     Returns every subscription tier with prices and resource limits, ordered from cheapest to most
    expensive. Each tier is priced in USD and in EUR. -1 means unlimited for limits and custom pricing
    for prices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse]:
    """List plans

     Returns every subscription tier with prices and resource limits, ordered from cheapest to most
    expensive. Each tier is priced in USD and in EUR. -1 means unlimited for limits and custom pricing
    for prices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse | None:
    """List plans

     Returns every subscription tier with prices and resource limits, ordered from cheapest to most
    expensive. Each tier is priced in USD and in EUR. -1 means unlimited for limits and custom pricing
    for prices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsBillingPlansResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
