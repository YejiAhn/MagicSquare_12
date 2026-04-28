"""Shared fixtures aligned with docs/MagicSquare_4x4_TestCase_Specification_Form.md."""

from __future__ import annotations

import pytest


REF_MS = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

REF_PARTIAL_01 = [
    [0, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
]

REF_PARTIAL_02 = [
    [16, 0, 2, 13],
    [0, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# Forward placement fails; reverse completes REF_MS (TC reverse / TASK-025).
REF_PARTIAL_REVERSE_ONLY = [
    [16, 0, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
]

# TC-MS-D-008: two blanks, valid range, no duplicate non-zero, neither placement is magic.
D008_NO_PLACEMENT = [
    [0, 0, 8, 14],
    [7, 1, 9, 4],
    [10, 5, 11, 3],
    [6, 15, 16, 2],
]


def apply_solution(grid: list[list[int]], r1: int, c1: int, n1: int, r2: int, c2: int, n2: int) -> list[list[int]]:
    """Apply 1-based PRD output to a copy of the grid."""
    out = [row[:] for row in grid]
    out[r1 - 1][c1 - 1] = n1
    out[r2 - 1][c2 - 1] = n2
    return out


@pytest.fixture
def ref_ms() -> list[list[int]]:
    return [row[:] for row in REF_MS]


@pytest.fixture
def ref_partial_01() -> list[list[int]]:
    return [row[:] for row in REF_PARTIAL_01]
