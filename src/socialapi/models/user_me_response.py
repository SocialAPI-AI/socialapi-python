from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_me_response_signup_metadata_type_0 import UserMeResponseSignupMetadataType0


T = TypeVar("T", bound="UserMeResponse")


@_attrs_define
class UserMeResponse:
    """
    Attributes:
        allowed_platforms (list[str]):  Example: ['instagram', 'facebook'].
        avatar_url (None | str):  Example: https://example.com/avatar.jpg.
        beta_tester (bool):  Example: False.
        billing_blocked (bool): BillingBlocked is true when API access and webhook delivery are paused.
            Read BillingBlockReason to tell why and whether paying lifts it. Example: False.
        billing_currency (str): BillingCurrency is the currency your subscription is billed in: "usd"
            or "eur". A subscription never changes currency, so plan changes are
            priced in it. Kept after a cancellation; "" when you never subscribed. Example: usd.
        email (str):  Example: user@example.com.
        experiment_enrolled (bool): ExperimentEnrolled is true only when ExperimentVariant was assigned by
            the experiment itself. False means the "control" above is a fallback
            (not enrolled, flag off, or evaluation failed) and must not be recorded
            as the caller's arm. Example: False.
        experiment_variant (str): ExperimentVariant is the caller's variant for staged feature rollouts:
            "control" or "treatment". "control" unless the caller is enrolled. Example: control.
        facebook_page_selection (bool): FacebookPageSelection, when true, makes a Facebook connection (and an
            Instagram connection through Facebook Login) end with
            status=selection_required so you choose the Pages. Read-only. Example: False.
        id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        job_role (None | str): JobRole is what best describes the user, as answered during
            onboarding. Null until answered. Example: Founder / CEO.
        lock_accounts_to_brand (bool): LockAccountsToBrand, when true, rejects connecting a social account that is
            already connected to another of your brands (409 account.already_linked)
            instead of moving it. Default false. Example: False.
        onboarding (bool):  Example: True.
        plan (str):  Example: free.
        role (str): Role is the caller's team role: "admin", "developer", or "" for the
            account Owner, who holds no Role. An API key and an OAuth token both
            read "". Example: admin.
        signup_metadata (None | UserMeResponseSignupMetadataType0): SignupMetadata holds open-ended answers recorded at
            signup, such as
            referral_source and search_query. An empty object until answered.
        use_case (None | str):  Example: Managing clients' accounts (agency).
        billing_block_reason (str | Unset): BillingBlockReason is why access is paused, empty when it is not.
            "past_due": a payment failed, and settling it restores access.
            "ban": the account was suspended for a Terms of Service violation.
            Paying does not lift it, and every route except this one returns
            403 auth.suspended. Contact support to appeal. Example: past_due.
        billing_blocked_at (datetime.datetime | Unset): BillingBlockedAt is when the block began, or null when not
            blocked.
    """

    allowed_platforms: list[str]
    avatar_url: None | str
    beta_tester: bool
    billing_blocked: bool
    billing_currency: str
    email: str
    experiment_enrolled: bool
    experiment_variant: str
    facebook_page_selection: bool
    id: str
    job_role: None | str
    lock_accounts_to_brand: bool
    onboarding: bool
    plan: str
    role: str
    signup_metadata: None | UserMeResponseSignupMetadataType0
    use_case: None | str
    billing_block_reason: str | Unset = UNSET
    billing_blocked_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_me_response_signup_metadata_type_0 import UserMeResponseSignupMetadataType0  # noqa: PLC0415

        allowed_platforms = self.allowed_platforms

        avatar_url: None | str
        avatar_url = self.avatar_url

        beta_tester = self.beta_tester

        billing_blocked = self.billing_blocked

        billing_currency = self.billing_currency

        email = self.email

        experiment_enrolled = self.experiment_enrolled

        experiment_variant = self.experiment_variant

        facebook_page_selection = self.facebook_page_selection

        id = self.id

        job_role: None | str
        job_role = self.job_role

        lock_accounts_to_brand = self.lock_accounts_to_brand

        onboarding = self.onboarding

        plan = self.plan

        role = self.role

        signup_metadata: dict[str, Any] | None
        if isinstance(self.signup_metadata, UserMeResponseSignupMetadataType0):
            signup_metadata = self.signup_metadata.to_dict()
        else:
            signup_metadata = self.signup_metadata

        use_case: None | str
        use_case = self.use_case

        billing_block_reason = self.billing_block_reason

        billing_blocked_at: str | Unset = UNSET
        if not isinstance(self.billing_blocked_at, Unset):
            billing_blocked_at = self.billing_blocked_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_platforms": allowed_platforms,
                "avatar_url": avatar_url,
                "beta_tester": beta_tester,
                "billing_blocked": billing_blocked,
                "billing_currency": billing_currency,
                "email": email,
                "experiment_enrolled": experiment_enrolled,
                "experiment_variant": experiment_variant,
                "facebook_page_selection": facebook_page_selection,
                "id": id,
                "job_role": job_role,
                "lock_accounts_to_brand": lock_accounts_to_brand,
                "onboarding": onboarding,
                "plan": plan,
                "role": role,
                "signup_metadata": signup_metadata,
                "use_case": use_case,
            }
        )
        if billing_block_reason is not UNSET:
            field_dict["billing_block_reason"] = billing_block_reason
        if billing_blocked_at is not UNSET:
            field_dict["billing_blocked_at"] = billing_blocked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_me_response_signup_metadata_type_0 import UserMeResponseSignupMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        allowed_platforms = cast(list[str], d.pop("allowed_platforms"))

        def _parse_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url"))

        beta_tester = d.pop("beta_tester")

        billing_blocked = d.pop("billing_blocked")

        billing_currency = d.pop("billing_currency")

        email = d.pop("email")

        experiment_enrolled = d.pop("experiment_enrolled")

        experiment_variant = d.pop("experiment_variant")

        facebook_page_selection = d.pop("facebook_page_selection")

        id = d.pop("id")

        def _parse_job_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        job_role = _parse_job_role(d.pop("job_role"))

        lock_accounts_to_brand = d.pop("lock_accounts_to_brand")

        onboarding = d.pop("onboarding")

        plan = d.pop("plan")

        role = d.pop("role")

        def _parse_signup_metadata(data: object) -> None | UserMeResponseSignupMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signup_metadata_type_0 = UserMeResponseSignupMetadataType0.from_dict(data)

                return signup_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserMeResponseSignupMetadataType0, data)

        signup_metadata = _parse_signup_metadata(d.pop("signup_metadata"))

        def _parse_use_case(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        use_case = _parse_use_case(d.pop("use_case"))

        billing_block_reason = d.pop("billing_block_reason", UNSET)

        _billing_blocked_at = d.pop("billing_blocked_at", UNSET)
        billing_blocked_at: datetime.datetime | Unset
        if isinstance(_billing_blocked_at, Unset):
            billing_blocked_at = UNSET
        else:
            billing_blocked_at = datetime.datetime.fromisoformat(_billing_blocked_at)

        user_me_response = cls(
            allowed_platforms=allowed_platforms,
            avatar_url=avatar_url,
            beta_tester=beta_tester,
            billing_blocked=billing_blocked,
            billing_currency=billing_currency,
            email=email,
            experiment_enrolled=experiment_enrolled,
            experiment_variant=experiment_variant,
            facebook_page_selection=facebook_page_selection,
            id=id,
            job_role=job_role,
            lock_accounts_to_brand=lock_accounts_to_brand,
            onboarding=onboarding,
            plan=plan,
            role=role,
            signup_metadata=signup_metadata,
            use_case=use_case,
            billing_block_reason=billing_block_reason,
            billing_blocked_at=billing_blocked_at,
        )

        user_me_response.additional_properties = d
        return user_me_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
