#!/usr/bin/env python3
"""Mechanical gates for idl-design COURSE.md + DIAGNOSTIC.md."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    data: dict[str, str] = {}
    stack: list[tuple[int, str]] = []
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        m = re.match(r"^(\s*)([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if not m:
            continue
        indent, key, value = len(m.group(1)), m.group(2), m.group(3).strip()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        full = ".".join([x[1] for x in stack] + [key])
        if value:
            data[full] = value.strip('"\'')
        else:
            stack.append((indent, key))
    return data


def section(text: str, heading: str) -> str:
    m = re.search(rf"(?mi)^##\s+{re.escape(heading)}\s*$", text)
    if not m:
        return ""
    tail = text[m.end():]
    n = re.search(r"(?m)^##\s+", tail)
    return tail[: n.start()] if n else tail


def table_rows(block: str) -> tuple[list[str], list[dict[str, str]]]:
    lines = [line.strip() for line in block.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return [], []
    cells = lambda line: [c.strip() for c in line.strip("|").split("|")]
    headers = cells(lines[0])
    rows: list[dict[str, str]] = []
    for line in lines[1:]:
        vals = cells(line)
        if vals and all(re.fullmatch(r":?-{3,}:?", v) for v in vals):
            continue
        if len(vals) == len(headers):
            rows.append(dict(zip(headers, vals)))
    return headers, rows


def col(row: dict[str, str], prefix: str) -> str:
    for key, value in row.items():
        if key.lower().startswith(prefix.lower()):
            return value.strip()
    return ""


def pause_targets(cell: str) -> list[tuple[str, str]]:
    """Accept misconception:id, misconception(id), or misconception[id]."""
    return [
        (kind.lower(), rid.lower())
        for kind, rid in re.findall(
            r"\b(misconception|completion|prediction)\s*(?::|\(|\[)\s*([a-z0-9][a-z0-9-]*)",
            cell,
            flags=re.I,
        )
    ]


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: validate_idl_design.py COURSE.md DIAGNOSTIC.md")
        return 2

    course_path, diagnostic_path = map(Path, sys.argv[1:])
    failures: list[str] = []
    warnings: list[str] = []
    passes: list[str] = []

    def gate(condition: bool, label: str, detail: str) -> None:
        (passes if condition else failures).append(f"{label}: {detail}")

    if not course_path.is_file() or not diagnostic_path.is_file():
        if not course_path.is_file():
            failures.append(f"Files: missing {course_path}")
        if not diagnostic_path.is_file():
            failures.append(f"Files: missing {diagnostic_path}")
        return report(passes, warnings, failures)

    course = course_path.read_text(encoding="utf-8")
    diagnostic = diagnostic_path.read_text(encoding="utf-8")
    cfm, dfm = frontmatter(course), frontmatter(diagnostic)

    gate(bool(cfm), "Course frontmatter", "valid opening/closing delimiters")
    gate(bool(dfm), "Diagnostic frontmatter", "valid opening/closing delimiters")
    slug = cfm.get("course_id", "")
    gate(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)), "Course slug", slug or "missing")
    gate(dfm.get("course") == slug, "Course linkage", f"diagnostic course={dfm.get('course', 'missing')}")
    gate(cfm.get("status") in {"draft", "approved"}, "Status", cfm.get("status", "missing"))
    gate(cfm.get("grounding") in {"ok", "weak"}, "Grounding field", cfm.get("grounding", "missing"))

    audience = [cfm.get(f"audience.{k}", "") for k in ("background", "assumed_prior", "goal")]
    gate(all(audience), "Audience schema", "background, assumed_prior, and goal present")
    identity_markers = re.compile(r"\b(my name is|works? at|employed by|@[A-Za-z0-9_]+)\b", re.I)
    gate(not any(identity_markers.search(v) for v in audience), "Audience role", "no obvious personal identity marker")

    registry_block = section(course, "3. Registry — misconceptions and principles")
    if not registry_block:
        registry_block = section(course, "3. Registry - misconceptions and principles")
    _, registry = table_rows(registry_block)
    gate(bool(registry), "Registry", f"{len(registry)} rows parsed")

    by_id: dict[str, dict[str, str]] = {}
    grounded = 0
    for i, row in enumerate(registry, 1):
        rid = col(row, "registry_id").strip("`").lower()
        kind = col(row, "kind").lower()
        tier = col(row, "tier").strip()
        if rid:
            by_id[rid] = row
        if kind == "misconception" and tier in {"1", "2"}:
            grounded += 1
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", rid):
            failures.append(f"Registry row {i}: invalid registry_id {rid!r}")
        if kind not in {"misconception", "principle"}:
            failures.append(f"Registry {rid or i}: kind must be misconception or principle")
        if kind == "misconception" and tier not in {"1", "2", "4"}:
            failures.append(f"Registry {rid or i}: misconception tier must be 1, 2, or 4")
        if tier == "3":
            failures.append(f"Registry {rid or i}: tier 3 is forbidden")
        if not col(row, "evidence"):
            failures.append(f"Registry {rid or i}: evidence/cite is missing")

    floor_ok = grounded >= 3
    weak = cfm.get("grounding") == "weak"
    banner = bool(re.search(r"(?im)^\s*(?:>\s*)?(?:⚠|warning\b).*ground", course))
    gate(floor_ok or (weak and banner), "Grounding floor", f"{grounded} tier-1/2 misconceptions; weak={weak}; banner={banner}")

    outcomes = set(re.findall(r"\bLO-\d+\b", section(course, "5. Learning outcomes")))
    gate(5 <= len(outcomes) <= 10, "Learning outcomes", f"{len(outcomes)} unique LO ids")

    chapter_block = section(course, "6. Chapter map")
    _, chapters = table_rows(chapter_block)
    gate(bool(chapters), "Chapter map", f"{len(chapters)} rows parsed")
    planned_misconceptions: set[str] = set()
    for i, row in enumerate(chapters, 1):
        mapped = set(re.findall(r"\bLO-\d+\b", col(row, "outcomes")))
        if not mapped:
            failures.append(f"Chapter row {i}: no outcome")
        unknown = mapped - outcomes
        if unknown:
            failures.append(f"Chapter row {i}: unknown outcomes {sorted(unknown)}")
        targets = pause_targets(col(row, "planned pause"))
        for pause_type, rid in targets:
            target = by_id.get(rid)
            if target is None:
                failures.append(f"Chapter row {i}: unknown registry target {rid}")
                continue
            kind = col(target, "kind").lower()
            tier = col(target, "tier").strip()
            if pause_type == "misconception":
                planned_misconceptions.add(rid)
                if kind != "misconception" or tier not in {"1", "2"}:
                    failures.append(f"Chapter row {i}: misconception:{rid} requires kind=misconception and tier 1/2")
            if pause_type == "completion" and kind != "principle":
                failures.append(f"Chapter row {i}: completion:{rid} requires kind=principle")
    if chapters and not any(pause_targets(col(r, "planned pause")) for r in chapters):
        failures.append("Chapter map: no machine-readable pause targets; use misconception:<id>, completion:<id>, or prediction:<id>")

    diagnostic_ids = set(re.findall(r"registry_id=([a-z0-9][a-z0-9-]*)", diagnostic, re.I))
    missing = planned_misconceptions - {x.lower() for x in diagnostic_ids}
    gate(not missing, "Diagnosability", "all planned misconceptions covered" if not missing else f"missing {sorted(missing)}")

    items = re.split(r"(?m)^###\s+D\d+\s+—", diagnostic)[1:]
    declared = dfm.get("items", "")
    gate(3 <= len(items) <= 4, "Diagnostic count", f"{len(items)} items parsed")
    gate(declared == str(len(items)), "Diagnostic declaration", f"frontmatter={declared or 'missing'}, parsed={len(items)}")
    for i, item in enumerate(items, 1):
        options = re.findall(r"(?m)^-\s+\([a-z]\)\s+(.+)$", item)
        correct = sum("<!-- correct -->" in x for x in options)
        unknown = sum(bool(re.search(r"I don['’]t know", x, re.I)) for x in options)
        confidence = bool(re.search(r"\*\*Confidence:\*\*\s*guessing\s*/\s*fairly sure\s*/\s*confident", item, re.I))
        gate(correct == 1, f"D{i} correct option", f"{correct} marked")
        gate(unknown == 1, f"D{i} no-belief option", f"{unknown} I-don't-know options")
        gate(confidence, f"D{i} confidence", "required scale present")
        for option in options:
            if "<!-- correct -->" in option or re.search(r"I don['’]t know", option, re.I):
                continue
            if not re.search(r"registry_id=[a-z0-9][a-z0-9-]*", option, re.I):
                failures.append(f"D{i}: substantive distractor lacks registry_id")

    chapter_dir = course_path.parent / "chapters"
    voiced = set()
    if chapter_dir.is_dir():
        for path in chapter_dir.glob("*.md"):
            voiced.update(x.lower() for x in re.findall(r"registry_id=([a-z0-9][a-z0-9-]*)", path.read_text(encoding="utf-8"), re.I))
    retrofit_missing = voiced - set(by_id)
    gate(not retrofit_missing, "Retrofit coverage", "all chapter registry IDs covered" if not retrofit_missing else f"missing {sorted(retrofit_missing)}")

    warnings.extend([
        "MANUAL: verify each source and citation locator against the opened source.",
        "MANUAL: verify Bloom alignment, audience usefulness, vocabulary completeness, and P8 format neutrality.",
        "MANUAL: verify the Safety / Consumption envelope is present and adequate for sensitive domains.",
        "MANUAL: explicit human approval is required before changing status to approved.",
    ])
    return report(passes, warnings, failures)


def report(passes: list[str], warnings: list[str], failures: list[str]) -> int:
    for item in passes:
        print(f"PASS  {item}")
    for item in warnings:
        print(f"CHECK {item}")
    for item in failures:
        print(f"FAIL  {item}")
    print(f"\nResult: {len(passes)} passed, {len(warnings)} manual checks, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
