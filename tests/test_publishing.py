from __future__ import annotations

from .conftest import BASE_URL

POST_JSON = {
    "id": "post_new_001",
    "text": "New post content",
    "status": "draft",
    "created_at": "2026-03-20T10:00:00Z",
    "updated_at": "2026-03-20T10:00:00Z",
}

# Wire shape: nested constraints as returned by GET /v1/posts/validate
CONSTRAINTS_JSON = {
    "data": {
        "instagram": {
            "text": {
                "max_length": 2200,
                "max_hashtags": 30,
                "max_mentions": 20,
                "counting_mode": "chars",
            },
            "media": {
                "max_image_size_bytes": 8388608,
                "max_video_size_bytes": 314572800,
                "max_video_duration_sec": 900,
                "min_video_duration_sec": 3,
                "max_video_fps": 0,
                "supported_image_types": ["image/jpeg"],
                "supported_video_types": ["video/mp4", "video/quicktime"],
            },
            "carousel": {
                "supported": True,
                "min_items": 2,
                "max_items": 10,
                "allow_video": True,
                "images_only": False,
                "photos_only": False,
            },
        },
        "linkedin": {
            "text": {
                "max_length": 3000,
                "max_hashtags": 0,
                "max_mentions": 0,
                "counting_mode": "chars",
            },
            "media": {
                "max_image_size_bytes": 10485760,
                "max_video_size_bytes": 524288000,
                "max_video_duration_sec": 1800,
                "min_video_duration_sec": 3,
                "max_video_fps": 30,
                "supported_image_types": ["image/jpeg", "image/png", "image/gif"],
                "supported_video_types": ["video/mp4"],
            },
            "carousel": {
                "supported": True,
                "min_items": 2,
                "max_items": 20,
                "allow_video": False,
                "images_only": True,
                "photos_only": False,
            },
        },
    }
}


def test_create_post(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json=POST_JSON,
    )
    post = client.publishing.create(text="New post content")
    assert post.id == "post_new_001"
    assert post.text == "New post content"
    assert post.status == "draft"

    request = httpx_mock.get_requests()[0]
    assert request.method == "POST"
    import json

    body = json.loads(request.content)
    assert body["text"] == "New post content"


def test_update_post(httpx_mock, client) -> None:
    updated = {**POST_JSON, "text": "Updated content"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_new_001",
        json=updated,
    )
    post = client.publishing.update("post_new_001", text="Updated content")
    assert post.text == "Updated content"


def test_delete_post(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_new_001",
        json={"success": True, "deleted": True, "results": []},
    )
    client.posts.delete("post_new_001")


def test_retry_post(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_new_001/retry",
        json={"success": True},
    )
    result = client.posts.retry("post_new_001")
    assert result is None


def test_validate_post(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/validate",
        json={
            "valid": True,
            "errors": [],
            "warnings": [{"platform": "instagram", "field": "text", "message": "Consider adding hashtags"}],
        },
    )
    result = client.publishing.validate(text="My post")
    assert result.valid is True
    assert len(result.errors) == 0
    assert len(result.warnings) == 1
    assert result.warnings[0].platform == "instagram"


def test_get_constraints_nested_shape(httpx_mock, client) -> None:
    """get_constraints() parses nested wire shape (text/media/carousel sub-objects)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/validate",
        json=CONSTRAINTS_JSON,
    )
    constraints = client.publishing.get_constraints()
    assert "instagram" in constraints
    ig = constraints["instagram"]
    assert ig.text.max_length == 2200
    assert ig.text.max_hashtags == 30
    assert ig.text.counting_mode == "chars"
    assert ig.media.max_image_size_bytes == 8388608
    assert ig.media.supported_image_types == ["image/jpeg"]
    assert ig.carousel.supported is True
    assert ig.carousel.max_items == 10

    assert "linkedin" in constraints
    li = constraints["linkedin"]
    assert li.text.max_length == 3000
    assert li.media.max_video_fps == 30
    assert li.carousel.images_only is True


def test_get_upload_url_sends_media_type_param(httpx_mock, client) -> None:
    """get_upload_url() must send media_type (not content_type) as query param."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/upload-url?media_type=image%2Fjpeg&filename=photo.jpg",
        json={
            "media_id": "media_001",
            "upload_url": "https://storage.example.com/presigned/abc123",
            "expires_at": "2026-03-20T11:00:00Z",
        },
    )
    result = client.publishing.get_upload_url(media_type="image/jpeg", filename="photo.jpg")
    assert result.media_id == "media_001"
    assert result.upload_url.startswith("https://storage.example.com")
    # Confirm the param name sent
    req = httpx_mock.get_requests()[0]
    assert "media_type=image" in str(req.url)
    assert "content_type" not in str(req.url)


