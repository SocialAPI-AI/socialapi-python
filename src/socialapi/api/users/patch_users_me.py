from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_patch_me_request import ApiEndpointsPatchMeRequest
from ...models.api_endpoints_user_me_response import ApiEndpointsUserMeResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ApiEndpointsPatchMeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/users/me",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsUserMeResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsPatchMeRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse]:
    """Update current user

     Updates the authenticated user's profile. Supports setting onboarding=false to mark onboarding as
    complete, and optionally recording use_case, referral, job_role and signup_metadata. The response
    reflects the current billing_blocked state, unaffected by this update. The response includes the
    caller's team role: "admin", "developer", or "" for the account owner.

    Args:
        body (ApiEndpointsPatchMeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsPatchMeRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse | None:
    """Update current user

     Updates the authenticated user's profile. Supports setting onboarding=false to mark onboarding as
    complete, and optionally recording use_case, referral, job_role and signup_metadata. The response
    reflects the current billing_blocked state, unaffected by this update. The response includes the
    caller's team role: "admin", "developer", or "" for the account owner.

    Args:
        body (ApiEndpointsPatchMeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsPatchMeRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse]:
    """Update current user

     Updates the authenticated user's profile. Supports setting onboarding=false to mark onboarding as
    complete, and optionally recording use_case, referral, job_role and signup_metadata. The response
    reflects the current billing_blocked state, unaffected by this update. The response includes the
    caller's team role: "admin", "developer", or "" for the account owner.

    Args:
        body (ApiEndpointsPatchMeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsPatchMeRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse | None:
    """Update current user

     Updates the authenticated user's profile. Supports setting onboarding=false to mark onboarding as
    complete, and optionally recording use_case, referral, job_role and signup_metadata. The response
    reflects the current billing_blocked state, unaffected by this update. The response includes the
    caller's team role: "admin", "developer", or "" for the account owner.

    Args:
        body (ApiEndpointsPatchMeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsUserMeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
