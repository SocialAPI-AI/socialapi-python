from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.google_attributes_response import GoogleAttributesResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/accounts/{account_id}/attributes".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GoogleAttributesResponse | None:
    if response.status_code == 200:
        response_200 = GoogleAttributesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

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
) -> Response[ErrorResponse | GoogleAttributesResponse]:
    """List a Google Business Profile location's attributes

     Returns the attributes set on a location, such as outdoor seating, accepted payment methods or a
    wheelchair accessible entrance. value_type says which value field is filled: bool_value for BOOL,
    enum_value for ENUM, uri_values for URL, repeated_enum_value for REPEATED_ENUM.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleAttributesResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | GoogleAttributesResponse | None:
    """List a Google Business Profile location's attributes

     Returns the attributes set on a location, such as outdoor seating, accepted payment methods or a
    wheelchair accessible entrance. value_type says which value field is filled: bool_value for BOOL,
    enum_value for ENUM, uri_values for URL, repeated_enum_value for REPEATED_ENUM.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleAttributesResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | GoogleAttributesResponse]:
    """List a Google Business Profile location's attributes

     Returns the attributes set on a location, such as outdoor seating, accepted payment methods or a
    wheelchair accessible entrance. value_type says which value field is filled: bool_value for BOOL,
    enum_value for ENUM, uri_values for URL, repeated_enum_value for REPEATED_ENUM.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleAttributesResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | GoogleAttributesResponse | None:
    """List a Google Business Profile location's attributes

     Returns the attributes set on a location, such as outdoor seating, accepted payment methods or a
    wheelchair accessible entrance. value_type says which value field is filled: bool_value for BOOL,
    enum_value for ENUM, uri_values for URL, repeated_enum_value for REPEATED_ENUM.

    Args:
        account_id (str):

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
        )
    ).parsed
