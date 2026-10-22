# BAYORA Residual Risk Register

Security controls require testing and do not guarantee perfect security.

| Risk | Current status | Next step |
|---|---|---|
| Cross-team leakage | Not validated | Implement tenant separation |
| Session contamination | Not validated | Add isolated sessions |
| Unauthorized API access | Authentication absent | Add authentication and authorization |
| Audit record loss | Logs are in memory | Add durable storage |
| Audit modification | Hash verification implemented | Add protected storage and signatures |
| Side-channel leakage | Not tested | Design dedicated security tests |
| Host compromise | Not addressed | Harden and monitor the host |
| LLM-specific vulnerabilities | No live LLM connected | Integrate an authorized test model |

## Limitations

The current prototype is a functional workflow demonstration, not a
production-ready multi-tenant security platform.

A passing simulated evaluation does not prove that an AI model is safe.

A valid hash chain does not prove that an event was truthful or that
an attacker could not replace the entire log.

## Future Improvements

1. Implement isolated execution environments.
2. Introduce authenticated users and scoped permissions.
3. Persist audit events securely.
4. Integrate a test LLM in an authorized environment.
5. Add reproducible security tests.
6. Measure latency and resource overhead.
7. Evaluate and report residual risks.
