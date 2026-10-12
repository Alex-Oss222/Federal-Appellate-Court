# Appellate render template

Render after every simulation turn without waiting for a separate Render request. Display the readable report directly in the response and save it; a completion notice or file link alone is not the turn output. This applies to turns that prepare or advance a case, adjudicate it, process follow-up, or advance the simulation calendar. Repository maintenance and standalone explanatory questions do not themselves require a simulated court report.

Choose the form:

- **Form A: Court report.** The default output after every simulation turn. Use the eight-section overview below, emphasizing the case and developments handled in that turn. Save at `years/YYYY/output/YYYY-MM-DD-court-report.md`.
- **Form B: Individual appellate decision.** A decision summary followed by the actual written opinion and any supported separate opinions. Save at `years/YYYY/cases/<case-slug>/output/YYYY-MM-DD-<event>.md`.
- **Form C: Procedural or subsequent-review event.** A compact report of a completed action at the same case output location.

Limit case entries to the user's selected cases and their connected review or remand proceedings, including earlier-year carryovers. Do not create entries for other Supreme Court or circuit cases merely because they are important or were decided that year. Other authorities may be cited only as context directly needed to explain a selected case or its applicable law.

Write for a reader who wants to understand the case, the outcome, and realistically relevant context. Use developed, accessible prose for substantive case explanations; explain necessary legal terms, connect the governing rule to the decisive facts, and describe the supported practical effect and limits. Do not reduce the output to labels, a status table, or bookkeeping. Keep unchanged institutional sections brief. Present new decisions and their supported written opinions in detail, without reprinting every earlier case.

A preparation turn explains the dispute, each side's position, and what remains to be decided. A decision turn explains the completed outcome and reasoning and includes the actual supported opinion text. A follow-up turn explains the verified action and its effect. When no decision was issued, say so; do not fill the opinion section with a prediction.

These are presentations, not new sources of authority or additional editable state registers. Replace bracketed fields, remove drafting instructions, and omit inapplicable repeated blocks. For a court report, retain the eight main sections and say when no supported entry exists. Do not add a section 9, period-close report, ideological court climate, voting forecast, or strategic-career narrative.

Follow the [render contract](../RENDER_CONTRACT.md). A preparer supplies dated, scoped source extracts for Form A; Forms B and C use the final event record's Public decision material. The renderer does not independently research, decide a case, invent a procedural event, or read private proposals and historical-comparator files.

## Form A: Court report

# Second Circuit court report

