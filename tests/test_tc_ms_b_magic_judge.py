"""TC-MS-B-001 .. B-005 — is_magic_square."""

from __future__ import annotations

from magicsquare.magic_judge import is_magic_square

from tests.conftest import REF_MS


def test_TC_MS_B_001_valid_reference_magic_square() -> None:
    assert is_magic_square(REF_MS) is True


def test_TC_MS_B_002_row_sum_broken() -> None:
    b002 = [
        [15, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(b002) is False


def test_TC_MS_B_003_column_sum_broken() -> None:
    b003 = [
        [17, 2, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(b003) is False


def test_TC_MS_B_004_main_diagonal_broken() -> None:
    b004 = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 2],
    ]
    assert is_magic_square(b004) is False


def test_TC_MS_B_005_anti_diagonal_broken() -> None:
    b005 = [
        [16, 3, 2, 12],
        [5, 10, 11, 8],
        [9, 6, 7, 13],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(b005) is False


def test_is_magic_square_rejects_zeros() -> None:
    assert is_magic_square(REF_MS)  # sanity
    partial = [row[:] for row in REF_MS]
    partial[0][0] = 0
    assert is_magic_square(partial) is False
