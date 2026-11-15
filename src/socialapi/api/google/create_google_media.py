from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_google_media_request import CreateGoogleMediaRequest
from ...models.error_response import ErrorResponse
from ...models.google_media_item import GoogleMediaItem
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: CreateGoogleMediaRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/google/accounts/{account_id}/media".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GoogleMediaItem | None:
    if response.status_code == 201:
        response_201 = GoogleMediaItem.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | GoogleMediaItem]:
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
    body: CreateGoogleMediaRequest,
) -> Response[ErrorResponse | GoogleMediaItem]:
    """Add media to a Google Business Profile location

     Attaches one photo or video to a location's public profile under the given category. media takes
    exactly one item in the same form the publishing endpoints accept: a stored media library id
    (source_type media_id), a public URL (url), or a reference to bytes you uploaded to Google yourself
    (platform_attachment_id). The photo or video format is derived from the item you supply, so you
    never set Google's own upload fields. Google limits a location to 10 edits per minute, and that
    limit cannot be raised.

    Args:
        account_id (str):
        body (CreateGoogleMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleMediaItem]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateGoogleMediaRequest,
) -> ErrorResponse | GoogleMediaItem | None:
    """Add media to a Google Business Profile location

     Attaches one photo or video to a location's public profile under the given category. media takes
    exactly one item in the same form the publishing endpoints accept: a stored media library id
    (source_type media_id), a public URL (url), or a reference to bytes you uploaded to Google yourself
    (platform_attachment_id). The photo or video format is derived from the item you supply, so you
    never set Google's own upload fields. Google limits a location to 10 edits per minute, and that
    limit cannot be raised.

    Args:
        account_id (str):
        body (CreateGoogleMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleMediaItem
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateGoogleMediaRequest,
) -> Response[ErrorResponse | GoogleMediaItem]:
    """Add media to a Google Business Profile location

     Attaches one photo or video to a location's public profile under the given category. media takes
    exactly one item in the same form the publishing endpoints accept: a stored media library id
    (source_type media_id), a public URL (url), or a reference to bytes you uploaded to Google yourself
    (platform_attachment_id). The photo or video format is derived from the item you supply, so you
    never set Google's own upload fields. Google limits a location to 10 edits per minute, and that
    limit cannot be raised.

    Args:
        account_id (str):
        body (CreateGoogleMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleMediaItem]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateGoogleMediaRequest,
) -> ErrorResponse | GoogleMediaItem | None:
    """Add media to a Google Business Profile location

     Attaches one photo or video to a location's public profile under the given category. media takes
    exactly one item in the same form the publishing endpoints accept: a stored media library id
    (source_type media_id), a public URL (url), or a reference to bytes you uploaded to Google yourself
    (platform_attachment_id). The photo or video format is derived from the item you supply, so you
    never set Google's own upload fields. Google limits a location to 10 edits per minute, and that
    limit cannot be raised.

    Args:
        account_id (str):
        body (CreateGoogleMediaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleMediaItem
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
