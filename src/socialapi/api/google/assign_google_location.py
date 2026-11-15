from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_location_request import AssignLocationRequest
from ...models.assign_location_response import AssignLocationResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    login_id: str,
    location_id: str,
    *,
    body: AssignLocationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/google/logins/{login_id}/locations/{location_id}/assign".format(
            login_id=quote(str(login_id), safe=""),
            location_id=quote(str(location_id), safe=""),
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

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

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
    location_id: str,
    *,
    client: AuthenticatedClient,
    body: AssignLocationRequest,
) -> Response[AssignLocationResponse | ErrorResponse]:
    """Assign a Google Business Profile location to a brand

     Assigns one location from this login to the given brand, without re-doing OAuth. Each location
    belongs to exactly one brand, and each brand holds at most one Google Business Profile.

    Args:
        login_id (str):
        location_id (str):
        body (AssignLocationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignLocationResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
        location_id=location_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_id: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
    body: AssignLocationRequest,
) -> AssignLocationResponse | ErrorResponse | None:
    """Assign a Google Business Profile location to a brand

     Assigns one location from this login to the given brand, without re-doing OAuth. Each location
    belongs to exactly one brand, and each brand holds at most one Google Business Profile.

    Args:
        login_id (str):
        location_id (str):
        body (AssignLocationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignLocationResponse | ErrorResponse
    """

    return sync_detailed(
        login_id=login_id,
        location_id=location_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    login_id: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
    body: AssignLocationRequest,
) -> Response[AssignLocationResponse | ErrorResponse]:
    """Assign a Google Business Profile location to a brand

     Assigns one location from this login to the given brand, without re-doing OAuth. Each location
    belongs to exactly one brand, and each brand holds at most one Google Business Profile.

    Args:
        login_id (str):
        location_id (str):
        body (AssignLocationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignLocationResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        login_id=login_id,
        location_id=location_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_id: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
    body: AssignLocationRequest,
) -> AssignLocationResponse | ErrorResponse | None:
    """Assign a Google Business Profile location to a brand

     Assigns one location from this login to the given brand, without re-doing OAuth. Each location
    belongs to exactly one brand, and each brand holds at most one Google Business Profile.

    Args:
        login_id (str):
        location_id (str):
        body (AssignLocationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignLocationResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            login_id=login_id,
            location_id=location_id,
            client=client,
            body=body,
        )
    ).parsed
