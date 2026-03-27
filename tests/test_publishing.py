from __future__ import annotations

from .conftest import BASE_URL

POST_JSON = {
    "id": "post_new_001",
    "text": "New post content",
    "status": "draft",
    "created_at": "2026-03-20T10:00:00Z",
    "updated_at": "2026-03-20T10:00:00Z",
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
        status_code=204,
    )
    client.posts.delete("post_new_001")


def test_retry_post(httpx_mock, client) -> None:
    retried = {**POST_JSON, "status": "publishing"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_new_001/retry",
        json=retried,
    )
    post = client.posts.retry("post_new_001")
    assert post.status == "publishing"


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


def test_get_constraints(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/validate",
        json={
            "data": {
                "instagram": {"max_text_length": 2200, "max_images": 10, "supports_scheduling": True},
                "linkedin": {"max_text_length": 3000, "max_images": 9},
            }
        },
    )
    constraints = client.publishing.get_constraints()
    assert "instagram" in constraints
    assert constraints["instagram"].max_text_length == 2200
    assert constraints["instagram"].platform == "instagram"
    assert "linkedin" in constraints
    assert constraints["linkedin"].max_text_length == 3000


def test_get_upload_url(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/upload-url?content_type=image%2Fjpeg&filename=photo.jpg",
        json={
            "media_id": "media_001",
            "upload_url": "https://storage.example.com/presigned/abc123",
            "expires_at": "2026-03-20T11:00:00Z",
        },
    )
    result = client.publishing.get_upload_url(media_type="image/jpeg", filename="photo.jpg")
    assert result.media_id == "media_001"
    assert result.upload_url.startswith("https://storage.example.com")


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


async def test_get_constraints_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/validate",
        json={
            "data": {
                "instagram": {"max_text_length": 2200, "max_images": 10},
            }
        },
    )
    constraints = await async_client.publishing.get_constraints()
    assert "instagram" in constraints
    assert constraints["instagram"].max_text_length == 2200


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


async def test_get_upload_url_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/upload-url?content_type=image%2Fpng&filename=pic.png",
        json={
            "media_id": "media_002",
            "upload_url": "https://storage.example.com/presigned/xyz",
            "expires_at": "2026-03-20T12:00:00Z",
        },
    )
    result = await async_client.publishing.get_upload_url(media_type="image/png", filename="pic.png")
    assert result.media_id == "media_002"


async def test_verify_upload_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/media_001/verify",
        status_code=204,
    )
    await async_client.publishing.verify_upload("media_001")
