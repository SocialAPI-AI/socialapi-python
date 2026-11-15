from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_google_place_action_link_response import ApiEndpointsGooglePlaceActionLinkResponse
from ...models.social_api_ai_core_api_connectors_base_gbp_place_action_link_input import (
    SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput,
)
from ...types import Response


def _get_kwargs(
    id: str,
    link_id: str,
    *,
    body: SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/platforms/google/accounts/{id}/place-action-links/{link_id}".format(
            id=quote(str(id), safe=""),
            link_id=quote(str(link_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsGooglePlaceActionLinkResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse]:
    """Update an action link on a Google Business Profile location

     Changes the uri, place_action_type or is_preferred of one link. Only the fields you send change.
    Links with is_editable=false belong to a third-party provider and are refused.

    Args:
        id (str):
        link_id (str):
        body (SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        link_id=link_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput,
) -> ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse | None:
    """Update an action link on a Google Business Profile location

     Changes the uri, place_action_type or is_preferred of one link. Only the fields you send change.
    Links with is_editable=false belong to a third-party provider and are refused.

    Args:
        id (str):
        link_id (str):
        body (SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse
    """

    return sync_detailed(
        id=id,
        link_id=link_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse]:
    """Update an action link on a Google Business Profile location

     Changes the uri, place_action_type or is_preferred of one link. Only the fields you send change.
    Links with is_editable=false belong to a third-party provider and are refused.

    Args:
        id (str):
        link_id (str):
        body (SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        link_id=link_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput,
) -> ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse | None:
    """Update an action link on a Google Business Profile location

     Changes the uri, place_action_type or is_preferred of one link. Only the fields you send change.
    Links with is_editable=false belong to a third-party provider and are refused.

    Args:
        id (str):
        link_id (str):
        body (SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLinkInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsGooglePlaceActionLinkResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            link_id=link_id,
            client=client,
            body=body,
        )
    ).parsed
