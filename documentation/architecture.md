# BAYORA System Architecture

## 1. Overview

BAYORA is a prototype for secure adversarial AI safety evaluation.

The current implementation demonstrates an evaluation API, simulated
Red-Team and Blue-Team workflow, and hash-linked audit events.

## 2. Architecture Components

### Red-Team Tenant

Represents the source of authorized test requests.

### Control Plane

Represents policy-controlled configuration and evaluation management.

### Evaluation Broker

The API acts as a prototype boundary for receiving evaluation requests.

### Model-Under-Test Zone

The current version simulates model evaluation. It does not connect
to a real LLM.

### Blue-Team Tenant

Represents a policy-review stage. The current outcome is selected
as demonstration input and is not a real safety classification.

### Evidence Plane

Stores evaluation events in an in-memory hash-linked audit log.

### Observability Plane

The current prototype exposes basic service status and audit endpoints.
Advanced privacy-preserving telemetry is future work.

## 3. Data Flow

1. The user selects a test category.
2. The dashboard submits a request to the API.
3. The API validates the request.
4. A simulated evaluation outcome is generated.
5. An audit event is created and hash-linked.
6. The result is displayed on the dashboard.
7. The audit endpoint verifies the event chain.

## 4. Implementation Status

Implemented in the prototype:
- API health endpoint
- Request validation
- Simulated evaluation
- In-memory hash-linked audit log
- Audit verification
- Interactive dashboard

Not yet implemented:
- Real multi-tenant isolation
- Hardened Docker sandbox
- Real LLM integration
- Production secrets management
- Network micro-segmentation
- Signed audit evidence
- Hardware side-channel protection