def test_import_posts_multipart(httpx_mock, client) -> None:
    """import_posts() must send multipart/form-data with a 'file' field."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/import",
        json={"total_rows": 2, "created": 2, "failed": 0, "errors": [], "posts": []},
    )
    csv_bytes = b"text,title\nHello world,My Title\nSecond post,Another"
    result = client.publishing.import_posts(file=csv_bytes, filename="posts.csv")
    assert result.total_rows == 2
    assert result.created == 2

    req = httpx_mock.get_requests()[0]
    content_type = req.headers.get("content-type", "")
    assert "multipart/form-data" in content_type
    assert b"posts.csv" in req.content


def test_import_posts_dry_run(httpx_mock, client) -> None:
    """import_posts(dry_run=True) passes dry_run=true as query param."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/import?dry_run=true",
        json={"total_rows": 1, "created": 0, "failed": 0, "errors": [], "posts": []},
    )
    csv_bytes = b"text\nHello world"
    result = client.publishing.import_posts(file=csv_bytes, filename="posts.csv", dry_run=True)
    assert result.total_rows == 1

    req = httpx_mock.get_requests()[0]
    assert "dry_run=true" in str(req.url)


def test_create_post_with_all_options(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json=POST_JSON,
    )
    post = client.publishing.create(
        text="New post content",
        title="My Title",
        media_ids=["media_001"],
        visibility="public",
        first_comment="First!",
        scheduled_at="2026-04-01T12:00:00Z",
        publish_now=True,
        skip_duplicate_check=True,
        targets=[{"account_id": "acc_ig_001", "platform": "instagram"}],
    )
    assert post.id == "post_new_001"

    import json

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["title"] == "My Title"
    assert body["media_ids"] == ["media_001"]
    assert body["visibility"] == "public"
    assert body["first_comment"] == "First!"
    assert body["scheduled_at"] == "2026-04-01T12:00:00Z"
    assert body["publish_now"] is True
    assert body["skip_duplicate_check"] is True
    assert body["targets"] == [{"account_id": "acc_ig_001", "platform": "instagram"}]


def test_update_post_with_all_options(httpx_mock, client) -> None:
    updated = {**POST_JSON, "text": "Updated", "hidden": True}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_new_001",
        json=updated,
    )
    post = client.publishing.update(
        "post_new_001",
        text="Updated",
        title="New Title",
        media_ids=["m1"],
        visibility="private",
        first_comment="Comment",
        scheduled_at="2026-04-02T00:00:00Z",
        hidden=True,
        targets=[{"account_id": "acc_1"}],
    )
    assert post.id == "post_new_001"

    import json

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["text"] == "Updated"
    assert body["title"] == "New Title"
    assert body["media_ids"] == ["m1"]
    assert body["visibility"] == "private"
    assert body["first_comment"] == "Comment"
    assert body["scheduled_at"] == "2026-04-02T00:00:00Z"
    assert body["hidden"] is True
    assert body["targets"] == [{"account_id": "acc_1"}]


def test_validate_post_with_all_options(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/validate",
        json={"valid": True, "errors": [], "warnings": []},
    )
    result = client.publishing.validate(
        text="Check me",
        platforms=["instagram", "linkedin"],
        account_ids=["acc_1"],
        media_ids=["m1"],
        scheduled_at="2026-04-01T00:00:00Z",
        targets=[{"platform": "instagram"}],
    )
    assert result.valid is True

    import json

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["platforms"] == ["instagram", "linkedin"]
    assert body["account_ids"] == ["acc_1"]
    assert body["media_ids"] == ["m1"]
    assert body["scheduled_at"] == "2026-04-01T00:00:00Z"
    assert body["targets"] == [{"platform": "instagram"}]


