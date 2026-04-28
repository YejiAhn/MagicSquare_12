# MagicSquare 4x4 구현용 To-Do 보고서

## 1. 문서 개요

- **문서명**: MagicSquare 4x4 완성 시스템 — 구현용 To-Do 구조
- **프로젝트명**: MagicSquare
- **방법론**: Concept-to-Code Traceability, Dual-Track UI + Logic TDD, ECB(Entity / Control / Boundary), RED → GREEN → REFACTOR
- **문서 목적**: 부분적으로 비어 있는 4x4 Magic Square 완성 시스템 개발 시, **To-Do → Scenario → Test → Code**로 추적 가능한 작업 보드를 제공한다.
- **관련 문서**: `01_4x4_Magic_Square_Problem_Definition_Report.md`, `02_MagicSquare_4x4_DualTrack_TDD_Report.md`, `04_MagicSquare_User_Journey_Report.md`, `05_MagicSquare_PRD.md`

## 2. 도메인 규칙(요약)

- 보드는 **4x4**이다.
- 숫자는 **1~16**만 사용한다.
- **0**은 빈칸이다.
- **정확히 2칸**이 비어 있다.
- **0을 제외한 중복 숫자**는 허용되지 않는다.
- 모든 행, 열, 대각선의 합은 **34**여야 한다(완성 판정 시).
- 해결 가능한 경우 빈칸 값을 찾아 채운다.
- 유효하지 않은 보드는 **거부**한다.

## 3. ECB 및 Dual-Track 제약

| 역할 | 책임 |
|------|------|
| **Entity** | 보드 상태 및 값 객체(좌표, 누락 쌍 등) 표현 |
| **Control** | 검증과 해결 **흐름 조율**(유스케이스). 비즈니스 규칙은 Logic에 위임 |
| **Boundary** | 입출력·표시·파싱·오류 메시지 매핑. **비즈니스 규칙(합 34, 중복 등) 금지** |
| **Logic** | 검증기, 빈칸/누락 탐색, 마방진 판정, 배치 해결 등 순수 도메인 연산(ECB 문서에서는 Control이 호출하는 하위 계층으로 명시) |

- **Logic-Track**: 도메인·유스케이스(Control)·단위/통합 테스트
- **UI-Track**: 입력 수집·결과 표시·Boundary; 규칙은 넣지 않음

## 4. Scenario Level 정의

| 레벨 | 의미 |
|------|------|
| **L0** | 기능 개요 |
| **L1** | 정상 흐름 |
| **L2** | 경계 상황 |
| **L3** | 실패 상황 |

## 5. 추적 원칙

**Concept → User Story → Task → Scenario(L0~L3) → Test → Code**

각 Task는 **RED / GREEN / REFACTOR** 중 하나로 구분한다.

---

## 6. Epic

- [ ] **Epic-001 — Invariant 기반 4x4 Magic Square 완성 시스템**
  - **목표**: 부분 채움 보드(0=빈칸 2개)를 입력으로 받아, 도메인 규칙을 만족하면 빈칸을 채운 결과를 반환하고, 위반 시 거부한다.
  - **Dual-Track**: Logic-Track과 UI-Track을 병렬로 진행하되, **규칙은 Logic에만** 둔다.
  - **완료 개념**: 각 Task가 L0~L3 시나리오, 테스트 이름, 대상 코드까지 역추적 가능.

---

## 7. User Story

- [ ] **US-001 — 보드 표현 및 생성**  
  As a 개발자, I want 4x4 보드 상태를 Entity로 표현하고 생성하고 싶다, So that 이후 검증·탐색이 동일 계약으로 동작한다.

- [ ] **US-002 — 보드 유효성 검사**  
  As a 시스템, I want 형태·값 범위·빈칸 개수·중복을 검증하고 싶다, So that 비정상 보드가 해결 로직으로 넘어가지 않는다.

- [ ] **US-003 — 빈칸 탐지**  
  As a 시스템, I want 정확히 두 개의 0 좌표를 고정 순서로 얻고 싶다, So that 배치 시도가 결정적이다.

- [ ] **US-004 — 후보값(누락 숫자) 산출**  
  As a 시스템, I want 1~16 중 누락된 두 수를 오름차순으로 얻고 싶다, So that 유효 보드에서 후보 조합이 명확해진다.

