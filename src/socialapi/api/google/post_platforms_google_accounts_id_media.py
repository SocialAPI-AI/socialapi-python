from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_create_google_media_request import ApiEndpointsCreateGoogleMediaRequest
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_google_media_item import ApiEndpointsGoogleMediaItem
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ApiEndpointsCreateGoogleMediaRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/google/accounts/{id}/media".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem | None:
    if response.status_code == 201:
        response_201 = ApiEndpointsGoogleMediaItem.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_422

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
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateGoogleMediaRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]:
    """Add media to a Google Business Profile location

     Attaches one photo or video to a location's public profile under the given category. media takes
    exactly one item in the same form the publishing endpoints accept: a stored media library id
    (source_type media_id), a public URL (url), or a reference to bytes you uploaded to Google yourself
    (platform_attachment_id). The photo or video format is derived from the item you supply, so you
    never set Google's own upload fields. Google limits a location to 10 edits per minute, and that
    limit cannot be raised.

    Args:
        id (str):
        body (ApiEndpointsCreateGoogleMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateGoogleMediaRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem | None:
    """Add media to a Google Business Profile location

     Attaches one photo or video to a location's public profile under the given category. media takes
    exactly one item in the same form the publishing endpoints accept: a stored media library id
    (source_type media_id), a public URL (url), or a reference to bytes you uploaded to Google yourself
    (platform_attachment_id). The photo or video format is derived from the item you supply, so you
    never set Google's own upload fields. Google limits a location to 10 edits per minute, and that
    limit cannot be raised.

    Args:
        id (str):
        body (ApiEndpointsCreateGoogleMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateGoogleMediaRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]:
    """Add media to a Google Business Profile location

     Attaches one photo or video to a location's public profile under the given category. media takes
    exactly one item in the same form the publishing endpoints accept: a stored media library id
    (source_type media_id), a public URL (url), or a reference to bytes you uploaded to Google yourself
    (platform_attachment_id). The photo or video format is derived from the item you supply, so you
    never set Google's own upload fields. Google limits a location to 10 edits per minute, and that
    limit cannot be raised.

    Args:
        id (str):
        body (ApiEndpointsCreateGoogleMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateGoogleMediaRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem | None:
    """Add media to a Google Business Profile location

     Attaches one photo or video to a location's public profile under the given category. media takes
    exactly one item in the same form the publishing endpoints accept: a stored media library id
    (source_type media_id), a public URL (url), or a reference to bytes you uploaded to Google yourself
    (platform_attachment_id). The photo or video format is derived from the item you supply, so you
    never set Google's own upload fields. Google limits a location to 10 edits per minute, and that
    limit cannot be raised.

    Args:
        id (str):
        body (ApiEndpointsCreateGoogleMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleMediaItem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
