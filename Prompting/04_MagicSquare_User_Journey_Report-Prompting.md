# Magic Square user journey epic
_Exported on 4/27/2026 at 17:27:58 GMT+9 from Cursor (3.2.11)_

---

**User**

Magic Square를 위한 사용자 여정 작성 (Epic → User Story → Task)을 하고자 합니다.
먼저, Level 1: Epic (비즈니스 목표): EPIC — Business Goal에 대한 내용을 다음처럼 작성해 주세요.
Epic: “Invariant(불변조건) 기반 사고 훈련 시스템 구축”
목적
4x4 Magic Square 문제를 활용하여:
Invariant 중심 설계 사고 훈련
Dual-Track TDD 적용 훈련
입력/출력 계약 명확화 훈련
설계 → 테스트 → 구현 → 리팩토링 흐름 체화

성공 기준
Domain Logic 95% 이상 테스트 커버리지
입력 검증 100% 계약 테스트 통과
하드코딩 없음
매직 넘버 없음
Invariant → Test 추적 가능

---

**Cursor**

## Level 1: Epic (Business Goal)

### EPIC
**“Invariant(불변조건) 기반 사고 훈련 시스템 구축”**

### 목적
4x4 Magic Square 문제를 활용하여 다음 역량을 체계적으로 훈련한다.

- **Invariant 중심 설계 사고 훈련**
- **Dual-Track TDD 적용 훈련**
- **입력/출력 계약 명확화 훈련**
- **설계 → 테스트 → 구현 → 리팩토링 흐름 체화**

### 성공 기준 (Success Criteria)

- **Domain Logic 테스트 커버리지 95% 이상 달성**
- **입력 검증 계약 테스트 100% 통과**
- **하드코딩 없음**
- **매직 넘버 없음**
- **Invariant와 테스트 간 추적 가능성 확보** (Invariant → Test Traceability)

원하시면 다음 단계로 **Level 2: User Story**를 이 Epic에 맞춰 역할별(학습자/평가자/시스템)로 바로 분해해드리겠습니다.

---

**User**

Level 2: User Journey (사용자 여정)를 다음 내용처럼 작성해 주세요.
Persona
소프트웨어 개발 학습자
TDD 훈련 중
Clean Architecture 이해 중

Journey
Step 1 — 문제 인식
“마방진을 구현한다”가 아니라

Step 2 — 계약 정의
입력 스키마 정의
출력 스키마 정의
예외 정책 정의


Step 3 — Domain 분리
BlankFinder
MissingNumberFinder
MagicSquareValidator
Solver

Step 4 — Dual-Track 진행
UI RED / Logic RED 병렬
GREEN 최소 구현
REFACTOR 통합 정리

Step 5 — 회귀 보호
엣지 케이스 추가
입력 오류 케이스 추가
조합 실패 케이스 추가

---

**Cursor**

## Level 2: User Journey (사용자 여정)

### Persona
- **소프트웨어 개발 학습자**
- **TDD 훈련 중**
- **Clean Architecture 이해 중**

### Journey

#### Step 1 — 문제 인식
학습자는 목표를 단순히 “마방진을 구현한다”로 두지 않고,  
**“불변조건(Invariant)을 먼저 정의하고 검증 가능한 구조로 설계한다”**로 재정의한다.

#### Step 2 — 계약 정의
구현 전에 Boundary 관점의 계약을 먼저 고정한다.

- **입력 스키마 정의**: 4x4 그리드 형식, 허용 값 범위, 공백(빈칸) 표현
- **출력 스키마 정의**: 완성된 4x4 그리드, 검증 결과, 실패 사유 포맷
- **예외 정책 정의**: 타입 오류, 범위 오류, 중복 값, 해 불가능 케이스 처리 규칙

#### Step 3 — Domain 분리
도메인 책임을 Entity/Control 관점으로 분리해 결합도를 낮춘다.

- **BlankFinder**: 빈칸 위치 탐지
- **MissingNumberFinder**: 누락 숫자 후보 산출
- **MagicSquareValidator**: 행/열/대각선 합 및 불변조건 검증
- **Solver**: 탐색/조합 전략으로 해를 완성하고 결과 반환

#### Step 4 — Dual-Track 진행
UI와 Logic을 분리하되 동기화된 TDD 사이클로 진행한다.

- **UI RED / Logic RED 병렬**: 각 트랙에서 실패 테스트를 먼저 작성
- **GREEN 최소 구현**: 현재 실패 테스트를 통과하는 최소 코드만 반영
- **REFACTOR 통합 정리**: 중복 제거, 네이밍 정리, 레이어 경계 재확인

