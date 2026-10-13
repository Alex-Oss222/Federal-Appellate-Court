#!/usr/bin/env python3
"""Bookkeeping helper for the Second Circuit simulation (stdlib only).

  plan [year|session]            file-derived ledger, next stage, and the task sentence for each case
  stage SLUG STAGE --dest DIR    copy exactly the files an isolated stage may read
  accept SLUG STAGE --dest DIR   check a finished stage folder and file its single output in the case folder
  draw --case SLUG               reproducible ordering of the historical seats for Stone's substitution
  draw --docket D --panel "A;B"  the same ordering from typed inputs
  author --case SLUG --eligible "A;B"
                                 reproducible ordering of eligible majority judges for opinion authorship
  check                          links, case lists, cycle counts, stage-file coherence, panel substitution

Only `accept` writes inside the repository, and it writes one expected output file and nothing
else. The script never decides legal meaning, votes, or approvals (AGENTS.md, working rules).
See foundation/RUN.md.
"""
import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISO = re.compile(r"\d{4}-\d{2}-\d{2}")
STATUSES = {"admitted", "prepared", "blocked", "played", "withdrawn"}
OPENING = "1994-01-01"
DOC_ROOTS = ["AGENTS.md", "README.md", "foundation", "state", "years", ".claude"]


def read(path):
    return path.read_text(encoding="utf-8")


def field(text, label):
    """Value of '**Label:** v' (anywhere on a line, ending at the next bold label) or of a '- Label: v' line."""
    m = re.search(rf"\*\*{re.escape(label)}:\*\*[ \t]*(.*?)(?=[ \t]+\*\*[A-Z][^*\n]*?:\*\*|$)", text, re.I | re.M)
    if m:
        return m.group(1).strip()
    m = re.search(rf"^[ \t>*-]*{re.escape(label)}[ \t]*:?\**[ \t]*:?[ \t]*(.*)$", text, re.I | re.M)
    return m.group(1).strip() if m else ""


MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"


def parse_date(s):
    """First ISO date or 'Month D, YYYY' in s, as ISO; else None."""
    m = ISO.search(s or "")
    if m:
        return m.group()
    m = re.search(rf"({MONTHS})\s+(\d{{1,2}}),\s+(\d{{4}})", s or "")
    return datetime.strptime(" ".join(m.groups()), "%B %d %Y").strftime("%Y-%m-%d") if m else None


# ---------------------------------------------------------------- state

def standing():
    text = read(ROOT / "state/STANDING_STATE.md")
    d = re.search(r"\*\*Current simulation date:\*\*\s*(\d{4}-\d{2}-\d{2})", text)
    p = re.search(r"\*\*Current bookkeeping period:\*\*\s*(\d{4}-\d{2}-\d{2}) through (\d{4}-\d{2}-\d{2})", text)
    if not d or not p:
        sys.exit("Standing State: current date or bookkeeping period not found")
    table = {}
    for m in re.finditer(r"^\|\s*(\d{3})\s*\|\s*(\d)\.[^|]*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|", text, re.M):
        table[(m[1], int(m[2]))] = tuple(int(m[i]) for i in range(3, 7))
    last = field(text, "Last completed simulation event")
    return {"date": d[1], "period": (p[1], p[2]), "table": table, "last": last}


@dataclass
class Case:
    cycle: str
    name: str
    docket: str
    stage_text: str
    group: int
    status: str
    departure: str
    list_file: Path
    folder: Path
    row: int

    @property
    def slug(self):
        return self.folder.name

    @property
    def year(self):
        return self.list_file.parent.name


