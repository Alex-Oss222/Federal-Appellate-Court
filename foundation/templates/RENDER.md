# Appellate render template

Follow the [render contract](../RENDER_CONTRACT.md). Rendering presents established material; it cannot adjudicate, approve a proposal, create proceedings, or advance time.

- **Form A: Court report.** Display automatically after each simulation turn and save at `years/YYYY/output/YYYY-MM-DD-court-report.md`. A file link or completion notice alone is insufficient. Further turns on the same date update that report, with earlier versions retained in Git.
- **Form B: Individual appellate decision.** Use when specifically requested; save at `years/YYYY/cases/<case-slug>/output/YYYY-MM-DD-<event>.md`.
- **Form C: Procedural or subsequent-review event.** Use for an individual completed action at the same case output location.

Forms B and C do not replace the automatic court report unless the user expressly requests a different output.

## Instructions for preparing the report

Produce this report after each simulation turn that prepares, decides, or advances a selected case. A turn may cover one event, several cases, or part of a year. Do not advance time merely to fill the template. Ordinary questions and project editing do not trigger a report.

For Form A, use only the preparer's scoped, sourced, date-eligible packet authorized by the render contract. It contains the basic character extract, administrative state, selected-case facts and assignments, finalized Public decision material, and permitted comparison and follow-up extracts. Do not browse linked raw files or independently research during rendering. Forms B and C receive only the final record's Public decision material, this template, and the contract. Report what has happened as of the simulation date; do not make new decisions.

- Include only user-selected historical cases and proceedings arising from them. An unselected case may appear as necessary legal authority or background for a selected case, never as a separate docket entry. Do not invent cases.
- Keep neutral analysis, Stone's proposal, and historical comparison separate in the underlying work. The renderer does not receive private proposals, frozen commitments, or raw comparator files. An approved proposal is not an adopted holding. Never feed the combined report, character snapshot, or comparison extract into neutral modeling.
- Preserve the distinction between a simulated appellate decision and verified historical events. Label simulated opinions as simulation text. Never present them as authentic historical quotations.
- Use only information and law available by the applicable event date. Preserve established simulated circuit holdings and their later treatment. Do not import holdings from a separate Supreme Court simulation.
- Follow the established simulation roster and case-specific assignment. Calabresi never joins this court. Taking an institutional seat does not automatically place Stone on every historical panel.
- Do not add ideological classifications, allies or opponents, relationship scores, influence ratings, speculative coalitions, predictions of review, invented conversations, or national political scenery.
- Use ordinary explanatory prose for the case, reasoning, and consequences. Use tables for the docket, roster changes, and actual procedural updates. Do not turn every paragraph into a rating or checklist.
- Display the report directly in chat. Retain all eight main Form A sections; keep unchanged or empty sections to one line and omit their optional detail. Remove instructions and placeholders. Give each event one substantive account and refer back to it elsewhere. Do not add a section 9 or period-close presentation.

Before presenting the report, check dates, panel eligibility, votes and joins, holdings, remedies, and procedural status. Explain only material gaps that prevent a reliable account. Use “Not established” for an unknown fact and “None” only for a confirmed absence. Do not print the internal checklist or manufacture a result to make the report look complete.

---

## Form A: Court report

# Second Circuit court report

## 1. Current position

Simulation date: [Date through which events have actually occurred]  
This turn: [Events or period covered; completed work and any unresolved matter]

Character snapshot: [Name] | [Age, if established] | [Current judicial position] | [Time served on this court]

Keep the snapshot to this line. Do not repeat the biography, jurisprudence, temperament, relationships, personal life, or a narrative of professional growth. Update these basics only from established information. Mention seniority or an administrative role elsewhere only when it affects the current work.

## 2. Court composition and administration

Chief judge: [Name]  
Court status: [Verified active membership and vacancies, if available]

