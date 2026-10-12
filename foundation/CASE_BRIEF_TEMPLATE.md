# Appellate case-brief template

Create a case folder under `years/YYYY/cases/<case-slug>/`. Fill the forms below as three separate files: `neutral.md`, `stone.md`, and `history.md`. Replace bracketed fields with supported information and omit inapplicable optional fields. Never send a combined completed template to the neutral modeler. One live version of each input is maintained, with superseded versions preserved in Git.

The brief prepares a case; it does not adjudicate it. Governing tests and review standards are researched here and preserved in the final decision when applied. No separate Holdings or Standards and Tests document is required.

The latest user-approved `stone.md` is the sole source of Stone's case-specific disposition and reasoning. `stone/JURISPRUDENCE.md` is archival storage and must never be read, searched, imported, summarized, embedded, validated, or otherwise used in preparing or processing this brief or any later stage. Do not use engine-generated summaries, cached extracts, embeddings, digests, or other archival derivatives, including existing ones. Use explicit allowed-file lists that exclude the archive and engine-generated archival derivatives. The user's expressly supplied case-specific brief remains an authorized input under the engine's archive exclusion.

## File: neutral.md

### Identity and assignment

**Historical caption:** [Actual parties and case name].
**Circuit:** Second Circuit.
**Docket or citation:** [Verified identifier].
**Admission source:** [Primary-source link and pinpoint establishing this circuit's proceeding].
**Coverage cycle:** [Number].
**Primary group:** [Number and label from the six-group selection policy].
**Secondary subjects:** [Overlapping subfields; or None].
**Principal question:** [Question properly presented for appellate decision].
**Selection reason:** [Coverage and rotation reason, without desired outcome].
**Canonical case-list reference:** [File and case identity; do not reproduce the Departure column].
**Lower tribunal:** [Court or agency].
**Judgment or order under review:** [Date, precise disposition, and source].
**Requested appellate relief:** [What each party asks the circuit to do].
**Historical entry stage and date:** [Point where detailed play begins].
**Historical argument or submission:** [Mode, date, and source].
**Simulation argument or submission:** [Date and supported premise for any difference].
**Proposed event date:** [Date and basis; not a preselected result].
**Historical panel:** [Names, active/senior/visiting status, and source; withhold the result, author, and joins].
**Member Stone replaces:** [Name].
**Assignment method and reason:** [Disclosed method and basis fixed before modeling votes].
**Resulting panel:** [Names and roles].
**Participation checks:** [Qualification, recusal, designation, quorum, and timing; specific gaps if any].
**Further panel departure:** [Separate justification for another replacement, if necessary; otherwise None].

Apply the [selection policy](CASE_SELECTION.md). Calabresi never sits on this simulation court. Replacing another judge for one case does not remove that judge from the roster. A later decision date does not establish eligibility to participate in an earlier submission.

### Record and issues

**Material record:** [Actual dispute and decision-material facts, with sources. Distinguish findings, allegations, disputed evidence, stipulations, and concessions].
**Appellate jurisdiction:** [Statutory route, finality or exception, timeliness, relevant filing dates, and any dispute].
**Claims and issues raised:** [What was presented below and on appeal; identify relevant limits].
**Related proceedings or dependencies:** [Only date-eligible material; or None].
**Missing facts, documents, or findings:** [Exact gap and materiality; or None].
**Bounded reconstruction or scheduling premise:** [Explicit premise, basis, and limits; or None].

Preserve the historical parties, dispute, claims, material facts, and pre-entry procedure. An assumption cannot resolve a disputed material fact without support. Leave unsupported details unspecified rather than improving the vehicle.

### Law entering the event

**Legal cutoff:** [Exact simulation date and sources checked].
**Effective earlier simulation records:** [Relevant final-record links, including same-year decisions; or None].

Repeat this block for each genuinely distinct issue:

#### Issue [number]: [Question]

**Preservation and reach:** [How raised; relevant waiver, forfeiture, exhaustion, justiciability, or scope limit].
**Standard of review:** [Applicable standard and date-eligible authority].
**Governing test and burdens:** [Actual elements, conditions, exceptions, and burden allocation, with sources].
**Historical Supreme Court authority:** [Decision, operative proposition, date, and current force; or no directly controlling holding identified].
**Other governing authority:** [Circuit law, statutes, rules, state law where applicable, and their authority status].
**Applicable simulation holding:** [Proposition, final-record link, scope, and later treatment; or None].
**Open question or conflict:** [Precisely what remains unsettled or changed; or None].
**Appellant's strongest supported position:** [Argument, material evidence, and relief].
**Appellee's strongest supported position:** [Argument, material evidence, and relief].
**Additional material position:** [Amicus or other party only when relevant].
**Error and remedy constraints:** [Applicable harmless/plain-error analysis or other remedial limit; omit if irrelevant].
**Lawful paths:** [Supported threshold, merits, or remand alternatives; no vote predictions. List the alternatives symmetrically, with no sequencing, order of reach, or preferred route].

### Sources and neutral handoff

**Primary sources supplied:** [Links or extracted material and pinpoints. Include relevant date-eligible writings by the participating judges other than Stone, with usable extracts tied to the issues; identify material gaps below].
**Unavailable material and consequence:** [Specific limitation; or None].
**Date-eligibility check:** [Confirm that the operative facts, arguments, and authorities were available at this simulated stage].

Give primary-source links and pinpoints sufficient to verify the material propositions. When facts were extracted from the historical opinion under simulation, identify their provenance without handing that opinion's result to the modeler. Supply a sanitized extract rather than directing the modeler to read the full comparator. Separate lower-court rulings that are legitimately part of the record from the current appellate outcome that must remain withheld.

Exclude Stone's private proposal and biography, the selected appellate event's historical result and voting alignment, and later Supreme Court events. The archive exclusion above applies to every stage, not only this neutral handoff. Case identity may permit latent familiarity; do not claim the model has no prior knowledge. The enforced boundary is the material supplied or retrieved during the scoped stage.

## File: stone.md

### Status

**Case:** [Caption and docket].
**Version:** [One live version].
**Approval status:** [Proposed / user-approved].
**Approval reference:** [Actual instruction or delegation and date; or not yet approved].
**Legal cutoff and packet version:** [Neutral baseline addressed by this position].
**Conditions or delegated choices:** [Express scope; or None].

### Stone's position

Repeat for each separable issue or judgment component:

**Component:** [Issue or claim].
**Jurisdiction and reach:** [What Stone may decide and why].
**Vote and disposition:** [Exact result sought].
**Governing law:** [Binding rule, review standard, and material burdens].
**Legal relationship:** [Applying binding law / resolving an open question / following a binding rule while urging lawful reconsideration].
**Proposed holding:** [Precise proposition, application, and material qualifications].
**Supporting reasoning:** [Connect the governing rule, review standard, and material burdens to the decisive record facts. Explain why they support the proposed disposition and answer the strongest material contrary argument; identify any unresolved point rather than supplying an unsupported answer].
**Remedy and remand:** [Operative relief and instructions].
**Limits and reserved questions:** [Scope].
**Acceptable narrower join or fallback:** [Only if approved; otherwise not supplied].
**Separate writing:** [Approved substance and conditions, if any].

Distinguish what binding law requires, what is open to this court, and what Stone would urge another court to change. His personal view does not authorize ignoring precedent. Prepare proposals only from the user's case-specific instructions and the legal packet, and preserve the approval requirement. Record choices covered by a genuine existing delegation without seeking duplicate approval. Ask for user input only when neither the approved brief nor a genuine existing delegation covers a required choice; do not infer it from biography, the archive or engine-generated archival derivatives, or an old project permission.

## File: history.md

**Case:** [Caption and docket].
**Historical event and date:** [Selected appellate event only].
**Historical disposition:** [Result by component].
**Historical panel:** [Names].
**Opinion author and joins:** [Actual writing structure].
**Historical holding and grounds:** [Operative propositions and qualifications].
**Separate opinions:** [Authors, joins, and substantive differences; or None].
**Remedy and mandate:** [Verified scope and date/status; unknown if not established].
**Sources:** [Primary links and pinpoints supporting the above].
**Known differences in premises:** [Differences from the neutral facts, law, posture, or requested relief; do not predict new votes. Do not describe, characterize, or refer to `stone.md` or Stone's proposal].

This file is introduced only after neutral commitments are frozen, in a separate reconciliation context that never sees `stone.md`. It supplies evidence for comparison, not a command to copy history.

Put later historical rehearing and Supreme Court outcomes in a separate optional `historical-follow-up.md`. That file is for due-date follow-up research, not initial neutral modeling, reconciliation, or assembly. Historical outcomes cannot leak backward through an undifferentiated case-history block.

## Files created by Run

- `commitments.md`: non-Stone judges' concise independently modeled dispositions, grounds, sources, remedy positions, and join limits; neutral context identifier and allowed inputs.
- `reconciled.md`: frozen final positions after historical comparison; specific bases for departures or unresolved uncertainty; separate context identifier and allowed inputs.
- `events/YYYY-MM-DD-<event>.md`: final record using the [decision template](templates/DECISION_RECORD.md). A later rehearing or remand is a separate event, not an overwrite of a valid earlier decision.
- Optional `output/YYYY-MM-DD-<event>.md`: readable presentation after the record is locked, using the [render template](templates/RENDER.md) under the [render contract](RENDER_CONTRACT.md).

Record preparation or execution identifiers internally and accurately. Do not claim a context was isolated merely because the corresponding files exist. Do not create empty Run outputs to imply that a case has been adjudicated.

Maintain the live tracker using the [Standing State template](templates/STANDING_STATE.md). Holdings and applied tests stay in final decision records, with navigation and later treatment in the precedent index.

