# Second Circuit appellate engine

## 1. Project boundary

Stone is commissioned and takes the required judicial oaths on December 1, 1993 in the Meskill vacancy, instead of Calabresi. These are fictional appointment dates established by the character sheet. Detailed play opens January 1, 1994, making 1994 his first full calendar year on the court. He is a new circuit judge, not chief judge, and inherits neither Meskill's seniority nor his former chief position. Selected appeals may differ because Stone sits on their panels. The Supreme Court remains historical; this project imports none of the separate Supreme Court simulation's law or institutional changes.

Use real historical appeals as the starting cases. A selected case's actual caption, docket, lower-court record, and procedural posture must be verified. Declared panel substitutions and resulting appellate rulings are simulation events. Never represent invented facts, filings, quotations, or dockets as historical research.

The character's prior district-court service and signature opinion remain supplied biography. No fictional earlier holding is automatically entered into circuit precedent. Admission of a specific prior fictional decision requires a user-established legal baseline identifying its holding and status.

`stone/JURISPRUDENCE.md` is archival storage only. The engine and its agents must never open, read, search, index, summarize, embed, import, validate, or otherwise process its contents. This boundary applies to preparation, research, generation, neutral modeling, reconciliation, assembly, validation, follow-up, rendering, and engine maintenance. Engine-generated summaries, embeddings, digests, cached extracts, and other archival derivatives are equally excluded, even if created earlier. Use explicit allowed-file lists for all source access; the archive and engine-generated archival derivatives are never eligible inputs. Its presence in the repository grants no permission to use it. The user's expressly supplied case-specific brief is an authorized input; hypothetical provenance does not disqualify it. Do not compare that brief with the archive or reconstruct the archive to enforce this exclusion.

## 2. Legal and documentary authority

At each event, identify the date, the record, the issue properly before the court, the controlling legal sources, and the authority of the participating court.

- Actual Supreme Court decisions enter on their actual dates and bind according to their legal scope, subsequent treatment, and applicable temporal rules. Later authority cannot influence an earlier decision.
- Historical Second Circuit decisions remain available unless displaced by an effective simulation decision or otherwise incompatible with a documented change. Other circuits, district courts, and state courts receive the authority governing law gives them. State-law questions require the applicable state's law.
- A selected appeal's historical opinion is its comparator, not a second live disposition alongside the simulation's replacement decision. If an earlier stage of the same case remains effective, identify it separately.
- Historical decisions outside selected appeals can remain background law when compatible with this timeline. If one depends materially on a replaced ruling or on an impossible panel, assess and record the compatibility problem before relying on it. Do not automatically erase all later cases, but do not invent replacement reasoning, authorship, or votes to repair one.
- Final simulation event records establish this circuit's changed holdings, judgments, and procedure. Their legal effect depends on court authority, publication status, actual joins, dates, and later treatment.
- The latest user-approved case brief `stone.md` is the sole source of Stone's case-specific disposition and reasoning. It is his position, not binding law or another judge's view. `stone/CHARACTER.md` supplies biography only; the jurisprudence archive supplies nothing to the engine.
- [Standing State](../state/STANDING_STATE.md) tracks present institutional and procedural status. [Precedent](../state/PRECEDENT.md) indexes controlling propositions. Neither overrides its source record.

No separate Holdings or Standards and Tests register is required. State the operative holding, applied test, review standard, burdens, and material qualifications in the final event record. The precedent index remains a concise pointer and subsequent-treatment aid; historical law is researched from its actual sources.

Distinguish a disagreement with precedent from authority to depart from it. A panel cannot exercise the Supreme Court's overruling power. Apply the Second Circuit's date-specific prior-panel, intervening-authority, en banc, mandate, and law-of-the-case rules. Check publication and citation rules as of the relevant date. A nonprecedential disposition may still bind the parties and matter for preclusion or the same litigation; lack of precedential force does not mean no legal effect.

## 3. Calendar and scope

