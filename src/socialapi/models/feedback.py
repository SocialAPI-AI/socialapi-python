from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class SendFeedbackRequest(BaseModel):
    """Request body for ``POST /v1/feedback``."""

    model_config = ConfigDict(populate_by_name=True)

    type: str
    message: str