[Briefly identify appointments, departures, senior-status changes, or administrative changes effective during this turn. On the opening turn, include a compact established roster; thereafter report changes only. Do not assume every senior judge is available to sit.]

| Judge | Change | Effective date | Relevant consequence |
|---|---|---|---|
| [Name] | [Established change] | [Date] | [Effect on eligibility, administration, or a selected case] |

[If unchanged: “No relevant change in court composition or administration.”]

Do not add judicial profiles, appointing-party summaries, ideological balance estimates, or predictions about future panel votes.

## 3. Cases for this session

List the selected cases or follow-up events being handled in this session in chronological order, linking each caption to its existing case record. Include earlier selected cases only when carried forward for current work. A follow-up does not count as another selected case.

| No. | Caption | Docket(s) | Event date | Event type | Status | Area of law |
|---|---|---|---|---|---|---|
| [No.] | [Caption] | [Verified number(s)] | [Date and historical/simulated/scheduled status where needed] | [Submission, decision, rehearing, review, remand, etc.] | [Actual current stage] | [Plain-language subject] |

An unknown date remains unknown. A scheduled event is not a completed event. Record historical and simulated dates separately when they differ.

Do not include chunks, generic MERITS categories, category quotas, or statistics for the court's unplayed docket. Any totals refer only to selected cases and distinguish cases from procedural events. Area of law describes the case, not a reassignment of its primary coverage group; selection counts remain in the canonical case list and Standing State.

## 4. Current case or proceeding

Use this section for a selected matter that remains pending or was only prepared this turn. Repeat only for pending matters needing a substantive update. A case decided this turn receives its full account in Section 5 instead.

### [Case name]

- What the dispute is: [Material facts, parties, and relief sought, distinguishing allegations from established findings.]
- How it reached this court: [Relevant lower-court or agency action, reasoning below, and present procedural posture.]
- What the court must decide: [Material questions, including threshold issues where relevant.]
- Each side's position: [The strongest material arguments, stated fairly.]
- Current status: [Work completed, established next step, and any missing information that actually matters.]

Identify the historical panel and proposed or established simulation panel when relevant to this stage. State any unresolved assignment issue. Do not forecast votes, reveal the historical disposition, or treat Stone's proposal as the pending court's result.

[If no matter needs this account: one brief status line.]

## 5. Completed appellate decisions and written opinions

Give one complete account for each selected appellate decision finalized this turn, including an en banc merits decision. Do not repeat earlier opinions unless they have materially changed.

### [Case name]

Decision date: [Simulation date; identify a different historical date if relevant]  
Docket(s): [Verified number(s)]  
Decision type: [Panel/en banc; established precedential or nonprecedential status]  
Final decision record: [Reference]

Historical panel: [Names]  
Simulation panel: [Names]  
Stone replaces: [Historical member]  
Assignment basis: [Established method and reason this assignment is eligible for this case and date]

For en banc decisions, give the participating court and relevant exclusions instead of forcing a three-judge replacement format. Historical-panel replacement details are prepared administrative context, outside the opinion and Form B.

#### The case and the result

[Explain the dispute, material facts, procedural route, reasoning below, and the question presented. Summarize the material arguments from each side. Use enough detail for the reader to understand why the result matters without reproducing the entire brief.]

[State what the court actually decided, which parts of the judgment changed, and the immediate effect on the parties.]

Judgment: [Exact disposition and affected claims or orders]  
Vote: [Actual recorded division on the judgment]  
Opinion and joins: [Author; who joins the reasoning, joins only the judgment, or writes separately]

When judges differ by issue, explain those differences. Use a component table only if it makes a genuinely divided result clearer. Do not assume that agreement on the judgment means agreement on every rationale.

#### Opinion of the court

*Simulated judicial opinion based on the finalized decision.*

[Provide the actual written opinion in judicial prose, not an abstract or an outline. Explain the relevant record, threshold rulings, governing authority, standard of review, burdens and tests where material, application, substantial contrary arguments, and disposition.]