#### Step 5 — 회귀 보호
기능 완성 후 회귀 위험이 큰 영역을 테스트로 보강한다.

- **엣지 케이스 추가**: 경계값/최소-최대 입력
- **입력 오류 케이스 추가**: 스키마 위반, 타입 불일치, 중복/결측
- **조합 실패 케이스 추가**: 해가 존재하지 않는 구성, 탐색 실패 경로 검증

원하시면 이어서 이 Journey를 기준으로 **Level 3: Task(실행 가능한 작업 항목)**까지 바로 분해해드리겠습니다.

---

**User**

Level 3: User Stories를 다음 내용처럼 작성해 주세요.
Story 1 — 입력 검증
As a 학습자
I want to 입력이 정확히 4x4인지 검증되길 원한다
So that 잘못된 데이터가 Domain으로 전달되지 않도록 한다

Acceptance Criteria:
4x4가 아니면 예외
빈칸 2개 아니면 예외
중복 숫자 예외
범위 위반 예외

Story 2 — 빈칸 탐색
As a 학습자
I want to 0의 좌표를 정확히 찾고 싶다
So that 조합 시도가 가능하다

Acceptance Criteria:
row-major 순서 유지
정확히 2개 반환

Story 3 — 누락 숫자 탐색
Acceptance Criteria:
1~16 중 누락 2개
오름차순 반환

Story 4 — 마방진 판정
Acceptance Criteria:
모든 행 합 동일
모든 열 합 동일
대각선 동일

Story 5 — 두 조합 시도
Acceptance Criteria:
small→first blank 시도
실패 시 reverse
정답 배열 길이 6

---

**Cursor**

## Level 3: User Stories

### Story 1 — 입력 검증
**As a** 학습자  
**I want to** 입력이 정확히 4x4인지 검증되길 원한다  
**So that** 잘못된 데이터가 Domain으로 전달되지 않도록 한다

**Acceptance Criteria**
- 4x4 형식이 아니면 예외를 반환한다.
- 빈칸(0) 개수가 2개가 아니면 예외를 반환한다.
- 중복 숫자가 있으면 예외를 반환한다.
- 허용 범위(1~16, 빈칸은 0) 위반 시 예외를 반환한다.

---

### Story 2 — 빈칸 탐색
**As a** 학습자  
**I want to** 0의 좌표를 정확히 찾고 싶다  
**So that** 조합 시도가 가능하다

**Acceptance Criteria**
- 빈칸 좌표는 row-major 순서로 반환한다.
- 빈칸 좌표는 정확히 2개를 반환한다.

---

### Story 3 — 누락 숫자 탐색
**As a** 학습자  
**I want to** 1~16 범위에서 누락된 숫자 2개를 찾고 싶다  
**So that** Solver가 후보 조합을 생성할 수 있다

**Acceptance Criteria**
- 1~16 중 누락 숫자 2개를 반환한다.
- 반환 순서는 오름차순을 유지한다.

---

### Story 4 — 마방진 판정
**As a** 학습자  
**I want to** 현재 보드가 마방진 조건을 만족하는지 판정하고 싶다  
**So that** 유효한 해인지 검증할 수 있다

**Acceptance Criteria**
- 모든 행의 합이 동일해야 한다.
- 모든 열의 합이 동일해야 한다.
- 두 대각선의 합이 동일해야 한다.

---

### Story 5 — 두 조합 시도
**As a** 학습자  
**I want to** 누락 숫자 2개의 배치를 두 가지 경우로 시도하고 싶다  
**So that** 정답 후보를 빠르게 결정할 수 있다

**Acceptance Criteria**
- 작은 수를 첫 번째 빈칸에 우선 배치해 시도한다.
- 첫 시도 실패 시 reverse 배치를 시도한다.
- 최종 정답 배열 길이는 6이어야 한다.

원하시면 다음으로 각 Story를 `Task` 단위(테스트 케이스/구현 작업/완료 정의)로 바로 쪼개드리겠습니다.

---

**User**

