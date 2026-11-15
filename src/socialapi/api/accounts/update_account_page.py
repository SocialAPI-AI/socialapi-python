from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_page_response import AccountPageResponse
from ...models.error_response import ErrorResponse
from ...models.update_page_request import UpdatePageRequest
from ...types import Response


def _get_kwargs(
    account_id: str,
    page_id: str,
    *,
    body: UpdatePageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/accounts/{account_id}/pages/{page_id}".format(
            account_id=quote(str(account_id), safe=""),
            page_id=quote(str(page_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AccountPageResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AccountPageResponse.from_dict(response.json())

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
) -> Response[AccountPageResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePageRequest,
) -> Response[AccountPageResponse | ErrorResponse]:
    """Update account page

     Update a page's is_default or is_active status.

    Args:
        account_id (str):
        page_id (str):
        body (UpdatePageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountPageResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        page_id=page_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePageRequest,
) -> AccountPageResponse | ErrorResponse | None:
    """Update account page

     Update a page's is_default or is_active status.

    Args:
        account_id (str):
        page_id (str):
        body (UpdatePageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountPageResponse | ErrorResponse
    """

    return sync_detailed(
        account_id=account_id,
        page_id=page_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePageRequest,
) -> Response[AccountPageResponse | ErrorResponse]:
    """Update account page

     Update a page's is_default or is_active status.

    Args:
        account_id (str):
        page_id (str):
        body (UpdatePageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountPageResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        page_id=page_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePageRequest,
) -> AccountPageResponse | ErrorResponse | None:
    """Update account page

     Update a page's is_default or is_active status.

    Args:
        account_id (str):
        page_id (str):
        body (UpdatePageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountPageResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            page_id=page_id,
            client=client,
            body=body,
        )
    ).parsed
