from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_response_wrapper import AnalyticsResponseWrapper
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["metrics"] = metrics

    params["page_id"] = page_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_id}/analytics".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AnalyticsResponseWrapper | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AnalyticsResponseWrapper.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AnalyticsResponseWrapper | ErrorResponse]:
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
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
) -> Response[AnalyticsResponseWrapper | ErrorResponse]:
    """Get account analytics history

     Returns daily counts of the replies, private replies, DMs, review and mention replies, and comment
    moderation SocialAPI performed for a connected account. An account with none of these in the range
    returns an empty series. Follower, reach and view figures are not part of this history: read them
    from the platform insight routes, such as GET /v1/platforms/instagram/accounts/{account_id}/summary.
    Each series names its metric kind (gauge for a level you may diff, flow for a per-day count you may
    sum) and the timezone its days were cut on. Every point also carries how many subjects contributed
    to that day, always present and always at least 1, even for a single-subject account.

    Args:
        account_id (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):
        page_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsResponseWrapper | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        from_=from_,
        to=to,
        metrics=metrics,
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
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
) -> AnalyticsResponseWrapper | ErrorResponse | None:
    """Get account analytics history

     Returns daily counts of the replies, private replies, DMs, review and mention replies, and comment
    moderation SocialAPI performed for a connected account. An account with none of these in the range
    returns an empty series. Follower, reach and view figures are not part of this history: read them
    from the platform insight routes, such as GET /v1/platforms/instagram/accounts/{account_id}/summary.
    Each series names its metric kind (gauge for a level you may diff, flow for a per-day count you may
    sum) and the timezone its days were cut on. Every point also carries how many subjects contributed
    to that day, always present and always at least 1, even for a single-subject account.

    Args:
        account_id (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):
        page_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsResponseWrapper | ErrorResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        from_=from_,
        to=to,
        metrics=metrics,
        page_id=page_id,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
) -> Response[AnalyticsResponseWrapper | ErrorResponse]:
    """Get account analytics history

     Returns daily counts of the replies, private replies, DMs, review and mention replies, and comment
    moderation SocialAPI performed for a connected account. An account with none of these in the range
    returns an empty series. Follower, reach and view figures are not part of this history: read them
    from the platform insight routes, such as GET /v1/platforms/instagram/accounts/{account_id}/summary.
    Each series names its metric kind (gauge for a level you may diff, flow for a per-day count you may
    sum) and the timezone its days were cut on. Every point also carries how many subjects contributed
    to that day, always present and always at least 1, even for a single-subject account.

    Args:
        account_id (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):
        page_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsResponseWrapper | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        from_=from_,
        to=to,
        metrics=metrics,
        page_id=page_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
) -> AnalyticsResponseWrapper | ErrorResponse | None:
    """Get account analytics history

     Returns daily counts of the replies, private replies, DMs, review and mention replies, and comment
    moderation SocialAPI performed for a connected account. An account with none of these in the range
    returns an empty series. Follower, reach and view figures are not part of this history: read them
    from the platform insight routes, such as GET /v1/platforms/instagram/accounts/{account_id}/summary.
    Each series names its metric kind (gauge for a level you may diff, flow for a per-day count you may
    sum) and the timezone its days were cut on. Every point also carries how many subjects contributed
    to that day, always present and always at least 1, even for a single-subject account.

    Args:
        account_id (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):
        page_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsResponseWrapper | ErrorResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            from_=from_,
            to=to,
            metrics=metrics,
            page_id=page_id,
        )
    ).parsed
