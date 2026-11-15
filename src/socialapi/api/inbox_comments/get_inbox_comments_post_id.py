from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_comments_with_caps_list_response import ApiEndpointsCommentsWithCapsListResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    post_id: str,
    *,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    moderation_status: str | Unset = UNSET,
    order: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["limit"] = limit

    params["cursor"] = cursor

    params["moderation_status"] = moderation_status

    params["order"] = order

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/inbox/comments/{post_id}".format(
            post_id=quote(str(post_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsCommentsWithCapsListResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]:
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
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    moderation_status: str | Unset = UNSET,
    order: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]:
    """List comments on a post

     Returns comments for a specific inbox post, including per-platform capability flags (can_reply,
    can_delete, can_hide, can_like, can_private_reply). Uses cursor-based pagination.

    Args:
        post_id (str):
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):
        moderation_status (str | Unset):
        order (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        account_id=account_id,
        limit=limit,
        cursor=cursor,
        moderation_status=moderation_status,
        order=order,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    moderation_status: str | Unset = UNSET,
    order: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse | None:
    """List comments on a post

     Returns comments for a specific inbox post, including per-platform capability flags (can_reply,
    can_delete, can_hide, can_like, can_private_reply). Uses cursor-based pagination.

    Args:
        post_id (str):
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):
        moderation_status (str | Unset):
        order (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
        account_id=account_id,
        limit=limit,
        cursor=cursor,
        moderation_status=moderation_status,
        order=order,
        q=q,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    moderation_status: str | Unset = UNSET,
    order: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]:
    """List comments on a post

     Returns comments for a specific inbox post, including per-platform capability flags (can_reply,
    can_delete, can_hide, can_like, can_private_reply). Uses cursor-based pagination.

    Args:
        post_id (str):
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):
        moderation_status (str | Unset):
        order (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        account_id=account_id,
        limit=limit,
        cursor=cursor,
        moderation_status=moderation_status,
        order=order,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    moderation_status: str | Unset = UNSET,
    order: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse | None:
    """List comments on a post

     Returns comments for a specific inbox post, including per-platform capability flags (can_reply,
    can_delete, can_hide, can_like, can_private_reply). Uses cursor-based pagination.

    Args:
        post_id (str):
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):
        moderation_status (str | Unset):
        order (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
            account_id=account_id,
            limit=limit,
            cursor=cursor,
            moderation_status=moderation_status,
            order=order,
            q=q,
        )
    ).parsed
