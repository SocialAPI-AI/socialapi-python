from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict, PrivateAttr

from socialapi._exceptions import SocialAPIError

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


def _empty_ctx() -> dict[str, Any]:
    return {}


class UnboundModelError(SocialAPIError):
    """Raised when an action method is called on a model not bound to a client.

    Models constructed via ``Model.model_validate(...)`` or ``Model(**fields)``
    have no client reference. Such instances are pure data objects -- to perform
    an action, either fetch the model through a client (e.g.
    ``client.comments.list(...)``) or call the resource-level method directly
    (e.g. ``client.comments.reply(...)``).
    """


class MissingContextError(SocialAPIError):
    """Raised when a bound action requires a context key that wasn't seeded."""


class _Bound(BaseModel):
    """Base class for domain models that can carry a client + context.

    Two private attributes hold runtime-only state that is *not* serialized:

    * ``_client``: the underlying ``BaseSyncClient`` or ``BaseAsyncClient`` that
      built this instance, or ``None`` for raw / user-constructed models.
    * ``_ctx``: a dict of contextual identifiers (e.g. ``account_id``,
      ``inbox_post_id``) that bound action methods need but the model itself
      may not expose as fields.
    """

    model_config = ConfigDict(populate_by_name=True)

    _client: Any = PrivateAttr(default=None)
    _ctx: dict[str, Any] = PrivateAttr(default_factory=_empty_ctx)

    def _bind(self, client: Any, ctx: dict[str, Any] | None = None) -> None:
        """Attach a client and contextual identifiers to this instance.

        Called by resource methods when constructing models from API responses.
        Not part of the public API.
        """
        self._client = client
        if ctx:
            new_ctx: dict[str, Any] = dict(ctx)
            self._ctx = new_ctx

    def _client_or_raise_sync(self) -> BaseSyncClient:
        """Return the bound sync client or raise ``UnboundModelError``."""
        from socialapi._base_client import BaseSyncClient

        if self._client is None:
            msg = (
                f"{type(self).__name__} is not bound to a client. "
                f"Either retrieve it through a client (e.g. client.<resource>.list(...)) "
                f"or call the resource-level method directly."
            )
            raise UnboundModelError(msg)
        if not isinstance(self._client, BaseSyncClient):
            msg = (
                f"{type(self).__name__} is bound to an async client; "
                f"use the awaitable variant of this method or the corresponding Async* model."
            )
            raise UnboundModelError(msg)
        return self._client

    def _client_or_raise_async(self) -> BaseAsyncClient:
        """Return the bound async client or raise ``UnboundModelError``."""
        from socialapi._base_client import BaseAsyncClient

        if self._client is None:
            msg = (
                f"{type(self).__name__} is not bound to a client. "
                f"Either retrieve it through a client (e.g. client.<resource>.list(...)) "
                f"or call the resource-level method directly."
            )
            raise UnboundModelError(msg)
        if not isinstance(self._client, BaseAsyncClient):
            msg = (
                f"{type(self).__name__} is bound to a sync client; "
                f"use the synchronous variant of this method or the corresponding non-Async model."
            )
            raise UnboundModelError(msg)
        return self._client

    def _ctx_value(self, key: str) -> str:
        """Return ``self._ctx[key]`` or raise ``MissingContextError``."""
        value = self._ctx.get(key)
        if value is None:
            msg = (
                f"{type(self).__name__}.{key} is required for this action but was not seeded "
                f"by the resource. Use the resource-level method directly and pass {key} explicitly."
            )
            raise MissingContextError(msg)
        return str(value)


def bind_one(
    model_cls: type[Any],
    raw: dict[str, Any],
    *,
    client: Any,
    ctx: dict[str, Any] | None = None,
) -> Any:
    """Validate raw JSON into ``model_cls`` and attach client + ctx."""
    obj = model_cls.model_validate(raw)
    if isinstance(obj, _Bound):
        obj._bind(client, ctx)
    return obj


def bind_many(
    model_cls: type[Any],
    raw_list: list[dict[str, Any]],
    *,
    client: Any,
    ctx: dict[str, Any] | None = None,
) -> list[Any]:
    """Validate a list of raw items and attach client + ctx to each."""
    return [bind_one(model_cls, raw, client=client, ctx=ctx) for raw in raw_list]
