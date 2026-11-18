"""Turn this template into a named project. Run once, right after creating a repo from it.

Usage:
    python scripts/init_project.py fraudshield "Real-time payment fraud detection"

It renames the package folder and replaces every `project_name` / `project-name` placeholder.
Works on Windows, macOS and Linux (no sed needed).
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_SNAKE = "project_name"
PLACEHOLDER_KEBAB = "project-name"
PLACEHOLDER_DESCRIPTION = "One line: the problem this project solves."
TEXT_SUFFIXES = {".py", ".toml", ".md", ".yml", ".yaml", ".cfg", ".txt", ".lock", ""}
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".ruff_cache", ".pytest_cache", "data"}
NAME_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")


def validate_name(name: str) -> str:
    if not NAME_PATTERN.match(name):
        raise SystemExit(
            f"Invalid name '{name}'. Use lowercase letters, digits and underscores, "
            "starting with a letter (e.g. fraudshield, credit_lens)."
        )
    return name


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.is_file() and (path.suffix in TEXT_SUFFIXES or path.name == "Makefile"):
            yield path


def replace_placeholders(root: Path, snake: str, description: str | None) -> list[Path]:
    kebab = snake.replace("_", "-")
    changed = []
    for path in iter_text_files(root):
        if path.resolve() == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = text.replace(PLACEHOLDER_SNAKE, snake).replace(PLACEHOLDER_KEBAB, kebab)
        if description:
            new = new.replace(PLACEHOLDER_DESCRIPTION, description)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed.append(path)
    return changed


def rename_package(root: Path, snake: str) -> None:
    old = root / "src" / PLACEHOLDER_SNAKE
    new = root / "src" / snake
    if not old.exists():
        raise SystemExit(f"{old} not found. Has this project already been initialised?")
    shutil.move(str(old), str(new))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("name", help="package name in snake_case, e.g. fraudshield")
    parser.add_argument("description", nargs="?", help="one-line project description")
    args = parser.parse_args()

    snake = validate_name(args.name)
    changed = replace_placeholders(ROOT, snake, args.description)
    rename_package(ROOT, snake)
    print(f"Renamed package to src/{snake}/ and updated {len(changed)} files.")
    print("Next: delete scripts/init_project.py, run `make setup`, then commit.")


if __name__ == "__main__":
    main()
