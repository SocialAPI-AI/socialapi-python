from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.api_endpoints_reply_review_request import ApiEndpointsReplyReviewRequest
from ...models.api_endpoints_reply_to_review_response import ApiEndpointsReplyToReviewResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ApiEndpointsReplyReviewRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/reviews/{id}/reply".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse | None:
    if response.status_code == 200:
        response_200 = ApiEndpointsReplyToReviewResponse.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsReplyReviewRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse]:
    """Reply to a review

     Posts a public reply to a review on the platform (Google Business Profile, App Store Connect).
    Consumes 1 interaction credit. On Google, replies are moderated: a successful response returns state
    PENDING and the reply is not publicly visible until it becomes APPROVED. A rejected reply is never
    published, and the reason is reported as policy_violation on the review. On App Store Connect,
    replying again replaces your earlier response, and a response can take up to 24 hours to appear on
    the App Store.

    Args:
        id (str):
        body (ApiEndpointsReplyReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsReplyReviewRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse | None:
    """Reply to a review

     Posts a public reply to a review on the platform (Google Business Profile, App Store Connect).
    Consumes 1 interaction credit. On Google, replies are moderated: a successful response returns state
    PENDING and the reply is not publicly visible until it becomes APPROVED. A rejected reply is never
    published, and the reason is reported as policy_violation on the review. On App Store Connect,
    replying again replaces your earlier response, and a response can take up to 24 hours to appear on
    the App Store.

    Args:
        id (str):
        body (ApiEndpointsReplyReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsReplyReviewRequest,
) -> Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse]:
    """Reply to a review

     Posts a public reply to a review on the platform (Google Business Profile, App Store Connect).
    Consumes 1 interaction credit. On Google, replies are moderated: a successful response returns state
    PENDING and the reply is not publicly visible until it becomes APPROVED. A rejected reply is never
    published, and the reason is reported as policy_violation on the review. On App Store Connect,
    replying again replaces your earlier response, and a response can take up to 24 hours to appear on
    the App Store.

    Args:
        id (str):
        body (ApiEndpointsReplyReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiEndpointsReplyReviewRequest,
) -> ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse | None:
    """Reply to a review

     Posts a public reply to a review on the platform (Google Business Profile, App Store Connect).
    Consumes 1 interaction credit. On Google, replies are moderated: a successful response returns state
    PENDING and the reply is not publicly visible until it becomes APPROVED. A rejected reply is never
    published, and the reason is reported as policy_violation on the review. On App Store Connect,
    replying again replaces your earlier response, and a response can take up to 24 hours to appear on
    the App Store.

    Args:
        id (str):
        body (ApiEndpointsReplyReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | ApiEndpointsReplyToReviewResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
