# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Python package `members-csv-claude-fcc` for reading and processing CSV files with member data. Study project based on the Python for Beginners course from freeCodeCamp.

## Environment

- Python 3.14.4 via local `.venv`
- No external dependencies (standard library only)

## Commands

```powershell
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install package in editable mode (required to import or use the CLI)
pip install -e .

# Use the CLI after installation
members-csv members.csv
```

## Structure

```
src/members_csv_claude_fcc/
    __init__.py   — exports read_members and get_full_names
    reader.py     — core functions with type hints and docstrings
    cli.py        — CLI entry point (members-csv <filepath>)
pyproject.toml    — package metadata and entry point
members.csv       — sample data file (1,000 records)
```

## Package API

- `read_members(filepath)` → `list[dict]` — reads any CSV and returns all rows
- `get_full_names(filepath)` → `list[str]` — returns `"first_name last_name"` for each row

Both accept `str` or `pathlib.Path`. Expect UTF-8 CSV with a header row.
