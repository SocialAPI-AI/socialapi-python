from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_facebook_daily_insights_response import ApiEndpointsFacebookDailyInsightsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    page_id: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page_id"] = page_id

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/facebook/accounts/{id}/insights/daily".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsFacebookDailyInsightsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse]:
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
    page_id: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse]:
    """Get daily Facebook Page insights

     Returns one point per day for one Page of a connected Facebook account: followers at the end of the
    day, plus that day's views, reach and post engagements. Days with no data are omitted. Same
    permission errors as the Page insights summary.

    Args:
        id (str):
        page_id (str | Unset):
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        page_id=page_id,
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    page_id: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse | None:
    """Get daily Facebook Page insights

     Returns one point per day for one Page of a connected Facebook account: followers at the end of the
    day, plus that day's views, reach and post engagements. Days with no data are omitted. Same
    permission errors as the Page insights summary.

    Args:
        id (str):
        page_id (str | Unset):
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        page_id=page_id,
        days=days,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    page_id: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse]:
    """Get daily Facebook Page insights

     Returns one point per day for one Page of a connected Facebook account: followers at the end of the
    day, plus that day's views, reach and post engagements. Days with no data are omitted. Same
    permission errors as the Page insights summary.

    Args:
        id (str):
        page_id (str | Unset):
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        page_id=page_id,
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    page_id: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse | None:
    """Get daily Facebook Page insights

     Returns one point per day for one Page of a connected Facebook account: followers at the end of the
    day, plus that day's views, reach and post engagements. Days with no data are omitted. Same
    permission errors as the Page insights summary.

    Args:
        id (str):
        page_id (str | Unset):
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsFacebookDailyInsightsResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page_id=page_id,
            days=days,
        )
    ).parsed
