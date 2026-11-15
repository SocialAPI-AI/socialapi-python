from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.export_status_response import ExportStatusResponse
from ...types import Response


def _get_kwargs(
    export_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/exports/{export_id}".format(
            export_id=quote(str(export_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | ExportStatusResponse | None:
    if response.status_code == 200:
        response_200 = ExportStatusResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | ExportStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    export_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ExportStatusResponse]:
    """Get export status and result

     Returns the current status, progress, result download URL (presigned Excel), and report URL for an
    export job.

    Args:
        export_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExportStatusResponse]
    """

    kwargs = _get_kwargs(
        export_id=export_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    export_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ExportStatusResponse | None:
    """Get export status and result

     Returns the current status, progress, result download URL (presigned Excel), and report URL for an
    export job.

    Args:
        export_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExportStatusResponse
    """

    return sync_detailed(
        export_id=export_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    export_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ExportStatusResponse]:
    """Get export status and result

     Returns the current status, progress, result download URL (presigned Excel), and report URL for an
    export job.

    Args:
        export_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExportStatusResponse]
    """

    kwargs = _get_kwargs(
        export_id=export_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    export_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ExportStatusResponse | None:
    """Get export status and result

     Returns the current status, progress, result download URL (presigned Excel), and report URL for an
    export job.

    Args:
        export_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExportStatusResponse
    """

    return (
        await asyncio_detailed(
            export_id=export_id,
            client=client,
        )
    ).parsed
