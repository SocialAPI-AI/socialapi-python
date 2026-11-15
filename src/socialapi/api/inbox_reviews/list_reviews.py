from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_reviews_order import ListReviewsOrder
from ...models.reviews_list_response import ReviewsListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    order: ListReviewsOrder | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/inbox/reviews/{account_id}".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | ReviewsListResponse | None:
    if response.status_code == 200:
        response_200 = ReviewsListResponse.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | ReviewsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    order: ListReviewsOrder | Unset = UNSET,
) -> Response[ErrorResponse | ReviewsListResponse]:
    """List reviews for an Account

     Returns one page of reviews for a single connected Account, newest first by default. Supported on
    Google Business Profile and App Store Connect. App Store Connect reviews also carry a title; App
    Store Connect does not report an average rating, so summary.average_rating is 0 for those Accounts.

    Args:
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):
        order (ListReviewsOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ReviewsListResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        limit=limit,
        cursor=cursor,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    order: ListReviewsOrder | Unset = UNSET,
) -> ErrorResponse | ReviewsListResponse | None:
    """List reviews for an Account

     Returns one page of reviews for a single connected Account, newest first by default. Supported on
    Google Business Profile and App Store Connect. App Store Connect reviews also carry a title; App
    Store Connect does not report an average rating, so summary.average_rating is 0 for those Accounts.

    Args:
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):
        order (ListReviewsOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ReviewsListResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        limit=limit,
        cursor=cursor,
        order=order,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    order: ListReviewsOrder | Unset = UNSET,
) -> Response[ErrorResponse | ReviewsListResponse]:
    """List reviews for an Account

     Returns one page of reviews for a single connected Account, newest first by default. Supported on
    Google Business Profile and App Store Connect. App Store Connect reviews also carry a title; App
    Store Connect does not report an average rating, so summary.average_rating is 0 for those Accounts.

    Args:
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):
        order (ListReviewsOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ReviewsListResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        limit=limit,
        cursor=cursor,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    order: ListReviewsOrder | Unset = UNSET,
) -> ErrorResponse | ReviewsListResponse | None:
    """List reviews for an Account

     Returns one page of reviews for a single connected Account, newest first by default. Supported on
    Google Business Profile and App Store Connect. App Store Connect reviews also carry a title; App
    Store Connect does not report an average rating, so summary.average_rating is 0 for those Accounts.

    Args:
        account_id (str):
        limit (int | Unset):
        cursor (str | Unset):
        order (ListReviewsOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ReviewsListResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            limit=limit,
            cursor=cursor,
            order=order,
        )
    ).parsed
