from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_whats_app_template_list_response import ApiEndpointsWhatsAppTemplateListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/whatsapp/accounts/{id}/templates".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsWhatsAppTemplateListResponse.from_dict(response.json())

        return response_200

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse]:
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
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse]:
    """List message templates

     Returns all message templates configured on the WhatsApp Business Account (WABA) associated with
    this connected account. Templates include approved, pending, rejected, and paused entries. Use the
    after cursor from paging.cursors to fetch subsequent pages.

    Args:
        id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse | None:
    """List message templates

     Returns all message templates configured on the WhatsApp Business Account (WABA) associated with
    this connected account. Templates include approved, pending, rejected, and paused entries. Use the
    after cursor from paging.cursors to fetch subsequent pages.

    Args:
        id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse]:
    """List message templates

     Returns all message templates configured on the WhatsApp Business Account (WABA) associated with
    this connected account. Templates include approved, pending, rejected, and paused entries. Use the
    after cursor from paging.cursors to fetch subsequent pages.

    Args:
        id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse | None:
    """List message templates

     Returns all message templates configured on the WhatsApp Business Account (WABA) associated with
    this connected account. Templates include approved, pending, rejected, and paused entries. Use the
    after cursor from paging.cursors to fetch subsequent pages.

    Args:
        id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsWhatsAppTemplateListResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
