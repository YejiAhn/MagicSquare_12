"""Find the two numbers in 1..16 absent from a partially filled board."""

from __future__ import annotations

from magicsquare.constants import GRID_SIZE, MAX_CELL


def find_missing_pair(grid: list[list[int]]) -> tuple[int, int]:
    """Return (a, b) with a < b for the two values in 1..16 not present on the grid."""
    present: set[int] = set()
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            v = grid[r][c]
            if v != 0:
                present.add(v)
    missing = [x for x in range(1, MAX_CELL + 1) if x not in present]
    if len(missing) != 2:
        raise ValueError("expected exactly two missing numbers for two blank cells")
    a, b = missing[0], missing[1]
    return tuple(sorted((a, b)))