Use calendar-year folders for convenience. The first period is January 1 through December 31, 1994, Stone's first full calendar year after his December 1, 1993 appointment and oaths. The December transition is background only; no unplayed 1993 appellate case, panel assignment, or simulation holding is automatically created. The period is not a Supreme Court October Term. Selected cases are a sample of Stone's work, not his entire annual judicial workload. Follow [the case-selection policy](CASE_SELECTION.md): six groups, three real historical Second Circuit cases per group, eighteen cases per cycle. A cycle is a coverage unit, not an annual deadline. Keep one canonical row per case under [the case-list template](templates/CASE_LIST.md), with one primary group and secondary tags for overlaps. Carry unfilled group slots across years without moving historical disputes backward, duplicating cases, or fabricating facts. Preserve the historical parties, dispute, claims, material facts, and procedure up to the simulation's entry point.

A later opinion can support research into an earlier proceeding, but only date-eligible facts, arguments, and authorities enter the neutral packet. Administrative case-list columns recording departures and subsequent history are not inputs to the neutral modeler. Cases and events remain chronological even when coverage cycles overlap; follow-up to an already counted case does not supply an additional quota entry.

Process adjudicative and material institutional events in date order, including intervening historical Supreme Court decisions. Record submission or argument separately from decision and mandate dates. Stone cannot participate in a pre-appointment submission simply because the historical opinion was released later; a lawful reargument, resubmission, or replacement procedure needs a supported basis and a clearly identified simulation premise.

A late-discovered earlier event requires an assessment of affected completed decisions. Do not quietly insert it and preserve incompatible later results. Correct only with the user's authorization, preserving unaffected work.

## 4. Court and panel assignment

Read the roster as of the relevant participation date. Verify actual qualification to sit, recusal, designation, active or senior status, and any change before decision. A commission date alone is not proof of an oath, a first sitting, or assignment to an already-submitted case. Stone's required oaths are expressly established on December 1, 1993 by the fictional character timeline; his participation in any particular case still requires the assignment and timing checks.

Every selected appeal identifies:

1. The verified historical panel and each member's status.
2. The one member Stone replaces and the reason for the substitution.
3. The resulting panel, with an eligibility and timing check for each member.
4. Any further departure from history and its independently justified basis.

If Calabresi appears on the historical panel, Stone normally occupies that place. Calabresi never joins this simulation court. If Calabresi was not on the panel, use a disclosed rotation or reproducible draw among eligible replacement positions, fixed before modeling votes. Preserve the other historical panelists when lawful. Record the method and result; do not redraw for a desired ideology, vote, author, or outcome. If no assignment method was supplied, preparation may propose one; identify it as a premise before Run.

Replacing a judge on one case does not remove that judge from the roster. A visiting judge or senior judge is not interchangeable with an active judge for all institutional purposes. Verify statutory composition, quorum, and designation requirements. Distinguish who can request or vote on rehearing from who can sit en banc. Use the rules effective then, not a permanently hard-coded roster or voting denominator.

Chief-judge succession is governed by law, not by the President's choice of a new appointee. The opening chief is Jon O. Newman. Legal starting references include [28 U.S.C. 45](https://www.law.cornell.edu/uscode/text/28/45) and [28 U.S.C. 46](https://www.law.cornell.edu/uscode/text/28/46); verify historical text and amendments when applying them to a dated event.

## 5. Required appellate intake

Use [the brief template](CASE_BRIEF_TEMPLATE.md). Identify appellate jurisdiction and timeliness; the decision under review; requested relief; record facts and lower-court findings; preserved issues, forfeiture or waiver; each issue's standard of review; burdens; controlling authority; and material remedial constraints. Consider mootness, standing, harmless or plain error, immunity, exhaustion, and other thresholds only when relevant.

De novo legal review does not authorize a new trial or new factfinding. Distinguish conclusions of law, factual findings, discretionary rulings, jury verdicts, and agency determinations. Identify any lawful basis for additional material. If a material finding is absent, address the proper consequence rather than inventing it. A legal violation does not by itself choose damages, reversal, suppression, release, or remand.

