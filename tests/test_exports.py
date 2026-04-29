from __future__ import annotations

from typing import TYPE_CHECKING

from .conftest import BASE_URL

if TYPE_CHECKING:
    from socialapi import AsyncSocialAPI, SocialAPI


def test_exports_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports",
        json={"data": [{"id": "exp_001", "status": "completed"}]},
    )
    exports = client.exports.list()
    assert len(exports) == 1
    assert exports[0].id == "exp_001"
    assert exports[0].status == "completed"


def test_exports_list_with_status_filter(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports?status=completed",
        json={"data": []},
    )
    exports = client.exports.list(status="completed")
    assert exports == []


def test_exports_get(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001",
        json={
            "id": "exp_001",
            "status": "completed",
            "progress": 1.0,
            "download_url": "https://example.com/exports/exp_001.xlsx",
        },
    )
    export = client.exports.get("exp_001")
    assert export.status == "completed"
    assert export.download_url is not None


def test_exports_list_videos(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/exports/exp_001/videos",
        json={"data": [{"id": "v_1", "url": "https://cdn/v.mp4"}]},
    )
    videos = client.exports.list_videos("exp_001")
    assert len(videos) == 1
    assert videos[0].url == "https://cdn/v.mp4"


def test_export_refresh_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001",
        json={"id": "exp_001", "status": "processing", "progress": 0.5},
    )
    export = client.exports.get("exp_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports/exp_001",
        json={"id": "exp_001", "status": "completed", "progress": 1.0},
    )
    refreshed = export.refresh()
    assert refreshed.status == "completed"


async def test_exports_list_async(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/exports",
        json={"data": [{"id": "exp_001", "status": "completed"}]},
    )
    exports = await async_client.exports.list()
    assert len(exports) == 1
    assert exports[0].id == "exp_001"