Level 4:구현 시나리오 - Technical를 다음 내용처럼 작성해 주세요.
Feature: 4x4 마방진 완성

  불변조건 기반 로직을 검증하기 위해
  TDD를 연습하는 개발자로서
  부분적으로 채워진 4x4 마방진을 완성하고 싶다

  Background:
    Given 4x4 행렬이 주어지고
    And 0은 빈칸을 의미하며
    And 정확히 2개의 셀이 0을 포함하고 있고
    And 숫자는 1부터 16 사이여야 하며
    And 0을 제외한 중복 숫자는 허용되지 않으며
    And 4x4의 마방진 상수는 34이다

  Scenario: 작은 수 → 큰 수 순서로 마방진이 완성되는 경우
    Given 다음과 같은 행렬이 주어졌을 때:
      | 16 |  2 |  3 | 13 |
      |  5 | 11 | 10 |  8 |
      |  9 |  7 |  0 | 12 |
      |  4 | 14 | 15 |  0 |
    When 시스템이 빈칸 좌표를 찾고
    And 누락된 두 숫자를 찾은 뒤
    And 작은 숫자를 첫 번째 빈칸에 배치하고
    And 큰 숫자를 두 번째 빈칸에 배치하면
    Then 모든 행의 합은 34여야 하고
    And 모든 열의 합은 34여야 하며
    And 두 대각선의 합도 34여야 하고
    And 결과는 길이 6의 배열로 반환되어야 하며
    And 반환되는 좌표는 1-index 기준이어야 한다

  Scenario: 역순 배치 시 마방진이 완성되는 경우
    Given 다음과 같은 행렬이 주어졌을 때:
      | 16 |  2 |  3 | 13 |
      |  5 | 11 | 10 |  8 |
      |  9 |  7 |  0 | 12 |
      |  4 | 14 | 15 |  0 |
    When 작은 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되지 않고
    And 큰 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되면
    Then 시스템은 역순 배치 결과를 반환해야 하며
    And 최종 행렬은 마방진 상수 34를 만족해야 한다

  Scenario: 빈칸 개수가 올바르지 않은 경우
    Given 행렬에 빈칸이 1개만 존재할 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다

  Scenario: 중복 숫자가 존재하는 경우
    Given 0을 제외한 중복 숫자가 포함된 행렬일 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다

  Scenario: 값의 범위를 벗어난 경우
    Given 행렬에 16을 초과하는 숫자가 포함되어 있을 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다

---

**Cursor**

## Level 4: 구현 시나리오 - Technical

```gherkin
Feature: 4x4 마방진 완성

  불변조건 기반 로직을 검증하기 위해
  TDD를 연습하는 개발자로서
  부분적으로 채워진 4x4 마방진을 완성하고 싶다

  Background:
    Given 4x4 행렬이 주어지고
    And 0은 빈칸을 의미하며
    And 정확히 2개의 셀이 0을 포함하고 있고
    And 숫자는 1부터 16 사이여야 하며
    And 0을 제외한 중복 숫자는 허용되지 않으며
    And 4x4의 마방진 상수는 34이다

  Scenario: 작은 수 → 큰 수 순서로 마방진이 완성되는 경우
    Given 다음과 같은 행렬이 주어졌을 때:
      | 16 |  2 |  3 | 13 |
      |  5 | 11 | 10 |  8 |
      |  9 |  7 |  0 | 12 |
      |  4 | 14 | 15 |  0 |
    When 시스템이 빈칸 좌표를 찾고
    And 누락된 두 숫자를 찾은 뒤
    And 작은 숫자를 첫 번째 빈칸에 배치하고
    And 큰 숫자를 두 번째 빈칸에 배치하면
    Then 모든 행의 합은 34여야 하고
    And 모든 열의 합은 34여야 하며
    And 두 대각선의 합도 34여야 하고
    And 결과는 길이 6의 배열로 반환되어야 하며
    And 반환되는 좌표는 1-index 기준이어야 한다

  Scenario: 역순 배치 시 마방진이 완성되는 경우
    Given 다음과 같은 행렬이 주어졌을 때:
      | 16 |  2 |  3 | 13 |
      |  5 | 11 | 10 |  8 |
      |  9 |  7 |  0 | 12 |
      |  4 | 14 | 15 |  0 |
    When 작은 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되지 않고
    And 큰 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되면
    Then 시스템은 역순 배치 결과를 반환해야 하며
    And 최종 행렬은 마방진 상수 34를 만족해야 한다

  Scenario: 빈칸 개수가 올바르지 않은 경우
    Given 행렬에 빈칸이 1개만 존재할 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다

  Scenario: 중복 숫자가 존재하는 경우
    Given 0을 제외한 중복 숫자가 포함된 행렬일 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다

  Scenario: 값의 범위를 벗어난 경우
    Given 행렬에 16을 초과하는 숫자가 포함되어 있을 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다
```

원하시면 다음 단계로 이 시나리오를 바로 `pytest` 테스트 케이스 형태(`tests/entity`, `tests/control`)로 변환해드리겠습니다.

---

**User**

Level 5: 시나리오 검증 및 정리를 다음 내용처럼 작성해 주세요.

시나리오 완성도 체크리스트
## ✅ 4레벨 일관성 확인

