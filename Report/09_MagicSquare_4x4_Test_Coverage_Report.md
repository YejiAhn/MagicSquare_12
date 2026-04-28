# MagicSquare 4x4 Test & Coverage Report

- 작성일: 2026-04-28
- 범위: `src/magicsquare`
- 실행 환경: Python 3.10.11 / pytest 9.0.3 / pytest-cov 7.1.0

## 1) 실행 명령

```bash
python -m pytest --cov=src/magicsquare --cov-report=term-missing --cov-report=html
```

## 2) 테스트 결과

- 수집 테스트: 52
- 통과: 52
- 실패: 0
- 결과: PASS

## 3) 커버리지 요약

- TOTAL: **100%** (`227 statements`, `0 missed`)
- HTML 리포트 출력: `htmlcov/index.html`
- Live 확인 URL(로컬 서버): `http://localhost:5500`

## 4) 파일별 커버리지

| File | Stmts | Miss | Cover |
|---|---:|---:|---:|
| `src/magicsquare/__init__.py` | 5 | 0 | 100% |
| `src/magicsquare/blank_coords.py` | 8 | 0 | 100% |
| `src/magicsquare/boundary.py` | 15 | 0 | 100% |
| `src/magicsquare/constants.py` | 5 | 0 | 100% |
| `src/magicsquare/domain.py` | 6 | 0 | 100% |
| `src/magicsquare/errors.py` | 10 | 0 | 100% |
| `src/magicsquare/gui/__init__.py` | 0 | 0 | 100% |
| `src/magicsquare/gui/__main__.py` | 4 | 0 | 100% |
| `src/magicsquare/gui/app.py` | 67 | 0 | 100% |
| `src/magicsquare/magic_judge.py` | 33 | 0 | 100% |
| `src/magicsquare/missing_numbers.py` | 14 | 0 | 100% |
| `src/magicsquare/solver.py` | 26 | 0 | 100% |
| `src/magicsquare/validator.py` | 34 | 0 | 100% |

## 5) 관찰 및 다음 액션

- GUI Screen 레이어(`gui/app.py`)와 진입점(`gui/__main__.py`)에 대한 분기 테스트를 추가해 UI 코드도 커버리지에 포함했습니다.
- Boundary/Validator의 예외 경로(TypeError/ValidationError 래핑) 테스트를 보강해 계약 경로를 모두 검증했습니다.
- 커버리지 유지 가드 예시: `--cov-fail-under=100`를 CI 또는 로컬 스크립트에 도입.
