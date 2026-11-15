from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_delete_post_response import ApiEndpointsDeletePostResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs(
    pid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/posts/{pid}".format(
            pid=quote(str(pid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsDeletePostResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse]:
    """Delete or cancel a post

     Deletes a draft/scheduled/failed post locally, or deletes a published post from every platform that
    supports it. Platforms that do not support deletion (or fail) keep their copy live and the post is
    kept rather than removed. Returns a per-platform result.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        pid=pid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse | None:
    """Delete or cancel a post

     Deletes a draft/scheduled/failed post locally, or deletes a published post from every platform that
    supports it. Platforms that do not support deletion (or fail) keep their copy live and the post is
    kept rather than removed. Returns a per-platform result.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        pid=pid,
        client=client,
    ).parsed


async def asyncio_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse]:
    """Delete or cancel a post

     Deletes a draft/scheduled/failed post locally, or deletes a published post from every platform that
    supports it. Platforms that do not support deletion (or fail) keep their copy live and the post is
    kept rather than removed. Returns a per-platform result.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        pid=pid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pid: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse | None:
    """Delete or cancel a post

     Deletes a draft/scheduled/failed post locally, or deletes a published post from every platform that
    supports it. Platforms that do not support deletion (or fail) keep their copy live and the post is
    kept rather than removed. Returns a per-platform result.

    Args:
        pid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsDeletePostResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            pid=pid,
            client=client,
        )
    ).parsed
