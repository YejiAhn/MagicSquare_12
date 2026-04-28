"""Domain facade for logic-only rules."""

from __future__ import annotations

from magicsquare.blank_coords import find_blank_coords as _find_blank_coords
from magicsquare.constants import GRID_SIZE

MATRIX_SIZE = GRID_SIZE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return row-major blank coordinates (value 0)."""
    return _find_blank_coords(grid)
