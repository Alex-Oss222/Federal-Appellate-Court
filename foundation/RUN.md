# Run commands

Chat commands that drive the stages in [AGENTS.md](../AGENTS.md) and the [engine](ENGINE.md). They add no legal rule, vote, or approval. Where this file and the engine differ, the engine controls.

## Commands

| Say | Slash form | Scope |
|---|---|---|
| run this year | `/run-year` | The current simulation year, from case selection through annual close. |
| run this session | `/run-session` | The admitted, unfinished cases. If none is open, first admit one batch (see Selection). |

The year is the calendar year of **Current simulation date** in [Standing State](../state/STANDING_STATE.md), never the real-world date. A later year cannot run until the current one is closed or its open matters are explicitly carried. A session is a working batch; the report labels it by the date range of its events. Words after the command can only narrow it (a case count, one group, one case) or delegate Stone's approval as described under Gates. A run never continues into the next year on its own.

## Before every run

1. `python3 tools/court.py check`. Fix bookkeeping errors inside the scope; report the rest.
2. `python3 tools/court.py plan year` or `plan session`. The plan is derived from the files. After an interruption or a context reset, run it again and continue from it instead of relying on memory of earlier turns.

The plan lists each case in event-date order with its next stage: prepare, propose, neutral, reconcile, approve, assemble, render, finalize, done, or blocked and withdrawn.

## Stages

| Stage | Done when | Executed by | Inputs | Output |
|---|---|---|---|---|
| select | Case-list row with a verified source ([rule 6](CASE_SELECTION.md)) | One research agent per group with an open slot | Selection policy, case lists, primary sources | Row, status `admitted` |
| prepare | `neutral.md` and `history.md` exist | Preparer agent; it may read the historical opinion and returns only paths and gaps, never a disposition or rationale | [Brief template](CASE_BRIEF_TEMPLATE.md), engine sections 3 to 5, primary sources | `neutral.md`, `history.md`, optional `historical-follow-up.md` |
| propose | `stone.md` exists, marked Proposed | This context | `neutral.md` and `stone/`; never `history.md` | `stone.md`, status `prepared` |
| neutral | `commitments.md` exists | Fresh agent | Staged inputs | `commitments.md`, committed alone |
| reconcile | `reconciled.md` exists | A second fresh agent | Staged inputs | `reconciled.md`, committed alone |
| approve | `stone.md` shows user-approved with a reference | The user | | Approval fields in `stone.md` |
| assemble | A final event record exists and validates | Fresh agent | Staged inputs | `events/YYYY-MM-DD-<event>.md` |
| render | The case's `output/` holds the individual decision | Fresh agent | Staged Public decision section | `output/YYYY-MM-DD-<event>.md` |
| finalize | Status `played`; Departure cell written; Standing State and [precedent index](../state/PRECEDENT.md) updated | This context, plus a comparator agent for the Departure cell and follow-up compatibility | Public decision section; `history.md` and `historical-follow-up.md` for the comparator only | Case list, `state/` files |

Before accepting an assembled record, run `check` and read the judgment, joins, and remedy for arithmetic and consistency; send defects back to the assembling agent. Finalize updates the simulation date to the decision date, the last-event pointer, the cycle table from the case list, and pending proceedings only for events the engine supports ([section 8](ENGINE.md)).

## Isolation

Each isolated stage runs in a fresh `general-purpose` agent, never a `fork`, which inherits this conversation. Stage its inputs with:

`python3 tools/court.py stage <slug> <neutral|reconcile|assemble|render|compare> --dest <scratch>/<slug>-<stage>`

The command copies exactly the permitted files and prints the list; render and compare receive only the final record's Public decision section. The agent's prompt carries the stage task from the engine, the staging directory, the printed list, the one output file, and these limits: read nothing outside the staging directory, run no git commands, do not search the repository, and in the neutral stage do not look up this case's own appellate opinion or anything dated after the legal cutoff.

When the agent finishes, confirm the only new file is the expected output, copy it into the case folder, and add a short block with the agent id (or that none was exposed), the permitted list, the input commit from `git rev-parse HEAD`, and the date. Claim no more than a fresh context and a staged allowlist; this is not an operating-system sandbox. Commit `commitments.md` and `reconciled.md` each on its own so Git shows the freeze. If an agent reports reading outside its list, discard its output and rerun the stage in a new agent. If fresh agents are unavailable, finish preparation, state the limitation, and do not claim a Run.