- [ ] **US-005 — 완성(배치) 및 마방진 판정**  
  As a 시스템, I want 두 후보를 두 빈칸에 시도하고 행/열/대각 합 34를 만족하는지 판정해 결과를 내고 싶다, So that 해결 가능한 경우에만 완성된 값을 확정한다.

- [ ] **US-006 — 잘못된 입력 처리**  
  As a 사용자/학습자, I want 명확한 오류로 거부되길 원한다, So that Boundary는 사유 코드만 전달하고 UI는 메시지를 표시한다.

- [ ] **US-007 — Control을 통한 유스케이스 완결**  
  As a 시스템, I want 검증→탐색→후보→시도→응답이 한 흐름으로 묶이길 원한다, So that UI는 Control만 호출한다.

- [ ] **US-008 — UI·Boundary(I/O)**  
  As a 사용자, I want 보드를 입력하고 결과/오류를 보고 싶다, So that UI에 마방진 규칙을 넣지 않고 표현만 한다.

- [ ] **US-009 — 품질·추적성**  
  As a 팀, I want 커버리지와 Concept-to-Code 매트릭스를 유지하고 싶다, So that 회귀와 교육 목표를 만족한다.

---

## 8. Phase별 Task 목록

### Phase 0 — 개념·계약·스캐폴딩 (Concept-to-Code Traceability)

- [ ] **TASK-000**
  - **단계**: REFACTOR(문서/코드 골격)
  - **작업 제목**: 도메인 용어·오류 코드·패키지 구조를 ECB로 고정(추적 매트릭스 초안)
  - **Scenario Level**: **L0**
  - **연결 Test**: `TraceabilityMatrixTest`(플레이스홀더) 또는 팀 정책에 맞는 단일 검증 수단
  - **연결 Code**: `docs/traceability.md` 또는 `package-info` / `ErrorCode` enum
  - **ECB**: Boundary(공개 계약)·Control(유스케이스 인터페이스)·Entity(타입) 경계 정의
  - **체크포인트**: Invariant 목록이 Task ID와 1:1 대응 초안 완료

### Phase 1 — Entity: 보드 생성 (US-001)

- [ ] **TASK-001**
  - **단계**: RED
  - **작업 제목**: `MagicSquare4x4` 생성 — 정상 4x4 원시 배열을 보유
  - **Scenario Level**: **L1**
  - **연결 Test**: `MagicSquare4x4Test.should_hold_4x4_matrix`
  - **연결 Code**: `MagicSquare4x4` (Entity), `MagicSquare4x4.fromGrid(int[][])`
  - **ECB**: Entity

- [ ] **TASK-002**
  - **단계**: GREEN
  - **작업 제목**: TASK-001 테스트 통과용 최소 구현
  - **Scenario Level**: **L1**
  - **연결 Test**: `MagicSquare4x4Test.should_hold_4x4_matrix`
  - **연결 Code**: `MagicSquare4x4`
  - **ECB**: Entity

- [ ] **TASK-003**
  - **단계**: REFACTOR
  - **작업 제목**: 불변/방어적 복사·팩토리 정리(규칙 검증은 별도 Logic에 유지)
  - **Scenario Level**: **L2**
  - **연결 Test**: `MagicSquare4x4Test.should_defensively_copy_source_grid`
  - **연결 Code**: `MagicSquare4x4`
  - **ECB**: Entity

### Phase 2 — Logic: 보드 유효성 검사 (US-002)

- [ ] **TASK-004**
  - **단계**: RED
  - **작업 제목**: 4x4 아님 → 거부
  - **Scenario Level**: **L3**
  - **연결 Test**: `BoardValidatorTest.should_reject_non_4x4`
  - **연결 Code**: `BoardValidator` (Logic), `MagicSquare4x4`
  - **ECB**: Logic

- [ ] **TASK-005**
  - **단계**: GREEN
  - **작업 제목**: TASK-004 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `BoardValidatorTest.should_reject_non_4x4`
  - **연결 Code**: `BoardValidator.validateShape`
  - **ECB**: Logic

