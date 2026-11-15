from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.import_posts_body import ImportPostsBody
from ...models.import_posts_dry_run import ImportPostsDryRun
from ...models.import_posts_response import ImportPostsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ImportPostsBody,
    dry_run: ImportPostsDryRun | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_dry_run: str | Unset = UNSET
    if not isinstance(dry_run, Unset):
        json_dry_run = dry_run.value

    params["dry_run"] = json_dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/posts/import",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | ImportPostsResponse | None:
    if response.status_code == 200:
        response_200 = ImportPostsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | ImportPostsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ImportPostsBody,
    dry_run: ImportPostsDryRun | Unset = UNSET,
) -> Response[ErrorResponse | ImportPostsResponse]:
    """Bulk import posts from CSV

     Upload a CSV file to create multiple posts. Use dry_run=true to validate without creating. Columns,
    in order: text, title, account_ids, scheduled_at, visibility, first_comment, platform_data,
    board_id. Only text is required. account_ids is pipe separated.

    Args:
        dry_run (ImportPostsDryRun | Unset):
        body (ImportPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImportPostsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        dry_run=dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ImportPostsBody,
    dry_run: ImportPostsDryRun | Unset = UNSET,
) -> ErrorResponse | ImportPostsResponse | None:
    """Bulk import posts from CSV

     Upload a CSV file to create multiple posts. Use dry_run=true to validate without creating. Columns,
    in order: text, title, account_ids, scheduled_at, visibility, first_comment, platform_data,
    board_id. Only text is required. account_ids is pipe separated.

    Args:
        dry_run (ImportPostsDryRun | Unset):
        body (ImportPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImportPostsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ImportPostsBody,
    dry_run: ImportPostsDryRun | Unset = UNSET,
) -> Response[ErrorResponse | ImportPostsResponse]:
    """Bulk import posts from CSV

     Upload a CSV file to create multiple posts. Use dry_run=true to validate without creating. Columns,
    in order: text, title, account_ids, scheduled_at, visibility, first_comment, platform_data,
    board_id. Only text is required. account_ids is pipe separated.

    Args:
        dry_run (ImportPostsDryRun | Unset):
        body (ImportPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImportPostsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ImportPostsBody,
    dry_run: ImportPostsDryRun | Unset = UNSET,
) -> ErrorResponse | ImportPostsResponse | None:
    """Bulk import posts from CSV

     Upload a CSV file to create multiple posts. Use dry_run=true to validate without creating. Columns,
    in order: text, title, account_ids, scheduled_at, visibility, first_comment, platform_data,
    board_id. Only text is required. account_ids is pipe separated.

    Args:
        dry_run (ImportPostsDryRun | Unset):
        body (ImportPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImportPostsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            dry_run=dry_run,
        )
    ).parsed
