# Run commands

Chat commands that drive the stages in [AGENTS.md](../AGENTS.md) and the [engine](ENGINE.md). They add no legal rule, vote, or approval. Where this file and the engine differ, the engine controls.

## Commands

| Say | Slash form | Scope |
|---|---|---|
| run this year | `/run-year` | The current simulation year, from case selection through annual close. |
| run this session | `/run-session` | The admitted, unfinished cases. If none is open, first admit one batch (see Selection). |

The year is the calendar year of **Current simulation date** in [Standing State](../state/STANDING_STATE.md), never the real-world date. A later year cannot run until the current one is closed or its open matters are explicitly carried. A session is a working batch; the report labels it by the date range of its events. Words after the command can only narrow it (a case count, one group, one case) or delegate a stated kind of Stone choice as described under Gates. A narrowed run (`python3 tools/court.py plan session --only <slug>,<slug>`) holds finalization only against the cases it names; the unnamed earlier cases stay unplayed, and playing one of them later is a late-discovered earlier event under [engine section 3](ENGINE.md). Use a narrowed run for a test whose results the user intends to discard. A run never continues into the next year on its own.

## Before every run

1. `python3 tools/court.py check`. Fix bookkeeping errors inside the scope; report the rest.
2. `python3 tools/court.py plan year` or `plan session`. The plan is derived from the files. After an interruption or a context reset, run it again and continue from it instead of relying on memory of earlier turns.

The plan lists each case in event-date order with its next stage (prepare, neutral, reconcile, brief, assemble, render, compare, finalize, done, or blocked and withdrawn) and the task sentence that starts it. It also shows each case's brief as missing, proposed, or approved.

## Stages

| Stage | Done when | Executed by | Inputs | Output |
|---|---|---|---|---|
| select | Case-list row with a verified source ([rule 6](CASE_SELECTION.md)) | One research agent per group with an open slot | Selection policy, case lists, primary sources | Row, status `admitted` |
| prepare | `neutral.md` and `history.md` exist | Preparer agent; it may read the historical opinion and returns only paths and gaps, never a disposition or rationale | [Brief template](CASE_BRIEF_TEMPLATE.md), engine sections 3 to 5, primary sources | `neutral.md`, `history.md`, optional `historical-follow-up.md` |
| neutral | `commitments.md` exists | Fresh agent or task | Staged inputs | `commitments.md`, committed alone |
| reconcile | `reconciled.md` exists | A second fresh agent or task | Staged inputs | `reconciled.md`, committed alone |
| brief | `stone.md` exists and shows user-approved with a reference | The user supplies and approves it; this context may only format the user's case-specific instructions into the template, marked Proposed | The user's instructions and `neutral.md`; never `history.md` | `stone.md` |
| assemble | A final event record exists and validates | Fresh agent or task | Staged inputs | `events/YYYY-MM-DD-<event>.md` |
| render | The case's `output/` holds the individual decision | Fresh agent or task | Staged Public decision section | `output/YYYY-MM-DD-<event>.md` |
| compare | `comparison.md` exists | Fresh agent or task | Staged Public decision section; `history.md`; `historical-follow-up.md` if present | `comparison.md`: the Departure text, a comparison extract of at most 180 words, and the follow-up compatibility table |
| finalize | Status `played`; Departure cell written; Standing State and [precedent index](../state/PRECEDENT.md) updated | This context | `comparison.md` and the Public decision section | Case list, `state/` files |

Neutral and reconcile never read the brief, so they proceed while the user supplies or approves it. No stage, agent, or script opens `stone/JURISPRUDENCE.md`, which is archival storage, and `stone/CHARACTER.md` supplies biography only; neither appears in any allowed-file list.

Before accepting an assembled record, run `check` and read the judgment, joins, and remedy for arithmetic and consistency; send defects back to the assembling agent. Finalize (after the render and `comparison.md` exist) updates the simulation date to the decision date, the last-event pointer, the cycle table from the case list, and the final record's origin year and review follow-up reference, and adds pending proceedings only for events the engine supports ([section 8](ENGINE.md)).

