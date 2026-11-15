from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.google_place_action_types_response import GooglePlaceActionTypesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    language_code: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["language_code"] = language_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/google/accounts/{account_id}/place-action-types".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GooglePlaceActionTypesResponse | None:
    if response.status_code == 200:
        response_200 = GooglePlaceActionTypesResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GooglePlaceActionTypesResponse]:
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
    language_code: str | Unset = UNSET,
) -> Response[ErrorResponse | GooglePlaceActionTypesResponse]:
    """List the action link types a Google Business Profile location can offer

     Returns the place_action_type values available to the location, with a display name, so you only
    offer buttons Google will accept for it.

    Args:
        account_id (str):
        language_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GooglePlaceActionTypesResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        language_code=language_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    language_code: str | Unset = UNSET,
) -> ErrorResponse | GooglePlaceActionTypesResponse | None:
    """List the action link types a Google Business Profile location can offer

     Returns the place_action_type values available to the location, with a display name, so you only
    offer buttons Google will accept for it.

    Args:
        account_id (str):
        language_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GooglePlaceActionTypesResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        language_code=language_code,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    language_code: str | Unset = UNSET,
) -> Response[ErrorResponse | GooglePlaceActionTypesResponse]:
    """List the action link types a Google Business Profile location can offer

     Returns the place_action_type values available to the location, with a display name, so you only
    offer buttons Google will accept for it.

    Args:
        account_id (str):
        language_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GooglePlaceActionTypesResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        language_code=language_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    language_code: str | Unset = UNSET,
) -> ErrorResponse | GooglePlaceActionTypesResponse | None:
    """List the action link types a Google Business Profile location can offer

     Returns the place_action_type values available to the location, with a display name, so you only
    offer buttons Google will accept for it.

    Args:
        account_id (str):
        language_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GooglePlaceActionTypesResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            language_code=language_code,
        )
    ).parsed
