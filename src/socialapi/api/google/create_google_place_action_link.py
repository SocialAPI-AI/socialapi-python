from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.gbp_place_action_link_input import GBPPlaceActionLinkInput
from ...models.google_place_action_link_response import GooglePlaceActionLinkResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: GBPPlaceActionLinkInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/google/accounts/{account_id}/place-action-links".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GooglePlaceActionLinkResponse | None:
    if response.status_code == 201:
        response_201 = GooglePlaceActionLinkResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | GooglePlaceActionLinkResponse]:
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
    body: GBPPlaceActionLinkInput,
) -> Response[ErrorResponse | GooglePlaceActionLinkResponse]:
    """Add an action link to a Google Business Profile location

     Adds a booking, reservation or ordering button that opens uri. uri and place_action_type are
    required; place_action_type is one of APPOINTMENT, ONLINE_APPOINTMENT, DINING_RESERVATION,
    FOOD_ORDERING, FOOD_DELIVERY, FOOD_TAKEOUT or SHOP_ONLINE, and GET
    /platforms/google/accounts/{account_id}/place-action-types lists the ones the location can offer. A
    location cannot hold two links with the same uri and type (409). Only one link per type can be
    preferred: is_preferred=true picks the one Google shows first.

    Args:
        account_id (str):
        body (GBPPlaceActionLinkInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GooglePlaceActionLinkResponse]
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
    body: GBPPlaceActionLinkInput,
) -> ErrorResponse | GooglePlaceActionLinkResponse | None:
    """Add an action link to a Google Business Profile location

     Adds a booking, reservation or ordering button that opens uri. uri and place_action_type are
    required; place_action_type is one of APPOINTMENT, ONLINE_APPOINTMENT, DINING_RESERVATION,
    FOOD_ORDERING, FOOD_DELIVERY, FOOD_TAKEOUT or SHOP_ONLINE, and GET
    /platforms/google/accounts/{account_id}/place-action-types lists the ones the location can offer. A
    location cannot hold two links with the same uri and type (409). Only one link per type can be
    preferred: is_preferred=true picks the one Google shows first.

    Args:
        account_id (str):
        body (GBPPlaceActionLinkInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GooglePlaceActionLinkResponse
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
    body: GBPPlaceActionLinkInput,
) -> Response[ErrorResponse | GooglePlaceActionLinkResponse]:
    """Add an action link to a Google Business Profile location

     Adds a booking, reservation or ordering button that opens uri. uri and place_action_type are
    required; place_action_type is one of APPOINTMENT, ONLINE_APPOINTMENT, DINING_RESERVATION,
    FOOD_ORDERING, FOOD_DELIVERY, FOOD_TAKEOUT or SHOP_ONLINE, and GET
    /platforms/google/accounts/{account_id}/place-action-types lists the ones the location can offer. A
    location cannot hold two links with the same uri and type (409). Only one link per type can be
    preferred: is_preferred=true picks the one Google shows first.

    Args:
        account_id (str):
        body (GBPPlaceActionLinkInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GooglePlaceActionLinkResponse]
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
    body: GBPPlaceActionLinkInput,
) -> ErrorResponse | GooglePlaceActionLinkResponse | None:
    """Add an action link to a Google Business Profile location

     Adds a booking, reservation or ordering button that opens uri. uri and place_action_type are
    required; place_action_type is one of APPOINTMENT, ONLINE_APPOINTMENT, DINING_RESERVATION,
    FOOD_ORDERING, FOOD_DELIVERY, FOOD_TAKEOUT or SHOP_ONLINE, and GET
    /platforms/google/accounts/{account_id}/place-action-types lists the ones the location can offer. A
    location cannot hold two links with the same uri and type (409). Only one link per type can be
    preferred: is_preferred=true picks the one Google shows first.

    Args:
        account_id (str):
        body (GBPPlaceActionLinkInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GooglePlaceActionLinkResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
