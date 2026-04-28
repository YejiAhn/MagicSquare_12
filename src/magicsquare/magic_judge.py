"""Magic square completion judge (1..16 permutation, sums == 34)."""

from __future__ import annotations

from magicsquare.constants import GRID_SIZE, MAGIC_SUM, MAX_CELL, MIN_CELL


def is_magic_square(grid: list[list[int]]) -> bool:
    """
    True iff grid is 4x4, has no zeros, uses 1..16 exactly once,
    and every row, column, and both diagonals sum to 34.
    """
    if grid is None or not isinstance(grid, list):
        return False
    if len(grid) != GRID_SIZE:
        return False
    if any(len(row) != GRID_SIZE for row in grid):
        return False
    flat: list[int] = []
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            v = grid[r][c]
            if not isinstance(v, int):
                return False
            flat.append(v)
    if any(v == 0 for v in flat):
        return False
    if any(v < MIN_CELL + 1 or v > MAX_CELL for v in flat):
        return False
    if len(set(flat)) != GRID_SIZE * GRID_SIZE:
        return False
    for r in range(GRID_SIZE):
        if sum(grid[r][c] for c in range(GRID_SIZE)) != MAGIC_SUM:
            return False
    for c in range(GRID_SIZE):
        if sum(grid[r][c] for r in range(GRID_SIZE)) != MAGIC_SUM:
            return False
    if sum(grid[i][i] for i in range(GRID_SIZE)) != MAGIC_SUM:
        return False
    if sum(grid[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)) != MAGIC_SUM:
        return False
    return True
