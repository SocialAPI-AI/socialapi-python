from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pending_connection_detail_response import PendingConnectionDetailResponse
from ...types import Response


def _get_kwargs(
    connection_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/pending/{connection_id}".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | PendingConnectionDetailResponse | None:
    if response.status_code == 200:
        response_200 = PendingConnectionDetailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | PendingConnectionDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | PendingConnectionDetailResponse]:
    """Get a pending account selection

     Returns the candidates of a pending connection: the Google Business Profiles of a Google login that
    manages more than one, the LinkedIn member profile and company Pages of a LinkedIn authorization
    that offers more than one, or the phone numbers of a WhatsApp Business account that holds several.
    Choose one with the select endpoint.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PendingConnectionDetailResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | PendingConnectionDetailResponse | None:
    """Get a pending account selection

     Returns the candidates of a pending connection: the Google Business Profiles of a Google login that
    manages more than one, the LinkedIn member profile and company Pages of a LinkedIn authorization
    that offers more than one, or the phone numbers of a WhatsApp Business account that holds several.
    Choose one with the select endpoint.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PendingConnectionDetailResponse
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | PendingConnectionDetailResponse]:
    """Get a pending account selection

     Returns the candidates of a pending connection: the Google Business Profiles of a Google login that
    manages more than one, the LinkedIn member profile and company Pages of a LinkedIn authorization
    that offers more than one, or the phone numbers of a WhatsApp Business account that holds several.
    Choose one with the select endpoint.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PendingConnectionDetailResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | PendingConnectionDetailResponse | None:
    """Get a pending account selection

     Returns the candidates of a pending connection: the Google Business Profiles of a Google login that
    manages more than one, the LinkedIn member profile and company Pages of a LinkedIn authorization
    that offers more than one, or the phone numbers of a WhatsApp Business account that holds several.
    Choose one with the select endpoint.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PendingConnectionDetailResponse
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
        )
    ).parsed
