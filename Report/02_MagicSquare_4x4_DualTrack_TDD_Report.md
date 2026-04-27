# 1) Logic Layer (Domain Layer) 설계

## 1.1 도메인 개념

### Entities / Value Objects / Domain Services 목록과 책임(SRP)

| 분류 | 이름 | 책임(SRP) | 검증 규칙 |
|---|---|---|---|
| Entity | MagicSquare4x4 | 4x4 행렬 상태를 보유하고 도메인 연산 입력을 제공 | 내부 상태는 유효성 검증 통과 행렬만 허용 |
| Value Object | CellPosition | 셀 좌표 표현 | 좌표는 1-index, row/col 각각 1~4 |
| Value Object | MissingNumbersPair | 누락 숫자 쌍 표현 | (small,big) 정렬, small < big, 각 1~16 |
| Value Object | PlacementPlan | 두 빈칸에 두 숫자 배치 계획 | 정확히 2개 배치, 빈칸 좌표와 일치 |
| Domain Service | BlankLocator | 빈칸(0) 두 위치 탐색 | 상->하, 좌->우 고정 스캔 순서 |
| Domain Service | MissingNumberFinder | 1~16에서 누락 숫자 2개 계산 | 0 제외 중복 없는 입력만 처리 |
| Domain Service | MagicSquareJudge | 마방진 성립 여부 판정 | 4x4 기준 Magic Constant=34 사용 |
| Domain Service | DualPlacementResolver | 두 배치 조합 시도 후 결과 결정 | 출력은 반드시 int[6] 계약 준수 |

## 1.2 도메인 불변조건(Invariants)

| ID | 불변조건 | 검증 가능한 규칙 |
|---|---|---|
| I-01 | 행렬 크기 고정 | `rows == 4` AND `for all row: row.length == 4` |
| I-02 | 빈칸 개수 고정 | `count(value == 0) == 2` |
| I-03 | 값 범위 고정 | `value in {0} U [1..16]` |
| I-04 | 0 제외 중복 금지 | `duplicates(nonZeroValues) == false` |
| I-05 | Magic Constant 고정 | `M = 4 * (16 + 1) / 2 = 34` |
| I-06 | 라인 합 일치 | 4개 행 + 4개 열 + 2개 대각선 합이 모두 34 |
| I-07 | 출력 형식 고정 | 결과 길이 6, `[r1,c1,n1,r2,c2,n2]`, 좌표 1-index |
| I-08 | 조합 선택 규칙 고정 | (small->첫빈칸, big->둘째빈칸) 성립 시 그 순서, 아니면 반대 |

## 1.3 핵심 유스케이스(도메인 관점)

| Use Case | 입력 | 출력 | 실패조건 |
|---|---|---|---|
| UC-D-01 빈칸 찾기 | 유효한 4x4 행렬 | `CellPosition[2]` | 빈칸 수가 2가 아니면 실패 |
| UC-D-02 누락 숫자 찾기 | 유효한 4x4 행렬 | `MissingNumbersPair(small,big)` | 누락 숫자를 정확히 2개 확정 못하면 실패 |
| UC-D-03 마방진 판정 | 숫자 채워진 4x4 행렬 | `boolean` | 행렬 크기 위반 시 실패 |
| UC-D-04 두 조합 시도 | 원본 행렬 + 빈칸 2개 + 누락숫자 2개 | `int[6]` | 두 조합 모두 실패 시 도메인 실패 |

## 1.4 Domain API(내부 계약)

| API 시그니처(코드 아님) | 입력 | 출력 | 실패조건 |
|---|---|---|---|
| `createMatrix(matrix:int[][]): MagicSquare4x4` | I-01/I-03/I-04 만족 | Domain Entity | `DOMAIN_MATRIX_SHAPE_INVALID`, `DOMAIN_VALUE_RANGE_INVALID`, `DOMAIN_DUPLICATE_NON_ZERO` |
| `locateBlanks(square:MagicSquare4x4): [CellPosition,CellPosition]` | I-02 만족 | 빈칸 2개(고정 순서) | `DOMAIN_BLANK_COUNT_INVALID` |
| `findMissingNumbers(square:MagicSquare4x4): MissingNumbersPair` | 중복 없는 non-zero 집합 | `(small,big)` | `DOMAIN_MISSING_NUMBERS_INVALID` |
| `isMagicAfterPlacement(square, plan): boolean` | plan이 빈칸 좌표와 일치 | `true/false` | `DOMAIN_PLACEMENT_INVALID` |
| `resolveResult(square:MagicSquare4x4): int[6]` | I-01~I-08 전제 | `[r1,c1,n1,r2,c2,n2]` | `DOMAIN_NO_VALID_PLACEMENT` |

