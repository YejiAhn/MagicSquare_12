"""Boundary layer for input validation and domain delegation."""

from __future__ import annotations

from magicsquare.domain import MATRIX_SIZE
from magicsquare.errors import ValidationError
from magicsquare.solver import solve as _solve
from magicsquare.validator import BoardValidator


def validate(grid: list[list[int]]) -> None:
    """
    Validate input at boundary and normalize failures to ValueError.

    This keeps UI handling simple while preserving domain internals.
    """
    if len(grid) != MATRIX_SIZE:
        raise ValueError(f"grid must have exactly {MATRIX_SIZE} rows")
    try:
        BoardValidator().validate(grid)
    except (TypeError, ValidationError) as exc:
        raise ValueError(str(exc)) from exc


def solve(grid: list[list[int]]) -> list[int]:
    """Validate first, then delegate to domain solver contract output."""
    validate(grid)
    return _solve(grid)