def load_cases():
    cases, problems = [], []
    for lst in sorted((ROOT / "years").glob("*/case-list.md")):
        for n, line in enumerate(read(lst).splitlines(), 1):
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not re.fullmatch(r"\d{3}", cells[0]):
                continue
            where = f"{lst.relative_to(ROOT)}:{n}"
            if len(cells) != 11:
                problems.append(f"{where}: {len(cells)} columns, expected 11")
                continue
            link = re.search(r"\]\(([^)]+)\)", cells[1])
            g = re.match(r"\s*(\d)", cells[5])
            status = (re.match(r"[a-z]+", cells[9].lower()) or [""])[0]
            if not link or not g:
                problems.append(f"{where}: case name must link to its folder and the group must start with its number")
                continue
            folder = (lst.parent / link.group(1).split("#")[0]).resolve()
            if folder.suffix:
                folder = folder.parent
            cases.append(Case(cells[0], cells[1], cells[3], cells[4], int(g[1]), status, cells[10], lst, folder, n))
            if status not in STATUSES:
                problems.append(f"{where}: unknown simulation status '{cells[9]}'")
    return cases, problems


def event_date(c):
    """The case's proposed event date: neutral.md first, then the case-list stage cell."""
    neutral = c.folder / "neutral.md"
    if neutral.is_file():
        text = read(neutral)
        for label in ("Proposed event date", "Proposed event", "Proposed operative event"):
            d = parse_date(field(text, label))
            if d:
                return d
    m = re.search(r"proposed (?:decision |operative )?event (\d{4}-\d{2}-\d{2})", c.stage_text, re.I)
    if m:
        return m.group(1)
    dates = ISO.findall(c.stage_text)
    return dates[-1] if dates else None


def final_events(folder):
    out = []
    for f in sorted((folder / "events").glob("*.md")):
        if field(read(f), "Status").lower().startswith("final"):
            out.append(f)
    return out


def brief_state(folder):
    """missing, proposed, or approved: the user's case-specific brief (stone.md)."""
    stone = folder / "stone.md"
    if not stone.is_file():
        return "missing"
    return "approved" if approval(stone)[0] else "proposed"


def approval(stone):
    """(approved, reference) from stone.md. Reads 'Approval status' or the brief's own 'Status' field.

    A status that says proposed, pending, or "not ... approved" is unapproved; only a plain
    approved / user-approved status counts.
    """
    if not stone.is_file():
        return False, ""
    text = read(stone)
    status = (field(text, "Approval status") or field(text, "Status")).lower()
    ok = bool(re.search(r"\b(?:user-)?approved\b", status)) and not re.search(r"\b(?:not|proposed|pending|unapproved|awaiting)\b", status)
    return ok, field(text, "Approval reference")


def committed(path):
    """False when git reports the file untracked or modified; True when clean or when git cannot say."""
    r = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain", "--", str(path)], capture_output=True, text=True)
    return r.returncode != 0 or not r.stdout.strip()


def next_stage(c):
    d = c.folder
    if c.status == "withdrawn":
        return "withdrawn"
    if c.status == "blocked":
        return "blocked"
    if not (d / "neutral.md").is_file() or not (d / "history.md").is_file():
        return "prepare"
    if not (d / "commitments.md").is_file():
        return "neutral"
    if not (d / "reconciled.md").is_file():
        return "reconcile"
    if not final_events(d):
        return "assemble" if brief_state(d) == "approved" else "brief"
    if not list((d / "output").glob("*.md")):
        return "render"
    if not (d / "comparison.md").is_file():
        return "compare"
    if c.status != "played" or c.departure.lower().startswith("not yet assessed"):
        return "finalize"
    return "done"


TERMINAL = {"done", "blocked", "withdrawn"}

TASKS = {
    "prepare": "Prepare {slug}",
    "neutral": "Neutral stage: {slug}",
    "reconcile": "Reconcile stage: {slug}",
    "assemble": "Assemble stage: {slug}",
    "render": "Render stage: {slug}",
    "compare": "Compare stage: {slug}",
    "finalize": "Finalize: {slug}",
}


def unfinished(cases):
    return [c for c in cases if next_stage(c) not in TERMINAL]


def ordered(cases):
    return sorted(cases, key=lambda c: (event_date(c) or "9999-99-99", c.list_file.parent.name, c.row))


def slot_counts(cases):
    """{cycle: {group: admitted}} counting every row except withdrawn."""
    out = {}
    for c in cases:
        if c.status != "withdrawn":
            out.setdefault(c.cycle, {g: 0 for g in range(1, 7)})[c.group] += 1
    return out


