# Magic square test case specification
_Exported on 4/28/2026 at 14:21:13 GMT+9 from Cursor (3.2.11)_

---

**User**

@docs/MagicSquare_4x4_TestCase_Specification_Form.md 를 참조해 테스트해 볼 수 있도록 자세하게 다시 작성해줘.

---

**Cursor**

해당 문서와 관련 코드를 읽어 테스트 가능하도록 상세히 재작성합니다.



구현체의 API와 도메인 규칙을 확인해 명세와 일치시킵니다.



PRD에 맞춰 `solution()`은 `int[6]`(1-인덱스) 출력, 빈칸 2개 등을 명세에 반영합니다. `docs/MagicSquare_4x4_TestCase_Specification_Form.md`를 실행 가능한 수준으로 전면 재작성합니다.



B-005 픽스처에서 중복·모순된 설명을 정리합니다.



`Report/07_...`에 동일 본문을 동기화합니다.



작업을 반영했습니다. 요약만 정리합니다.

## 변경 요약

[`docs/MagicSquare_4x4_TestCase_Specification_Form.md`](c:\DEV\MagicSquare_12\docs\MagicSquare_4x4_TestCase_Specification_Form.md)를 **버전 2.0 실행용 상세본**으로 다시 썼습니다. [`docs/PRD.md`](c:\DEV\MagicSquare_12\docs\PRD.md)·[`Report/05_MagicSquare_PRD.md`](c:\DEV\MagicSquare_12\Report\05_MagicSquare_PRD.md)와 맞추었습니다.

### 반영한 내용

1. **도메인·계약** — 빈칸 `0` **정확히 2개**, 값 `0` 또는 1~16, 마방진 합 **34**, 빈칸 순서 **row-major**, 성공 시 **`int[6]` = `[r1,c1,n1,r2,c2,n2]` (좌표 1-기반)** 및 정순/역순 배치 규칙.
2. **좌표 이중 표기** — 내부·단위 테스트는 **0-기반**, 제품 출력은 **1-기반**과 변환 식.
3. **참조 픽스처** — `REF_MS`, `REF_PARTIAL_01`, `REF_PARTIAL_02`에 **리터럴 + 행·열·대각 검산**.
4. **실행 가이드** — `apply_solution` 의사코드, 수동 검산 절차, `pytest` 단언 예시.
5. **TC별** — 입력 행렬, 기대값, 수동 계산, `assert` 예시, PRD와 어긋날 때의 해석(예: A-003~005는 **검증 전 단독** 테스트).
6. **B-005** — 1~16 퍼뮤테이션을 유지하면서 부대각 합 ≠ 34인 **`B005_ANTI_BROKEN`**으로 정리하고, “부대각만 깨진” 구성의 난이도는 **비고**로 명시.
7. **추가 권장 TC** — **D-007**(빈칸 개수 위반), **D-008**(배치 불가 / `DOMAIN_NO_VALID_PLACEMENT`).

동일 본문은 [`Report/07_MagicSquare_4x4_TestCase_Specification_Form.md`](c:\DEV\MagicSquare_12\Report\07_MagicSquare_4x4_TestCase_Specification_Form.md)에도 맞춰 두었고, Report 쪽 **상대 링크**만 Report 기준으로 수정했습니다.

테스트할 때는 문서 §4의 `REF_PARTIAL_01` / `REF_PARTIAL_02`와 §5의 `apply_solution` 흐름만 복사해도 C-001·C-002를 바로 재현할 수 있습니다.

---

**User**

가상환경에서 실행할 수 있도록 방법을 알려줘.

---

**Cursor**

프로젝트에 Python·의존성 정의가 있는지 확인합니다.



지금 저장소에는 `requirements.txt`나 `pyproject.toml`이 없고, README에도 “구현 추가 후”로만 적혀 있습니다. PRD·테스트 명세가 **Python + pytest**를 가정하므로, **Windows PowerShell** 기준으로 가상환경에서 돌리는 일반적인 방법만 정리합니다.

