from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_threads_insights_response import ApiEndpointsThreadsInsightsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: str,
    level: str,
    post_id: str | Unset = UNSET,
    metric: str | Unset = UNSET,
    breakdown: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["level"] = level

    params["post_id"] = post_id

    params["metric"] = metric

    params["breakdown"] = breakdown

    params["since"] = since

    params["until"] = until

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/threads/insights",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsThreadsInsightsResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str,
    level: str,
    post_id: str | Unset = UNSET,
    metric: str | Unset = UNSET,
    breakdown: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse]:
    """Get Threads insights

     Returns engagement metrics for a single Threads post (level=media) or for the connected account
    (level=account). An account connected before 2026-10-17 returns 403
    platform.threads.insights_scope_missing until it is reconnected. Media metrics are views, likes,
    replies, reposts, quotes and shares. Account metrics are those five plus clicks, followers_count and
    follower_demographics. shares is media-only and clicks is account-only. follower_demographics
    requires exactly one breakdown (country, city, age or gender) and rejects since or until.

    Args:
        account_id (str):
        level (str):
        post_id (str | Unset):
        metric (str | Unset):
        breakdown (str | Unset):
        since (int | Unset):
        until (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        level=level,
        post_id=post_id,
        metric=metric,
        breakdown=breakdown,
        since=since,
        until=until,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: str,
    level: str,
    post_id: str | Unset = UNSET,
    metric: str | Unset = UNSET,
    breakdown: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse | None:
    """Get Threads insights

     Returns engagement metrics for a single Threads post (level=media) or for the connected account
    (level=account). An account connected before 2026-10-17 returns 403
    platform.threads.insights_scope_missing until it is reconnected. Media metrics are views, likes,
    replies, reposts, quotes and shares. Account metrics are those five plus clicks, followers_count and
    follower_demographics. shares is media-only and clicks is account-only. follower_demographics
    requires exactly one breakdown (country, city, age or gender) and rejects since or until.

    Args:
        account_id (str):
        level (str):
        post_id (str | Unset):
        metric (str | Unset):
        breakdown (str | Unset):
        since (int | Unset):
        until (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        level=level,
        post_id=post_id,
        metric=metric,
        breakdown=breakdown,
        since=since,
        until=until,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str,
    level: str,
    post_id: str | Unset = UNSET,
    metric: str | Unset = UNSET,
    breakdown: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse]:
    """Get Threads insights

     Returns engagement metrics for a single Threads post (level=media) or for the connected account
    (level=account). An account connected before 2026-10-17 returns 403
    platform.threads.insights_scope_missing until it is reconnected. Media metrics are views, likes,
    replies, reposts, quotes and shares. Account metrics are those five plus clicks, followers_count and
    follower_demographics. shares is media-only and clicks is account-only. follower_demographics
    requires exactly one breakdown (country, city, age or gender) and rejects since or until.

    Args:
        account_id (str):
        level (str):
        post_id (str | Unset):
        metric (str | Unset):
        breakdown (str | Unset):
        since (int | Unset):
        until (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        level=level,
        post_id=post_id,
        metric=metric,
        breakdown=breakdown,
        since=since,
        until=until,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str,
    level: str,
    post_id: str | Unset = UNSET,
    metric: str | Unset = UNSET,
    breakdown: str | Unset = UNSET,
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse | None:
    """Get Threads insights

     Returns engagement metrics for a single Threads post (level=media) or for the connected account
    (level=account). An account connected before 2026-10-17 returns 403
    platform.threads.insights_scope_missing until it is reconnected. Media metrics are views, likes,
    replies, reposts, quotes and shares. Account metrics are those five plus clicks, followers_count and
    follower_demographics. shares is media-only and clicks is account-only. follower_demographics
    requires exactly one breakdown (country, city, age or gender) and rejects since or until.

    Args:
        account_id (str):
        level (str):
        post_id (str | Unset):
        metric (str | Unset):
        breakdown (str | Unset):
        since (int | Unset):
        until (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsThreadsInsightsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            level=level,
            post_id=post_id,
            metric=metric,
            breakdown=breakdown,
            since=since,
            until=until,
        )
    ).parsed
