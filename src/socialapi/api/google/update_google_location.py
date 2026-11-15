from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.gbp_location_update import GBPLocationUpdate
from ...models.update_google_location_response import UpdateGoogleLocationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: GBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["validate_only"] = validate_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/platforms/google/accounts/{account_id}".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | UpdateGoogleLocationResponse | None:
    if response.status_code == 200:
        response_200 = UpdateGoogleLocationResponse.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | UpdateGoogleLocationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: GBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> Response[ErrorResponse | UpdateGoogleLocationResponse]:
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
        account_id (str):
        validate_only (bool | Unset):
        body (GBPLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpdateGoogleLocationResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        validate_only=validate_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: GBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> ErrorResponse | UpdateGoogleLocationResponse | None:
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
        account_id (str):
        validate_only (bool | Unset):
        body (GBPLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpdateGoogleLocationResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        validate_only=validate_only,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: GBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> Response[ErrorResponse | UpdateGoogleLocationResponse]:
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
        account_id (str):
        validate_only (bool | Unset):
        body (GBPLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpdateGoogleLocationResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        validate_only=validate_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: GBPLocationUpdate,
    validate_only: bool | Unset = UNSET,
) -> ErrorResponse | UpdateGoogleLocationResponse | None:
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
        account_id (str):
        validate_only (bool | Unset):
        body (GBPLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpdateGoogleLocationResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            validate_only=validate_only,
        )
    ).parsed
