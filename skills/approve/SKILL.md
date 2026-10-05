---
name: approve
description: Use when a verified figure needs an approval decision. Prepares the approval request for the metric owner and records the decision only after a named human has made it. Never records an approval that did not happen.
---

# Approve

## Purpose
Put the decision in front of the person who owns it, with the evidence attached, and record what
they decided. The approval is the human's; the skill prepares it and writes it down.

## Entry conditions
- Item is `verified`: `verification-report.md` exists, every check passes, and a second reader is
  named in it.

## Required context
- `evidence/<ITEM>/verification-report.md`, `intake-record.md`, `route-decision.md`.
- `docs/policies.md` for `POLICY-05`, `POLICY-06`, `POLICY-13`.

## Prohibited context
- Any message, chat or memory as evidence of approval. Only a decision the approver writes or
  confirms in this repository counts.

## Procedure
1. Draft `evidence/<ITEM>/approval-request.md`: metric, version, period, audience, the figure file,
   the verification report, the policies that apply and whether each is met.
2. Name the approver: the metric owner (`metric-definitions.yaml` owner field), and the `POLICY-06`
   approver if a mart was dropped.
3. Stop and wait.
4. When the approver decides, record `evidence/<ITEM>/approval-record.md` with their name, role,
   date, decision (approved, refused, approved with conditions) and conditions, in their words.
5. Append a row to `state/transitions.md` naming the approver as the actor.

## Evidence produced
- `evidence/<ITEM>/approval-request.md` (always).
- `evidence/<ITEM>/approval-record.md` (only after a human decision).

## Proposed transition
- `approved`, `rejected` or `correction-required`, as the approver decided.
- Without a decision the item stays `verified`.

## Stop or escalation conditions
- No named approver is available: stop. Do not substitute the requester or the author.
- The approver is the author of the model change: stop and ask for another approver.
- Asked to record an approval that the approver did not give: refuse.

## Human judgment boundary
Whether a figure is fit to leave the team, and for which audience, is the metric owner's decision.
This skill has no authority to approve.
