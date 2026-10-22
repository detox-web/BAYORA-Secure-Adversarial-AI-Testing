# BAYORA Setup Instructions

## Prerequisites

- Python 3.10 or newer
- GitHub repository access
- A modern web browser

## 1. Download the Project

Clone the repository:

    git clone https://github.com/YOUR-USERNAME/BAYORA-Secure-Adversarial-AI-Testing.git

Enter the project directory:

    cd BAYORA-Secure-Adversarial-AI-Testing

Replace YOUR-USERNAME with the actual GitHub username.

Alternatively, download the repository as a ZIP file from GitHub and
extract it.

## 2. Create a Virtual Environment

Windows:

    py -m venv .venv
    .venv\Scripts\activate

macOS/Linux:

    python3 -m venv .venv
    source .venv/bin/activate

## 3. Install Dependencies

    python -m pip install -r requirements.txt

## 4. Start the Backend

From the repository root directory, run:

    python -m uvicorn backend.app:app --reload

The API should be available at:

    http://127.0.0.1:8000

API documentation:

    http://127.0.0.1:8000/docs

## 5. Open the Dashboard

Open frontend/index.html in your web browser.

Keep the backend terminal running while using the dashboard.

## 6. Run Automated Tests

Open another terminal in the project directory, activate the virtual
environment, and run:

    python -m pytest -q

## 7. Test Audit Verification

Run an evaluation from the dashboard.

Then select Verify Audit Chain.

The API should report whether the in-memory hash-linked events pass
the implemented verification checks.

## Important Limitations

- Evaluation outcomes are simulated.
- No real LLM is connected.
- Audit events are stored in memory.
- Restarting the backend clears the audit events.
- Docker isolation and production security controls are not yet
  implemented.
