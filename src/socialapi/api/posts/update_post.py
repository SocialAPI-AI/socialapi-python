from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_response import PostResponse
from ...models.update_post_request import UpdatePostRequest
from ...types import Response


def _get_kwargs(
    post_id: str,
    *,
    body: UpdatePostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/posts/{post_id}".format(
            post_id=quote(str(post_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | PostResponse | None:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | PostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    post_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePostRequest,
) -> Response[ErrorResponse | PostResponse]:
    """Update a post

     Updates the text, media, schedule time, targets, or hidden status of a pending post.
    Posts in `draft`, `scheduled`, or `failed` status accept every field. Updating a failed post does
    not republish it: call `POST /posts/{post_id}/retry` afterwards.
    A `published` or `partial` post can be edited only when it is live on Google Business Profile alone.
    Send `text`, `platform_data.google.callToAction`, or both: any other field returns `400
    validation.field_not_editable`. A post also live on another platform returns `409
    post.state_invalid`.
    When the post is live on several Google locations and only some accept the edit, the response is the
    error from the first location that refused, and `error.meta` lists `updated_account_ids` and
    `not_updated_account_ids`. Send the same request again to finish the edit.
    `queue_id` moves the post to another Queue, and `queue_id: null` takes it out of its Queue and keeps
    its time.
    Omit `targets` to keep the current ones. Sending `targets` replaces them all.
    `scheduled_at` must be in the future, and a scheduled post must keep at least one target.

    Args:
        post_id (str):
        body (UpdatePostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePostRequest,
) -> ErrorResponse | PostResponse | None:
    """Update a post

     Updates the text, media, schedule time, targets, or hidden status of a pending post.
    Posts in `draft`, `scheduled`, or `failed` status accept every field. Updating a failed post does
    not republish it: call `POST /posts/{post_id}/retry` afterwards.
    A `published` or `partial` post can be edited only when it is live on Google Business Profile alone.
    Send `text`, `platform_data.google.callToAction`, or both: any other field returns `400
    validation.field_not_editable`. A post also live on another platform returns `409
    post.state_invalid`.
    When the post is live on several Google locations and only some accept the edit, the response is the
    error from the first location that refused, and `error.meta` lists `updated_account_ids` and
    `not_updated_account_ids`. Send the same request again to finish the edit.
    `queue_id` moves the post to another Queue, and `queue_id: null` takes it out of its Queue and keeps
    its time.
    Omit `targets` to keep the current ones. Sending `targets` replaces them all.
    `scheduled_at` must be in the future, and a scheduled post must keep at least one target.

    Args:
        post_id (str):
        body (UpdatePostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostResponse
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePostRequest,
) -> Response[ErrorResponse | PostResponse]:
    """Update a post

     Updates the text, media, schedule time, targets, or hidden status of a pending post.
    Posts in `draft`, `scheduled`, or `failed` status accept every field. Updating a failed post does
    not republish it: call `POST /posts/{post_id}/retry` afterwards.
    A `published` or `partial` post can be edited only when it is live on Google Business Profile alone.
    Send `text`, `platform_data.google.callToAction`, or both: any other field returns `400
    validation.field_not_editable`. A post also live on another platform returns `409
    post.state_invalid`.
    When the post is live on several Google locations and only some accept the edit, the response is the
    error from the first location that refused, and `error.meta` lists `updated_account_ids` and
    `not_updated_account_ids`. Send the same request again to finish the edit.
    `queue_id` moves the post to another Queue, and `queue_id: null` takes it out of its Queue and keeps
    its time.
    Omit `targets` to keep the current ones. Sending `targets` replaces them all.
    `scheduled_at` must be in the future, and a scheduled post must keep at least one target.

    Args:
        post_id (str):
        body (UpdatePostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePostRequest,
) -> ErrorResponse | PostResponse | None:
    """Update a post

     Updates the text, media, schedule time, targets, or hidden status of a pending post.
    Posts in `draft`, `scheduled`, or `failed` status accept every field. Updating a failed post does
    not republish it: call `POST /posts/{post_id}/retry` afterwards.
    A `published` or `partial` post can be edited only when it is live on Google Business Profile alone.
    Send `text`, `platform_data.google.callToAction`, or both: any other field returns `400
    validation.field_not_editable`. A post also live on another platform returns `409
    post.state_invalid`.
    When the post is live on several Google locations and only some accept the edit, the response is the
    error from the first location that refused, and `error.meta` lists `updated_account_ids` and
    `not_updated_account_ids`. Send the same request again to finish the edit.
    `queue_id` moves the post to another Queue, and `queue_id: null` takes it out of its Queue and keeps
    its time.
    Omit `targets` to keep the current ones. Sending `targets` replaces them all.
    `scheduled_at` must be in the future, and a scheduled post must keep at least one target.

    Args:
        post_id (str):
        body (UpdatePostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
            body=body,
        )
    ).parsed