## 1.5 Domain 단위 테스트 설계(RED 우선)

### 테스트 케이스 목록 (정상/비정상/엣지)

- D-RED-01: 유효 4x4 행렬 허용 (정상)
- D-RED-02: 4x3 행렬 거부 (비정상)
- D-RED-03: 빈칸 1개 거부 (비정상)
- D-RED-04: 빈칸 3개 거부 (비정상)
- D-RED-05: 값 17 거부 (엣지)
- D-RED-06: 음수 거부 (엣지)
- D-RED-07: 0 제외 중복 값 거부 (비정상)
- D-RED-08: Magic Constant=34 고정 검증 (정상)
- D-RED-09: small->첫빈칸 조합으로 성립 검증 (정상)
- D-RED-10: 반대 조합으로만 성립하는 경우 검증 (엣지)
- D-RED-11: 두 조합 모두 실패 시 도메인 실패 검증 (비정상)
- D-RED-12: 출력 길이/포맷 int[6] 검증 (정상)

### 각 테스트가 보호하는 invariant

| 테스트 | 보호 Invariant |
|---|---|
| D-RED-01 | I-01, I-03, I-04 |
| D-RED-02 | I-01 |
| D-RED-03, D-RED-04 | I-02 |
| D-RED-05, D-RED-06 | I-03 |
| D-RED-07 | I-04 |
| D-RED-08 | I-05 |
| D-RED-09, D-RED-10 | I-08 |
| D-RED-11 | I-06, I-08 |
| D-RED-12 | I-07 |

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)

## 2.1 사용자/호출자 관점 시나리오

1. 호출자가 `matrix:int[][]`를 전달한다.
2. UI Boundary가 입력 계약을 검증한다.
3. 검증 성공 시 Domain API를 1회 호출한다.
4. Domain 성공 시 결과를 고정 출력 스키마로 반환한다.
5. 검증 실패 또는 Domain 실패 시 표준 에러 스키마로 반환한다.

## 2.2 UI 계약(외부 계약)

### Input schema

```text
{
  matrix: int[][]
}
제약:
- 4x4
- 0 개수 정확히 2
- 값 범위: 0 또는 1~16
- 0 제외 중복 금지
```

### Output schema

```text
{
  result: int[6]
}
제약:
- 형식: [r1,c1,n1,r2,c2,n2]
- r1,c1,r2,c2는 1~4 (1-index)
- n1,n2는 누락 숫자 2개
- 순서 규칙: small->첫빈칸/ big->둘째빈칸 성립 시 해당 순서, 아니면 반대
```

### Error schema

```text
{
  code: string,
  message: string,
  details: string[]
}
```

## 2.3 UI 레벨 테스트(Contract-first, RED 우선)

- UI-RED-01: 잘못된 행 개수 -> `400 VALIDATION_ERROR`, Domain 호출 0회
- UI-RED-02: 잘못된 열 개수 -> `400 VALIDATION_ERROR`, Domain 호출 0회
- UI-RED-03: 빈칸 개수 오류 -> `400 VALIDATION_ERROR`, Domain 호출 0회
- UI-RED-04: 값 범위 오류 -> `400 VALIDATION_ERROR`, Domain 호출 0회
- UI-RED-05: 중복 오류 -> `400 VALIDATION_ERROR`, Domain 호출 0회
- UI-RED-06: Domain 성공 mock -> `200 OK`, `result` 길이 6 검증
- UI-RED-07: Domain 실패 mock(`NO_VALID_PLACEMENT`) -> `422 DOMAIN_NO_VALID_PLACEMENT`
- UI-RED-08: 출력 포맷 위반 감지 -> `500 INTERNAL_CONTRACT_BROKEN`

## 2.4 UX/출력 규칙

