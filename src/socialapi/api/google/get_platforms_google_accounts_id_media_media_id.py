from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_google_media_item import ApiEndpointsGoogleMediaItem
from ...types import Response


def _get_kwargs(
    id: str,
    media_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/accounts/{id}/media/{media_id}".format(
            id=quote(str(id), safe=""),
            media_id=quote(str(media_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsGoogleMediaItem.from_dict(response.json())

        return response_200

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]:
    """Get one Google Business Profile media item

     Returns one photo or video from a location's profile. mediaId accepts either the bare id or the full
    Google resource name returned by the list endpoint.

    Args:
        id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]
    """

    kwargs = _get_kwargs(
        id=id,
        media_id=media_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem | None:
    """Get one Google Business Profile media item

     Returns one photo or video from a location's profile. mediaId accepts either the bare id or the full
    Google resource name returned by the list endpoint.

    Args:
        id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem
    """

    return sync_detailed(
        id=id,
        media_id=media_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]:
    """Get one Google Business Profile media item

     Returns one photo or video from a location's profile. mediaId accepts either the bare id or the full
    Google resource name returned by the list endpoint.

    Args:
        id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]
    """

    kwargs = _get_kwargs(
        id=id,
        media_id=media_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem | None:
    """Get one Google Business Profile media item

     Returns one photo or video from a location's profile. mediaId accepts either the bare id or the full
    Google resource name returned by the list endpoint.

    Args:
        id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem
    """

    return (
        await asyncio_detailed(
            id=id,
            media_id=media_id,
            client=client,
        )
    ).parsed
