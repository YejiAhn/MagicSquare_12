"""Complete two-blank board: validate, place missing pair, return int[6] (1-based coords)."""

from __future__ import annotations

from magicsquare.blank_coords import find_blank_coords
from magicsquare.constants import GRID_SIZE
from magicsquare.errors import DomainError
from magicsquare.magic_judge import is_magic_square
from magicsquare.missing_numbers import find_missing_pair
from magicsquare.validator import BoardValidator


def _apply_pair(
    grid: list[list[int]],
    r1: int,
    c1: int,
    v1: int,
    r2: int,
    c2: int,
    v2: int,
) -> list[list[int]]:
    out = [row[:] for row in grid]
    out[r1][c1] = v1
    out[r2][c2] = v2
    return out


def _to_solution_vector(r1: int, c1: int, n1: int, r2: int, c2: int, n2: int) -> list[int]:
    """1-based row/col per PRD output contract."""
    return [r1 + 1, c1 + 1, n1, r2 + 1, c2 + 1, n2]


def _try_placement(
    grid: list[list[int]],
    r1: int,
    c1: int,
    r2: int,
    c2: int,
    n1: int,
    n2: int,
) -> list[int] | None:
    """Try one value order; return contract vector if grid becomes magic."""
    placed = _apply_pair(grid, r1, c1, n1, r2, c2, n2)
    if not is_magic_square(placed):
        return None
    return _to_solution_vector(r1, c1, n1, r2, c2, n2)


def solve(grid: list[list[int]]) -> list[int]:
    """
    Return [r1,c1,n1,r2,c2,n2] with 1-based coordinates (PRD §7.2).

    Try **forward**: smaller missing → row-major first blank, larger → second.
    If the filled grid is not magic, try **reverse** (larger → first, smaller → second).
    Return the vector for whichever attempt first yields a valid magic square.
    """
    BoardValidator().validate(grid)
    blanks = find_blank_coords(grid)
    (r1, c1), (r2, c2) = blanks[0], blanks[1]
    lo, hi = find_missing_pair(grid)

    forward_result = _try_placement(grid, r1, c1, r2, c2, lo, hi)
    if forward_result is not None:
        return forward_result

    reverse_result = _try_placement(grid, r1, c1, r2, c2, hi, lo)
    if reverse_result is not None:
        return reverse_result

    raise DomainError("DOMAIN_NO_VALID_PLACEMENT", "no valid placement for the two missing values")
