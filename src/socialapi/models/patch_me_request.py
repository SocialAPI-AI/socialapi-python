from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_me_request_signup_metadata import PatchMeRequestSignupMetadata


T = TypeVar("T", bound="PatchMeRequest")


@_attrs_define
class PatchMeRequest:
    """
    Attributes:
        job_role (str | Unset): JobRole records what best describes the user. Surrounding whitespace is
            trimmed, an empty value leaves the current one unchanged, and values
            longer than 120 characters are truncated. Example: Founder / CEO.
        lock_accounts_to_brand (bool | Unset): LockAccountsToBrand toggles whether a social account already connected to
            one brand may be re-connected (moved) to a different brand. When true, such
            a connect attempt is rejected with 409 account.already_linked. Example: True.
        onboarding (bool | Unset):  Example: False.
        referral (str | Unset):  Example: Google search.
        signup_metadata (PatchMeRequestSignupMetadata | Unset): SignupMetadata adds keys to the signup answers on
            record: a shallow
            merge, so keys sent replace the same keys and others are kept. At most
            4096 bytes once encoded.
        use_case (str | Unset):  Example: Managing my own brand's social accounts.
    """

    job_role: str | Unset = UNSET
    lock_accounts_to_brand: bool | Unset = UNSET
    onboarding: bool | Unset = UNSET
    referral: str | Unset = UNSET
    signup_metadata: PatchMeRequestSignupMetadata | Unset = UNSET
    use_case: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_role = self.job_role

        lock_accounts_to_brand = self.lock_accounts_to_brand

        onboarding = self.onboarding

        referral = self.referral

        signup_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signup_metadata, Unset):
            signup_metadata = self.signup_metadata.to_dict()

        use_case = self.use_case

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_role is not UNSET:
            field_dict["job_role"] = job_role
        if lock_accounts_to_brand is not UNSET:
            field_dict["lock_accounts_to_brand"] = lock_accounts_to_brand
        if onboarding is not UNSET:
            field_dict["onboarding"] = onboarding
        if referral is not UNSET:
            field_dict["referral"] = referral
        if signup_metadata is not UNSET:
            field_dict["signup_metadata"] = signup_metadata
        if use_case is not UNSET:
            field_dict["use_case"] = use_case

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_me_request_signup_metadata import PatchMeRequestSignupMetadata  # noqa: PLC0415

        d = dict(src_dict)
        job_role = d.pop("job_role", UNSET)

        lock_accounts_to_brand = d.pop("lock_accounts_to_brand", UNSET)

        onboarding = d.pop("onboarding", UNSET)

        referral = d.pop("referral", UNSET)

        _signup_metadata = d.pop("signup_metadata", UNSET)
        signup_metadata: PatchMeRequestSignupMetadata | Unset
        if isinstance(_signup_metadata, Unset):
            signup_metadata = UNSET
        else:
            signup_metadata = PatchMeRequestSignupMetadata.from_dict(_signup_metadata)

        use_case = d.pop("use_case", UNSET)

        patch_me_request = cls(
            job_role=job_role,
            lock_accounts_to_brand=lock_accounts_to_brand,
            onboarding=onboarding,
            referral=referral,
            signup_metadata=signup_metadata,
            use_case=use_case,
        )

        patch_me_request.additional_properties = d
        return patch_me_request

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
