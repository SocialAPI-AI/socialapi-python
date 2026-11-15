from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_analytics_response_wrapper import ApiEndpointsAnalyticsResponseWrapper
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pid: str,
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
        "url": "/posts/{pid}/analytics".format(
            pid=quote(str(pid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsAnalyticsResponseWrapper.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> Response[ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse]:
    """Get post analytics history

     Returns daily history for a published post: how its engagement counters accrued, one point per day.
    This is the history route. For the post's current figures, use GET /v1/posts/{pid}/metrics instead.
    History does not extend back before the post was first tracked, so an older post may have no earlier
    points.

    Args:
        pid (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        pid=pid,
        from_=from_,
        to=to,
        metrics=metrics,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pid: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse | None:
    """Get post analytics history

     Returns daily history for a published post: how its engagement counters accrued, one point per day.
    This is the history route. For the post's current figures, use GET /v1/posts/{pid}/metrics instead.
    History does not extend back before the post was first tracked, so an older post may have no earlier
    points.

    Args:
        pid (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        pid=pid,
        client=client,
        from_=from_,
        to=to,
        metrics=metrics,
    ).parsed


async def asyncio_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> Response[ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse]:
    """Get post analytics history

     Returns daily history for a published post: how its engagement counters accrued, one point per day.
    This is the history route. For the post's current figures, use GET /v1/posts/{pid}/metrics instead.
    History does not extend back before the post was first tracked, so an older post may have no earlier
    points.

    Args:
        pid (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        pid=pid,
        from_=from_,
        to=to,
        metrics=metrics,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pid: str,
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    metrics: str | Unset = UNSET,
) -> ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse | None:
    """Get post analytics history

     Returns daily history for a published post: how its engagement counters accrued, one point per day.
    This is the history route. For the post's current figures, use GET /v1/posts/{pid}/metrics instead.
    History does not extend back before the post was first tracked, so an older post may have no earlier
    points.

    Args:
        pid (str):
        from_ (str | Unset):
        to (str | Unset):
        metrics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAnalyticsResponseWrapper | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            pid=pid,
            client=client,
            from_=from_,
            to=to,
            metrics=metrics,
        )
    ).parsed
