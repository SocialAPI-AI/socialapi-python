from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    link_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/platforms/google/accounts/{account_id}/place-action-links/{link_id}".format(
            account_id=quote(str(account_id), safe=""),
            link_id=quote(str(link_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | ErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorResponse]:
    """Remove an action link from a Google Business Profile location

     Deletes one link. Links with is_editable=false belong to a third-party provider and are refused.

    Args:
        account_id (str):
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        link_id=link_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorResponse | None:
    """Remove an action link from a Google Business Profile location

     Deletes one link. Links with is_editable=false belong to a third-party provider and are refused.

    Args:
        account_id (str):
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        account_id=account_id,
        link_id=link_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorResponse]:
    """Remove an action link from a Google Business Profile location

     Deletes one link. Links with is_editable=false belong to a third-party provider and are refused.

    Args:
        account_id (str):
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        link_id=link_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorResponse | None:
    """Remove an action link from a Google Business Profile location

     Deletes one link. Links with is_editable=false belong to a third-party provider and are refused.

    Args:
        account_id (str):
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            link_id=link_id,
            client=client,
        )
    ).parsed
