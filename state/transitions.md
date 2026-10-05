# Transition log

Append-only. One row per state transition. A row is added only when the evidence file it names
exists. Exploratory runs (prepared for an escalation) are logged with `exploratory` in the
`to` column and do not change the item's state.

Correcting a row means appending a new row that says so. Rows are never edited or deleted.

| # | When (UTC) | Item | From | To | Skill | Actor | Evidence | Note |
| -: | :- | :- | :- | :- | :- | :- | :- | :- |
| 1 | 2026-10-05 | REQUEST-007 | (none) | `requested` | (record) | inbox | `data/requests/inbox.csv` row | Received 2026-08-11 per inbox. Recorded here at first trace |
| 2 | 2026-10-05 | REQUEST-007 | `requested` | `blocked` | intake | agent | `evidence/REQUEST-007/intake-record.md` | Version not stated; possible duplicate of REQUEST-011 |
| 3 | 2026-10-05 | REQUEST-007 | `blocked` | `escalated` | recover | agent | `evidence/REQUEST-007/recovery-log.md` | Decisions owed by metric owner and requesters |
| 4 | 2026-10-05 | REQUEST-007 | `escalated` | `exploratory` context | context | agent | `evidence/REQUEST-007/context-manifest.md` | Short extract; v3 fields absent; five contradictions |
| 5 | 2026-10-05 | REQUEST-007 | `escalated` | `exploratory` route | route | agent | `evidence/REQUEST-007/route-decision.md` | Path B proposed, not confirmed |
| 6 | 2026-10-05 | REQUEST-007 | `escalated` | `exploratory` act | act | agent | `evidence/REQUEST-007/act-build-output.txt`, `figure-draft.csv` | Build exit 0, six tests pass, on the v2 rule |
| 7 | 2026-10-05 | REQUEST-007 | `escalated` | `exploratory` verify | verify | agent | `evidence/REQUEST-007/verification-report.md`, `verify-checks-output.txt` | Checks 1, 3, 4, 5, 6 fail; check 2 passes |

Current state of REQUEST-007: **`escalated`**.
