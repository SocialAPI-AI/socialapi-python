from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_linked_in_insights_response import ApiEndpointsLinkedInInsightsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    account_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/linkedin/insights",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsLinkedInInsightsResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse]:
    """Get LinkedIn insights

     Returns the follower count plus per-post performance for a connected LinkedIn account. For a company
    Page, `posts` covers the Page's recent posts. For a personal profile, `posts` covers the 5 most
    recent posts published to it through SocialAPI, and `clicks` and `engagement_rate` are always 0.
    `kind` is `organization` for a Page and `member` for a profile.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: str,
) -> ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse | None:
    """Get LinkedIn insights

     Returns the follower count plus per-post performance for a connected LinkedIn account. For a company
    Page, `posts` covers the Page's recent posts. For a personal profile, `posts` covers the 5 most
    recent posts published to it through SocialAPI, and `clicks` and `engagement_rate` are always 0.
    `kind` is `organization` for a Page and `member` for a profile.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse]:
    """Get LinkedIn insights

     Returns the follower count plus per-post performance for a connected LinkedIn account. For a company
    Page, `posts` covers the Page's recent posts. For a personal profile, `posts` covers the 5 most
    recent posts published to it through SocialAPI, and `clicks` and `engagement_rate` are always 0.
    `kind` is `organization` for a Page and `member` for a profile.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str,
) -> ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse | None:
    """Get LinkedIn insights

     Returns the follower count plus per-post performance for a connected LinkedIn account. For a company
    Page, `posts` covers the Page's recent posts. For a personal profile, `posts` covers the 5 most
    recent posts published to it through SocialAPI, and `clicks` and `engagement_rate` are always 0.
    `kind` is `organization` for a Page and `member` for a profile.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsLinkedInInsightsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
        )
    ).parsed