def target_cycle(cases, table):
    """(cycle, unfilled-by-group) for new admissions, or (None, {}) when none is due.

    The lowest cycle with an unfilled slot is the target. A new cycle opens only when every
    existing cycle is fully played (or none exists); a fully admitted but unplayed cycle is not
    a reason to select more cases.
    """
    counts = slot_counts(cases)
    seen = sorted(set(counts) | {k[0] for k in table})
    for cyc in seen:
        have = counts.get(cyc, {g: 0 for g in range(1, 7)})
        if any(v < 3 for v in have.values()):
            return cyc, {g: 3 - v for g, v in have.items() if v < 3}

    def played(cyc, g):
        return sum(1 for c in cases if c.cycle == cyc and c.group == g and c.status == "played")

    if all(played(cyc, g) >= 3 for cyc in seen for g in range(1, 7)):
        nxt = f"{int(seen[-1]) + 1:03d}" if seen else "001"
        return nxt, {g: 3 for g in range(1, 7)}
    return None, {}


# ---------------------------------------------------------------- plan

def cmd_plan(args):
    ss = standing()
    cases, problems = load_cases()
    year = ss["date"][:4]
    print(f"Simulation date {ss['date']} | year {year} | period {ss['period'][0]} to {ss['period'][1]}")
    print(f"Scope: {args.scope}")
    for p in problems:
        print(f"PROBLEM {p}")
    open_cases = ordered(unfinished(cases))
    cyc, gaps = target_cycle(cases, ss["table"])
    if cyc is None:
        print("Admission target: none; every existing cycle is fully admitted and awaits play")
    else:
        slots = ", ".join(f"group {g}: {n}" for g, n in gaps.items())
        print(f"Admission target: cycle {cyc}, unfilled {sum(gaps.values())} ({slots})")

    if args.scope == "year":
        print(f"Selection window: {ss['date']} through {year}-12-31")
        print("Selection: " + ("needed" if gaps else "not needed"))
    elif not open_cases:
        batch = ", ".join(str(g) for g in gaps)
        print(f"Session: no unfinished case; admit one batch, at most one case each for groups {batch}")

    print(f"Unfinished cases: {len(open_cases)}")
    missing, proposed = [], []
    for i, c in enumerate(open_cases, 1):
        stage = next_stage(c)
        brief = brief_state(c.folder)
        earlier = [e.slug for e in ordered(unfinished(cases)) if e is not c and (event_date(e) or "9999") < (event_date(c) or "9999")]
        hold = f" held-by={','.join(earlier)}" if stage in {"assemble", "render", "compare", "finalize"} and earlier else ""
        task = TASKS.get(stage, "").format(slug=c.slug)
        print(f" {i}. {event_date(c) or 'no-date':10} {c.slug} cycle={c.cycle} group={c.group} "
              f"stage={stage} brief={brief}{hold}" + (f'\n      task: "{task}"' if task else ""))
        if brief == "missing":
            missing.append(c.slug)
        elif brief == "proposed":
            proposed.append(c.slug)
    if missing:
        print("Needs the user's Stone brief (stone.md): " + ", ".join(missing))
    if proposed:
        print("Awaiting the user's approval of stone.md: " + ", ".join(proposed))
    if args.scope == "year":
        if open_cases:
            print("Annual close: not yet; unfinished cases remain")
        else:
            print("Annual close: due" + (" after selection" if gaps else ""))
    return 0


# ---------------------------------------------------------------- stage

def public_decision(path):
    text = read(path)
    m = re.search(r"^## Public decision[ \t]*$.*?(?=^## |\Z)", text, re.M | re.S)
    if not m:
        sys.exit(f"{path.relative_to(ROOT)}: no '## Public decision' section")
    return m.group().rstrip() + "\n"


