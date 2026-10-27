import os
import time
import requests
import hashlib
import pytest

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8080")

def test_task_polling_lifecycle():
    # Dispatch task
    response = requests.post(f"{BASE_URL}/api/v1/tasks/dispatch", json={"asset_id": "test_asset_123"})
    assert response.status_code == 202
    task_data = response.json()
    task_id = task_data.get("task_id")
    assert task_id is not None

    # Poll task status
    max_retries = 10
    status = "PENDING"
    for _ in range(max_retries):
        resp = requests.get(f"{BASE_URL}/api/v1/tasks/{task_id}/status")
        assert resp.status_code == 200
        status = resp.json().get("status")
        if status == "COMPLETED":
            break
        time.sleep(1)

    assert status == "COMPLETED"

def test_partial_chunk_downloads():
    asset_id = "test_asset_123"

    # Download first chunk
    headers = {"Range": "bytes=0-1023"}
    response = requests.get(f"{BASE_URL}/api/v1/assets/{asset_id}/download", headers=headers)
    assert response.status_code == 206
    assert len(response.content) <= 1024

    # Download second chunk
    headers = {"Range": "bytes=1024-2047"}
    response = requests.get(f"{BASE_URL}/api/v1/assets/{asset_id}/download", headers=headers)
    assert response.status_code == 206
    assert len(response.content) <= 1024

def test_checksum_verification():
    asset_id = "test_asset_123"

    # Get asset metadata for expected checksum
    meta_resp = requests.get(f"{BASE_URL}/api/v1/assets/{asset_id}/metadata")
    assert meta_resp.status_code == 200
    expected_checksum = meta_resp.json().get("checksum_sha256")
    assert expected_checksum is not None

    # Download full asset
    response = requests.get(f"{BASE_URL}/api/v1/assets/{asset_id}/download")
    assert response.status_code == 200

    # Verify checksum
    actual_checksum = hashlib.sha256(response.content).hexdigest()
    assert actual_checksum == expected_checksum
