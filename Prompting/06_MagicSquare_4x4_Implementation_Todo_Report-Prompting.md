# To-Do 리스트 작성 참조 문서
_Exported on 4/28/2026 at 10:56:50 GMT+9 from Cursor (3.2.11)_

---

**User**

To-Do 리스트를 작성하고 싶습니다. 작성한 문서 중 무엇을 참조해서 만들어야 할까요?

---

**Cursor**

프로젝트에 어떤 문서가 있는지 확인합니다.



사용자 여정 보고서의 나머지 스토리와 PRD의 구현 관련 섹션을 확인합니다.



To-Do 리스트를 만들 때는 **정리된 산출물인 `Report/` 문서**를 기준으로 잡는 것이 좋습니다. `Prompting/`은 대화·프롬프트 기록이라, 체크리스트의 “원본 근거”로 쓰기보다는 참고용에 가깝습니다.

## 1순위: `Report/04_MagicSquare_User_Journey_Report.md`

**Epic → 여정(Step 1~5) → User Story 5개 → Acceptance Criteria → Gherkin 시나리오**까지 이미 있어서, To-Do를 **스토리별·시나리오별**로 쪼개기 가장 좋습니다.

- Journey 단계(계약 정의, 도메인 분리, Dual-Track, 회귀 보호)를 **마일스톤**으로 두고  
- 각 Story의 AC와 Level 4 Gherkin을 **구체 작업·테스트 항목**으로 옮기면 됩니다.

## 2순위: `Report/05_MagicSquare_PRD.md`

**제품 범위(In/Out of scope), I/O·오류 계약, 비기능·DoD, 아키텍처 제약**이 들어 있어, “빼먹지 말아야 할 항목”과 **완료 정의**를 To-Do에 반영할 때 참조하면 좋습니다.

## 구현·TDD 순서를 맞출 때: `Report/02_MagicSquare_4x4_DualTrack_TDD_Report.md`

도메인 서비스 이름(`BlankLocator`, `MissingNumberFinder` 등), **D-RED-01~12** 같은 RED 테스트 목록, UI/Logic 듀얼 트랙이 정리되어 있어 **실제 코딩 순서·테스트 이름**을 To-Do로 내릴 때 쓰기 좋습니다.

## 문제·불변조건과 맞추고 싶을 때: `Report/01_4x4_Magic_Square_Problem_Definition_Report.md`

요구사항이 “왜 이런 제약인지”와 불변조건과 맞는지 검증할 때 보조로 쓰면 됩니다.

---

**요약**: 실행 가능한 할 일 목록의 뼈대는 **`04_MagicSquare_User_Journey_Report.md`**, 범위·완료 기준 보강은 **`05_MagicSquare_PRD.md`**, 코딩·테스트 쪼개기는 **`02_MagicSquare_4x4_DualTrack_TDD_Report.md`** 순으로 참조하는 구성을 추천합니다.

---