Epic → Journey
- [x] Epic의 성공 지표가 Journey에 반영됨
- [x] Journey의 모든 단계가 Epic 목표 달성에 기여
- [x] Pain Points가 명확히 정의됨

Journey → Story
- [x] Journey의 각 Stage마다 최소 1개 Story
- [x] Story가체적인 기능으로 변환됨
- [x] Acceptance Criteria가 측정 가능

Story → Technical
- [x] 모든 AC가 Gherkin 시나리오로 변환
- [x] Given-When-Then이 명확
- [x] 테스트 자동화 가능

## ✅ Edge Case 커버리지

정상 케이스
- [x] Happy Path 시나리오 존재

예외 케이스
- [x] 네트워크 오류
- [x] 권한 없음
- [x] 잘못된 입력
- [x] 중복 실행

경계 케이스
- [x] 최솟값, 최댓값
- [x] 빈 값
- [x] 특수 문자

## ✅ 사용자 중심성

실제 사용자 검증
- [ ] 현장 엔지니어 1명과 시나리오 리뷰
- [ ] 관리자 1명과 Journey 검증
- [ ] 피드백 반영

감정 흐름
- [x] 각 Journey Stage마다 감정 표시
- [x] 부정 → 긍정 전환 명확

## ✅ 구현 가능성

기술 검증
- [x] QR 스캔 라이브러리 조사 완료
- [x] 오프라인 DB 방식 결정
- [x] 자동 검증 알고리즘 설계

데이터 요구사항
- [x] 필요한 Entity 모두 정의됨 (Mission 2)
- [x] API 스펙 초안 작성

---

**Cursor**

## Level 5: 시나리오 검증 및 정리

시나리오 완성도 체크리스트

## ✅ 4레벨 일관성 확인

Epic → Journey
- [x] Epic의 성공 지표가 Journey에 반영됨
- [x] Journey의 모든 단계가 Epic 목표 달성에 기여
- [x] Pain Points가 명확히 정의됨

Journey → Story
- [x] Journey의 각 Stage마다 최소 1개 Story
- [x] Story가 구체적인 기능으로 변환됨
- [x] Acceptance Criteria가 측정 가능

Story → Technical
- [x] 모든 AC가 Gherkin 시나리오로 변환
- [x] Given-When-Then이 명확
- [x] 테스트 자동화 가능

## ✅ Edge Case 커버리지

정상 케이스
- [x] Happy Path 시나리오 존재

예외 케이스
- [x] 네트워크 오류
- [x] 권한 없음
- [x] 잘못된 입력
- [x] 중복 실행

경계 케이스
- [x] 최솟값, 최댓값
- [x] 빈 값
- [x] 특수 문자

## ✅ 사용자 중심성

실제 사용자 검증
- [ ] 현장 엔지니어 1명과 시나리오 리뷰
- [ ] 관리자 1명과 Journey 검증
- [ ] 피드백 반영

감정 흐름
- [x] 각 Journey Stage마다 감정 표시
- [x] 부정 → 긍정 전환 명확

## ✅ 구현 가능성

기술 검증
- [x] QR 스캔 라이브러리 조사 완료
- [x] 오프라인 DB 방식 결정
- [x] 자동 검증 알고리즘 설계

데이터 요구사항
- [x] 필요한 Entity 모두 정의됨 (Mission 2)
- [x] API 스펙 초안 작성

원하시면 다음으로 Magic Square 도메인에 맞게 위 체크리스트의 `네트워크/권한/QR` 항목을 `입력 계약/불변조건/Solver 조합 검증` 중심으로 재정렬한 버전도 만들어드리겠습니다.

---

**User**

Report 폴더에 보고서로 내보내줘.

---

**Cursor**

요청하신 내용(작성한 Level 1~5)을 `Report` 폴더에 보고서 파일로 정리해 내보내겠습니다. 먼저 기존 보고서 네이밍 규칙을 확인한 뒤 동일한 형식으로 새 파일을 생성하겠습니다.

기존 규칙에 맞춰 `04_..._Report.md` 파일을 새로 만들고, 방금까지 확정한 Level 1~5 내용을 한 문서에 통합해 저장하겠습니다.

보고서를 `Report` 폴더로 내보냈습니다.

- 생성 파일: `Report/04_MagicSquare_User_Journey_Report.md`
- 포함 내용: Level 1(Epic) ~ Level 5(시나리오 검증 및 정리) 전체

원하시면 다음으로 `03_MagicSquare_CursorRules_Report.md`와 형식을 맞춰 목차(TOC)와 버전/작성일 섹션도 추가해드리겠습니다.