Research may use a historical opinion's recitation of facts, with attribution. Extract those facts into the neutral packet without giving the modeler the current appeal's historical disposition, lineup, or rationale. A preparer who has seen the result must hand off to a fresh neutral context. Distinguish missing historical material from a procedurally reconstructed simulation event. Label a bounded assumption and its effect; if it decides a disputed material fact without support, do not adjudicate on it.

## 6. Separated adjudication

The user controls Stone's case-specific position through `stone.md`. Prepare proposals from the user's case-specific instructions and the legal packet, never from the jurisprudence archive or engine-generated archival derivatives. Drafts remain drafts until approved or covered by a genuine existing delegation. Record choices made within that delegation in `stone.md` without seeking duplicate approval. Ask for the user's case-specific input only when neither the approved brief nor a genuine existing delegation covers a required choice; do not infer it from biography or an old project permission. There is no inherited Supreme Court standing fallback.

### Neutral modeling

A fresh scoped context sees `neutral.md`, date-eligible authorities and public prior decisions relevant to the case, and these procedural rules. It does not see Stone's proposal or personal documents, the current case's historical appellate outcome, or future Supreme Court follow-up. For each participating non-Stone judge, save a concise disposition, sufficient legal ground, material remedy position, sources, and any actual barrier to joining another rationale in `commitments.md`. Routine agreement may be stated compactly without losing individual attribution.

Use that judge's available date-eligible writings and the legal record. Party of appointment, ideological labels, a desired margin, or dramatic value cannot supply a vote. Consider genuinely plausible alternative paths when they matter, without manufacturing a second viable answer. Save and lock this stage before exposing history. Isolation is a property of the execution context, not merely of the file layout.

### Historical reconciliation

A separate context receives the frozen neutral material and commitments plus `history.md`, but no Stone proposal or personal material. History is strong evidence to the extent its premises survive. For each material difference, identify the changed legal, factual, procedural, or remedial premise and why it matters to that particular judge. Neither force agreement with history nor authorize a departure just because Stone is now present. Save the final reconciled positions and remaining uncertainty in `reconciled.md` before assembly.

### Assembly

Introduce the approved `stone.md` only after reconciliation is locked. Compare exact judgment components, legal propositions, remedies, and join limits. Agreement on the disposition alone is not agreement on every rationale. A normal three-judge panel needs two actual joins for a majority proposition. Where the panel is fractured or an exceptional composition applies, determine authority under governing law rather than adding incompatible rationales together.

Opinion assignment and circulation follow the circuit's applicable practice; authorship is not Stone's entitlement or mechanically copied from the historical case. A revised join must answer a documented legal objection and state its scope. New neutral evidence or a new decisive legal premise returns the affected issue to fresh neutral modeling and reconciliation. Do not secretly rewrite frozen positions in assembly to obtain a coalition.

Preserve concise grounds and sources, not hidden reasoning transcripts. Retain only the current live stage files plus Git history. If an isolation boundary was breached, redo the affected uncommitted stage in a fresh context.

## 7. Judgment, authority, and preservation

Use [the decision-record template](templates/DECISION_RECORD.md). State the judgment for each separable component; the author and joins of each writing; the controlling holding and operative qualifications; the standard applied; treatment of earlier law; questions left open; and the precise remedy, mandate status, and next step.

Separate circuit precedent, party-specific relief, dicta, and separate opinions. Stone's dissent never becomes circuit law merely by appearing in the record. A historical citation identifies the source appeal; do not represent a new simulation opinion as a published historical reporter text.

A final record is authoritative once validated and saved. Update the precedent index and Standing State immediately after it, preserving the correct effective date. A render cannot add a holding or repair an unsupported vote. Corrections are explicit, user-authorized changes with internal lineage and Git history; public decision prose need not narrate the editing workflow.

