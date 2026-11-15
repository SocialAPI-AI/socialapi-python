from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_instagram_account_summary_response import ApiEndpointsInstagramAccountSummaryResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/instagram/accounts/{id}/summary".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsInstagramAccountSummaryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse]:
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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse]:
    """Get Instagram account insights summary

     Returns live profile counts plus trailing-30-day insight totals (reach, views, interactions, engaged
    accounts, net follower change) for a connected Instagram account. The totals need the analytics.read
    permission. An account without it returns 403 account.permission_missing: add analytics.read to the
    account's permissions or reconnect the account. If Instagram itself has withdrawn the insights
    access, the next call can return 403 platform.instagram.insights_scope_missing instead: reconnect
    the account.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse | None:
    """Get Instagram account insights summary

     Returns live profile counts plus trailing-30-day insight totals (reach, views, interactions, engaged
    accounts, net follower change) for a connected Instagram account. The totals need the analytics.read
    permission. An account without it returns 403 account.permission_missing: add analytics.read to the
    account's permissions or reconnect the account. If Instagram itself has withdrawn the insights
    access, the next call can return 403 platform.instagram.insights_scope_missing instead: reconnect
    the account.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse]:
    """Get Instagram account insights summary

     Returns live profile counts plus trailing-30-day insight totals (reach, views, interactions, engaged
    accounts, net follower change) for a connected Instagram account. The totals need the analytics.read
    permission. An account without it returns 403 account.permission_missing: add analytics.read to the
    account's permissions or reconnect the account. If Instagram itself has withdrawn the insights
    access, the next call can return 403 platform.instagram.insights_scope_missing instead: reconnect
    the account.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse | None:
    """Get Instagram account insights summary

     Returns live profile counts plus trailing-30-day insight totals (reach, views, interactions, engaged
    accounts, net follower change) for a connected Instagram account. The totals need the analytics.read
    permission. An account without it returns 403 account.permission_missing: add analytics.read to the
    account's permissions or reconnect the account. If Instagram itself has withdrawn the insights
    access, the next call can return 403 platform.instagram.insights_scope_missing instead: reconnect
    the account.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsInstagramAccountSummaryResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
