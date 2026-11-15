from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.inbox_sync_request import InboxSyncRequest
from ...models.inbox_sync_response import InboxSyncResponse
from ...types import Response


def _get_kwargs(
    *,
    body: InboxSyncRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/sync",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | InboxSyncResponse | None:
    if response.status_code == 202:
        response_202 = InboxSyncResponse.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | InboxSyncResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InboxSyncRequest,
) -> Response[ErrorResponse | InboxSyncResponse]:
    """Start an inbox sync

     Refreshes an account's inbox from the platform. Add conversation_id to refresh a single thread
    instead. Returns immediately: poll GET /inbox/sync until state leaves "syncing". A sync already
    running for the same target is returned as-is rather than duplicated.

    Args:
        body (InboxSyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InboxSyncResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InboxSyncRequest,
) -> ErrorResponse | InboxSyncResponse | None:
    """Start an inbox sync

     Refreshes an account's inbox from the platform. Add conversation_id to refresh a single thread
    instead. Returns immediately: poll GET /inbox/sync until state leaves "syncing". A sync already
    running for the same target is returned as-is rather than duplicated.

    Args:
        body (InboxSyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InboxSyncResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InboxSyncRequest,
) -> Response[ErrorResponse | InboxSyncResponse]:
    """Start an inbox sync

     Refreshes an account's inbox from the platform. Add conversation_id to refresh a single thread
    instead. Returns immediately: poll GET /inbox/sync until state leaves "syncing". A sync already
    running for the same target is returned as-is rather than duplicated.

    Args:
        body (InboxSyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InboxSyncResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InboxSyncRequest,
) -> ErrorResponse | InboxSyncResponse | None:
    """Start an inbox sync

     Refreshes an account's inbox from the platform. Add conversation_id to refresh a single thread
    instead. Returns immediately: poll GET /inbox/sync until state leaves "syncing". A sync already
    running for the same target is returned as-is rather than duplicated.

    Args:
        body (InboxSyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InboxSyncResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
