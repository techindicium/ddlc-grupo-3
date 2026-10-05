---
name: verify
description: Use when a built figure must be checked before approval. Runs the ordered checks (coverage, shape, definition match, applicability, denominator, continuity) and writes a verification report. A green shape-test run is not sufficient evidence.
---

# Verify

## Purpose
Establish that the figure is the number it claims to be. The six shape tests check that a number
is the kind of thing a number should be. They passed on a mart that implements the wrong
definition version. This skill checks the rest.

## Entry conditions
- Item is `built`: `act-build-output.txt` shows exit code 0 and `figure-draft.csv` exists.

## Required context
- `evidence/<ITEM>/` files from intake, context, route and act.
- The definition block for the requested version.
- The mart and staging SQL that compute the metric.

## Prohibited context
- Editing a test, a threshold or the definition to make a check pass.
- `course-shared/heldout/` and any held-out course material.

## Procedure
Run the checks in this order and record each with its query or reading, its result, and the
reader's name.
1. **Coverage.** Extract `taken_at` and latest event timestamp reach the period's last day.
2. **Load and shape.** Exit code 0 and all six shape tests pass. Record, do not stop here.
3. **Definition match.** The mart numerator, denominator and exclusions match the requested
   version's definition, field by field.
4. **Applicability.** Accounts where the metric does not apply carry `not applicable`.
5. **Denominator.** The denominator counts what the definition says (closed tickets in the period),
   not tickets opened.
6. **Continuity.** If the consumer's previous figure used another version, the report names both
   versions and the figure file carries the current one.
7. Write `evidence/<ITEM>/verification-report.md` and append a row to `state/transitions.md`.

## Evidence produced
- `evidence/<ITEM>/verification-report.md`: one row per check, pass or fail, with the evidence.

## Proposed transition
- Proposes `approved` to the metric owner when every check passes. The skill does not make the move.
- `correction-required` when check 2, 4 or 5 fails.
- `escalated` when check 1 or 3 fails, or check 6 shows an unannounced version change.

## Stop or escalation conditions
- Any check fails: stop and report. Do not continue to approval with a failing check.
- Check 3 fails: escalate to the metric owner. Changing the model or the definition is path B.
- The author of the model change is the only available reader: stop. The habit rule says someone
  else reads the SQL.

## Human judgment boundary
The second reader is a person other than the author. The skill prepares the report; the reader
signs it by name. The skill never writes an approval.
