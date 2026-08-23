# Security Policy

## Purpose

The Agentic AI Library contains reference implementations for agentic AI and multi-agent systems. Security reports that affect this repository or any linked standalone system are taken seriously.

## Supported branch

Security fixes are maintained on the default `main` branch unless a repository-specific policy states otherwise.

## Reporting a vulnerability

Please do not open a public issue for an unpatched vulnerability, exposed secret, authentication weakness, unsafe tool permission, prompt-injection path, data-exfiltration path, privilege-escalation path, or other security-sensitive finding.

Use GitHub's private vulnerability reporting feature when it is available for the affected repository. If private reporting is not available, contact the repository owner privately through an appropriate verified channel before public disclosure.

A useful report should include:

- affected repository and file or component
- clear description of the issue
- impact and realistic attack conditions
- minimal reproduction steps or proof of concept
- affected versions or commits when known
- suggested remediation when available

## Agentic AI security scope

Security review for this library includes conventional software vulnerabilities and agent-specific risks such as:

- prompt injection and instruction hierarchy failures
- unsafe or overprivileged tool use
- secret or credential exposure
- unauthorized external actions
- cross-agent privilege escalation
- memory poisoning and untrusted state propagation
- data exfiltration through tools, logs, or generated content
- insecure retrieval or untrusted document ingestion
- supply-chain compromise
- unsafe code execution
- missing authorization gates
- audit-log tampering
- control bypass and fail-open behavior

## Responsible disclosure

Please allow reasonable time for investigation and remediation before public disclosure. Good-faith security research that avoids privacy violations, data destruction, service disruption, and unauthorized access is appreciated.

## Security design principle

Consequential actions should use least privilege, explicit authorization, traceable evidence, deterministic controls where possible, and fail-closed behavior when required evidence or approval is missing.
