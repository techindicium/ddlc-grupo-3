# Route decision: REQUEST-007 (exploratory)

Skill: `route`, exploratory. Run: 2026-10-05.

## Path

**B, definition change.** Proposed, not confirmed.

Reasons:

- The mart implements v2; the definition in force is v3.
- The consumer's previous figure (July) was taken from the same mart, so the version the consumer
  last received is v2 if the mart was unchanged, which is not recorded.
- v3 is not computable from the extract (no `human_edit_material`, no reopen time). Path B needs a
  field from Portal engineering before any model change can be written.

Path A would apply only if the metric owner and the requester decide the August figure is v2,
labelled as v2 and superseded.

## Autonomy

Agent may build in a scratch clone and draft a labelled figure file for evidence. It may not change
a published definition, change the track's models, drop a table, or publish.

## Reviewers

- Metric owner: Sofia Marques, to confirm the path and the version.
- Second reader of any model change: Declan Byrne or another analytics member who did not write it.

## Result

`escalated`. Path B needs the metric owner's confirmation.
