from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_media_upload_info_response import ApiEndpointsMediaUploadInfoResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    media_type: str,
    filename: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["media_type"] = media_type

    params["filename"] = filename

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/media/upload-url",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsMediaUploadInfoResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 413:
        response_413 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    media_type: str,
    filename: str,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse]:
    """Get a presigned media upload URL

     Returns a presigned PUT URL for client-side media upload. Upload the file directly
    via HTTP PUT to the returned URL, then call POST /v1/media/:id/verify to confirm.

    Args:
        media_type (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse]
    """

    kwargs = _get_kwargs(
        media_type=media_type,
        filename=filename,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    media_type: str,
    filename: str,
) -> ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse | None:
    """Get a presigned media upload URL

     Returns a presigned PUT URL for client-side media upload. Upload the file directly
    via HTTP PUT to the returned URL, then call POST /v1/media/:id/verify to confirm.

    Args:
        media_type (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse
    """

    return sync_detailed(
        client=client,
        media_type=media_type,
        filename=filename,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    media_type: str,
    filename: str,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse]:
    """Get a presigned media upload URL

     Returns a presigned PUT URL for client-side media upload. Upload the file directly
    via HTTP PUT to the returned URL, then call POST /v1/media/:id/verify to confirm.

    Args:
        media_type (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse]
    """

    kwargs = _get_kwargs(
        media_type=media_type,
        filename=filename,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    media_type: str,
    filename: str,
) -> ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse | None:
    """Get a presigned media upload URL

     Returns a presigned PUT URL for client-side media upload. Upload the file directly
    via HTTP PUT to the returned URL, then call POST /v1/media/:id/verify to confirm.

    Args:
        media_type (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsMediaUploadInfoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            media_type=media_type,
            filename=filename,
        )
    ).parsed
