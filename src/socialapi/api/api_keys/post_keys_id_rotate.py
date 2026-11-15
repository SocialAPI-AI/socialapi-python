from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_create_key_response import ApiEndpointsCreateKeyResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/keys/{id}/rotate".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsCreateKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]:
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
) -> Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]:
    """Rotate API key

     Issues a new secret for an existing key, keeping its id, name, scopes, and brand restrictions. The
    old key value stops working immediately. The new raw key is shown once. Requires a full-access key
    or the dashboard.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse | None:
    """Rotate API key

     Issues a new secret for an existing key, keeping its id, name, scopes, and brand restrictions. The
    old key value stops working immediately. The new raw key is shown once. Requires a full-access key
    or the dashboard.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]:
    """Rotate API key

     Issues a new secret for an existing key, keeping its id, name, scopes, and brand restrictions. The
    old key value stops working immediately. The new raw key is shown once. Requires a full-access key
    or the dashboard.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse | None:
    """Rotate API key

     Issues a new secret for an existing key, keeping its id, name, scopes, and brand restrictions. The
    old key value stops working immediately. The new raw key is shown once. Requires a full-access key
    or the dashboard.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsCreateKeyResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
