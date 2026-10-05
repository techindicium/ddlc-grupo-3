---
name: intake
description: Use when a figure or metric request from another team (REQUEST-NNN in data/requests/inbox.csv) needs to be accepted and bounded before any context is gathered or any model is run.
---

# Intake

## Purpose
Turn a request for a number into a bounded work item: one metric, one definition version, one
period, one audience. Most of what went wrong with `REQUEST-005` and `REQUEST-007` was lost here,
because the request text never named a version or a comparison.

## Entry conditions
- The request has a `REQUEST-NNN` identifier in `data/requests/inbox.csv`. A request that exists
  only in a message has no identifier; stop and ask for it to be registered.
- The requester is named.

## Required context
- The inbox row and the request document in `data/requests/` if one exists.
- `project/metrics/metric-definitions.yaml`, to list the versions of the metric in force.
- Every other open row in `data/requests/inbox.csv` and `data/tracker.csv`, to find duplicates.

## Prohibited context
- Warehouse output and mart SQL. Intake decides what is asked, not how it is computed.
- `course-shared/heldout/` and any held-out course material.

## Procedure
1. Copy the request text verbatim into the intake record.
2. Fill each field from the request: metric name, definition version, period (first and last day),
   grain, audience (internal or customer-facing), needed-by, consumer, non-goals.
3. For every field the request does not state, write `not stated`. Do not infer a version from
   "same as last month".
4. List the versions of the metric in `metric-definitions.yaml` with `effective_from`, and the
   version the previous delivery used if recorded, or `unknown`.
5. Search the inbox and tracker for open requests on the same metric, a synonym, or the same
   period and consumer. List each with its text.
6. Normalise the inbox status spelling in the record only. Do not edit the inbox.
7. Write `evidence/<ITEM>/intake-record.md` and append a row to `state/transitions.md`.

## Evidence produced
- `evidence/<ITEM>/intake-record.md`: request text, the field table, versions in force, possible
  duplicates, and the list of fields that are `not stated`.

## Proposed transition
- `bounded` when metric, version, period and audience are all stated.
- `blocked` (awaiting requester) when any of the four is `not stated`.
- `escalated` when a possible duplicate exists.

## Stop or escalation conditions
- Version, period or audience not stated: stop and draft one question to the requester per field.
- A possible duplicate request exists: stop and escalate to the metric owner.
- The request is for a customer-facing figure and no consumer is named: stop.

## Human judgment boundary
The skill never chooses a definition version for the requester and never decides that two requests
are the same. Version choice belongs to the requester with the metric owner; duplicate resolution
belongs to the metric owner.
