from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.facebook_login_pages_response import FacebookLoginPagesResponse
from ...types import Response


def _get_kwargs(
    login_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/facebook/logins/{login_id}/pages".format(
            login_id=quote(str(login_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | FacebookLoginPagesResponse | None:
    if response.status_code == 200:
        response_200 = FacebookLoginPagesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | FacebookLoginPagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | FacebookLoginPagesResponse]:
    """List a Facebook login's Pages

     Lists every Page this login can manage, with the brand that holds each. assignable reflects
    ownership only. When facebook_page_selection is true, assigning can still fail on the per-brand Page
    allowance. A brand-restricted key does not see Pages held by brands outside its list.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FacebookLoginPagesResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | FacebookLoginPagesResponse | None:
    """List a Facebook login's Pages

     Lists every Page this login can manage, with the brand that holds each. assignable reflects
    ownership only. When facebook_page_selection is true, assigning can still fail on the per-brand Page
    allowance. A brand-restricted key does not see Pages held by brands outside its list.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FacebookLoginPagesResponse
    """

    return sync_detailed(
        login_id=login_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | FacebookLoginPagesResponse]:
    """List a Facebook login's Pages

     Lists every Page this login can manage, with the brand that holds each. assignable reflects
    ownership only. When facebook_page_selection is true, assigning can still fail on the per-brand Page
    allowance. A brand-restricted key does not see Pages held by brands outside its list.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FacebookLoginPagesResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | FacebookLoginPagesResponse | None:
    """List a Facebook login's Pages

     Lists every Page this login can manage, with the brand that holds each. assignable reflects
    ownership only. When facebook_page_selection is true, assigning can still fail on the per-brand Page
    allowance. A brand-restricted key does not see Pages held by brands outside its list.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FacebookLoginPagesResponse
    """

    return (
        await asyncio_detailed(
            login_id=login_id,
            client=client,
        )
    ).parsed
