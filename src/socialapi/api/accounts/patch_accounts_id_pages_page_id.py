from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_account_page_response import ApiEndpointsAccountPageResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_update_page_request import ApiEndpointsUpdatePageRequest
from ...types import Response


def _get_kwargs(
    id: str,
    page_id: str,
    *,
    body: ApiEndpointsUpdatePageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/accounts/{id}/pages/{page_id}".format(
            id=quote(str(id), safe=""),
            page_id=quote(str(page_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsAccountPageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsUpdatePageRequest,
) -> Response[ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse]:
    """Update account page

     Update a page's is_default or is_active status.

    Args:
        id (str):
        page_id (str):
        body (ApiEndpointsUpdatePageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        page_id=page_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsUpdatePageRequest,
) -> ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse | None:
    """Update account page

     Update a page's is_default or is_active status.

    Args:
        id (str):
        page_id (str):
        body (ApiEndpointsUpdatePageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        id=id,
        page_id=page_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsUpdatePageRequest,
) -> Response[ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse]:
    """Update account page

     Update a page's is_default or is_active status.

    Args:
        id (str):
        page_id (str):
        body (ApiEndpointsUpdatePageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        page_id=page_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsUpdatePageRequest,
) -> ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse | None:
    """Update account page

     Update a page's is_default or is_active status.

    Args:
        id (str):
        page_id (str):
        body (ApiEndpointsUpdatePageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAccountPageResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            page_id=page_id,
            client=client,
            body=body,
        )
    ).parsed
