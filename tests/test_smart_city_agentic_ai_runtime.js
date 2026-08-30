const assert = require('assert');
const core = require('../docs/smart-city-agentic-ai-core.js');

const report = core.runSelfTest();
assert.strictEqual(report.ok, true, JSON.stringify(report, null, 2));

const heat = core.runScenario('heat', { run_id: 'test-city-heat' });
assert.strictEqual(heat.status, 'STABILIZED');
assert.ok(heat.events.length > 15);
assert.ok(heat.counters.handoffs >= 4);
assert.ok(heat.counters.tool_calls >= 10);
assert.ok(heat.counters.auto_actions >= 4);
assert.strictEqual(heat.city.hospital_power, 'PROTECTED');
assert.ok(heat.city.grid_load_pct < core.SCENARIOS.heat.grid_load_pct);

const flood = core.runScenario('flood', { run_id: 'test-city-flood' });
assert.strictEqual(flood.status, 'STABILIZED');
assert.ok(flood.city.emergency_eta_min < core.SCENARIOS.flood.emergency_eta_min);
assert.ok(flood.city.flood_depth_cm < core.SCENARIOS.flood.flood_depth_cm);

const cyber = core.runScenario('cyber', { run_id: 'test-city-cyber' });
assert.strictEqual(cyber.status, 'CITY_HOLD');
assert.strictEqual(cyber.authority.protected_action_denied, true);
assert.ok(cyber.blockers.some(b => b.code === 'ADVERSARIAL_INPUT'));
assert.ok(cyber.events.some(e => e.type === 'tool.denied' && e.payload.tool === 'city.surveillance.identity.track'));

const denied = core.requestProtectedAction(heat, 'city.evacuation.order', 'Test Harness');
assert.strictEqual(denied.status, 'CITY_HOLD');
assert.ok(denied.blockers.some(b => b.code === 'PROTECTED_ACTION_REQUEST'));

const injected = core.injectSecondaryFault(heat);
assert.strictEqual(injected.status, 'CITY_HOLD');
assert.ok(injected.blockers.some(b => b.code === 'TWIN_STALE'));

const pkg = core.cityPackage(heat);
assert.strictEqual(pkg.schema_version, 'smart.city.agentic.package.v1');
assert.strictEqual(pkg.run_id, 'test-city-heat');
assert.strictEqual(pkg.decision_graph.nodes.length, heat.events.length);

console.log(`Smart City Agentic AI runtime tests passed: ${report.passed}/${report.total} self tests plus integration assertions.`);