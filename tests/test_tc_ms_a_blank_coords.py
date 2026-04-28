"""TC-MS-A-001 .. A-005 — find_blank_coords (0-based, row-major)."""

from __future__ import annotations

import pytest

from magicsquare.blank_coords import find_blank_coords

from tests.conftest import REF_MS, REF_PARTIAL_01


def test_TC_MS_A_001_find_blanks_row_major_two_zeros() -> None:
    assert find_blank_coords(REF_PARTIAL_01) == [(0, 0), (3, 3)]


def test_TC_MS_A_002_corner_blanks_same_as_partial_01() -> None:
    assert find_blank_coords(REF_PARTIAL_01) == [(0, 0), (3, 3)]


def test_TC_MS_A_003_no_blanks_returns_empty() -> None:
    assert find_blank_coords(REF_MS) == []


def test_TC_MS_A_004_single_blank() -> None:
    grid_one_blank = [
        [0, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    assert find_blank_coords(grid_one_blank) == [(0, 0)]


def test_TC_MS_A_005_three_blanks_row_major() -> None:
    grid_three = [
        [0, 0, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 0],
    ]
    assert find_blank_coords(grid_three) == [(0, 0), (0, 1), (3, 3)]
