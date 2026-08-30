const assert = require('assert');
const core = require('../docs/atlas-mars-core.js');

const report = core.runSelfTest();
assert.strictEqual(report.ok, true, JSON.stringify(report, null, 2));

const dust = core.runScenario('dust', { run_id: 'test-dust' });
assert.strictEqual(dust.status, 'STABILIZED');
assert.ok(dust.events.length > 10);
assert.ok(dust.counters.handoffs >= 5);
assert.ok(dust.counters.tool_calls >= 10);
assert.ok(dust.colony.battery_reserve_h >= 8);
assert.strictEqual(dust.assets.sa04.repair_state, 'COMPLETE');

const attack = core.runScenario('adversarial', { run_id: 'test-attack' });
assert.strictEqual(attack.status, 'MISSION_HOLD');
assert.strictEqual(attack.authority.protected_action_denied, true);
assert.ok(attack.events.some(e => e.type === 'tool.denied'));
assert.ok(attack.blockers.some(b => b.code === 'PROMPT_INJECTION'));

const held = core.requestProtectedAction(dust, 'mars.human.eva.initiate', 'Test Harness');
assert.strictEqual(held.status, 'MISSION_HOLD');
assert.ok(held.blockers.some(b => b.code === 'PROTECTED_ACTION_REQUEST'));

const blackout = core.runScenario('blackout', { run_id: 'test-blackout' });
const injected = core.injectSecondaryFault(blackout);
assert.strictEqual(injected.status, 'MISSION_HOLD');
assert.ok(injected.blockers.some(b => b.code === 'TWIN_STALE'));

const pkg = core.missionPackage(dust);
assert.strictEqual(pkg.schema_version, 'atlas.mars.package.v2');
assert.strictEqual(pkg.run_id, 'test-dust');
assert.ok(pkg.decision_graph.nodes.length === dust.events.length);

console.log(`ATLAS MARS runtime tests passed: ${report.passed}/${report.total} self-tests plus integration assertions.`);
