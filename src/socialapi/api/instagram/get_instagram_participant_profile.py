from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.instagram_participant_profile_response import InstagramParticipantProfileResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    participant_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/platforms/instagram/accounts/{account_id}/participants/{participant_id}/profile".format(
            account_id=quote(str(account_id), safe=""),
            participant_id=quote(str(participant_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | InstagramParticipantProfileResponse | None:
    if response.status_code == 200:
        response_200 = InstagramParticipantProfileResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 501:
        response_501 = ErrorResponse.from_dict(response.json())

        return response_501

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | InstagramParticipantProfileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    participant_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | InstagramParticipantProfileResponse]:
    """Get an Instagram messaging participant's profile

     Returns the profile Instagram exposes for a messaging participant, including the follow relationship
    in both directions (is_user_follow_business, is_business_follow_user). Works for an Instagram
    account connected either directly or through a linked Facebook Page. The follow relationship is
    current as of the call; do not cache it, since it changes the moment someone unfollows. Instagram
    only returns this data for users who have consented by messaging your account or tapping an
    icebreaker or the persistent menu; for anyone else this returns 403 platform.instagram.230, which
    means Instagram will not disclose the relationship and is NOT the same as "does not follow". Branch
    on that error rather than treating it as a negative. Fields name and profile_pic are absent for
    users who have set neither; the follow fields are still returned. profile_pic URLs expire after a
    few days, so do not store them.

    Args:
        account_id (str):
        participant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstagramParticipantProfileResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        participant_id=participant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    participant_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | InstagramParticipantProfileResponse | None:
    """Get an Instagram messaging participant's profile

     Returns the profile Instagram exposes for a messaging participant, including the follow relationship
    in both directions (is_user_follow_business, is_business_follow_user). Works for an Instagram
    account connected either directly or through a linked Facebook Page. The follow relationship is
    current as of the call; do not cache it, since it changes the moment someone unfollows. Instagram
    only returns this data for users who have consented by messaging your account or tapping an
    icebreaker or the persistent menu; for anyone else this returns 403 platform.instagram.230, which
    means Instagram will not disclose the relationship and is NOT the same as "does not follow". Branch
    on that error rather than treating it as a negative. Fields name and profile_pic are absent for
    users who have set neither; the follow fields are still returned. profile_pic URLs expire after a
    few days, so do not store them.

    Args:
        account_id (str):
        participant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstagramParticipantProfileResponse
    """

    return sync_detailed(
        account_id=account_id,
        participant_id=participant_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    participant_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | InstagramParticipantProfileResponse]:
    """Get an Instagram messaging participant's profile

     Returns the profile Instagram exposes for a messaging participant, including the follow relationship
    in both directions (is_user_follow_business, is_business_follow_user). Works for an Instagram
    account connected either directly or through a linked Facebook Page. The follow relationship is
    current as of the call; do not cache it, since it changes the moment someone unfollows. Instagram
    only returns this data for users who have consented by messaging your account or tapping an
    icebreaker or the persistent menu; for anyone else this returns 403 platform.instagram.230, which
    means Instagram will not disclose the relationship and is NOT the same as "does not follow". Branch
    on that error rather than treating it as a negative. Fields name and profile_pic are absent for
    users who have set neither; the follow fields are still returned. profile_pic URLs expire after a
    few days, so do not store them.

    Args:
        account_id (str):
        participant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstagramParticipantProfileResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        participant_id=participant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    participant_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | InstagramParticipantProfileResponse | None:
    """Get an Instagram messaging participant's profile

     Returns the profile Instagram exposes for a messaging participant, including the follow relationship
    in both directions (is_user_follow_business, is_business_follow_user). Works for an Instagram
    account connected either directly or through a linked Facebook Page. The follow relationship is
    current as of the call; do not cache it, since it changes the moment someone unfollows. Instagram
    only returns this data for users who have consented by messaging your account or tapping an
    icebreaker or the persistent menu; for anyone else this returns 403 platform.instagram.230, which
    means Instagram will not disclose the relationship and is NOT the same as "does not follow". Branch
    on that error rather than treating it as a negative. Fields name and profile_pic are absent for
    users who have set neither; the follow fields are still returned. profile_pic URLs expire after a
    few days, so do not store them.

    Args:
        account_id (str):
        participant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstagramParticipantProfileResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            participant_id=participant_id,
            client=client,
        )
    ).parsed
