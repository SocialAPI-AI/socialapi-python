from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_instagram_collaborators_response import ApiEndpointsInstagramCollaboratorsResponse
from ...types import Response


def _get_kwargs(
    id: str,
    media_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/instagram/accounts/{id}/media/{media_id}/collaborators".format(
            id=quote(str(id), safe=""),
            media_id=quote(str(media_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsInstagramCollaboratorsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

    if response.status_code == 503:
        response_503 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse]:
    """List collaborators on an Instagram post

     Returns the collaborators invited on a co-authored Instagram post and the state of each invite
    (accepted, pending, declined). Readable only by the account that published the media: Meta scopes
    co-authored media data to the publisher, so a collaborating account cannot read this edge.
    Collaborators can only be invited when the post is created (platform_data.collaborators); Instagram
    exposes no API to add one to an already-published post.

    Args:
        id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        media_id=media_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse | None:
    """List collaborators on an Instagram post

     Returns the collaborators invited on a co-authored Instagram post and the state of each invite
    (accepted, pending, declined). Readable only by the account that published the media: Meta scopes
    co-authored media data to the publisher, so a collaborating account cannot read this edge.
    Collaborators can only be invited when the post is created (platform_data.collaborators); Instagram
    exposes no API to add one to an already-published post.

    Args:
        id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse
    """

    return sync_detailed(
        id=id,
        media_id=media_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse]:
    """List collaborators on an Instagram post

     Returns the collaborators invited on a co-authored Instagram post and the state of each invite
    (accepted, pending, declined). Readable only by the account that published the media: Meta scopes
    co-authored media data to the publisher, so a collaborating account cannot read this edge.
    Collaborators can only be invited when the post is created (platform_data.collaborators); Instagram
    exposes no API to add one to an already-published post.

    Args:
        id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        media_id=media_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    media_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse | None:
    """List collaborators on an Instagram post

     Returns the collaborators invited on a co-authored Instagram post and the state of each invite
    (accepted, pending, declined). Readable only by the account that published the media: Meta scopes
    co-authored media data to the publisher, so a collaborating account cannot read this edge.
    Collaborators can only be invited when the post is created (platform_data.collaborators); Instagram
    exposes no API to add one to an already-published post.

    Args:
        id (str):
        media_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsInstagramCollaboratorsResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            media_id=media_id,
            client=client,
        )
    ).parsed