- [ ] **TASK-006**
  - **단계**: RED
  - **작업 제목**: 값 범위(1~16 및 0) 위반 → 거부
  - **Scenario Level**: **L2** / **L3**
  - **연결 Test**: `BoardValidatorTest.should_reject_out_of_range_values`
  - **연결 Code**: `BoardValidator.validateValueRange`
  - **ECB**: Logic

- [ ] **TASK-007**
  - **단계**: GREEN
  - **작업 제목**: TASK-006 통과
  - **Scenario Level**: **L2**
  - **연결 Test**: `BoardValidatorTest.should_reject_out_of_range_values`
  - **연결 Code**: `BoardValidator`
  - **ECB**: Logic

- [ ] **TASK-008**
  - **단계**: RED
  - **작업 제목**: 빈칸(0) 개수 ≠ 2 → 거부
  - **Scenario Level**: **L2** / **L3**
  - **연결 Test**: `BoardValidatorTest.should_reject_invalid_blank_count`
  - **연결 Code**: `BoardValidator.validateBlankCount`
  - **ECB**: Logic

- [ ] **TASK-009**
  - **단계**: GREEN
  - **작업 제목**: TASK-008 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `BoardValidatorTest.should_reject_invalid_blank_count`
  - **연결 Code**: `BoardValidator`
  - **ECB**: Logic

- [ ] **TASK-010**
  - **단계**: RED
  - **작업 제목**: 0 제외 중복 숫자 → 거부
  - **Scenario Level**: **L3**
  - **연결 Test**: `BoardValidatorTest.should_reject_duplicate_non_zero`
  - **연결 Code**: `BoardValidator.validateNoDuplicateNonZero`
  - **ECB**: Logic

- [ ] **TASK-011**
  - **단계**: GREEN
  - **작업 제목**: TASK-010 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `BoardValidatorTest.should_reject_duplicate_non_zero`
  - **연결 Code**: `BoardValidator`
  - **ECB**: Logic

- [ ] **TASK-012**
  - **단계**: REFACTOR
  - **작업 제목**: 검증 파이프라인 단일 진입점·오류 코드 매핑 정리
  - **Scenario Level**: **L0**
  - **연결 Test**: `BoardValidatorTest.should_follow_team_error_aggregation_policy`
  - **연결 Code**: `BoardValidator`, `ValidationResult` / `DomainError`
  - **ECB**: Logic

### Phase 3 — Logic: 빈칸 탐지 (US-003)

- [ ] **TASK-013**
  - **단계**: RED
  - **작업 제목**: 빈칸 2개 좌표를 row-major 고정 순서로 반환
  - **Scenario Level**: **L1**
  - **연결 Test**: `BlankLocatorTest.should_return_two_positions_in_row_major_order`
  - **연결 Code**: `BlankLocator` (Logic), `CellPosition` (Entity/VO)
  - **ECB**: Logic + Entity(VO)

- [ ] **TASK-014**
  - **단계**: GREEN
  - **작업 제목**: TASK-013 통과
  - **Scenario Level**: **L1**
  - **연결 Test**: `BlankLocatorTest.should_return_two_positions_in_row_major_order`
  - **연결 Code**: `BlankLocator.locate`
  - **ECB**: Logic

- [ ] **TASK-015**
  - **단계**: RED
  - **작업 제목**: 선결 조건 위반 시 빈칸 탐색 실패(또는 Control에서 선행 차단)
  - **Scenario Level**: **L3**
  - **연결 Test**: `BlankLocatorTest.should_fail_if_preconditions_not_met`
  - **연결 Code**: `BlankLocator` / 호출 계약
  - **ECB**: Logic

- [ ] **TASK-016**
  - **단계**: GREEN
  - **작업 제목**: TASK-015 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `BlankLocatorTest.should_fail_if_preconditions_not_met`
  - **연결 Code**: `BlankLocator`
  - **ECB**: Logic

### Phase 4 — Logic: 후보값(누락 숫자) 필터링 (US-004)

- [ ] **TASK-017**
  - **단계**: RED
  - **작업 제목**: 1~16 중 나타나지 않은 두 수를 오름차순으로 산출
  - **Scenario Level**: **L1**
  - **연결 Test**: `MissingNumbersFinderTest.should_find_sorted_missing_pair`
  - **연결 Code**: `MissingNumbersFinder` (Logic), `MissingNumbersPair` (Entity/VO)
  - **ECB**: Logic + Entity(VO)

