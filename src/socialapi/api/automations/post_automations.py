from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_endpoints_error_response import ApiEndpointsErrorResponse
from ...models.social_api_ai_core_api_service_automation import SocialApiAiCoreApiServiceAutomation
from ...models.social_api_ai_core_api_service_create_automation_params import (
    SocialApiAiCoreApiServiceCreateAutomationParams,
)
from ...types import Response


def _get_kwargs(
    *,
    body: SocialApiAiCoreApiServiceCreateAutomationParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/automations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation | None:
    if response.status_code == 201:
        response_201 = SocialApiAiCoreApiServiceAutomation.from_dict(response.json())

        return response_201

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

    if response.status_code == 409:
        response_409 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ApiEndpointsErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiServiceCreateAutomationParams,
) -> Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation]:
    """Create an Automation

     Creates an Automation on an Instagram or Facebook account. When a comment or DM on the account
    matches its filters, its actions are carried out within seconds, with no code on your side. Each
    action costs what the same API call costs: reply_comment and send_dm cost 1 credit, private_reply
    and hide_comment are free. The first step's actions depend on the trigger: a comment trigger allows
    hide_comment, reply_comment and private_reply; a dm trigger allows send_dm. Steps after start run
    when the person taps one of your postback buttons, and may only send DMs. An account holds at most
    50 Automations. Comments and messages sent by the account itself never trigger it; on Facebook that
    is the Page, so a Page admin commenting from their personal profile does trigger it. A dm Automation
    answers the same person at most 5 times an hour. Besides automations:write, a scoped key needs the
    scope each action's own API call needs: inbox:write for hide_comment, reply_comment and
    private_reply, dms:send for send_dm. Send follow_gate instead of steps to build a Follow gate: the
    commenter gets a private reply with a button, and a tap sends the link if they follow the account,
    otherwise a follow-first message with a button to try again. Instagram only.

    Args:
        body (SocialApiAiCoreApiServiceCreateAutomationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation]
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
    body: SocialApiAiCoreApiServiceCreateAutomationParams,
) -> ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation | None:
    """Create an Automation

     Creates an Automation on an Instagram or Facebook account. When a comment or DM on the account
    matches its filters, its actions are carried out within seconds, with no code on your side. Each
    action costs what the same API call costs: reply_comment and send_dm cost 1 credit, private_reply
    and hide_comment are free. The first step's actions depend on the trigger: a comment trigger allows
    hide_comment, reply_comment and private_reply; a dm trigger allows send_dm. Steps after start run
    when the person taps one of your postback buttons, and may only send DMs. An account holds at most
    50 Automations. Comments and messages sent by the account itself never trigger it; on Facebook that
    is the Page, so a Page admin commenting from their personal profile does trigger it. A dm Automation
    answers the same person at most 5 times an hour. Besides automations:write, a scoped key needs the
    scope each action's own API call needs: inbox:write for hide_comment, reply_comment and
    private_reply, dms:send for send_dm. Send follow_gate instead of steps to build a Follow gate: the
    commenter gets a private reply with a button, and a tap sends the link if they follow the account,
    otherwise a follow-first message with a button to try again. Instagram only.

    Args:
        body (SocialApiAiCoreApiServiceCreateAutomationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiServiceCreateAutomationParams,
) -> Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation]:
    """Create an Automation

     Creates an Automation on an Instagram or Facebook account. When a comment or DM on the account
    matches its filters, its actions are carried out within seconds, with no code on your side. Each
    action costs what the same API call costs: reply_comment and send_dm cost 1 credit, private_reply
    and hide_comment are free. The first step's actions depend on the trigger: a comment trigger allows
    hide_comment, reply_comment and private_reply; a dm trigger allows send_dm. Steps after start run
    when the person taps one of your postback buttons, and may only send DMs. An account holds at most
    50 Automations. Comments and messages sent by the account itself never trigger it; on Facebook that
    is the Page, so a Page admin commenting from their personal profile does trigger it. A dm Automation
    answers the same person at most 5 times an hour. Besides automations:write, a scoped key needs the
    scope each action's own API call needs: inbox:write for hide_comment, reply_comment and
    private_reply, dms:send for send_dm. Send follow_gate instead of steps to build a Follow gate: the
    commenter gets a private reply with a button, and a tap sends the link if they follow the account,
    otherwise a follow-first message with a button to try again. Instagram only.

    Args:
        body (SocialApiAiCoreApiServiceCreateAutomationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SocialApiAiCoreApiServiceCreateAutomationParams,
) -> ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation | None:
    """Create an Automation

     Creates an Automation on an Instagram or Facebook account. When a comment or DM on the account
    matches its filters, its actions are carried out within seconds, with no code on your side. Each
    action costs what the same API call costs: reply_comment and send_dm cost 1 credit, private_reply
    and hide_comment are free. The first step's actions depend on the trigger: a comment trigger allows
    hide_comment, reply_comment and private_reply; a dm trigger allows send_dm. Steps after start run
    when the person taps one of your postback buttons, and may only send DMs. An account holds at most
    50 Automations. Comments and messages sent by the account itself never trigger it; on Facebook that
    is the Page, so a Page admin commenting from their personal profile does trigger it. A dm Automation
    answers the same person at most 5 times an hour. Besides automations:write, a scoped key needs the
    scope each action's own API call needs: inbox:write for hide_comment, reply_comment and
    private_reply, dms:send for send_dm. Send follow_gate instead of steps to build a Follow gate: the
    commenter gets a private reply with a button, and a tap sends the link if they follow the account,
    otherwise a follow-first message with a button to try again. Instagram only.

    Args:
        body (SocialApiAiCoreApiServiceCreateAutomationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEndpointsErrorResponse | SocialApiAiCoreApiServiceAutomation
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
