from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    name: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/platforms/whatsapp/accounts/{id}/templates".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ApiEndpointsErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> Response[Any | ApiEndpointsErrorResponse]:
    """Delete a message template

     Deletes a template by name from the WhatsApp Business Account (WABA) associated with this connected
    account. WhatsApp deletes all language variants that share the given name. Templates cannot be
    deleted while they are being used in active campaigns.

    Args:
        id (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> Any | ApiEndpointsErrorResponse | None:
    """Delete a message template

     Deletes a template by name from the WhatsApp Business Account (WABA) associated with this connected
    account. WhatsApp deletes all language variants that share the given name. Templates cannot be
    deleted while they are being used in active campaigns.

    Args:
        id (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> Response[Any | ApiEndpointsErrorResponse]:
    """Delete a message template

     Deletes a template by name from the WhatsApp Business Account (WABA) associated with this connected
    account. WhatsApp deletes all language variants that share the given name. Templates cannot be
    deleted while they are being used in active campaigns.

    Args:
        id (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> Any | ApiEndpointsErrorResponse | None:
    """Delete a message template

     Deletes a template by name from the WhatsApp Business Account (WABA) associated with this connected
    account. WhatsApp deletes all language variants that share the given name. Templates cannot be
    deleted while they are being used in active campaigns.

    Args:
        id (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            name=name,
        )
    ).parsed
