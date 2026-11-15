from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.metrics_response_wrapper import MetricsResponseWrapper
from ...types import Response


def _get_kwargs(
    post_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/posts/{post_id}/metrics".format(
            post_id=quote(str(post_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | MetricsResponseWrapper | None:
    if response.status_code == 200:
        response_200 = MetricsResponseWrapper.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | MetricsResponseWrapper]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    post_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | MetricsResponseWrapper]:
    """Get post metrics

     Fetches engagement metrics from platform APIs for a published post. Accepts the SocialAPI post ID or
    a platform post ID.
    Instagram targets add views, reach and interactions, plus follows, profile visits and profile
    actions on feed posts, and watch time, skip rate and crossposted views on Reels. A metric the
    platform does not report for a post is omitted. If an Instagram target returns none of them,
    reconnect the account to grant the insights permission.

    Args:
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MetricsResponseWrapper]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | MetricsResponseWrapper | None:
    """Get post metrics

     Fetches engagement metrics from platform APIs for a published post. Accepts the SocialAPI post ID or
    a platform post ID.
    Instagram targets add views, reach and interactions, plus follows, profile visits and profile
    actions on feed posts, and watch time, skip rate and crossposted views on Reels. A metric the
    platform does not report for a post is omitted. If an Instagram target returns none of them,
    reconnect the account to grant the insights permission.

    Args:
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MetricsResponseWrapper
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | MetricsResponseWrapper]:
    """Get post metrics

     Fetches engagement metrics from platform APIs for a published post. Accepts the SocialAPI post ID or
    a platform post ID.
    Instagram targets add views, reach and interactions, plus follows, profile visits and profile
    actions on feed posts, and watch time, skip rate and crossposted views on Reels. A metric the
    platform does not report for a post is omitted. If an Instagram target returns none of them,
    reconnect the account to grant the insights permission.

    Args:
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MetricsResponseWrapper]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | MetricsResponseWrapper | None:
    """Get post metrics

     Fetches engagement metrics from platform APIs for a published post. Accepts the SocialAPI post ID or
    a platform post ID.
    Instagram targets add views, reach and interactions, plus follows, profile visits and profile
    actions on feed posts, and watch time, skip rate and crossposted views on Reels. A metric the
    platform does not report for a post is omitted. If an Instagram target returns none of them,
    reconnect the account to grant the insights permission.

    Args:
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MetricsResponseWrapper
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
        )
    ).parsed