[All substantive content must come from the final record's Public decision material. Preserve the reasoning actually adopted and its limits. Do not add facts, findings, authorities, quotations, arguments, holdings, joins, or relief. Return a material source gap for correction rather than supplying new reasoning. Identify matters expressly left open.]

If no majority supports a single opinion, use the correct description for the actual writings and identify any supported common ground without inventing a unified rationale.

#### Separate opinions

[Include each established concurrence or dissent as a written opinion with its author and exact joins. State what it agrees or disagrees with, its reasoning, and the alternative judgment or approach where applicable.]

Omit this subsection if there is no separate writing. Do not invent one for variety or make Stone the author by default.

#### What the decision does

- Controlling holding: [Concise operative rule, necessary conditions, important exceptions, and limits. Distinguish binding reasoning from dicta or separate views. Note when the case simply applies settled law.]
- Effect on the parties: [Relief granted or denied and what remains unresolved.]
- Mandate and remand: [Current established status, instructions, and any verified next step. Do not infer that a mandate has issued.]

#### Historical comparison

[After the simulated decision is settled, briefly state the historical appellate disposition and material similarities or differences, with its source. Distinguish a changed judgment from changed reasoning producing the same judgment. Identify any concrete consequence for later procedural compatibility.]

Use only the preparer's short comparison extract authorized by the render contract, after finalization and only once the historical disposition itself has occurred by the report date. Omit it if not date-eligible. Keep it outside the judicial opinion and Forms B and C. Do not open raw comparator files or reveal later historical proceedings. The historical ruling is not a second live judgment.

#### Public source notes, if supplied

[References intended for publication in the final record. Keep comparison sources with the separate comparison.]

## 6. Legal developments affecting selected cases

Include only a development that changes the law, posture, or available relief for a selected case.

[Name the affected selected case, identify the authority or finalized simulated holding and its effective date, and explain the specific effect. State whether an earlier rule remains operative, is limited, or has been superseded.]

A historical Supreme Court decision may be relevant authority even when that Supreme Court case is not a selected case. Explain only its effect on the selected matter. Do not add a general Supreme Court roundup or repeat Section 5's holdings.

[If none: “No additional legal development affecting the selected cases.”]

## 7. Follow-up proceedings and historical compatibility

Cover actual non-Supreme Court developments in selected cases, including prior-year cases. Do not invent a petition or deadline because one would be procedurally possible.

| Selected case | Date | Event and source | Effect on judgment or relief | Current status or established next step |
|---|---|---|---|---|
| [Case and original decision year] | [Date] | [Verified historical event admitted to this timeline, or finalized simulated action] | [Specific effect] | [Known next step, pending question, or closure] |

[Add a short explanation when the table cannot convey the reasoning or practical effect. A substantive en banc opinion belongs in Section 5; refer to it here.]

When a simulated departure changes the posture of later historical proceedings, identify the affected proceeding and the specific incompatibility. Do not silently reuse its historical result.

### Open matters and compatibility

Derive this compact view from Standing State, covering the current year, previous two origin years, and every older unresolved selected case. Do not create another ledger. Supreme Court events receive their substantive explanation in section 8.

| Origin year | Selected case and docket links | Last established event | Present status | Known next step or specific blocker |
|---|---|---|---|---|
| [Year of first selected circuit decision] | [Original case; connected review identifiers] | [Date and source] | [Actual stage] | [Verified step or unresolved question] |

Follow-up checked through: [Actual cutoff and any coverage limitation]

For a new or changed compatibility issue, identify the historical event, the relevant simulation change, the affected judgment, relief, party, question, posture, or date, and the specific reason the event does or does not fit. Use the preparer's scoped assessment. Preserve `unresolved: historical path incompatible` where required. An incompatible historical event does not establish what happened instead. Unchanged matters need only a status reference.

Unknown filing status is a research gap, not proof of a pending petition. Do not close matters merely because they are old or the year ends. These administrative notes are not court orders or neutral modeling inputs.

[If there are no events or open matters: one brief line.]

## 8. Supreme Court review of selected cases

Report only review connected to selected circuit cases. Carry the original case and decision year through any changed caption or Supreme Court docket.

Track current-year and previous-two-year selected decisions, plus every older unresolved matter. This is a tracking window, not a mandatory three-year schedule. Events appear on their actual applicable dates. Do not force a grant in the next year or a decision in the year after that.

### Updates this turn

| Original selected case and year | Supreme Court caption/docket | Date | Actual review event | Effect on the simulated appellate judgment |
|---|---|---|---|---|
| [Original case/year] | [Verified caption and number, or Not established] | [Date] | [Petition filed, grant, denial, argument, disposition, mandate, etc.] | [Compatible effect or specific unresolved incompatibility] |

Include only historically verified Supreme Court events compatible with this timeline. Do not invent Supreme Court votes, opinions, citations to Stone, grants, denials, or alternative outcomes. A changed appellate judgment requires a compatibility check; the historical review path does not automatically carry over.

For a Supreme Court decision actually applicable to a selected case, explain:

- The question reviewed and the Court's disposition.
- Its holding and principal reasoning, with material separate views where useful.
- Which parts of the simulated appellate judgment or reasoning survive, change, or fall.
- The resulting relief and any established mandate or remand work.

Report a denial without treating it as approval of the appellate reasoning. If the Court provides no explanation for an order, do not supply one.

If the historical path is incompatible, say so plainly and identify what remains unresolved. The historical Supreme Court opinion may still become governing law on its actual date; that does not make it a disposition of this altered case.

### Selected cases awaiting argument or decision

[For newly granted or materially changed review, identify the original selected case, Supreme Court caption and docket, accepted question, simulation judgment under review, neutral account of available principal arguments, and current stage. Distinguish a pending petition from granted review, and a granted case awaiting argument from an argued case awaiting decision.]

Give an argument date only when its scheduling was established by the report date. Describe material argument developments only from supported public sources; questions from the bench do not establish votes. Do not reveal the eventual outcome early.

Use short references to section 7 for unchanged pending petitions and mandate/remand work, including older carryovers. Do not repeat full case briefs.

[If there are no updates, say so briefly and list only genuinely open matters. Do not fill this section with unrelated cases, forecasts, or future outcomes.]

---

## Form B: Individual appellate decision

# [Case caption]

Court: United States Court of Appeals for the Second Circuit  
Docket(s): [Verified identifiers]  
Argued or submitted: [Established date and mode, when relevant]  
Decided: [Date]  
Panel or en banc court: [Participants]  
Disposition status: [Supported status]  
Final record: [Reference]

Use section 5's case-and-result account, written opinion, established separate opinions, controlling holding, relief, mandate status, and public source notes. Identify authors and exact joins, including agreement only with the judgment. Use a proportionate form for a short nonprecedential disposition without inventing a full published opinion.

Read only the finalized Public decision material, this template, and the contract. Do not append the character snapshot, historical panel-replacement context, historical comparison, other administrative sections, or future Supreme Court developments.

## Form C: Procedural or subsequent-review event

# [Case caption: event]

Court: [Court taking action]  
Docket: [Verified identifier]  
Effective date: [Date]  
Stage: [Rehearing, mandate, review, disposition, remand, etc.]

Action: [What the finalized action does]  
Published ground: [Supplied explanation; omit if none disclosed]  
Participation or separate statement: [Established names, votes, and writings only]  
Effect on this case: [Change to judgment, relief, mandate, or stage]  
Next step: [Established action or deadline, not an assumed filing]

Include a written simulated circuit order or separate statement only when supported by the finalized Public decision material. A procedural order does not require a merits opinion. A Supreme Court entry reports a verified historical action admitted as compatible with this case, never a substitute simulated order.
