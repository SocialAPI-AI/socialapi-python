from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_moderate_you_tube_comment_request import ApiEndpointsModerateYouTubeCommentRequest
from ...models.api_endpoints_success_response import ApiEndpointsSuccessResponse
from ...types import Response


def _get_kwargs(
    comment_id: str,
    *,
    body: ApiEndpointsModerateYouTubeCommentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/platforms/youtube/comments/{comment_id}/moderate".format(
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 501:
        response_501 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    comment_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsModerateYouTubeCommentRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Moderate a YouTube comment

     Sets the moderation status of a YouTube comment (published, held_for_review, or rejected),
    optionally banning the author. ban_author is only valid with status=rejected. YouTube only.

    Args:
        comment_id (str):
        body (ApiEndpointsModerateYouTubeCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    comment_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsModerateYouTubeCommentRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Moderate a YouTube comment

     Sets the moderation status of a YouTube comment (published, held_for_review, or rejected),
    optionally banning the author. ban_author is only valid with status=rejected. YouTube only.

    Args:
        comment_id (str):
        body (ApiEndpointsModerateYouTubeCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return sync_detailed(
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    comment_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsModerateYouTubeCommentRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]:
    """Moderate a YouTube comment

     Sets the moderation status of a YouTube comment (published, held_for_review, or rejected),
    optionally banning the author. ban_author is only valid with status=rejected. YouTube only.

    Args:
        comment_id (str):
        body (ApiEndpointsModerateYouTubeCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    comment_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsModerateYouTubeCommentRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse | None:
    """Moderate a YouTube comment

     Sets the moderation status of a YouTube comment (published, held_for_review, or rejected),
    optionally banning the author. ban_author is only valid with status=rejected. YouTube only.

    Args:
        comment_id (str):
        body (ApiEndpointsModerateYouTubeCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsSuccessResponse
    """

    return (
        await asyncio_detailed(
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
