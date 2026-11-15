from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_queue_params import UpdateQueueParams
from ...models.update_queue_response import UpdateQueueResponse
from ...types import Response


def _get_kwargs(
    queue_id: str,
    *,
    body: UpdateQueueParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/queues/{queue_id}".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | UpdateQueueResponse | None:
    if response.status_code == 200:
        response_200 = UpdateQueueResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | UpdateQueueResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateQueueParams,
) -> Response[ErrorResponse | UpdateQueueResponse]:
    """Update a Queue

     Updates the fields you send and keeps the rest. slots replaces the whole list. Set active to false
    to pause the Queue: posts already in it keep their times, and no new post can join it. is_default
    can only be set to true, which makes this Queue the Brand's default; to change the default, set
    another Queue's is_default to true. Posts already queued keep their times unless you send
    reshuffle_existing: true, which moves them onto the new slots in their current order and returns
    reshuffled_count.

    Args:
        queue_id (str):
        body (UpdateQueueParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpdateQueueResponse]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateQueueParams,
) -> ErrorResponse | UpdateQueueResponse | None:
    """Update a Queue

     Updates the fields you send and keeps the rest. slots replaces the whole list. Set active to false
    to pause the Queue: posts already in it keep their times, and no new post can join it. is_default
    can only be set to true, which makes this Queue the Brand's default; to change the default, set
    another Queue's is_default to true. Posts already queued keep their times unless you send
    reshuffle_existing: true, which moves them onto the new slots in their current order and returns
    reshuffled_count.

    Args:
        queue_id (str):
        body (UpdateQueueParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpdateQueueResponse
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateQueueParams,
) -> Response[ErrorResponse | UpdateQueueResponse]:
    """Update a Queue

     Updates the fields you send and keeps the rest. slots replaces the whole list. Set active to false
    to pause the Queue: posts already in it keep their times, and no new post can join it. is_default
    can only be set to true, which makes this Queue the Brand's default; to change the default, set
    another Queue's is_default to true. Posts already queued keep their times unless you send
    reshuffle_existing: true, which moves them onto the new slots in their current order and returns
    reshuffled_count.

    Args:
        queue_id (str):
        body (UpdateQueueParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpdateQueueResponse]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateQueueParams,
) -> ErrorResponse | UpdateQueueResponse | None:
    """Update a Queue

     Updates the fields you send and keeps the rest. slots replaces the whole list. Set active to false
    to pause the Queue: posts already in it keep their times, and no new post can join it. is_default
    can only be set to true, which makes this Queue the Brand's default; to change the default, set
    another Queue's is_default to true. Posts already queued keep their times unless you send
    reshuffle_existing: true, which moves them onto the new slots in their current order and returns
    reshuffled_count.

    Args:
        queue_id (str):
        body (UpdateQueueParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpdateQueueResponse
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            body=body,
        )
    ).parsed
