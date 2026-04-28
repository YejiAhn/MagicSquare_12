# MagicSquare 4x4

부분적으로 비어 있는 **4x4 Magic Square**(빈칸 `0` 두 칸)를 입력으로 받아, 도메인 규칙을 만족하면 빈칸을 채우고, 위반 시 거부하는 **완성 시스템**을 구현하기 위한 학습용 저장소입니다.  
요구사항·여정·TDD·구현 To-Do는 [`Report/`](Report/) 폴더의 보고서로 정리되어 있습니다.

## 이 프로젝트의 목표

- **Invariant·계약**을 먼저 고정하고, **Dual-Track(UI + Logic) TDD**로 구현한다.
- **ECB(Entity / Control / Boundary)**로 책임을 나누고, 비즈니스 규칙은 **Logic**에만 둔다.
- 작업은 **To-Do → Scenario(L0~L3) → Test → Code**로 추적 가능하게 유지한다.

## 도메인 규칙(요약)

| 항목 | 규칙 |
|------|------|
| 크기 | 4x4 |
| 숫자 | 1~16, `0`은 빈칸 |
| 빈칸 | 정확히 2칸 |
| 중복 | `0`을 제외한 중복 불가 |
| 완성 판정 | 모든 행·열·대각선의 합 **34** |
| 비정상 보드 | 거부 |

자세한 정의는 [문제 정의 보고서](Report/01_4x4_Magic_Square_Problem_Definition_Report.md)와 [PRD](Report/05_MagicSquare_PRD.md)를 참고하세요.

## 문서 목록

| 문서 | 용도 |
|------|------|
| [01 — 문제 정의](Report/01_4x4_Magic_Square_Problem_Definition_Report.md) | 불변조건·문제 정의 |
| [02 — Dual-Track TDD](Report/02_MagicSquare_4x4_DualTrack_TDD_Report.md) | 도메인 구성·RED 테스트 목록·UI/Logic 트랙 |
| [03 — Cursor 규칙](Report/03_MagicSquare_CursorRules_Report.md) | 에디터/AI 가이드 |
| [04 — 사용자 여정](Report/04_MagicSquare_User_Journey_Report.md) | Epic·여정·User Story·Gherkin |
| [05 — PRD](Report/05_MagicSquare_PRD.md) | 제품 요구사항·범위·계약 |
| [**06 — 구현용 To-Do**](Report/06_MagicSquare_4x4_Implementation_Todo_Report.md) | **TASK-000~045 전체**(Scenario·Test·Code·ECB) |

## 빌드 및 실행

구현 코드와 빌드 도구(`package.json`, `pom.xml` 등)가 추가되면 이 섹션에 설치·테스트·실행 명령을 적습니다.

```bash
# 예시 (도구 확정 후 수정)
# npm test
# mvn test
```

## 구현 To-Do (체크박스 · 단계별 번호 · Requirements 추적)

작업 ID·시나리오 레벨·테스트·코드 대상의 **정본**은 [**06 — 구현용 To-Do 보고서**](Report/06_MagicSquare_4x4_Implementation_Todo_Report.md)와 동일하게 맞춰 두었습니다. README에서는 **실습 보드**로 빠르게 밟을 수 있게 계층만 펼쳐 놓았습니다.

### 추적 규칙 (한 줄)

**Task → Req → Scenario(L0~L3) → Test → Code (ECB)** 링크를 유지하면 Concept-to-Code Traceability입니다. 하위 `TASK-xxx-n`은 **RED → GREEN → REFACTOR** 순서를 강제하는 단계 번호입니다.

### Req ID와 Invariant 대응(요약)

| Req ID | 의미(불변조건·요구와 대응) |
|--------|---------------------------|
| REQ-ARCH | 패키지·오류 코드·추적 매트릭스 초안 |
| REQ-I01 | 4x4 형태 |
| REQ-I02 | 빈칸(0) 정확히 2개 |
| REQ-I03 | 값 범위 0 및 1~16 |
| REQ-I04 | 0 제외 중복 없음 |
| REQ-I05 | 빈칸 좌표 고정 순서(row-major) |
| REQ-I06 | 1~16 누락 두 수·오름차순 |
| REQ-I07 | 마방진 합 34 판정 |
| REQ-I08 | 두 빈칸에 두 수 배치·정순 우선·역순 폴백 |
| REQ-UC | Control 유스케이스(검증 선행·단계 격리) |
| REQ-IO | Boundary 파싱·오류 메시지 매핑(규칙 없음) |
| REQ-UI | UI-Track: 수집·표시만 |
| REQ-QA | 커버리지·매트릭스·회귀 |

