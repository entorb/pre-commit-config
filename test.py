"""
Simple Python test script.

for testing Ruff findings and solutions

here is a customword for cspell
"""

import datetime as dt
from pathlib import Path


def calc_sum(x: int, y: float) -> float:
    """
    Calculate the sum of an integer and a float.

    Args:
    ----
        x (int): The integer to be added.
        y (float): The float to be added.

    Returns:
    -------
        float: The sum of x and y.
    """
    return x + y


def print_date() -> None:
    """Print the current date."""
    print(dt.datetime.now(tz=dt.timezone.utc).date())


def read_file(filename: Path) -> str:
    """Read a file and return first line."""
    with filename.open(encoding="utf-8") as f:
        return f.readline()


# init main
if __name__ == "__main__":
    print_date()
    print(calc_sum(1, 2.2))
    print(read_file(Path("LICENSE")))
