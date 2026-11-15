from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_post_response import DeletePostResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    post_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/posts/{post_id}".format(
            post_id=quote(str(post_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeletePostResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeletePostResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DeletePostResponse | ErrorResponse]:
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
) -> Response[DeletePostResponse | ErrorResponse]:
    """Delete or cancel a post

     Deletes a draft/scheduled/failed post locally, or deletes a published post from every platform that
    supports it. Platforms that do not support deletion (or fail) keep their copy live and the post is
    kept rather than removed. Returns a per-platform result.

    Args:
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletePostResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: str,
    *,
    client: AuthenticatedClient,
) -> DeletePostResponse | ErrorResponse | None:
    """Delete or cancel a post

     Deletes a draft/scheduled/failed post locally, or deletes a published post from every platform that
    supports it. Platforms that do not support deletion (or fail) keep their copy live and the post is
    kept rather than removed. Returns a per-platform result.

    Args:
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletePostResponse | ErrorResponse
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeletePostResponse | ErrorResponse]:
    """Delete or cancel a post

     Deletes a draft/scheduled/failed post locally, or deletes a published post from every platform that
    supports it. Platforms that do not support deletion (or fail) keep their copy live and the post is
    kept rather than removed. Returns a per-platform result.

    Args:
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletePostResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    *,
    client: AuthenticatedClient,
) -> DeletePostResponse | ErrorResponse | None:
    """Delete or cancel a post

     Deletes a draft/scheduled/failed post locally, or deletes a published post from every platform that
    supports it. Platforms that do not support deletion (or fail) keep their copy live and the post is
    kept rather than removed. Returns a per-platform result.

    Args:
        post_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletePostResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
        )
    ).parsed
