# Git branching strategy for README.md
_Exported on 4/28/2026 at 13:42:45 GMT+9 from Cursor (3.2.11)_

---

**User**

@README.md 작업을 하려고 하는데, 깃 브랜치 전략을 어떻게 하면 좋을지 알려줘.

---

**Cursor**

README.md를 읽어 프로젝트 맥락을 파악한 뒤 브랜치 전략을 제안합니다.



README 기준으로 보면 **Epic → US → TASK**가 이미 잘 쪼개져 있어서, 브랜치도 그 흐름에 맞추면 추적이 쉽습니다.

## 1. 기본 줄기

| 브랜치 | 역할 |
|--------|------|
| **`main`** | 항상 빌드·테스트 통과하는 상태. 문서만 있을 때는 “초기 상태”로 두고, 구현이 붙으면 여기로만 머지. |
| **`develop` (선택)** | 혼자 작업·PR 없으면 생략해도 됩니다. 팀이거나 릴리즈 전에 안정화 구간이 필요할 때만 두세요. |

혼자 학습이면 **`main` + 기능 브랜치**만으로도 충분합니다.

## 2. 기능 브랜치 이름 (README와 맞추기)

TASK ID가 정본이므로 브랜치에 붙이면 커밋·PR·To-Do와 1:1에 가깝습니다.

- **US 단위(권장 시작점)**  
  - `feature/us-002-board-validation`  
  - `feature/us-005-magic-judge-placement`  
  한 US 안에 여러 TASK가 있어도 한 브랜치에서 RED→GREEN→REFACTOR를 연속으로 해도 됩니다.

- **TASK가 크거나 중간에 멈출 수 있을 때**  
  - `feature/task-004-board-validator-shape`  
  작은 단위로 PR/리뷰를 나누고 싶을 때.

- **스캐폴딩만 먼저**  
  - `feature/task-000-scaffolding`  
  README의 Phase 0(TASK-000)과 맞습니다.

README의 **구현 순서 힌트**(Logic → Control → Boundary/UI)를 따른다면, 브랜치도 대략 **US-002 → US-003 → … → US-007 → US-006/US-008** 순으로 열고 머지하면 의존성과 맞습니다.

## 3. 커밋 메시지와의 연결 (선택)

커밋에 TASK를 적어 두면 나중에 traceability에 도움이 됩니다.

- `TASK-004-1: RED — BoardValidator non-4x4`
- `TASK-004-2: GREEN — validateShape`

## 4. 머지 방식

- **Fast-forward / Squash merge**: 학습용·혼자면 둘 다 OK. 히스토리를 깔끔히 남기려면 squash, 실습 과정을 그대로 보려면 일반 merge.
- **작은 PR 단위**: US 하나 또는 TASK 몇 개씩 머지하면 리뷰·롤백이 쉽습니다.

## 5. 요약 추천

- **`main`은 항상 녹색**(테스트 도입 후에는 CI 또는 로컬에서 `test` 통과 후 머지).
- 브랜치는 **`feature/us-0xx-짧은-영문-설명`** 또는 **`feature/task-0xx-...`** 중 하나로 통일.
- 첫 구현은 **`feature/task-000-scaffolding`** 또는 **`feature/us-001-entity`**처럼 README Phase/US 순서대로 시작.

팀 규모(혼자 vs 여러 명)와 PR을 쓸지 여부를 알려주시면, `develop` 유무와 브랜치를 US 단위로 묶을지 TASK 단위로 쪼갤지까지 더 좁혀서 적어 드리겠습니다.

---

**User**

우선, red 브랜치를 만들어줘.

---

**Cursor**

`red` 브랜치 생성 중입니다.



작업했습니다.

- **`red`** 브랜치를 `main`에서 만들었고, 지금 체크아웃된 브랜치가 `red`입니다.

확인하려면:

```powershell
git branch
```

`main`으로 돌아가려면:

```powershell
git switch main
```

---

**User**

을

테스테스트 케이스	프로젝트명	
	대상 시스템	
단계		작성자		승인자		문서 상태	
작성일		버전		테스트 범위		테스트 조직	
테스트 ID			테스트 일자	
테스트 목적	
테스트 기능	
입력값	
테스트단계					
					
					
					
					
					
					
					
					
					
					
					
	
테스트환경	
전제 조건	
성공 /실패 기준	
특별하게 필요한 절차	


