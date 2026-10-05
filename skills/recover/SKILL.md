---
name: recover
description: Use when a figure request is blocked, escalated, needs correction, or was rejected. Classifies the failure, applies the retry limit for its class, and either returns the item to the stage that failed or hands the decision to a named person.
---

# Recover

## Purpose
Handle the item when the happy path stops, without restarting from scratch and without guessing
the missing fact.

## Entry conditions
- Item is in `blocked`, `escalated`, `correction-required` or `rejected`, and the evidence file of
  the stage that stopped names the reason.

## Required context
- All files in `evidence/<ITEM>/`, and `state/transitions.md` rows for the item.
- The failure and recovery table in `lifecycle.md`.

## Prohibited context
- Filling a missing fact with an estimate. An empty field is information.
- Editing `docs/incidents/` or `docs/pr-notes/` to make sources agree.

## Procedure
1. Classify the failure: underspecified request, duplicate, stale or short extract, schema drift,
   missing source field, model does not match definition, shape test failure, contradiction,
   refused approval.
2. Attribute the cause: specification, data, model, process, or fixture.
3. Count previous attempts for this class from `state/transitions.md`.
4. If under the retry limit and the fix is within the route's autonomy: describe the action and
   return the item to the stage that failed.
5. Otherwise: write the decision needed, the options, the evidence for each, and the person who
   owns it. Move the item to `escalated`. To prepare the evidence for each option, `context`, `act`
   and `verify` may be run in exploratory mode. Their outputs are labelled `exploratory` and do not
   move the item's state.
6. Write or append `evidence/<ITEM>/recovery-log.md` and append a row to `state/transitions.md`.

## Evidence produced
- `evidence/<ITEM>/recovery-log.md`: failure class, cause, attempt number, action or decision
  requested, owner.

## Proposed transition
- Back to `bounded`, `context-assembled` or `routed` after a recoverable fix.
- `escalated` when the retry limit is reached or the decision is a human's.
- `rejected`, `merged` or `retired` only when a human decided it.

## Stop or escalation conditions
- Retry limit reached for the class: escalate.
- The recovery would need a decision listed in the human judgment table: escalate.
- The same item has been escalated twice for the same question without an answer: stop and flag the
  due date risk to the requester.

## Human judgment boundary
Recovery never resolves a contradiction, chooses a version, or decides a duplicate. It prepares the
question and names who answers it.
