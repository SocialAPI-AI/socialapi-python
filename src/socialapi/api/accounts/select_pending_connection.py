from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connect_account_response import ConnectAccountResponse
from ...models.error_response import ErrorResponse
from ...models.select_profile_request import SelectProfileRequest
from ...types import Response


def _get_kwargs(
    connection_id: str,
    *,
    body: SelectProfileRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/pending/{connection_id}/select".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ConnectAccountResponse | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = ConnectAccountResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ConnectAccountResponse | ErrorResponse]:
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
    body: SelectProfileRequest,
) -> Response[ConnectAccountResponse | ErrorResponse]:
    """Select the account or Pages to connect from a pending connection

     Promotes a pending connection into a connected account. For Google, LinkedIn and WhatsApp, pass
    platform_account_id to choose exactly one candidate. For Facebook, pass page_ids with the subset of
    candidate Pages to assign to the brand. First selection wins; the pending connection is then
    consumed.

    Args:
        connection_id (str):
        body (SelectProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectAccountResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    body: SelectProfileRequest,
) -> ConnectAccountResponse | ErrorResponse | None:
    """Select the account or Pages to connect from a pending connection

     Promotes a pending connection into a connected account. For Google, LinkedIn and WhatsApp, pass
    platform_account_id to choose exactly one candidate. For Facebook, pass page_ids with the subset of
    candidate Pages to assign to the brand. First selection wins; the pending connection is then
    consumed.

    Args:
        connection_id (str):
        body (SelectProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectAccountResponse | ErrorResponse
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    body: SelectProfileRequest,
) -> Response[ConnectAccountResponse | ErrorResponse]:
    """Select the account or Pages to connect from a pending connection

     Promotes a pending connection into a connected account. For Google, LinkedIn and WhatsApp, pass
    platform_account_id to choose exactly one candidate. For Facebook, pass page_ids with the subset of
    candidate Pages to assign to the brand. First selection wins; the pending connection is then
    consumed.

    Args:
        connection_id (str):
        body (SelectProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectAccountResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    body: SelectProfileRequest,
) -> ConnectAccountResponse | ErrorResponse | None:
    """Select the account or Pages to connect from a pending connection

     Promotes a pending connection into a connected account. For Google, LinkedIn and WhatsApp, pass
    platform_account_id to choose exactly one candidate. For Facebook, pass page_ids with the subset of
    candidate Pages to assign to the brand. First selection wins; the pending connection is then
    consumed.

    Args:
        connection_id (str):
        body (SelectProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectAccountResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            body=body,
        )
    ).parsed
