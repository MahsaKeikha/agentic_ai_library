const assert = require('assert');
const { createServer } = require('../tools/atlas-mars-server.js');

async function main() {
  const server = createServer();
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const { port } = server.address();
  const base = `http://127.0.0.1:${port}`;
  try {
    const health = await fetch(`${base}/healthz`).then(r => r.json());
    assert.strictEqual(health.status, 'ok');

    const createdResponse = await fetch(`${base}/v1/runs`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ scenario: 'dust', run_id: 'api-smoke-dust' })
    });
    assert.strictEqual(createdResponse.status, 201);
    const created = await createdResponse.json();
    assert.strictEqual(created.status, 'STABILIZED');

    const events = await fetch(`${base}/v1/runs/api-smoke-dust/events`).then(r => r.json());
    assert.ok(events.events.length > 10);

    const deny = await fetch(`${base}/v1/runs/api-smoke-dust/actions/propose`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ tool: 'mars.safety.interlock.override', actor: 'API Smoke Test' })
    }).then(r => r.json());
    assert.strictEqual(deny.decision, 'DENY');
    assert.strictEqual(deny.reason, 'PROTECTED_AUTHORITY');

    const pkg = await fetch(`${base}/v1/runs/api-smoke-dust/package`).then(r => r.json());
    assert.strictEqual(pkg.schema_version, 'atlas.mars.package.v2');

    console.log('ATLAS MARS local API smoke tests passed.');
  } finally {
    await new Promise(resolve => server.close(resolve));
  }
}

main().catch(err => {
  console.error(err);
  process.exitCode = 1;
});
