# Recovery log: REQUEST-007

Skill: `recover`. Run: 2026-10-05.

## Attempt 1: intake stopped

| Field | Value |
| :- | :- |
| Failure class | Underspecified request; possible duplicate |
| Cause | Specification. The request names no version. A second request may ask for the same number |
| Attempt | 1 |
| Within autonomy? | No. Version choice and duplicate resolution are human decisions |
| Action | Escalate. Gather evidence for each option with exploratory runs of `context`, `act`, `verify` |

## Decision requested

**To:** Sofia Marques (metric owner, owner of `POLICY-05` and `POLICY-13`), with Lucia Ferreira
(requester, `REQUEST-007`) and Henrik Sole (requester, `REQUEST-011`).

**Questions:**

1. Which version does the August figure use?
2. Are `REQUEST-007` and `REQUEST-011` the same number?
3. Is a figure from an extract that ends 2026-08-27 acceptable for the August packs, or is a new
   extract required?

**Options for question 1, with evidence:**

| Option | What it gives | What blocks it | Evidence |
| :- | :- | :- | :- |
| v2, "same as July" | A number computable today from the existing mart, comparable to July if July was v2 | v2 is superseded. Publishing it to customers needs the pack to say "v2, superseded" (`POLICY-13`). July's version is not recorded | `figure-draft.csv`, `verification-report.md` |
| v3, current definition | The number the definitions file says is right | Not computable: extract has no `human_edit_material` and no reopen time. Needs a field from Portal engineering, a mart change, a second reader, and a `POLICY-05` announcement that is already late | `context-manifest.md` |

**Options for question 3:**

| Option | Gap | Owner |
| :- | :- | :- |
| New extract after 2026-08-31 | None; needs whoever runs the export (contradiction on who that is) | Data engineer |
| Partial figure with caveat | 2026-08-28 to 2026-08-31 missing | Requester with metric owner |

## Contradictions handed over, not resolved

- Why Sunder's figure moved June to July: INCIDENT-03 versus change note 0088 and the v2 build.
- Who takes the extract: manifest versus interview.

## State

`escalated`. Retry count for this class: 1. No further retry is within the skill's authority. No
human decision has been recorded.