def stage_plan(c, stage, event):
    d, f = c.folder, (lambda p: ROOT / p)
    engine = f("foundation/ENGINE.md")
    pub = None
    if stage in ("render", "compare"):
        finals = final_events(d)
        if event:
            ev = Path(event).resolve()
        elif len(finals) == 1:
            ev = finals[0]
        else:
            sys.exit("need exactly one final event record, or pass --event FILE")
        pub = ("extract", ev, "public-decision.md")
    plans = {
        "neutral": [d / "neutral.md", engine],
        "reconcile": [d / "neutral.md", d / "commitments.md", d / "history.md", engine],
        "assemble": [d / "neutral.md", d / "reconciled.md", d / "stone.md", engine,
                     f("foundation/templates/DECISION_RECORD.md"), f("state/PRECEDENT.md")],
        "render": [pub, f("foundation/RENDER_CONTRACT.md"), f("foundation/templates/RENDER.md")],
        "compare": [pub, d / "history.md", ("optional", d / "historical-follow-up.md"), engine],
    }
    return plans[stage]


def find_case(slug):
    cases, _ = load_cases()
    match = [c for c in cases if c.slug == slug]
    if len(match) != 1:
        sys.exit(f"case '{slug}' not found in the case lists" if not match else f"slug '{slug}' is ambiguous")
    return match[0]


def stage_items(c, stage, event=None):
    """[(source path, staged name, is_extract)] for the files an isolated stage may read."""
    items = []
    for item in stage_plan(c, stage, event):
        if isinstance(item, tuple) and item[0] == "extract":
            items.append((item[1], item[2], True))
        elif isinstance(item, tuple) and item[0] == "optional":
            if item[1].is_file():
                items.append((item[1], item[1].name, False))
        else:
            items.append((item, item.name, False))
    return items


OUTPUT_NAME = {"neutral": "commitments.md", "reconcile": "reconciled.md", "assemble": "<YYYY-MM-DD>-<event>.md",
               "render": "<YYYY-MM-DD>-<event>.md", "compare": "comparison.md"}


def cmd_stage(args):
    c = find_case(args.slug)
    if args.stage == "assemble" and not approval(c.folder / "stone.md")[0]:
        sys.exit("assemble needs a user-approved stone.md; Stone's position is not approved")
    frozen = {"reconcile": "commitments.md", "assemble": "reconciled.md"}.get(args.stage)
    if frozen and (c.folder / frozen).is_file() and not committed(c.folder / frozen):
        sys.exit(f"{frozen} is not committed; commit the frozen stage before staging {args.stage}")
    dest = Path(args.dest).resolve()
    if ROOT in dest.parents or dest == ROOT:
        sys.exit("--dest must be outside the repository")
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"{dest} is not empty")
    items = stage_items(c, args.stage, args.event)
    missing = [str(s.relative_to(ROOT)) for s, _, _ in items if not s.is_file()]
    if missing:
        sys.exit("missing required input(s): " + ", ".join(missing))
    dest.mkdir(parents=True, exist_ok=True)
    for src, name, extract in items:
        if extract:
            (dest / name).write_text(public_decision(src), encoding="utf-8")
        else:
            shutil.copyfile(src, dest / name)
    print(f"Staged in {dest}:")
    for _, name, _ in items:
        print(f"  {name}")
    print(f"The agent may write only: {OUTPUT_NAME[args.stage]}")
    return 0


STAGE_TITLE = {"neutral": "Neutral modeling", "reconcile": "Historical reconciliation", "assemble": "Assembly",
               "render": "Render", "compare": "Comparison"}


def git_head():
    r = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip() or "not established"


