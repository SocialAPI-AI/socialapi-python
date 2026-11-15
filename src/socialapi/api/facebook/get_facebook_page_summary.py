from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.facebook_account_summary_response import FacebookAccountSummaryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    page_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page_id"] = page_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/facebook/accounts/{account_id}/summary".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | FacebookAccountSummaryResponse | None:
    if response.status_code == 200:
        response_200 = FacebookAccountSummaryResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | FacebookAccountSummaryResponse]:
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
    page_id: str | Unset = UNSET,
) -> Response[ErrorResponse | FacebookAccountSummaryResponse]:
    """Get Facebook Page insights summary

     Returns trailing-30-day Page insight aggregates (followers, views, reach, post engagements, net
    follower change) for one Page of a connected Facebook account. A Page connected before 2026-10-17,
    or whose login declined the insights permission, returns 403
    platform.facebook.insights_scope_missing and must be reconnected.

    Args:
        account_id (str):
        page_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FacebookAccountSummaryResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        page_id=page_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    page_id: str | Unset = UNSET,
) -> ErrorResponse | FacebookAccountSummaryResponse | None:
    """Get Facebook Page insights summary

     Returns trailing-30-day Page insight aggregates (followers, views, reach, post engagements, net
    follower change) for one Page of a connected Facebook account. A Page connected before 2026-10-17,
    or whose login declined the insights permission, returns 403
    platform.facebook.insights_scope_missing and must be reconnected.

    Args:
        account_id (str):
        page_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FacebookAccountSummaryResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        page_id=page_id,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    page_id: str | Unset = UNSET,
) -> Response[ErrorResponse | FacebookAccountSummaryResponse]:
    """Get Facebook Page insights summary

     Returns trailing-30-day Page insight aggregates (followers, views, reach, post engagements, net
    follower change) for one Page of a connected Facebook account. A Page connected before 2026-10-17,
    or whose login declined the insights permission, returns 403
    platform.facebook.insights_scope_missing and must be reconnected.

    Args:
        account_id (str):
        page_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FacebookAccountSummaryResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        page_id=page_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    page_id: str | Unset = UNSET,
) -> ErrorResponse | FacebookAccountSummaryResponse | None:
    """Get Facebook Page insights summary

     Returns trailing-30-day Page insight aggregates (followers, views, reach, post engagements, net
    follower change) for one Page of a connected Facebook account. A Page connected before 2026-10-17,
    or whose login declined the insights permission, returns 403
    platform.facebook.insights_scope_missing and must be reconnected.

    Args:
        account_id (str):
        page_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FacebookAccountSummaryResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            page_id=page_id,
        )
    ).parsed
