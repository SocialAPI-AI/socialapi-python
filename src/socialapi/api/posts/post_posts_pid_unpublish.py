from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_success_response import ApiEndpointsSuccessResponse
from ...models.api_endpoints_unpublish_request import ApiEndpointsUnpublishRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pid: str,
    *,
    body: ApiEndpointsUnpublishRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/posts/{pid}/unpublish".format(
            pid=quote(str(pid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

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
    pid: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsUnpublishRequest | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Unpublish a post

     Unpublishes a published post from a specific account (if account_id provided) or all accounts.

    Args:
        pid (str):
        body (ApiEndpointsUnpublishRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        pid=pid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsUnpublishRequest | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Unpublish a post

     Unpublishes a published post from a specific account (if account_id provided) or all accounts.

    Args:
        pid (str):
        body (ApiEndpointsUnpublishRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return sync_detailed(
        pid=pid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsUnpublishRequest | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Unpublish a post

     Unpublishes a published post from a specific account (if account_id provided) or all accounts.

    Args:
        pid (str):
        body (ApiEndpointsUnpublishRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        pid=pid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pid: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsUnpublishRequest | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Unpublish a post

     Unpublishes a published post from a specific account (if account_id provided) or all accounts.

    Args:
        pid (str):
        body (ApiEndpointsUnpublishRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return (
        await asyncio_detailed(
            pid=pid,
            client=client,
            body=body,
        )
    ).parsed