- [ ] **TASK-018**
  - **단계**: GREEN
  - **작업 제목**: TASK-017 통과
  - **Scenario Level**: **L1**
  - **연결 Test**: `MissingNumbersFinderTest.should_find_sorted_missing_pair`
  - **연결 Code**: `MissingNumbersFinder.find`
  - **ECB**: Logic

- [ ] **TASK-019**
  - **단계**: RED
  - **작업 제목**: 누락 쌍이 2개로 확정되지 않는 경우 거부
  - **Scenario Level**: **L3**
  - **연결 Test**: `MissingNumbersFinderTest.should_reject_when_pair_not_uniquely_determined`
  - **연결 Code**: `MissingNumbersFinder`
  - **ECB**: Logic

- [ ] **TASK-020**
  - **단계**: GREEN
  - **작업 제목**: TASK-019 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `MissingNumbersFinderTest.should_reject_when_pair_not_uniquely_determined`
  - **연결 Code**: `MissingNumbersFinder`
  - **ECB**: Logic

### Phase 5 — Logic: 완성 로직 + 마방진 판정 (US-005)

- [ ] **TASK-021**
  - **단계**: RED
  - **작업 제목**: 채워진(임시 배치) 보드에 대해 행·열·대각 합이 모두 34인지 판정
  - **Scenario Level**: **L1**
  - **연결 Test**: `MagicSquareJudgeTest.should_validate_magic_constant_34`
  - **연결 Code**: `MagicSquareJudge` (Logic), 상수 `MAGIC_SUM=34`는 Logic 전용
  - **ECB**: Logic

- [ ] **TASK-022**
  - **단계**: GREEN
  - **작업 제목**: TASK-021 통과
  - **Scenario Level**: **L1**
  - **연결 Test**: `MagicSquareJudgeTest.should_validate_magic_constant_34`
  - **연결 Code**: `MagicSquareJudge.isMagic`
  - **ECB**: Logic

- [ ] **TASK-023**
  - **단계**: RED
  - **작업 제목**: 작은 수→첫 빈칸, 큰 수→둘째 빈칸 시도 후 성공 시 해당 배치 채택
  - **Scenario Level**: **L1**
  - **연결 Test**: `DualPlacementResolverTest.should_resolve_with_forward_order_first`
  - **연결 Code**: `DualPlacementResolver` (Logic), `PlacementPlan` (Entity/VO)
  - **ECB**: Logic

- [ ] **TASK-024**
  - **단계**: GREEN
  - **작업 제목**: TASK-023 통과
  - **Scenario Level**: **L1**
  - **연결 Test**: `DualPlacementResolverTest.should_resolve_with_forward_order_first`
  - **연결 Code**: `DualPlacementResolver.resolve`
  - **ECB**: Logic

- [ ] **TASK-025**
  - **단계**: RED
  - **작업 제목**: 정순 실패 시 역순 배치만 성공하는 케이스
  - **Scenario Level**: **L2**
  - **연결 Test**: `DualPlacementResolverTest.should_fallback_to_reverse_order`
  - **연결 Code**: `DualPlacementResolver`
  - **ECB**: Logic

- [ ] **TASK-026**
  - **단계**: GREEN
  - **작업 제목**: TASK-025 통과
  - **Scenario Level**: **L2**
  - **연결 Test**: `DualPlacementResolverTest.should_fallback_to_reverse_order`
  - **연결 Code**: `DualPlacementResolver`
  - **ECB**: Logic

- [ ] **TASK-027**
  - **단계**: RED
  - **작업 제목**: 두 조합 모두 실패 시 도메인 실패
  - **Scenario Level**: **L3**
  - **연결 Test**: `DualPlacementResolverTest.should_fail_when_no_valid_placement`
  - **연결 Code**: `DualPlacementResolver`
  - **ECB**: Logic

- [ ] **TASK-028**
  - **단계**: GREEN
  - **작업 제목**: TASK-027 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `DualPlacementResolverTest.should_fail_when_no_valid_placement`
  - **연결 Code**: `DualPlacementResolver`
  - **ECB**: Logic

