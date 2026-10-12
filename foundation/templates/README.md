# Reusable templates

| Template | Used for | Output location |
|---|---|---|
| [Standing State](STANDING_STATE.md) | Current court, coverage cycles, pending proceedings, and carryovers | `state/STANDING_STATE.md` |
| [Case brief](../CASE_BRIEF_TEMPLATE.md) | Separate neutral packet, Stone proposal, and historical comparator | `years/YYYY/cases/<case-slug>/neutral.md`, `stone.md`, and `history.md` |
| [Decision record](DECISION_RECORD.md) | Authoritative completed event, holdings, tests, remedy, and provenance | The case's `events/YYYY-MM-DD-<event>.md` |
| [Render](RENDER.md) | Readable merits decision or procedural event, projected from the final record | The case's `output/YYYY-MM-DD-<event>.md` |
| [Annual case list](CASE_LIST.md) | One canonical selection entry per historical case | `years/YYYY/case-list.md` |

The case-brief template remains at its existing canonical path; this index links to it rather than duplicating it. Forms contain instructions and placeholders, not completed cases or current state.

There is no separate Holdings or Standards and Tests document. Each final decision record preserves the actual holding, applied legal test, review standard, burdens, and qualifications. `state/PRECEDENT.md` is a short navigation and subsequent-treatment index. It is not a replacement source of legal rules. Standing State tracks procedure and institutional setting, not a second legal digest.
