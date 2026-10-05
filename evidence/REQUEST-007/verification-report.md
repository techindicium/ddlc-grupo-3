# Verification report: REQUEST-007 (exploratory)

Skill: `verify`, exploratory, against the draft built from the v2 mart. Run: 2026-10-05.
Queries and raw results: `verify-checks-output.txt`. Build output: `act-build-output.txt`.

Second reader: **none**. This is an exploratory run for the escalation, not a verification of a
figure to publish.

| # | Check | Result | Evidence |
| -: | :- | :- | :- |
| 1 | Coverage: extract reaches 2026-08-31 | **FAIL** | `taken_at` 2026-08-28T09:14:00Z; latest `opened_at` 2026-08-27 18:57. `staging.extract_metadata` reports the build time (2026-10-05) as `extracted_at`, so the warehouse itself cannot answer how old the data is |
| 2 | Load and shape: exit 0, six tests pass | pass | `OK: 0 failing test(s)`, exit code 0 |
| 3 | Definition match: mart implements the requested version | **FAIL** | Requested version not stated. Mart applies the v2 rule on 533 of 533 suggestions. v3 fields absent from the extract |
| 4 | Applicability: non-pilot accounts are not applicable | **FAIL** | `ACCOUNT-1005`, `1007`, `1009`, `1010` carry 0.0 in the mart (`ISSUE-32`). The draft labels them `not applicable` |
| 5 | Denominator: closed tickets in the period | **FAIL** | Mart denominator 418 for August; 408 tickets closed, 10 not closed. The mart counts tickets opened in the month, and the extract has no close date |
| 6 | Continuity: version change against the prior figure is named | **FAIL** | Prior figure's version is unknown. No pack names a version (`POLICY-13`) |

## The red state

Check 2 is the only check the current process runs. It passes. Checks 1, 3, 4, 5 and 6 fail on the
same build. A figure that passes every existing test is not the figure the definition describes,
does not cover the month, and reports non-pilot accounts as failing.

## Result

`escalated`. Checks 1 and 3 require human decisions (see `recovery-log.md`).
