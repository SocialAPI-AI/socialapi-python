from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.gbp_food_menus import GBPFoodMenus
from ...models.google_food_menus_response import GoogleFoodMenusResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: GBPFoodMenus,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/platforms/google/accounts/{account_id}/food-menus".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | GoogleFoodMenusResponse | None:
    if response.status_code == 200:
        response_200 = GoogleFoodMenusResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GoogleFoodMenusResponse]:
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
    body: GBPFoodMenus,
) -> Response[ErrorResponse | GoogleFoodMenusResponse]:
    """Replace a Google Business Profile location's food menus

     Replaces every menu on the location with the menus you send, so send the full list each time. An
    empty menus list removes all menus. Every menu, section, dish and option needs at least one label
    with a display_name (up to 140 characters, description up to 1000), every menu needs a section,
    every section needs a dish, and every dish needs a price. Values such as cuisines, allergen,
    dietary_restriction and preparation_methods take Google's enum names, for example ITALIAN, PEANUT,
    VEGAN or GRILLED. media_keys reference photos already on the location's profile. Only locations
    whose details report can_have_food_menus=true support menus, so check it first: Google refuses menus
    on any other location.

    Args:
        account_id (str):
        body (GBPFoodMenus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleFoodMenusResponse]
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
    body: GBPFoodMenus,
) -> ErrorResponse | GoogleFoodMenusResponse | None:
    """Replace a Google Business Profile location's food menus

     Replaces every menu on the location with the menus you send, so send the full list each time. An
    empty menus list removes all menus. Every menu, section, dish and option needs at least one label
    with a display_name (up to 140 characters, description up to 1000), every menu needs a section,
    every section needs a dish, and every dish needs a price. Values such as cuisines, allergen,
    dietary_restriction and preparation_methods take Google's enum names, for example ITALIAN, PEANUT,
    VEGAN or GRILLED. media_keys reference photos already on the location's profile. Only locations
    whose details report can_have_food_menus=true support menus, so check it first: Google refuses menus
    on any other location.

    Args:
        account_id (str):
        body (GBPFoodMenus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleFoodMenusResponse
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
    body: GBPFoodMenus,
) -> Response[ErrorResponse | GoogleFoodMenusResponse]:
    """Replace a Google Business Profile location's food menus

     Replaces every menu on the location with the menus you send, so send the full list each time. An
    empty menus list removes all menus. Every menu, section, dish and option needs at least one label
    with a display_name (up to 140 characters, description up to 1000), every menu needs a section,
    every section needs a dish, and every dish needs a price. Values such as cuisines, allergen,
    dietary_restriction and preparation_methods take Google's enum names, for example ITALIAN, PEANUT,
    VEGAN or GRILLED. media_keys reference photos already on the location's profile. Only locations
    whose details report can_have_food_menus=true support menus, so check it first: Google refuses menus
    on any other location.

    Args:
        account_id (str):
        body (GBPFoodMenus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GoogleFoodMenusResponse]
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
    body: GBPFoodMenus,
) -> ErrorResponse | GoogleFoodMenusResponse | None:
    """Replace a Google Business Profile location's food menus

     Replaces every menu on the location with the menus you send, so send the full list each time. An
    empty menus list removes all menus. Every menu, section, dish and option needs at least one label
    with a display_name (up to 140 characters, description up to 1000), every menu needs a section,
    every section needs a dish, and every dish needs a price. Values such as cuisines, allergen,
    dietary_restriction and preparation_methods take Google's enum names, for example ITALIAN, PEANUT,
    VEGAN or GRILLED. media_keys reference photos already on the location's profile. Only locations
    whose details report can_have_food_menus=true support menus, so check it first: Google refuses menus
    on any other location.

    Args:
        account_id (str):
        body (GBPFoodMenus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GoogleFoodMenusResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
