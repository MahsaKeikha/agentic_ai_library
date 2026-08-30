# ATLAS: MARS Developer Quick Start

ATLAS: MARS now has two executable surfaces:

1. the public browser mission-control page
2. a zero-dependency local Node.js API server for testing the same deterministic runtime core outside the UI

The local API still uses synthetic state. It does not connect to real robots, habitats, spacecraft, telemetry, or production model providers.

## Requirements

- Node.js 20 or later
- no npm packages are required

## Run the deterministic tests

```bash
node tests/test_atlas_mars_runtime.js
node tests/test_atlas_mars_server.js
```

## Start the local mission API

```bash
node tools/atlas-mars-server.js
```

Default address:

```text
http://127.0.0.1:8787
```

Optional environment variables:

```bash
PORT=9000 HOST=127.0.0.1 CORS_ORIGIN=http://localhost:8000 node tools/atlas-mars-server.js
```

## Health check

```bash
curl http://127.0.0.1:8787/healthz
```

The health response runs the built-in deterministic runtime self-test.

## Inspect registered scenarios

```bash
curl http://127.0.0.1:8787/v1/scenarios
```

## Inspect the tool registry

```bash
curl http://127.0.0.1:8787/v1/tools
```

Each tool declares its authority class. Protected tools remain denied by policy.

## Run the solar-array scenario

```bash
curl -X POST http://127.0.0.1:8787/v1/runs \
  -H 'content-type: application/json' \
  -d '{"scenario":"dust","run_id":"demo-001"}'
```

## Read mission events

```bash
curl http://127.0.0.1:8787/v1/runs/demo-001/events
```

## Inject the scenario's secondary fault

```bash
curl -X POST http://127.0.0.1:8787/v1/runs/demo-001/faults \
  -H 'content-type: application/json' \
  -d '{}'
```

## Test a protected action

```bash
curl -X POST http://127.0.0.1:8787/v1/runs/demo-001/actions/propose \
  -H 'content-type: application/json' \
  -d '{"tool":"mars.safety.interlock.override","actor":"Operator test"}'
```

Expected policy result:

```json
{
  "decision": "DENY",
  "reason": "PROTECTED_AUTHORITY"
}
```

The run state is also updated with a protected-action blocker and denied-action evidence.

## Export a mission package

```bash
curl http://127.0.0.1:8787/v1/runs/demo-001/package > demo-001-package.json
```

The package includes state, assets, twin state, authority state, decisions, blockers, warnings, counters, the complete event trace, and decision graph.

## Browser-only static serving

For local testing of the public page, serve the `docs` directory rather than opening the HTML with a `file://` URL.

For example:

```bash
python3 -m http.server 8000 --directory docs
```

Then open:

```text
http://127.0.0.1:8000/atlas-mars.html
```

## Production boundary

The local server is a development harness, not a production service. A real deployment needs authentication, authorization, durable state, signed requests, secret management, idempotency, telemetry freshness controls, audit storage, rate limits, timeout policies, independent safety review, and organization-specific verification.

The reference API design is documented in `docs/ATLAS_MARS_API.yaml`.
