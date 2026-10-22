from fastapi.testclient import TestClient

from backend.app import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_system_status():
    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json()["mode"] == "simulation"


def test_simulated_evaluation():
    response = client.post(
        "/api/evaluate",
        json={
            "test_category": "prompt_robustness",
            "simulated_outcome": "pass",
        },
    )

    assert response.status_code == 200
    assert response.json()["result"] == "PASS"
    assert response.json()["audit_hash"]


def test_flagged_evaluation():
    response = client.post(
        "/api/evaluate",
        json={
            "test_category": "policy_compliance",
            "simulated_outcome": "flag",
        },
    )

    assert response.status_code == 200
    assert response.json()["result"] == "REVIEW_REQUIRED"


def test_invalid_category_is_rejected():
    response = client.post(
        "/api/evaluate",
        json={
            "test_category": "invalid_category",
            "simulated_outcome": "pass",
        },
    )

    assert response.status_code == 422


def test_audit_chain_verification():
    client.post(
        "/api/evaluate",
        json={
            "test_category": "session_isolation",
            "simulated_outcome": "pass",
        },
    )

    response = client.get("/api/audit/verify")

    assert response.status_code == 200
    assert response.json()["valid"] is True
