from __future__ import annotations

from typing import TYPE_CHECKING

from .conftest import BASE_URL

if TYPE_CHECKING:
    from socialapi import AsyncSocialAPI, SocialAPI

# Real ExportsListResponse shape from Go: envelope key is "exports" not "data"
# Real ExportItem fields: id, account_id, platform, status, total_videos, processed_videos,
#   error (omitempty), created_at, completed_at (omitempty), expires_at
# Real ExportStatusResponse fields: same plus result: {excel_url?, report_url?}
# No flat download_url, no flat report_url, no progress

EXPORT_ITEM_JSON = {
    "id": "exp_001",
    "account_id": "acc_tiktok_1",
    "platform": "tiktok",
    "status": "completed",
    "total_videos": 42,
    "processed_videos": 42,
    "created_at": "2026-05-01T10:00:00Z",
    "expires_at": "2026-06-01T10:00:00Z",
    "completed_at": "2026-05-01T11:00:00Z",
}

EXPORT_STATUS_JSON = {
    "id": "exp_001",
    "account_id": "acc_tiktok_1",
    "platform": "tiktok",
    "status": "completed",
    "total_videos": 42,
    "processed_videos": 42,
    "created_at": "2026-05-01T10:00:00Z",
    "expires_at": "2026-06-01T10:00:00Z",
    "completed_at": "2026-05-01T11:00:00Z",
    "result": {
        "excel_url": "https://example.com/exports/exp_001.xlsx",
        "report_url": "https://example.com/reports/token_abc",
    },
}

EXPORT_WITH_ERROR_JSON = {
    "id": "exp_002",
    "account_id": "acc_tiktok_2",
    "platform": "tiktok",
    "status": "failed",
    "total_videos": 0,
    "processed_videos": 0,
    "created_at": "2026-05-02T10:00:00Z",
    "expires_at": "2026-06-02T10:00:00Z",
    "error": "platform rate limit exceeded",
}


def test_exports_list(httpx_mock, client: SocialAPI) -> None:
    """list() reads the 'exports' envelope key, not 'data'."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports",
        json={"exports": [EXPORT_ITEM_JSON]},
    )
    exports = client.exports.list()
    assert len(exports) == 1
    assert exports[0].id == "exp_001"
    assert exports[0].status == "completed"


def test_exports_list_new_fields(httpx_mock, client: SocialAPI) -> None:
    """New fields platform, total_videos, processed_videos, expires_at are parsed."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports",
        json={"exports": [EXPORT_ITEM_JSON]},
    )
    exports = client.exports.list()
    e = exports[0]
    assert e.platform == "tiktok"
    assert e.total_videos == 42
    assert e.processed_videos == 42
    assert e.expires_at is not None


def test_exports_list_with_error_field(httpx_mock, client: SocialAPI) -> None:
    """Export with error field parses correctly."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports",
        json={"exports": [EXPORT_WITH_ERROR_JSON]},
    )
    exports = client.exports.list()
    assert len(exports) == 1
    assert exports[0].error == "platform rate limit exceeded"


def test_exports_list_with_status_filter(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports?status=completed",
        json={"exports": []},
    )
    exports = client.exports.list(status="completed")
    assert exports == []


def test_exports_get(httpx_mock, client: SocialAPI) -> None:
    """GET /v1/exports/{id} returns nested result object."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001",
        json=EXPORT_STATUS_JSON,
    )
    export = client.exports.get("exp_001")
    assert export.status == "completed"
    assert export.result is not None
    assert export.result.excel_url == "https://example.com/exports/exp_001.xlsx"
    assert export.result.report_url == "https://example.com/reports/token_abc"
    # spurious flat fields must NOT exist
    assert not hasattr(export, "download_url") or export.download_url is None  # type: ignore[union-attr]
    assert not hasattr(export, "progress") or export.progress is None  # type: ignore[union-attr]


def test_exports_get_no_result(httpx_mock, client: SocialAPI) -> None:
    """GET /v1/exports/{id} without result (not completed) parses correctly."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_002",
        json={
            "id": "exp_002",
            "account_id": "acc_tiktok_2",
            "platform": "tiktok",
            "status": "processing",
            "total_videos": 10,
            "processed_videos": 3,
            "created_at": "2026-05-02T10:00:00Z",
            "expires_at": "2026-06-02T10:00:00Z",
        },
    )
    export = client.exports.get("exp_002")
    assert export.status == "processing"
    assert export.result is None


def test_exports_list_videos(httpx_mock, client: SocialAPI) -> None:
    """list_videos must hit /v1/exports/{id}/videos (with /v1 prefix)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001/videos",
        json={"data": [{"id": "v_1", "url": "https://cdn/v.mp4"}]},
    )
    videos = client.exports.list_videos("exp_001")
    assert len(videos) == 1
    assert videos[0].url == "https://cdn/v.mp4"


def test_export_refresh_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001",
        json={
            "id": "exp_001",
            "account_id": "acc_tiktok_1",
            "platform": "tiktok",
            "status": "processing",
            "total_videos": 10,
            "processed_videos": 3,
            "created_at": "2026-05-01T10:00:00Z",
            "expires_at": "2026-06-01T10:00:00Z",
        },
    )
    export = client.exports.get("exp_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001",
        json=EXPORT_STATUS_JSON,
    )
    refreshed = export.refresh()
    assert refreshed.status == "completed"


def test_export_list_videos_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    """Bound Export.list_videos must also use /v1/exports/{id}/videos."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001",
        json={
            "id": "exp_001",
            "account_id": "acc_tiktok_1",
            "platform": "tiktok",
            "status": "completed",
            "total_videos": 1,
            "processed_videos": 1,
            "created_at": "2026-05-01T10:00:00Z",
            "expires_at": "2026-06-01T10:00:00Z",
        },
    )
    export = client.exports.get("exp_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001/videos",
        json={"data": [{"id": "v_1", "url": "https://cdn/v.mp4"}]},
    )
    videos = export.list_videos()
    assert len(videos) == 1
    assert videos[0].url == "https://cdn/v.mp4"


def test_create_export_request_defaults() -> None:
    """CreateExportRequest defaults must be False (not None) per Go plain bool."""
    from socialapi import CreateExportRequest

    req = CreateExportRequest()
    assert req.include_transcript is False
    assert req.include_vision is False


async def test_exports_list_async(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports",
        json={"exports": [EXPORT_ITEM_JSON]},
    )
    exports = await async_client.exports.list()
    assert len(exports) == 1
    assert exports[0].id == "exp_001"


async def test_exports_list_videos_async(httpx_mock, async_client: AsyncSocialAPI) -> None:
    """Async list_videos must also use /v1/ prefix."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001/videos",
        json={"data": [{"id": "v_1", "url": "https://cdn/v.mp4"}]},
    )
    videos = await async_client.exports.list_videos("exp_001")
    assert len(videos) == 1
    assert videos[0].url == "https://cdn/v.mp4"
