from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_update_you_tube_video_request import ApiEndpointsUpdateYouTubeVideoRequest
from ...models.patch_platforms_youtube_accounts_id_videos_video_id_response_200 import (
    PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    video_id: str,
    *,
    body: ApiEndpointsUpdateYouTubeVideoRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/platforms/youtube/accounts/{id}/videos/{video_id}".format(
            id=quote(str(id), safe=""),
            video_id=quote(str(video_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ApiEndpointsUpdateYouTubeVideoRequest | Unset = UNSET,
) -> Response[PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200]:
    """Edit a published YouTube video (title, description, visibility, Studio tags, cover)

    Args:
        id (str):
        video_id (str):
        body (ApiEndpointsUpdateYouTubeVideoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        video_id=video_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ApiEndpointsUpdateYouTubeVideoRequest | Unset = UNSET,
) -> PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200 | None:
    """Edit a published YouTube video (title, description, visibility, Studio tags, cover)

    Args:
        id (str):
        video_id (str):
        body (ApiEndpointsUpdateYouTubeVideoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200
    """

    return sync_detailed(
        id=id,
        video_id=video_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ApiEndpointsUpdateYouTubeVideoRequest | Unset = UNSET,
) -> Response[PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200]:
    """Edit a published YouTube video (title, description, visibility, Studio tags, cover)

    Args:
        id (str):
        video_id (str):
        body (ApiEndpointsUpdateYouTubeVideoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        video_id=video_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ApiEndpointsUpdateYouTubeVideoRequest | Unset = UNSET,
) -> PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200 | None:
    """Edit a published YouTube video (title, description, visibility, Studio tags, cover)

    Args:
        id (str):
        video_id (str):
        body (ApiEndpointsUpdateYouTubeVideoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchPlatformsYoutubeAccountsIdVideosVideoIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            video_id=video_id,
            client=client,
            body=body,
        )
    ).parsed
