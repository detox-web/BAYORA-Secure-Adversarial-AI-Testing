from datetime import datetime, timezone
from hashlib import sha256
from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(
    title="BAYORA",
    description=(
        "Prototype for secure adversarial AI safety evaluation."
    ),
    version="0.1.0",
)

# Allows the local dashboard to communicate with this API.
# This is for local development, not a production security policy.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

audit_events = []
previous_hash = "GENESIS"


class EvaluationRequest(BaseModel):
    test_category: str = Field(
        default="prompt_robustness",
        pattern="^(prompt_robustness|policy_compliance|session_isolation)$",
    )
    simulated_outcome: str = Field(
        default="pass",
        pattern="^(pass|flag)$",
    )


def record_audit_event(event_type: str, details: dict) -> dict:
    """Add an event to an in-memory hash-linked audit log."""
    global previous_hash

    event = {
        "event_id": str(uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "details": details,
        "previous_hash": previous_hash,
    }

    event_text = str(event).encode("utf-8")
    event_hash = sha256(event_text).hexdigest()
    event["event_hash"] = event_hash

    audit_events.append(event)
    previous_hash = event_hash

    return event


@app.get("/")
def home():
    return {
        "project": "BAYORA",
        "status": "running",
        "mode": "simulated_prototype",
    }


@app.get("/api/health")
def health():
    return {"status": "healthy"}


@app.get("/api/status")
def system_status():
    return {
        "red_team": "ready",
        "blue_team": "ready",
        "model_zone": "simulated",
        "evaluation_broker": "ready",
        "audit": "enabled",
        "mode": "simulation",
    }


@app.post("/api/evaluate")
def evaluate(request: EvaluationRequest):
    """Run a safe, simulated evaluation without calling a real LLM."""

    evaluation_id = str(uuid4())

    # Demonstration rule: a flagged test requires review.
    # This is not a real AI safety classifier.
    if request.simulated_outcome == "flag":
        result = "REVIEW_REQUIRED"
        risk_level = "MEDIUM"
        policy_status = "FLAGGED"
    else:
        result = "PASS"
        risk_level = "LOW"
        policy_status = "PASSED"

    event = record_audit_event(
        "evaluation_completed",
        {
            "evaluation_id": evaluation_id,
            "test_category": request.test_category,
            "result": result,
            "policy_status": policy_status,
        },
    )

    return {
        "evaluation_id": evaluation_id,
        "test_category": request.test_category,
        "result": result,
        "risk_level": risk_level,
        "policy_status": policy_status,
        "model_mode": "simulated",
        "audit_event_id": event["event_id"],
        "audit_hash": event["event_hash"],
        "message": (
            "Simulation completed. "
            "This result does not represent a real LLM assessment."
        ),
    }


@app.get("/api/audit")
def get_audit_events():
    return {
        "count": len(audit_events),
        "events": audit_events,
    }


@app.get("/api/audit/verify")
def verify_audit_chain():
    """Check the in-memory hash links for accidental modifications."""
    expected_previous_hash = "GENESIS"

    for event in audit_events:
        if event["previous_hash"] != expected_previous_hash:
            return {"valid": False}

        event_copy = {
            key: value
            for key, value in event.items()
            if key != "event_hash"
        }

        expected_hash = sha256(
            str(event_copy).encode("utf-8")
        ).hexdigest()

        if event["event_hash"] != expected_hash:
            return {"valid": False}

        expected_previous_hash = event["event_hash"]

    return {
        "valid": True,
        "verified_events": len(audit_events),
    }
