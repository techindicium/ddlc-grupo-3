---
name: context
description: Use when a bounded figure request needs its inputs assembled, with source and age recorded for each, before a route is chosen. Detects stale extracts and contradictions between sources.
---

# Context

## Purpose
Assemble every input the figure depends on, record where each came from and how old it is, and
surface the contradictions before anything is built. "The numbers looked plausible" is how March
was built off February's extract.

## Entry conditions
- Item is `bounded`: `evidence/<ITEM>/intake-record.md` names metric, version, period and audience.

## Required context
- The definition block for the requested version in `project/metrics/metric-definitions.yaml`.
- `data/ops-extract/extract-manifest.yaml` and the column headers of every extract CSV.
- The staging and mart SQL that compute the metric.
- `docs/policies.md`, `docs/identifiers.md`, `docs/dependencies.md`.
- `docs/incidents/` and `docs/pr-notes/` entries that mention the metric.
- `docs/data-dictionary.xlsx`, read as a secondary source only.

## Prohibited context
- `course-shared/heldout/` and any held-out course material.
- Writing to the track repository. It is read-only.
- Treating `staging.extract_metadata` as the extract date. It records build time.

## Procedure
1. For each artifact read, record path, origin (system, hand-kept, generated) and age. If the age is
   not recorded, write `unknown`.
2. Compare the extract with the period: `taken_at` against the period's last day, and the latest
   event timestamp in the extract against the period's last day.
3. Compare the extract columns with the fields the definition needs (numerator, denominator,
   exclusions). List every field the definition needs that the extract does not carry.
4. Read the mart SQL and note which version's rule it implements. Do not fix it.
5. List applicable policies and say for each whether anything enforces it.
6. List known consumers of the metric, or write that no consumer list exists (`ISSUE-30`).
7. For each fact the item depends on, if two sources disagree, record both and mark it open.
8. Write `evidence/<ITEM>/context-manifest.md` and append a row to `state/transitions.md`.

## Evidence produced
- `evidence/<ITEM>/context-manifest.md`: artifact table, extract coverage, missing fields, mart
  version reading, policies, consumers, contradictions.

## Proposed transition
- `context-assembled` when the extract covers the period, every needed field exists, and no
  contradiction on a dependent fact is open.
- `blocked` when the extract is short or stale, or a needed field is missing.
- `escalated` when a contradiction on a dependent fact is open.

## Stop or escalation conditions
- Extract `taken_at` or latest event is before the period's last day: stop.
- The definition needs a field the extract does not carry: stop.
- Two sources disagree on a fact the item depends on: stop. Do not pick the more plausible one.
- An input has no identifiable source: stop.

## Human judgment boundary
Whether a short extract is acceptable for this audience is decided by the requester with the metric
owner. Which of two contradicting sources is right is decided by the owner of each source.
