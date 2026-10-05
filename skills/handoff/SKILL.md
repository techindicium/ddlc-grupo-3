---
name: handoff
description: Use when an approved figure is to be delivered to the requesting team. Delivers a file that names metric, version, period and extract, and records who received it as a consumer.
---

# Handoff

## Purpose
Deliver the figure as a file that can answer "where did this number come from" in three months.
Today the handoff is a CSV or a pasted message, and "then there is no file" (interview).

## Entry conditions
- Item is `approved`: `approval-record.md` exists, written from a named human decision.

## Required context
- `evidence/<ITEM>/approval-record.md`, `figure-draft.csv`, `intake-record.md`.
- The consumer register (`state/consumers.md`, created on first handoff if absent).

## Prohibited context
- Delivering a number in a message body without the file.
- Changing any value in the figure file after approval.

## Procedure
1. Check that the figure file carries `metric`, `version`, `period` and `extract_taken_at` on every
   row (`POLICY-13`, identifiers rule).
2. Record the file's checksum.
3. Deliver the file to the requester named in the intake record.
4. Add or update the consumer register: consumer, metric, version, period, date delivered.
5. Write `evidence/<ITEM>/handoff-record.md` and append a row to `state/transitions.md`.

## Evidence produced
- `evidence/<ITEM>/handoff-record.md`: recipient, channel, file, checksum, date.
- A row in `state/consumers.md`.

## Proposed transition
- `published`.

## Stop or escalation conditions
- Any row lacks metric or version: stop. That is the failure in INCIDENT-03.
- Approval has conditions that are not met: stop.
- The recipient asks for the number in a message instead of the file: send the file anyway and
  record the request.

## Human judgment boundary
None beyond the approval already recorded. A request to change a value after approval sends the
item back to `correction-required`.
