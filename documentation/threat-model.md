# BAYORA Threat Model

## Purpose

Identify risks that may affect the confidentiality, integrity, and
reliability of adversarial AI safety evaluations.

## Threats

### T1: Cross-Team Information Leakage

Risk: Red-Team test information may be exposed to the Blue Team.

Control goal: Separate tenant data and restrict information sharing.

Status: Not yet validated in the current simulation.

### T2: Cross-Session Contamination

Risk: One evaluation may affect another evaluation.

Control goal: Use independent sessions and isolated model state.

Status: Dedicated production-grade session isolation is future work.

### T3: Unauthorized Access

Risk: A user may attempt to access an unauthorized operation.

Control goal: Add authenticated identities and least-privilege access.

Status: Authentication and production authorization are not implemented.

### T4: Audit Tampering

Risk: Evaluation records may be modified.

Control goal: Verify hash-linked event records.

Status: In-memory hash-chain verification is implemented. Durable storage
and externally protected audit evidence are future work.

### T5: Side-Channel Leakage

Risk: Timing and resource behaviour may reveal sensitive information.

Control goal: Conduct dedicated side-channel testing and apply
appropriate isolation controls.

Status: Not tested in the current prototype.

## Testing Approach

- Validate API input.
- Test evaluation outcomes.
- Verify audit hash links.
- Document unimplemented security controls.
