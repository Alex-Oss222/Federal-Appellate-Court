---
name: run-session
description: Run the Second Circuit simulation for the current session, meaning the admitted unfinished cases, or one new batch if none is open. Use only when the user says "run this session" or "run the session", or invokes /run-session.
argument-hint: "[optional narrowing, or an explicit delegation of Stone's approval]"
---

Run the **session** scope of [the runbook](../../../foundation/RUN.md) for this repository.

1. Read `foundation/RUN.md` and `AGENTS.md`, then follow the runbook from "Before every run".
2. A session covers the admitted, unfinished cases in event-date order. If none is open, admit one batch as the runbook's Selection section describes. Annual close is not part of a session.
3. This command starts the run; it does not approve Stone's positions. Stop at each `stone.md` that is not user-approved unless the arguments below delegate approval in the user's own words.
4. End the turn with the Form A court report.

Arguments: $ARGUMENTS
