import argparse

from .reader import get_full_names


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="members-csv",
        description="Print member names from a CSV file.",
    )
    parser.add_argument("filepath", help="Path to the CSV file")
    args = parser.parse_args()

    for name in get_full_names(args.filepath):
        print(name)
