# BAYORA Prototype Demonstration

## Objective

Demonstrate the evaluation workflow, policy outcomes, and audit
verification available in the current prototype.

## Demonstration Steps

### Step 1: Start the Backend

Run the setup instructions in docs/setup.md.

### Step 2: Open the Dashboard

Open frontend/index.html in a browser.

### Step 3: Check Backend Connectivity

Click Check Backend.

Expected result: the API reports a healthy status.

### Step 4: Run a Passing Simulation

Choose Prompt Robustness.

Choose Pass — demonstration case.

Click Run Simulated Evaluation.

Expected result: PASS and an audit hash are displayed.

### Step 5: Run a Flagged Simulation

Choose Policy Compliance.

Choose Flag for review.

Click Run Simulated Evaluation.

Expected result: REVIEW_REQUIRED.

### Step 6: Review Audit Events

Click View Audit Events.

The events recorded since the backend started should be displayed.

### Step 7: Verify the Audit Chain

Click Verify Audit Chain.

Expected result: the API reports whether the current event chain
passes its integrity checks.

## What the Demonstration Proves

It demonstrates a simulated evaluation API, request validation,
dashboard interaction, audit event creation, and hash-chain verification.

It does not prove real LLM safety, production tenant isolation,
or protection against every information-leakage attack.
