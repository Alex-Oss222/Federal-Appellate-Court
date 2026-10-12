# Federal Appellate Court

A historical Second Circuit simulation centered on Circuit Judge Alex-Lamar Stone-Khoury, beginning July 21, 1994. Stone receives the appointment historically given to Guido Calabresi, filling the vacancy left by Thomas J. Meskill. Calabresi does not join this court in this simulation.

The Supreme Court remains historical. Its actual decisions become governing authority on their historical dates. No holdings, Justices, or outcomes from the separate `scotus-career` simulation are imported.

## Start here

- [Operating instructions](AGENTS.md)
- [Appellate engine](foundation/ENGINE.md)
- [Case-selection policy](foundation/CASE_SELECTION.md) and [case-list template](foundation/templates/CASE_LIST.md)
- [Court roster](foundation/COURT_ROSTER.md)
- [Character](stone/CHARACTER.md) and [jurisprudence](stone/JURISPRUDENCE.md)
- [Standing State](state/STANDING_STATE.md): current date, institutional setting, and pending proceedings
- [Precedent index](state/PRECEDENT.md): effective simulation holdings and subsequent treatment
- [1994 case list](years/1994/case-list.md)

The character and jurisprudence documents retain their supplied content. The character currently makes Stone 38 at commission; the earlier preference for 40 has not been silently substituted. General references in the jurisprudence to a later Supreme Court career do not establish a Supreme Court appointment in this project.

## Work cycle

1. **Prepare the [year] case list.** Select real historical Second Circuit appeals under the six-group policy: three cases per group, eighteen per cycle. Record each case once using the case-list template, and establish its case-specific panel substitution in the linked packet. Historical availability controls timing; cycles may span years.
2. **Prepare [case].** Use the [case brief template](foundation/CASE_BRIEF_TEMPLATE.md) to make separate neutral, Stone, and historical-comparison files. A proposed Stone position is not an approved vote.
3. **Run [case].** Model the other judges from neutral materials in a fresh context, reconcile against history in a separate context, then introduce Stone's approved proposal in assembly. Save the final event under the [decision-record template](foundation/templates/DECISION_RECORD.md).
4. **Render [case].** Present the completed decision under the [render contract](foundation/RENDER_CONTRACT.md), without changing it. This can follow Run once the decision is locked.
5. **Update follow-up / close [year].** Record verified subsequent proceedings and carry open matters and unfinished coverage cycles forward in Standing State. Audit each completed eighteen-case cycle separately. Closing a year does not close an unresolved appeal or delay the effectiveness of its holdings.

Folders named `years/` are simulation bookkeeping periods, not an assertion that the circuit follows Supreme Court October Terms. The initial period is July 21 through December 31, 1994. No case has been selected or adjudicated yet.

Historical law and the historical procedural fate of a particular case are checked separately. A changed appellate judgment does not automatically inherit the historical certiorari result, Supreme Court disposition, or remand. An incompatible follow-up remains explicitly unresolved; this engine does not invent Supreme Court action.

See [migration notes](foundation/MIGRATION.md) for what was adapted from the Supreme Court framework.