For a completed judicial event, use the [render template](templates/RENDER.md) under the [render contract](RENDER_CONTRACT.md) after locking the record. An individual decision includes a summary and the actual written opinion, plus supported separate writings; the record's Public decision section must contain the identity, dates, panel, joins, and every substantive item needed. Internal metadata and historical comparison are not inputs to that decision render. After every simulation turn, automatically display and save the eight-section Form A court report using the contract's scoped, dated administrative and public-source packet. This includes preparation and follow-up turns where no decision is issued. Explain the current case in readable detail, then any completed outcome, controlling reasoning, supported practical effect, and written opinions for decisions completed that turn. Keep unchanged sections brief. A link or completion notice alone is not the turn output. A report is presentation only: it cannot alter state, invent a proceeding, approve Stone's position, or become the combined input for neutral modeling. Do not include future outcomes or ideological forecasts. Repository maintenance and standalone explanatory questions do not themselves require a simulation report.

## 8. Historical Supreme Court and later proceedings

The Supreme Court's actual composition, holdings, and dates remain historical. Do not import `scotus-career` holdings or model a new Supreme Court vote, certiorari choice, merits result, or remand. Its historical decisions govern later circuit events according to their actual scope and temporal effect, even when this circuit reached a different view earlier.

The render shows only the user's selected cases and their connected review proceedings, including earlier-year carryovers. Every Supreme Court review entry must link to a selected circuit case and explain its effect on the finalized simulated judgment. Do not add independent entries for other Supreme Court cases. Continue researching and applying relevant historical law; mention other cases in the render only as authority directly needed to explain a selected case or its applicable law.

Keep two questions separate:

1. **What historical Supreme Court law now binds this circuit?** Research and apply the real authority, including its temporal reach. Record any effect on an indexed circuit holding.
2. **What actually happened, or can coherently be retained, in this changed appeal's procedural path?** A historical petition or outcome attaches only after checking the judgment, parties seeking review, questions, posture, relief, and timing against this appeal's final record.

Track petitions, grants, denials, merits decisions, vacaturs, mandates, and remands in Standing State when supported and due. Do not infer a filing, denial, finality, or automatic reversal from silence, the passage of time, or a historical event belonging to a materially different judgment. Denial of certiorari is not approval of the circuit's reasoning.

When a historical follow-up's predicates no longer fit, preserve it in the segregated historical material as a comparator, mark the live matter `unresolved: historical path incompatible`, and state what remains uncertain. Do not invent a substitute Supreme Court proceeding or automatically transfer its case-specific mandate. The historical Supreme Court opinion remains law on its date; the procedural reconciliation of this changed case remains open. Resolve it only on supported compatible events or an explicit later user instruction. Continue unrelated cases.

The circuit may independently simulate its own rehearing, mandate, and remand proceedings when properly before it, using the historical Supreme Court law then in effect. Verify whether relief is available in the actual procedural posture; a new precedent does not automatically reopen a closed judgment.

### Rolling review across calendar years

Supreme Court follow-up is part of every simulation turn and calendar advance, not a separate task the user must remember to request. Organize review by the year of each case's first selected circuit decision. Retain that origin year through later petitions, renamed captions, new Supreme Court docket numbers, rehearings, and remands; keep supported links between those identifiers.

The default review view emphasizes the current calendar year and the previous two years. Thus the 1996 view includes 1994, 1995, and 1996 cases, and the 1997 view includes 1995, 1996, and 1997 cases. Also include every older unresolved matter. This is a rolling tracking window, not a three-year procedural schedule or an expiration rule. Actual historical event dates control: do not delay an early grant, denial, or decision, or manufacture a result at origin year plus two. Do not remove open matters at the end of the repository's 2020 folder range.

Apply this sequence:

