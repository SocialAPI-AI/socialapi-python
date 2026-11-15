from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.brand_response import BrandResponse
from ...models.error_response import ErrorResponse
from ...models.update_brand_request import UpdateBrandRequest
from ...types import Response


def _get_kwargs(
    brand_id: str,
    *,
    body: UpdateBrandRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/brands/{brand_id}".format(
            brand_id=quote(str(brand_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> BrandResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = BrandResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[BrandResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    brand_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBrandRequest,
) -> Response[BrandResponse | ErrorResponse]:
    """Update a brand

     Renames a brand.

    Args:
        brand_id (str):
        body (UpdateBrandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        brand_id=brand_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    brand_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBrandRequest,
) -> BrandResponse | ErrorResponse | None:
    """Update a brand

     Renames a brand.

    Args:
        brand_id (str):
        body (UpdateBrandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandResponse | ErrorResponse
    """

    return sync_detailed(
        brand_id=brand_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    brand_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBrandRequest,
) -> Response[BrandResponse | ErrorResponse]:
    """Update a brand

     Renames a brand.

    Args:
        brand_id (str):
        body (UpdateBrandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        brand_id=brand_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    brand_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBrandRequest,
) -> BrandResponse | ErrorResponse | None:
    """Update a brand

     Renames a brand.

    Args:
        brand_id (str):
        body (UpdateBrandRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            brand_id=brand_id,
            client=client,
            body=body,
        )
    ).parsed
