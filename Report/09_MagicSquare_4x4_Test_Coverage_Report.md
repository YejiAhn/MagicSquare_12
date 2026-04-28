# MagicSquare 4x4 Test & Coverage Report

- 작성일: 2026-04-28
- 범위: `src/magicsquare`
- 실행 환경: Python 3.10.11 / pytest 9.0.3 / pytest-cov 7.1.0

## 1) 실행 명령

```bash
python -m pytest --cov=src/magicsquare --cov-report=term-missing --cov-report=html
```

## 2) 테스트 결과

- 수집 테스트: 37
- 통과: 37
- 실패: 0
- 결과: PASS

## 3) 커버리지 요약

- TOTAL: **62%** (`229 statements`, `88 missed`)
- HTML 리포트 출력: `htmlcov/index.html`
- Live 확인 URL(로컬 서버): `http://localhost:5500`

## 4) 파일별 커버리지

| File | Stmts | Miss | Cover |
|---|---:|---:|---:|
| `src/magicsquare/__init__.py` | 5 | 0 | 100% |
| `src/magicsquare/blank_coords.py` | 8 | 0 | 100% |
| `src/magicsquare/boundary.py` | 15 | 6 | 60% |
| `src/magicsquare/constants.py` | 5 | 0 | 100% |
| `src/magicsquare/domain.py` | 6 | 0 | 100% |
| `src/magicsquare/errors.py` | 10 | 0 | 100% |
| `src/magicsquare/gui/__init__.py` | 0 | 0 | 100% |
| `src/magicsquare/gui/__main__.py` | 4 | 4 | 0% |
| `src/magicsquare/gui/app.py` | 67 | 67 | 0% |
| `src/magicsquare/magic_judge.py` | 33 | 7 | 79% |
| `src/magicsquare/missing_numbers.py` | 16 | 2 | 88% |
| `src/magicsquare/solver.py` | 26 | 0 | 100% |
| `src/magicsquare/validator.py` | 34 | 2 | 94% |

## 5) 관찰 및 다음 액션

- GUI Screen 레이어(`gui/app.py`)는 자동화 테스트가 없어 현재 0%입니다.
- `boundary.py`는 실패 경로(예외 매핑) 중심 테스트를 추가하면 빠르게 상승 가능합니다.
- 다음 목표 예시: `TOTAL 70%` 이상 (`--cov-fail-under=70` 도입 검토).
