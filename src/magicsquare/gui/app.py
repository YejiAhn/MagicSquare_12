"""PyQt6 screen MVP wired to boundary layer."""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from magicsquare.boundary import solve as boundary_solve
from magicsquare.boundary import validate as boundary_validate
from magicsquare.domain import MATRIX_SIZE


class MagicSquareWindow(QWidget):
    """Simple 4x4 input form with solve action."""

    def __init__(self) -> None:
        super().__init__()
        self._inputs: list[list[QLineEdit]] = []
        self._result_label = QLabel("결과: -")
        self._build_ui()

    def _build_ui(self) -> None:
        self.setWindowTitle("MagicSquare 4x4")

        root = QVBoxLayout()
        root.addWidget(QLabel("4x4 숫자 입력 (빈칸은 0)"))

        grid = QGridLayout()
        for r in range(MATRIX_SIZE):
            row_inputs: list[QLineEdit] = []
            for c in range(MATRIX_SIZE):
                edit = QLineEdit()
                edit.setMaxLength(2)
                edit.setPlaceholderText("0")
                edit.setFixedWidth(56)
                grid.addWidget(edit, r, c)
                row_inputs.append(edit)
            self._inputs.append(row_inputs)
        root.addLayout(grid)

        actions = QHBoxLayout()
        solve_btn = QPushButton("풀기")
        solve_btn.clicked.connect(self._on_solve_clicked)
        actions.addWidget(solve_btn)
        root.addLayout(actions)

        self._result_label.setWordWrap(True)
        root.addWidget(self._result_label)

        self.setLayout(root)
        self.resize(320, 260)

    def _read_grid(self) -> list[list[int]]:
        grid: list[list[int]] = []
        for r in range(MATRIX_SIZE):
            row: list[int] = []
            for c in range(MATRIX_SIZE):
                raw = self._inputs[r][c].text().strip()
                if raw == "":
                    row.append(0)
                    continue
                try:
                    row.append(int(raw))
                except ValueError as exc:
                    raise ValueError(f"cell ({r + 1},{c + 1}) must be an integer") from exc
            grid.append(row)
        return grid

    def _on_solve_clicked(self) -> None:
        try:
            grid = self._read_grid()
            boundary_validate(grid)
            out = boundary_solve(grid)
        except ValueError as exc:
            self._result_label.setText("결과: -")
            QMessageBox.warning(self, "입력 오류", str(exc))
            return

        self._result_label.setText(f"결과 [r1,c1,n1,r2,c2,n2]: {out}")


def run() -> int:
    """Start Qt application loop."""
    app = QApplication(sys.argv)
    window = MagicSquareWindow()
    window.show()
    return app.exec()
