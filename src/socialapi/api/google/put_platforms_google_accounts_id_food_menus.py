from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_google_food_menus_response import ApiEndpointsGoogleFoodMenusResponse
from ...models.social_api_ai_core_api_connectors_base_gbp_food_menus import SocialApiAiCoreApiConnectorsBaseGBPFoodMenus
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SocialApiAiCoreApiConnectorsBaseGBPFoodMenus,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/platforms/google/accounts/{id}/food-menus".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsGoogleFoodMenusResponse.from_dict(response.json())

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
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse]:
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
    body: SocialApiAiCoreApiConnectorsBaseGBPFoodMenus,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse]:
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
        id (str):
        body (SocialApiAiCoreApiConnectorsBaseGBPFoodMenus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse]
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
    body: SocialApiAiCoreApiConnectorsBaseGBPFoodMenus,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse | None:
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
        id (str):
        body (SocialApiAiCoreApiConnectorsBaseGBPFoodMenus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse
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
    body: SocialApiAiCoreApiConnectorsBaseGBPFoodMenus,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse]:
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
        id (str):
        body (SocialApiAiCoreApiConnectorsBaseGBPFoodMenus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse]
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
    body: SocialApiAiCoreApiConnectorsBaseGBPFoodMenus,
) -> ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse | None:
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
        id (str):
        body (SocialApiAiCoreApiConnectorsBaseGBPFoodMenus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGoogleFoodMenusResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
