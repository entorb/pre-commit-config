"""
Example Python script.

for testing Ruff findings and solutions
"""  # noqa: INP001

import datetime as dt
from pathlib import Path
from zoneinfo import ZoneInfo

TZ_DE = ZoneInfo("Europe/Berlin")


def calc_sum(x: int, y: float) -> float:
    """Calculate the sum of an integer and a float."""
    return x + y


def print_date() -> None:
    """Print the current date."""
    # DTZ011 do not use dt.date.today()
    print(dt.datetime.now(tz=TZ_DE).date())


def read_file(filename: Path) -> str:
    """Read a file and return first line."""
    with filename.open(encoding="utf-8") as f:
        return f.readline()


if __name__ == "__main__":
    print_date()
    print(calc_sum(1, 2.2))
    print(read_file(Path("LICENSE")))
