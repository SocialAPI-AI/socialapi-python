from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_google_login_locations_response import ApiEndpointsGoogleLoginLocationsResponse
from ...types import Response


def _get_kwargs(
    login_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/logins/{login_id}/locations".format(
            login_id=quote(str(login_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsGoogleLoginLocationsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse]:
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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse]:
    """List a Google login's Business Profile locations

     Lists every Business Profile location this login can manage, live from Google, merged with
    assignment state. Locations added in Google Business Profile after the last authorization appear
    here without re-authenticating. assignable reflects ownership only. login_email identifies the
    Google account itself, and may be empty on older connections.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse]
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
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse | None:
    """List a Google login's Business Profile locations

     Lists every Business Profile location this login can manage, live from Google, merged with
    assignment state. Locations added in Google Business Profile after the last authorization appear
    here without re-authenticating. assignable reflects ownership only. login_email identifies the
    Google account itself, and may be empty on older connections.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse
    """

    return sync_detailed(
        login_id=login_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse]:
    """List a Google login's Business Profile locations

     Lists every Business Profile location this login can manage, live from Google, merged with
    assignment state. Locations added in Google Business Profile after the last authorization appear
    here without re-authenticating. assignable reflects ownership only. login_email identifies the
    Google account itself, and may be empty on older connections.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse]
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
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse | None:
    """List a Google login's Business Profile locations

     Lists every Business Profile location this login can manage, live from Google, merged with
    assignment state. Locations added in Google Business Profile after the last authorization appear
    here without re-authenticating. assignable reflects ownership only. login_email identifies the
    Google account itself, and may be empty on older connections.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleLoginLocationsResponse
    """

    return (
        await asyncio_detailed(
            login_id=login_id,
            client=client,
        )
    ).parsed
