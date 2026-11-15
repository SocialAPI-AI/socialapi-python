from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_google_search_keywords_response import ApiEndpointsGoogleSearchKeywordsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
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
        "url": "/platforms/google/accounts/{id}/search-keywords".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsGoogleSearchKeywordsResponse.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse]:
    """Get the search keywords that surfaced a Google Business Profile

     Returns the keywords people searched before seeing the location, aggregated by month over an
    inclusive YYYY-MM range. A low-volume keyword comes back with threshold and is_threshold=true
    instead of value: Google withholds the exact count and gives an upper bound, so treating a threshold
    as a count overstates the keyword. limit is capped at 100 by Google.

    Args:
        id (str):
        start_month (str):
        end_month (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    *,
    client: AuthenticatedClient,
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse | None:
    """Get the search keywords that surfaced a Google Business Profile

     Returns the keywords people searched before seeing the location, aggregated by month over an
    inclusive YYYY-MM range. A low-volume keyword comes back with threshold and is_threshold=true
    instead of value: Google withholds the exact count and gives an upper bound, so treating a threshold
    as a count overstates the keyword. limit is capped at 100 by Google.

    Args:
        id (str):
        start_month (str):
        end_month (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        start_month=start_month,
        end_month=end_month,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse]:
    """Get the search keywords that surfaced a Google Business Profile

     Returns the keywords people searched before seeing the location, aggregated by month over an
    inclusive YYYY-MM range. A low-volume keyword comes back with threshold and is_threshold=true
    instead of value: Google withholds the exact count and gives an upper bound, so treating a threshold
    as a count overstates the keyword. limit is capped at 100 by Google.

    Args:
        id (str):
        start_month (str):
        end_month (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        start_month=start_month,
        end_month=end_month,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    start_month: str,
    end_month: str,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse | None:
    """Get the search keywords that surfaced a Google Business Profile

     Returns the keywords people searched before seeing the location, aggregated by month over an
    inclusive YYYY-MM range. A low-volume keyword comes back with threshold and is_threshold=true
    instead of value: Google withholds the exact count and gives an upper bound, so treating a threshold
    as a count overstates the keyword. limit is capped at 100 by Google.

    Args:
        id (str):
        start_month (str):
        end_month (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleSearchKeywordsResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            start_month=start_month,
            end_month=end_month,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
