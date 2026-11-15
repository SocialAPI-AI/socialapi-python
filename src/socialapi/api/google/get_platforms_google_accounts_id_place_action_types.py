from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_google_place_action_types_response import ApiEndpointsGooglePlaceActionTypesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    language_code: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["language_code"] = language_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/accounts/{id}/place-action-types".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsGooglePlaceActionTypesResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse]:
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
    language_code: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse]:
    """List the action link types a Google Business Profile location can offer

     Returns the place_action_type values available to the location, with a display name, so you only
    offer buttons Google will accept for it.

    Args:
        id (str):
        language_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        language_code=language_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    language_code: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse | None:
    """List the action link types a Google Business Profile location can offer

     Returns the place_action_type values available to the location, with a display name, so you only
    offer buttons Google will accept for it.

    Args:
        id (str):
        language_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        language_code=language_code,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    language_code: str | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse]:
    """List the action link types a Google Business Profile location can offer

     Returns the place_action_type values available to the location, with a display name, so you only
    offer buttons Google will accept for it.

    Args:
        id (str):
        language_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        language_code=language_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    language_code: str | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse | None:
    """List the action link types a Google Business Profile location can offer

     Returns the place_action_type values available to the location, with a display name, so you only
    offer buttons Google will accept for it.

    Args:
        id (str):
        language_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionTypesResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            language_code=language_code,
        )
    ).parsed
