"""Track B first RED: domain row-major blank coordinates."""

from __future__ import annotations

from magicsquare.domain import find_blank_coords

from tests.conftest import REF_PARTIAL_01


def test_L_RED_01_domain_find_blank_coords_row_major_two_zeros() -> None:
    assert find_blank_coords(REF_PARTIAL_01) == [(0, 0), (3, 3)]
