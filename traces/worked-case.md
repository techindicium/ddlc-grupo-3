# Worked lifecycle case

Run manually in Claude Code on 2026-10-05, following the skills in `skills/` in order. The track
repository was read in place and built in a scratch clone at `a8aecb4`; the track checkout was not
modified. Every state change is in `state/transitions.md`; every evidence file is in
`evidence/REQUEST-007/`.

## Case

| Field | Value |
| :- | :- |
| Work item | `REQUEST-007`, self-service per account for the August packs (Reporting, Lucia Ferreira, due 2026-09-04) |
| Intended outcome | A per-account August figure for the service review packs that names metric, version, period and extract |
| Starting state | `requested` (inbox row dated 2026-08-11) |
| Final state | `escalated`, waiting on three decisions from the metric owner and the requesters. Not published |

## Trace

| # | Skill invoked | Context read | Evidence produced | Proposed state | Result | Human intervention |
| -: | :- | :- | :- | :- | :- | :- |
| 1 | `intake` | `data/requests/inbox.csv`, `REQUEST-007.docx`, `REQUEST-011.docx`, `metric-definitions.yaml`, `data/tracker.csv` | `intake-record.md` | `blocked` | **Stop.** Version not stated; "same as July" is not a version. Possible duplicate `REQUEST-011` | None available. Needed: requester and metric owner |
| 2 | `recover` | `intake-record.md`, failure table in `lifecycle.md` | `recovery-log.md` (decision request with options) | `escalated` | Retry not within authority. Decision request drafted for Sofia Marques, Lucia Ferreira, Henrik Sole | Decision requested, **not received** |
| 3 | `context` (exploratory) | Extract manifest and CSV headers, staging and mart SQL, change note 0088, INCIDENT-03, interview, policies, identifiers, dependencies, data dictionary | `context-manifest.md` | `blocked` / `escalated` | **Stop.** Extract ends 2026-08-27 18:57. v3 needs `human_edit_material` and reopen time; neither is in the extract. Five contradictions recorded | None |
| 4 | `route` (exploratory) | `intake-record.md`, `context-manifest.md`, blast radius table | `route-decision.md` | `escalated` | Path B (definition change) proposed. Needs metric owner confirmation and a field from Portal engineering | None |
| 5 | `act` (exploratory) | Scratch clone of the track repo | `act-build-output.txt`, `figure-draft.csv` | `built` (exploratory only) | Build exit 0. Six of six tests pass. Draft labelled v2 and "not for publication"; non-pilot rows written as `not applicable` | None |
| 6 | `verify` (exploratory) | All evidence above, definition block, mart SQL | `verification-report.md`, `verify-checks-output.txt` | `escalated` | **Red.** Check 2 (the only one the current process runs) passes. Checks 1, 3, 4, 5, 6 fail | None. No second reader exists for an exploratory run |
| 7 | `approve` | `verification-report.md` | none | stays `escalated` | **Refused to run.** Entry condition is `verified` with every check passing. No approval is recorded because none happened | Would need Sofia Marques |
| 8 | `handoff`, `observe` | none | none | none | Not reached | |

## Failure, refusal, or ambiguity

**What happened:** The request asked for "the same self-service number we had in July". The
definition changed to v3 on 2026-07-01, the mart still computes v2, and July's version was never
recorded. Run anyway, the build is green: `OK: 0 failing test(s)`. The number it produces is the v2
rule, over an extract that stops on 2026-08-27, with 0.0 for four accounts that never had the
portal, and a denominator that counts 10 tickets that are not closed.

**Why the lifecycle did not advance:** `intake` stopped because the version was not stated for a
customer-facing figure and a possible duplicate existed. The exploratory runs confirmed that no
version can be honestly published today: v2 is superseded and its use would have to be labelled
under `POLICY-13`; v3 is not computable from the extract. `approve` refused to run because nothing
was verified. Writing an approval would have recorded a decision nobody made.

**Recovery or escalation:** `recover` escalated three questions to the metric owner with the
requesters, with the evidence for each option: which version, whether `REQUEST-007` and
`REQUEST-011` are the same number, and whether a short extract is acceptable. Two contradictions
were handed over unresolved: why Sunder's figure moved between June and July, and who takes the
extract.

**Where the current process lost the information (the red state):** step 4 of the current-process
table in `lifecycle.md`. The request was registered without a version, and nothing at any later
step asks for one. The build is the only automated check, and it passes on the wrong definition.

## Limitations and next improvement

- The trace stops at `escalated`. The people who own the decisions are fixture characters, so no
  decision can be recorded without inventing one. `approve`, `handoff` and `observe` are written
  but were not exercised on this item.
- The exploratory runs went past a stop on purpose, to give the escalation its evidence. In a
  harness with state enforcement this needs an explicit exploratory mode that cannot publish.
- Check 3 (definition match) is a reading of SQL against prose. It is the check that would have
  caught the drift and it is the least mechanical.
- The state log is a markdown table edited by hand. Nothing refuses a transition without its
  evidence file or a row edited after the fact.
- `SEED-MANIFEST.md` was present in the track repository (it says to delete it before handover)
  and was read. It names two seeded defects; both were also found independently from the
  manifest and the dictionary. Nothing under `course-shared/heldout/` was read.
- Next improvement (Module 2 candidate): a context contract for `context` that refuses to proceed
  when extract coverage does not reach the period's last day, with this case as its failing input.