## 1. Python 확인

```powershell
python --version
```

`Python 3.10+` 권장. `python`이 없으면 `py -3.12 --version`처럼 **Windows Python Launcher**를 써도 됩니다.

## 2. 프로젝트 폴더로 이동

```powershell
cd c:\DEV\MagicSquare_12
```

## 3. 가상환경 만들기

```powershell
python -m venv .venv
```

(`py -3.12 -m venv .venv` 도 동일 역할)

## 4. 가상환경 활성화 (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

프롬프트 앞에 `(.venv)`가 붙으면 활성화된 상태입니다.

**실행 정책 오류**가 나면(스크립트 차단), 관리자 없이 현재 사용자만 허용하려면:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

다시 `Activate.ps1`을 실행합니다.

**CMD**를 쓰는 경우:

```cmd
.\.venv\Scripts\activate.bat
```

## 5. pip 업그레이드(선택)

```powershell
python -m pip install --upgrade pip
```

## 6. 테스트 도구 설치

구현·`tests/`가 생기면 최소한:

```powershell
pip install pytest
```

나중에 타입 체크 등을 쓰면 `pip install pytest mypy`처럼 추가하면 됩니다.

## 7. 테스트 실행

```powershell
pytest
```

특정 파일만:

```powershell
pytest tests\test_board.py -v
```

## 8. 비활성화

```powershell
deactivate
```

---

**정리**: 코드와 `tests/`가 아직 없으면 `pytest`는 실패하거나 수집할 테스트가 없을 수 있습니다. 그때는 위 1~5단계까지만 해 두고, 구현이 생기면 6~7을 쓰면 됩니다.  
의존성을 고정하려면 프로젝트 루트에 `requirements.txt`(예: `pytest>=8.0`)를 두고 `pip install -r requirements.txt`로 설치하는 방식이 좋습니다. 원하면 그 파일 초안을 저장소에 추가해 줄 수 있습니다.

---

**User**

테스트 코드를 구현해줘

---

**Cursor**

구현 코드 존재 여부와 To-Do 보고서의 테스트·모듈 구조를 확인합니다.



구현이 없어 테스트가 통과하려면 최소 도메인 로직이 필요합니다. `src/magicsquare`에 로직을 두고 명세·To-Do에 맞춘 `pytest` 테스트를 추가합니다.



역순 전용 케이스와 D008 픽스처를 빠르게 검증합니다.



구현과 테스트를 추가합니다. `REF_PARTIAL_REVERSE_ONLY`는 `[[16,0,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,0]]`이며 기대 출력은 `[1,2,3,4,4,1]`입니다.



명세의 `[1,1,1,4,4,16]`은 행 합이 맞지 않습니다. PRD대로 정순(작은 수→첫 빈칸)을 먼저 시도하고, 마방진이 되지 않으면 역순을 쓰면 기대값은 `[1, 1, 16, 4, 4, 1]`입니다. 테스트를 실제 계약에 맞게 수정합니다.



작업을 반영했습니다. 테스트가 통과하려면 도메인 구현이 필요해 `src/magicsquare`에 최소 로직을 함께 두었습니다.

## 구성

| 경로 | 역할 |
|------|------|
| `src/magicsquare/` | `find_blank_coords`, `is_magic_square`, `solve`, `BoardValidator`, `ValidationError` / `DomainError` |
| `tests/conftest.py` | `REF_MS`, `REF_PARTIAL_*`, `D008_NO_PLACEMENT`, `apply_solution` |
| `tests/test_tc_ms_*.py` | 명세 TC-MS-A~D 대응 |
| `tests/test_board_validator.py` | To-Do `BoardValidatorTest` 이름에 맞춘 검증 테스트 |
| `tests/test_missing_numbers.py` | 누락 수 `(lo, hi)` |
| `pyproject.toml` | `pytest`용 `pythonpath = ["src"]` |
| `requirements-dev.txt` | `pytest>=8.0` |