1. After a selected circuit decision is finalized, establish its origin year and review follow-up reference in the final record. Carry any supported pending proceeding in Standing State. If petition status is not established, create a specific research task instead of inventing a pending petition.
2. Before advancing from the current date to the next authorized event date, check all unresolved review proceedings and research tasks, including older carryovers, and relevant intervening Supreme Court law. A full-year advance must process intervening events in date order before any later circuit adjudication, rather than postponing all review to year-end.
3. The follow-up preparer may research historical chronology, using segregated `historical-follow-up.md` material where needed. Release only verified events due on or before the current processing cutoff. Future outcomes stay outside Standing State, the render packet, and neutral adjudication. A future argument date may appear only when its scheduling was already established by that cutoff.
4. For each due event, verify the source, exact event date, linked appellate judgment, Supreme Court docket or other identifier, and compatibility with the simulated case. Process verified filings, grants, denials, arguments, merits dispositions, vacaturs, mandates, and remands when they occur; do not require every case to pass through every stage. A denial or other terminal event does not generate a later merits decision.
5. Record each admitted event once, using its case identity, docket, date, event type, and source to avoid applying it again on repeated turns. Save the dated final event record, then update the existing Standing State row and any affected precedent-index entry. Recheck compatibility when an intervening change affects the judgment or posture. A historical Supreme Court opinion's effect as general law is recorded separately from any incompatible case-specific path.
6. Before the turn's render, summarize new review events and all still-open matters. Link each update to its origin-year case, even when the current session's selected docket contains only newer cases. Section 8 reports newly filed petitions, grants or denials, arguments, and actual results, with published reasoning when available; section 7 carries the outstanding procedural status and blockers. If nothing changed, say so briefly, without implying that an unverified filing does not exist.
7. Preserve unresolved proceedings and research gaps at year-end, beyond the three-year view, and after a Supreme Court disposition if mandate or remand work remains. Archive only a supported terminal matter whose remaining obligations have been reconciled. A late-discovered event affecting completed decisions follows the explicit-correction rule; never silently rewrite those decisions.

Standing State records the latest completed follow-up check and its coverage limitations. The check date is not evidence of a petition, denial, or finality. Do not mark an unperformed or incomplete check as complete. A source gap blocks only the affected issue or case; continue independent work when consistent with the chronology rules.

## 9. Standing State and annual close

Standing State is a living tracker here, not a copy of the Supreme Court project's narrower opening-term document. It contains the current institutional snapshot, case-list pointers, and open rehearings, petitions, mandates, remand returns, dependencies, and specific follow-up blockers. Link every change to a dated final event record or a verified source. Keep private positions, frozen deliberative material, and future historical outcomes outside it.

Maintain it using the [Standing State template](templates/STANDING_STATE.md). Preserve origin years and review identifiers, check unresolved review automatically before calendar advances and renders, and carry older open cases alongside the three-year view. Replace placeholders with sourced current information, preserve existing unresolved entries and cycle counts, and remove only reconciled terminal items. The form is not authorization to reset the live tracker or create an annual duplicate.

Separate a **research task** from a known pending proceeding. Unknown petition status is not proof a petition exists. Record only evidenced deadlines and identify any unresolved date calculation. Retain a succinct terminal entry until annual close, then preserve its source in the case record and carry forward only live matters. A year may close with explicitly carried pending cases.

Annual close checks selected-case coverage, records, effective precedent treatment, chronology, roster updates, and all carryovers, including unfinished coverage cycles. Each completed eighteen-case cycle separately receives the selection policy's coverage and source audit, with exactly three cases in each group. Neither close process reruns merits, creates new law, or requires copying the entire body of historical law. There is no five-pass close or mandatory duplicate tracker set.

## 10. Validation and failures

Check source identity and date; panel eligibility; preserved questions and review standards; disposition and join arithmetic; controlling status; remedy and mandate consistency; historical compatibility; and links between final records, state, and public output. Identify limitations specifically. Never claim an unsupported source, a fresh context that did not exist, a user approval that was not given, or a legal conclusion established by a script.

If a defect affects only one issue or case, preserve the remaining valid work. Do not erase completed decisions to tidy a directory. File cleanup preserves the single current version and uses repository history for superseded content.

