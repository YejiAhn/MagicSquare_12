"""TC-MS-C-001 .. C-008 — solve() and completed grid sums."""

from __future__ import annotations

import pytest

from magicsquare import is_magic_square, solve
from magicsquare.errors import ValidationError

from tests.conftest import REF_MS, REF_PARTIAL_01, REF_PARTIAL_02, REF_PARTIAL_REVERSE_ONLY, apply_solution


def test_TC_MS_C_001_solve_partial_01() -> None:
    """정순(1→첫 빈칸, 16→둘째)은 행0 합이 34가 아니므로 실패하고 역순이 선택된다."""
    out = solve(REF_PARTIAL_01)
    assert out == [1, 1, 16, 4, 4, 1]
    filled = apply_solution(REF_PARTIAL_01, *out)
    assert is_magic_square(filled) is True


def test_TC_MS_C_002_solve_partial_02() -> None:
    out = solve(REF_PARTIAL_02)
    assert out == [1, 2, 3, 2, 1, 5]
    assert is_magic_square(apply_solution(REF_PARTIAL_02, *out)) is True


def test_TC_MS_C_003_completed_board_rejected_by_validator() -> None:
    with pytest.raises(ValidationError) as ei:
        solve(REF_MS)
    assert ei.value.code == "VALIDATION_BLANKS"


def test_TC_MS_C_004_result_contains_minimum_one() -> None:
    out = solve(REF_PARTIAL_01)
    assert 1 in (out[2], out[5])


def test_TC_MS_C_005_result_contains_maximum_sixteen() -> None:
    out = solve(REF_PARTIAL_01)
    assert 16 in (out[2], out[5])


def test_TC_MS_C_006_to_C_008_row_col_diag_sums_after_apply() -> None:
    g = apply_solution(REF_PARTIAL_01, 1, 1, 16, 4, 4, 1)
    assert [sum(g[i]) for i in range(4)] == [34, 34, 34, 34]
    assert [sum(g[i][j] for i in range(4)) for j in range(4)] == [34, 34, 34, 34]
    assert sum(g[i][i] for i in range(4)) == 34
    assert sum(g[i][3 - i] for i in range(4)) == 34


def test_dual_placement_resolver_reverse_fallback() -> None:
    """TASK-025: forward fails, reverse succeeds — expect reverse mapping in int[6]."""
    out = solve(REF_PARTIAL_REVERSE_ONLY)
    assert out == [1, 2, 3, 4, 4, 1]
    assert is_magic_square(apply_solution(REF_PARTIAL_REVERSE_ONLY, *out)) is True
