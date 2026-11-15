from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_analytics_overview_response_wrapper import ApiEndpointsAnalyticsOverviewResponseWrapper
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tz: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["tz"] = tz

    params["account_id"] = account_id

    params["brand_id"] = brand_id

    params["platform"] = platform

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/overview",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsAnalyticsOverviewResponseWrapper.from_dict(response.json())

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
) -> Response[ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tz: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse]:
    """Get analytics overview

     Summarises how the posts published in a range performed: totals against the previous range of equal
    length, engagement per publish day, breakdowns by platform and media type, the top posts, the hours
    your posts did best in, and the daily replies, DMs and moderation SocialAPI performed. Covers every
    account the key can read, or one account, brand, or platform.
    Engagements are likes + comments + shares + saves. Views are reported apart, by the platforms that
    publish them. Counters are the ones SocialAPI last synced (see metrics_synced_at), so this makes no
    platform call and costs no credits. Accounts without the analytics.read permission are left out and
    counted in accounts_excluded.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        tz (str | Unset):
        account_id (str | Unset):
        brand_id (str | Unset):
        platform (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        tz=tz,
        account_id=account_id,
        brand_id=brand_id,
        platform=platform,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tz: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse | None:
    """Get analytics overview

     Summarises how the posts published in a range performed: totals against the previous range of equal
    length, engagement per publish day, breakdowns by platform and media type, the top posts, the hours
    your posts did best in, and the daily replies, DMs and moderation SocialAPI performed. Covers every
    account the key can read, or one account, brand, or platform.
    Engagements are likes + comments + shares + saves. Views are reported apart, by the platforms that
    publish them. Counters are the ones SocialAPI last synced (see metrics_synced_at), so this makes no
    platform call and costs no credits. Accounts without the analytics.read permission are left out and
    counted in accounts_excluded.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        tz (str | Unset):
        account_id (str | Unset):
        brand_id (str | Unset):
        platform (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        tz=tz,
        account_id=account_id,
        brand_id=brand_id,
        platform=platform,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tz: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse]:
    """Get analytics overview

     Summarises how the posts published in a range performed: totals against the previous range of equal
    length, engagement per publish day, breakdowns by platform and media type, the top posts, the hours
    your posts did best in, and the daily replies, DMs and moderation SocialAPI performed. Covers every
    account the key can read, or one account, brand, or platform.
    Engagements are likes + comments + shares + saves. Views are reported apart, by the platforms that
    publish them. Counters are the ones SocialAPI last synced (see metrics_synced_at), so this makes no
    platform call and costs no credits. Accounts without the analytics.read permission are left out and
    counted in accounts_excluded.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        tz (str | Unset):
        account_id (str | Unset):
        brand_id (str | Unset):
        platform (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        tz=tz,
        account_id=account_id,
        brand_id=brand_id,
        platform=platform,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tz: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse | None:
    """Get analytics overview

     Summarises how the posts published in a range performed: totals against the previous range of equal
    length, engagement per publish day, breakdowns by platform and media type, the top posts, the hours
    your posts did best in, and the daily replies, DMs and moderation SocialAPI performed. Covers every
    account the key can read, or one account, brand, or platform.
    Engagements are likes + comments + shares + saves. Views are reported apart, by the platforms that
    publish them. Counters are the ones SocialAPI last synced (see metrics_synced_at), so this makes no
    platform call and costs no credits. Accounts without the analytics.read permission are left out and
    counted in accounts_excluded.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        tz (str | Unset):
        account_id (str | Unset):
        brand_id (str | Unset):
        platform (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAnalyticsOverviewResponseWrapper | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            tz=tz,
            account_id=account_id,
            brand_id=brand_id,
            platform=platform,
            sort=sort,
        )
    ).parsed
