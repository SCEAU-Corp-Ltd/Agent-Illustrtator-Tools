#!/usr/bin/env python3
"""Build a readable Illustrator menu command index from the public CSV data."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "illustrator-menu-commands.csv"
TARGET = ROOT / "docs" / "illustrator-menu-command-links.md"


def md(text: object) -> str:
    value = "" if text is None else str(text)
    value = value.replace("\r", " ").replace("\n", "<br>")
    value = value.replace("|", "\\|")
    return value.strip()


def version(row: dict[str, str]) -> str:
    min_version = (row.get("minVersion") or "").strip()
    max_version = (row.get("maxVersion") or "").strip()
    if min_version and max_version:
        return f"{min_version}-{max_version}"
    if min_version:
        return f">= {min_version}"
    if max_version:
        return f"<= {max_version}"
    return ""


def requirements(row: dict[str, str]) -> str:
    parts = []
    if (row.get("docRequired") or "").upper() == "TRUE":
        parts.append("document")
    if (row.get("selRequired") or "").upper() == "TRUE":
        parts.append("selection")
    return ", ".join(parts)


def section_name(menu_path: str) -> str:
    if " > " in menu_path:
        return menu_path.split(" > ", 1)[0]
    if menu_path.startswith("Preferences"):
        return "Preferences"
    if menu_path.startswith("About"):
        return "About"
    return "Other"


def row_status(row: dict[str, str]) -> str:
    parts = []
    if (row.get("ignore") or "").upper() == "TRUE":
        parts.append("ignored")
    notes = (row.get("notes") or "").strip()
    if notes:
        parts.append(notes)
    return "; ".join(parts)


def main() -> None:
    with SOURCE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[section_name(row.get("en") or "")].append(row)

    counts = Counter(section_name(row.get("en") or "") for row in rows)
    sorted_sections = sorted(groups)

    lines = [
        "# Illustrator Menu Command Links",
        "",
        "This index is generated from `data/illustrator-menu-commands.csv`,",
        "which mirrors the public AiCommandPalette menu command data.",
        "",
        "Use the `value` field as the command identifier when an Illustrator",
        "automation surface supports menu-command execution. Verify each command",
        "against the active Illustrator version before using it in a destructive",
        "or batch workflow.",
        "",
        "Source: https://github.com/joshbduncan/AiCommandPalette/blob/main/data/menu_commands.csv",
        "",
        f"Total command rows: {len(rows)}.",
        "",
        "## Groups",
        "",
        "| Group | Rows |",
        "|---|---:|",
    ]

    for section in sorted_sections:
        anchor = section.lower().replace(" ", "-").replace("&", "").replace("/", "")
        lines.append(f"| [{md(section)}](#{anchor}) | {counts[section]} |")

    for section in sorted_sections:
        lines.extend(
            [
                "",
                f"## {section}",
                "",
                "| ID | Command value | Menu path | Requires | Version | Notes |",
                "|---|---|---|---|---|---|",
            ]
        )
        for row in groups[section]:
            command = md(row.get("value"))
            lines.append(
                "| {id} | `{command}` | {menu} | {requires} | {version} | {notes} |".format(
                    id=md(row.get("id")),
                    command=command.replace("`", "\\`"),
                    menu=md(row.get("en")),
                    requires=md(requirements(row)),
                    version=md(version(row)),
                    notes=md(row_status(row)),
                )
            )

    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
