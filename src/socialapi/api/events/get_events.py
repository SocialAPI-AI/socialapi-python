from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_events_list_response import ApiEndpointsEventsListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    action: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category"] = category

    params["status"] = status

    params["platform"] = platform

    params["account_id"] = account_id

    params["resource_id"] = resource_id

    params["action"] = action

    params["from"] = from_

    params["to"] = to

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsEventsListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    action: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse]:
    """List developer events

     Returns a paginated, filtered slice of the unified event log. Events cover post lifecycle, inbox
    activity, account changes, and webhook deliveries. Retention varies by plan tier; the response
    includes the user's current retention window.

    Args:
        category (str | Unset):
        status (str | Unset):
        platform (str | Unset):
        account_id (str | Unset):
        resource_id (str | Unset):
        action (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse]
    """

    kwargs = _get_kwargs(
        category=category,
        status=status,
        platform=platform,
        account_id=account_id,
        resource_id=resource_id,
        action=action,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    action: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse | None:
    """List developer events

     Returns a paginated, filtered slice of the unified event log. Events cover post lifecycle, inbox
    activity, account changes, and webhook deliveries. Retention varies by plan tier; the response
    includes the user's current retention window.

    Args:
        category (str | Unset):
        status (str | Unset):
        platform (str | Unset):
        account_id (str | Unset):
        resource_id (str | Unset):
        action (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse
    """

    return sync_detailed(
        client=client,
        category=category,
        status=status,
        platform=platform,
        account_id=account_id,
        resource_id=resource_id,
        action=action,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    action: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse]:
    """List developer events

     Returns a paginated, filtered slice of the unified event log. Events cover post lifecycle, inbox
    activity, account changes, and webhook deliveries. Retention varies by plan tier; the response
    includes the user's current retention window.

    Args:
        category (str | Unset):
        status (str | Unset):
        platform (str | Unset):
        account_id (str | Unset):
        resource_id (str | Unset):
        action (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse]
    """

    kwargs = _get_kwargs(
        category=category,
        status=status,
        platform=platform,
        account_id=account_id,
        resource_id=resource_id,
        action=action,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category: str | Unset = UNSET,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    action: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse | None:
    """List developer events

     Returns a paginated, filtered slice of the unified event log. Events cover post lifecycle, inbox
    activity, account changes, and webhook deliveries. Retention varies by plan tier; the response
    includes the user's current retention window.

    Args:
        category (str | Unset):
        status (str | Unset):
        platform (str | Unset):
        account_id (str | Unset):
        resource_id (str | Unset):
        action (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsEventsListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            status=status,
            platform=platform,
            account_id=account_id,
            resource_id=resource_id,
            action=action,
            from_=from_,
            to=to,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
