# Historical case selection

Use six groups, three historical cases per group, for an **18-case cycle**. Historical availability determines when a cycle can be completed. A cycle can span calendar years; it is not an annual quota and does not describe the historical court's entire docket.

The supplied rule called this a fifteen-case cycle, but six groups multiplied by three cases equals eighteen. This policy preserves the six groups and three cases per group, and uses eighteen consistently for completion and audit.

## Six coverage groups

| Group | Areas covered |
|---|---|
| 1. Criminal law, sentencing, and post-conviction review | Criminal offenses, searches and seizures, interrogation, evidence, trial rights, sentencing, habeas corpus, capital punishment |
| 2. Constitutional rights, civil rights, and elections | Speech, religion, association, equal protection, substantive due process, reproductive rights, firearms, prisoners' civil rights, housing discrimination, voting, election law |
| 3. Labor, employment, and employee benefits | Employment discrimination, retaliation, wages and hours, unions, collective bargaining, workplace safety, public employment, pensions, ERISA |
| 4. Government powers, administrative law, and public regulation | Federalism, separation of powers, federal Indian law, agency review, immigration, environmental law, taxation, public benefits, public lands, transportation, energy, communications |
| 5. Business, property, and private civil litigation | Contracts, torts, insurance, securities, antitrust, bankruptcy, copyright, trademark, maritime law, property, takings, commercial arbitration |
| 6. Federal courts, civil procedure, and remedies | Jurisdiction, standing, removal, federal-state court relations, immunity, pleading, discovery, summary judgment, class actions, preclusion, appellate procedure, injunctions, damages, attorney fees |

## Selection rules

1. **Historical cases only.** Every selected case must correspond to an identifiable, real proceeding. Preserve its actual parties, underlying dispute, material facts, claims, and procedural history up to the point at which the simulation takes over. Do not create composite cases or invent facts to improve a legal question.
2. **Use the selected circuit's historical docket.** For this project, a case must actually have been before the Second Circuit at the relevant time. Cases from other circuits can supply precedent or background where appropriate, but cannot be transplanted into the playable docket.
3. **Select three cases from each group.** Count each case once. Assign its primary group according to the principal question the simulated court must decide. Record overlapping subjects as secondary tags. An incidental jurisdictional or remedial issue does not automatically move every case into Group 6. Do not relabel a case merely to fill a slot.
4. **Rotate narrower subjects.** The three cases within a group should address different subfields whenever the historical docket permits. Across cycles, prioritize available subjects that have appeared least recently.
5. **Let chronology control eligibility.** Introduce each case at the appropriate historical stage. If a group lacks a suitable case, leave its slot pending and carry it forward as simulated time advances. Do not move a later dispute backward merely to finish the cycle. Apply the engine's appointment, submission, and panel-eligibility checks as well.
6. **Verify the source before admission.** Record the case name, court, docket number or reported citation, relevant dates, and supporting source. Use court opinions, docket records, orders, and briefs where available. Identify allegations and disputed facts accurately. Leave unsupported details unspecified. An unverified candidate is not an admitted case and cannot fill a completed slot.
7. **Separate historical research from the playable record.** A later opinion may help reconstruct an earlier proceeding, but the judge receives only facts, arguments, and authorities available at the simulated decision point. Later holdings do not become earlier precedent. Preserve the engine's separate neutral, reconciliation, and Stone stages; never pass the full historical case list to a neutral modeler if it reveals outcomes or departures.
8. **Preserve the historical starting point; allow simulated appellate decisions.** The underlying case is historical. Its appellate disposition may change through the simulation. Record any resulting departure from actual history, and check whether that departure affects the eligibility or posture of later historical cases. This does not authorize fictional Supreme Court actions or import the separate Supreme Court simulation's law.
9. **Select for coverage, not preferred outcomes.** Include ordinary applications of settled law alongside difficult statutory, factual, and constitutional disputes. Do not require ideological balance in winners, divided panels, or doctrinal breakthroughs.
10. **Audit each completed 18-case cycle.** Verify three completed cases in each of the six groups. Review neglected subfields, repeated issues, source quality, departures from history, and the consequences for later cases. Carry those findings into subsequent selection. An incomplete cycle remains open across a year boundary.

## Counting and chronological continuity

- A case receives one cycle number and one primary group. Admission reserves a slot; completion requires a saved final record resolving the selected appellate event. A jurisdictional dismissal may complete that event. A draft, proposed vote, or mere preparation does not.
- Consolidated companion matters handled as one detailed-play unit count once. Multiple claims, opinions, or docket numbers do not multiply the count. A genuinely distinct later appeal is a new unit only if admitted and justified separately, not merely because it follows a remand.
- Rehearing, certiorari activity, mandates, remand proceedings, rendering, and corrections do not count as additional cases for the same selected unit. Track continuing proceedings in Standing State even after the unit counts as played.
- Keep actual events in chronological order. Do not hold an otherwise selected historical event for a later fictional date to wait for another group's slot. If its group is already filled in an earlier cycle, it may be allocated to the next cycle with an available slot. Open cycles can overlap in time; do not overfill a group or erase older pending slots.
- If a candidate is withdrawn before play because the source or posture fails verification, release its reserved slot and record the reason. Do not invent a replacement proceeding. Document any justified classification correction and reconcile the affected cycle totals without altering the decision itself.
- Annual close reconciles pending work; cycle close audits coverage. They are separate operations. Neither requires reopening completed merits or stopping unrelated due events.

## Tracking and file ownership

Each admitted case has one canonical row in the case list for the calendar year in which detailed play begins. Link its case name to its case folder. Later years and cycle audits point back to that row instead of creating another selection entry.

Use the [case-list template](templates/CASE_LIST.md):

**Cycle | Case name | Circuit | Docket/citation | Historical stage and date | Primary group | Secondary subjects | Principal question | Source | Simulation status | Departure from history**

The Cycle column links the user's requested fields to cross-year coverage accounting. Historical panel membership, the member Stone replaces, the assignment reason, and detailed simulation dates remain mandatory in the linked neutral packet and final event record under the [case brief template](CASE_BRIEF_TEMPLATE.md).

Before play, Departure from history is `Not yet assessed`; it is not a prediction. After play, summarize the actual difference or state that none was found, and link to the final record. This administrative column is excluded from neutral inputs.

[Standing State](../state/STANDING_STATE.md) holds a small progress summary for open cycles and their remaining group slots. It does not duplicate the case rows. Once a cycle is complete, save a concise audit at `cycles/NNN/audit.md` with links to its eighteen canonical rows and final records, verified group totals, coverage gaps, source concerns, and downstream history checks. Do not create an empty audit file that implies completion.
