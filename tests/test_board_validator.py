"""BoardValidator tests (TASK-004 .. TASK-011 naming alignment)."""

from __future__ import annotations

import pytest

from magicsquare.errors import ValidationError
from magicsquare.validator import BoardValidator

from tests.conftest import REF_MS, REF_PARTIAL_01


@pytest.fixture
def validator() -> BoardValidator:
    return BoardValidator()


def test_should_reject_non_4x4(validator: BoardValidator) -> None:
    with pytest.raises(ValidationError) as ei:
        validator.validate([[1, 2], [3, 4]])
    assert ei.value.code == "VALIDATION_SHAPE"


def test_should_reject_out_of_range_values(validator: BoardValidator) -> None:
    bad = [row[:] for row in REF_PARTIAL_01]
    bad[0][1] = 99
    with pytest.raises(ValidationError) as ei:
        validator.validate(bad)
    assert ei.value.code == "VALIDATION_RANGE"


def test_should_reject_invalid_blank_count(validator: BoardValidator) -> None:
    with pytest.raises(ValidationError) as ei:
        validator.validate(REF_MS)
    assert ei.value.code == "VALIDATION_BLANKS"


def test_should_reject_duplicate_non_zero(validator: BoardValidator) -> None:
    dup = [row[:] for row in REF_PARTIAL_01]
    dup[3][0] = 3
    with pytest.raises(ValidationError) as ei:
        validator.validate(dup)
    assert ei.value.code == "VALIDATION_DUPLICATE"


def test_should_accept_valid_partial_board(validator: BoardValidator) -> None:
    validator.validate(REF_PARTIAL_01)
