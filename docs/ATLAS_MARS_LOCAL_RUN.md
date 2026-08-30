# ATLAS: MARS Developer Quick Start

ATLAS: MARS has two executable surfaces:

1. the public browser mission-control page
2. a local Node.js API that runs the same deterministic mission core outside the browser

The browser is the easiest way to experience the system. The local API is there for engineers who want to inspect the runtime more directly, call it programmatically, and verify that the mission logic is not only a visual animation.

The current implementation uses synthetic state throughout. It does not connect to real robots, habitats, spacecraft, telemetry, command systems, or production model providers.

## Requirements

You only need:

- Node.js 20 or later
- a local terminal

There are no npm packages to install for the runtime server or the included Node.js tests.

## Run the tests first

From the repository root, run:

```bash
node tests/test_atlas_mars_runtime.js
node tests/test_atlas_mars_server.js
```

The first test exercises the mission runtime directly.

The second test starts the local API on a temporary port, calls the service, creates a mission run, inspects its events, attempts a protected action, and verifies the exported mission package.

If both commands complete successfully, the core runtime and local API are behaving as expected for the current test set.

## Start the local mission API

Run:

```bash
node tools/atlas-mars-server.js
```

By default the server listens on:

```text
http://127.0.0.1:8787
```

You can change the port, host, or allowed development origin with environment variables:

```bash
PORT=9000 HOST=127.0.0.1 CORS_ORIGIN=http://localhost:8000 node tools/atlas-mars-server.js
```

The server is intentionally small and dependency free. It is meant to expose the deterministic runtime for local engineering work, not to act as a production deployment.

## Check runtime health

Once the server is running, open another terminal and call:

```bash
curl http://127.0.0.1:8787/healthz
```

The health response includes the runtime status and executes the built-in self-test.

This is useful when you want a quick check that the core loaded correctly before creating a mission run.

## See the available mission scenarios

```bash
curl http://127.0.0.1:8787/v1/scenarios
```

The current public runtime includes three scenarios:

- solar array failure during a dust event
- Earth-link loss with declining reserve
- adversarial maintenance message

Each scenario starts from a different synthetic colony state and is designed to test a different part of the architecture.

## Inspect the tool registry

```bash
curl http://127.0.0.1:8787/v1/tools
```

This endpoint is important because the runtime does not treat every tool equally.

Each registered tool declares an authority class. The classes used by the public runtime are:

```text
READ_ONLY
ANALYSIS
BOUNDED_AUTONOMY
PROTECTED
```

Protected tools are denied by policy. They do not become available because an agent asks for them.

## Run the main solar-array scenario

Create a new run with:

```bash
curl -X POST http://127.0.0.1:8787/v1/runs \
  -H 'content-type: application/json' \
  -d '{"scenario":"dust","run_id":"demo-001"}'
```

The response contains the completed deterministic mission state for that run.

In the nominal dust scenario, the runtime should work through power analysis, habitat reserve protection, digital-twin checks, maintenance diagnosis, logistics verification, robotics planning, resource arbitration, bounded synthetic actions, and final assurance review.

## Read the event trace

After the run has been created:

```bash
curl http://127.0.0.1:8787/v1/runs/demo-001/events
```

The event list contains the same type of evidence shown in the browser Mission Event Trace.

Typical events include:

```text
run.created
agent.handoff
tool.call
resource.conflict
arbitration.completed
evaluation.completed
safety.review
run.completed
```

The adversarial and authority-test cases can also produce `tool.denied`, `gate.blocker`, and other failure records.

## Inject a second fault

You can change the mission after the first run by injecting the scenario's predefined secondary fault:

```bash
curl -X POST http://127.0.0.1:8787/v1/runs/demo-001/faults \
  -H 'content-type: application/json' \
  -d '{}'
```

The actual fault depends on the selected scenario.

For example, the Earth-link-loss case can receive stale digital-twin synchronization. That new evidence can move a previously acceptable mission into `MISSION_HOLD`.

