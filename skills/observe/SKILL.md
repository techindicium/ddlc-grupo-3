---
name: observe
description: Use after a published figure has gone into a pack or another consumer's work, to check how it was used, whether anyone questioned it, and whether it should close, be corrected, or be retired.
---

# Observe

## Purpose
Find out what happened after handoff. INCIDENT-03 shows the current observation channel: a
customer asks why the number moved, and it takes two days to answer.

## Entry conditions
- Item is `published`: `handoff-record.md` exists and the consumer's pack or report has gone out.

## Required context
- `evidence/<ITEM>/` files and `state/consumers.md`.
- Customer tickets that mention the metric or the pack (read through the extract or the service
  desk, never a live endpoint).
- The next period's figure for the same metric and account, once it exists.

## Prohibited context
- Editing the published figure. A correction is a new linked item.

## Procedure
1. List questions or tickets about the figure since handoff.
2. For each question, check that it can be answered from the evidence files alone. Record the time
   it took.
3. Ask each consumer in the register whether they pinned the version.
4. When the next period exists, compare the figures and note whether a change comes from the
   account's behaviour or from the measure.
5. Write `evidence/<ITEM>/observation.md` and append a row to `state/transitions.md`.

## Evidence produced
- `evidence/<ITEM>/observation.md`: questions received, answerable from evidence (yes or no),
  consumers pinned (yes, no, unknown), next-period comparison.

## Proposed transition
- `closed` after one observation window with no unresolved question.
- `correction-required` when the figure is shown to be wrong; opens a new linked item.
- `retired` when the definition version is superseded and consumers are told.

## Stop or escalation conditions
- A consumer question cannot be answered from the recorded evidence within one business day:
  escalate to the metric owner.
- A consumer is found who is not in the register: record them and escalate under `POLICY-05`.

## Human judgment boundary
Whether a figure is wrong, and whether to retire a version, is the metric owner's decision.
