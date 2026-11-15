from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.google_attributes_response import GoogleAttributesResponse
from ...models.update_google_attributes_request import UpdateGoogleAttributesRequest
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: UpdateGoogleAttributesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/platforms/google/accounts/{account_id}/attributes".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GoogleAttributesResponse | None:
    if response.status_code == 200:
        response_200 = GoogleAttributesResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GoogleAttributesResponse]:
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
    body: UpdateGoogleAttributesRequest,
) -> Response[ErrorResponse | GoogleAttributesResponse]:
    """Update a Google Business Profile location's attributes

     Sets the attributes you list and leaves every other attribute as it is. Set the one value field that
    matches the attribute's value_type: bool_value, enum_value, uri_values or repeated_enum_value. An
    attribute sent with no value field is removed from the location. Attribute ids and accepted values
    come from GET /platforms/google/accounts/{account_id}/attributes/available and depend on the
    location's category and country. Google moderates profile edits, so a 200 means the change was
    accepted for review rather than already live on Search and Maps. Google allows 10 edits per minute
    per Business Profile.

    Args:
        account_id (str):
        body (UpdateGoogleAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleAttributesResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateGoogleAttributesRequest,
) -> ErrorResponse | GoogleAttributesResponse | None:
    """Update a Google Business Profile location's attributes

     Sets the attributes you list and leaves every other attribute as it is. Set the one value field that
    matches the attribute's value_type: bool_value, enum_value, uri_values or repeated_enum_value. An
    attribute sent with no value field is removed from the location. Attribute ids and accepted values
    come from GET /platforms/google/accounts/{account_id}/attributes/available and depend on the
    location's category and country. Google moderates profile edits, so a 200 means the change was
    accepted for review rather than already live on Search and Maps. Google allows 10 edits per minute
    per Business Profile.

    Args:
        account_id (str):
        body (UpdateGoogleAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleAttributesResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateGoogleAttributesRequest,
) -> Response[ErrorResponse | GoogleAttributesResponse]:
    """Update a Google Business Profile location's attributes

     Sets the attributes you list and leaves every other attribute as it is. Set the one value field that
    matches the attribute's value_type: bool_value, enum_value, uri_values or repeated_enum_value. An
    attribute sent with no value field is removed from the location. Attribute ids and accepted values
    come from GET /platforms/google/accounts/{account_id}/attributes/available and depend on the
    location's category and country. Google moderates profile edits, so a 200 means the change was
    accepted for review rather than already live on Search and Maps. Google allows 10 edits per minute
    per Business Profile.

    Args:
        account_id (str):
        body (UpdateGoogleAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleAttributesResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateGoogleAttributesRequest,
) -> ErrorResponse | GoogleAttributesResponse | None:
    """Update a Google Business Profile location's attributes

     Sets the attributes you list and leaves every other attribute as it is. Set the one value field that
    matches the attribute's value_type: bool_value, enum_value, uri_values or repeated_enum_value. An
    attribute sent with no value field is removed from the location. Attribute ids and accepted values
    come from GET /platforms/google/accounts/{account_id}/attributes/available and depend on the
    location's category and country. Google moderates profile edits, so a 200 means the change was
    accepted for review rather than already live on Search and Maps. Google allows 10 edits per minute
    per Business Profile.

    Args:
        account_id (str):
        body (UpdateGoogleAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleAttributesResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
