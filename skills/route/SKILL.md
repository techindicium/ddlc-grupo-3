---
name: route
description: Use when a figure request has assembled context and the path (standard refresh, definition change, or ad-hoc analysis), the agent's autonomy, and the required reviewers must be chosen.
---

# Route

## Purpose
Choose the path the item takes and how much the agent may do alone, from the work profile rather
than from the due date.

## Entry conditions
- Item is `context-assembled`: `context-manifest.md` exists with no open contradiction.

## Required context
- `evidence/<ITEM>/intake-record.md` and `evidence/<ITEM>/context-manifest.md`.
- `docs/architecture-rules.md`, blast radius table.

## Prohibited context
- New reads of the track repository beyond what the manifest lists. If something is missing, go
  back to `context`.

## Procedure
1. Decide the path:
   - **A, standard refresh.** The mart implements the requested version, the extract covers the
     period, the audience has received this metric before on this version.
   - **B, definition change.** The mart does not implement the requested version, or the version
     differs from the one the consumer last received. Needs a model change, second reader,
     `POLICY-05` announcement, and `POLICY-06` approver if a mart is dropped.
   - **C, ad-hoc analysis.** No existing metric covers the request. Needs a definition first.
2. Set autonomy:
   - Path A: agent may build, compute and draft the figure file. It may not publish.
   - Path B and C: agent may draft SQL and a change note. It may not change a published
     definition, drop a table, or publish.
3. Name the reviewers and the evidence verify must produce.
4. Write `evidence/<ITEM>/route-decision.md` and append a row to `state/transitions.md`.

## Evidence produced
- `evidence/<ITEM>/route-decision.md`: path, reasons, autonomy level, reviewers, required checks.

## Proposed transition
- `routed` for path A.
- `escalated` for path B or C, until the metric owner confirms the path.

## Stop or escalation conditions
- Path B or C: stop and escalate to the metric owner. The agent proposes, the owner confirms.
- Any action that would drop or rebuild a mart: stop. `POLICY-06` needs a named approver and
  `project/rebuild.py` does not ask for one (`ISSUE-37`).

## Human judgment boundary
The metric owner confirms any path other than A. A definition change during an open reporting
period is the metric owner's decision under `POLICY-05`.
