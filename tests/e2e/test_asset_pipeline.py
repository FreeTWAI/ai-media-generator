import os
import time
import requests
import hashlib
import pytest

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8080")

@pytest.fixture(scope="session")
def api_client():
    with requests.Session() as session:
        yield session

def test_task_polling_lifecycle(api_client):
    # Dispatch task
    response = api_client.post(f"{BASE_URL}/api/v1/tasks/dispatch", json={"asset_id": "test_asset_123"})
    assert response.status_code == 202
    task_data = response.json()
    task_id = task_data.get("task_id")
    assert task_id is not None

    # Poll task status
    max_retries = 10
    status = "PENDING"
    for _ in range(max_retries):
        resp = api_client.get(f"{BASE_URL}/api/v1/tasks/{task_id}/status")
        assert resp.status_code == 200
        status = resp.json().get("status")
        if status == "COMPLETED":
            break
        time.sleep(1)

    assert status == "COMPLETED"

def test_partial_chunk_downloads(api_client):
    asset_id = "test_asset_123"

    # Download first chunk
    headers = {"Range": "bytes=0-1023"}
    response = api_client.get(f"{BASE_URL}/api/v1/assets/{asset_id}/download", headers=headers)
    assert response.status_code == 206
    assert len(response.content) <= 1024

    # Download second chunk
    headers = {"Range": "bytes=1024-2047"}
    response = api_client.get(f"{BASE_URL}/api/v1/assets/{asset_id}/download", headers=headers)
    assert response.status_code == 206
    assert len(response.content) <= 1024

def _verify_checksum(api_client, asset_id):
    # Get asset metadata for expected checksum
    meta_resp = api_client.get(f"{BASE_URL}/api/v1/assets/{asset_id}/metadata")
    assert meta_resp.status_code == 200
    expected_checksum = meta_resp.json().get("checksum_sha256")
    assert expected_checksum is not None

    # Download full asset in chunks to optimize memory allocation
    response = api_client.get(f"{BASE_URL}/api/v1/assets/{asset_id}/download", stream=True)
    assert response.status_code == 200

    # Verify checksum
    sha256 = hashlib.sha256()
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            sha256.update(chunk)
    actual_checksum = sha256.hexdigest()
    assert actual_checksum == expected_checksum
    return actual_checksum

def test_checksum_verification(api_client):
    _verify_checksum(api_client, "test_asset_123")

def test_checksum_verification_benchmark(benchmark, api_client):
    benchmark(_verify_checksum, api_client, "test_asset_123")
