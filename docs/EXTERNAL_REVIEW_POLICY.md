# External Review Policy

## Purpose

External review helps the Multi-Agent AI Atlas distinguish internal engineering evidence from independent scrutiny. A review may challenge one system, one evaluation, one safety boundary, one domain assumption, or a defined part of the shared standard. It does not need to endorse the entire collection.

## What qualifies as a recorded review

A public review record should include:

- reviewer name or an authorized organization identifier
- relevant expertise or review perspective
- system, artifact, claim, or release reviewed
- review scope and explicit exclusions
- date and version or commit
- findings, limitations, and unresolved questions
- maintainer response and disposition
- reviewer permission for public attribution

Anonymous comments, social reactions, automated scores, and private conversations are not listed as independent review evidence.

## Review categories

- architecture and orchestration
- evaluation and reproducibility
- security and tool authorization
- safety and human authority
- domain assumptions and professional boundaries
- documentation and teaching suitability
- accessibility and developer experience

## Independence and conflicts

Reviewers should disclose financial, employment, research, personal, or implementation relationships that could reasonably affect interpretation. Paid review may still be useful, but it must be labeled as commissioned rather than independent.

## Corrections

Confirmed errors are corrected through normal repository history. Material corrections should identify the affected artifact, the evidence considered, the change made, and the release or commit containing the correction.

## Security exception

Unpatched security vulnerabilities must follow `SECURITY.md` and should not be disclosed through a public review issue.
