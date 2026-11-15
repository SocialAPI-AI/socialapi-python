from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_create_export_request import ApiEndpointsCreateExportRequest
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_export_accepted_response import ApiEndpointsExportAcceptedResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ApiEndpointsCreateExportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/{id}/export".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse | None:
    if response.status_code == 202:
        response_202 = ApiEndpointsExportAcceptedResponse.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse]:
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
    body: ApiEndpointsCreateExportRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse]:
    """Create analytics export

     Enqueue an async analytics export job for a connected account. Subject to plan limits (exports per
    month, cooldown hours, concurrent export cap). For some TikTok accounts, include_transcript and
    include_vision are refused with 400 account.export_enrichment_not_supported; export again without
    them.

    Args:
        id (str):
        body (ApiEndpointsCreateExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateExportRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse | None:
    """Create analytics export

     Enqueue an async analytics export job for a connected account. Subject to plan limits (exports per
    month, cooldown hours, concurrent export cap). For some TikTok accounts, include_transcript and
    include_vision are refused with 400 account.export_enrichment_not_supported; export again without
    them.

    Args:
        id (str):
        body (ApiEndpointsCreateExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateExportRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse]:
    """Create analytics export

     Enqueue an async analytics export job for a connected account. Subject to plan limits (exports per
    month, cooldown hours, concurrent export cap). For some TikTok accounts, include_transcript and
    include_vision are refused with 400 account.export_enrichment_not_supported; export again without
    them.

    Args:
        id (str):
        body (ApiEndpointsCreateExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsCreateExportRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse | None:
    """Create analytics export

     Enqueue an async analytics export job for a connected account. Subject to plan limits (exports per
    month, cooldown hours, concurrent export cap). For some TikTok accounts, include_transcript and
    include_vision are refused with 400 account.export_enrichment_not_supported; export again without
    them.

    Args:
        id (str):
        body (ApiEndpointsCreateExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsExportAcceptedResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
