# Appellate presentation contract

The [render template](templates/RENDER.md) supports an eight-section court report, an individual appellate decision, and a compact procedural-event report. Rendering explains established material; it never determines or revises legal substance.

## Default output after each simulation turn

After each turn that prepares or advances a case, adjudicates it, processes follow-up, or advances the simulation calendar, render Form A automatically. Present the report directly to the user and save it. A file link, terse completion message, or case table alone does not fulfill the turn output. A standalone individual opinion or event report is available when specifically requested; it does not otherwise replace the default turn report.

Repository maintenance and explanatory questions do not themselves constitute simulation turns. Rendering does not supply permission to advance the calendar, approve Stone's position, skip isolation stages, or finalize an undecided case.

Make the current case and completed outcome the substantive focus. Explain the dispute, material facts, procedural history, the parties' positions, and the relevant legal framework in ordinary language. After a decision, explain the controlling reasoning, actual disagreements, judgment, remedy, practical consequences established by the record, and remaining questions. Include the supported written opinions for decisions completed in that turn.

Prepare enough sourced public material upstream to support those explanations. The renderer may clarify and connect supplied material, but cannot invent missing case facts or judicial reasoning. Additional context must be date-eligible, relevant, and sourced in the allowed packet; it cannot silently amend a final record. Do not fill the report with speculative reactions, political narratives, or predictions merely because they sound realistic.

Preserve all eight main sections while keeping unchanged or empty sections short. Do not reprint the entire judicial history or all earlier opinions on every turn. A preparation turn explains what awaits decision; a decision turn gives the result and reasoning; a follow-up turn explains the supported procedural development and its effect. No new decision means no fabricated outcome or opinion.

## Court report inputs and boundaries

Form A presents the turn's dated overview at `years/YYYY/output/YYYY-MM-DD-court-report.md`. Further turns on the same simulation date update that date's report, with prior versions preserved in Git; always display the current turn output in the response. Before rendering, prepare an explicit allowed-input packet of sourced extracts limited to:

- Current administrative facts from Standing State and the dated roster.
- Current-session case identities, docket numbers, event dates and types, statuses, and areas of law from canonical case lists and supported case records, excluding future outcomes and historical-result commentary.
- Verified identity, record, procedural status, assignment, parties' positions, sourced date-eligible explanatory context, and open questions for current cases from their neutral preparation material.
- The Public decision sections of finalized event records for completed decisions and operative legal developments.
- Scoped compatibility conclusions from Standing State or final-record follow-up notes, without private proposals, frozen positions, or raw historical-comparator material.
- Verified historical Supreme Court events and public reasoning available by the simulation date, with sources and any case-specific compatibility restriction.

The renderer does not independently research or browse linked raw files. A source link is attribution, not permission to open a document containing excluded material. The preparer must extract and date-check the allowed content. If a preparation field is absent, mark the gap; do not assume the event or assignment exists.

Use exactly the eight main report sections in the template. Section 3 lists the session's cases using No., Caption, Docket(s), Event date, Event type, Status, and Area of law. Do not display chunks, generic MERITS categories, or coverage quota tables; retain selection classifications and counts in their existing background records. Section 5 includes decision summaries and actual written appellate opinions. Section 8 covers Supreme Court cases awaiting argument, awaiting decision, and already decided, including summaries of published reasoning. There is no section 9 or period-close presentation. Omitting that presentation does not change the engine's bookkeeping or annual-close rules.

The report is a dated presentation, not a second editable Standing State or precedent register. It cannot advance time, admit a case, change counts, finalize a decision, or create a pending proceeding. It is not handed wholesale to a neutral modeler. Select only authorized, date-eligible case material and relevant public prior authority for that separate stage.

## Individual decision and procedural-event inputs

Forms B and C read only the final event record's Public decision material, this contract, and the template. They do not read Stone's private input, historical comparison, frozen commitments, the court-report packet, or later case history.

Preserve the caption, docket, court, panel, relevant dates, publication status, posture, material facts, issues, component judgments, named joins, holding, governing standard, authorities, application, qualifications, treatment of precedent, remedy, and mandate status. Include a next step only when established. Use a table only when mixed dispositions or partial joins are clearer that way. A short order does not require the structure of a merits opinion.

## Written opinions

For completed appellate decisions, give an accessible decision summary and the opinion itself in clear judicial prose. Include supported concurrences and dissents as actual prose writings, with their authors and precise joins. Stone's role follows the finalized adjudication; authorship and dissent are not assigned by the template.

Explain the supplied reasoning, including what each authority contributes, the governing test and burdens, the application to the material record, and the supported answer to the principal contrary argument. Do not add findings, arguments, authorities, rationales, holdings, quotations, joins, or remedial instructions absent from the final public material. If the record cannot support a requested passage, return that specific gap for correction rather than completing it through new adjudication.

Distinguish controlling law from a plurality, concurrence, dissent, dicta, and proposed future law. Preserve operative conditions and the difference between permission and obligation. A generated simulation opinion is not a verbatim historical reporter text. Summarize actual Supreme Court reasoning from supplied sources; do not author a substitute Supreme Court opinion.

## Neutrality and chronology

Exclude ideological labels, ally/opponent assignments, favorable-panel probabilities, projected alignments, strategic career goals, invented conference dialogue, and predetermined narrative impact. Relevant dated judicial writings may inform the engine's separate adjudication stages; a court-report personality sketch cannot supply a vote.

Do not disclose future holdings or votes, even when historical research has established them. A scheduled future argument may be listed only if the scheduling information was available by the report date. Questions asked at oral argument do not establish intended votes.

Keep actual Supreme Court law separate from the procedural fate of a selected simulated appeal. A historical grant, hearing, denial, merits disposition, or remand attaches to that appeal only after the engine's compatibility check. An incompatible path remains unresolved; an unknown filing is not a pending proceeding. Once issued, a historical Supreme Court opinion still enters as law under the engine's rules.

## Verification and corrections

Match each presentation to its authorized source material. Keep private approvals, model context identifiers, workflow prompts, and correction provenance out of written judicial opinions. Court-report administrative notes may identify a specific open question but must not expose private deliberations or unavailable future outcomes.

Remove unused instructions and placeholders. Do not invent a public tally, opinion, or procedural event. Identify material gaps explicitly and preserve unaffected output. A corrected source record updates the affected presentation without silently revising unrelated decisions. The event record and verified sources control if a summary conflicts with them.
