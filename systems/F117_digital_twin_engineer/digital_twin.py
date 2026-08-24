"""Deterministic flagship demonstration for F117 Digital Twin Engineer.

The module models decision support only. It never connects to industrial
equipment, issues commands, changes setpoints, or bypasses site procedures.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List


class TwinInputError(ValueError):
    """Raised when the digital twin cannot establish trustworthy input state."""


@dataclass(frozen=True)
class AssetLimits:
    temperature_warning_c: float = 80.0
    temperature_trip_c: float = 95.0
    vibration_warning_mm_s: float = 4.5
    vibration_trip_mm_s: float = 7.1
    current_warning_a: float = 32.0
    max_telemetry_age_seconds: int = 120


@dataclass(frozen=True)
class Telemetry:
    asset_id: str
    observed_at: str
    temperature_c: float
    vibration_mm_s: float
    current_a: float
    speed_rpm: float
    throughput_units_min: float
    source: str


@dataclass
class TraceEvent:
    sequence: int
    agent: str
    action: str
    evidence: List[str]
    outcome: str


@dataclass
class TwinResult:
    system_id: str = "F117"
    system_name: str = "Agentic Digital Twin Engineer"
    asset_id: str = ""
    state: Dict[str, Any] = field(default_factory=dict)
    hypotheses: List[Dict[str, Any]] = field(default_factory=list)
    simulations: List[Dict[str, Any]] = field(default_factory=list)
    recommendation: Dict[str, Any] = field(default_factory=dict)
    governance: Dict[str, Any] = field(default_factory=dict)
    trace: List[Dict[str, Any]] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)
    status: str = "DRAFT - AUTHORIZED ENGINEER REVIEW REQUIRED"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _parse_time(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise TwinInputError("observed_at must be an ISO 8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise TwinInputError("observed_at must include a timezone")
    return parsed.astimezone(timezone.utc)


def _telemetry_from_case(case: Dict[str, Any]) -> Telemetry:
    required = {
        "asset_id", "observed_at", "temperature_c", "vibration_mm_s",
        "current_a", "speed_rpm", "throughput_units_min", "source",
    }
    missing = sorted(required - set(case))
    if missing:
        raise TwinInputError("Missing telemetry fields: " + ", ".join(missing))
    telemetry = Telemetry(**{name: case[name] for name in required})
    numeric = {
        "temperature_c": telemetry.temperature_c,
        "vibration_mm_s": telemetry.vibration_mm_s,
        "current_a": telemetry.current_a,
        "speed_rpm": telemetry.speed_rpm,
        "throughput_units_min": telemetry.throughput_units_min,
    }
    invalid = [name for name, value in numeric.items() if not isinstance(value, (int, float)) or value < 0]
    if invalid:
        raise TwinInputError("Invalid nonnegative numeric telemetry: " + ", ".join(invalid))
    if not telemetry.asset_id.strip() or not telemetry.source.strip():
        raise TwinInputError("asset_id and source must be nonempty")
    return telemetry


def _record(trace: List[TraceEvent], agent: str, action: str, evidence: List[str], outcome: str) -> None:
    trace.append(TraceEvent(len(trace) + 1, agent, action, evidence, outcome))


def _state_estimate(telemetry: Telemetry, limits: AssetLimits, now: datetime, trace: List[TraceEvent]) -> Dict[str, Any]:
    observed = _parse_time(telemetry.observed_at)
    age = max(0.0, (now - observed).total_seconds())
    if age > limits.max_telemetry_age_seconds:
        raise TwinInputError(f"Telemetry is stale: {age:.0f} seconds old")
    ratios = {
        "temperature": telemetry.temperature_c / limits.temperature_warning_c,
        "vibration": telemetry.vibration_mm_s / limits.vibration_warning_mm_s,
        "current": telemetry.current_a / limits.current_warning_a,
    }
    trip = telemetry.temperature_c >= limits.temperature_trip_c or telemetry.vibration_mm_s >= limits.vibration_trip_mm_s
    warning_count = sum(value >= 1.0 for value in ratios.values())
    condition = "TRIP_THRESHOLD_EXCEEDED" if trip else "DEGRADED" if warning_count else "NOMINAL"
    confidence = round(min(0.99, 0.72 + 0.08 * warning_count + (0.08 if trip else 0)), 2)
    state = {
        "condition": condition,
        "confidence": confidence,
        "telemetry_age_seconds": round(age, 1),
        "warning_ratios": {key: round(value, 2) for key, value in ratios.items()},
        "trip_threshold_exceeded": trip,
    }
    _record(trace, "State Estimator", "construct current asset state", [telemetry.source, telemetry.observed_at], condition)
    return state


def _diagnose(telemetry: Telemetry, state: Dict[str, Any], trace: List[TraceEvent]) -> List[Dict[str, Any]]:
    vibration_signal = min(1.0, telemetry.vibration_mm_s / 7.1)
    heat_signal = min(1.0, telemetry.temperature_c / 95.0)
    current_signal = min(1.0, telemetry.current_a / 32.0)
    hypotheses = [
        {"cause": "bearing degradation or lubrication loss", "confidence": round(0.45 * vibration_signal + 0.35 * heat_signal + 0.20 * current_signal, 2), "supporting_evidence": ["elevated vibration", "elevated temperature", "increased motor current"]},
        {"cause": "mechanical misalignment", "confidence": round(0.55 * vibration_signal + 0.15 * heat_signal + 0.10, 2), "supporting_evidence": ["elevated vibration", "stable speed measurement"]},
        {"cause": "process overload", "confidence": round(0.45 * current_signal + 0.25 * heat_signal, 2), "supporting_evidence": ["increased motor current", "thermal load"]},
    ]
    hypotheses.sort(key=lambda item: item["confidence"], reverse=True)
    _record(trace, "Diagnosis Agent", "rank competing failure hypotheses", list(state["warning_ratios"]), hypotheses[0]["cause"])
    return hypotheses


def _simulate(telemetry: Telemetry, state: Dict[str, Any], trace: List[TraceEvent]) -> List[Dict[str, Any]]:
    severity = max(state["warning_ratios"].values())
    options = [
        {"option": "continue_and_monitor", "projected_risk": "CRITICAL" if severity >= 1.45 else "HIGH", "projected_temperature_c": round(telemetry.temperature_c + 8.0 * severity, 1), "projected_throughput_units_min": telemetry.throughput_units_min, "assumptions": ["load remains constant", "degradation does not accelerate"]},
        {"option": "derate_to_70_percent", "projected_risk": "MEDIUM", "projected_temperature_c": round(max(25.0, telemetry.temperature_c - 9.0), 1), "projected_throughput_units_min": round(telemetry.throughput_units_min * 0.70, 1), "assumptions": ["site controls permit derating", "reduced load lowers thermal stress"]},
        {"option": "controlled_stop_and_inspection", "projected_risk": "LOW", "projected_temperature_c": round(max(25.0, telemetry.temperature_c - 18.0), 1), "projected_throughput_units_min": 0.0, "assumptions": ["authorized site procedure is followed", "inspection occurs before restart"]},
    ]
    _record(trace, "Simulation Agent", "compare three what-if response options", ["current twin state", "declared scenario assumptions"], "controlled_stop_and_inspection has lowest projected risk")
    return options


def _govern(case: Dict[str, Any], state: Dict[str, Any], recommendation: str, trace: List[TraceEvent]) -> Dict[str, Any]:
    protected_actions = {"derate_to_70_percent", "controlled_stop_and_inspection"}
    approval = case.get("approval") or {}
    valid_approval = approval.get("approved") is True and approval.get("role") == "authorized_engineer" and bool(approval.get("approver")) and bool(approval.get("procedure_reference"))
    needs_approval = recommendation in protected_actions
    blocked = needs_approval and not valid_approval
    governance = {
        "protected_action": needs_approval,
        "approval_valid": valid_approval,
        "execution_blocked": blocked,
        "command_issued": False,
        "required_role": "authorized_engineer" if needs_approval else None,
        "site_procedure_required": needs_approval,
        "reason": "This reference system cannot command equipment or change setpoints.",
    }
    outcome = "BLOCKED_PENDING_ENGINEER_APPROVAL" if blocked else "AUTHORIZED_FOR_SITE_PROCEDURE" if needs_approval else "DECISION_SUPPORT_ONLY"
    _record(trace, "Deployment Gatekeeper", "enforce protected-action boundary", [state["condition"], recommendation], outcome)
    return governance


def run_twin(case: Dict[str, Any], now: datetime | None = None) -> TwinResult:
    """Run the deterministic F117 flagship scenario."""
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    trace: List[TraceEvent] = []
    telemetry = _telemetry_from_case(case)
    _record(trace, "Telemetry Interface Agent", "validate telemetry contract", [telemetry.source], "VALID")
    state = _state_estimate(telemetry, AssetLimits(), now, trace)
    hypotheses = _diagnose(telemetry, state, trace)
    simulations = _simulate(telemetry, state, trace)
    recommendation = "continue_and_monitor"
    rationale = "The observed state remains below warning thresholds."
    if state["condition"] == "DEGRADED":
        recommendation = "derate_to_70_percent"
        rationale = "Multiple warning signals indicate a degraded state while trip thresholds remain unconfirmed."
    if state["condition"] == "TRIP_THRESHOLD_EXCEEDED":
        recommendation = "controlled_stop_and_inspection"
        rationale = "A declared trip threshold is exceeded. Continuing operation has the highest projected risk."
    governance = _govern(case, state, recommendation, trace)
    status = "DECISION SUPPORT COMPLETE"
    if governance["execution_blocked"]:
        status = "AWAITING AUTHORIZED ENGINEER APPROVAL"
    elif governance["protected_action"]:
        status = "AUTHORIZED FOR SITE PROCEDURE - NO COMMAND ISSUED"
    return TwinResult(
        asset_id=telemetry.asset_id,
        state=state,
        hypotheses=hypotheses,
        simulations=simulations,
        recommendation={"action": recommendation, "rationale": rationale},
        governance=governance,
        trace=[asdict(event) for event in trace],
        limitations=["Synthetic deterministic model for architecture demonstration only.", "Not a validated physics model, safety function, maintenance instruction, or control system.", "Site data, asset specifications, qualified engineering review, and approved procedures are required."],
        status=status,
    )
