from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_assign_page_request import ApiEndpointsAssignPageRequest
from ...models.api_endpoints_assign_page_response import ApiEndpointsAssignPageResponse
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...types import Response


def _get_kwargs(
    login_id: str,
    page_id: str,
    *,
    body: ApiEndpointsAssignPageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/facebook/logins/{login_id}/pages/{page_id}/assign".format(
            login_id=quote(str(login_id), safe=""),
            page_id=quote(str(page_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse | None:
    if response.status_code == 201:
        response_201 = ApiEndpointsAssignPageResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsAssignPageRequest,
) -> Response[ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse]:
    """Assign a Facebook Page to a brand

     Assigns one Page from this login to the given brand. Each Page belongs to exactly one brand, so a
    Page another of your brands holds moves to the target brand. When facebook_page_selection is true,
    assigning beyond your plan's Facebook Pages per brand returns 403 platform.facebook.page_cap.

    Args:
        login_id (str):
        page_id (str):
        body (ApiEndpointsAssignPageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
        page_id=page_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsAssignPageRequest,
) -> ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse | None:
    """Assign a Facebook Page to a brand

     Assigns one Page from this login to the given brand. Each Page belongs to exactly one brand, so a
    Page another of your brands holds moves to the target brand. When facebook_page_selection is true,
    assigning beyond your plan's Facebook Pages per brand returns 403 platform.facebook.page_cap.

    Args:
        login_id (str):
        page_id (str):
        body (ApiEndpointsAssignPageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse
    """

    return sync_detailed(
        login_id=login_id,
        page_id=page_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    login_id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsAssignPageRequest,
) -> Response[ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse]:
    """Assign a Facebook Page to a brand

     Assigns one Page from this login to the given brand. Each Page belongs to exactly one brand, so a
    Page another of your brands holds moves to the target brand. When facebook_page_selection is true,
    assigning beyond your plan's Facebook Pages per brand returns 403 platform.facebook.page_cap.

    Args:
        login_id (str):
        page_id (str):
        body (ApiEndpointsAssignPageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
        page_id=page_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_id: str,
    page_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsAssignPageRequest,
) -> ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse | None:
    """Assign a Facebook Page to a brand

     Assigns one Page from this login to the given brand. Each Page belongs to exactly one brand, so a
    Page another of your brands holds moves to the target brand. When facebook_page_selection is true,
    assigning beyond your plan's Facebook Pages per brand returns 403 platform.facebook.page_cap.

    Args:
        login_id (str):
        page_id (str):
        body (ApiEndpointsAssignPageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsAssignPageResponse | ApiEndpointsErrorResponse
    """

    return (
        await asyncio_detailed(
            login_id=login_id,
            page_id=page_id,
            client=client,
            body=body,
        )
    ).parsed
