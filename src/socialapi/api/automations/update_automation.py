from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.automation import Automation
from ...models.error_response import ErrorResponse
from ...models.update_automation_params import UpdateAutomationParams
from ...types import Response


def _get_kwargs(
    automation_id: str,
    *,
    body: UpdateAutomationParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/automations/{automation_id}".format(
            automation_id=quote(str(automation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Automation | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = Automation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Automation | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    automation_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAutomationParams,
) -> Response[Automation | ErrorResponse]:
    """Update an Automation

     Updates the fields you send and keeps the rest. Set status to paused to stop the Automation and to
    active to resume it. steps replaces the whole list. Changed steps or post_ids must meet the same
    rules as creation. Renaming or pausing needs only automations:write; resuming, or changing steps,
    post_ids or once_per_person, also needs each action's own scope.

    Args:
        automation_id (str):
        body (UpdateAutomationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Automation | ErrorResponse]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    automation_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAutomationParams,
) -> Automation | ErrorResponse | None:
    """Update an Automation

     Updates the fields you send and keeps the rest. Set status to paused to stop the Automation and to
    active to resume it. steps replaces the whole list. Changed steps or post_ids must meet the same
    rules as creation. Renaming or pausing needs only automations:write; resuming, or changing steps,
    post_ids or once_per_person, also needs each action's own scope.

    Args:
        automation_id (str):
        body (UpdateAutomationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Automation | ErrorResponse
    """

    return sync_detailed(
        automation_id=automation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    automation_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAutomationParams,
) -> Response[Automation | ErrorResponse]:
    """Update an Automation

     Updates the fields you send and keeps the rest. Set status to paused to stop the Automation and to
    active to resume it. steps replaces the whole list. Changed steps or post_ids must meet the same
    rules as creation. Renaming or pausing needs only automations:write; resuming, or changing steps,
    post_ids or once_per_person, also needs each action's own scope.

    Args:
        automation_id (str):
        body (UpdateAutomationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Automation | ErrorResponse]
    """

    kwargs = _get_kwargs(
        automation_id=automation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    automation_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAutomationParams,
) -> Automation | ErrorResponse | None:
    """Update an Automation

     Updates the fields you send and keeps the rest. Set status to paused to stop the Automation and to
    active to resume it. steps replaces the whole list. Changed steps or post_ids must meet the same
    rules as creation. Renaming or pausing needs only automations:write; resuming, or changing steps,
    post_ids or once_per_person, also needs each action's own scope.

    Args:
        automation_id (str):
        body (UpdateAutomationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Automation | ErrorResponse
    """

    return (
        await asyncio_detailed(
            automation_id=automation_id,
            client=client,
            body=body,
        )
    ).parsed
