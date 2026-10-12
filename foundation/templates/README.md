# Reusable templates

| Template | Used for | Output location |
|---|---|---|
| [Standing State](STANDING_STATE.md) | Current court, coverage cycles, pending proceedings, and carryovers | `state/STANDING_STATE.md` |
| [Case brief](../CASE_BRIEF_TEMPLATE.md) | Separate neutral packet, Stone proposal, and historical comparator | `years/YYYY/cases/<case-slug>/neutral.md`, `stone.md`, and `history.md` |
| [Decision record](DECISION_RECORD.md) | Authoritative completed event, holdings, tests, remedy, and provenance | The case's `events/YYYY-MM-DD-<event>.md` |
| [Render](RENDER.md) | Automatic eight-section output after every simulation turn; individual decision with written opinions; compact procedural event | `years/YYYY/output/YYYY-MM-DD-court-report.md` or the case's `output/YYYY-MM-DD-<event>.md` |
| [Annual case list](CASE_LIST.md) | One canonical selection entry per historical case | `years/YYYY/case-list.md` |

The court report is displayed directly to the user and saved after every simulation turn, without a separate Render request. It explains the current case, any completed outcome, the reasoning, and supported context; unchanged sections stay brief. The character snapshot is one line of sourced basics. Pending-case explanations and completed opinions are not duplicated, and the opening roster is followed by change-only updates. Panel replacement and a settled case's date-eligible historical comparison appear as separate report context, not in judicial opinions. The report excludes relationship scores, review forecasts, and statistics for unplayed cases. The court report uses a scoped, dated source packet under the render contract. It does not replace Standing State, case lists, or final records. Individual decision renders use only finalized Public decision material. Court reports must not be supplied wholesale to neutral modeling.

The case-brief template remains at its existing canonical path; this index links to it rather than duplicating it. Forms contain instructions and placeholders, not completed cases or current state.

There is no separate Holdings or Standards and Tests document. Each final decision record preserves the actual holding, applied legal test, review standard, burdens, and qualifications. `state/PRECEDENT.md` is a short navigation and subsequent-treatment index. It is not a replacement source of legal rules. Standing State tracks procedure and institutional setting, not a second legal digest.