def cmd_accept(args):
    """File the single output of a finished isolated stage; refuse anything unexpected."""
    c = find_case(args.slug)
    dest = Path(args.dest).resolve()
    if not dest.is_dir():
        sys.exit(f"{dest} is not a directory")
    items = stage_items(c, args.stage, args.event)
    staged = {name for _, name, _ in items}
    if any(p.is_dir() for p in dest.iterdir()):
        sys.exit("the stage folder contains a subdirectory; only the staged inputs and one output file are allowed")
    present = {p.name for p in dest.iterdir()}
    for src, name, extract in items:
        if name not in present:
            sys.exit(f"staged input {name} is missing from the stage folder")
        if not extract and (dest / name).read_bytes() != src.read_bytes():
            sys.exit(f"staged input {name} was modified")
    new = sorted(present - staged)
    if args.stage in ("assemble", "render"):
        ok = len(new) == 1 and re.fullmatch(r"\d{4}-\d{2}-\d{2}-[\w.-]+\.md", new[0])
    else:
        ok = new == [OUTPUT_NAME[args.stage]]
    if not ok:
        sys.exit(f"expected exactly one new file ({OUTPUT_NAME[args.stage]}); found: {', '.join(new) or 'none'}")
    out_name = new[0]
    folder = {"assemble": "events", "render": "output"}.get(args.stage)
    target = (c.folder / folder / out_name) if folder else (c.folder / out_name)
    if target.exists() and not args.replace:
        sys.exit(f"{target.relative_to(ROOT)} already exists; pass --replace only for a user-authorized correction")
    text = read(dest / out_name)
    mode = args.mode or "a fresh Codex cloud task started for this stage"
    who = f"{mode} ({args.agent})" if args.agent else mode
    inputs = ", ".join(sorted(staged))
    today = datetime.now().strftime("%Y-%m-%d")
    caveat = "A fresh context with an allowed-file list, not an operating-system sandbox."
    if args.stage in ("neutral", "reconcile"):
        if "## Execution record" not in text:
            text = text.rstrip() + (f"\n\n---\n\n## Execution record\n\n- Stage: {STAGE_TITLE[args.stage]} (ENGINE.md section 6).\n"
                                   f"- Execution: {who}. {caveat}\n- Permitted inputs: {inputs}.\n"
                                   f"- Input commit: {git_head()}.\n- Date run: {today}.\n")
    elif args.stage == "assemble":
        line = (f"- **Execution record:** Assembly run by {who}, working only with {inputs}; input commit {git_head()}; "
                f"run {today}. {caveat} commitments.md and reconciled.md were each committed alone before this stage; "
                "commitments.md was not staged to it.")
        text, n = re.subn(r"^- \*\*Execution record:\*\*.*$", lambda m: line, text, count=1, flags=re.M)
        if n != 1:
            sys.exit("the assembled record has no '- **Execution record:**' line to complete")
        if not re.search(r"^- \*\*Status:\*\*\s*(final|draft)", text, re.M):
            sys.exit("the assembled record has no '- **Status:** final' or 'draft, blocked' line")
    elif args.stage == "render":
        finals = final_events(c.folder)
        if len(finals) != 1:
            sys.exit("render needs exactly one final event record to link")
        ref = f"[years/{c.year}/cases/{c.slug}/events/{finals[0].name}](../events/{finals[0].name})"
        text, n = re.subn(r"^(Final record:).*$", lambda m: f"{m.group(1)} {ref}", text, count=1, flags=re.M)
        if n != 1:
            sys.exit("the render has no 'Final record:' line")
    target.parent.mkdir(exist_ok=True)
    target.write_text(text, encoding="utf-8")
    rel = target.relative_to(ROOT)
    print(f"Filed {rel}")
    print(f"Commit it alone: git add {rel} && git commit -m \"{c.slug}: {args.stage} stage\"")
    return 0


# ---------------------------------------------------------------- draw

def seat_key(name):
    """Normalized form of a judge's name for hashing: lower case, single spaces, no trailing period."""
    return " ".join(name.lower().split()).rstrip(".")


def packet_panel(c):
    """(docket, [(name, role)]) read from the case's neutral.md 'Historical panel' and 'Docket or citation' lines."""
    path = c.folder / "neutral.md"
    if not path.is_file():
        sys.exit(f"{c.slug}: neutral.md not found")
    text = read(path)
    m = re.search(r"^\*\*Historical panel:\*\*\s*(.*?)\s*Source:", text, re.M)
    d = re.search(r"^\*\*Docket or citation:\*\*\s*([^;\n]+)", text, re.M)
    if not m or not d:
        sys.exit(f"{c.slug}: neutral.md needs 'Historical panel' (ending before 'Source:') and 'Docket or citation' lines")
    seats = []
    for part in m.group(1).split(";"):
        part = re.sub(r"\)\.$", ")", part.strip())
        if part:
            role = re.search(r"\(([^)]*)\)\s*$", part)
            seats.append((re.sub(r"\s*\([^)]*\)\s*$", "", part).strip(), role.group(1) if role else ""))
    return d.group(1).strip(), seats


