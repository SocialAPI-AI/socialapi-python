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
    brand_id: str,
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["metrics"] = metrics

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/brands/{brand_id}/analytics".format(
            brand_id=quote(str(brand_id), safe=""),
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
    brand_id: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> Response[AnalyticsResponseWrapper | ErrorResponse]:
    """Get brand analytics history

     Returns daily history for every account and page in a brand, summed per metric per day. A brand
    total always reflects the accounts the brand holds right now.
    Read subjects_counted before drawing a chart. A brand whose accounts did not all report on a given
    day produces a lower sum for that day, and without the count that reads as a decline instead of a
    gap.

    Args:
        brand_id (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsResponseWrapper | ErrorResponse]
    """

    kwargs = _get_kwargs(
        brand_id=brand_id,
        from_=from_,
        to=to,
        metrics=metrics,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    brand_id: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> AnalyticsResponseWrapper | ErrorResponse | None:
    """Get brand analytics history

     Returns daily history for every account and page in a brand, summed per metric per day. A brand
    total always reflects the accounts the brand holds right now.
    Read subjects_counted before drawing a chart. A brand whose accounts did not all report on a given
    day produces a lower sum for that day, and without the count that reads as a decline instead of a
    gap.

    Args:
        brand_id (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsResponseWrapper | ErrorResponse
    """

    return sync_detailed(
        brand_id=brand_id,
        client=client,
        from_=from_,
        to=to,
        metrics=metrics,
    ).parsed


async def asyncio_detailed(
    brand_id: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> Response[AnalyticsResponseWrapper | ErrorResponse]:
    """Get brand analytics history

     Returns daily history for every account and page in a brand, summed per metric per day. A brand
    total always reflects the accounts the brand holds right now.
    Read subjects_counted before drawing a chart. A brand whose accounts did not all report on a given
    day produces a lower sum for that day, and without the count that reads as a decline instead of a
    gap.

    Args:
        brand_id (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsResponseWrapper | ErrorResponse]
    """

    kwargs = _get_kwargs(
        brand_id=brand_id,
        from_=from_,
        to=to,
        metrics=metrics,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    brand_id: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> AnalyticsResponseWrapper | ErrorResponse | None:
    """Get brand analytics history

     Returns daily history for every account and page in a brand, summed per metric per day. A brand
    total always reflects the accounts the brand holds right now.
    Read subjects_counted before drawing a chart. A brand whose accounts did not all report on a given
    day produces a lower sum for that day, and without the count that reads as a decline instead of a
    gap.

    Args:
        brand_id (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsResponseWrapper | ErrorResponse
    """

    return (
        await asyncio_detailed(
            brand_id=brand_id,
            client=client,
            from_=from_,
            to=to,
            metrics=metrics,
        )
    ).parsed