**Simulation date:** [Exact date].
**Calendar year:** [1994–2020].
**Session:** [Session label or covered date range].
**Last completed event:** [Case or institutional event, date, and record reference].
**Current activity:** [Preparing a case / awaiting Stone's position / adjudication / follow-up / advancing the calendar].

## 1. Current position

[Lead with what happened in this turn and the resulting position of the case or court. Identify the most recent completed work, the matters presently before the court, and what remains open. Make clear whether a decision was issued, preparation was completed, a subsequent event occurred, or time advanced. Do not imply that a preparation step changed the judicial result or simulation date.]

**Next supported event:** [Event and date, or not yet established].
**Outstanding preparation:** [Specific work needed].
**Open uncertainty:** [What is unknown and whether it affects the next event].

Do not predict a result, promise a doctrinal development, or assign Stone a narrative role.

## 2. Court composition and administration

**Chief judge:** [Name, source, and effective date].
**Roster reference:** [Dated roster reference].
**Verified vacancies:** [Seats and effective dates, or none].
**Changes since the previous report:** [Verified appointments, departures, senior status, or other material developments].

| Judge relevant to current work | Status on event date | Participation or administrative role | Source or limitation |
|---|---|---|---|
| [Name] | [Active / senior / visiting] | [Assigned panel member, chief judge, etc.] | [Source; any unresolved qualification or designation issue] |

Include relevant participation restrictions and supported recusals without inventing reasons. Calabresi never joins this simulation court. Appointment to his historical seat does not establish Stone's assignment to every appeal.

Do not include ideological ratings, allies or opponents, predicted votes, favorable-panel probabilities, or speculative retirements and nominations.

## 3. Cases for this session

List the cases being handled in the current session in chronological order. Use the existing case identities and link each caption to its case record.

| No. | Caption | Docket(s) | Event date | Event type | Status | Area of law |
|---|---|---|---|---|---|---|
| [1] | [Case caption and record link] | [Verified docket number(s)] | [Date and whether actual, scheduled, or proposed] | [Argument / submission on briefs / panel decision / rehearing / remand return / other specified event] | [In preparation / scheduled / submitted, awaiting decision / decided / on hold] | [Specific subject or subjects] |

Use one row per case event included in this session. The event type states what is being handled; the status states its present stage as of the report date. Give only supported dates, and use "not yet established" when necessary. A proposed simulation date must be identified as a proposal, not a verified court setting.

Do not include a Chunk column, generic MERITS category, category totals, or quota tables. Area of law describes the case; it does not reassign the case's primary selection group. Coverage groups and cycle counts remain in the canonical case list and Standing State. A follow-up row does not count as another selected case.

Keep the detailed dispute and procedural explanation in section 4 and completed opinions in section 5. Do not reveal a future historical result in the status field. If no cases have been selected for this session, say so without creating example proceedings.

## 4. Current case or proceeding

Repeat for each matter requiring present attention. A candidate awaiting verification must be identified as such, not presented as an assigned or pending proceeding.

**Case:** [Historical caption].
**Docket or citation:** [Verified identifier].
**Case-list and brief references:** [References].
**Current procedural stage:** [Exact stage and date].

### What the case concerns

[Explain the actual dispute as connected prose: who the parties are, what happened, how the dispute reached this stage, and what each side seeks. Include the material factual and procedural background needed to understand the case. Distinguish allegations, findings, agreed facts, and disputed evidence.]

### The parties' positions and relevant context

[Explain each side's principal supported argument and the governing legal question in accessible language. Include sourced context when it helps explain the dispute, such as the statute, agency action, trial ruling, or existing doctrine at issue. Explain what turns on the question for these parties. This is an account of the available record and arguments, not a forecast of the judges' votes or the result. Leave unsupported details unspecified.]

### Why it is before this court

**Decision or action under review:** [What the lower tribunal did].
**Basis for this proceeding:** [Verified appeal, petition, remand return, or other event, with source].
**Question presently before the court:** [Issue at this stage].
**Jurisdictional or procedural dispute:** [Any live dispute, or none identified].

A jurisdictional dispute can itself be an issue for adjudication. Missing research is not a judicial finding.

### Panel and assignment

**Historical panel:** [Names, status, and source].
**Member Stone replaces:** [Name].
**Assignment basis:** [Recorded method and timing].
**Resulting panel:** [Names].
**Participation issues:** [Specific unresolved matters, or none].

### What must happen next

[Supported procedural or preparation step. Identify any source gap beside the affected matter. Do not forecast votes or disclose the historical result of the selected event before adjudication.]

## 5. Completed appellate decisions and written opinions

Give the decisions completed in this turn substantive treatment, including the supported written opinions below. For multiple completed decisions, use a separate case block for each. Briefly cross-reference earlier decisions when necessary to understand current work; do not reprint the entire accumulated docket on every turn. If no decision was completed in this turn, state that clearly and use a short reference for any earlier decision that remains relevant.

**Case:** [Caption and docket or citation].
**Decision date:** [Date].
**Argued or submitted:** [Date and mode, when relevant].
**Panel:** [Participating judges and relevant roles].
**Disposition status:** [Precedential / nonprecedential / other supported status].
**Opinion author and joins:** [Author and exact joins for each writing].
**Final decision record:** [Reference; distinguish any historical source citation from the simulated opinion].

### Decision summary

**What the dispute concerned:** [Underlying dispute and route to this court].
**What the court decided:** [Exact result for each issue or claim and relief ordered].
**Why the court decided that way:** [Governing law, material facts, and controlling application; identify any threshold ground preventing a merits decision].
**Where the judges disagreed:** [Actual disagreements over judgment, reasoning, or remedy; say when there was no separate opinion].
**Practical effect and limits:** [What the judgment and remedy actually change for the parties; any established effect on governing circuit law; and what remains undecided. Distinguish a supported legal consequence from an uncertain downstream possibility.]
**What happens next:** [Mandate status, remand instructions, or another supported procedural step].

Develop these explanations in paragraphs proportionate to the case. Connect the rule to the decisive facts and explain why it yields this outcome; a bare disposition or citation is insufficient. Give realistically relevant detail supported by the final public record, without inventing reactions, political effects, litigation, or future consequences.

Name the judges supporting each materially different component. Use a component or opinion-join table only when mixed dispositions or partial joins are clearer that way.

### Opinion of the court

**Author:** [Judge].
**Joined by:** [Judges and precise limits on their joins].

[Write the opinion itself in judicial prose, not merely an outline or summary. Include relevant background, issues, jurisdiction where material, the standard of review, governing authorities, operative tests and burdens, application to the record, and the precise disposition. Explain the principal contrary argument and the reason it does not control. Preserve qualifications, treatment of prior authority, questions left open, publication status, remedy, and mandate limits.]

All substance must be supplied by the final record's Public decision material. Prose may explain supplied reasoning but cannot add findings, authorities, arguments, holdings, joins, or remedial instructions. If the record lacks enough material for a requested passage, report that gap rather than authoring a new judicial position.

If no rationale has majority support, label the actual plurality or separate writings and state their support accurately. Do not manufacture an opinion of the court.

### Concurring opinion, if any

**Author:** [Judge].
**Joined by:** [Judges and scope, if any].

[Write the concurrence in judicial prose. Explain what the author joins, what they decline to join, and the supported alternative or additional reasoning.]

### Dissenting opinion, if any

**Author:** [Judge].
**Joined by:** [Judges and scope, if any].

[Write the dissent in judicial prose. Identify the disagreement, its legal and factual basis, and the disposition or remedy the author would order.]

Use accurate labels for writings concurring and dissenting in part. Stone may author the court's opinion, a concurrence, or a dissent only as established by the finalized adjudication. Do not create a separate opinion merely to fill the template. Do not present a dissent as controlling circuit law.

### Public source notes, if supplied

[References intended for publication in the final record. Do not present the generated simulation opinion as the verbatim historical reporter text.]

## 6. Current legal developments

Include only effective legal developments directly affecting a selected case, its operative holding, or its pending review. Identify the affected selected case first, then explain the relevant rule and consequence. Cite other decisions as necessary authority without giving them independent case entries or a general Supreme Court roundup. Full holdings and tests remain in their source decisions.

**Affected selected case:** [Case and record reference].
**Authority and effective date:** [Source].
**Operative proposition:** [Rule and material qualifications].
**Affected earlier authority:** [What changed, if anything].
**Known relevance to pending work:** [Specific issue or dependency].
**Precedent-index reference:** [Reference where applicable].

Explain actual legal developments without predicting judicial votes. Do not introduce future decisions or assume that a new precedent automatically disposes of another case or reopens a final judgment.

## 7. Follow-up proceedings and historical compatibility

Report the current year and previous two origin-year groups, together with all older unresolved cases. Derive this view from Standing State; do not create a new ledger or omit an older case because it is outside the current session docket. An origin year is the year of the first selected circuit decision, not a predicted review date.

| Origin year | Matter and docket references | Latest supported event | Present status | Next supported step or date | Dependency or uncertainty |
|---|---|---|---|---|---|
| [Year] | [Original case; circuit and Supreme Court dockets where established] | [Event, date, source] | [Precise status] | [Verified step, or unknown] | [Specific issue] |

**Follow-up checked through:** [Cutoff and any limits from the actual check].
**Older carryovers:** [Unresolved references, or None].

For a historical follow-up affected by a simulated decision, include the scoped compatibility conclusion prepared under the engine:

**Historical event assessed:** [Event and source; only when chronologically appropriate].
**Relevant simulation change:** [Final-record reference].
**What the change affects:** [Governing law / judgment / relief / party seeking review / questions presented / procedural posture / timing].
**Compatibility conclusion:** [Compatible / compatible in specified respects / unresolved / incompatible].
**Reason:** [The connection between this change and this event].
**Supported next step or open question:** [Action or specific research gap].

An incompatible historical event does not establish what happened instead. Retain `unresolved: historical path incompatible` where required by the engine. Do not invent a petition, grant, denial, finality, reversal, or remand. Unknown filing status is a research question, not proof of a pending proceeding.

This section is administrative reporting, not a court order or an input to neutral vote modeling. Do not reproduce private deliberations or future comparator material.

## 8. Supreme Court review of selected cases

**Information current through:** [Simulation date].

Show only Supreme Court proceedings linked to a case in the user's selected docket, including selected cases from earlier years. Require a reference to that selected circuit case for every entry below, even if its Supreme Court caption or docket differs. Use verified historical events released by the engine's follow-up check; do not add unrelated petitions, arguments, or decisions to fill this section. Other Supreme Court law may inform a selected case under section 6 without becoming a review entry here. The three-year view does not move historical dates or remove older pending work.

### Review updates for our circuit cases

**Origin-year case:** [Original circuit case, decision year, and final-record reference].
**Review identifiers:** [Linked Supreme Court caption and docket, if verified].
**Event this turn:** [Petition filed / review granted / review denied / argument / merits decision / vacatur / mandate / remand / other verified event, with date and source].
**Our circuit decision:** [What the finalized simulated judgment ordered, with record reference].
**What changed:** [What this Supreme Court event does to that judgment, its reasoning, the parties' relief, and any remand obligations; distinguish what remains effective from what is displaced or unresolved].
**Published reason, if any:** [Supported explanation; if the source supplies none, say no explanation is supplied rather than inventing one].
**Remaining work:** [Pending review, mandate, remand, supported closure, or a specific uncertainty].
**Compatibility:** [Admitted compatible event or reference to the unresolved issue in section 7].

Give a short update here for filings, grants, denials, and other review developments. Use the detailed blocks below for arguments and merits decisions without duplicating the same explanation. A denial is reported when it occurs; it is not held until the third year and does not promise a later merits decision. Do not place unverified petitions in the awaiting-argument block.

When there are no new verified review events for selected cases, say so briefly and point to any pending or unresolved selected matter in section 7. If none has established Supreme Court proceedings, say that directly. Do not substitute other cases or repeat a past event as though it happened again this turn.

### Selected cases awaiting oral argument

**Selected circuit case:** [Original case, year, and final-record reference].
**Supreme Court case:** [Linked historical caption and docket].
**Review status:** [Verified grant of review and date].
**Argument date:** [Scheduled date only if the scheduling information is available by the report date; otherwise not yet established].
**Question presented:** [Question accepted for review].
**Simulation judgment under review:** [The selected circuit judgment, relief, and reasoning supported by its final record and admitted review path].
**Principal arguments:** [Neutral account of positions available by the report date].
**Relevance to the Second Circuit:** [Potentially affected issue or rule, without predicting the result].
**Source:** [Supporting record].

Identify a petition awaiting a grant as a pending petition in section 7 when relevant, not as a case scheduled to be heard. If this is the historical version of a selected simulated appeal, apply section 7 before attaching the grant, hearing, or other event to the live appeal. Keep an incompatible comparator outside the report.

### Selected cases argued and awaiting decision

**Selected circuit case:** [Original case, year, and final-record reference].
**Supreme Court case:** [Linked caption and docket].
**Argument date:** [Verified date].
**Question before the Court:** [Issue].
**Status:** Awaiting decision.
**Relevant argument developments:** [Supported clarification of questions or positions, if useful].
**Affected circuit matters:** [Specific matters or legal questions, if any].
**Source:** [Supporting record].

Do not turn oral-argument questions into predicted votes. Do not disclose the eventual historical result before its decision date.

### Supreme Court decisions on selected cases

**Selected circuit case:** [Original case, year, and final-record reference].
**Supreme Court case and citation:** [Verified linked identity].
**Decision date:** [Date].
**Disposition:** [Exact result].
**Opinion author and joins:** [Actual writing structure].

**Holding:** [What the Court established and its material limits].
**Summary of the Court's reasoning:** [The legal rule, application, and explanation supporting the judgment].
**Concurrences and dissents:** [Actual reasoning and disagreements, if present].
**Effect on circuit law:** [Rule confirmed, displaced, narrowed, or left unresolved].
**Effect on our circuit judgment:** [What is affirmed, reversed, vacated, left effective, or otherwise affected, with the admitted case-specific order and its limits].
**Effect on relief and next proceedings:** [What changes for the parties and any remaining mandate or remand work, with sources].
**Effect on other selected cases, if any:** [Supported consequence for identified selected cases only; distinguish governing law from a case-specific order].
**Historical-path compatibility:** [Section 7 assessment if relevant before attaching a disposition or remand to a selected appeal].
**Sources:** [Opinion and relevant orders].

Report actual Supreme Court holdings and published explanations. Do not generate a replacement Supreme Court opinion, vote, certiorari decision, or procedural history.

## Form B: Individual appellate decision

# [Case caption]

**Court:** United States Court of Appeals for the Second Circuit.
**Docket:** [Verified docket or consolidated dockets].
**Argued or submitted:** [Date and actual mode].
**Decided:** [Date].
**Panel:** [Names and relevant roles].
**Disposition status:** [Supported status].
**Final record:** [Reference].

Use the content blocks from Form A, section 5: Decision summary; Opinion of the court or accurately labeled other writings; supported Concurring and Dissenting opinions; Public source notes if supplied. Include the full supported written opinions, not only summaries. For a short nonprecedential disposition, use its proper form and proportionate length without inventing a full published opinion.

This individual decision receives only the final record's Public decision material, this template, and the render contract. Do not append the report's administrative sections, historical compatibility assessment, or future Supreme Court outcome.

## Form C: Procedural or subsequent-review event

# [Case caption: event]

**Court:** [Court taking the action].
**Docket:** [Verified docket].
**Date:** [Effective event date].
**Stage:** [Panel rehearing, en banc consideration, mandate, certiorari, Supreme Court disposition, or remand].

**Action:** [What the verified historical event or authorized simulated circuit order actually does].
**Ground or published explanation:** [Only what the final record supplies; omit if none is public].
**Participation or separate statement:** [Only disclosed names, votes, or writings; omit if unknown].
**Effect on this case:** [Operative change to judgment, relief, mandate, or next stage].
**Next step:** [Established step and date if known; do not invent a filing or deadline].

Include a written simulated circuit order or separate statement when the finalized public material supports it. A short procedural order does not require a merits opinion.

A Supreme Court entry reports an actual historical action admitted as compatible with this case. An incompatible historical path is a follow-up problem, not a fictional Supreme Court order. A denial of certiorari does not become an endorsement of the reasoning below.

## Render check

Operator guidance, not output:

- Confirm that the simulation turn ends with the report displayed to the user, not only a saved-file link or completion notice.
- Confirm that the current case, any completed outcome, the reasons, and supported practical effects receive readable explanation; keep unchanged sections brief.
- Match the report date, session cases, event dates, statuses, and administrative facts to the scoped source packet.
- Confirm every Supreme Court review entry links to a selected circuit case and accounts for the actual simulated judgment. Do not include independent entries for unselected cases.
- Confirm the engine's follow-up check occurred, with limitations disclosed, and include newly due review events for earlier-year cases. Preserve older unresolved carryovers and avoid reporting an old event as new.
- Match every disposition, name, join, holding, qualification, opinion passage, and remedial instruction to the finalized public record.
- Keep future outcomes, ideological forecasts, private proposals, frozen commitments, and comparator files out of render inputs.
- Remove placeholders, unused forms, drafting instructions, internal approval and context identifiers, and unsupported predictions.
- Keep a court report separate from the input for an undecided case. Its final opinions and administrative compatibility notes do not become a combined neutral packet.
- Raise a material source gap beside the affected report entry or to the operator for an individual decision. Do not invent a judicial finding to fill it.