### 에러 메시지 표준 규칙

- 규칙 E-STD-01: `message`는 고정 문자열이어야 한다.
- 규칙 E-STD-02: `details`는 실패 필드명/규칙 ID만 포함한다.
- 규칙 E-STD-03: `code`는 `E-VAL-*`, `E-DOM-*`, `E-DATA-*` 네임스페이스를 따른다.
- 규칙 E-STD-04: 저장소 구현 세부사항(경로, 스택트레이스)을 message에 포함하지 않는다.

### 고정 메시지 카탈로그

- E-VAL-001: `Matrix must be 4x4.`
- E-VAL-002: `Matrix must contain exactly two zeros.`
- E-VAL-003: `Each value must be 0 or between 1 and 16.`
- E-VAL-004: `Non-zero values must be unique.`
- E-DOM-001: `No valid placement makes a magic square.`
- E-DATA-001: `Unable to load saved matrix.`
- E-DATA-002: `Unable to save execution result.`

# 3) Data Layer 설계 (Data Layer)

## 3.1 목적 정의

- 목적 D-PUR-01: TDD 회귀 재현을 위한 입력 저장/로드
- 목적 D-PUR-02: 실패 케이스 재실행을 위한 fixture 고정
- 범위 D-SCP-01: 입력 행렬 저장/로드는 필수
- 범위 D-SCP-02: 실행 결과 저장/로드는 선택
- 제외 D-OUT-01: DB/네트워크/트랜잭션은 범위 밖

## 3.2 인터페이스 계약

| 메서드(코드 아님) | 입력 전제 | 출력 | 실패조건 |
|---|---|---|---|
| `saveMatrix(id:string, matrix:int[][]): SaveAck` | id 비어있지 않음, 입력 계약 통과 | `{id,savedAt}` | `DATA_SAVE_FAILED` |
| `loadMatrix(id:string): int[][]` | id 비어있지 않음 | 4x4 행렬 | `DATA_NOT_FOUND`, `DATA_FORMAT_INVALID` |
| `saveResult(id:string, result:int[6]): SaveAck` | id 비어있지 않음, 길이 6 | `{id,savedAt}` | `DATA_SAVE_FAILED` |
| `loadResult(id:string): int[6]` | id 비어있지 않음 | 길이 6 결과 | `DATA_NOT_FOUND`, `DATA_FORMAT_INVALID` |

## 3.3 구현 옵션 비교(메모리/파일)

| 옵션 | 장점 | 단점 | 적합 용도 |
|---|---|---|---|
| 옵션 A: InMemory | 테스트 속도 빠름, IO 불안정성 없음, Mock/Fake 단순 | 프로세스 종료 시 데이터 소실 | 기본 TDD 루프 |
| 옵션 B: File(JSON/CSV) | 실행 간 데이터 유지, 수동 점검 쉬움 | 파일 없음/형식오류/인코딩 이슈 | 보조 회귀/학습 시나리오 |

### 추천안

- **추천: 옵션 A(InMemory)**
- 이유 1: RED-GREEN-REFACTOR 사이클 시간을 최소화한다.
- 이유 2: 실패 원인을 도메인/경계 규칙으로 좁혀 디버깅 분기를 줄인다.
- 이유 3: 파일 어댑터는 통합 테스트에서 별도 대상으로 검증 가능하다.

## 3.4 Data 레이어 테스트

- DATA-RED-01: saveMatrix 후 loadMatrix 값 완전 일치
- DATA-RED-02: saveResult 후 loadResult 값 완전 일치
- DATA-RED-03: 없는 id load 시 `DATA_NOT_FOUND`
- DATA-RED-04: 형식 손상 파일 load 시 `DATA_FORMAT_INVALID`
- DATA-RED-05: 로드된 행렬이 4x4 아니면 반환 거부
- DATA-RED-06: 로드된 행렬에서 빈칸 2개 아니면 반환 거부

# 4) Integration & Verification (통합 및 검증)

## 4.1 통합 경로 정의

```text
UI Boundary -> Application Facade(선택) -> Domain -> Data Interface -> Data Adapter
```

