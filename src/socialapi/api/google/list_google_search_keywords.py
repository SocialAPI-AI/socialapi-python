from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.google_search_keywords_response import GoogleSearchKeywordsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start_month"] = start_month

    params["end_month"] = end_month

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/accounts/{account_id}/search-keywords".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GoogleSearchKeywordsResponse | None:
    if response.status_code == 200:
        response_200 = GoogleSearchKeywordsResponse.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | GoogleSearchKeywordsResponse]:
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
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | GoogleSearchKeywordsResponse]:
    """Get the search keywords that surfaced a Google Business Profile

     Returns the keywords people searched before seeing the location, aggregated by month over an
    inclusive YYYY-MM range. A low-volume keyword comes back with threshold and is_threshold=true
    instead of value: Google withholds the exact count and gives an upper bound, so treating a threshold
    as a count overstates the keyword. limit is capped at 100 by Google.

    Args:
        account_id (str):
        start_month (str):
        end_month (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleSearchKeywordsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        start_month=start_month,
        end_month=end_month,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | GoogleSearchKeywordsResponse | None:
    """Get the search keywords that surfaced a Google Business Profile

     Returns the keywords people searched before seeing the location, aggregated by month over an
    inclusive YYYY-MM range. A low-volume keyword comes back with threshold and is_threshold=true
    instead of value: Google withholds the exact count and gives an upper bound, so treating a threshold
    as a count overstates the keyword. limit is capped at 100 by Google.

    Args:
        account_id (str):
        start_month (str):
        end_month (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleSearchKeywordsResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        start_month=start_month,
        end_month=end_month,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | GoogleSearchKeywordsResponse]:
    """Get the search keywords that surfaced a Google Business Profile

     Returns the keywords people searched before seeing the location, aggregated by month over an
    inclusive YYYY-MM range. A low-volume keyword comes back with threshold and is_threshold=true
    instead of value: Google withholds the exact count and gives an upper bound, so treating a threshold
    as a count overstates the keyword. limit is capped at 100 by Google.

    Args:
        account_id (str):
        start_month (str):
        end_month (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleSearchKeywordsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        start_month=start_month,
        end_month=end_month,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | GoogleSearchKeywordsResponse | None:
    """Get the search keywords that surfaced a Google Business Profile

     Returns the keywords people searched before seeing the location, aggregated by month over an
    inclusive YYYY-MM range. A low-volume keyword comes back with threshold and is_threshold=true
    instead of value: Google withholds the exact count and gives an upper bound, so treating a threshold
    as a count overstates the keyword. limit is capped at 100 by Google.

    Args:
        account_id (str):
        start_month (str):
        end_month (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleSearchKeywordsResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            start_month=start_month,
            end_month=end_month,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
