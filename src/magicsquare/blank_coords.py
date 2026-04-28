"""Locate blank cells (value 0) in row-major order."""

from __future__ import annotations


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return (row, col) for every cell equal to 0, sorted row-major."""
    coords: list[tuple[int, int]] = []
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 0:
                coords.append((r, c))
    return coords
