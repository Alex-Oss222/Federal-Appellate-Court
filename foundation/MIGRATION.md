# Framework migration record

This project adapts operating ideas from [Alex-Oss222/scotus-career](https://github.com/Alex-Oss222/scotus-career/tree/3fb9731ed440999aaec513d60ce5a899d4b7afc6), inspected at commit `3fb9731ed440999aaec513d60ce5a899d4b7afc6`. That repository is a design reference, not a legal authority or a source of continuing permissions for this project.

| Source | Retained principle | Appellate implementation |
|---|---|---|
| `AGENTS.md` | Stage-specific reading, user control, explicit corrections | Short root instructions, fresh scoped stages, and no inherited Stone fallback |
| `foundation/ENGINE.md` | Neutral modeling, historical reconciliation, assembly, chronology, supported joins | Second Circuit engine with historical Supreme Court authority and case-specific panel substitutions |
| `foundation/CASE_BRIEF_TEMPLATE.md` | Physically separable neutral, Stone, and comparator inputs | Separate files from intake; appellate jurisdiction, preservation, review standards, assignment, and remedies |
| `foundation/RENDER_CONTRACT.md` | Presentation projects a locked decision | Compact standalone render contract; no mandatory duplicate render-input layer |
| `foundation/COURT_COMPOSITION.md` | Dated, sourced institutional membership | Independently researched July 1994 Second Circuit roster, seniors, vacancies, and near-term changes |
| `foundation/templates/STANDING_STATE_TEMPLATE.md` | Institutional state and carryover continuity | Living Standing State explicitly extended to rehearing, petitions, mandates, remands, and follow-up blockers |
| Holdings and standards templates | Distinguish controlling law from personal positions | One precedent index pointing to complete final records, alongside historical legal sources |
| Validation tools | Mechanical consistency checks do not adjudicate | Integrity checks during setup; no copied Supreme Court-dependent scripts or new runtime dependency |

## Existing appellate documents

- `CHARACTER SHEET (1994) - ALEX-LAMAR STONE-KHOURY.txt` becomes `stone/CHARACTER.md`, preserving the original content.
- `Master Jurisprudence Judge Stone, Court of Appeals.md` becomes `stone/JURISPRUDENCE.md`, preserving the original content.
- The supplied age of 38 is unchanged. The previous wish for 40 remains a separate character-edit decision, not an implicit infrastructure correction.
- References to later Supreme Court service in the personal jurisprudence do not override this project's historical Supreme Court setting.

## Excluded material

No Supreme Court simulation holdings, standards, case files, judicial roster, alternate appointments, future doctrinal roadmaps, prior approvals, standing voting fallback, or named-case exceptions were imported. Unrelated attached legal files were not used as an opening baseline. The large October Term workflow, duplicate state volumes, runtime splitting copies, and five-pass close are not required here.

No cases, panel votes, Supreme Court actions, or fictional historical sources were created during setup. Setup initially left the count and subject rotation open. The subsequently supplied [case-selection policy](CASE_SELECTION.md) establishes six groups with three historical cases each, for eighteen-case cycles that may span years. The original reference to fifteen was corrected to preserve the six-by-three distribution. No annual quota is imposed.
