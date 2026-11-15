from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.instagram_account_summary_response import InstagramAccountSummaryResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/instagram/accounts/{account_id}/summary".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | InstagramAccountSummaryResponse | None:
    if response.status_code == 200:
        response_200 = InstagramAccountSummaryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | InstagramAccountSummaryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | InstagramAccountSummaryResponse]:
    """Get Instagram account insights summary

     Returns live profile counts plus trailing-30-day insight totals (reach, views, interactions, engaged
    accounts, net follower change) for a connected Instagram account. The totals need the analytics.read
    permission. An account without it returns 403 account.permission_missing: add analytics.read to the
    account's permissions or reconnect the account. If Instagram itself has withdrawn the insights
    access, the next call can return 403 platform.instagram.insights_scope_missing instead: reconnect
    the account.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstagramAccountSummaryResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | InstagramAccountSummaryResponse | None:
    """Get Instagram account insights summary

     Returns live profile counts plus trailing-30-day insight totals (reach, views, interactions, engaged
    accounts, net follower change) for a connected Instagram account. The totals need the analytics.read
    permission. An account without it returns 403 account.permission_missing: add analytics.read to the
    account's permissions or reconnect the account. If Instagram itself has withdrawn the insights
    access, the next call can return 403 platform.instagram.insights_scope_missing instead: reconnect
    the account.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstagramAccountSummaryResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | InstagramAccountSummaryResponse]:
    """Get Instagram account insights summary

     Returns live profile counts plus trailing-30-day insight totals (reach, views, interactions, engaged
    accounts, net follower change) for a connected Instagram account. The totals need the analytics.read
    permission. An account without it returns 403 account.permission_missing: add analytics.read to the
    account's permissions or reconnect the account. If Instagram itself has withdrawn the insights
    access, the next call can return 403 platform.instagram.insights_scope_missing instead: reconnect
    the account.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstagramAccountSummaryResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | InstagramAccountSummaryResponse | None:
    """Get Instagram account insights summary

     Returns live profile counts plus trailing-30-day insight totals (reach, views, interactions, engaged
    accounts, net follower change) for a connected Instagram account. The totals need the analytics.read
    permission. An account without it returns 403 account.permission_missing: add analytics.read to the
    account's permissions or reconnect the account. If Instagram itself has withdrawn the insights
    access, the next call can return 403 platform.instagram.insights_scope_missing instead: reconnect
    the account.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstagramAccountSummaryResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
