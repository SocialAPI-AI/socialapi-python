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
    comment_id: str,
    *,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/inbox/comments/{post_id}/{comment_id}/replies".format(
            post_id=quote(str(post_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
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

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

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
    comment_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]:
    """List replies to a comment

     Returns paginated replies to a specific comment. Same response shape as top-level comments. Uses
    cursor-based pagination.

    Args:
        post_id (str):
        comment_id (str):
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        comment_id=comment_id,
        account_id=account_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse | None:
    """List replies to a comment

     Returns paginated replies to a specific comment. Same response shape as top-level comments. Uses
    cursor-based pagination.

    Args:
        post_id (str):
        comment_id (str):
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        post_id=post_id,
        comment_id=comment_id,
        client=client,
        account_id=account_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]:
    """List replies to a comment

     Returns paginated replies to a specific comment. Same response shape as top-level comments. Uses
    cursor-based pagination.

    Args:
        post_id (str):
        comment_id (str):
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        comment_id=comment_id,
        account_id=account_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse | None:
    """List replies to a comment

     Returns paginated replies to a specific comment. Same response shape as top-level comments. Uses
    cursor-based pagination.

    Args:
        post_id (str):
        comment_id (str):
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCommentsWithCapsListResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            comment_id=comment_id,
            client=client,
            account_id=account_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