def draw_order(docket, names, salt=""):
    d = " ".join(docket.lower().split())
    return sorted(names, key=lambda s: hashlib.sha256(f"{d}|{salt}{seat_key(s)}".encode()).hexdigest())


def cmd_draw(args):
    if args.case:
        docket, seats = packet_panel(find_case(args.case))
        names = [n for n, _ in seats]
    elif args.docket and args.panel:
        docket, names = args.docket, [s.strip() for s in args.panel.split(";") if s.strip()]
    else:
        sys.exit("give --case SLUG, or both --docket and --panel")
    if any("calabresi" in s.lower() for s in names):
        print("Calabresi is on the historical panel: Stone takes that seat. No draw.")
        return 0
    print(f"Docket key: {' '.join(docket.lower().split())}")
    print("Order (Stone replaces the first seat that can lawfully be replaced; a seat skipped for a reason unrelated to "
          "votes or authorship is recorded):")
    for i, s in enumerate(draw_order(docket, names), 1):
        print(f"  {i}. {s}")
    return 0


def cmd_author(args):
    docket, _ = packet_panel(find_case(args.case))
    names = [s.strip() for s in args.eligible.split(";") if s.strip()]
    if not names:
        sys.exit("--eligible needs at least one judge")
    print("Authorship draw (equal chance among the eligible majority judges; the first name is the drawn author):")
    for i, s in enumerate(draw_order(docket, names, "author|"), 1):
        print(f"  {i}. {s}")
    return 0


# ---------------------------------------------------------------- check

def md_files():
    """Explicit allowlist of roots. stone/ is never opened: it holds biography and the archived jurisprudence."""
    for root in DOC_ROOTS:
        base = ROOT / root
        yield from ([base] if base.is_file() else sorted(base.rglob("*.md")))


