from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_invite_request import CreateInviteRequest
from ...models.error_response import ErrorResponse
from ...models.invite_response import InviteResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateInviteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/invites",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | InviteResponse | None:
    if response.status_code == 201:
        response_201 = InviteResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[ErrorResponse | InviteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInviteRequest,
) -> Response[ErrorResponse | InviteResponse]:
    """Create an invite link

     Creates a single-use invite link for an external user to connect a social account to a brand.
    The brand must not already have a connected account for the specified platform, and
    no active (unused, unexpired) invite may exist for the same brand+platform combination.

    Args:
        body (CreateInviteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InviteResponse]
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
    body: CreateInviteRequest,
) -> ErrorResponse | InviteResponse | None:
    """Create an invite link

     Creates a single-use invite link for an external user to connect a social account to a brand.
    The brand must not already have a connected account for the specified platform, and
    no active (unused, unexpired) invite may exist for the same brand+platform combination.

    Args:
        body (CreateInviteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InviteResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInviteRequest,
) -> Response[ErrorResponse | InviteResponse]:
    """Create an invite link

     Creates a single-use invite link for an external user to connect a social account to a brand.
    The brand must not already have a connected account for the specified platform, and
    no active (unused, unexpired) invite may exist for the same brand+platform combination.

    Args:
        body (CreateInviteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InviteResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateInviteRequest,
) -> ErrorResponse | InviteResponse | None:
    """Create an invite link

     Creates a single-use invite link for an external user to connect a social account to a brand.
    The brand must not already have a connected account for the specified platform, and
    no active (unused, unexpired) invite may exist for the same brand+platform combination.

    Args:
        body (CreateInviteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InviteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
