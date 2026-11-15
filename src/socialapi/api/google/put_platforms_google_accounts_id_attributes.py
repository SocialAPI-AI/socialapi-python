from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_google_attributes_response import ApiEndpointsGoogleAttributesResponse
from ...models.api_endpoints_update_google_attributes_request import ApiEndpointsUpdateGoogleAttributesRequest
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ApiEndpointsUpdateGoogleAttributesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/platforms/google/accounts/{id}/attributes".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsGoogleAttributesResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse]:
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
    body: ApiEndpointsUpdateGoogleAttributesRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse]:
    """Update a Google Business Profile location's attributes

     Sets the attributes you list and leaves every other attribute as it is. Set the one value field that
    matches the attribute's value_type: bool_value, enum_value, uri_values or repeated_enum_value. An
    attribute sent with no value field is removed from the location. Attribute ids and accepted values
    come from GET /platforms/google/accounts/{id}/attributes/available and depend on the location's
    category and country. Google moderates profile edits, so a 200 means the change was accepted for
    review rather than already live on Search and Maps. Google allows 10 edits per minute per Business
    Profile.

    Args:
        id (str):
        body (ApiEndpointsUpdateGoogleAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse]
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
    body: ApiEndpointsUpdateGoogleAttributesRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse | None:
    """Update a Google Business Profile location's attributes

     Sets the attributes you list and leaves every other attribute as it is. Set the one value field that
    matches the attribute's value_type: bool_value, enum_value, uri_values or repeated_enum_value. An
    attribute sent with no value field is removed from the location. Attribute ids and accepted values
    come from GET /platforms/google/accounts/{id}/attributes/available and depend on the location's
    category and country. Google moderates profile edits, so a 200 means the change was accepted for
    review rather than already live on Search and Maps. Google allows 10 edits per minute per Business
    Profile.

    Args:
        id (str):
        body (ApiEndpointsUpdateGoogleAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse
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
    body: ApiEndpointsUpdateGoogleAttributesRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse]:
    """Update a Google Business Profile location's attributes

     Sets the attributes you list and leaves every other attribute as it is. Set the one value field that
    matches the attribute's value_type: bool_value, enum_value, uri_values or repeated_enum_value. An
    attribute sent with no value field is removed from the location. Attribute ids and accepted values
    come from GET /platforms/google/accounts/{id}/attributes/available and depend on the location's
    category and country. Google moderates profile edits, so a 200 means the change was accepted for
    review rather than already live on Search and Maps. Google allows 10 edits per minute per Business
    Profile.

    Args:
        id (str):
        body (ApiEndpointsUpdateGoogleAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse]
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
    body: ApiEndpointsUpdateGoogleAttributesRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse | None:
    """Update a Google Business Profile location's attributes

     Sets the attributes you list and leaves every other attribute as it is. Set the one value field that
    matches the attribute's value_type: bool_value, enum_value, uri_values or repeated_enum_value. An
    attribute sent with no value field is removed from the location. Attribute ids and accepted values
    come from GET /platforms/google/accounts/{id}/attributes/available and depend on the location's
    category and country. Google moderates profile edits, so a 200 means the change was accepted for
    review rather than already live on Search and Maps. Google allows 10 edits per minute per Business
    Profile.

    Args:
        id (str):
        body (ApiEndpointsUpdateGoogleAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleAttributesResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