This is intentional. The runtime is designed to react to changed evidence rather than assume the original plan remains valid forever.

## Test the authority boundary

One of the most useful tests is to deliberately request an action the autonomous system is not allowed to perform.

For example:

```bash
curl -X POST http://127.0.0.1:8787/v1/runs/demo-001/actions/propose \
  -H 'content-type: application/json' \
  -d '{"tool":"mars.safety.interlock.override","actor":"Operator test"}'
```

The policy response should be:

```json
{
  "decision": "DENY",
  "reason": "PROTECTED_AUTHORITY"
}
```

The important part is not only the API response.

The mission state is also updated with denied-action evidence and a protected-action blocker. This means the attempted escalation remains part of the audit trail.

You can test other protected tools in the same way, including human EVA initiation, survival-limit changes, and critical-redundancy disablement.

## Export the mission package

To save the complete run record:

```bash
curl http://127.0.0.1:8787/v1/runs/demo-001/package > demo-001-package.json
```

The exported package includes:

- scenario definition
- final mission status
- colony state
- asset state
- digital-twin state
- authority state
- counters
- blockers
- warnings
- decisions
- complete event trace
- decision graph

This gives an engineer a single artifact that can be inspected after the run.

## Serve the browser demo locally

If you want to test the web interface on your own machine, serve the `docs` folder with a local web server instead of opening the HTML file directly with a `file://` URL.

A simple option is Python:

```bash
python3 -m http.server 8000 --directory docs
```

Then open:

```text
http://127.0.0.1:8000/atlas-mars.html
```

The browser page and the Node.js API both use the same deterministic runtime model, but they are separate execution surfaces in the current implementation.

## Main local API endpoints

The development server currently exposes:

```text
GET  /healthz
GET  /v1/scenarios
GET  /v1/tools
POST /v1/runs
GET  /v1/runs/{runId}
GET  /v1/runs/{runId}/events
POST /v1/runs/{runId}/faults
POST /v1/runs/{runId}/actions/propose
GET  /v1/runs/{runId}/package
```

The API is intentionally small enough to understand without a framework.

A reference production API design is also documented in:

`docs/ATLAS_MARS_API.yaml`

That file describes the direction of a server-hosted implementation. It should not be read as a claim that the public site is already running a production mission backend.

## What to inspect as an engineer

If you are reviewing the project technically, I recommend looking at the system in this order:

1. `docs/atlas-mars-core.js` for state, tools, policy, scenarios, invariants, and decision logic
2. `tests/test_atlas_mars_runtime.js` for expected runtime behavior
3. `tools/atlas-mars-server.js` for the local API wrapper
4. `tests/test_atlas_mars_server.js` for API-level smoke tests
5. `docs/atlas-mars.js` for the browser presentation layer
6. `docs/ATLAS_MARS_ARCHITECTURE.md` for the reasoning behind the design

That order makes it easier to separate the runtime from the visual presentation.

## Production boundary

The local server is a development harness.

A real deployment would need substantially more infrastructure and assurance, including:

- authentication
- authorization
- durable state
- service identities
- signed requests
- secret management
- least-privilege connector scopes
- idempotency for side effects
- telemetry freshness checks
- append-only audit storage
- rate limits
- timeout and retry policies
- model and prompt versioning
- human approval records
- incident response
- rollback
- independent safety review
- verification against the actual operational environment

Real physical adapters would also need their own engineering controls and safety cases. A public browser simulation is not evidence that a robot, habitat, spacecraft, or life-support system is safe to control.

## Why this local runtime exists

The goal is straightforward.

I wanted ATLAS: MARS to be something an engineer could inspect and run, not only something a visitor could watch.

The browser demonstrates the behavior visually. The deterministic core makes the behavior explicit in software. The local API gives developers a way to interact with that same logic outside the user interface.

That is the current boundary of the project, and it is intentionally visible.