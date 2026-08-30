#!/usr/bin/env node
'use strict';

const http = require('http');
const { URL } = require('url');
const core = require('../docs/atlas-mars-core.js');

const runs = new Map();
const PORT = Number(process.env.PORT || 8787);
const HOST = process.env.HOST || '127.0.0.1';

function json(res, status, body) {
  const data = JSON.stringify(body, null, 2);
  res.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
    'content-length': Buffer.byteLength(data),
    'access-control-allow-origin': process.env.CORS_ORIGIN || 'http://localhost:8000',
    'access-control-allow-headers': 'content-type, authorization, x-request-id, idempotency-key',
    'access-control-allow-methods': 'GET,POST,OPTIONS'
  });
  res.end(data);
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let raw = '';
    req.on('data', chunk => {
      raw += chunk;
      if (raw.length > 1024 * 1024) {
        reject(new Error('request body too large'));
        req.destroy();
      }
    });
    req.on('end', () => {
      if (!raw) return resolve({});
      try { resolve(JSON.parse(raw)); }
      catch (err) { reject(new Error('invalid JSON body')); }
    });
    req.on('error', reject);
  });
}

function publicRun(state) {
  return {
    run_id: state.run_id,
    runtime_version: state.runtime_version,
    scenario: state.scenario.id,
    status: state.status,
    phase: state.phase,
    colony: state.colony,
    assets: state.assets,
    twin: state.twin,
    authority: state.authority,
    counters: state.counters,
    blockers: state.blockers,
    warnings: state.warnings,
    decisions: state.decisions,
    event_count: state.events.length,
    completed_at: state.completed_at
  };
}

function parseRunPath(pathname) {
  const m = pathname.match(/^\/v1\/runs\/([^/]+)(?:\/(events|faults|package|actions\/propose))?$/);
  if (!m) return null;
  return { runId: decodeURIComponent(m[1]), sub: m[2] || null };
}

async function handler(req, res) {
  if (req.method === 'OPTIONS') return json(res, 204, {});
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);

  if (req.method === 'GET' && url.pathname === '/healthz') {
    const selfTest = core.runSelfTest();
    return json(res, selfTest.ok ? 200 : 503, {
      service: 'atlas-mars-runtime',
      runtime_version: core.VERSION,
      status: selfTest.ok ? 'ok' : 'degraded',
      self_test: selfTest
    });
  }

  if (req.method === 'GET' && url.pathname === '/v1/tools') {
    return json(res, 200, { runtime_version: core.VERSION, tools: core.TOOL_REGISTRY });
  }

  if (req.method === 'GET' && url.pathname === '/v1/scenarios') {
    return json(res, 200, { scenarios: core.SCENARIOS });
  }

  if (req.method === 'POST' && url.pathname === '/v1/runs') {
    try {
      const body = await readBody(req);
      const scenario = body.scenario || 'dust';
      if (!core.SCENARIOS[scenario]) return json(res, 400, { error: 'unknown_scenario', allowed: Object.keys(core.SCENARIOS) });
      const runId = body.run_id || `api-${scenario}-${Date.now().toString(36)}`;
      if (runs.has(runId)) return json(res, 409, { error: 'run_id_exists', run_id: runId });
      const state = core.runScenario(scenario, { run_id: runId });
      runs.set(runId, state);
      return json(res, 201, publicRun(state));
    } catch (err) {
      return json(res, 400, { error: 'bad_request', message: err.message });
    }
  }

  const route = parseRunPath(url.pathname);
  if (!route) return json(res, 404, { error: 'not_found' });
  const state = runs.get(route.runId);
  if (!state) return json(res, 404, { error: 'run_not_found', run_id: route.runId });

  if (req.method === 'GET' && route.sub === null) return json(res, 200, publicRun(state));
  if (req.method === 'GET' && route.sub === 'events') return json(res, 200, { run_id: state.run_id, events: state.events });
  if (req.method === 'GET' && route.sub === 'package') return json(res, 200, core.missionPackage(state));

  if (req.method === 'POST' && route.sub === 'faults') {
    const next = core.injectSecondaryFault(state);
    runs.set(route.runId, next);
    return json(res, 202, publicRun(next));
  }

  if (req.method === 'POST' && route.sub === 'actions/propose') {
    try {
      const body = await readBody(req);
      const tool = body.tool;
      const spec = core.TOOL_REGISTRY[tool];
      if (!spec) return json(res, 400, { decision: 'DENY', reason: 'UNKNOWN_TOOL', tool });
      if (spec.authority === 'PROTECTED') {
        const next = core.requestProtectedAction(state, tool, body.actor || 'API Authority Test');
        runs.set(route.runId, next);
        return json(res, 200, {
          decision: 'DENY',
          reason: 'PROTECTED_AUTHORITY',
          tool,
          authority_class: spec.authority,
          run: publicRun(next)
        });
      }
      return json(res, 200, {
        decision: spec.authority === 'BOUNDED_AUTONOMY' ? 'ALLOW_WITHIN_PREAPPROVED_ENVELOPE' : 'ALLOW',
        tool,
        authority_class: spec.authority,
        note: 'Policy decision only. This endpoint does not execute an additional side effect.'
      });
    } catch (err) {
      return json(res, 400, { error: 'bad_request', message: err.message });
    }
  }

  return json(res, 405, { error: 'method_not_allowed' });
}

function createServer() { return http.createServer((req, res) => handler(req, res).catch(err => json(res, 500, { error: 'internal_error', message: err.message }))); }

if (require.main === module) {
  const server = createServer();
  server.listen(PORT, HOST, () => {
    console.log(`ATLAS MARS runtime API v${core.VERSION} listening on http://${HOST}:${PORT}`);
    console.log('Public demo note: this local server still uses synthetic state and no external control system.');
  });
}

module.exports = { createServer, handler, runs };
