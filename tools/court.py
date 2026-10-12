#!/usr/bin/env python3
"""Bookkeeping helper for the Second Circuit simulation (stdlib only).

  plan [year|session]            file-derived ledger and next stage for each case
  stage SLUG STAGE --dest DIR    copy exactly the files an isolated stage may read
  draw --docket D --panel "A;B"  reproducible ordering of seats for Stone's substitution
  check                          links, case lists, cycle counts, stage-file coherence

It writes nothing inside the repository and never decides legal meaning, votes, or
approvals (AGENTS.md, working rules). See foundation/RUN.md.
"""
import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISO = re.compile(r"\d{4}-\d{2}-\d{2}")
STATUSES = {"admitted", "prepared", "blocked", "played", "withdrawn"}
OPENING = "1994-07-21"
SKIP_DIRS = {".git", "node_modules"}


def read(path):
    return path.read_text(encoding="utf-8")


def field(text, label):
    """Value of a 'Label:' line in either '**Label:** v' or '- Label: v' form."""
    m = re.search(rf"^[ \t>*-]*{re.escape(label)}[ \t]*:?\**[ \t]*:?[ \t]*(.*)$", text, re.I | re.M)
    return m.group(1).strip() if m else ""


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
    neutral = c.folder / "neutral.md"
    if neutral.is_file():
        m = ISO.search(field(read(neutral), "Proposed event date"))
        if m:
            return m.group()
    m = ISO.search(c.stage_text)
    return m.group() if m else None


def final_events(folder):
    out = []
    for f in sorted((folder / "events").glob("*.md")):
        if field(read(f), "Status").lower().startswith("final"):
            out.append(f)
    return out


def approval(stone):
    """(approved, reference) from stone.md; a placeholder naming both states is unapproved."""
    if not stone.is_file():
        return False, ""
    text = read(stone)
    status = field(text, "Approval status").lower()
    ok = "user-approved" in status and "proposed" not in status
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
    if not (d / "stone.md").is_file():
        return "propose"
    if not (d / "commitments.md").is_file():
        return "neutral"
    if not (d / "reconciled.md").is_file():
        return "reconcile"
    if not final_events(d):
        return "assemble" if approval(d / "stone.md")[0] else "approve"
    if not list((d / "output").glob("*.md")):
        return "render"
    if c.status != "played" or c.departure.lower().startswith("not yet assessed"):
        return "finalize"
    return "done"


TERMINAL = {"done", "blocked", "withdrawn"}


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
    counts = slot_counts(cases)
    seen = sorted(set(counts) | {k[0] for k in table})
    for cyc in seen:
        have = counts.get(cyc, {g: 0 for g in range(1, 7)})
        if any(v < 3 for v in have.values()):
            return cyc, {g: 3 - v for g, v in have.items() if v < 3}
    nxt = f"{int(seen[-1]) + 1:03d}" if seen else "001"
    return nxt, {g: 3 for g in range(1, 7)}


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
    slots = ", ".join(f"group {g}: {n}" for g, n in gaps.items())
    print(f"Admission target: cycle {cyc}, unfilled {sum(gaps.values())} ({slots})")

    if args.scope == "year":
        print(f"Selection window: {ss['date']} through {year}-12-31")
        print("Selection: " + ("needed" if gaps else "not needed"))
    elif not open_cases:
        batch = ", ".join(str(g) for g in gaps)
        print(f"Session: no unfinished case; admit one batch, at most one case each for groups {batch}")

    print(f"Unfinished cases: {len(open_cases)}")
    waiting = []
    for i, c in enumerate(open_cases, 1):
        stage = next_stage(c)
        appr, _ = approval(c.folder / "stone.md")
        earlier = [e.slug for e in ordered(unfinished(cases)) if e is not c and (event_date(e) or "9999") < (event_date(c) or "9999")]
        hold = f" held-by={','.join(earlier)}" if stage in {"assemble", "render", "finalize"} and earlier else ""
        print(f" {i}. {event_date(c) or 'no-date':10} {c.slug} cycle={c.cycle} group={c.group} "
              f"stage={stage} approved={'yes' if appr else 'no'}{hold}")
        if (c.folder / "stone.md").is_file() and not appr:
            waiting.append(c.slug)
    if waiting:
        print("Awaiting Stone approval: " + ", ".join(waiting))
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


def cmd_stage(args):
    cases, _ = load_cases()
    match = [c for c in cases if c.slug == args.slug]
    if len(match) != 1:
        sys.exit(f"case '{args.slug}' not found in the case lists" if not match else f"slug '{args.slug}' is ambiguous")
    c = match[0]
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
    items = []
    for item in stage_plan(c, args.stage, args.event):
        if isinstance(item, tuple) and item[0] == "extract":
            items.append((item[1], item[2], True))
        elif isinstance(item, tuple) and item[0] == "optional":
            if item[1].is_file():
                items.append((item[1], item[1].name, False))
        else:
            items.append((item, item.name, False))
    missing = [str(s.relative_to(ROOT)) for s, _, _ in items if not s.is_file()]
    if missing:
        sys.exit("missing required input(s): " + ", ".join(missing))
    dest.mkdir(parents=True, exist_ok=True)
    for src, name, extract in items:
        if extract:
            (dest / name).write_text(public_decision(src), encoding="utf-8")
        else:
            shutil.copyfile(src, dest / name)
    output = {"neutral": "commitments.md", "reconcile": "reconciled.md", "assemble": "<YYYY-MM-DD>-<event>.md",
              "render": "<YYYY-MM-DD>-<event>.md", "compare": "comparison.md"}[args.stage]
    print(f"Staged in {dest}:")
    for _, name, _ in items:
        print(f"  {name}")
    print(f"The agent may write only: {output}")
    return 0


# ---------------------------------------------------------------- draw

def cmd_draw(args):
    seats = [s.strip() for s in args.panel.split(";") if s.strip()]
    if any("calabresi" in s.lower() for s in seats):
        print("Calabresi is on the historical panel: Stone takes that seat. No draw.")
        return 0
    docket = " ".join(args.docket.lower().split())
    key = lambda s: hashlib.sha256(f"{docket}|{' '.join(s.lower().split())}".encode()).hexdigest()
    print("Order (replace the first seat that can lawfully be replaced):")
    for i, s in enumerate(sorted(seats, key=key), 1):
        print(f"  {i}. {s}")
    return 0


# ---------------------------------------------------------------- check

def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        if not SKIP_DIRS & set(p.relative_to(ROOT).parts):
            yield p


def cmd_check(args):
    errors, warns = [], []
    for p in md_files():
        for m in re.finditer(r"\]\(([^)\s]+)\)", read(p)):
            t = m.group(1).split("#")[0]
            if t and not re.match(r"[a-z]+:", t) and not (p.parent / t).exists():
                errors.append(f"{p.relative_to(ROOT)}: broken link {m.group(1)}")

    ss = standing()
    cases, problems = load_cases()
    errors += problems

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
    d = sub.add_parser("draw")
    d.add_argument("--docket", required=True)
    d.add_argument("--panel", required=True, help="semicolon-separated historical panel")
    d.set_defaults(fn=cmd_draw)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