def test_verify_upload(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/media_001/verify",
        status_code=204,
    )
    client.publishing.verify_upload("media_001")


def test_target_request_has_page_id() -> None:
    """TargetRequest model must accept page_id field."""
    from socialapi.models.publishing import TargetRequest

    tr = TargetRequest(account_id="acc_001", page_id="sapi_page_001")
    assert tr.page_id == "sapi_page_001"


def test_target_request_page_id_optional() -> None:
    """TargetRequest page_id is optional."""
    from socialapi.models.publishing import TargetRequest

    tr = TargetRequest(account_id="acc_001")
    assert tr.page_id is None


async def test_create_post_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json=POST_JSON,
    )
    post = await async_client.publishing.create(text="New post content")
    assert post.id == "post_new_001"


async def test_create_post_async_with_options(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json=POST_JSON,
    )
    post = await async_client.publishing.create(
        text="New post content",
        title="Title",
        media_ids=["m1"],
        visibility="public",
        first_comment="Hi",
        scheduled_at="2026-04-01T00:00:00Z",
        publish_now=True,
        skip_duplicate_check=True,
        targets=[{"platform": "instagram"}],
    )
    assert post.id == "post_new_001"


async def test_update_post_async(httpx_mock, async_client) -> None:
    updated = {**POST_JSON, "text": "Async updated"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_new_001",
        json=updated,
    )
    post = await async_client.publishing.update(
        "post_new_001",
        text="Async updated",
        title="T",
        media_ids=["m1"],
        visibility="private",
        first_comment="C",
        scheduled_at="2026-05-01T00:00:00Z",
        hidden=True,
        targets=[{"platform": "linkedin"}],
    )
    assert post.text == "Async updated"


async def test_get_constraints_nested_shape_async(httpx_mock, async_client) -> None:
    """get_constraints() parses nested wire shape (async)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/validate",
        json=CONSTRAINTS_JSON,
    )
    constraints = await async_client.publishing.get_constraints()
    assert "instagram" in constraints
    ig = constraints["instagram"]
    assert ig.text.max_length == 2200
    assert ig.media.max_image_size_bytes == 8388608
    assert ig.carousel.supported is True


async def test_validate_post_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/validate",
        json={
            "valid": False,
            "errors": [{"platform": "instagram", "field": "text", "message": "Too long"}],
            "warnings": [],
        },
    )
    result = await async_client.publishing.validate(
        text="x" * 5000,
        platforms=["instagram"],
        account_ids=["acc_1"],
        media_ids=["m1"],
        scheduled_at="2026-04-01T00:00:00Z",
        targets=[{"platform": "instagram"}],
    )
    assert result.valid is False
    assert len(result.errors) == 1


async def test_get_upload_url_sends_media_type_param_async(httpx_mock, async_client) -> None:
    """get_upload_url() must send media_type (not content_type) as query param (async)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/upload-url?media_type=image%2Fpng&filename=pic.png",
        json={
            "media_id": "media_002",
            "upload_url": "https://storage.example.com/presigned/xyz",
            "expires_at": "2026-03-20T12:00:00Z",
        },
    )
    result = await async_client.publishing.get_upload_url(media_type="image/png", filename="pic.png")
    assert result.media_id == "media_002"
    req = httpx_mock.get_requests()[0]
    assert "media_type=image" in str(req.url)
    assert "content_type" not in str(req.url)


async def test_import_posts_multipart_async(httpx_mock, async_client) -> None:
    """import_posts() must send multipart/form-data (async)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/import",
        json={"total_rows": 1, "created": 1, "failed": 0, "errors": [], "posts": []},
    )
    csv_bytes = b"text\nHello world"
    result = await async_client.publishing.import_posts(file=csv_bytes, filename="posts.csv")
    assert result.total_rows == 1

    req = httpx_mock.get_requests()[0]
    content_type = req.headers.get("content-type", "")
    assert "multipart/form-data" in content_type


async def test_verify_upload_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/media_001/verify",
        status_code=204,
    )
    await async_client.publishing.verify_upload("media_001")
