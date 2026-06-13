from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class YouTubeChannelSummary(BaseModel):
    """Channel-level statistics from ``GET /v1/platforms/youtube/accounts/{id}/summary``.

    Models the ``YouTubeChannelSummaryResponse`` Go struct from ``types_youtube.go``.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str
    handle: str
    thumbnail_url: str
    subscriber_count: int
    view_count: int
    video_count: int