의 양식에 맞춰서 작성해줘.

---

**Cursor**

이미지와 프로젝트 보고서를 확인해 양식에 맞춰 문서를 작성합니다.



이미지 명세의 21개 TC를 사용자 양식에 맞춰 정리합니다. 이미지 해상도로 일부 셀 문구는 표준 Given/When/Then으로 보완합니다.



스프레드시트 이미지의 **21개 TC**를 요청하신 항목 구조에 맞춰 풀어서 저장했습니다.

**파일:** [`Report/07_MagicSquare_4x4_TestCase_Specification_Form.md`](Report/07_MagicSquare_4x4_TestCase_Specification_Form.md)

**구성 요약**

1. **문서 공통** — 테스트 케이스·프로젝트명·대상 시스템·단계·작성자·승인자·문서 상태·작성일·버전·테스트 범위·테스트 조직을 표로 정리했습니다.  
2. **공통 블록** — 테스트환경, 전제 조건, 공통 특별 절차(우선순위·좌표 체계·본 저장소 REQ와의 정렬 주의).  
3. **TC별 블록** — 각 TC마다 **테스트 ID**, **테스트 일자**(실행 시 기재), **테스트 목적**, **테스트 기능**, **입력값**, **테스트단계**(Given/When/Then 표), **테스트환경**, **전제 조건**, **성공/실패 기준**, **특별하게 필요한 절차**를 채웠습니다.  
4. **부록** — TC ID 색인과 `06` To-Do와의 연계 안내.

원본 표의 일부 셀은 해상도상 문구가 불명확해, **Given/When/Then**은 이미지 설명과 일반적인 BDD 형태로 통일해 두었습니다. 좌표는 **0-based (행, 열)** 가정을 적어 두었고, 구현이 1-based이면 해당 TC만 치환하면 됩니다.  
또한 README의 **“빈칸 정확히 2개”** 규칙과 이미지의 A/C 일부 TC가 어긋날 수 있어, 공통 특별 절차와 C-001 등에 **도메인 계약에 맞게 기대값을 조정하라**는 주석을 넣었습니다.

작성자·승인자·테스트 조직은 `(작성)` 등 placeholder로 두었으니 조직 양식에 맞게 바꾸시면 됩니다.

---

**User**

https://github.com/YejiAhn/MagicSquare_12.git 에 작업한 내용 올려줘

---

**Cursor**

원격 저장소 설정과 작업 트리 상태를 확인한 뒤 푸시합니다. 토큰으로 보이는 파일은 커밋에서 제외합니다.



`main`과 `red`는 동일 커밋이며, 미추적 작업은 `docs/` 폴더뿐입니다. `docs/` 내용을 확인한 뒤 커밋하고 `red` 브랜치를 푸시합니다.



`docs/`에 테스트 명세 등이 있습니다. 커밋한 뒤 `red`와 `main`에 반영해 원격에 푸시합니다.



---

**User**

main 에 푸쉬하지 말고 red 에만 올려줘

---

**Cursor**

`red` 브랜치만 원격에 푸시합니다.



여기 실행 환경에서는 `github.com`으로 연결이 되지 않아 **원격 푸시는 실패**했습니다. 로컬 저장소 상태는 요청하신 대로입니다.

**현재 상태**

- **`main`**: `f5618f1` — `docs/` 추가 커밋 없음  
- **`red`**: `81b7866` — `docs/`(테스트 명세, PRD, TODO) 포함  
- **`main`에는 푸시하지 않음** — 이전에도 merge/push는 적용되지 않았습니다.

**PC에서 직접 푸시할 때 (`red`만)**

```powershell
cd c:\DEV\MagicSquare_12
git checkout red
git push -u origin red
```

