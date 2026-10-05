# Intake record: REQUEST-007

Skill: `intake`. Run: 2026-10-05, Claude Code session operated by Aluizio Cidral.

## Request, verbatim

From `data/requests/REQUEST-007.docx`:

> "The same self-service number we had in July, per account, for the August packs."

From `data/requests/inbox.csv`:

`REQUEST-007,Reporting,Lucia Ferreira,2026-08-11,2026-09-04,open,Self-service per account for the August packs`

## Fields

| Field | Value | Source |
| :- | :- | :- |
| Metric name | `self_service_rate` | Inferred from "self-service"; the only metric with that name in `metric-definitions.yaml` |
| Definition version | **not stated** | The request says "the same number we had in July". It names no version |
| Period | 2026-08-01 to 2026-08-31 | "August packs" |
| Grain | per account (period grain implied monthly) | Request text. The definition says `account-day`; the mart is account-month. Not reconciled |
| Audience | customer-facing | Service review packs go to accounts |
| Requester | Lucia Ferreira, Reporting | inbox |
| Needed by | 2026-09-04 | inbox, tracker and request document agree |
| Consumer | August service review packs | Request text |
| Non-goals | not stated | |

## Versions in force

| Version | Effective from | Status | Rule |
| :- | :- | :- | :- |
| 3 | 2026-07-01 | current | Sent and not materially edited; excludes tickets reopened within 48 hours |
| 2 | 2026-04-01 | superseded by 3 | Every sent suggestion |

Version used for the July figure (`REQUEST-004`): **unknown**. `REQUEST-007.docx` says the July
number came from `marts.self_service` and that "the July packs were built before anyone noticed".

## Possible duplicates

| Item | Text | Scope | Due | Owner |
| :- | :- | :- | :- | :- |
| `REQUEST-011` | "Automation rate for each Enterprise account ... Share of tickets handled without a person." (Henrik Sole) | Enterprise accounts only | 2026-09-04 | none in tracker |

`ISSUE-36` already records that nobody has asked whether they are the same number.

## Fields not stated

- Definition version.
- Non-goals.

## Result

Stop. Version is not stated for a customer-facing figure, and a possible duplicate exists.
Proposed state: `blocked`, then `escalated` (see `recovery-log.md`).
