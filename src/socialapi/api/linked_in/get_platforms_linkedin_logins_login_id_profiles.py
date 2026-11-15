from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_linked_in_login_profiles_response import ApiEndpointsLinkedInLoginProfilesResponse
from ...types import Response


def _get_kwargs(
    login_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/linkedin/logins/{login_id}/profiles".format(
            login_id=quote(str(login_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsLinkedInLoginProfilesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse]:
    """List the profile and Pages of a LinkedIn login

     Lists the member profile and every company Page a LinkedIn login can connect, with assignment state.
    A Page the member started administering after the last authorization appears without re-
    authenticating. A login authorized with connection_type profile lists the member only, and one
    authorized with connection_type organization lists its Pages only. loginId is the login_id of any
    LinkedIn account connected through that login.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse | None:
    """List the profile and Pages of a LinkedIn login

     Lists the member profile and every company Page a LinkedIn login can connect, with assignment state.
    A Page the member started administering after the last authorization appears without re-
    authenticating. A login authorized with connection_type profile lists the member only, and one
    authorized with connection_type organization lists its Pages only. loginId is the login_id of any
    LinkedIn account connected through that login.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse
    """

    return sync_detailed(
        login_id=login_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse]:
    """List the profile and Pages of a LinkedIn login

     Lists the member profile and every company Page a LinkedIn login can connect, with assignment state.
    A Page the member started administering after the last authorization appears without re-
    authenticating. A login authorized with connection_type profile lists the member only, and one
    authorized with connection_type organization lists its Pages only. loginId is the login_id of any
    LinkedIn account connected through that login.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse | None:
    """List the profile and Pages of a LinkedIn login

     Lists the member profile and every company Page a LinkedIn login can connect, with assignment state.
    A Page the member started administering after the last authorization appears without re-
    authenticating. A login authorized with connection_type profile lists the member only, and one
    authorized with connection_type organization lists its Pages only. loginId is the login_id of any
    LinkedIn account connected through that login.

    Args:
        login_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsLinkedInLoginProfilesResponse
    """

    return (
        await asyncio_detailed(
            login_id=login_id,
            client=client,
        )
    ).parsed