---

## Epic-001: Invariant 기반 4x4 Magic Square 완성 시스템

- [ ] **Epic-001** — 부분 보드 입력 → 규칙 충족 시 완성 / 위반 시 거부. Logic-Track + UI-Track 병렬, **규칙은 Logic에만**.

### US-000: Phase 0 — 계약·스캐폴딩 (REQ-ARCH)

- [ ] **TASK-000** ECB 경계·오류 코드·추적 문서 초안 (`docs/traceability.md` 등)
  - [ ] TASK-000-1 **REFACTOR** — 패키지/모듈 구조·`ErrorCode`·유스케이스 인터페이스 스켈레톤
  - **체크포인트**: Invariant ↔ Task ID 매트릭스 초안 1페이지 이상

### US-001: 보드 표현 및 생성 (Entity · REQ-I01)

- [ ] **TASK-001** `MagicSquare4x4` Entity — 4x4 그리드 보유
  - [ ] TASK-001-1 **RED** — `MagicSquare4x4Test.should_hold_4x4_matrix`
  - [ ] TASK-001-2 **GREEN** — `MagicSquare4x4` / `fromGrid`
  - [ ] TASK-001-3 **REFACTOR** — 불변·방어적 복사 (`should_defensively_copy_source_grid`)

### US-002: 보드 유효성 검사 (Logic · REQ-I01~I04)

- [ ] **TASK-004** `BoardValidator` — 4x4 아님 거부
  - [ ] TASK-004-1 **RED** — `BoardValidatorTest.should_reject_non_4x4`
  - [ ] TASK-004-2 **GREEN** — `validateShape`
- [ ] **TASK-006** 값 범위(0, 1~16) 위반 거부
  - [ ] TASK-006-1 **RED** — `should_reject_out_of_range_values`
  - [ ] TASK-006-2 **GREEN** — `validateValueRange`
- [ ] **TASK-008** 빈칸 개수 ≠ 2 거부
  - [ ] TASK-008-1 **RED** — `should_reject_invalid_blank_count`
  - [ ] TASK-008-2 **GREEN** — `validateBlankCount`
- [ ] **TASK-010** 0 제외 중복 거부
  - [ ] TASK-010-1 **RED** — `should_reject_duplicate_non_zero`
  - [ ] TASK-010-2 **GREEN** — `validateNoDuplicateNonZero`
- [ ] **TASK-012** 검증 파이프라인·오류 코드 정리
  - [ ] TASK-012-1 **REFACTOR** — 단일 진입점·`ValidationResult` / `DomainError`

### US-003: 빈칸 탐지 (Logic · REQ-I02·I05)

- [ ] **TASK-013** `BlankLocator` + `CellPosition`(VO)
  - [ ] TASK-013-1 **RED** — `BlankLocatorTest.should_return_two_positions_in_row_major_order`
  - [ ] TASK-013-2 **GREEN** — `BlankLocator.locate`
- [ ] **TASK-015** 선결 조건 위반 시 실패(또는 Control에서 선차단)
  - [ ] TASK-015-1 **RED** — `should_fail_if_preconditions_not_met`
  - [ ] TASK-015-2 **GREEN**

### US-004: 후보값(누락 숫자) 산출 (Logic · REQ-I06)

- [ ] **TASK-017** `MissingNumbersFinder` + `MissingNumbersPair`
  - [ ] TASK-017-1 **RED** — `MissingNumbersFinderTest.should_find_sorted_missing_pair`
  - [ ] TASK-017-2 **GREEN** — `find`
- [ ] **TASK-019** 누락 쌍 비확정 시 거부
  - [ ] TASK-019-1 **RED** — `should_reject_when_pair_not_uniquely_determined`
  - [ ] TASK-019-2 **GREEN**

