"""Magic square completion judge (1..16 permutation, sums == 34)."""

from __future__ import annotations

from magicsquare.constants import GRID_SIZE, MAGIC_SUM, MAX_CELL, MIN_CELL


def _sum_row(grid: list[list[int]], row_index: int) -> int:
    """Return sum of one row."""
    return sum(grid[row_index][col_index] for col_index in range(GRID_SIZE))


def _sum_col(grid: list[list[int]], col_index: int) -> int:
    """Return sum of one column."""
    return sum(grid[row_index][col_index] for row_index in range(GRID_SIZE))


def _sum_main_diag(grid: list[list[int]]) -> int:
    """Return sum of top-left to bottom-right diagonal."""
    return sum(grid[index][index] for index in range(GRID_SIZE))


def _sum_anti_diag(grid: list[list[int]]) -> int:
    """Return sum of top-right to bottom-left diagonal."""
    return sum(grid[index][GRID_SIZE - 1 - index] for index in range(GRID_SIZE))


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
    for row_index in range(GRID_SIZE):
        if _sum_row(grid, row_index) != MAGIC_SUM:
            return False
    for col_index in range(GRID_SIZE):
        if _sum_col(grid, col_index) != MAGIC_SUM:
            return False
    if _sum_main_diag(grid) != MAGIC_SUM:
        return False
    if _sum_anti_diag(grid) != MAGIC_SUM:
        return False
    return True