- 의존성 방향 규칙 INT-DEP-01: 바깥 레이어가 안쪽 레이어 추상화에 의존한다.
- 의존성 방향 규칙 INT-DEP-02: Domain은 UI/Data 구현체를 참조하지 않는다.
- 의존성 방향 규칙 INT-DEP-03: Data Adapter는 Domain 계약 위반 데이터를 반환하지 않는다.

## 4.2 통합 테스트 시나리오

### 정상 시나리오 (2개 이상)

- INT-OK-01: 유효 입력 A -> `200` + `int[6]` 반환
- INT-OK-02: 유효 입력 B(스왑 조합만 성립) -> `200` + 스왑 규칙 적용 결과 반환

### 실패 시나리오 (3개 이상)

- INT-FAIL-01: 입력 크기 오류 -> `400 VALIDATION_ERROR`
- INT-FAIL-02: 도메인 조합 실패 -> `422 DOMAIN_NO_VALID_PLACEMENT`
- INT-FAIL-03: 데이터 로드 대상 없음 -> `404 DATA_NOT_FOUND`
- INT-FAIL-04: 데이터 형식 오류 -> `422 DATA_FORMAT_INVALID`
- INT-FAIL-05: 데이터 저장 실패 -> `500 DATA_SAVE_FAILED`

## 4.3 회귀 보호 규칙

- REG-01: 기존 통과 테스트 삭제 금지 (CI에서 삭제 수 0 강제)
- REG-02: Input/Output/Error 계약 스키마 변경 금지 (승인 없는 변경 실패)
- REG-03: 출력 배열 포맷 `[r1,c1,n1,r2,c2,n2]` 변경 금지
- REG-04: 에러 코드/메시지 카탈로그 변경 시 계약 테스트 동시 갱신 필수
- REG-05: 리팩토링 전후 전체 테스트 결과 동등성 유지

## 4.4 커버리지 목표

- Domain Logic: **95%+**
- UI Boundary: **85%+**
- Data Layer: **80%+**

측정 규칙:
- Domain은 분기 커버리지 포함, 조합 선택 분기 2개 모두 필수 커버
- UI는 입력 검증 분기 + 도메인 오류 매핑 분기 커버
- Data는 save/load 성공/실패 경로 모두 커버

## 4.5 Traceability Matrix (필수)

| Concept(Invariant) | Rule | Use Case | Contract | Test | Component |
|---|---|---|---|---|---|
| I-01 Shape 4x4 | R-Shape-4x4 | UC-D-01, UC-D-03 | Input schema 4x4 | D-RED-02, UI-RED-01, UI-RED-02, DATA-RED-05 | InputValidator, MagicSquare4x4, RepositoryAdapter |
| I-02 Blank count=2 | R-Blank-Exactly-2 | UC-D-01 | Input schema zeros=2 | D-RED-03, D-RED-04, UI-RED-03, DATA-RED-06 | BlankLocator, InputValidator |
| I-03 Value range | R-Value-Range | UC-D-01 | Input schema value rule | D-RED-05, D-RED-06, UI-RED-04 | RangeValidator |
| I-04 Non-zero unique | R-Unique-NonZero | UC-D-02 | Input schema uniqueness | D-RED-07, UI-RED-05 | DuplicateValidator, MissingNumberFinder |
| I-05 Magic Constant=34 | R-Magic-Constant | UC-D-03 | Domain Judge contract | D-RED-08 | MagicSquareJudge |
| I-06 Line sums=34 | R-Line-Sum-Equality | UC-D-03, UC-D-04 | isMagicAfterPlacement contract | D-RED-11, INT-OK-01 | MagicSquareJudge, DualPlacementResolver |
| I-07 Output int[6] | R-Output-Format | UC-D-04 | Output schema result:int[6] | D-RED-12, UI-RED-06, INT-OK-01 | DualPlacementResolver, UIBoundarySerializer |
| I-08 Ordering fallback | R-Order-Decision | UC-D-04 | Output ordering rule | D-RED-09, D-RED-10, INT-OK-02 | DualPlacementResolver |

---

체크리스트:

- [x] 구현 코드 미포함
- [x] UI를 Boundary 계약으로 정의
- [x] Data를 저장/로드 인터페이스 수준으로 제한
- [x] 입력/출력 계약 고정
- [x] 모든 규칙을 테스트로 검증 가능하게 명시
