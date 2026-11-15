from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_review_accounts_response import ApiEndpointsReviewAccountsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["platform"] = platform

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/inbox/reviews",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsReviewAccountsResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    platform: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse]:
    """List Accounts with reviews

     Lists your review-capable connected Accounts, each with its live review summary (average rating,
    total count, last review time). Use this to build the reviews inbox navigation, then GET
    /inbox/reviews/{account_id} for one Account's reviews.

    Args:
        platform (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse]
    """

    kwargs = _get_kwargs(
        platform=platform,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    platform: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse | None:
    """List Accounts with reviews

     Lists your review-capable connected Accounts, each with its live review summary (average rating,
    total count, last review time). Use this to build the reviews inbox navigation, then GET
    /inbox/reviews/{account_id} for one Account's reviews.

    Args:
        platform (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse
    """

    return sync_detailed(
        client=client,
        platform=platform,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    platform: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse]:
    """List Accounts with reviews

     Lists your review-capable connected Accounts, each with its live review summary (average rating,
    total count, last review time). Use this to build the reviews inbox navigation, then GET
    /inbox/reviews/{account_id} for one Account's reviews.

    Args:
        platform (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse]
    """

    kwargs = _get_kwargs(
        platform=platform,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    platform: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse | None:
    """List Accounts with reviews

     Lists your review-capable connected Accounts, each with its live review summary (average rating,
    total count, last review time). Use this to build the reviews inbox navigation, then GET
    /inbox/reviews/{account_id} for one Account's reviews.

    Args:
        platform (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsReviewAccountsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
        )
    ).parsed
