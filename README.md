# Federal Appellate Court

A historical Second Circuit simulation centered on Circuit Judge Alex-Lamar Stone-Khoury, beginning January 1, 1994. In this fictional timeline, Stone is commissioned and takes the required judicial oaths on December 1, 1993, so 1994 is his first full calendar year. He fills Thomas J. Meskill's vacancy ahead of the appointment historically given to Guido Calabresi. Calabresi does not join this court in this simulation.

The Supreme Court remains historical. Its actual decisions become governing authority on their historical dates. No holdings, Justices, or outcomes from the separate `scotus-career` simulation are imported.

## Start here

- [Operating instructions](AGENTS.md)
- [Run commands](foundation/RUN.md): say "run this year" or "run this session" in chat; `tools/court.py` checks bookkeeping and stages isolated inputs
- [Reusable templates](foundation/templates/README.md): Standing State, case brief, decision record, render, and case list
- [Appellate engine](foundation/ENGINE.md)
- [Case-selection policy](foundation/CASE_SELECTION.md) and [case-list template](foundation/templates/CASE_LIST.md)
- [Court roster](foundation/COURT_ROSTER.md)
- [Character](stone/CHARACTER.md): biography only
- [Standing State](state/STANDING_STATE.md): current date, institutional setting, and pending proceedings
- [Precedent index](state/PRECEDENT.md): effective simulation holdings and subsequent treatment
- [1994 case list](years/1994/case-list.md)

The character's appointment chronology has been revised to make 1994 his first full calendar year; his other background remains intact. Stone is 38 at commission and at the January 1994 opening; the earlier preference for 40 has not been silently substituted.

`stone/JURISPRUDENCE.md` is retained only as the user's archive. The engine must never read, search, import, summarize, embed, validate, or use it at any stage, including through existing engine-generated summaries or other archival derivatives. The latest user-approved case brief `stone.md` supplies Stone's case-specific disposition and reasoning. Ask for user input only when neither the approved brief nor a genuine existing delegation covers a required choice; never use an archival fallback.

## Work cycle

1. **Prepare the [year] case list.** Select real historical Second Circuit appeals under the six-group policy: three cases per group, eighteen per cycle. Record each case once using the case-list template, and establish its case-specific panel substitution in the linked packet. Historical availability controls timing; cycles may span years.
2. **Prepare [case].** Use the [case brief template](foundation/CASE_BRIEF_TEMPLATE.md) to make separate neutral, Stone, and historical-comparison files. Prepare Stone's proposed position from the user's case-specific instructions and the legal packet. A proposed Stone position is not an approved vote.
3. **Run [case].** Model the other judges from neutral materials in a fresh context, reconcile against history in a separate context, then introduce Stone's approved proposal in assembly. Save the final event under the [decision-record template](foundation/templates/DECISION_RECORD.md).
4. **Read the automatic turn report.** Every simulation turn ends with the [render template](foundation/templates/RENDER.md)'s eight-section court report displayed in the response and saved under the [render contract](foundation/RENDER_CONTRACT.md); no separate Render request is needed. This includes preparation and follow-up turns where no decision is issued. Explain the current case, any completed outcome, the reasoning, and realistically relevant sourced context in readable detail, with unchanged sections kept brief. A standalone case opinion or event report can also be requested. A completed decision includes a summary and actual written opinions, including supported concurrences or dissents, without changing the final record. A court report uses eight sections for current work, court composition, the session's case list, current case details, completed opinions, legal developments, follow-up, and Supreme Court review of selected cases awaiting argument or decision and already decided. Every review entry links to the original selected circuit case and explains its effect on the simulated judgment; unselected cases appear only as necessary legal authority, not independent case reports. The session table gives case captions, dockets, event dates and types, status, and areas of law; coverage counts stay in the background records. The report uses dated source extracts, excludes vote forecasts and future outcomes, and does not replace the live state or neutral case packet.
5. **Automatic rolling follow-up / close [year].** Before every calendar advance and turn report, check review events for the current year, the previous two decision years, and every older unresolved case. Process due events chronologically and report new petitions, grants or denials, arguments, decisions, and remands with their original case and year. Use the [Standing State template](foundation/templates/STANDING_STATE.md) to retain docket links, check limitations, pending proceedings, and unfinished coverage cycles. The three-year view does not force a 1994 case to receive a Supreme Court result in 1996; actual historical dates and compatibility control. Audit each completed eighteen-case cycle separately. Closing a year does not close an unresolved appeal or delay the effectiveness of its holdings.

Holdings and legal tests stay in the individual final decision records. There are no separate Holdings or Standards and Tests documents. The small precedent index links to those records and tracks later treatment; Standing State tracks the court and pending procedure.

Folders named `years/` are simulation bookkeeping periods, not an assertion that the circuit follows Supreme Court October Terms. The initial period is January 1 through December 31, 1994. December 1993 is an appointment and transition baseline, not an extra played year. Eighteen 1994 appeals were admitted and all eighteen have been played, through the simulation date of 1994-12-23; the year has not yet been annually reconciled.

Historical law and the historical procedural fate of a particular case are checked separately. A changed appellate judgment does not automatically inherit the historical certiorari result, Supreme Court disposition, or remand. An incompatible follow-up remains explicitly unresolved; this engine does not invent Supreme Court action.

See [migration notes](foundation/MIGRATION.md) for what was adapted from the Supreme Court framework.