def cmd_check(args):
    errors, warns = [], []
    ss = standing()
    cases, problems = load_cases()
    errors += problems
    # an admitted case has no folder until the prepare stage creates it, so its case-list link is not broken
    pending = {c.folder for c in cases if c.status == "admitted"}
    for p in md_files():
        for m in re.finditer(r"\]\(([^)\s]+)\)", read(p)):
            t = m.group(1).split("#")[0]
            if t and not re.match(r"[a-z]+:", t) and not (p.parent / t).exists() and (p.parent / t).resolve() not in pending:
                errors.append(f"{p.relative_to(ROOT)}: broken link {m.group(1)}")

    seen = {}
    for c in cases:
        where = f"{c.list_file.relative_to(ROOT)}:{c.row}"
        if c.folder.parent.name != "cases" or c.folder.parent.parent != c.list_file.parent:
            errors.append(f"{where}: folder must be years/{c.year}/cases/<slug>")
        if c.status not in {"admitted", "withdrawn"} and not c.folder.is_dir():
            errors.append(f"{where}: status '{c.status}' but folder {c.slug} does not exist")
        for key in (("slug", c.slug), ("docket", c.docket.lower())):
            if key in seen:
                errors.append(f"{where}: duplicate {key[0]} also at {seen[key]}")
            seen[key] = where
        d = c.folder
        has = lambda n: (d / n).is_file()
        finals = final_events(d)
        if has("commitments.md") and not has("neutral.md"):
            errors.append(f"{c.slug}: commitments.md without neutral.md")
        if has("reconciled.md") and not has("commitments.md"):
            errors.append(f"{c.slug}: reconciled.md without commitments.md")
        if finals and not has("reconciled.md"):
            errors.append(f"{c.slug}: final record without reconciled.md")
        if finals:
            ok, ref = approval(d / "stone.md")
            if not ok or not ref or "not yet" in ref.lower():
                errors.append(f"{c.slug}: final record without a user-approved stone.md and approval reference")
            if (d / "events").is_dir() and any(ISO.match(f.name) and ISO.match(f.name).group() > ss["date"] for f in finals):
                errors.append(f"{c.slug}: final record dated after the simulation date {ss['date']}")
            if c.status not in {"played"}:
                warns.append(f"{c.slug}: final record exists but status is '{c.status}' (finalize pending)")
        elif c.status == "played":
            errors.append(f"{c.slug}: status played without a final record")
        if not event_date(c) and c.status != "withdrawn":
            errors.append(f"{c.slug}: no ISO event date in neutral.md or the case-list row")
        if has("neutral.md") and c.status != "withdrawn":
            ntext = read(d / "neutral.md")
            rep = re.search(r"^\*\*Member Stone replaces:\*\*\s*(.*)$", ntext, re.M)
            docket, seats = packet_panel(c) if rep else (None, [])
            if rep and not any("calabresi" in n.lower() for n, _ in seats):
                first = draw_order(docket, [n for n, _ in seats])[0]
                declared = re.split(r"\.\s+Declared", rep.group(1))[0]
                if seat_key(declared) != seat_key(first) and not re.search(r"^\*\*Seat skipped:\*\*", ntext, re.M):
                    errors.append(f"{c.slug}: Stone replaces '{declared}' but the draw order starts with '{first}'; "
                                  "follow the draw or record a '**Seat skipped:**' reason")

    for lst in sorted((ROOT / "years").glob("*/case-list.md")):
        dates = [event_date(c) or "" for c in cases if c.list_file == lst]
        if dates != sorted(dates):
            warns.append(f"{lst.relative_to(ROOT)}: rows are not in chronological entry order")

    counts = slot_counts(cases)
    played = {}
    for c in cases:
        if c.status == "played":
            played[(c.cycle, c.group)] = played.get((c.cycle, c.group), 0) + 1
    for cyc in sorted(set(counts) | {k[0] for k in ss["table"]}):
        for g in range(1, 7):
            adm = counts.get(cyc, {}).get(g, 0)
            pl = played.get((cyc, g), 0)
            if adm > 3:
                errors.append(f"cycle {cyc} group {g}: {adm} admitted, limit 3")
            want = (3, adm, pl, 3 - adm)
            got = ss["table"].get((cyc, g))
            if got != want:
                errors.append(f"Standing State cycle {cyc} group {g}: has {got}, case lists give {want} (target, admitted, played, unfilled)")

    all_finals = [f for c in cases for f in final_events(c.folder)]
    if all_finals and ss["last"].lower().startswith("none"):
        errors.append("Standing State says no completed event but final records exist")
    if not all_finals and not ss["last"].lower().startswith("none"):
        errors.append("Standing State names a completed event but no final record exists")
    if ss["date"] < OPENING:
        errors.append(f"simulation date {ss['date']} precedes the opening date {OPENING}")

    for w in warns:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"{len(errors)} error(s), {len(warns)} warning(s). Not checked mechanically: join arithmetic, panel eligibility, "
          "authority status, legal meaning.")
    return 1 if errors else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("scope", nargs="?", choices=["year", "session"], default="year")
    p.set_defaults(fn=cmd_plan)
    s = sub.add_parser("stage")
    s.add_argument("slug")
    s.add_argument("stage", choices=["neutral", "reconcile", "assemble", "render", "compare"])
    s.add_argument("--dest", required=True)
    s.add_argument("--event")
    s.set_defaults(fn=cmd_stage)
    a = sub.add_parser("accept")
    a.add_argument("slug")
    a.add_argument("stage", choices=["neutral", "reconcile", "assemble", "render", "compare"])
    a.add_argument("--dest", required=True)
    a.add_argument("--event")
    a.add_argument("--mode", help="how the stage ran, recorded in the execution record")
    a.add_argument("--agent", help="task or agent identifier, if exposed")
    a.add_argument("--replace", action="store_true", help="overwrite an existing output (user-authorized correction only)")
    a.set_defaults(fn=cmd_accept)
    d = sub.add_parser("draw")
    d.add_argument("--case", help="case slug: reads the docket and historical panel from its neutral.md")
    d.add_argument("--docket")
    d.add_argument("--panel", help="semicolon-separated historical panel")
    d.set_defaults(fn=cmd_draw)
    au = sub.add_parser("author")
    au.add_argument("--case", required=True)
    au.add_argument("--eligible", required=True, help="semicolon-separated majority judges who join every proposition")
    au.set_defaults(fn=cmd_author)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