- [ ] **TASK-029**
  - **단계**: REFACTOR
  - **작업 제목**: 배치 시도와 판정의 중복 제거(기능 동일)
  - **Scenario Level**: **L0**
  - **연결 Test**: `DualPlacementResolverTest`, `MagicSquareJudgeTest` 회귀 전체
  - **연결 Code**: `DualPlacementResolver`, `MagicSquareJudge`
  - **ECB**: Logic

### Phase 6 — Control: 유스케이스 조율 (US-007)

- [ ] **TASK-030**
  - **단계**: RED
  - **작업 제목**: `CompleteMagicSquareUseCase` — 검증→빈칸→누락→해결 순서 고정
  - **Scenario Level**: **L1**
  - **연결 Test**: `CompleteMagicSquareUseCaseTest.should_return_completed_board_on_happy_path`
  - **연결 Code**: `CompleteMagicSquareUseCase` (Control), `CompletionResult` (DTO)
  - **ECB**: Control

- [ ] **TASK-031**
  - **단계**: GREEN
  - **작업 제목**: TASK-030 통과
  - **Scenario Level**: **L1**
  - **연결 Test**: `CompleteMagicSquareUseCaseTest.should_return_completed_board_on_happy_path`
  - **연결 Code**: `CompleteMagicSquareUseCase.execute`
  - **ECB**: Control

- [ ] **TASK-032**
  - **단계**: RED
  - **작업 제목**: 검증 실패 시 해결 단계 미실행(단계 격리)
  - **Scenario Level**: **L3**
  - **연결 Test**: `CompleteMagicSquareUseCaseTest.should_short_circuit_on_validation_failure`
  - **연결 Code**: `CompleteMagicSquareUseCase`
  - **ECB**: Control

- [ ] **TASK-033**
  - **단계**: GREEN
  - **작업 제목**: TASK-032 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `CompleteMagicSquareUseCaseTest.should_short_circuit_on_validation_failure`
  - **연결 Code**: `CompleteMagicSquareUseCase`
  - **ECB**: Control

- [ ] **TASK-034**
  - **단계**: REFACTOR
  - **작업 제목**: 의존성 주입·인터페이스 추출
  - **Scenario Level**: **L0**
  - **연결 Test**: `CompleteMagicSquareUseCaseTest`
  - **연결 Code**: `CompleteMagicSquareUseCase`
  - **ECB**: Control

### Phase 7 — Boundary: 잘못된 입력 처리·I/O (US-006)

- [ ] **TASK-035**
  - **단계**: RED
  - **작업 제목**: 문자열/CLI 인자 파싱 실패 → Boundary에서 구조적 오류 반환(규칙 판단 없음)
  - **Scenario Level**: **L3**
  - **연결 Test**: `StdioMagicSquareAdapterTest.should_fail_on_malformed_input`
  - **연결 Code**: `StdioMagicSquareAdapter` (Boundary), `ParsedBoardInput`
  - **ECB**: Boundary

- [ ] **TASK-036**
  - **단계**: GREEN
  - **작업 제목**: TASK-035 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `StdioMagicSquareAdapterTest.should_fail_on_malformed_input`
  - **연결 Code**: `StdioMagicSquareAdapter.parse`
  - **ECB**: Boundary

- [ ] **TASK-037**
  - **단계**: RED
  - **작업 제목**: 도메인 오류 코드 → 사용자 메시지 매핑(문구만, 재판단 금지)
  - **Scenario Level**: **L3**
  - **연결 Test**: `ErrorPresenterTest.should_map_domain_codes_to_messages`
  - **연결 Code**: `ErrorPresenter` (Boundary)
  - **ECB**: Boundary

- [ ] **TASK-038**
  - **단계**: GREEN
  - **작업 제목**: TASK-037 통과
  - **Scenario Level**: **L3**
  - **연결 Test**: `ErrorPresenterTest.should_map_domain_codes_to_messages`
  - **연결 Code**: `ErrorPresenter`
  - **ECB**: Boundary

### Phase 8 — UI-Track (Dual-Track, US-008)

- [ ] **TASK-039**
  - **단계**: RED (**UI-Track**)
  - **작업 제목**: 입력 수집 후 Boundary로 전달(합·중복 계산 없음)
  - **Scenario Level**: **L1**
  - **연결 Test**: `MagicSquareConsoleUiTest.should_collect_sixteen_cells_without_domain_rules`
  - **연결 Code**: `MagicSquareConsoleUi` (Boundary/UI)
  - **ECB**: Boundary

