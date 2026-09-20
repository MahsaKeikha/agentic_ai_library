# Originality and Cross-Paper Separation Policy

## Purpose

This file prevents the 15-paper program from becoming repetitive, self-plagiarized, or artificially fragmented.

## What may be shared

The papers may share:
- the Multi-Agent AI Atlas as infrastructure
- common notation for agents, tools, evidence, and authority
- public reference architectures
- baseline scenarios when clearly identified
- common software utilities

Shared material must be cited or acknowledged and should not be counted as the new contribution of more than one paper.

## What must be unique

Every paper must have its own:
- primary hypothesis
- formal problem statement
- main theorem or algorithmic contribution when theory is claimed
- paper-specific experiment harness
- benchmark comparison
- main quantitative results
- primary figures
- limitations analysis
- target audience and venue rationale

## Conference versus journal lineage

A journal extension of a conference paper is allowed only when it adds substantial value. Acceptable additions include:
- a materially stronger theorem or proof
- a broader system class
- significant new experiments or real-world data
- new baselines or ablations
- new robustness analysis
- new human-machine evaluation

The journal manuscript must cite the conference version and explicitly explain the new material.

## Claims discipline

Do not use phrases such as "first", "novel", "unprecedented", or "state of the art" until supported by a documented literature search.

Synthetic scenarios must be labeled synthetic. Reference architectures must not be described as deployed systems unless deployment evidence exists. A passing deterministic test is evidence of software behavior, not evidence of real-world safety.

## Result provenance

Every quantitative table should trace to:
1. a committed experiment configuration,
2. a deterministic or seeded run command,
3. raw result files,
4. an analysis script,
5. a figure/table generator,
6. a result manifest containing commit SHA and environment information.

## Paper overlap ledger

Before submission, each manuscript gets a table listing:
- concepts reused from Atlas
- concepts reused from another paper
- text overlap intentionally retained
- datasets/scenarios reused
- figures reused or adapted
- code modules shared
- new material unique to that manuscript
