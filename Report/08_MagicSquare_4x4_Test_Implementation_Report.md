# MagicSquare 4×4 — 테스트 구현·실행 보고서

## 1. 문서 개요

| 항목 | 내용 |
|------|------|
| **문서명** | 테스트 구현·가상환경 실행·산출물 구조 보고 |
| **프로젝트명** | MagicSquare 4×4 |
| **작성 목적** | 저장소에 반영된 **단위·통합 테스트 코드**와 **실행 방법**을 Report에 기록하고, 명세·PRD·To-Do와의 추적 관계를 명시한다. |
| **작성일** | 2026-04-28 |
| **문서 상태** | 확정(구현 시점 스냅샷) |

### 1.1 관련 문서

| 문서 | 경로 |
|------|------|
| 테스트 케이스 명세(실행용 상세) | [`07_MagicSquare_4x4_TestCase_Specification_Form.md`](./07_MagicSquare_4x4_TestCase_Specification_Form.md) |
| 구현 To-Do | [`06_MagicSquare_4x4_Implementation_Todo_Report.md`](./06_MagicSquare_4x4_Implementation_Todo_Report.md) |
| PRD | [`05_MagicSquare_PRD.md`](./05_MagicSquare_PRD.md) |
| 동기 `docs` 명세 | [`../docs/MagicSquare_4x4_TestCase_Specification_Form.md`](../docs/MagicSquare_4x4_TestCase_Specification_Form.md) |

---

## 2. 산출물 구조(코드)

저장소 루트 기준이다.

| 경로 | 설명 |
|------|------|
| `src/magicsquare/` | 도메인 패키지: 검증, 빈칸 탐색, 누락 수, 마방진 판정, `solve` |
| `src/magicsquare/__init__.py` | 공개 API: `find_blank_coords`, `is_magic_square`, `solve`, `ValidationError`, `DomainError` |
| `src/magicsquare/constants.py` | `GRID_SIZE`, `MAGIC_SUM`(34), 값 범위 상수 |
| `src/magicsquare/errors.py` | `ValidationError`·`DomainError` 및 `code` 필드 |
| `src/magicsquare/blank_coords.py` | `find_blank_coords` — row-major `(행, 열)` 0-기반 |
| `src/magicsquare/magic_judge.py` | `is_magic_square` — 1~16 퍼뮤테이션 및 행·열·대각 합 34 |
| `src/magicsquare/missing_numbers.py` | 두 빈칸 전제 하 1~16 중 누락 쌍 `(lo, hi)` |
| `src/magicsquare/validator.py` | `BoardValidator` — 형태·범위·빈칸 2개·중복 |
| `src/magicsquare/solver.py` | `solve` — 검증 후 정순 배치 시도, 실패 시 역순, 성공 시 `int[6]`(좌표 1-기반) |
| `tests/conftest.py` | `REF_MS`, `REF_PARTIAL_*`, `D008_NO_PLACEMENT`, `apply_solution` |
| `tests/test_tc_ms_*.py` | 명세 TC-MS-A~D 블록과 대응하는 pytest 모듈 |
| `tests/test_board_validator.py` | To-Do의 `BoardValidatorTest` 계열 이름 정렬 |
| `tests/test_missing_numbers.py` | 누락 수 산출 |
| `pyproject.toml` | 프로젝트 메타, `[tool.pytest.ini_options]` — `pythonpath = ["src"]`, `testpaths = ["tests"]` |
| `requirements-dev.txt` | `pytest>=8.0` |

---

## 3. 테스트 실행(가상환경)

### 3.1 Windows PowerShell

```powershell
cd c:\DEV\MagicSquare_12
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements-dev.txt
python -m pytest tests -v
```

`Activate.ps1`이 차단되면 `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` 후 다시 활성화한다.

### 3.2 비활성화

```powershell
deactivate
```

### 3.3 최근 실행 결과(스냅샷)

- **수집**: 35 tests  
- **결과**: **35 passed**  
- **소요**: 약 0.1초 내(로컬 기준)

---

## 4. 명세 TC ID ↔ 테스트 모듈 매핑

| 명세 구간 | 테스트 파일 | 비고 |
|-----------|----------------|------|
| TC-MS-A-001 ~ A-005 | `tests/test_tc_ms_a_blank_coords.py` | A-003~005는 검증 없이 `find_blank_coords` 단독 시나리오 |
| TC-MS-B-001 ~ B-005 | `tests/test_tc_ms_b_magic_judge.py` | `is_magic_square` |
| TC-MS-C-001 ~ C-008, 역순 폴백 | `tests/test_tc_ms_c_solver.py` | `solve`, `apply_solution`, 행·열·대각 검산 |
| TC-MS-D-001 ~ D-008 | `tests/test_tc_ms_d_validation.py` | `solve` 입구 검증·도메인 실패 |
| BoardValidator (TASK-004 등) | `tests/test_board_validator.py` | `BoardValidator.validate` |
| 누락 수 쌍 | `tests/test_missing_numbers.py` | `find_missing_pair` |

---

## 5. 계약·판정 메모(PRD 정렬)

### 5.1 `solve` 성공 출력

- 형식: **`[r1, c1, n1, r2, c2, n2]`** — 좌표는 **1~4**(1-기반), `n1`·`n2`는 해당 칸에 놓인 값.
- 배치 시도: **정순**(작은 누락 수 → row-major 첫 빈칸, 큰 수 → 둘째 빈칸)으로 채운 뒤 `is_magic_square`가 참이면 채택. 아니면 **역순**(큰 수 → 첫 빈칸, 작은 수 → 둘째)을 시도한다.

### 5.2 `REF_PARTIAL_01` 기대 벡터 정정

`REF_PARTIAL_01`(첫 행 `[0, 3, 2, 13]`)에서 정순으로 **1**을 첫 빈칸에 두면 첫 행 합이 34가 되지 않아 마방진이 성립하지 않는다. 따라서 올바른 완성은 **역순**(16 → 첫 빈칸, 1 → 둘째 빈칸)이며, 테스트가 기대하는 벡터는 **`[1, 1, 16, 4, 4, 1]`**이다. (과거 명세 초안에 있던 `[1, 1, 1, 4, 4, 16]`은 동일 보드에 대해 수학적으로 성립하지 않는다.)

### 5.3 오류 코드

| 코드 | 용도 |
|------|------|
| `VALIDATION_SHAPE` | 4×4 아님, 비직사각형 행렬 |
| `VALIDATION_RANGE` | 0~16 밖 값 |
| `VALIDATION_BLANKS` | 빈칸(0) 개수 ≠ 2 |
| `VALIDATION_DUPLICATE` | 0 제외 중복 |
| `VALIDATION_TYPE` | 셀이 정수가 아님 |
| `DOMAIN_NO_VALID_PLACEMENT` | 정순·역순 모두 마방진 실패(예: `D008_NO_PLACEMENT` 픽스처) |

---

## 6. 후속 권장 작업(Report 06 정본과의 정렬)

- **Control·Boundary** 전용 테스트(`CompleteMagicSquareUseCase`, CLI 어댑터 등)는 To-Do Phase 6~7에 따라 추가한다.
- **명세 문서 07**의 C-001 예시 벡터를 본 보고서 §5.2와 동일하게 갱신하면 문서·코드 불일치가 제거된다.

---

## 7. 변경 이력

| 일자 | 내용 |
|------|------|
| 2026-04-28 | 최초 작성: 테스트·소스 트리, venv 실행법, TC 매핑, `REF_PARTIAL_01` 계약 메모 반영 |