### US-005: 마방진 판정·완성 배치 (Logic · REQ-I07·I08)

- [ ] **TASK-021** `MagicSquareJudge` — 합 34 판정
  - [ ] TASK-021-1 **RED** — `MagicSquareJudgeTest.should_validate_magic_constant_34`
  - [ ] TASK-021-2 **GREEN** — `isMagic`
- [ ] **TASK-023** `DualPlacementResolver` — 정순(작은 수→첫 빈칸) 우선
  - [ ] TASK-023-1 **RED** — `DualPlacementResolverTest.should_resolve_with_forward_order_first`
  - [ ] TASK-023-2 **GREEN** — `resolve`
- [ ] **TASK-025** 역순 폴백
  - [ ] TASK-025-1 **RED** — `should_fallback_to_reverse_order`
  - [ ] TASK-025-2 **GREEN**
- [ ] **TASK-027** 두 조합 모두 실패 시 도메인 실패
  - [ ] TASK-027-1 **RED** — `should_fail_when_no_valid_placement`
  - [ ] TASK-027-2 **GREEN**
- [ ] **TASK-029** 배치·판정 중복 제거
  - [ ] TASK-029-1 **REFACTOR** — `DualPlacementResolver` / `MagicSquareJudge` 회귀 전부 통과

### US-006: 잘못된 입력·오류 표현 (Boundary · REQ-IO)

- [ ] **TASK-035** `StdioMagicSquareAdapter` — 파싱만(규칙 판단 금지)
  - [ ] TASK-035-1 **RED** — `StdioMagicSquareAdapterTest.should_fail_on_malformed_input`
  - [ ] TASK-035-2 **GREEN** — `parse`
- [ ] **TASK-037** `ErrorPresenter` — 도메인 코드→문자열
  - [ ] TASK-037-1 **RED** — `ErrorPresenterTest.should_map_domain_codes_to_messages`
  - [ ] TASK-037-2 **GREEN**

### US-007: Control 유스케이스 조율 (REQ-UC)

- [ ] **TASK-030** `CompleteMagicSquareUseCase` + `CompletionResult`
  - [ ] TASK-030-1 **RED** — `CompleteMagicSquareUseCaseTest.should_return_completed_board_on_happy_path`
  - [ ] TASK-030-2 **GREEN** — `execute`
- [ ] **TASK-032** 검증 실패 시 해결 단계 미실행
  - [ ] TASK-032-1 **RED** — `should_short_circuit_on_validation_failure`
  - [ ] TASK-032-2 **GREEN**
- [ ] **TASK-034** DI·인터페이스
  - [ ] TASK-034-1 **REFACTOR** — 테스트 더블 용이

> **구현 순서 힌트**: 도메인 Logic(US-002~005)을 먼저 두고 **Control(US-007)**으로 묶은 뒤, **Boundary(US-006)**·**UI(US-008)**를 얹으면 의존성이 단순해집니다.

### US-008: UI-Track (Boundary · REQ-UI)

- [ ] **TASK-039** 콘솔/UI에서 16칸 수집 → Boundary 전달 (**합·중복 계산 없음**)
  - [ ] TASK-039-1 **RED** — `MagicSquareConsoleUiTest.should_collect_sixteen_cells_without_domain_rules`
  - [ ] TASK-039-2 **GREEN**
- [ ] **TASK-041** 완성 보드 출력(포맷만)
  - [ ] TASK-041-1 **RED** — `should_render_completed_grid`
  - [ ] TASK-041-2 **GREEN**
- [ ] **TASK-043** `Application` / `main` — UI→Control 와이어링만
  - [ ] TASK-043-1 **REFACTOR** — `ApplicationSmokeTest.should_wire_ui_to_control`

### US-009: 품질·추적성 (REQ-QA)

- [ ] **TASK-044** 테스트 커버리지 게이트(Logic 핵심 패키지 목표치)
  - **체크포인트**: Domain Logic 커버리지 ≥ 팀 목표(예: 95%) · L3 시나리오마다 최소 1 테스트
