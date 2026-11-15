from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_delete_queue_response import ApiEndpointsDeleteQueueResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs(
    qid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/queues/{qid}".format(
            qid=quote(str(qid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsDeleteQueueResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    qid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse]:
    """Delete a Queue

     Deletes a Queue. Its posts keep their scheduled times and are no longer queued; released_count is
    how many there were. If it was the default, the Brand's oldest remaining Queue becomes the default.

    Args:
        qid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        qid=qid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    qid: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse | None:
    """Delete a Queue

     Deletes a Queue. Its posts keep their scheduled times and are no longer queued; released_count is
    how many there were. If it was the default, the Brand's oldest remaining Queue becomes the default.

    Args:
        qid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        qid=qid,
        client=client,
    ).parsed


async def asyncio_detailed(
    qid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse]:
    """Delete a Queue

     Deletes a Queue. Its posts keep their scheduled times and are no longer queued; released_count is
    how many there were. If it was the default, the Brand's oldest remaining Queue becomes the default.

    Args:
        qid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        qid=qid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    qid: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse | None:
    """Delete a Queue

     Deletes a Queue. Its posts keep their scheduled times and are no longer queued; released_count is
    how many there were. If it was the default, the Brand's oldest remaining Queue becomes the default.

    Args:
        qid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsDeleteQueueResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            qid=qid,
            client=client,
        )
    ).parsed
