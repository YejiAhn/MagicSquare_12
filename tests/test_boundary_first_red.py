"""Track A first RED: boundary shape validation."""

from __future__ import annotations

import pytest

from magicsquare.boundary import validate


def test_U_RED_01_boundary_validate_raises_for_non_4x4() -> None:
    bad_shape = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError):
        validate(bad_shape)