- [ ] **TASK-045** Concept-to-Code 매트릭스 완성 (`docs/traceability.md`)
  - **체크포인트**: Epic / US / TASK / Req / Test 클래스가 서로 링크 가능

---

### Requirements 추적 매트릭스 (요약)

구현이 진행되면 **상태** 열을 업데이트합니다. (⬜ TODO · 🔴 RED 실패 중 · 🟢 GREEN 통과 · ✅ 완료)

| Task ID | Req ID | Scenario | 테스트(예) | ECB | 상태 |
|---------|--------|----------|-------------|-----|------|
| TASK-000 | REQ-ARCH | L0 | (팀 정책) | 문서/경계 | ⬜ |
| TASK-001 | REQ-I01 | L1 | `MagicSquare4x4Test.should_hold_4x4_matrix` | Entity | ⬜ |
| TASK-004 | REQ-I01 | L3 | `BoardValidatorTest.should_reject_non_4x4` | Logic | ⬜ |
| TASK-006 | REQ-I03 | L2/L3 | `should_reject_out_of_range_values` | Logic | ⬜ |
| TASK-008 | REQ-I02 | L2/L3 | `should_reject_invalid_blank_count` | Logic | ⬜ |
| TASK-010 | REQ-I04 | L3 | `should_reject_duplicate_non_zero` | Logic | ⬜ |
| TASK-013 | REQ-I05 | L1 | `BlankLocatorTest.should_return_two_positions_in_row_major_order` | Logic | ⬜ |
| TASK-017 | REQ-I06 | L1 | `MissingNumbersFinderTest.should_find_sorted_missing_pair` | Logic | ⬜ |
| TASK-021 | REQ-I07 | L1 | `MagicSquareJudgeTest.should_validate_magic_constant_34` | Logic | ⬜ |
| TASK-023 | REQ-I08 | L1 | `DualPlacementResolverTest.should_resolve_with_forward_order_first` | Logic | ⬜ |
| TASK-025 | REQ-I08 | L2 | `should_fallback_to_reverse_order` | Logic | ⬜ |
| TASK-027 | REQ-I08 | L3 | `should_fail_when_no_valid_placement` | Logic | ⬜ |
| TASK-030 | REQ-UC | L1 | `CompleteMagicSquareUseCaseTest.should_return_completed_board_on_happy_path` | Control | ⬜ |
| TASK-032 | REQ-UC | L3 | `should_short_circuit_on_validation_failure` | Control | ⬜ |
| TASK-035 | REQ-IO | L3 | `StdioMagicSquareAdapterTest.should_fail_on_malformed_input` | Boundary | ⬜ |
| TASK-037 | REQ-IO | L3 | `ErrorPresenterTest.should_map_domain_codes_to_messages` | Boundary | ⬜ |
| TASK-039 | REQ-UI | L1 | `MagicSquareConsoleUiTest.should_collect_sixteen_cells_without_domain_rules` | Boundary | ⬜ |
| TASK-041 | REQ-UI | L1 | `should_render_completed_grid` | Boundary | ⬜ |
| TASK-043 | REQ-UI | L0 | `ApplicationSmokeTest.should_wire_ui_to_control` | Boundary | ⬜ |
| TASK-044 | REQ-QA | L0 | CI 커버리지 임계값 | (도구) | ⬜ |
| TASK-045 | REQ-QA | L0 | 리뷰/아키텍처 테스트 | (문서) | ⬜ |

**전체 Task·세부 RED/GREEN/REFACTOR·추가 테스트 행**: [06 — 구현용 To-Do 보고서](Report/06_MagicSquare_4x4_Implementation_Todo_Report.md)의 §8 Phase별 Task 목록과 **동일 번호 체계**입니다.

> **Traceability**: `Task → Req → Scenario → Test → Code(ECB)` 이 한 줄이 곧 C2C(Concept-to-Code) 실습입니다. UI-Track 작업(TASK-039~043)에는 **마방진 규칙을 넣지 않습니다.**

## 참고

- 프롬프트·대화보내기 원본은 [`Prompting/`](Prompting/)에 있습니다. 근거 문서로는 **`Report/`**를 우선하세요.