이후 GitHub에서는 브랜치를 `red`로 바꿔 확인하면 됩니다: [YejiAhn/MagicSquare_12](https://github.com/YejiAhn/MagicSquare_12.git).

인증이 필요하면 GitHub CLI(`gh auth login`) 또는 자격 증명 관리자로 HTTPS 로그인을 맞춰 주세요.

---

**User**

내가 작업한 docs/ 파일들이 왜 안 나와? 이거 red 브랜치에 올려야 되는데

---

**Cursor**

로컬 Git 상태와 `docs/` 폴더를 확인합니다.



원인은 **`docs/`가 커밋에 없어서가 아니라**, GitHub에는 **`red` 브랜치 자체가 아직 없기 때문**에 그렇게 보이는 겁니다.

### 로컬에서는 이미 `red`에 들어가 있음

- 브랜치: **`red`**
- 커밋: `81b7866` — *Add docs: 4x4 test case specification form, PRD, and TODO notes.*
- 그 커밋에 포함된 파일:
  - `docs/MagicSquare_4x4_TestCase_Specification_Form.md`
  - `docs/PRD.md`
  - `docs/TODO.md`

`git ls-tree`로 확인했을 때 위 세 파일이 **`red`에 정상 추적**되어 있습니다.

### GitHub에서 안 보이는 이유

원격에는 지금 **`origin/main`만** 있고 **`origin/red`가 없습니다**.  
이전에 여기서 `git push origin red`를 시도했을 때 **네트워크 오류로 푸시가 실패**했기 때문에, GitHub 저장소에는 `red`가 한 번도 올라가지 않은 상태로 보는 게 맞습니다.

그래서 GitHub 기본 화면(**`main`**)만 보면 `docs/`가 없고, **`red` 브랜치로 바꿔도** 아직 원격에 `red`가 없으면 역시 안 나옵니다.

### 해결 방법

로컬에서 네트워크·인증이 되는 환경에서 한 번만 실행하세요.

```powershell
cd c:\DEV\MagicSquare_12
git checkout red
git push -u origin red
```

푸시가 끝나면 GitHub에서 브랜치를 **`red`**로 선택하면 `docs/`가 보입니다.

---

**정리:** 파일이 빠진 게 아니라 **`red`를 원격에 올리는 푸시가 아직 성공하지 않은 상태**입니다. `main`에는 의도적으로 `docs` 커밋을 넣지 않았으므로, `main`만 보면 계속 안 나오는 것이 정상입니다.

---

**User**

Reports 폴더에 보고서로 내보내줘.

---

**Cursor**

`docs/` 내용을 `Report/` 폴더의 보고서 번호 체계에 맞춰 옮깁니다. 기존 `Report/`와 `docs/` 파일을 확인합니다.



`docs/`의 세 파일을 `Report/`에 번호 체계(07–09)로 복사하고, `Report` 기준으로 문서 역할·링크를 정리합니다. `README.md` 문서 목록에 항목을 추가합니다.



프로젝트에는 **`Report` 폴더**(복수 `Reports` 아님)가 있어서, 그쪽에 보고서로 반영했습니다.

### 추가·반영된 파일 (`Report/`)

| 파일 | 내용 |
|------|------|
| [`Report/07_MagicSquare_4x4_TestCase_Specification_Form.md`](Report/07_MagicSquare_4x4_TestCase_Specification_Form.md) | `docs`의 테스트 케이스 명세 전체 복사 + 상단에 Report 정본 안내 |
| [`Report/08_MagicSquare_PRD_Summary_Report.md`](Report/08_MagicSquare_PRD_Summary_Report.md) | `docs/PRD.md`와 같은 요약을 Report 링크 기준으로 정리 |
| [`Report/09_MagicSquare_Implementation_Todo_Summary_Report.md`](Report/09_MagicSquare_Implementation_Todo_Summary_Report.md) | `docs/TODO.md`와 같은 To-Do 요약을 Report 링크 기준으로 정리 |

### 기타

- [`README.md`](README.md)의 **문서 목록** 표에 07·08·09 행을 넣었습니다.
- [`docs/PRD.md`](docs/PRD.md), [`docs/TODO.md`](docs/TODO.md), [`docs/MagicSquare_4x4_TestCase_Specification_Form.md`](docs/MagicSquare_4x4_TestCase_Specification_Form.md)에는 각각 대응하는 **Report 경로**를 한 줄씩 적어 두었습니다.

이제 근거 문서는 **`Report/`**를 기준으로 보시면 됩니다. `git add Report/ README.md docs/` 후 커밋하시면 됩니다.

