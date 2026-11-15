from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import File, Response


def _get_kwargs(
    media_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/inbox/media/{media_id}".format(
            media_id=quote(str(media_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> ErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.content)

        return response_404

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.content)

        return response_410

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.content)

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | File]:
    """Get inbox media

     Returns the bytes of an inbox attachment: one received on WhatsApp or Telegram, or one sent with a
    media_id. 503 means retry shortly, not gone.

    Args:
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        media_id=media_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | File | None:
    """Get inbox media

     Returns the bytes of an inbox attachment: one received on WhatsApp or Telegram, or one sent with a
    media_id. 503 means retry shortly, not gone.

    Args:
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return sync_detailed(
        media_id=media_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | File]:
    """Get inbox media

     Returns the bytes of an inbox attachment: one received on WhatsApp or Telegram, or one sent with a
    media_id. 503 means retry shortly, not gone.

    Args:
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        media_id=media_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | File | None:
    """Get inbox media

     Returns the bytes of an inbox attachment: one received on WhatsApp or Telegram, or one sent with a
    media_id. 503 means retry shortly, not gone.

    Args:
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return (
        await asyncio_detailed(
            media_id=media_id,
            client=client,
        )
    ).parsed
