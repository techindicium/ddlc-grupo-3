# Context manifest: REQUEST-007 (exploratory)

Skill: `context`, run in exploratory mode under `recover`, to prepare evidence for the escalated
decision. It does not move the item's state. Run: 2026-10-05.

Track repository: `techindicium/portwell-analytics` at `a8aecb4`, read in place and built in a
scratch clone.

## Artifacts read

| Artifact | Origin | Age |
| :- | :- | :- |
| `data/requests/inbox.csv` | Hand-kept | unknown (no date on file; latest row received 2026-08-26) |
| `data/requests/REQUEST-007.docx`, `REQUEST-011.docx` | Hand-written notes | unknown (document metadata shows a 2013 generator default, not a real date) |
| `data/tracker.csv` | Hand-kept spreadsheet | unknown; latest `last_touched` 2026-08-30 |
| `project/metrics/metric-definitions.yaml` | Source of truth for definitions | `published_at: 2026-08-20` |
| `data/ops-extract/extract-manifest.yaml` and CSVs | Manual export | `taken_at: 2026-08-28T09:14:00Z` |
| `project/models/staging/stg_suggestions.sql`, `marts/self_service.sql` | Code | unknown beyond repo commit 2026-09-09 |
| `docs/pr-notes/0088-self-service-v3.md` | Change note | merged 2026-06-27 |
| `docs/incidents/INCIDENT-03.md` | Incident write-up | written 2026-08-06 |
| `docs/interviews/2026-08-12 Declan Byrne, where the numbers come from.docx` | Interview | 2026-08-12 |
| `docs/policies.md`, `docs/identifiers.md`, `docs/dependencies.md`, `docs/architecture-rules.md` | Hand-kept | unknown |
| `docs/data-dictionary.xlsx` | Hand-kept, secondary | "Last full review: 2026-05-12"; `self_service_rate` row reviewed 2026-04-02 |

## Extract coverage against the period

| Fact | Value |
| :- | :- |
| Period | 2026-08-01 to 2026-08-31 |
| `taken_at` | 2026-08-28T09:14:00Z, before the period ends |
| Latest `opened_at` in extract | 2026-08-27 18:57 |
| Manifest note | "Covers tickets opened before 2026-08-28" |
| Gap | 2026-08-28 to 2026-08-31 not covered |

**Short extract. Stop condition.**

## Fields the definition needs

| Version | Needs | In extract? |
| :- | :- | :- |
| 3 numerator | `proposal_sent`, `human_edit_material` | `sent` yes; `human_edit_material` **no** |
| 3 exclusion | reopen time within 48 hours | **no** (`ticket` has `status` only) |
| 2 and 3 denominator | tickets closed in the period | Only `status`; no close date. Mart counts tickets by opened month |

**Version 3 cannot be computed from this extract. Stop condition.**

## Mart version reading

`stg_suggestions.sql` sets `is_self_served = CAST(sent AS BOOLEAN)`. `marts/self_service.sql` sums
`is_self_served`. That is the version 2 rule. Change note 0088 says the same.

## Policies

| Policy | Applies | Enforced by |
| :- | :- | :- |
| `POLICY-05` announce definition change one period ahead | Yes, v2 to v3 | nothing |
| `POLICY-13` every pack figure names metric and version | Yes, customer-facing | nothing; marts emit bare numbers |
| `POLICY-06` named approver for destructive transformation | Only if a mart is dropped | nothing (`ISSUE-37`) |
| `POLICY-03` EU data transfer basis | Four accounts are EU; aggregated figures only | nothing |

## Consumers known for `self_service_rate`

No consumer list exists (`ISSUE-30`). From INCIDENT-03: service review packs, the help portal
(pins no version), a board slide from `REQUEST-005`.

## Contradictions

| Fact | Source A | Source B | Status |
| :- | :- | :- | :- |
| Why Sunder's figure moved June to July | INCIDENT-03: definition went v2 to v3 | Change note 0088: mart still v2. Our v2 build: Sunder 0.0 in June, 0.3478 in July | open |
| Who takes the extract | Manifest: `taken_by: Declan Byrne` | Interview: someone in support, "usually Joao" | open |
| How the warehouse reads operational data | `docs/how-we-work-today.md`: `ATTACH` the ops database | `project/run.py`: committed extract by default, `--live` optional | open |
| Name of the self-service column | Dictionary: `was_self-served` | Model: `is_self_served` | open |
| Which version the mart serves | Dictionary: `self_service_rate v2` | `metric-definitions.yaml`: v3 current | open (consistent with 0088) |

## Result

Stop. Three stop conditions hold: short extract, v3 fields absent, open contradictions on facts
the item depends on.
