"""MissingNumbersFinder alignment — find_missing_pair."""

from __future__ import annotations

from magicsquare.missing_numbers import find_missing_pair

from tests.conftest import REF_PARTIAL_01, REF_PARTIAL_02


def test_should_find_sorted_missing_pair_partial_01() -> None:
    assert find_missing_pair(REF_PARTIAL_01) == (1, 16)


def test_should_find_sorted_missing_pair_partial_02() -> None:
    assert find_missing_pair(REF_PARTIAL_02) == (3, 5)
