# Appellate case preparation

Create a case folder under `years/YYYY/cases/<case-slug>/`. This template describes separate files; do not send a combined completed template to the neutral modeler. One live version of each input is maintained, with superseded versions preserved in Git.

## File: neutral.md

### Identity and assignment

- Historical case caption, docket, and source citation.
- Coverage cycle, primary group from the [selection policy](CASE_SELECTION.md), and secondary subjects; principal question, selection reason, and reference to the canonical annual case-list entry. Do not include that entry's Departure column or other outcome-revealing material in the neutral packet.
- Lower tribunal, judgment or order under review, and requested appellate relief.
- Historical argument/submission date; simulation argument/submission date; proposed event date; basis for any difference.
- Historical panel, each judge's status, and source proving membership. Put the panel's result, author, and joins only in `history.md`.
- Member Stone replaces; assignment method and reason; resulting panel.
- Qualification, recusal, designation, quorum, and timing checks. If a different second replacement is necessary, justify it separately.

### Record and issues

- Material facts and their source; distinguish findings, allegations, disputed evidence, and stipulations.
- Issues actually raised and preserved; waiver, forfeiture, exhaustion, or other relevant limitation.
- Appellate jurisdiction, timeliness, finality or other route to review.
- For each issue: governing standard of review, burden, relevant error rule, and relief available at this posture.
- Strongest supported position of each side and material alternative grounds.
- Missing facts, documents, or findings; any explicit bounded assumption and whether it could affect the result.

### Law entering the event

- Exact legal cutoff and sources checked.
- Relevant historical Supreme Court authority available by then.
- Relevant historical circuit and other governing authority, with current status.
- Effective earlier simulation holdings and links to the final records, including same-year decisions.
- Material open question, conflicting authority, or intervening legal development.
- Lawful disposition and remedy paths; no judicial vote prediction.

### Sources and neutral handoff

Give primary-source links and pinpoints sufficient to verify the material propositions. When facts were extracted from the historical opinion under simulation, identify their provenance without handing that opinion's result to the modeler. Supply a sanitized extract rather than directing the modeler to read the full comparator. Separate lower-court rulings that are legitimately part of the record from the current appellate outcome that must remain withheld.

Exclude Stone's private proposal, personal jurisprudence and biography, the selected appellate event's historical result and voting alignment, and later Supreme Court events. Case identity may permit latent familiarity; do not claim the model has no prior knowledge. The enforced boundary is the material supplied or retrieved during the scoped stage.

## File: stone.md

### Status

- Version and approval status: proposed or user-approved.
- Actual approval reference and date, if approved.
- Legal cutoff and any conditions or delegated choices.

### Stone's position

For each separable issue or judgment component, state jurisdiction and reach; disposition; sufficient reasoning and controlling authorities; proposed holding; remedy and remand instructions; scope, qualifications, and reserved questions; and any approved fallback or acceptable narrower join.

Distinguish what binding law requires, what is open to this court, and what Stone would urge another court to change. His personal view does not authorize ignoring precedent. Do not infer a missing user-controlled position from the jurisprudence document or an old project permission.

## File: history.md

Record only the selected historical appellate event's verified disposition, panel, author and joins, holdings, separate writings, remedy, and sources. Identify material differences between that event's premises and the neutral packet. This file is introduced only after neutral commitments are frozen.

Put later historical rehearing and Supreme Court outcomes in a separate optional `historical-follow-up.md`. That file is for due-date follow-up research, not initial neutral modeling, reconciliation, or assembly. Historical outcomes cannot leak backward through an undifferentiated case-history block.

## Files created by Run

- `commitments.md`: non-Stone judges' concise independently modeled dispositions, grounds, sources, remedy positions, and join limits; neutral context identifier and allowed inputs.
- `reconciled.md`: frozen final positions after historical comparison; specific bases for departures or unresolved uncertainty; separate context identifier and allowed inputs.
- `events/YYYY-MM-DD-<event>.md`: final record using the [decision template](templates/DECISION_RECORD.md). A later rehearing or remand is a separate event, not an overwrite of a valid earlier decision.
- Optional `output/YYYY-MM-DD-<event>.md`: readable presentation after the record is locked, under the [render contract](RENDER_CONTRACT.md).

Record preparation or execution identifiers internally and accurately. Do not claim a context was isolated merely because the corresponding files exist. Do not create empty Run outputs to imply that a case has been adjudicated.
