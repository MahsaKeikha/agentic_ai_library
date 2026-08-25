# Multi-Agent System Verification Registry

Version 0.2

This directory stores versioned, machine-readable verification records for systems listed in the Multi-Agent AI Atlas.

## Status discipline

Registry inclusion is not certification. Evidence Intake means public evidence has been mapped, but scoring and hard-gate verification are incomplete. Assessed requires a dated evaluation. Verified requires the stated score threshold and all applicable hard gates within the disclosed scope. Independent review requires a named reviewer, scope, date, and reviewed version.

## Record rules

1. Records identify an exact repository commit.
2. Missing evidence is published alongside supporting evidence.
3. Historical records are preserved.
4. Reassessment creates a new dated record.
5. Suspended or expired status is shown rather than silently removed.
6. Regulatory, legal, security, and production claims require separate evidence.

The public website reads its registry index from `docs/data/verification-registry.json`. Individual records remain in `verification_registry/records`.
