from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.google_insights_response import GoogleInsightsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    start_date: str,
    end_date: str,
    metric: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start_date"] = start_date

    params["end_date"] = end_date

    params["metric"] = metric

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/accounts/{account_id}/insights".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GoogleInsightsResponse | None:
    if response.status_code == 200:
        response_200 = GoogleInsightsResponse.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | GoogleInsightsResponse]:
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
    start_date: str,
    end_date: str,
    metric: str | Unset = UNSET,
) -> Response[ErrorResponse | GoogleInsightsResponse]:
    """Get Google Business Profile performance metrics

     Returns daily time series for a location: how many people saw it on Google Search and Maps, and how
    many then called, asked for directions, messaged, booked, ordered, or clicked through to the
    website. start_date and end_date are inclusive and formatted YYYY-MM-DD. metric takes a comma-
    separated list and defaults to every metric. A day with no activity comes back as a zero rather than
    a gap. Google publishes no retention window and no freshness lag for this data, so a recent day may
    still be filling in and an old range may return nothing.

    Args:
        account_id (str):
        start_date (str):
        end_date (str):
        metric (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleInsightsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        start_date=start_date,
        end_date=end_date,
        metric=metric,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    metric: str | Unset = UNSET,
) -> ErrorResponse | GoogleInsightsResponse | None:
    """Get Google Business Profile performance metrics

     Returns daily time series for a location: how many people saw it on Google Search and Maps, and how
    many then called, asked for directions, messaged, booked, ordered, or clicked through to the
    website. start_date and end_date are inclusive and formatted YYYY-MM-DD. metric takes a comma-
    separated list and defaults to every metric. A day with no activity comes back as a zero rather than
    a gap. Google publishes no retention window and no freshness lag for this data, so a recent day may
    still be filling in and an old range may return nothing.

    Args:
        account_id (str):
        start_date (str):
        end_date (str):
        metric (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleInsightsResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        start_date=start_date,
        end_date=end_date,
        metric=metric,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    metric: str | Unset = UNSET,
) -> Response[ErrorResponse | GoogleInsightsResponse]:
    """Get Google Business Profile performance metrics

     Returns daily time series for a location: how many people saw it on Google Search and Maps, and how
    many then called, asked for directions, messaged, booked, ordered, or clicked through to the
    website. start_date and end_date are inclusive and formatted YYYY-MM-DD. metric takes a comma-
    separated list and defaults to every metric. A day with no activity comes back as a zero rather than
    a gap. Google publishes no retention window and no freshness lag for this data, so a recent day may
    still be filling in and an old range may return nothing.

    Args:
        account_id (str):
        start_date (str):
        end_date (str):
        metric (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleInsightsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        start_date=start_date,
        end_date=end_date,
        metric=metric,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    metric: str | Unset = UNSET,
) -> ErrorResponse | GoogleInsightsResponse | None:
    """Get Google Business Profile performance metrics

     Returns daily time series for a location: how many people saw it on Google Search and Maps, and how
    many then called, asked for directions, messaged, booked, ordered, or clicked through to the
    website. start_date and end_date are inclusive and formatted YYYY-MM-DD. metric takes a comma-
    separated list and defaults to every metric. A day with no activity comes back as a zero rather than
    a gap. Google publishes no retention window and no freshness lag for this data, so a recent day may
    still be filling in and an old range may return nothing.

    Args:
        account_id (str):
        start_date (str):
        end_date (str):
        metric (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleInsightsResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            start_date=start_date,
            end_date=end_date,
            metric=metric,
        )
    ).parsed