**보안 참고**: 저장소에 `ghp_...txt`처럼 GitHub PAT 형태의 파일이 보입니다. To-Do 참고 문서로 쓰지 말고, 노출됐다면 [GitHub에서 토큰 폐기](https://github.com/settings/tokens) 후 해당 파일은 삭제·`.gitignore` 처리하는 것이 안전합니다.

---

**User**

다음 방법론을 적용하여
"Magic Square 4x4 완성 시스템"의 구현용 To-Do 구조를 작성하세요.

적용 방법론:
- Concept-to-Code Traceability
- Dual-Track UI + Logic TDD
- To-Do → Scenario → Test → Code 구조
- ECB(Entity / Control / Boundary) 모델
- RED → GREEN → REFACTOR

반드시 한국어로 작성하세요.

[시스템 목표]
부분적으로 비어 있는 4x4 Magic Square를 완성하는 시스템의 개발 To-Do를 작성합니다.

[도메인 규칙]
- 보드는 4x4이다.
- 숫자는 1~16만 사용한다.
- 0은 빈칸이다.
- 정확히 2칸이 비어 있다.
- 0을 제외한 중복 숫자는 허용되지 않는다.
- 모든 행, 열, 대각선의 합은 34여야 한다.
- 해결 가능한 경우 빈칸 값을 찾아 채운다.
- 유효하지 않은 보드는 거부한다.

[출력 형식]
다음 구조를 반드시 지켜서 작성하세요.

1. Epic
2. User Story
3. Phase별 Task 목록
4. 각 Task에는 반드시 아래 정보를 포함하세요.
   - Task ID
   - RED / GREEN / REFACTOR 여부
   - 작업 제목
   - Scenario Level (L0/L1/L2/L3)
   - 연결되는 Test 이름
   - 연결되는 Code 대상
   - ECB 스테레오타입 (Entity / Control / Boundary)
   - 필요 시 체크포인트

[표현 스타일]
- Markdown 사용
- 체크박스 형식 사용
- 실제 Cursor.AI 실습용 개발 보드처럼 작성
- 식별자는 Epic-001, US-001, TASK-001 형식 사용
- 유효한 케이스와 실패 케이스를 모두 포함
- 최소한 다음 작업을 포함
  - 보드 생성
  - 보드 유효성 검사
  - 빈칸 탐지
  - 후보값 필터링
  - 완성 로직
  - 잘못된 입력 처리
  - 테스트 커버리지 체크포인트

[Scenario Level 정의]
- L0: 기능 개요
- L1: 정상 흐름
- L2: 경계 상황
- L3: 실패 상황

[추가 제약]
- Logic 책임은 명확히 분리할 것
- UI/Boundary에는 비즈니스 규칙을 넣지 말 것
- Control은 검증과 해결 흐름을 조율할 것
- Entity는 보드 상태를 표현할 것
- 모든 To-Do는 Scenario, Test, Code로 추적 가능해야 함

이제
"Magic Square 4x4 완성 시스템"의 To-Do 구조를 생성하세요.

---

**Cursor**

아래는 요청하신 방법론·출력 형식·도메인 규칙에 맞춘 **구현용 To-Do 구조**입니다. (Cursor 실습 보드용으로 바로 복사해 쓸 수 있게 작성했습니다.)

---

# Magic Square 4x4 완성 시스템 — 구현용 To-Do 구조

**추적 원칙**: Concept → User Story → Task → **Scenario(L0~L3)** → **Test** → **Code**  
**개발 리듬**: Dual-Track **UI** + **Logic**, 각 Task는 **RED → GREEN → REFACTOR** 중 하나로 명시  
**ECB**: **Entity** = 보드/값 객체 상태 / **Control** = 검증·해결 **흐름 조율**(규칙은 Logic에 위임) / **Boundary** = 입출력·표시(I/O 파싱·에러 메시지 매핑만, **비즈니스 규칙 없음**)

---

## 1. Epic

- [ ] **Epic-001 — Invariant 기반 4x4 Magic Square 완성 시스템**  
  - **목표**: 부분 채움 보드(0=빈칸 2개)를 입력으로 받아, 도메인 규칙을 만족하면 빈칸을 채운 결과를 반환하고, 위반 시 거부한다.  
  - **Dual-Track**: **Logic-Track**(도메인·유스케이스·단위/통합 테스트)과 **UI-Track**(입력 수집·결과 표시·Boundary 어댑터)을 병렬로 진행하되, **규칙은 Logic에만** 둔다.  
  - **완료 개념**: 각 Task가 L0~L3 시나리오, 테스트 클래스/메서드, 대상 타입(파일)까지 역추적 가능.

---

## 2. User Story

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
  As a 사용자, I want 보드를 입력하고 결과/오류를 보고 싶다, So that UI에 마방진 규칙(34, 중복 등)을 넣지 않고 표현만 한다.

- [ ] **US-009 — 품질·추적성**  
  As a 팀, I want 커버리지와 Concept-to-Code 매트릭스를 유지하고 싶다, So that 회귀와 교육 목표(추적 가능성)를 만족한다.

---

## 3. Phase별 Task 목록

### Phase 0 — 개념·계약·스캐폴딩 (Concept-to-Code Traceability)

- [ ] **TASK-000**  
  - **단계**: REFACTOR(문서/코드 골격)  
  - **작업 제목**: 도메인 용어·오류 코드·패키지 구조를 ECB로 고정(추적 매트릭스 초안)  
  - **Scenario Level**: **L0** (기능 개요: “입력 보드 → 검증 → 해결 시도 → 출력/거부”)  
  - **연결 Test**: `TraceabilityMatrixTest`(수동/문서 링크 검증용 플레이스홀더) 또는 README/주석에 매핑 표 — *코드베이스 정책에 맞게 하나만 선택*  
  - **연결 Code**: `docs/traceability.md` 또는 `package-info` / `ErrorCode` enum  
  - **ECB**: Boundary(공개 계약)·Control(유스케이스 인터페이스)·Entity(타입) 경계 정의  
  - **체크포인트**: Invariant 목록이 Task ID와 1:1 대응 초안 완료  

---

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
  - **연결 Test**: 동일  
  - **연결 Code**: `MagicSquare4x4`  
  - **ECB**: Entity  

- [ ] **TASK-003**  
  - **단계**: REFACTOR  
  - **작업 제목**: 불변/방어적 복사·팩토리 정리(규칙 검증은 아직 분리)  
  - **Scenario Level**: **L2** (방어적 복사로 외부 변경 차단)  
  - **연결 Test**: `MagicSquare4x4Test.should_defensively_copy_source_grid`  
  - **연결 Code**: `MagicSquare4x4`  
  - **ECB**: Entity  

---

### Phase 2 — Logic: 보드 유효성 검사 (US-002)

- [ ] **TASK-004**  
  - **단계**: RED  
  - **작업 제목**: 4x4 아님 → 거부  
  - **Scenario Level**: **L3**  
  - **연결 Test**: `BoardValidatorTest.should_reject_non_4x4`  
  - **연결 Code**: `BoardValidator` (Logic), `MagicSquare4x4`  
  - **ECB**: Control이 호출할 **순수 검증기**(규칙은 Logic) — *스테레오타입은 Logic 서비스로 분류*  

- [ ] **TASK-005**  
  - **단계**: GREEN  
  - **작업 제목**: TASK-004 통과  
  - **Scenario Level**: **L3**  
  - **연결 Test**: 동일  
  - **연결 Code**: `BoardValidator.validateShape`  
  - **ECB**: Logic(검증 전담; ECB에서 “규칙 실행 주체”는 Entity가 아닌 Logic 계층으로 둠)  

- [ ] **TASK-006**  
  - **단계**: RED  
  - **작업 제목**: 값 범위(1~16 및 0) 위반 → 거부  
  - **Scenario Level**: **L2/L3** (17, 음수 등)  
  - **연결 Test**: `BoardValidatorTest.should_reject_out_of_range_values`  
  - **연결 Code**: `BoardValidator.validateValueRange`  
  - **ECB**: Logic  

- [ ] **TASK-007**  
  - **단계**: GREEN  
  - **작업 제목**: TASK-006 통과  
  - **Scenario Level**: **L2**  
  - **연결 Test**: 동일  
  - **연결 Code**: `BoardValidator`  
  - **ECB**: Logic  

- [ ] **TASK-008**  
  - **단계**: RED  
  - **작업 제목**: 빈칸(0) 개수 ≠ 2 → 거부  
  - **Scenario Level**: **L2/L3** (0개/1개/3개)  
  - **연결 Test**: `BoardValidatorTest.should_reject_invalid_blank_count`  
  - **연결 Code**: `BoardValidator.validateBlankCount`  
  - **ECB**: Logic  

- [ ] **TASK-009**  
  - **단계**: GREEN  
  - **작업 제목**: TASK-008 통과  
  - **Scenario Level**: **L3**  
  - **연결 Test**: 동일  
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
  - **연결 Test**: 동일  
  - **연결 Code**: `BoardValidator`  
  - **ECB**: Logic  

- [ ] **TASK-012**  
  - **단계**: REFACTOR  
  - **작업 제목**: 검증 파이프라인 단일 진입점·오류 코드 매핑 정리  
  - **Scenario Level**: **L0**  
  - **연결 Test**: `BoardValidatorTest.should_aggregate_validation_errors_or_first_error_policy` *(팀 정책에 맞게 하나)*  
  - **연결 Code**: `BoardValidator`, `ValidationResult` / `DomainError`  
  - **ECB**: Logic (+ 경량 값 객체는 Entity로 분류 가능)  

---

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
  - **연결 Test**: 동일  
  - **연결 Code**: `BlankLocator.locate`  
  - **ECB**: Logic  

- [ ] **TASK-015**  
  - **단계**: RED  
  - **작업 제목**: 검증된 보드 외 입력 시 빈칸 탐색 실패(선결 조건 위반)  
  - **Scenario Level**: **L3**  
  - **연결 Test**: `BlankLocatorTest.should_fail_if_preconditions_not_met` *(또는 Control 테스트로 이동)*  
  - **연결 Code**: `BlankLocator` / 호출 계약  
  - **ECB**: Logic  

- [ ] **TASK-016**  
  - **단계**: GREEN  
  - **작업 제목**: TASK-015 통과  
  - **Scenario Level**: **L3**  
  - **연결 Test**: 동일  
  - **연결 Code**: `BlankLocator`  
  - **ECB**: Logic  

---

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
  - **연결 Test**: 동일  
  - **연결 Code**: `MissingNumbersFinder.find`  
  - **ECB**: Logic  

- [ ] **TASK-019**  
  - **단계**: RED  
  - **작업 제목**: 누락 쌍이 2개로 확정되지 않는 비정상(선행 검증 누락 시) 거부  
  - **Scenario Level**: **L3**  
  - **연결 Test**: `MissingNumbersFinderTest.should_reject_when_pair_not_uniquely_determined`  
  - **연결 Code**: `MissingNumbersFinder`  
  - **ECB**: Logic  

- [ ] **TASK-020**  
  - **단계**: GREEN  
  - **작업 제목**: TASK-019 통과  
  - **Scenario Level**: **L3**  
  - **연결 Test**: 동일  
  - **연결 Code**: `MissingNumbersFinder`  
  - **ECB**: Logic  

---

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
  - **연결 Test**: 동일  
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
  - **연결 Test**: 동일  
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
  - **연결 Test**: 동일  
  - **연결 Code**: `DualPlacementResolver`  
  - **ECB**: Logic  

- [ ] **TASK-027**  
  - **단계**: RED  
  - **작업 제목**: 두 조합 모두 실패 시 “해결 불가” 도메인 실패  
  - **Scenario Level**: **L3**  
  - **연결 Test**: `DualPlacementResolverTest.should_fail_when_no_valid_placement`  
  - **연결 Code**: `DualPlacementResolver`  
  - **ECB**: Logic  

- [ ] **TASK-028**  
  - **단계**: GREEN  
  - **작업 제목**: TASK-027 통과  
  - **Scenario Level**: **L3**  
  - **연결 Test**: 동일  
  - **연결 Code**: `DualPlacementResolver`  
  - **ECB**: Logic  

- [ ] **TASK-029**  
  - **단계**: REFACTOR  
  - **작업 제목**: 배치 시도와 판정의 중복 제거(가독성·성능은 기능 동일)  
  - **Scenario Level**: **L0**  
  - **연결 Test**: 기존 Resolver/Judge 테스트 전체 회귀  
  - **연결 Code**: `DualPlacementResolver`, `MagicSquareJudge`  
  - **ECB**: Logic  

---

### Phase 6 — Control: 유스케이스 조율 (US-007)

- [ ] **TASK-030**  
  - **단계**: RED  
  - **작업 제목**: `CompleteMagicSquareUseCase` — 검증→빈칸→누락→해결 순서 고정, 성공 시 결과 DTO  
  - **Scenario Level**: **L1**  
  - **연결 Test**: `CompleteMagicSquareUseCaseTest.should_return_completed_board_on_happy_path`  
  - **연결 Code**: `CompleteMagicSquareUseCase` (Control), `CompletionResult` (DTO)  
  - **ECB**: Control  

- [ ] **TASK-031**  
  - **단계**: GREEN  
  - **작업 제목**: TASK-030 통과  
  - **Scenario Level**: **L1**  
  - **연결 Test**: 동일  
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
  - **연결 Test**: 동일  
  - **연결 Code**: `CompleteMagicSquareUseCase`  
  - **ECB**: Control  

- [ ] **TASK-034**  
  - **단계**: REFACTOR  
  - **작업 제목**: 의존성 주입·인터페이스 추출(테스트 더블 용이)  
  - **Scenario Level**: **L0**  
  - **연결 Test**: `CompleteMagicSquareUseCaseTest` (모킹 최소화 정책 유지)  
  - **연결 Code**: `CompleteMagicSquareUseCase`  
  - **ECB**: Control  

---

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
  - **연결 Test**: 동일  
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
  - **연결 Test**: 동일  
  - **연결 Code**: `ErrorPresenter`  
  - **ECB**: Boundary  

---

### Phase 8 — UI-Track (Dual-Track, US-008)

- [ ] **TASK-039**  
  - **단계**: RED (**UI-Track**)  
  - **작업 제목**: 입력 폼/콘솔 프롬프트에서 16칸 수집 후 Boundary로 전달(합·중복 계산 없음)  
  - **Scenario Level**: **L1**  
  - **연결 Test**: `MagicSquareConsoleUiTest.should_collect_sixteen_cells_without_domain_rules`  
  - **연결 Code**: `MagicSquareConsoleUi` (Boundary/UI)  
  - **ECB**: Boundary  

- [ ] **TASK-040**  
  - **단계**: GREEN (**UI-Track**)  
  - **작업 제목**: TASK-039 통과  
  - **Scenario Level**: **L1**  
  - **연결 Test**: 동일  
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
  - **연결 Test**: 동일  
  - **연결 Code**: `MagicSquareConsoleUi`  
  - **ECB**: Boundary  

- [ ] **TASK-043**  
  - **단계**: REFACTOR (**UI-Track**)  
  - **작업 제목**: UI에서 Control 호출 단일화(`App`/`Main`은 wiring만)  
  - **Scenario Level**: **L0**  
  - **연결 Test**: `ApplicationSmokeTest.should_wire_ui_to_control`  
  - **연결 Code**: `Application`, `main`  
  - **ECB**: Boundary + Control(조립)  

---

### Phase 9 — 품질: 테스트 커버리지·추적성 (US-009)

- [ ] **TASK-044**  
  - **단계**: REFACTOR  
  - **작업 제목**: **테스트 커버리지 체크포인트** — Logic 라인 커버리지 목표(예: 95%) 측정 및 미달 영역 Task 추가  
  - **Scenario Level**: **L0**  
  - **연결 Test**: CI의 `jacoco`/`coverage.py`/프레임워크 리포트 임계값  
  - **연결 Code**: 빌드 스크립트 `pom.xml` / `build.gradle` / `pytest.ini` 등  
  - **ECB**: *(도구)*  
  - **체크포인트**: **Domain Logic 핵심 패키지 커버리지 ≥ 목표**, L3 시나리오별 최소 1 테스트 존재  

- [ ] **TASK-045**  
  - **단계**: REFACTOR  
  - **작업 제목**: Concept-to-Code 매트릭스 완성 — Invariant/Story → Scenario Level → Test 클래스 → 타입  
  - **Scenario Level**: **L0**  
  - **연결 Test**: `ArchitectureTest` 또는 수동 리뷰 체크리스트  
  - **연결 Code**: `docs/traceability.md`  
  - **ECB**: *(문서)*  
  - **체크포인트**: Epic-001·US-001~009·TASK-000~045 상호 링크 가능  

---

## 4. Dual-Track 정리 (실습 보드용 한 줄 메모)

| Track | 담당 Task 범위 | 금지 사항 |
|--------|----------------|-----------|
| **Logic-Track** | TASK-004~029,030~034, 품질 일부 | Boundary에서 합 34·중복 검사 |
| **UI-Track** | TASK-039~043 | UI에 비즈니스 규칙·판정 로직 |

---

## 5. 최소 포함 항목 대응표

| 요구 항목 | 대표 Task |
|-----------|-----------|
| 보드 생성 | TASK-001~003 |
| 보드 유효성 검사 | TASK-004~012 |
| 빈칸 탐지 | TASK-013~016 |
| 후보값 필터링 | TASK-017~020 |
| 완성 로직 | TASK-021~029 |
| 잘못된 입력 처리 | TASK-004~011,032~038 |
| 테스트 커버리지 체크포인트 | TASK-044 |

---

이 구조를 그대로 이슈 트래커(Epic/Story/Task)나 Cursor 보드에 옮기면, 각 체크박스가 **Scenario(L0~L3) → Test 이름 → Code 대상 → ECB 역할**까지 한 줄로 추적되도록 맞춰 두었습니다. 원하시면 사용 중인 언어/프레임워크(Java, Kotlin, Python 등)에 맞춰 **테스트·클래스 이름만** 프로젝트 규칙에 맞게 일괄 치환한 버전도 만들어 드리겠습니다.

---

**User**

To-Do 리스트를  포함해 READMD.md 파일을 만들고 싶습니다. 무슨 문서를 참조하면 좋을까요?

---

**Cursor**

README에 **프로젝트 소개·실행 방법·To-Do**를 넣을 때 참고하면 좋은 문서를 정리합니다.



저장소에는 아직 `README.md`와 빌드 설정 파일이 없고, 주로 `Report/`·`Prompting/` 문서로 구성된 상태로 보입니다.

## README에 넣을 때 참고하면 좋은 문서

### To-Do·진행 상황·학습 목표
- **`Report/04_MagicSquare_User_Journey_Report.md`** — Epic, 여정, User Story, AC, Gherkin까지 있어 **README의 To-Do / 로드맵**을 쪼개기 가장 좋습니다.
- **`Report/02_MagicSquare_4x4_DualTrack_TDD_Report.md`** — 도메인 이름, RED 테스트 목록, UI/Logic 듀얼 트랙 순서를 To-Do **실행 순서**에 반영할 때 씁니다.
- 이전에 정리한 **구현용 To-Do 구조**(Epic / US / Phase / TASK-xxx)가 있다면, README에는 그중 **상위 몇 단계만** 요약하고 나머지는 링크나 별도 `docs/`로 두는 방식이 읽기 좋습니다.

### 프로젝트가 무엇인지·범위·용어
- **`Report/05_MagicSquare_PRD.md`** — 한 줄 소개, 범위(In/Out), 계약·품질 기준을 README **개요·비목표**에 맞춥니다.
- **`Report/01_4x4_Magic_Square_Problem_Definition_Report.md`** — 문제 정의·불변조건을 README **도메인 규칙** 블록에 요약할 때 씁니다.

### 개발 규칙·AI/에디터 가이드
- **`Report/03_MagicSquare_CursorRules_Report.md`** 또는 루트의 **`.cursorrules`**(있다면) — README의 **Contributing / 코딩·TDD 규칙** 한 줄 요약과 “자세한 규칙은 … 참고” 링크용입니다.

### 굳이 README 본문에 넣지 않아도 되는 것
- **`Prompting/`** — 채팅·프롬프트보내기라, **근거 문서**로는 `Report/`가 더 낫고, README에는 `Report` 경로만 안내해도 충분합니다.

---

**요약**: README 본문은 **`05_MagicSquare_PRD.md`(무엇/왜)` + `01`(규칙 요약)` + `04`(To-Do·스토리)` + `02`(구현·테스트 순서)`**를 참조하고, 세부 To-Do는 `04`·`02`를 기준으로 두면 됩니다. 코드와 빌드가 생기면 README의 **설치·실행**은 그때 생기는 `package.json` / `pom.xml` 등과 맞추면 됩니다.

원하시면 위 참조만으로 **README.md 초안**(개요 + 도메인 규칙 + To-Do 체크리스트 + `Report` 링크)을 이 저장소에 실제로 작성해 드릴까요?

---

**User**

Report 폴더에 보고서로 내보내줘.

---

**Cursor**

Report 폴더의 기존 보고서 번호를 확인한 뒤, 구현용 To-Do 구조 보고서를 추가합니다.



구현용 To-Do 구조를 `Report/06_...` 보고서로 작성합니다.



`Report` 폴더에 아래 보고서로 저장해 두었습니다.

**파일**: `Report/06_MagicSquare_4x4_Implementation_Todo_Report.md`

**포함 내용**  
- 문서 개요·관련 보고서(01, 02, 04, 05) 링크  
- 도메인 규칙·ECB·Dual-Track·Scenario L0~L3 정의  
- Epic-001, US-001~009  
- Phase 0~9, TASK-000~045(RED/GREEN/REFACTOR, Scenario, Test, Code, ECB, 체크포인트)  
- Dual-Track 요약표·필수 작업 매핑·02번 보고서와의 명명 정합 안내  
- 개정 이력(1.0 / 2026-04-28)

루트에 `README.md`를 만들 때는 이 파일을 **구현 To-Do 원본**으로 두고, 요약·링크만 README에 넣으면 됩니다.

---

**User**

To-Do　리스트를  포함해 READMD.md 파일을 만들고 싶습니다. 무슨 문서를 참조하면 좋을까요?


---

**Cursor**

`README.md`에 **To-Do**까지 넣을 때는 아래를 참조하면 됩니다. (지금 저장소 기준)

## To-Do 본문·체크리스트

- **`Report/06_MagicSquare_4x4_Implementation_Todo_Report.md`** — Epic / User Story / Phase / TASK-000~045, Scenario·Test·Code·ECB까지 정리된 **구현용 To-Do 원본**이라, README에는 이걸 **요약·링크**하거나 일부 Phase만 옮기면 됩니다.

## README 나머지 섹션용

- **`Report/05_MagicSquare_PRD.md`** — 프로젝트 한 줄 소개, 범위, 계약·품질 기준  
- **`Report/01_4x4_Magic_Square_Problem_Definition_Report.md`** — 문제 정의·불변조건(도메인 규칙 요약)  
- **`Report/04_MagicSquare_User_Journey_Report.md`** — Epic·여정·스토리·Gherkin(배경·용어 정렬용)  
- **`Report/02_MagicSquare_4x4_DualTrack_TDD_Report.md`** — 도메인 타입·RED 테스트 목록·실행 순서 보강  
- **`Report/03_MagicSquare_CursorRules_Report.md`** 또는 **`.cursorrules`** — 기여 규칙·TDD 한 줄 안내  

## 굳이 README에 안 넣어도 되는 것

- **`Prompting/`** — 대화 기록용이므로, 근거는 **`Report/`**만 README에 안내해도 충분합니다.

---

**한 줄 요약**: To-Do는 **`06_MagicSquare_4x4_Implementation_Todo_Report.md`**를 기준으로 하고, 소개·규칙·링크는 **`05` → `01` → `04`/`02`** 순으로 참조하면 README 구성이 맞습니다.

---

**User**

하나 만들어줘

---

**Cursor**

프로젝트 루트에 `README.md`를 작성합니다. `Report/06`과 기존 보고서 내용을 반영합니다.



프로젝트 루트에 **`README.md`**를 추가해 두었습니다.

**포함 내용**
- 프로젝트 한 줄 소개·목표(Invariant, Dual-Track, ECB, 추적)
- 도메인 규칙 표 + `01`/`05` 링크
- `Report/` 문서 표(01~06, **06을 To-Do 원본**으로 명시)
- 빌드/실행 자리(도구 정해지면 채우도록 안내)
- **To-Do**: Epic-001, US-001~009, Phase 0~9 체크박스 + 상세는 `06` 보고서로 안내

파일 경로: `c:\DEV\MagicSquare_12\README.md`

---

**User**

@README.md 파일 중 To-Do list 를 작성해줘. 자세하게 생각해서...

---

**Cursor**

README.md의 To-Do 섹션을 이미지 템플릿(계층 + RED/GREEN/REFACTOR 하위 항목 + 추적 매트릭스)에 맞춰 상세히 작성합니다.



README의 To-Do 섹션을 슬라이드 템플릿에 맞춰 계층 구조(RED/GREEN/REFACTOR 하위 항목), ECB 표기, 요구사항 추적 매트릭스로 확장합니다.



US 번호를 PRD·06과 맞추기 위해 **US-006(Boundary)**를 **US-007(Control)** 앞으로 옮깁니다.



`README.md`의 **구현 To-Do** 구간을 아래처럼 바꿔 두었습니다.

### 반영한 내용
- **슬라이드와 같은 체계**: 상단에 *체크박스 · 단계별 번호 · Requirements 추적* 안내, **Task → Req → Scenario → Test → Code(ECB)** 한 줄 규칙.
- **Req ID ↔ Invariant 표**: `REQ-I01`~`REQ-I08`, `REQ-UC`, `REQ-IO`, `REQ-UI`, `REQ-QA`, `REQ-ARCH`로 요구를 묶어 두었습니다.
- **`## Epic-001`** 아래 **`### US-xxx`** 계층 + 각 **TASK**마다 **`TASK-xxx-1` RED / `-2` GREEN / `-3` 또는 `-1` REFACTOR** 하위 체크박스(06번 보고서의 TASK 번호와 대응).
- **ECB·테스트 클래스 이름**을 본문에 박아 두어 Cursor 실습용으로 바로 쓸 수 있게 했습니다.
- **Requirements 추적 매트릭스** 표: Task ID | Req ID | Scenario | 테스트 | ECB | 상태(⬜/🔴/🟢/✅ 안내).
- **US-006 / US-007** 순서는 PRD·06과 맞추고, 의존성은 *Logic → Control → Boundary/UI* 권장이라는 **짧은 힌트**만 추가했습니다.
- 깨질 수 있는 앵커 링크 대신 **06 보고서 파일 링크**만 사용했습니다.

파일: `c:\DEV\MagicSquare_12\README.md` — 필요하면 매트릭스에 **TASK-002·005… 같은 짝수 GREEN 전용 행**을 더 넣어 확장할 수 있습니다.

