from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_linked_in_profile_request import AssignLinkedInProfileRequest
from ...models.assign_location_response import AssignLocationResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    login_id: str,
    profile_id: str,
    *,
    body: AssignLinkedInProfileRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/linkedin/logins/{login_id}/profiles/{profile_id}/assign".format(
            login_id=quote(str(login_id), safe=""),
            profile_id=quote(str(profile_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AssignLocationResponse | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = AssignLocationResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AssignLocationResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_id: str,
    profile_id: str,
    *,
    client: AuthenticatedClient,
    body: AssignLinkedInProfileRequest,
) -> Response[AssignLocationResponse | ErrorResponse]:
    """Connect a LinkedIn profile or Page from a login

     Connects the member profile or one company Page of a LinkedIn login to the given brand, without re-
    doing OAuth. Each LinkedIn account belongs to one brand. A brand can hold several LinkedIn accounts.

    Args:
        login_id (str):
        profile_id (str):
        body (AssignLinkedInProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignLocationResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
        profile_id=profile_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_id: str,
    profile_id: str,
    *,
    client: AuthenticatedClient,
    body: AssignLinkedInProfileRequest,
) -> AssignLocationResponse | ErrorResponse | None:
    """Connect a LinkedIn profile or Page from a login

     Connects the member profile or one company Page of a LinkedIn login to the given brand, without re-
    doing OAuth. Each LinkedIn account belongs to one brand. A brand can hold several LinkedIn accounts.

    Args:
        login_id (str):
        profile_id (str):
        body (AssignLinkedInProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignLocationResponse | ErrorResponse
    """

    return sync_detailed(
        login_id=login_id,
        profile_id=profile_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    login_id: str,
    profile_id: str,
    *,
    client: AuthenticatedClient,
    body: AssignLinkedInProfileRequest,
) -> Response[AssignLocationResponse | ErrorResponse]:
    """Connect a LinkedIn profile or Page from a login

     Connects the member profile or one company Page of a LinkedIn login to the given brand, without re-
    doing OAuth. Each LinkedIn account belongs to one brand. A brand can hold several LinkedIn accounts.

    Args:
        login_id (str):
        profile_id (str):
        body (AssignLinkedInProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignLocationResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
        profile_id=profile_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_id: str,
    profile_id: str,
    *,
    client: AuthenticatedClient,
    body: AssignLinkedInProfileRequest,
) -> AssignLocationResponse | ErrorResponse | None:
    """Connect a LinkedIn profile or Page from a login

     Connects the member profile or one company Page of a LinkedIn login to the given brand, without re-
    doing OAuth. Each LinkedIn account belongs to one brand. A brand can hold several LinkedIn accounts.

    Args:
        login_id (str):
        profile_id (str):
        body (AssignLinkedInProfileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignLocationResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            login_id=login_id,
            profile_id=profile_id,
            client=client,
            body=body,
        )
    ).parsed