## Isolation

Each isolated stage (neutral, reconcile, assemble, render, compare) runs in a fresh context that sees only its staged files: a fresh task in Codex cloud, a fresh `general-purpose` subagent in Claude Code, or an equivalent. Never fork or continue a conversation that contains Stone's brief or the comparator. The procedure is the same on every platform:

1. `python3 tools/court.py stage <slug> <stage> --dest <scratch>/<slug>-<stage>` copies exactly the permitted files (render and compare receive only the final record's Public decision section) and prints the one file the stage may write. The scratch folder is outside the repository.
2. The stage context is told the folder, the printed file list, the one output file, and these limits: read nothing outside the folder, run no git commands, do not search the repository, and in the neutral stage do not look up this case's own appellate opinion or anything dated after the legal cutoff.
3. When the stage finishes, `python3 tools/court.py accept <slug> <stage> --dest <folder> [--mode "..."] [--agent <id>]` checks that the folder holds only the staged inputs, unchanged, plus one new file; files it in the case folder; and completes the execution record (mode, permitted inputs, input commit, date). Commit `commitments.md` and `reconciled.md` each on its own so Git shows the freeze.
4. If a stage reports reading outside its list, discard its output and rerun the stage in a new context.

Claim no more than a fresh context and a staged allowlist; this is not an operating-system sandbox. In a full checkout, as in Codex cloud, the withheld files are on disk, so the stage is scoped by instruction and the execution record says so. If fresh contexts are unavailable, finish preparation, state the limitation, and do not claim a Run. Where the platform allows, launch independent stages together and wait for their completion rather than polling.

## Codex cloud

Setup, once: connect the repository; environment image `universal`; no setup script (the tools use only the Python standard library); internet **Limited** with an allowlist of the research hosts listed under Research sources; run each task on the branch that holds the current work.

A cloud task cannot start another task, so each isolated stage is its own task, merged before the next one begins. `python3 tools/court.py plan` prints the sentence to give for each case's next stage.

| Task sentence | What the task does |
|---|---|
| Run this session / Run this year | Reads Standing State and the case list, runs `check` and `plan`, and does the work that needs no isolation: preparation checks, the panel draw, follow-up checks, and finalize steps whose inputs exist. It never runs an isolated stage itself. It ends with the Form A report and the list of next task sentences. |
| Prepare <slug> | Builds or repairs `neutral.md`, `history.md`, and any follow-up file; fixes the panel with `draw --case`; may read the historical opinion; returns paths and gaps only. |
| Neutral stage: <slug> | Stages, models, accepts, and commits `commitments.md` alone. |
| Reconcile stage: <slug> | The same for `reconciled.md`. |
| Assemble stage: <slug> | The same for the final event record; needs an approved `stone.md`. |
| Render stage: <slug> | The same for the individual decision. |
| Compare stage: <slug> | The same for `comparison.md`. |
| Finalize: <slug> | In its own context: runs the follow-up check, writes the Departure cell from `comparison.md`, updates the case list, Standing State, and precedent index, moves the date, and ends with the Form A report. |

Stage tasks for different cases may run in any order, but assemble, render, compare, and finalize follow "Order and chronology". Where the same stage covers several cases with no overlap hold, one task may take them in turn. A stage task is part of a turn, not a turn of its own: it ends with a one-line status and the next task sentence, and the turn's Form A report comes from the Finalize or Run task that closes it.

## Selection

- Year scope: fill the unfilled slots of the lowest cycle that has any. Open a new cycle only when every existing cycle is fully played or the user asks; a fully admitted cycle that still awaits play is not a reason to select more cases. The search window is the simulation date through December 31 of the year. Admit only a case Stone could lawfully have heard; a submission before his oaths needs a supported reargument or resubmission premise recorded in `neutral.md` ([engine section 3](ENGINE.md)).
- Session scope with no open case: admit at most one case for each group with an unfilled slot in that cycle, earliest verified dates first.
- Carry instead of fill: when the user directs that open slots not be filled, record the direction and its date in Standing State and run no selection, in any scope, until the user lifts it. The slots stay open and carried; the plan's admission target is then informational only.
- Research agents return row fields and sources only. A candidate that fails rule 6 leaves its slot unfilled with the gap noted; never invent a replacement.
- Write ISO dates in the row's historical stage cell, set Departure to `Not yet assessed`, and keep rows in chronological order. An `admitted` row links to the case folder that the prepare stage will create, and `tools/court.py check` accepts that link until then.

Panel substitution: Stone replaces exactly one historical panelist. Run `python3 tools/court.py draw --case <slug>` before any modeling. The command reads only that case's `neutral.md`; the docket comes from `Docket or citation`, and the three full names come from `Historical panel`. Separate panelists with semicolons, put roles in parentheses, and place any source note after `Source:`. Calabresi's seat takes priority when he is present. Otherwise replace the first ranked seat without a recorded legal exclusion and retain the other two historical panelists.

The draw canonicalizes docket spacing, dash characters, leading numeric zeroes, duplicate docket entries, and docket order. Judge keys ignore case, whitespace, punctuation, accents, honorifics, parenthesized roles, Markdown formatting, and source notes. Use the same full identities; the helper does not guess aliases, missing initials, or misspellings. It sorts seats by SHA-256 of the canonical docket string, a literal `|`, and the normalized judge key. No random seed, panel-list position, date, or file path enters the ranking. Do not change these inputs to obtain another result.

Set `Replacement exclusions` to `None` unless a verified legal obstacle makes a particular seat impossible to replace. For each actual exclusion, use `Full judge name = legal reason and source`, separating multiple entries with semicolons. Reasons must be unrelated to votes or authorship. The helper validates the names and presence of a reason; the operator verifies its legal basis. If no seat is replaceable, or Calabresi cannot be replaced, stop that case. Do not substitute a second panelist.

Copy the command's three Markdown fields into the packet: `Member Stone replaces`, `Resulting panel`, and `Assignment method and reason`. Re-run the same command to confirm them; `check` and neutral/reconciliation/assembly staging reject mismatched assignments. The command is read-only. Assignment does not resolve a missing designation, qualification, or resubmission order.

## Research sources

Research and preparation agents use these hosts. The environment must allow them: in Codex cloud, the internet allowlist (`www.courtlistener.com`, `static.case.law`, `www.supremecourt.gov`, `www.oyez.org`, `www.law.cornell.edu`, `www.govinfo.gov`, `www.loc.gov`, `www.uscourts.gov`, `www.ca2.uscourts.gov`, and `www.fjc.gov`); in Claude Code, `.claude/settings.json`. Last tested 2026-10-12, from Claude Code only.

| Host | Use |
|---|---|
| www.courtlistener.com | Second Circuit opinions, dockets, and citations through its API (`/api/rest/v4/`); its HTML pages refuse automated requests |
| static.case.law | Reporter text and metadata (F.3d under `/f3d/<volume>/`, for example `CasesMetadata.json`) |
| www.supremecourt.gov | Supreme Court opinions, orders, and dockets |
| www.oyez.org | Supreme Court argument dates, decision dates, and questions presented |
| www.law.cornell.edu | U.S. Code, federal rules, Supreme Court opinions |
| www.govinfo.gov | Dated editions of the U.S. Code, Statutes at Large, CFR, Federal Register |
| www.loc.gov | U.S. Reports volumes and Statutes at Large |
| www.uscourts.gov, www.ca2.uscourts.gov | Federal and Second Circuit rules and court information |
| www.fjc.gov | Judge biographies and service dates cited in the [roster](COURT_ROSTER.md) |

supreme.justia.com, openjurist.org, www.congress.gov, and babel.hathitrust.org answer automated requests with a Cloudflare challenge even though the network allows them, so adding them to an allowlist does not help. web.archive.org failed in testing. When a needed source sits on a host that fails, record the gap under the case's missing material; do not fill it from memory. A host denied by the network policy itself is reported to the user, who changes the environment's allowed domains.

## Order and chronology

- Process cases by event date. Prepare, neutral, and reconcile for different cases may run in parallel.
- Before the neutral stage of a case that has earlier-dated unfinished cases, compare principal questions in the case list only. If a legal question overlaps, hold the neutral stage until the earlier case is final, then place a sanitized extract of its Public decision in `neutral.md`.
- Assemble and finalize strictly in event-date order. A case waiting on its brief, its approval, or an earlier stage holds the finalization of later cases but not their earlier stages. A `blocked` or `withdrawn` case holds nothing.
- The simulation date moves only to the date of a finalized event, or at annual close to the start of the next period. A folder, a draft, or an approval never moves it.
- Run the rolling Supreme Court follow-up check ([engine section 8](ENGINE.md)) before the date moves to a later event date, and again before the report. A follow-up agent works from `historical-follow-up.md` and returns only verified events due on or before the new date. This context admits each event once, in date order and before any later circuit adjudication, and updates the Standing State review fields: origin year, docket links, latest check, and its limits. A source gap blocks only that matter.

## Gates

**Stone's position.** `stone.md` is the user's case-specific brief and the only source of Stone's disposition and reasoning. If the user has given case-specific instructions, format them into the [brief template](CASE_BRIEF_TEMPLATE.md), marked Proposed. If a case has no brief, or a required choice is covered neither by an approved brief nor by a delegation recorded in it, stop that case and ask the user for the missing input, covering all such cases in one message. Show each proposed brief as a short summary (caption, docket, event date, vote and disposition, holding, remedy, limits, link to `stone.md`) and ask for approval or revision. To record approval, change the brief's `Status` (or `Approval status`) to read `user-approved` and quote the user's words and the date in `Approval reference`; keep the wording plain, because `tools/court.py` treats any status containing "not", "proposed", or "pending" as unapproved. Edit a brief only as the user directs. Assembly never starts before the brief is approved and `reconciled.md` is committed.

**Delegation.** Only the user's own words delegate a choice, whether in the brief or in the command, for example "where the panel splits, join the narrower ground". Record the delegated choice in `stone.md` under `Conditions or delegated choices`, quoting the words, and do not ask about it again. A delegation covers only the kind of choice it names and never supplies a disposition or reasoning the user has not given. Say in the report when a choice rested on delegation. A bare "run this year" delegates nothing.

**Other stops.** A material gap (an unverifiable source, an ineligible panel, a missing record) sets that case to `blocked: <specific gap>`, adds a research task to Standing State, and the run continues with other cases. A late-discovered earlier event, or any change to a completed record, waits for the user's authorization ([engine section 3](ENGINE.md)). New neutral evidence or a decisive new legal premise found in assembly returns that issue to new neutral and reconcile agents. If a source cannot be reached, follow Research sources; do not substitute memory for a primary source.

## Annual close

Year scope only, once every admitted case of the year is final, blocked, withdrawn, or carried at the user's explicit instruction. Follow [engine section 9](ENGINE.md): run the follow-up check through December 31; check coverage, records, precedent treatment, chronology, and carryovers, including older unresolved review matters; apply dated roster changes through December 31 and no later; write `cycles/NNN/audit.md` for any cycle that just reached eighteen played; mark the year's case list `annually reconciled`; and set Standing State to the next period, with unresolved matters carried. The closing turn is a simulation turn and gets a report.

## Turn output and commits

Every run turn ends with the eight-section Form A report (in Codex cloud, a turn ends with the Finalize or Run task, not with each stage task), displayed in the response and saved at `years/YYYY/output/YYYY-MM-DD-court-report.md` under the [render contract](RENDER_CONTRACT.md). Build the allowed-input packet in scratch from permitted sources only; it never contains `stone.md`, `history.md`, `commitments.md`, or `reconciled.md`. Sections 7 and 8 come from the follow-up check and cover only selected circuit cases and their review proceedings; add nothing for unrelated Supreme Court cases. When a brief or approval is pending, put that request first and close with the report, which says only that Stone's position is awaited.

Commit after each stage group with a message naming the case and stage, following the session's attribution instructions. Push the working branch at the end of every turn and before waiting at a gate, because the container is ephemeral. Do not open a pull request unless asked.