Launch independent agents in one message and wait for their completion notices rather than polling.

## Selection

- Year scope: fill the unfilled slots of the lowest cycle that has any. Open a new cycle only when every existing cycle is fully admitted, and never more than one per run. The search window is the simulation date through December 31 of the year.
- Session scope with no open case: admit at most one case for each group with an unfilled slot in that cycle, earliest verified dates first.
- Research agents return row fields and sources only. A candidate that fails rule 6 leaves its slot unfilled with the gap noted; never invent a replacement.
- Write ISO dates in the row's historical stage cell, set Departure to `Not yet assessed`, and keep rows in chronological order.

Panel substitution when the user has supplied no method: if Calabresi sat on the historical panel, Stone takes that seat. Otherwise run `python3 tools/court.py draw --docket "<docket>" --panel "<A>;<B>;<C>"` before any vote is modeled. The first seat in its output is replaced; if that seat cannot lawfully be replaced for a reason unrelated to votes or authorship, record the reason and take the next. Record the method, inputs, and result in `neutral.md` as a declared simulation premise. Never redraw for any other reason.

## Order and chronology

- Process cases by event date. Prepare, propose, neutral, and reconcile for different cases may run in parallel.
- Before the neutral stage of a case that has earlier-dated unfinished cases, compare principal questions in the case list only. If a legal question overlaps, hold the neutral stage until the earlier case is final, then place a sanitized extract of its Public decision in `neutral.md`.
- Assemble and finalize strictly in event-date order. A case waiting on approval or an earlier stage holds the finalization of later cases but not their earlier stages. A `blocked` or `withdrawn` case holds nothing.
- The simulation date moves only to the date of a finalized event, or at annual close to the start of the next period. A folder, a draft, or an approval never moves it.

## Gates

**Stone's position.** After propose, show each pending proposal as a short summary: caption, docket, event date, vote and disposition, proposed holding, remedy, limits, and a link to `stone.md`. Ask for approval, revision, or a different position. To record approval, set `Approval status: user-approved` and quote the user's words and the date in `Approval reference`. Edit a proposal only as the user directs. Never fill a missing position from the jurisprudence, the character sheet, or an earlier case. Approval may arrive before neutral and reconcile finish, but assembly never starts before `reconciled.md` is committed.

**Delegation.** Only the user's own words delegate approval, for example "approve Stone's proposals as drafted". Quote them in `Conditions or delegated choices` and `Approval reference`, limit the delegation to the cases and conditions named, and say in the report that approval rested on delegation. A bare "run this year" is not a delegation, and a delegation does not carry into later runs.

**Other stops.** A material gap (an unverifiable source, an ineligible panel, a missing record) sets that case to `blocked: <specific gap>`, adds a research task to Standing State, and the run continues with other cases. A late-discovered earlier event, or any change to a completed record, waits for the user's authorization ([engine section 3](ENGINE.md)). New neutral evidence or a decisive new legal premise found in assembly returns that issue to new neutral and reconcile agents. If a source host is blocked, read the environment's network documentation and report the gap; do not substitute memory for a primary source.

## Annual close

Year scope only, once every admitted case of the year is final, blocked, withdrawn, or carried at the user's explicit instruction. Follow [engine section 9](ENGINE.md): check coverage, records, precedent treatment, chronology, and carryovers; apply dated roster changes through December 31 and no later; write `cycles/NNN/audit.md` for any cycle that just reached eighteen played; mark the year's case list `annually reconciled`; and set Standing State to the next period, with unresolved matters carried. The closing turn is a simulation turn and gets a report.

## Turn output and commits

Every run turn ends with the eight-section Form A report, displayed in the response and saved at `years/YYYY/output/YYYY-MM-DD-court-report.md` under the [render contract](RENDER_CONTRACT.md). Build the allowed-input packet in scratch from permitted sources only; it never contains `stone.md`, `history.md`, `commitments.md`, or `reconciled.md`. Refresh section 8 only for the interval since the previous report. When approvals are pending, put the approval request first and close with the report, which says only that Stone's position is awaited.

Commit after each stage group with a message naming the case and stage, following the session's attribution instructions. Push the working branch at the end of every turn and before waiting at a gate, because the container is ephemeral. Do not open a pull request unless asked.
