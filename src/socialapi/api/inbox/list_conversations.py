from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conversations_list_response import ConversationsListResponse
from ...models.error_response import ErrorResponse
from ...models.list_conversations_status import ListConversationsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["brand_id"] = brand_id

    params["page_id"] = page_id

    params["platform"] = platform

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/inbox/conversations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConversationsListResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ConversationsListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ConversationsListResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ConversationsListResponse | ErrorResponse]:
    """List inbox conversations

     Returns paginated DM conversations for the authenticated user, optionally filtered by account,
    platform, and status.

    Args:
        account_id (str | Unset):
        brand_id (str | Unset):
        page_id (str | Unset):
        platform (str | Unset):
        status (ListConversationsStatus | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsListResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        brand_id=brand_id,
        page_id=page_id,
        platform=platform,
        status=status,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ConversationsListResponse | ErrorResponse | None:
    """List inbox conversations

     Returns paginated DM conversations for the authenticated user, optionally filtered by account,
    platform, and status.

    Args:
        account_id (str | Unset):
        brand_id (str | Unset):
        page_id (str | Unset):
        platform (str | Unset):
        status (ListConversationsStatus | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsListResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        brand_id=brand_id,
        page_id=page_id,
        platform=platform,
        status=status,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ConversationsListResponse | ErrorResponse]:
    """List inbox conversations

     Returns paginated DM conversations for the authenticated user, optionally filtered by account,
    platform, and status.

    Args:
        account_id (str | Unset):
        brand_id (str | Unset):
        page_id (str | Unset):
        platform (str | Unset):
        status (ListConversationsStatus | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsListResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        brand_id=brand_id,
        page_id=page_id,
        platform=platform,
        status=status,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    brand_id: str | Unset = UNSET,
    page_id: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ConversationsListResponse | ErrorResponse | None:
    """List inbox conversations

     Returns paginated DM conversations for the authenticated user, optionally filtered by account,
    platform, and status.

    Args:
        account_id (str | Unset):
        brand_id (str | Unset):
        page_id (str | Unset):
        platform (str | Unset):
        status (ListConversationsStatus | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsListResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            brand_id=brand_id,
            page_id=page_id,
            platform=platform,
            status=status,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
