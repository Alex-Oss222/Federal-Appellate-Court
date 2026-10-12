# Framework migration record

This project adapts operating ideas from [Alex-Oss222/scotus-career](https://github.com/Alex-Oss222/scotus-career/tree/3fb9731ed440999aaec513d60ce5a899d4b7afc6), inspected at commit `3fb9731ed440999aaec513d60ce5a899d4b7afc6`. That repository is a design reference, not a legal authority or a source of continuing permissions for this project.

| Source | Retained principle | Appellate implementation |
|---|---|---|
| `AGENTS.md` | Stage-specific reading, user control, explicit corrections | Short root instructions, fresh scoped stages, and no inherited Stone fallback |
| `foundation/ENGINE.md` | Neutral modeling, historical reconciliation, assembly, chronology, supported joins | Second Circuit engine with historical Supreme Court authority and case-specific panel substitutions |
| `foundation/CASE_BRIEF_TEMPLATE.md` | Physically separable neutral, Stone, and comparator inputs | Separate files from intake; appellate jurisdiction, preservation, review standards, assignment, and remedies |
| `foundation/RENDER_CONTRACT.md` | Presentation projects a locked decision | Compact standalone render contract; no mandatory duplicate render-input layer |
| `foundation/COURT_COMPOSITION.md` | Dated, sourced institutional membership | Sourced Second Circuit roster, seniors, vacancies, and near-term changes; opening snapshot revised to January 1994 |
| `foundation/templates/STANDING_STATE_TEMPLATE.md` | Institutional state and carryover continuity | Living Standing State explicitly extended to rehearing, petitions, mandates, remands, and follow-up blockers |
| Holdings and standards templates | Distinguish controlling law from personal positions | One precedent index pointing to complete final records, alongside historical legal sources |
| Validation tools | Mechanical consistency checks do not adjudicate | Integrity checks during setup; no copied Supreme Court-dependent scripts or new runtime dependency |

## Existing appellate documents

- `CHARACTER SHEET (1994) - ALEX-LAMAR STONE-KHOURY.txt` became `stone/CHARACTER.md`, preserving the original content at import. Its appointment chronology was subsequently revised at the user's request as recorded below.
- `Master Jurisprudence Judge Stone, Court of Appeals.md` became `stone/JURISPRUDENCE.md` for archival storage only, with its content preserved. It is excluded from all engine reads, searches, imports, indexing, generation, validation, and rendering. This exclusion also covers existing engine-generated summaries, embeddings, digests, and other archival derivatives.
- The supplied age of 38 is unchanged. The previous wish for 40 remains a separate character-edit decision, not an implicit infrastructure correction.
- Stone's case-specific disposition and reasoning come only from the latest user-approved case brief `stone.md`. Choices covered by a genuine existing delegation are recorded there without duplicate approval. Ask for user input only when neither the approved brief nor a genuine existing delegation covers a required choice; neither the archive nor biography is a fallback.

## First full year revision

The user requested 1994 as Stone's first full year. The fictional timeline now places nomination in October 1993, confirmation in November, and commission plus required judicial oaths on December 1, 1993. Detailed play opens January 1, 1994. Meskill's June 30, 1993 senior-status date provides the existing vacancy; other judges retain their historical dates. Stone remains 38. The district-service dates, hearing reference to time in therapy, and opening biographical wording were adjusted for consistency. No pre-opening case or holding is created, and case-specific panel eligibility still requires verification.

## Excluded material

No Supreme Court simulation holdings, standards, case files, judicial roster, alternate appointments, future doctrinal roadmaps, prior approvals, standing voting fallback, or named-case exceptions were imported. Unrelated attached legal files were not used as an opening baseline. The large October Term workflow, duplicate state volumes, runtime splitting copies, and five-pass close are not required here.

No cases, panel votes, Supreme Court actions, or fictional historical sources were created during setup. Setup initially left the count and subject rotation open. The subsequently supplied [case-selection policy](CASE_SELECTION.md) establishes six groups with three historical cases each, for eighteen-case cycles that may span years. The original reference to fifteen was corrected to preserve the six-by-three distribution. No annual quota is imposed.

