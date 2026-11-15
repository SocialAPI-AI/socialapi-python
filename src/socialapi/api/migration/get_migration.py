from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.migration_response import MigrationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider: str,
    *,
    refresh: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["refresh"] = refresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/migrations/{provider}".format(
            provider=quote(str(provider), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | MigrationResponse | None:
    if response.status_code == 200:
        response_200 = MigrationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | MigrationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = UNSET,
) -> Response[ErrorResponse | MigrationResponse]:
    """Get a migration

     Returns your migration from a provider: the authorisation text to accept before starting, and once
    started, your accounts, the Brands and plan they need, and progress. If the provider cannot be read,
    the response is still 200 with `assessment` null and `assessment_error` set. The assessment can be
    up to 5 minutes old unless `refresh` is true. Dashboard sessions only; API keys get 403.

    Args:
        provider (str):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MigrationResponse]
    """

    kwargs = _get_kwargs(
        provider=provider,
        refresh=refresh,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: str,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = UNSET,
) -> ErrorResponse | MigrationResponse | None:
    """Get a migration

     Returns your migration from a provider: the authorisation text to accept before starting, and once
    started, your accounts, the Brands and plan they need, and progress. If the provider cannot be read,
    the response is still 200 with `assessment` null and `assessment_error` set. The assessment can be
    up to 5 minutes old unless `refresh` is true. Dashboard sessions only; API keys get 403.

    Args:
        provider (str):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MigrationResponse
    """

    return sync_detailed(
        provider=provider,
        client=client,
        refresh=refresh,
    ).parsed


async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = UNSET,
) -> Response[ErrorResponse | MigrationResponse]:
    """Get a migration

     Returns your migration from a provider: the authorisation text to accept before starting, and once
    started, your accounts, the Brands and plan they need, and progress. If the provider cannot be read,
    the response is still 200 with `assessment` null and `assessment_error` set. The assessment can be
    up to 5 minutes old unless `refresh` is true. Dashboard sessions only; API keys get 403.

    Args:
        provider (str):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MigrationResponse]
    """

    kwargs = _get_kwargs(
        provider=provider,
        refresh=refresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = UNSET,
) -> ErrorResponse | MigrationResponse | None:
    """Get a migration

     Returns your migration from a provider: the authorisation text to accept before starting, and once
    started, your accounts, the Brands and plan they need, and progress. If the provider cannot be read,
    the response is still 200 with `assessment` null and `assessment_error` set. The assessment can be
    up to 5 minutes old unless `refresh` is true. Dashboard sessions only; API keys get 403.

    Args:
        provider (str):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MigrationResponse
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
            refresh=refresh,
        )
    ).parsed