- [ ] **TASK-040**
  - **단계**: GREEN (**UI-Track**)
  - **작업 제목**: TASK-039 통과
  - **Scenario Level**: **L1**
  - **연결 Test**: `MagicSquareConsoleUiTest.should_collect_sixteen_cells_without_domain_rules`
  - **연결 Code**: `MagicSquareConsoleUi`
  - **ECB**: Boundary

- [ ] **TASK-041**
  - **단계**: RED (**UI-Track**)
  - **작업 제목**: 성공 시 완성 보드 출력(포맷만)
  - **Scenario Level**: **L1**
  - **연결 Test**: `MagicSquareConsoleUiTest.should_render_completed_grid`
  - **연결 Code**: `MagicSquareConsoleUi`
  - **ECB**: Boundary

- [ ] **TASK-042**
  - **단계**: GREEN (**UI-Track**)
  - **작업 제목**: TASK-041 통과
  - **Scenario Level**: **L1**
  - **연결 Test**: `MagicSquareConsoleUiTest.should_render_completed_grid`
  - **연결 Code**: `MagicSquareConsoleUi`
  - **ECB**: Boundary

- [ ] **TASK-043**
  - **단계**: REFACTOR (**UI-Track**)
  - **작업 제목**: UI에서 Control 호출 단일화(`Application`/`main`은 wiring만)
  - **Scenario Level**: **L0**
  - **연결 Test**: `ApplicationSmokeTest.should_wire_ui_to_control`
  - **연결 Code**: `Application`, `main`
  - **ECB**: Boundary + Control(조립)

### Phase 9 — 품질: 테스트 커버리지·추적성 (US-009)

- [ ] **TASK-044**
  - **단계**: REFACTOR
  - **작업 제목**: 테스트 커버리지 체크포인트 — Logic 라인 커버리지 목표 측정 및 미달 영역 Task 추가
  - **Scenario Level**: **L0**
  - **연결 Test**: CI 커버리지 임계값(도구별)
  - **연결 Code**: 빌드/CI 설정 파일
  - **ECB**: *(도구)*
  - **체크포인트**: Domain Logic 핵심 패키지 커버리지 ≥ 팀 목표, L3 시나리오별 최소 1 테스트

- [ ] **TASK-045**
  - **단계**: REFACTOR
  - **작업 제목**: Concept-to-Code 매트릭스 완성 — Invariant/Story → Scenario Level → Test → 타입
  - **Scenario Level**: **L0**
  - **연결 Test**: `ArchitectureTest` 또는 수동 리뷰 체크리스트
  - **연결 Code**: `docs/traceability.md`
  - **ECB**: *(문서)*
  - **체크포인트**: Epic-001·US-001~009·TASK-000~045 상호 링크 가능

---

## 9. Dual-Track 요약

| Track | Task 범위 | 금지 |
|--------|-----------|------|
| **Logic-Track** | TASK-004~029, 030~034, 품질 일부 | Boundary에서 합 34·중복 검사 |
| **UI-Track** | TASK-039~043 | UI에 비즈니스 규칙·판정 로직 |

---

## 10. 필수 작업 매핑(요구사항 대응)

| 요구 항목 | 대표 Task |
|-----------|-----------|
| 보드 생성 | TASK-001~003 |
| 보드 유효성 검사 | TASK-004~012 |
| 빈칸 탐지 | TASK-013~016 |
| 후보값 필터링 | TASK-017~020 |
| 완성 로직 | TASK-021~029 |
| 잘못된 입력 처리 | TASK-004~011, 032~038 |
| 테스트 커버리지 체크포인트 | TASK-044 |

---

## 11. 참고: 테스트·타입 명명

본 보고서의 테스트·타입 이름은 `02_MagicSquare_4x4_DualTrack_TDD_Report.md`의 도메인 구성(`MagicSquare4x4`, `BlankLocator`, `MissingNumberFinder`, `MagicSquareJudge`, `DualPlacementResolver` 등)과 정합되도록 작성하였다. 실제 언어·프레임워크에 맞게 클래스/패키지 경로만 치환하면 된다.

---

## 12. 개정 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-04-28 | 초안 — 구현용 To-Do 구조 Report 폴더보내기 |
