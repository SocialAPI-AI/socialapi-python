from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_user_me_response_signup_metadata import ApiEndpointsUserMeResponseSignupMetadata


T = TypeVar("T", bound="ApiEndpointsUserMeResponse")


@_attrs_define
class ApiEndpointsUserMeResponse:
    """
    Attributes:
        allowed_platforms (list[str] | Unset):  Example: ['instagram', 'facebook'].
        avatar_url (str | Unset):  Example: https://example.com/avatar.jpg.
        beta_tester (bool | Unset):  Example: False.
        billing_block_reason (str | Unset): BillingBlockReason is why access is paused, empty when it is not.
            "past_due": a payment failed, and settling it restores access.
            "ban": the account was suspended for a Terms of Service violation.
            Paying does not lift it, and every route except this one returns
            403 auth.suspended. Contact support to appeal. Example: past_due.
        billing_blocked (bool | Unset): BillingBlocked is true when API access and webhook delivery are paused.
            Read BillingBlockReason to tell why and whether paying lifts it. Example: False.
        billing_blocked_at (str | Unset): BillingBlockedAt is when the block began, or null when not blocked.
        billing_currency (str | Unset): BillingCurrency is the currency your subscription is billed in: "usd"
            or "eur". A subscription never changes currency, so plan changes are
            priced in it. Kept after a cancellation; "" when you never subscribed. Example: usd.
        email (str | Unset):  Example: user@example.com.
        experiment_enrolled (bool | Unset): ExperimentEnrolled is true only when ExperimentVariant was assigned by
            the experiment itself. False means the "control" above is a fallback
            (not enrolled, flag off, or evaluation failed) and must not be recorded
            as the caller's arm. Example: False.
        experiment_variant (str | Unset): ExperimentVariant is the caller's variant for staged feature rollouts:
            "control" or "treatment". "control" unless the caller is enrolled. Example: control.
        facebook_page_selection (bool | Unset): FacebookPageSelection, when true, makes a Facebook connection (and an
            Instagram connection through Facebook Login) end with
            status=selection_required so you choose the Pages. Read-only. Example: False.
        id (str | Unset):  Example: 550e8400-e29b-41d4-a716-446655440000.
        job_role (str | Unset): JobRole is what best describes the user, as answered during
            onboarding. Null until answered. Example: Founder / CEO.
        lock_accounts_to_brand (bool | Unset): LockAccountsToBrand, when true, rejects connecting a social account that
            is
            already connected to another of your brands (409 account.already_linked)
            instead of moving it. Default false. Example: False.
        onboarding (bool | Unset):  Example: True.
        plan (str | Unset):  Example: free.
        role (str | Unset): Role is the caller's team role: "admin", "developer", or "" for the
            account Owner, who holds no Role. An API key and an OAuth token both
            read "". Example: admin.
        signup_metadata (ApiEndpointsUserMeResponseSignupMetadata | Unset): SignupMetadata holds open-ended answers
            recorded at signup, such as
            referral_source and search_query. An empty object until answered.
        use_case (str | Unset):  Example: Managing clients' accounts (agency).
    """

    allowed_platforms: list[str] | Unset = UNSET
    avatar_url: str | Unset = UNSET
    beta_tester: bool | Unset = UNSET
    billing_block_reason: str | Unset = UNSET
    billing_blocked: bool | Unset = UNSET
    billing_blocked_at: str | Unset = UNSET
    billing_currency: str | Unset = UNSET
    email: str | Unset = UNSET
    experiment_enrolled: bool | Unset = UNSET
    experiment_variant: str | Unset = UNSET
    facebook_page_selection: bool | Unset = UNSET
    id: str | Unset = UNSET
    job_role: str | Unset = UNSET
    lock_accounts_to_brand: bool | Unset = UNSET
    onboarding: bool | Unset = UNSET
    plan: str | Unset = UNSET
    role: str | Unset = UNSET
    signup_metadata: ApiEndpointsUserMeResponseSignupMetadata | Unset = UNSET
    use_case: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_platforms: list[str] | Unset = UNSET
        if not isinstance(self.allowed_platforms, Unset):
            allowed_platforms = self.allowed_platforms

        avatar_url = self.avatar_url

        beta_tester = self.beta_tester

        billing_block_reason = self.billing_block_reason

        billing_blocked = self.billing_blocked

        billing_blocked_at = self.billing_blocked_at

        billing_currency = self.billing_currency

        email = self.email

        experiment_enrolled = self.experiment_enrolled

        experiment_variant = self.experiment_variant

        facebook_page_selection = self.facebook_page_selection

        id = self.id

        job_role = self.job_role

        lock_accounts_to_brand = self.lock_accounts_to_brand

        onboarding = self.onboarding

        plan = self.plan

        role = self.role

        signup_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signup_metadata, Unset):
            signup_metadata = self.signup_metadata.to_dict()

        use_case = self.use_case

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_platforms is not UNSET:
            field_dict["allowed_platforms"] = allowed_platforms
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if beta_tester is not UNSET:
            field_dict["beta_tester"] = beta_tester
        if billing_block_reason is not UNSET:
            field_dict["billing_block_reason"] = billing_block_reason
        if billing_blocked is not UNSET:
            field_dict["billing_blocked"] = billing_blocked
        if billing_blocked_at is not UNSET:
            field_dict["billing_blocked_at"] = billing_blocked_at
        if billing_currency is not UNSET:
            field_dict["billing_currency"] = billing_currency
        if email is not UNSET:
            field_dict["email"] = email
        if experiment_enrolled is not UNSET:
            field_dict["experiment_enrolled"] = experiment_enrolled
        if experiment_variant is not UNSET:
            field_dict["experiment_variant"] = experiment_variant
        if facebook_page_selection is not UNSET:
            field_dict["facebook_page_selection"] = facebook_page_selection
        if id is not UNSET:
            field_dict["id"] = id
        if job_role is not UNSET:
            field_dict["job_role"] = job_role
        if lock_accounts_to_brand is not UNSET:
            field_dict["lock_accounts_to_brand"] = lock_accounts_to_brand
        if onboarding is not UNSET:
            field_dict["onboarding"] = onboarding
        if plan is not UNSET:
            field_dict["plan"] = plan
        if role is not UNSET:
            field_dict["role"] = role
        if signup_metadata is not UNSET:
            field_dict["signup_metadata"] = signup_metadata
        if use_case is not UNSET:
            field_dict["use_case"] = use_case

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_user_me_response_signup_metadata import (
            ApiEndpointsUserMeResponseSignupMetadata,  # noqa: PLC0415
        )

        d = dict(src_dict)
        allowed_platforms = cast(list[str], d.pop("allowed_platforms", UNSET))

        avatar_url = d.pop("avatar_url", UNSET)

        beta_tester = d.pop("beta_tester", UNSET)

        billing_block_reason = d.pop("billing_block_reason", UNSET)

        billing_blocked = d.pop("billing_blocked", UNSET)

        billing_blocked_at = d.pop("billing_blocked_at", UNSET)

        billing_currency = d.pop("billing_currency", UNSET)

        email = d.pop("email", UNSET)

        experiment_enrolled = d.pop("experiment_enrolled", UNSET)

        experiment_variant = d.pop("experiment_variant", UNSET)

        facebook_page_selection = d.pop("facebook_page_selection", UNSET)

        id = d.pop("id", UNSET)

        job_role = d.pop("job_role", UNSET)

        lock_accounts_to_brand = d.pop("lock_accounts_to_brand", UNSET)

        onboarding = d.pop("onboarding", UNSET)

        plan = d.pop("plan", UNSET)

        role = d.pop("role", UNSET)

        _signup_metadata = d.pop("signup_metadata", UNSET)
        signup_metadata: ApiEndpointsUserMeResponseSignupMetadata | Unset
        if isinstance(_signup_metadata, Unset):
            signup_metadata = UNSET
        else:
            signup_metadata = ApiEndpointsUserMeResponseSignupMetadata.from_dict(_signup_metadata)

        use_case = d.pop("use_case", UNSET)

        api_endpoints_user_me_response = cls(
            allowed_platforms=allowed_platforms,
            avatar_url=avatar_url,
            beta_tester=beta_tester,
            billing_block_reason=billing_block_reason,
            billing_blocked=billing_blocked,
            billing_blocked_at=billing_blocked_at,
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
        )

        api_endpoints_user_me_response.additional_properties = d
        return api_endpoints_user_me_response

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
