(() => {
  "use strict";

  const $ = (id) => document.getElementById(id);
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const clamp = (n, min, max) => Math.max(min, Math.min(max, Number(n)));
  const nowIso = () => new Date().toISOString();
  const makeId = (prefix) => `${prefix}-${Math.random().toString(36).slice(2, 8)}-${Date.now().toString(36).slice(-5)}`;

  const specialistRegistry = [
    { id: "spec-requirements", name: "Requirements Analyst", capabilities: ["requirements", "policy_mapping", "risk_classification"], reliability: 0.96, cost: 1, latency: 1 },
    { id: "spec-repo", name: "Repository Engineer", capabilities: ["code_review", "dependency_analysis", "tool_surface"], reliability: 0.94, cost: 2, latency: 2 },
    { id: "spec-eval", name: "Evaluation Engineer", capabilities: ["quality_eval", "benchmark", "regression_test"], reliability: 0.95, cost: 2, latency: 3 },
    { id: "spec-eval-backup", name: "Evaluation Backup", capabilities: ["quality_eval", "benchmark", "regression_test"], reliability: 0.90, cost: 3, latency: 2 },
    { id: "spec-security", name: "AI Security Reviewer", capabilities: ["prompt_injection", "tool_permission", "abuse_case"], reliability: 0.97, cost: 2, latency: 3 },
    { id: "spec-sre", name: "SRE Specialist", capabilities: ["observability", "rollback", "canary", "health_check"], reliability: 0.98, cost: 2, latency: 2 },
    { id: "spec-release", name: "Release Manager", capabilities: ["release_synthesis", "approval_package", "change_management"], reliability: 0.95, cost: 1, latency: 1 }
  ];

  const agentGraphTemplate = [
    ["Planner Agent", "Decompose the release goal into explicit dependent tasks"],
    ["Router Agent", "Score declared specialist capabilities for each task"],
    ["Execution Agent", "Invoke specialists through the audited tool gateway"],
    ["Critic Agent", "Check completeness, contradictions, and evidence quality"],
    ["Safety Agent", "Block unsafe progression and determine approval eligibility"],
    ["Human Authority", "Approve only after automated eligibility gates pass"],
    ["Deployment Verifier", "Execute sandbox canary and verify health before promotion"]
  ];

  const els = {
    run: $("run-runtime"), loadFailure: $("load-failure"), reset: $("reset-runtime"), download: $("download-state"),
    goal: $("goal-input"), coverage: $("coverage"), evalRate: $("eval-rate"), observability: $("observability"),
    coverageOutput: $("coverage-output"), evalOutput: $("eval-output"), observabilityOutput: $("observability-output"),
    promptAttack: $("prompt-attack"), toolFailure: $("tool-failure"), rollbackReady: $("rollback-ready"), privilegeScoped: $("privilege-scoped"),
    trace: $("event-trace"), graph: $("agent-graph"), registry: $("specialist-registry"), inspector: $("inspector"), inspectorEmpty: $("inspector-empty"),
    inspectId: $("inspect-id"), inspectType: $("inspect-type"), inspectActor: $("inspect-actor"), inspectJson: $("inspect-json"),
    runId: $("run-id"), stateVersion: $("state-version"), runtimeStatus: $("runtime-status"), handoffCount: $("handoff-count"), toolCount: $("tool-count"), retryCount: $("retry-count"), blockerCount: $("blocker-count"),
    eligibility: $("eligibility"), releaseState: $("release-state"), gateExplanation: $("gate-explanation"), remediate: $("remediate"), approve: $("approve-release"), promote: $("promote-release")
  };

  let running = false;
  let state = initialState();

  function initialState() {
    return {
      runId: null,
      version: 0,
      status: "idle",
      startedAt: null,
      completedAt: null,
      goal: "",
      sandbox: {},
      plan: [],
      routes: {},
      events: [],
      artifacts: {},
      blockers: [],
      critic: null,
      safety: null,
      eligibility: "not_evaluated",
      humanApproval: null,
      release: { state: "not_started", canaryPercent: 0, verified: false, promoted: false },
      metrics: { handoffs: 0, toolCalls: 0, retries: 0 }
    };
  }

  function readSandbox() {
    return {
      coverage: clamp(els.coverage.value, 40, 100),
      evalPassRate: clamp(els.evalRate.value, 40, 100),
      observability: clamp(els.observability.value, 30, 100),
      promptAttack: els.promptAttack.checked,
      transientEvalFailure: els.toolFailure.checked,
      rollbackReady: els.rollbackReady.checked,
      privilegeScoped: els.privilegeScoped.checked,
      injectedFailureConsumed: false,
      canaryHealth: 100
    };
  }

  function bumpVersion() {
    state.version += 1;
    renderStats();
  }

  function setStatus(status) {
    state.status = status;
    els.runtimeStatus.textContent = status.replaceAll("_", " ").toUpperCase();
    els.runtimeStatus.dataset.state = status;
    bumpVersion();
  }

  function setGraphStatus(index, status, detail) {
    const row = els.graph.querySelector(`[data-graph-index="${index}"]`);
    if (!row) return;
    row.dataset.status = status;
    row.querySelector(".graph-status").textContent = status.toUpperCase();
    if (detail) row.querySelector("small").textContent = detail;
  }

  function renderGraph() {
    els.graph.innerHTML = agentGraphTemplate.map((item, i) => `
      <div class="graph-row" data-graph-index="${i}" data-status="waiting">
        <div class="graph-agent">${item[0]}</div>
        <div class="graph-copy"><b>${item[1]}</b><small>Waiting for runtime execution</small></div>
        <div class="graph-status">WAITING</div>
      </div>`).join("");
  }

  function renderRegistry() {
    els.registry.innerHTML = specialistRegistry.map((s) => `
      <div class="specialist-card">
        <b>${s.name}</b><span class="registry-score">R ${Math.round(s.reliability * 100)}%</span>
        <p>${s.capabilities.join(" · ")}</p>
      </div>`).join("");
  }

  function renderSliders() {
    els.coverageOutput.value = `${els.coverage.value}%`;
    els.evalOutput.value = `${els.evalRate.value}%`;
    els.observabilityOutput.value = `${els.observability.value}%`;
  }

  function renderStats() {
    els.runId.textContent = state.runId || "not started";
    els.stateVersion.textContent = state.version;
    els.handoffCount.textContent = state.metrics.handoffs;
    els.toolCount.textContent = state.metrics.toolCalls;
    els.retryCount.textContent = state.metrics.retries;
    els.blockerCount.textContent = state.blockers.length;
  }

  function renderGate() {
    const labels = {
      not_evaluated: "NOT EVALUATED",
      blocked: "BLOCKED",
      eligible: "ELIGIBLE",
      approved: "HUMAN APPROVED"
    };
    els.eligibility.textContent = labels[state.eligibility] || state.eligibility.toUpperCase();
    els.releaseState.textContent = state.release.state.replaceAll("_", " ").toUpperCase();
    els.remediate.disabled = running || state.eligibility !== "blocked";
    els.approve.disabled = running || state.eligibility !== "eligible";
    els.promote.disabled = running || !(state.release.verified && !state.release.promoted);

    if (state.eligibility === "blocked") {
      els.gateExplanation.textContent = `${state.blockers.length} blocker${state.blockers.length === 1 ? "" : "s"} prevent approval: ${state.blockers.map((b) => b.title).join("; ")}.`;
    } else if (state.eligibility === "eligible") {
      els.gateExplanation.textContent = "Automated technical and safety gates passed. A human can now approve a bounded canary release.";
    } else if (state.eligibility === "approved") {
      els.gateExplanation.textContent = state.release.verified ? "Canary verification passed. Human promotion to full release is available." : "Human approval recorded. The runtime may execute only the bounded canary action.";
    } else {
      els.gateExplanation.textContent = "The release control is disabled until all technical and safety blockers are cleared.";
    }
  }

  function addEvent(type, actor, status, title, payload = {}) {
    const evt = {
      id: makeId("evt"),
      seq: state.events.length + 1,
      timestamp: nowIso(),
      type,
      actor,
      status,
      title,
      payload: structuredCloneSafe(payload)
    };
    state.events.push(evt);
    bumpVersion();
    const button = document.createElement("button");
    button.type = "button";
    button.className = "trace-event";
    button.dataset.eventId = evt.id;
    button.innerHTML = `<div><strong>${escapeHtml(title)}</strong><small>${String(evt.seq).padStart(2, "0")} · ${escapeHtml(type)}</small></div><div class="trace-actor">${escapeHtml(actor)}</div><div class="trace-status ${escapeHtml(status)}">${escapeHtml(status.toUpperCase())}</div>`;
    button.addEventListener("click", () => inspectEvent(evt.id));
    els.trace.prepend(button);
    return evt;
  }

  function updateEvent(evt, status, extraPayload = {}) {
    evt.status = status;
    evt.payload = { ...evt.payload, ...structuredCloneSafe(extraPayload), completedAt: nowIso() };
    bumpVersion();
    const row = els.trace.querySelector(`[data-event-id="${evt.id}"]`);
    if (row) {
      const statusNode = row.querySelector(".trace-status");
      statusNode.className = `trace-status ${status}`;
      statusNode.textContent = status.toUpperCase();
    }
  }

  function inspectEvent(id) {
    const evt = state.events.find((e) => e.id === id);
    if (!evt) return;
    els.trace.querySelectorAll(".trace-event.active").forEach((n) => n.classList.remove("active"));
    const row = els.trace.querySelector(`[data-event-id="${id}"]`);
    if (row) row.classList.add("active");
    els.inspectorEmpty.hidden = true;
    els.inspector.hidden = false;
    els.inspectId.textContent = evt.id;
    els.inspectType.textContent = evt.type;
    els.inspectActor.textContent = evt.actor;
    els.inspectJson.textContent = JSON.stringify(evt, null, 2);
  }

  function structuredCloneSafe(value) {
    try { return structuredClone(value); } catch { return JSON.parse(JSON.stringify(value)); }
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
  }

  function resetState(preserveInputs = true) {
    if (running) return;
    state = initialState();
    els.trace.innerHTML = "";
    els.inspector.hidden = true;
    els.inspectorEmpty.hidden = false;
    els.download.disabled = true;
    renderGraph();
    renderStats();
    renderGate();
    els.runtimeStatus.textContent = "IDLE";
    els.runtimeStatus.dataset.state = "idle";
    if (!preserveInputs) loadBaseline();
  }

  function loadBaseline() {
    els.goal.value = "Release version 2 of our AI customer support agent to production. It can search account data and issue refunds under policy. Validate quality, prompt injection resistance, tool permissions, observability, rollback readiness, and produce an approval-ready release decision.";
    els.coverage.value = 82;
    els.evalRate.value = 86;
    els.observability.value = 76;
    els.promptAttack.checked = false;
    els.toolFailure.checked = false;
    els.rollbackReady.checked = true;
    els.privilegeScoped.checked = true;
    renderSliders();
  }

  function loadFailureCase() {
    if (running) return;
    resetState(true);
    els.goal.value = "Ship the new tool-enabled AI support agent today. It can read account history and issue refunds. A red-team report found a prompt injection path and the evaluation service is unstable. Decide whether to release and recover safely if possible.";
    els.coverage.value = 71;
    els.evalRate.value = 73;
    els.observability.value = 52;
    els.promptAttack.checked = true;
    els.toolFailure.checked = true;
    els.rollbackReady.checked = false;
    els.privilegeScoped.checked = false;
    renderSliders();
  }

  function buildPlan(goal) {
    const tasks = [
      task("T1", "Extract release requirements and constraints", ["requirements", "policy_mapping", "risk_classification"], [], "requirements.extract"),
      task("T2", "Inspect implementation and tool surface", ["code_review", "dependency_analysis", "tool_surface"], ["T1"], "repo.scan"),
      task("T3", "Run quality and regression evaluation", ["quality_eval", "benchmark", "regression_test"], ["T2"], "eval.run"),
      task("T4", "Run prompt injection and tool permission review", ["prompt_injection", "tool_permission", "abuse_case"], ["T2"], "security.redteam"),
      task("T5", "Validate observability, rollback, and canary readiness", ["observability", "rollback", "canary", "health_check"], ["T2"], "ops.check"),
      task("T6", "Synthesize approval-ready release package", ["release_synthesis", "approval_package", "change_management"], ["T3", "T4", "T5"], "release.package")
    ];
    return { goal, tasks, dependencyWaves: [["T1"], ["T2"], ["T3", "T4", "T5"], ["T6"]] };
  }

  function task(id, title, requiredCapabilities, dependencies, tool) {
    return { id, title, requiredCapabilities, dependencies, tool, status: "planned", attempts: [], route: null, output: null };
  }

  function scoreSpecialist(taskObj, specialist) {
    const overlap = taskObj.requiredCapabilities.filter((c) => specialist.capabilities.includes(c)).length;
    if (!overlap) return null;
    const coverage = overlap / taskObj.requiredCapabilities.length;
    const score = Math.round(coverage * 70 + specialist.reliability * 22 - specialist.cost * 2 - specialist.latency * 1.5);
    return { specialistId: specialist.id, specialistName: specialist.name, overlap, coverage: Number(coverage.toFixed(2)), reliability: specialist.reliability, cost: specialist.cost, latency: specialist.latency, score };
  }

  function routeTask(taskObj, excluded = []) {
    const candidates = specialistRegistry
      .filter((s) => !excluded.includes(s.id))
      .map((s) => scoreSpecialist(taskObj, s))
      .filter(Boolean)
      .sort((a, b) => b.score - a.score);
    const selected = candidates[0] || null;
    const rejected = specialistRegistry
      .filter((s) => !candidates.some((c) => c.specialistId === s.id))
      .map((s) => ({ specialistId: s.id, specialistName: s.name, reason: "No required capability overlap" }));
    return { taskId: taskObj.id, requiredCapabilities: taskObj.requiredCapabilities, candidates, rejected, selected, ambiguous: Boolean(candidates[1] && selected && candidates[1].score === selected.score) };
  }

  async function runFull() {
    if (running) return;
    resetState(true);
    running = true;
    disableDuringRun(true);
    state.runId = makeId("run");
    state.startedAt = nowIso();
    state.goal = els.goal.value.trim() || "Evaluate release readiness for the AI support agent.";
    state.sandbox = readSandbox();
    renderStats();
    setStatus("running");

    try {
      await plannerStage();
      await routerAndExecutionStage();
      await criticStage();
      await safetyStage();
      state.completedAt = nowIso();
      els.download.disabled = false;
    } catch (error) {
      addEvent("runtime.error", "Orchestrator", "failed", "Runtime exception captured", { message: error.message, stack: error.stack });
      setStatus("blocked");
      state.blockers.push({ id: "runtime_exception", title: "Runtime exception", severity: "critical" });
    } finally {
      running = false;
      disableDuringRun(false);
      renderGate();
      renderStats();
    }
  }

  async function plannerStage() {
    setGraphStatus(0, "running", "Parsing goal and building dependency graph");
    const evt = addEvent("agent.start", "Planner Agent", "running", "Planner decomposes goal", { goal: state.goal });
    await sleep(300);
    const plan = buildPlan(state.goal);
    state.plan = plan.tasks;
    state.artifacts.plan = { id: makeId("artifact-plan"), createdBy: "Planner Agent", createdAt: nowIso(), dependencyWaves: plan.dependencyWaves, taskCount: plan.tasks.length };
    state.metrics.handoffs += 1;
    updateEvent(evt, "passed", { plan: state.artifacts.plan, tasks: state.plan.map(({ id, title, dependencies, requiredCapabilities }) => ({ id, title, dependencies, requiredCapabilities })) });
    setGraphStatus(0, "passed", `${plan.tasks.length} tasks across ${plan.dependencyWaves.length} dependency waves`);
  }

  async function routerAndExecutionStage() {
    setGraphStatus(1, "running", "Scoring capability matches for planned tasks");
    setGraphStatus(2, "running", "Executing routed specialists through tool gateway");
    for (const taskObj of state.plan) {
      const depsReady = taskObj.dependencies.every((id) => state.plan.find((t) => t.id === id)?.status === "passed");
      if (!depsReady) {
        taskObj.status = "blocked";
        addEvent("task.blocked", "Execution Agent", "blocked", `${taskObj.id} blocked by dependency`, { taskId: taskObj.id, dependencies: taskObj.dependencies });
        continue;
      }
      await executeTask(taskObj);
    }
    setGraphStatus(1, "passed", `${Object.keys(state.routes).length} routing decisions recorded`);
    const failed = state.plan.filter((t) => t.status !== "passed").length;
    setGraphStatus(2, failed ? "blocked" : "passed", failed ? `${failed} task remains unresolved` : `${state.plan.length} tasks executed with provenance`);
  }

  async function executeTask(taskObj) {
    const routeEvt = addEvent("routing.decision", "Router Agent", "running", `Route ${taskObj.id}: ${taskObj.title}`, { taskId: taskObj.id, requiredCapabilities: taskObj.requiredCapabilities });
    await sleep(150);
    let route = routeTask(taskObj);
    state.routes[taskObj.id] = route;
    taskObj.route = route;
    state.metrics.handoffs += 1;
    updateEvent(routeEvt, route.selected ? "passed" : "failed", route);
    if (!route.selected) {
      taskObj.status = "failed";
      return;
    }

    let result = await invokeSpecialist(taskObj, route.selected, 1);
    if (!result.ok && result.retryable) {
      state.metrics.retries += 1;
      const retryEvt = addEvent("execution.retry", "Execution Agent", "running", `${taskObj.id} reroute after retryable failure`, { failedSpecialist: route.selected, reason: result.error });
      await sleep(180);
      const fallbackRoute = routeTask(taskObj, [route.selected.specialistId]);
      if (fallbackRoute.selected) {
        taskObj.route.fallback = fallbackRoute;
        state.metrics.handoffs += 1;
        updateEvent(retryEvt, "passed", { selectedFallback: fallbackRoute.selected, preservedFailure: true });
        result = await invokeSpecialist(taskObj, fallbackRoute.selected, 2);
      } else {
        updateEvent(retryEvt, "failed", { reason: "No fallback specialist available" });
      }
    }
    taskObj.status = result.ok ? "passed" : "failed";
    taskObj.output = result.output || null;
  }

  async function invokeSpecialist(taskObj, selection, attemptNumber) {
    const specialist = specialistRegistry.find((s) => s.id === selection.specialistId);
    const invocationId = makeId("inv");
    const evt = addEvent("specialist.invoke", specialist.name, "running", `${taskObj.id} specialist attempt ${attemptNumber}`, { invocationId, taskId: taskObj.id, specialist: selection, tool: taskObj.tool, permittedTools: [taskObj.tool] });
    taskObj.attempts.push({ invocationId, specialistId: specialist.id, attempt: attemptNumber, status: "running", startedAt: nowIso() });
    state.metrics.handoffs += 1;
    await sleep(180 + specialist.latency * 45);
    const toolResult = await toolGateway(taskObj.tool, { taskId: taskObj.id, goal: state.goal, sandbox: state.sandbox, specialist: specialist.name });
    const attempt = taskObj.attempts[taskObj.attempts.length - 1];
    attempt.status = toolResult.ok ? "passed" : "failed";
    attempt.completedAt = nowIso();
    attempt.toolCallId = toolResult.callId;
    updateEvent(evt, toolResult.ok ? "passed" : "failed", { toolResult, attempt: structuredCloneSafe(attempt) });
    return toolResult;
  }

  async function toolGateway(toolName, args) {
    const callId = makeId("tool");
    state.metrics.toolCalls += 1;
    const sideEffectClass = ["release.canary", "release.promote"].includes(toolName) ? "protected_write" : toolName.startsWith("remediation.") ? "sandbox_write" : "read_or_compute";
    const authorized = sideEffectClass !== "protected_write" || (toolName === "release.canary" && state.eligibility === "approved") || (toolName === "release.promote" && state.release.verified);
    const evt = addEvent("tool.call", "Tool Gateway", "running", toolName, { callId, toolName, args: sanitizeArgs(args), sideEffectClass, authorized });
    const started = performance.now();
    await sleep(120);
    let response;
    try {
      response = runTool(toolName, args);
    } catch (error) {
      response = { ok: false, retryable: false, error: error.message };
    }
    const latencyMs = Math.round(performance.now() - started);
    const result = { callId, toolName, latencyMs, sideEffectClass, ...response };
    updateEvent(evt, result.ok ? "passed" : "failed", { result });
    return result;
  }

  function sanitizeArgs(args) {
    return { taskId: args.taskId, goal: args.goal, specialist: args.specialist, sandboxSnapshot: structuredCloneSafe(args.sandbox) };
  }

  function runTool(toolName) {
    const s = state.sandbox;
    switch (toolName) {
      case "requirements.extract": {
        const output = {
          protectedCapabilities: ["account_data_read", "refund_issue"],
          requiredControls: ["quality_eval", "prompt_injection_test", "least_privilege", "observability", "rollback", "human_release_approval"],
          riskClass: "high_control_surface",
          userGoalHash: simpleHash(state.goal)
        };
        state.artifacts.requirements = output;
        return { ok: true, retryable: false, output };
      }
      case "repo.scan": {
        const output = { coverage: s.coverage, toolSurface: ["account.search", "refund.issue"], permissionModel: s.privilegeScoped ? "scoped" : "broad", dependencyHealth: "nominal" };
        state.artifacts.repoScan = output;
        return { ok: true, retryable: false, output };
      }
      case "eval.run": {
        if (s.transientEvalFailure && !s.injectedFailureConsumed) {
          s.injectedFailureConsumed = true;
          return { ok: false, retryable: true, error: "Synthetic eval service timeout after 5 seconds", output: null };
        }
        const output = { passRate: s.evalPassRate, regressionCount: s.evalPassRate >= 80 ? 1 : 7, coverage: s.coverage, threshold: 80, status: s.evalPassRate >= 80 && s.coverage >= 80 ? "pass" : "gap" };
        state.artifacts.eval = output;
        return { ok: true, retryable: false, output };
      }
      case "security.redteam": {
        const attackSucceeded = s.promptAttack && !s.privilegeScoped;
        const output = { promptAttackInjected: s.promptAttack, privilegeScoped: s.privilegeScoped, attackSucceeded, toolEscalationPossible: attackSucceeded, severity: attackSucceeded ? "critical" : s.promptAttack ? "contained" : "no_attack_injected" };
        state.artifacts.security = output;
        return { ok: true, retryable: false, output };
      }
      case "ops.check": {
        const output = { observabilityScore: s.observability, rollbackReady: s.rollbackReady, canarySupported: true, healthChecks: ["error_rate", "latency_p95", "refund_anomaly_rate"], status: s.observability >= 70 && s.rollbackReady ? "ready" : "gap" };
        state.artifacts.ops = output;
        return { ok: true, retryable: false, output };
      }
      case "release.package": {
        const output = { evidenceRefs: Object.keys(state.artifacts), unresolvedTasks: state.plan.filter((t) => t.status !== "passed").map((t) => t.id), requestedAction: "canary_release", approvalRequired: true };
        state.artifacts.releasePackage = output;
        return { ok: true, retryable: false, output };
      }
      case "remediation.scope_privilege":
        s.privilegeScoped = true; els.privilegeScoped.checked = true; return { ok: true, retryable: false, output: { privilegeScoped: true, change: "refund tool limited by policy and amount" } };
      case "remediation.raise_coverage":
        s.coverage = Math.max(s.coverage, 88); els.coverage.value = s.coverage; renderSliders(); return { ok: true, retryable: false, output: { coverage: s.coverage, change: "added targeted regression tests" } };
      case "remediation.raise_eval":
        s.evalPassRate = Math.max(s.evalPassRate, 88); els.evalRate.value = s.evalPassRate; renderSliders(); return { ok: true, retryable: false, output: { evalPassRate: s.evalPassRate, change: "fixed failing behaviors and reran evaluation" } };
      case "remediation.observability":
        s.observability = Math.max(s.observability, 86); els.observability.value = s.observability; renderSliders(); return { ok: true, retryable: false, output: { observability: s.observability, change: "added traces, alerts, and refund anomaly metric" } };
      case "remediation.rollback":
        s.rollbackReady = true; els.rollbackReady.checked = true; return { ok: true, retryable: false, output: { rollbackReady: true, change: "validated one-click rollback and previous artifact" } };
      case "release.canary": {
        if (state.eligibility !== "approved") return { ok: false, retryable: false, error: "Human approval missing" };
        state.release.state = "canary_active";
        state.release.canaryPercent = 10;
        return { ok: true, retryable: false, output: { canaryPercent: 10, environment: "sandbox-production", releaseId: makeId("rel") } };
      }
      case "telemetry.verify": {
        const riskPenalty = (s.evalPassRate < 80 ? 8 : 0) + (s.observability < 70 ? 10 : 0) + (!s.privilegeScoped ? 15 : 0);
        s.canaryHealth = clamp(98 - riskPenalty, 0, 100);
        const output = { canaryHealth: s.canaryHealth, errorRate: s.canaryHealth >= 90 ? 0.14 : 2.8, latencyP95Ms: s.canaryHealth >= 90 ? 412 : 980, refundAnomalyRate: s.privilegeScoped ? 0.02 : 1.7, passed: s.canaryHealth >= 90 };
        state.artifacts.canaryVerification = output;
        return { ok: true, retryable: false, output };
      }
      case "release.promote": {
        if (!state.release.verified) return { ok: false, retryable: false, error: "Canary verification not passed" };
        state.release.state = "full_release";
        state.release.canaryPercent = 100;
        state.release.promoted = true;
        return { ok: true, retryable: false, output: { trafficPercent: 100, promotedAt: nowIso(), rollbackAvailable: s.rollbackReady } };
      }
      default:
        throw new Error(`Unknown tool: ${toolName}`);
    }
  }

  async function criticStage() {
    setGraphStatus(3, "running", "Reviewing task completion and evidence consistency");
    const evt = addEvent("agent.start", "Critic Agent", "running", "Critic reviews execution evidence", { taskStatuses: state.plan.map((t) => ({ id: t.id, status: t.status, attempts: t.attempts.length })) });
    await sleep(260);
    const findings = [];
    if (state.plan.some((t) => t.status !== "passed")) findings.push({ id: "task_failure", severity: "critical", title: "Unresolved specialist execution" });
    if ((state.artifacts.eval?.passRate ?? 0) < 80) findings.push({ id: "eval_gap", severity: "high", title: "Evaluation pass rate below 80%" });
    if ((state.artifacts.repoScan?.coverage ?? 0) < 80) findings.push({ id: "coverage_gap", severity: "high", title: "Test coverage below 80%" });
    if ((state.artifacts.ops?.observabilityScore ?? 0) < 70) findings.push({ id: "observability_gap", severity: "high", title: "Observability below release threshold" });
    if (!state.artifacts.ops?.rollbackReady) findings.push({ id: "rollback_gap", severity: "critical", title: "Rollback plan is not ready" });
    if (state.artifacts.security?.attackSucceeded) findings.push({ id: "prompt_injection", severity: "critical", title: "Prompt injection can escalate refund tool" });
    state.critic = { passed: findings.length === 0, findings, reviewedArtifacts: Object.keys(state.artifacts), provenanceComplete: state.plan.every((t) => t.attempts.length > 0) };
    updateEvent(evt, state.critic.passed ? "passed" : "blocked", state.critic);
    setGraphStatus(3, state.critic.passed ? "passed" : "blocked", state.critic.passed ? "No unresolved quality blockers" : `${findings.length} evidence-backed finding${findings.length === 1 ? "" : "s"}`);
  }

  async function safetyStage() {
    setGraphStatus(4, "running", "Evaluating blocker severity and protected action boundary");
    const evt = addEvent("agent.start", "Safety Agent", "running", "Safety evaluates release eligibility", { critic: state.critic });
    await sleep(240);
    const blockers = [...(state.critic?.findings || [])];
    if (!state.artifacts.security) blockers.push({ id: "missing_security", severity: "critical", title: "Security evidence missing" });
    if (!state.artifacts.releasePackage) blockers.push({ id: "missing_package", severity: "high", title: "Release package missing" });
    state.blockers = uniqueById(blockers);
    state.safety = {
      blockers: state.blockers,
      protectedAction: "production_release",
      toolBoundary: "human_required",
      approvalEligible: state.blockers.length === 0,
      decision: state.blockers.length ? "block" : "allow_human_review"
    };
    state.eligibility = state.safety.approvalEligible ? "eligible" : "blocked";
    updateEvent(evt, state.safety.approvalEligible ? "passed" : "blocked", state.safety);
    setGraphStatus(4, state.safety.approvalEligible ? "passed" : "blocked", state.safety.approvalEligible ? "Automated gates passed" : `${state.blockers.length} blocker${state.blockers.length === 1 ? "" : "s"} prevent approval`);
    setGraphStatus(5, state.safety.approvalEligible ? "waiting" : "blocked", state.safety.approvalEligible ? "Waiting for explicit human decision" : "Human approval cannot override active blockers");
    setStatus(state.safety.approvalEligible ? "eligible" : "blocked");
    renderGate();
  }

  async function runRemediation() {
    if (running || state.eligibility !== "blocked") return;
    running = true;
    disableDuringRun(true);
    setStatus("running");
    const remediationEvt = addEvent("remediation.start", "Execution Agent", "running", "Bounded remediation plan created", { blockers: state.blockers });
    try {
      for (const blocker of [...state.blockers]) {
        let tool = null;
        if (blocker.id === "prompt_injection") tool = "remediation.scope_privilege";
        if (blocker.id === "coverage_gap") tool = "remediation.raise_coverage";
        if (blocker.id === "eval_gap") tool = "remediation.raise_eval";
        if (blocker.id === "observability_gap") tool = "remediation.observability";
        if (blocker.id === "rollback_gap") tool = "remediation.rollback";
        if (blocker.id === "task_failure") tool = "remediation.raise_eval";
        if (!tool) continue;
        await toolGateway(tool, { taskId: "REMEDIATION", goal: state.goal, sandbox: state.sandbox, specialist: "Bounded Remediation" });
      }
      state.sandbox.transientEvalFailure = false;
      els.toolFailure.checked = false;
      await reexecuteEvidenceTasks();
      await criticStage();
      await safetyStage();
      updateEvent(remediationEvt, state.eligibility === "eligible" ? "passed" : "blocked", { eligibility: state.eligibility, blockers: state.blockers, completed: true });
      addEvent("remediation.complete", "Execution Agent", state.eligibility === "eligible" ? "passed" : "blocked", "Remediation cycle completed", { eligibility: state.eligibility, blockers: state.blockers });
    } finally {
      running = false;
      disableDuringRun(false);
      renderGate();
    }
  }

  async function reexecuteEvidenceTasks() {
    const ids = ["T2", "T3", "T4", "T5", "T6"];
    for (const id of ids) {
      const taskObj = state.plan.find((t) => t.id === id);
      if (!taskObj) continue;
      taskObj.status = "planned";
      await executeTask(taskObj);
    }
  }

  async function approveRelease() {
    if (running || state.eligibility !== "eligible") return;
    running = true;
    disableDuringRun(true);
    state.humanApproval = { approved: true, actor: "browser_user", timestamp: nowIso(), scope: "10_percent_canary_only" };
    state.eligibility = "approved";
    setGraphStatus(5, "passed", "Human approved a 10% canary only");
    addEvent("human.approval", "Human Authority", "passed", "Human approves bounded canary", state.humanApproval);
    renderGate();
    try {
      setGraphStatus(6, "running", "Executing canary then verifying operational health");
      const canary = await toolGateway("release.canary", { taskId: "RELEASE", goal: state.goal, sandbox: state.sandbox, specialist: "Deployment Verifier" });
      if (!canary.ok) throw new Error(canary.error || "Canary action failed");
      const verification = await toolGateway("telemetry.verify", { taskId: "VERIFY", goal: state.goal, sandbox: state.sandbox, specialist: "Deployment Verifier" });
      state.release.verified = Boolean(verification.output?.passed);
      state.release.state = state.release.verified ? "canary_verified" : "canary_failed";
      setGraphStatus(6, state.release.verified ? "passed" : "failed", state.release.verified ? `Canary health ${verification.output.canaryHealth}%` : `Canary health ${verification.output.canaryHealth}% requires rollback`);
      addEvent("release.verification", "Deployment Verifier", state.release.verified ? "passed" : "failed", state.release.verified ? "Canary verification passed" : "Canary verification failed", verification.output);
      setStatus(state.release.verified ? "eligible" : "blocked");
    } catch (error) {
      addEvent("release.error", "Deployment Verifier", "failed", "Canary release failed", { error: error.message });
      state.release.state = "canary_failed";
      setStatus("blocked");
    } finally {
      running = false;
      disableDuringRun(false);
      renderGate();
      renderStats();
    }
  }

  async function promoteRelease() {
    if (running || !state.release.verified || state.release.promoted) return;
    running = true;
    disableDuringRun(true);
    try {
      const evt = addEvent("human.approval", "Human Authority", "passed", "Human approves full promotion", { previousCanaryVerified: true, timestamp: nowIso() });
      const result = await toolGateway("release.promote", { taskId: "PROMOTE", goal: state.goal, sandbox: state.sandbox, specialist: "Deployment Verifier" });
      updateEvent(evt, result.ok ? "complete" : "failed", { promotionResult: result });
      if (result.ok) {
        state.release.state = "full_release";
        state.release.promoted = true;
        setStatus("complete");
        setGraphStatus(6, "passed", "100% traffic promoted with rollback retained");
      }
    } finally {
      running = false;
      disableDuringRun(false);
      renderGate();
      renderStats();
    }
  }

  function disableDuringRun(disabled) {
    els.run.disabled = disabled;
    els.loadFailure.disabled = disabled;
    els.reset.disabled = disabled;
    [els.goal, els.coverage, els.evalRate, els.observability, els.promptAttack, els.toolFailure, els.rollbackReady, els.privilegeScoped].forEach((el) => { el.disabled = disabled; });
    if (disabled) {
      els.remediate.disabled = true;
      els.approve.disabled = true;
      els.promote.disabled = true;
    }
  }

  function simpleHash(text) {
    let hash = 0;
    for (let i = 0; i < text.length; i += 1) hash = ((hash << 5) - hash + text.charCodeAt(i)) | 0;
    return `h${Math.abs(hash).toString(16)}`;
  }

  function uniqueById(items) {
    const seen = new Set();
    return items.filter((item) => item && !seen.has(item.id) && seen.add(item.id));
  }

  function downloadState() {
    if (!state.runId) return;
    const blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${state.runId}-f36-state.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  els.run.addEventListener("click", runFull);
  els.loadFailure.addEventListener("click", loadFailureCase);
  els.reset.addEventListener("click", () => resetState(false));
  els.download.addEventListener("click", downloadState);
  els.remediate.addEventListener("click", runRemediation);
  els.approve.addEventListener("click", approveRelease);
  els.promote.addEventListener("click", promoteRelease);
  [els.coverage, els.evalRate, els.observability].forEach((el) => el.addEventListener("input", renderSliders));

  renderGraph();
  renderRegistry();
  loadBaseline();
  renderStats();
  renderGate();
})();
