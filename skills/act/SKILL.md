---
name: act
description: Use when a routed figure request is ready to be built. Runs the warehouse build on the validated extract and drafts a figure file that carries metric, version, period and extract date.
---

# Act

## Purpose
Produce the figure. The build is the one step that already works; this skill adds the record that
the current process loses: the full output and a figure file that names what it is.

## Entry conditions
- Item is `routed` on path A, or on path B with the model change confirmed by the metric owner.
- The route decision lists what the agent may do.

## Required context
- `evidence/<ITEM>/route-decision.md` and `evidence/<ITEM>/context-manifest.md`.
- The track repository, as a scratch clone. Never build inside the read-only checkout.

## Prohibited context
- Editing `project/metrics/metric-definitions.yaml`, `docs/incidents/`, `docs/pr-notes/` or any
  track file. Model changes on path B are drafted in this repository, not applied to the track.
- `project/rebuild.py` without a named `POLICY-06` approver.
- `--live`. The operational database is not ours to reach.

## Procedure
1. Clone the track repository to a scratch location and run `./scripts/setup.sh`.
2. Run `.venv/bin/python project/run.py`. Save the full output, including the exit code.
3. Query the mart for the requested period and grain.
4. Write `figure-draft.csv` with columns `account_id, period, metric, version, value,
   extract_taken_at`. `version` is the version the mart implements according to the context
   manifest, not the version requested. If they differ, write both and say so.
5. Write rows for non-applicable accounts as `not applicable`, never `0.0` (`ISSUE-32`).
6. Append a row to `state/transitions.md`.

## Evidence produced
- `evidence/<ITEM>/act-build-output.txt`: command, full output, exit code.
- `evidence/<ITEM>/figure-draft.csv`.

## Proposed transition
- `built` when exit code is 0 and the figure file exists.
- `correction-required` when the build or a shape test fails.

## Stop or escalation conditions
- Proceeding would require editing the track repository or a published definition: stop.
- The build fails three times on the same item: stop and escalate.
- The mart's version differs from the requested version: build anyway for evidence, label the
  draft, and leave the decision to verify.

## Human judgment boundary
Whether a model change is applied to the track's mart is the metric owner's decision. The skill
drafts; it does not merge.
