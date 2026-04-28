"""TC-MS-D-001 .. D-008 — validation and domain errors on solve()."""

from __future__ import annotations

import pytest

from magicsquare.errors import DomainError, ValidationError
from magicsquare.solver import solve

from tests.conftest import D008_NO_PLACEMENT, REF_MS


def test_TC_MS_D_001_out_of_range_value() -> None:
    d001 = [
        [0, 17, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 0],
    ]
    with pytest.raises(ValidationError) as ei:
        solve(d001)
    assert ei.value.code == "VALIDATION_RANGE"


def test_TC_MS_D_002_duplicate_non_zero() -> None:
    d002 = [
        [0, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 3, 14, 0],
    ]
    with pytest.raises(ValidationError) as ei:
        solve(d002)
    assert ei.value.code == "VALIDATION_DUPLICATE"


def test_TC_MS_D_003_non_4x4_shape() -> None:
    d003 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValidationError) as ei:
        solve(d003)
    assert ei.value.code == "VALIDATION_SHAPE"


def test_TC_MS_D_004_none_grid_type_error() -> None:
    with pytest.raises(TypeError):
        solve(None)  # type: ignore[arg-type]


def test_TC_MS_D_004_empty_list_shape_error() -> None:
    with pytest.raises(ValidationError) as ei:
        solve([])
    assert ei.value.code == "VALIDATION_SHAPE"


def test_TC_MS_D_005_non_int_cell() -> None:
    d005 = [["16", 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 0]]
    with pytest.raises(ValidationError) as ei:
        solve(d005)
    assert ei.value.code == "VALIDATION_TYPE"


def test_TC_MS_D_006_jagged_rows() -> None:
    d006 = [[1, 2, 3, 4], [5, 6], [7, 8, 9, 10], [11, 12, 13, 14]]
    with pytest.raises(ValidationError) as ei:
        solve(d006)
    assert ei.value.code == "VALIDATION_SHAPE"


def test_TC_MS_D_007_wrong_blank_count_zero_blanks() -> None:
    with pytest.raises(ValidationError) as ei:
        solve(REF_MS)
    assert ei.value.code == "VALIDATION_BLANKS"


def test_TC_MS_D_007_wrong_blank_count_one_blank() -> None:
    one_blank = [
        [0, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    with pytest.raises(ValidationError) as ei:
        solve(one_blank)
    assert ei.value.code == "VALIDATION_BLANKS"


def test_TC_MS_D_008_no_valid_placement() -> None:
    with pytest.raises(DomainError) as ei:
        solve(D008_NO_PLACEMENT)
    assert ei.value.code == "DOMAIN_NO_VALID_PLACEMENT"
