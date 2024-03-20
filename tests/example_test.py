"""Unit Tests for example.py."""

# ruff: noqa: S101 D103 PLR2004 INP001

import sys
from pathlib import Path

# import pytest

sys.path.insert(0, (Path(__file__).parent.parent / "src").as_posix())

from example import calc_sum


def test_calc_sum() -> None:
    assert calc_sum(1, 2.2) == 3.2
