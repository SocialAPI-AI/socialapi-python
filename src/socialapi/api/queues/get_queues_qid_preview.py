from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_queue_preview_response import ApiEndpointsQueuePreviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    qid: str,
    *,
    count: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/queues/{qid}/preview".format(
            qid=quote(str(qid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsQueuePreviewResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse]:
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
    count: int | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse]:
    """Preview a Queue's next times

     Lists the next free times of a Queue as RFC 3339 with the Queue's local offset, soonest first. Works
    on a paused Queue. A forecast, not a reservation: send queue_id, never copy a previewed time into
    scheduled_at.

    Args:
        qid (str):
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse]
    """

    kwargs = _get_kwargs(
        qid=qid,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    qid: str,
    *,
    client: AuthenticatedClient,
    count: int | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse | None:
    """Preview a Queue's next times

     Lists the next free times of a Queue as RFC 3339 with the Queue's local offset, soonest first. Works
    on a paused Queue. A forecast, not a reservation: send queue_id, never copy a previewed time into
    scheduled_at.

    Args:
        qid (str):
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse
    """

    return sync_detailed(
        qid=qid,
        client=client,
        count=count,
    ).parsed


async def asyncio_detailed(
    qid: str,
    *,
    client: AuthenticatedClient,
    count: int | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse]:
    """Preview a Queue's next times

     Lists the next free times of a Queue as RFC 3339 with the Queue's local offset, soonest first. Works
    on a paused Queue. A forecast, not a reservation: send queue_id, never copy a previewed time into
    scheduled_at.

    Args:
        qid (str):
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse]
    """

    kwargs = _get_kwargs(
        qid=qid,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    qid: str,
    *,
    client: AuthenticatedClient,
    count: int | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse | None:
    """Preview a Queue's next times

     Lists the next free times of a Queue as RFC 3339 with the Queue's local offset, soonest first. Works
    on a paused Queue. A forecast, not a reservation: send queue_id, never copy a previewed time into
    scheduled_at.

    Args:
        qid (str):
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsQueuePreviewResponse
    """

    return (
        await asyncio_detailed(
            qid=qid,
            client=client,
            count=count,
        )
    ).parsed