## 실행

```powershell
cd c:\DEV\MagicSquare_12
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
python -m pytest tests -v
```

현재 **35개 테스트 모두 통과**합니다.

## 참고: `REF_PARTIAL_01` 기대 출력

정순(1→첫 빈칸 `(0,0)`, 16→둘째)으로는 첫 행 합이 34가 되지 않아 **역순만** 마방진이 됩니다. PRD의 “정순 시도 후 역순”과 맞게 `solve(REF_PARTIAL_01)` 결과는 **`[1, 1, 16, 4, 4, 1]`**이며, 예전 명세에 있던 `[1, 1, 1, 4, 4, 16]`은 수학적으로 맞지 않아 테스트·구현은 **실제로 성립하는 배치**를 기준으로 했습니다.

---

**User**

가상환경에서 실행 방법을 알려줘.

---

**Cursor**

이 저장소 기준으로 **Windows PowerShell**에서 가상환경을 만들고 테스트까지 돌리는 방법입니다.

## 1. 프로젝트로 이동

```powershell
cd c:\DEV\MagicSquare_12
```

## 2. 가상환경 생성

```powershell
python -m venv .venv
```

(`python`이 없으면 `py -3.12 -m venv .venv` 처럼 시도)

## 3. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

프롬프트 앞에 `(.venv)`가 보이면 활성화된 상태입니다.

**실행 정책 오류**가 나면:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 4. 의존성 설치

```powershell
pip install --upgrade pip
pip install -r requirements-dev.txt
```

## 5. 테스트 실행

```powershell
python -m pytest tests -v
```

`pyproject.toml`에 `pythonpath = ["src"]`가 있어서 **저장소 루트에서** 위처럼 실행하면 됩니다.

## 6. 비활성화

```powershell
deactivate
```

---

**CMD**를 쓰는 경우: `.\.venv\Scripts\activate.bat` 로 활성화하면 됩니다.

---

**User**

실행해줘

---

**Cursor**

가상환경에서 테스트 실행 중입니다.



실행했습니다.

- **`.venv`**가 없어서 만들었고, `requirements-dev.txt`로 `pytest`를 설치한 뒤  
- **`python -m pytest tests -v`** 를 `.venv`의 Python으로 돌렸습니다.

**결과: 35 passed** (약 0.09초)

다음에 직접 돌릴 때는 활성화 후:

```powershell
cd c:\DEV\MagicSquare_12
.\.venv\Scripts\Activate.ps1
python -m pytest tests -v
```

---

**User**

Report 폴더에 보고서로 내보내줘.

---

**Cursor**

Report 폴더의 보고서 번호 체계를 확인한 뒤, 테스트 구현·실행 방법을 정리한 보고서를 추가합니다.



`Report` 폴더에 아래 보고서를 추가했습니다.

**파일**: [`Report/10_MagicSquare_4x4_Test_Implementation_Report.md`](c:\DEV\MagicSquare_12\Report\10_MagicSquare_4x4_Test_Implementation_Report.md)

**포함 내용**
- 문서 개요·관련 Report 링크(01·05·06·07, `docs` 명세)
- `src/magicsquare`·`tests`·`pyproject.toml`·`requirements-dev.txt` 구조 표
- **가상환경 생성·활성화·`pytest` 실행** PowerShell 절차
- 최근 **35 passed** 실행 스냅샷
- **TC-MS-A~D** ↔ 테스트 파일 매핑, `BoardValidator`·누락 수 테스트
- PRD 정렬 메모(`solve` 출력, **정순→역순**, `REF_PARTIAL_01` 기대 벡터 `[1,1,16,4,4,1]` 및 명세 정정 안내)
- 오류 `code` 표
- Report 06과의 후속 정렬 권장(Control·Boundary 테스트, 07 문서 갱신)

번호는 기존 `07` 다음으로 **`10`**을 사용했습니다(저장소 `Report`에 08·09 파일이 없어 공번을 두었습니다).

