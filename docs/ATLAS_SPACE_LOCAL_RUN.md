# ATLAS: SPACE Local Run Guide

ATLAS: SPACE has two public execution paths.

The browser page runs the deterministic mission core directly in the browser. The local API wraps the same core in a small Node.js HTTP service for engineering tests and integration experiments.

Neither path connects to real mission systems.

## Browser runtime

From the repository root, serve the `docs` directory with any static web server.

For example:

```bash
python -m http.server 8000 --directory docs
```

Then open:

```text
http://localhost:8000/atlas-space.html
```

The page provides three synthetic scenarios:

- orbital platform power and thermal conflict
- remote surface outpost logistics and robotics fault
- adversarial mission command injection

It also exposes secondary fault injection, self tests, evidence inspection, and protected authority tests.

## Node.js runtime tests

Run:

```bash
node tests/test_atlas_space_runtime.js
```

The test suite checks that normal bounded scenarios stabilize, protected actions fail closed, adversarial requests create a mission hold, secondary faults reduce authority, and exported mission packages use the expected schema.

## Local API

Start the reference server:

```bash
node tools/atlas-space-server.js
```

The default address is:

```text
http://localhost:8788
```

Health check:

```bash
curl http://localhost:8788/health
```

List scenarios:

```bash
curl http://localhost:8788/api/scenarios
```

Run a scenario:

```bash
curl -X POST http://localhost:8788/api/run \
  -H 'Content-Type: application/json' \
  -d '{"scenario":"orbital"}'
```

Test protected authority:

```bash
curl -X POST http://localhost:8788/api/protected \
  -H 'Content-Type: application/json' \
  -d '{"scenario":"orbital","tool":"space.human.eva.initiate"}'
```

The response should show a denied protected tool request and a final mission hold state.

## API smoke test

Run:

```bash
node tests/test_atlas_space_server.js
```

The smoke test starts the server on an ephemeral local port and checks the health, scenario, run, and protected-action endpoints.

## Production boundary

This local server is intentionally small.

A production space-operations system would require authenticated APIs, strict identity and authorization, durable state, qualified telemetry and control interfaces, cybersecurity controls, mission-specific safety engineering, verification and validation, configuration management, simulation, formal command permissions, observability, and accountable human approval.

Do not use the reference runtime as flight software or as a command path to physical mission systems.
