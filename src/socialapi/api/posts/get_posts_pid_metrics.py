from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_metrics_response_wrapper import ApiEndpointsMetricsResponseWrapper
from ...types import Response


def _get_kwargs(
    pid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/posts/{pid}/metrics".format(
            pid=quote(str(pid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsMetricsResponseWrapper.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper]:
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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper]:
    """Get post metrics

     Fetches engagement metrics from platform APIs for a published post. Accepts the SocialAPI post ID or
    a platform post ID.
    Instagram targets add views, reach and interactions, plus follows, profile visits and profile
    actions on feed posts, and watch time, skip rate and crossposted views on Reels. A metric the
    platform does not report for a post is omitted. If an Instagram target returns none of them,
    reconnect the account to grant the insights permission.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper]
    """

    kwargs = _get_kwargs(
        pid=pid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper | None:
    """Get post metrics

     Fetches engagement metrics from platform APIs for a published post. Accepts the SocialAPI post ID or
    a platform post ID.
    Instagram targets add views, reach and interactions, plus follows, profile visits and profile
    actions on feed posts, and watch time, skip rate and crossposted views on Reels. A metric the
    platform does not report for a post is omitted. If an Instagram target returns none of them,
    reconnect the account to grant the insights permission.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper
    """

    return sync_detailed(
        pid=pid,
        client=client,
    ).parsed


async def asyncio_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper]:
    """Get post metrics

     Fetches engagement metrics from platform APIs for a published post. Accepts the SocialAPI post ID or
    a platform post ID.
    Instagram targets add views, reach and interactions, plus follows, profile visits and profile
    actions on feed posts, and watch time, skip rate and crossposted views on Reels. A metric the
    platform does not report for a post is omitted. If an Instagram target returns none of them,
    reconnect the account to grant the insights permission.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper]
    """

    kwargs = _get_kwargs(
        pid=pid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper | None:
    """Get post metrics

     Fetches engagement metrics from platform APIs for a published post. Accepts the SocialAPI post ID or
    a platform post ID.
    Instagram targets add views, reach and interactions, plus follows, profile visits and profile
    actions on feed posts, and watch time, skip rate and crossposted views on Reels. A metric the
    platform does not report for a post is omitted. If an Instagram target returns none of them,
    reconnect the account to grant the insights permission.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsMetricsResponseWrapper
    """

    return (
        await asyncio_detailed(
            pid=pid,
            client=client,
        )
    ).parsed
