'use strict';
const assert=require('assert');
const core=require('../docs/atlas-space-core.js');

const orbital=core.runScenario('orbital',{run_id:'test-orbital'});
assert.strictEqual(orbital.status,'MISSION_STABLE');
assert.ok(orbital.counters.auto_actions>=2);
assert.ok(orbital.events.some(e=>e.type==='arbitration.completed'));

const surface=core.runScenario('surface',{run_id:'test-surface'});
assert.strictEqual(surface.status,'MISSION_STABLE');
assert.ok(surface.events.some(e=>e.type==='authority.boundary'));

const adversarial=core.runScenario('adversarial',{run_id:'test-adversarial'});
assert.strictEqual(adversarial.status,'MISSION_HOLD');
assert.ok(adversarial.events.some(e=>e.type==='tool.denied'&&e.payload.tool==='space.safety.interlock.override'));
assert.ok(adversarial.authority.protected_action_denied);

const protectedState=core.requestProtectedAction(orbital,'space.human.eva.initiate','Runtime Test');
assert.strictEqual(protectedState.status,'MISSION_HOLD');
assert.ok(protectedState.authority.protected_action_denied);

const fault=core.injectSecondaryFault(orbital);
assert.strictEqual(fault.status,'MISSION_HOLD');
assert.strictEqual(fault.twin.sync,'STALE');

const pkg=core.missionPackage(orbital);
assert.strictEqual(pkg.schema_version,'atlas.space.package.v1');
assert.strictEqual(pkg.final_status,'MISSION_STABLE');
assert.ok(pkg.decision_graph.nodes.length>0);

const report=core.runSelfTest();
assert.ok(report.ok,JSON.stringify(report));
console.log(`ATLAS SPACE runtime tests passed: ${report.passed}/${report.total}`);
