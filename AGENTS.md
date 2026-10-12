# Appellate simulation instructions

This repository runs selected historical Second Circuit appeals beginning July 21, 1994. The user controls Judge Alex-Lamar Stone-Khoury. Follow [the engine](foundation/ENGINE.md). This is a separate project from `scotus-career`; its old instructions, permissions, case outcomes, and standing fallbacks do not apply here.

## Authority and reading boundaries

- The engine controls simulation procedure and source roles. Governing historical law still comes from verified legal sources, not from a character document.
- [Case selection](foundation/CASE_SELECTION.md) controls six coverage groups, three historical cases per group, and eighteen-case cycles across calendar years. Use the [case-list template](foundation/templates/CASE_LIST.md); keep one canonical row per case. Audit each completed cycle and carry unfinished group slots in Standing State.
- [Standing State](state/STANDING_STATE.md) identifies the current date and pending work. Maintain it with the [Standing State template](foundation/templates/STANDING_STATE.md), preserving existing live entries. [The roster](foundation/COURT_ROSTER.md) supplies dated institutional facts. Future roster entries are scheduling information only.
- [Precedent](state/PRECEDENT.md) is an index. Final event records and effective historical authorities control legal substance. Do not create separate Holdings or Standards and Tests registers; preserve holdings and applied tests in each final record.
- [Character](stone/CHARACTER.md) controls biography. [Jurisprudence](stone/JURISPRUDENCE.md) guides drafting Stone's position. Neither supplies a court holding, a colleague's agreement, or an approved case-specific choice.
- The latest user-approved `stone.md` controls Stone within the law and its stated scope. Do not assume the old Supreme Court fallback applies or silently fill a missing vote. A conflict with binding authority must be identified and resolved before assembly.
- [Render rules](foundation/RENDER_CONTRACT.md) and the [render template](foundation/templates/RENDER.md) govern presentation only. All reusable forms are linked in the [template index](foundation/templates/README.md).

Read only the sources needed for the stage. Do not preload Stone's files, the historical case result, or future legal developments into a neutral modeling context.

## Run stages

Use [the brief template](foundation/CASE_BRIEF_TEMPLATE.md) and these separate files under `years/YYYY/cases/<case-slug>/`:

1. Preparation creates `neutral.md`, `stone.md`, and `history.md`. A preparer who has read all three cannot act as the isolated neutral modeler in the same context.
2. A **fresh neutral context** sees only the neutral packet, its date-eligible authorities, relevant public prior decisions, and procedural engine rules. It models the participating judges other than Stone and saves `commitments.md`.
3. A **separate reconciliation context** sees the neutral material, frozen commitments, and historical comparison, but never Stone's private material. It saves `reconciled.md`.
4. Assembly receives the frozen reconciled positions and the approved Stone proposal. It determines actual agreement on judgment, reasoning, remedy, authorship, and separate writings. Save a dated final event record.
5. Update Standing State and the precedent index from completed final events. End every simulation turn with the template's eight-section Form A court report, displayed directly to the user and saved, without waiting for a separate Render request. Explain the current case, any completed outcome, the reasoning, and supported practical context; include written opinions for decisions completed in that turn. Keep unchanged sections brief and report an undecided case as undecided. The report uses the contract's separately prepared, dated administrative and public-source extracts; never feed that combined report to neutral modeling. Individual decision renders still receive only the final record's public decision, render contract, and template and cannot add legal substance. Repository maintenance or standalone explanatory questions do not themselves require a simulation report.

Delegate the substantive neutral and reconciliation stages to separate scoped agents or equivalent fresh executions when running a case. Pass an explicit allowed-file list and no inherited conversation containing Stone or the comparator. A new filename, prompt section, or instruction to forget is not isolation. If fresh contexts are unavailable, finish preparation and report that specific limitation; do not claim an isolated Run occurred. These requirements do not call for agents when merely editing infrastructure.

## Working rules

- Supreme Court membership and decisions remain historical. Never generate a replacement Supreme Court vote, holding, grant, denial, or remand.
- Select real historical Second Circuit appeals under the case-selection policy. Preserve their historical parties, dispute, material facts, claims, and pre-simulation procedure. A case-specific panel substitution is a declared simulation premise, not a discovered historical fact. Case-list departures and future outcomes are not neutral inputs.
- Keep the two supplied Stone documents substantively unchanged unless the user requests edits. Never revise an approved Stone proposal silently.
- Validate chronology, panel eligibility, vote and join arithmetic, authority status, record links, and follow-up continuity. Scripts may check bookkeeping but may not choose legal meaning or judicial votes.
- Use primary sources for legal propositions and the relevant date's statutes and rules. Do not transplant modern appellate rules into 1994.
- Record only concise conclusions, grounds, sources, and material uncertainties. Do not generate hidden reasoning transcripts or fictional conference dialogue.
- Stop only the affected case or issue for a material gap. Continue independent authorized work.
- User-authorized corrections replace the affected final record in place, identify the correction internally, and update dependent indexes and renders. Preserve history in Git. Do not silently change other completed cases.
- Update effective law and pending status after each final event. Annual close is reconciliation, not a new adjudication or a requirement to duplicate every historical holding.
