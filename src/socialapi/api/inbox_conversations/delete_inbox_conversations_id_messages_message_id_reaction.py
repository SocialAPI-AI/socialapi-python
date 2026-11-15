from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_success_response import ApiEndpointsSuccessResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    message_id: str,
    *,
    account_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/inbox/conversations/{id}/messages/{message_id}/reaction".format(
            id=quote(str(id), safe=""),
            message_id=quote(str(message_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    message_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Remove a reaction from a message

     Removes the account's emoji reaction from a message.

    Args:
        id (str):
        message_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        message_id=message_id,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    message_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Remove a reaction from a message

     Removes the account's emoji reaction from a message.

    Args:
        id (str):
        message_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return sync_detailed(
        id=id,
        message_id=message_id,
        client=client,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    message_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Remove a reaction from a message

     Removes the account's emoji reaction from a message.

    Args:
        id (str):
        message_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        message_id=message_id,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    message_id: str,
    *,
    client: AuthenticatedClient,
    account_id: str,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Remove a reaction from a message

     Removes the account's emoji reaction from a message.

    Args:
        id (str):
        message_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            message_id=message_id,
            client=client,
            account_id=account_id,
        )
    ).parsed
