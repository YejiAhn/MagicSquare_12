"""Coverage-completion tests for remaining branches."""

from __future__ import annotations

import runpy

import pytest
from PyQt6.QtWidgets import QApplication

import magicsquare.boundary as boundary_module
import magicsquare.gui.app as gui_app
from magicsquare.magic_judge import is_magic_square
from magicsquare.missing_numbers import find_missing_pair
from magicsquare.validator import BoardValidator
from tests.conftest import REF_MS, REF_PARTIAL_01


@pytest.fixture(scope="module")
def qapp() -> QApplication:
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


def test_boundary_validate_wraps_type_error_from_validator() -> None:
    with pytest.raises(ValueError):
        boundary_module.validate([1, 2, 3, 4])  # type: ignore[arg-type]


def test_boundary_validate_wraps_validation_error_from_validator() -> None:
    bad = [row[:] for row in REF_PARTIAL_01]
    bad[0][1] = 99
    with pytest.raises(ValueError):
        boundary_module.validate(bad)


def test_boundary_solve_delegates_after_validate(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    def fake_validate(grid: list[list[int]]) -> None:
        calls.append("validate")

    def fake_solve(grid: list[list[int]]) -> list[int]:
        calls.append("solve")
        return [1, 1, 16, 4, 4, 1]

    monkeypatch.setattr(boundary_module, "validate", fake_validate)
    monkeypatch.setattr(boundary_module, "_solve", fake_solve)

    out = boundary_module.solve(REF_PARTIAL_01)
    assert out == [1, 1, 16, 4, 4, 1]
    assert calls == ["validate", "solve"]


def test_magic_judge_guard_inputs() -> None:
    assert is_magic_square(None) is False  # type: ignore[arg-type]
    assert is_magic_square("not-a-grid") is False  # type: ignore[arg-type]
    assert is_magic_square([[1, 2], [3, 4]]) is False
    assert is_magic_square([[1, 2, 3, 4], [5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]) is False


def test_magic_judge_rejects_non_int_cells() -> None:
    bad = [row[:] for row in REF_MS]
    bad[0][0] = "16"  # type: ignore[index]
    assert is_magic_square(bad) is False


def test_magic_judge_rejects_column_sum_mismatch_after_row_checks() -> None:
    # Rows stay 34 and all values remain unique/ranged, but a column sum breaks.
    bad = [
        [3, 16, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(bad) is False


def test_magic_judge_rejects_main_diagonal_mismatch() -> None:
    # Row permutation preserves row/column sums while breaking main diagonal.
    bad = [
        [5, 10, 11, 8],
        [16, 3, 2, 13],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    assert is_magic_square(bad) is False


def test_magic_judge_rejects_anti_diagonal_mismatch() -> None:
    # Semi-magic: rows/cols and main diagonal are 34, anti-diagonal is not.
    bad = [
        [1, 2, 15, 16],
        [11, 14, 3, 6],
        [9, 8, 12, 5],
        [13, 10, 4, 7],
    ]
    assert is_magic_square(bad) is False


def test_find_missing_pair_raises_when_not_exactly_two_missing() -> None:
    with pytest.raises(ValueError):
        find_missing_pair(REF_MS)


def test_validator_row_must_be_list_type_error() -> None:
    with pytest.raises(TypeError):
        BoardValidator().validate([1, 2, 3, 4])  # type: ignore[arg-type]


def test_validator_grid_must_be_list_type_error() -> None:
    with pytest.raises(TypeError):
        BoardValidator().validate("not-a-list")  # type: ignore[arg-type]


def test_gui_window_success_flow_and_blank_parse(
    qapp: QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    called: dict[str, list[list[int]]] = {}

    def fake_validate(grid: list[list[int]]) -> None:
        called["validate"] = grid

    def fake_solve(grid: list[list[int]]) -> list[int]:
        called["solve"] = grid
        return [1, 1, 16, 4, 4, 1]

    monkeypatch.setattr(gui_app, "boundary_validate", fake_validate)
    monkeypatch.setattr(gui_app, "boundary_solve", fake_solve)

    window = gui_app.MagicSquareWindow()
    values = [
        ["", "3", "2", "13"],
        ["5", "10", "11", "8"],
        ["9", "6", "7", "12"],
        ["4", "15", "14", ""],
    ]
    for r, row in enumerate(values):
        for c, val in enumerate(row):
            window._inputs[r][c].setText(val)

    window._on_solve_clicked()

    assert called["validate"][0][0] == 0
    assert called["solve"][3][3] == 0
    assert "[1, 1, 16, 4, 4, 1]" in window._result_label.text()


def test_gui_window_error_flow_shows_warning(
    qapp: QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    window = gui_app.MagicSquareWindow()
    window._inputs[0][0].setText("x")

    captured: dict[str, str] = {}

    def fake_warning(parent: object, title: str, message: str) -> None:
        captured["title"] = title
        captured["message"] = message

    monkeypatch.setattr(gui_app.QMessageBox, "warning", fake_warning)

    window._on_solve_clicked()

    assert window._result_label.text() == "결과: -"
    assert captured["title"] == "입력 오류"
    assert "must be an integer" in captured["message"]


def test_gui_run_uses_qapplication_and_window(monkeypatch: pytest.MonkeyPatch) -> None:
    class DummyApp:
        def __init__(self, argv: list[str]) -> None:
            self.argv = argv

        def exec(self) -> int:
            return 7

    class DummyWindow:
        shown = False

        def show(self) -> None:
            DummyWindow.shown = True

    monkeypatch.setattr(gui_app, "QApplication", DummyApp)
    monkeypatch.setattr(gui_app, "MagicSquareWindow", DummyWindow)

    assert gui_app.run() == 7
    assert DummyWindow.shown is True


def test_gui_main_exits_using_run_result(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("magicsquare.gui.app.run", lambda: 0)
    with pytest.raises(SystemExit) as exc:
        runpy.run_module("magicsquare.gui.__main__", run_name="__main__")
    assert exc.value.code == 0
