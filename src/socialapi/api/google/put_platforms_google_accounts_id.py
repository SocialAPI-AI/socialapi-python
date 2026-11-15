from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_update_google_location_response import ApiEndpointsUpdateGoogleLocationResponse
from ...models.social_api_ai_core_api_connectors_base_gbp_location_update import (
    SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["validate_only"] = validate_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/platforms/google/accounts/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsUpdateGoogleLocationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse]:
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
    body: SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse]:
    """Update a Google Business Profile location

     Writes the location's public profile: name, description, phone numbers, address, website,
    categories, opening hours, service area, services. Only the fields you send are touched. A field you
    omit is left as it is, and a field you send with an empty value is CLEARED, which is how you remove
    a phone number or a website. Fields Google owns are not writable and are rejected: place_id,
    maps_uri, new_review_uri and the status flags are output-only, and language_code is fixed when the
    location is created. service_items replaces the whole list of services, and Google refuses it on a
    location whose details report can_modify_service_list=false. Google moderates these edits, so a 200
    means the change was accepted for review rather than already live on Search and Maps; read the
    location back to see what is live and check has_pending_edits. Google allows 10 edits per minute per
    Business Profile and that limit cannot be raised. Pass validate_only=true to have Google check the
    change without applying it, which is the only way to test against a real profile since the API has
    no sandbox.

    Args:
        id (str):
        validate_only (bool | Unset):
        body (SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        validate_only=validate_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse | None:
    """Update a Google Business Profile location

     Writes the location's public profile: name, description, phone numbers, address, website,
    categories, opening hours, service area, services. Only the fields you send are touched. A field you
    omit is left as it is, and a field you send with an empty value is CLEARED, which is how you remove
    a phone number or a website. Fields Google owns are not writable and are rejected: place_id,
    maps_uri, new_review_uri and the status flags are output-only, and language_code is fixed when the
    location is created. service_items replaces the whole list of services, and Google refuses it on a
    location whose details report can_modify_service_list=false. Google moderates these edits, so a 200
    means the change was accepted for review rather than already live on Search and Maps; read the
    location back to see what is live and check has_pending_edits. Google allows 10 edits per minute per
    Business Profile and that limit cannot be raised. Pass validate_only=true to have Google check the
    change without applying it, which is the only way to test against a real profile since the API has
    no sandbox.

    Args:
        id (str):
        validate_only (bool | Unset):
        body (SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        validate_only=validate_only,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse]:
    """Update a Google Business Profile location

     Writes the location's public profile: name, description, phone numbers, address, website,
    categories, opening hours, service area, services. Only the fields you send are touched. A field you
    omit is left as it is, and a field you send with an empty value is CLEARED, which is how you remove
    a phone number or a website. Fields Google owns are not writable and are rejected: place_id,
    maps_uri, new_review_uri and the status flags are output-only, and language_code is fixed when the
    location is created. service_items replaces the whole list of services, and Google refuses it on a
    location whose details report can_modify_service_list=false. Google moderates these edits, so a 200
    means the change was accepted for review rather than already live on Search and Maps; read the
    location back to see what is live and check has_pending_edits. Google allows 10 edits per minute per
    Business Profile and that limit cannot be raised. Pass validate_only=true to have Google check the
    change without applying it, which is the only way to test against a real profile since the API has
    no sandbox.

    Args:
        id (str):
        validate_only (bool | Unset):
        body (SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        validate_only=validate_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse | None:
    """Update a Google Business Profile location

     Writes the location's public profile: name, description, phone numbers, address, website,
    categories, opening hours, service area, services. Only the fields you send are touched. A field you
    omit is left as it is, and a field you send with an empty value is CLEARED, which is how you remove
    a phone number or a website. Fields Google owns are not writable and are rejected: place_id,
    maps_uri, new_review_uri and the status flags are output-only, and language_code is fixed when the
    location is created. service_items replaces the whole list of services, and Google refuses it on a
    location whose details report can_modify_service_list=false. Google moderates these edits, so a 200
    means the change was accepted for review rather than already live on Search and Maps; read the
    location back to see what is live and check has_pending_edits. Google allows 10 edits per minute per
    Business Profile and that limit cannot be raised. Pass validate_only=true to have Google check the
    change without applying it, which is the only way to test against a real profile since the API has
    no sandbox.

    Args:
        id (str):
        validate_only (bool | Unset):
        body (SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsUpdateGoogleLocationResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            validate_only=validate_only,
        )
    ).parsed
