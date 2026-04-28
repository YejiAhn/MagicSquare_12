"""Board input validation (PRD §7.1)."""

from __future__ import annotations

from magicsquare.blank_coords import find_blank_coords
from magicsquare.constants import GRID_SIZE, MAX_CELL, MIN_CELL, REQUIRED_BLANKS
from magicsquare.errors import ValidationError


class BoardValidator:
    def validate(self, grid: object) -> None:
        if grid is None:
            raise TypeError("grid must not be None")
        if not isinstance(grid, list):
            raise TypeError("grid must be a list of rows")
        if len(grid) != GRID_SIZE:
            raise ValidationError("VALIDATION_SHAPE", "grid must have exactly 4 rows")
        for r, row in enumerate(grid):
            if not isinstance(row, list):
                raise TypeError(f"row {r} must be a list")
            if len(row) != GRID_SIZE:
                raise ValidationError("VALIDATION_SHAPE", "each row must have length 4")
            for c, val in enumerate(row):
                if not isinstance(val, int):
                    raise ValidationError(
                        "VALIDATION_TYPE", f"cell ({r},{c}) must be int, got {type(val).__name__}"
                    )
                if val < MIN_CELL or val > MAX_CELL:
                    raise ValidationError(
                        "VALIDATION_RANGE", f"cell ({r},{c}) value {val} out of range 0..16"
                    )
        blanks = find_blank_coords(grid)
        if len(blanks) != REQUIRED_BLANKS:
            raise ValidationError(
                "VALIDATION_BLANKS",
                f"expected exactly {REQUIRED_BLANKS} blank cells (0), found {len(blanks)}",
            )
        seen: set[int] = set()
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                v = grid[r][c]
                if v == 0:
                    continue
                if v in seen:
                    raise ValidationError("VALIDATION_DUPLICATE", f"duplicate non-zero value {v}")
                seen.add(v)
