import csv
from pathlib import Path


def read_members(filepath: str | Path) -> list[dict]:
    """Read all rows from a CSV file and return as a list of dicts.

    Args:
        filepath: Path to a UTF-8 encoded CSV file with a header row.

    Returns:
        List of dicts where keys are the CSV column headers.
    """
    with open(filepath, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def get_full_names(filepath: str | Path) -> list[str]:
    """Return full names from a members CSV.

    Expects columns ``first_name`` and ``last_name``.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of strings in the format ``"first_name last_name"``.
    """
    return [f"{row['first_name']} {row['last_name']}" for row in read_members(filepath)]
