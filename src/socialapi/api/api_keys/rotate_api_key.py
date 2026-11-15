from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_key_response import CreateKeyResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    key_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/keys/{key_id}/rotate".format(
            key_id=quote(str(key_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CreateKeyResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CreateKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CreateKeyResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CreateKeyResponse | ErrorResponse]:
    """Rotate API key

     Issues a new secret for an existing key, keeping its id, name, scopes, and brand restrictions. The
    old key value stops working immediately. The new raw key is shown once. Requires a full-access key
    or the dashboard.

    Args:
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateKeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> CreateKeyResponse | ErrorResponse | None:
    """Rotate API key

     Issues a new secret for an existing key, keeping its id, name, scopes, and brand restrictions. The
    old key value stops working immediately. The new raw key is shown once. Requires a full-access key
    or the dashboard.

    Args:
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateKeyResponse | ErrorResponse
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CreateKeyResponse | ErrorResponse]:
    """Rotate API key

     Issues a new secret for an existing key, keeping its id, name, scopes, and brand restrictions. The
    old key value stops working immediately. The new raw key is shown once. Requires a full-access key
    or the dashboard.

    Args:
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateKeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> CreateKeyResponse | ErrorResponse | None:
    """Rotate API key

     Issues a new secret for an existing key, keeping its id, name, scopes, and brand restrictions. The
    old key value stops working immediately. The new raw key is shown once. Requires a full-access key
    or the dashboard.

    Args:
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateKeyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
        )
    ).parsed
