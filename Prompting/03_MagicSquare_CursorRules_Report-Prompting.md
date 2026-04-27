# YAML configuration for MagicSquare project
_Exported on 4/27/2026 at 17:18:13 GMT+9 from Cursor (3.2.11)_

---

**User**

1단계 — 뼈대 생성
```
MagicSquare 프로젝트의 .cursorrules YAML 파일 뼈대를 만들어줘.
아래 최상위 키만 포함하고 값은 비워둬:
project, code_style, architecture, tdd_rules, testing, forbidden, file_structure, ai_behavior
각 키 앞에 80자짜리 # 구분선 주석을 추가해.
YAML 내용만 출력해.
```
2단계 — 섹션별로 채우기
```
위 .cursorrules 파일의 tdd_rules 섹션을 채워줘.
  - red_phase: 테스트 먼저 작성, 실패 확인 후 다음 단계 진행 조건
  - green_phase: 최소 코드로만 테스트 통과, 이 단계에서 리팩터링 금지
  - refactor_phase: 기능 변경 없이 구조 개선, 커버리지 유지 조건
YAML 형식 유지. tdd_rules 블록만 출력해.
```
3단계 — 검토 요청
```
방금 완성한 .cursorrules 파일을 검토해줘.
아래 항목을 확인해:
1. YAML 문법 오류
2. 누락된 필수 섹션
3. tdd_rules와 forbidden 규칙 간의 충돌
4. Cursor AI가 실제로 따를 수 없는 ai_behavior 규칙

---

**Cursor**

요청하신 3단계를 순서대로 처리하겠습니다. 먼저 `.cursorrules` 작성 관련 스킬 지침을 확인한 뒤, 1단계/2단계 결과를 YAML로 제공하고 3단계 검토까지 이어서 진행하겠습니다.

```yaml
################################################################################
project:

################################################################################
code_style:

################################################################################
architecture:

################################################################################
tdd_rules:

################################################################################
testing:

################################################################################
forbidden:

################################################################################
file_structure:

################################################################################
ai_behavior:
```

```yaml
tdd_rules:
  red_phase:
    rule: "테스트를 먼저 작성하고 반드시 실패를 확인한다."
    proceed_condition:
      - "새 테스트가 실제로 실패(RED)한 로그/결과가 확인될 것"
      - "실패 원인이 테스트 의도와 일치할 것"
  green_phase:
    rule: "테스트를 통과시키는 최소 코드만 작성한다."
    constraints:
      - "새 기능/최적화/구조개선 추가 금지"
      - "이 단계에서는 리팩터링 금지"
  refactor_phase:
    rule: "기능 동작을 바꾸지 않고 구조만 개선한다."
    proceed_condition:
      - "모든 테스트가 계속 통과할 것"
      - "커버리지가 기존 수준 이상으로 유지될 것"
```

- YAML 문법 오류: 현재 구성(1단계 뼈대 + 2단계 `tdd_rules`) 기준으로 문법상 문제 없음
- 누락된 필수 섹션: 요청한 최상위 8개 섹션 모두 존재함
- `tdd_rules` 와 `forbidden` 충돌: `forbidden` 내용이 비어 있어 현재 기준 명시적 충돌 없음
- Cursor AI가 따를 수 없는 `ai_behavior` 규칙: `ai_behavior`가 비어 있어 현재 기준 실행 불가 규칙 없음

---

**User**

위에서 만든 .cursorrules 뼈대의 빈 섹션을 모두 채워줘.
MagicSquare 프로젝트 기준으로 작성해.

각 섹션 작성 규칙:

code_style:
  - python_version: "3.10+"
  - style_guide: PEP8 엄격 준수
  - type_hints: 모든 함수 파라미터와 반환값에 필수
  - docstring: Google 스타일, 모든 public 메서드에 필수
  - max_line_length: 88 (Black 기준)

architecture:
  ECB 패턴 3 레이어를 각각 정의해줘:
  - boundary: 외부 입출력 담당 (UI, API, CLI)
  - control: 비즈니스 로직 담당
  - entity: 도메인 데이터 및 규칙 담당
  레이어 간 의존성 방향도 명시해줘.

tdd_rules:
  지금은 문자열 1줄인데, 하위 항목으로 세분화해줘.
  각 phase마다:
    - description: 단계 설명
    - rules: 지켜야 할 규칙 목록
    - must_not: 이 단계에서 하면 안 되는 것

testing:
  - framework: pytest
  - pattern: AAA (Arrange-Act-Assert)
  - coverage_minimum: 80%
  - fixture_scope: 규칙 정의
  - naming_convention: test_ 접두사 필수

forbidden:
  항목마다 아래 구조로 작성:
    pattern: 금지 패턴
    reason: 금지 이유
    alternative: 대신 써야 할 것
  최소 포함 항목: print(), 하드코딩 상수, except 단독 사용

file_structure:
  ECB 기준 폴더 구조를 트리 형태 주석으로 작성해줘.
  boundary/, control/, entity/, tests/ 포함.

ai_behavior:
  Cursor AI가 코드 생성 전·중·후에 반드시 따라야 할 규칙.
  최소 포함:
    - 코드 작성 전 관련 테스트 파일 확인
    - ECB 레이어 경계 위반 금지
    - 타입힌트 없는 함수 생성 금지
    - tdd_rules 위반 시 경고 출력

완성된 .cursorrules 전체 파일을 출력해줘.

---

**Cursor**

```yaml
################################################################################
project:
  name: MagicSquare
  domain: "NxN 매직스퀘어 생성/검증"
  language: Python
  runtime: "3.10+"
  primary_goal:
    - "정확한 매직스퀘어 생성 로직 구현"
    - "ECB 아키텍처와 TDD 기반 개발 유지"

################################################################################
code_style:
  python_version: "3.10+"
  style_guide: "PEP8 엄격 준수"
  type_hints: "모든 함수 파라미터와 반환값에 필수"
  docstring: "Google 스타일, 모든 public 메서드에 필수"
  max_line_length: 88

################################################################################
architecture:
  pattern: ECB
  layers:
    boundary:
      role: "외부 입출력 담당 (UI, API, CLI)"
      responsibilities:
        - "사용자/외부 요청 수신 및 응답 포맷팅"
        - "입력 파싱 및 기본 검증"
        - "Control 레이어 호출"
    control:
      role: "비즈니스 로직 담당"
      responsibilities:
        - "유스케이스 오케스트레이션"
        - "Entity 규칙 호출 및 흐름 제어"
        - "Boundary에 전달할 결과 구성"
    entity:
      role: "도메인 데이터 및 규칙 담당"
      responsibilities:
        - "매직스퀘어 도메인 모델/불변식 관리"
        - "핵심 계산/검증 규칙 제공"
        - "외부 I/O 의존성 없이 순수 로직 유지"
  dependency_direction:
    allowed:
      - "boundary -> control"
      - "control -> entity"
    forbidden:
      - "entity -> control"
      - "entity -> boundary"
      - "control -> boundary (직접 출력/입력 처리)"
  boundary_rules:
    - "상위 레이어는 하위 레이어 인터페이스만 의존"
    - "하위 레이어는 상위 레이어 구현 세부사항을 알지 못함"

################################################################################
tdd_rules:
  red_phase:
    description: "실패하는 테스트를 먼저 작성하여 요구사항을 명세하는 단계"
    rules:
      - "구현 코드 작성 전에 테스트를 먼저 추가한다."
      - "새 테스트가 실패(RED)하는 것을 반드시 실행으로 확인한다."
      - "실패 원인이 테스트 의도(요구사항)와 일치하는지 확인한다."
    must_not:
      - "테스트 없이 구현 코드를 먼저 작성하지 않는다."
      - "실패 확인 없이 GREEN 단계로 넘어가지 않는다."
      - "기존 테스트를 임의 수정해 실패를 숨기지 않는다."
  green_phase:
    description: "테스트를 통과시키기 위한 최소 구현만 작성하는 단계"
    rules:
      - "현재 실패한 테스트를 통과시키는 최소 코드만 작성한다."
      - "변경 범위는 해당 테스트 통과에 필요한 부분으로 제한한다."
      - "테스트 전체를 실행해 회귀가 없는지 확인한다."
    must_not:
      - "리팩터링(구조 개선/이름 정리/중복 제거)을 수행하지 않는다."
      - "요구사항 외 최적화나 부가 기능을 추가하지 않는다."
      - "테스트를 약화시키는 방식으로 통과시키지 않는다."
  refactor_phase:
    description: "동작을 바꾸지 않고 구조를 개선하는 단계"
    rules:
      - "외부 관찰 가능한 기능 동작은 유지한다."
      - "중복 제거, 네이밍 개선, 책임 분리 등 구조 개선만 수행한다."
      - "리팩터링 후 전체 테스트 통과를 확인한다."
      - "커버리지는 기존 수준 이상으로 유지한다."
    must_not:
      - "새 기능을 추가하거나 기존 요구사항 동작을 변경하지 않는다."
      - "테스트를 삭제/약화하여 품질 지표를 낮추지 않는다."
      - "레이어 경계를 침범하는 의존성 추가를 하지 않는다."

################################################################################
testing:
  framework: pytest
  pattern: AAA
  coverage_minimum: "80%"
  fixture_scope:
    default: function
    rules:
      - "상태 공유가 필요한 경우에만 class/module/session scope 사용"
      - "scope 확장은 테스트 독립성 훼손이 없을 때만 허용"
      - "fixture는 목적이 드러나는 이름으로 작성"
  naming_convention:
    test_file_prefix: "test_"
    test_function_prefix: "test_"
    required: true

################################################################################
forbidden:
  - pattern: "print() 사용"
    reason: "테스트/운영 로그 일관성을 해치고 디버깅 출력이 코드에 잔존할 수 있음"
    alternative: "logging 모듈(레벨 기반) 또는 pytest caplog 사용"
  - pattern: "하드코딩 상수 (매직 넘버/문자열)"
    reason: "의도 파악이 어렵고 변경 비용 증가, 중복 유발"
    alternative: "의미 있는 상수명으로 entity/constants 모듈에 정의"
  - pattern: "except: (예외 타입 없는 단독 except)"
    reason: "시스템 종료 예외 포함 광범위 예외를 숨겨 장애 원인 추적이 어려움"
    alternative: "구체 예외 타입 명시 (예: except ValueError as e) 후 로깅/재전파"

################################################################################
file_structure:
  root: src
  # ECB 기준 권장 트리
  # src/
  #   boundary/
  #     cli/
  #     api/
  #   control/
  #     use_cases/
  #     services/
  #   entity/
  #     models/
  #     rules/
  # tests/
  #   boundary/
  #   control/
  #   entity/
  directories:
    - "src/boundary/"
    - "src/control/"
    - "src/entity/"
    - "tests/"
  mapping_rules:
    - "Boundary 테스트는 tests/boundary/에 배치"
    - "Control 테스트는 tests/control/에 배치"
    - "Entity 테스트는 tests/entity/에 배치"

################################################################################
ai_behavior:
  before_codegen:
    - "코드 작성 전 반드시 관련 테스트 파일(기존/신규 대상)을 확인한다."
    - "요구사항을 red_phase 기준으로 테스트 케이스로 먼저 분해한다."
  during_codegen:
    - "ECB 레이어 경계를 위반하는 참조/호출을 생성하지 않는다."
    - "타입힌트 없는 함수(파라미터/반환) 생성을 금지한다."
    - "public 메서드에는 Google 스타일 docstring을 포함한다."
  after_codegen:
    - "pytest를 실행하여 변경 영향 테스트를 확인한다."
    - "TDD 단계 위반이 감지되면 즉시 경고를 출력하고 수정 가이드를 제시한다."
    - "커버리지 기준(80% 이상) 미달 시 원인과 보완 테스트를 제안한다."
  enforcement:
    tdd_violation_warning: "경고: TDD 규칙 위반 가능성이 있습니다. RED->GREEN->REFACTOR 순서를 확인하세요."
```

---

**User**

Report 폴더에 보고서로 내보내줘.

---

**Cursor**

요청하신 내용을 `Report` 폴더에 새 보고서 파일로 저장하겠습니다. 먼저 기존 보고서 네이밍 패턴을 확인한 뒤, 방금 완성한 `.cursorrules` 전체 내용을 같은 형식의 문서로 내보내겠습니다.

기존 형식에 맞춰 `03_..._Report.md` 파일을 추가하고, 방금 확정한 `.cursorrules` 전체 YAML을 그대로 포함해 저장하겠습니다.

`Report` 폴더에 보고서로 내보냈습니다.

- 생성 파일: `Report/03_MagicSquare_CursorRules_Report.md`
- 내용: 방금 확정한 `.cursorrules` 전체 YAML 포함

원하시면 같은 내용을 프로젝트 루트의 실제 설정 파일인 `.cursorrules`로도 바로 저장해드릴게요.

---

**User**

.cursorrules 파일을 생성해줘.

파일 내용만 출력해. 설명, 마크다운 코드블록 불필요.

--- 프로젝트 정보 ---
프로젝트명: MagicSquare
설명: [한 줄로 프로젝트 설명 작성]
방법론: Dual-Track UI + Logic TDD with MLOps

--- 반드시 포함할 섹션 ---

1. project          → 프로젝트명, 설명, 방법론
2. code_style       → PEP8 엄격 준수, 타입힌트 필수(Python 3.10+), Google 스타일 docstring
3. architecture     → ECB 패턴 (boundary / control / entity 레이어별 역할 정의)
4. tdd_rules        → red_phase / green_phase / refactor_phase 각 단계별 규칙
5. testing          → pytest AAA 패턴(Arrange-Act-Assert), fixture 규칙, 커버리지 기준
6. forbidden        → print() 디버깅 금지, 그 외 금지 패턴 목록
7. file_structure   → 레이어별 폴더 구조 예시
8. ai_behavior      → 코드 생성 시 Cursor AI가 반드시 따라야 할 행동 규칙

--- 형식 규칙 ---
- YAML 형식, 들여쓰기 2 스페이스
- 각 섹션 앞에 80자 # 구분선 + 섹션 제목 주석
- 키는 영어, 설명은 한국어로 작성
- tdd_rules 하위에 red_phase / green_phase / refactor_phase 동일 깊이로 작성
- forbidden 항목마다 reason(이유)과 alternative(대안)을 함께 명시

---

**Cursor**

요청 형식 그대로 `.cursorrules` 파일을 생성하고, 최종 답변에는 파일 내용만 그대로 출력하겠습니다.

이제 프로젝트 루트에 `.cursorrules`를 새로 만들고, 지정하신 섹션/형식 규칙을 모두 반영해 작성합니다.

################################################################################
# project
project:
  name: MagicSquare
  description: 4x4 매직스퀘어를 UI와 로직 이중 트랙 TDD로 설계·구현·검증하는 프로젝트
  methodology: Dual-Track UI + Logic TDD with MLOps

################################################################################
# code_style
code_style:
  python_version: "3.10+"
  style_guide: PEP8 엄격 준수
  type_hints: 모든 함수 파라미터와 반환값에 타입힌트 필수
  docstring: Google 스타일 docstring을 모든 public 함수/메서드에 필수 적용
  max_line_length: 88

################################################################################
# architecture
architecture:
  pattern: ECB
  layers:
    boundary:
      role: UI/API/CLI 등 외부 입출력을 처리하고 입력/출력을 표준 형식으로 변환
    control:
      role: 유스케이스 흐름을 조정하고 비즈니스 로직 실행을 오케스트레이션
    entity:
      role: 도메인 데이터 구조와 핵심 규칙(불변조건, 계산 규칙)을 보유
  dependency_direction:
    - boundary -> control
    - control -> entity
    - entity는 상위 레이어에 의존 금지

################################################################################
# tdd_rules
tdd_rules:
  red_phase:
    description: 실패하는 테스트를 먼저 작성해 요구사항을 명확히 정의하는 단계
    rules:
      - 구현 코드보다 테스트 코드를 먼저 작성한다.
      - 새 테스트가 실제로 실패하는지 실행으로 확인한다.
      - 실패 원인이 요구사항과 일치하는지 점검한다.
    must_not:
      - 테스트 작성 전에 구현 코드를 작성하지 않는다.
      - 실패 확인 없이 green_phase로 진행하지 않는다.
  green_phase:
    description: 테스트를 통과시키기 위한 최소 구현만 추가하는 단계
    rules:
      - 현재 실패 테스트를 통과시키는 최소 코드만 작성한다.
      - 변경 범위를 해당 테스트의 요구사항으로 제한한다.
      - 통과 후 관련 테스트를 재실행해 회귀를 확인한다.
    must_not:
      - 구조 개선이나 코드 정리 목적의 리팩터링을 수행하지 않는다.
      - 요구사항 외 기능/최적화를 추가하지 않는다.
  refactor_phase:
    description: 기능 동작 변경 없이 구조를 개선하고 가독성을 높이는 단계
    rules:
      - 외부 동작을 바꾸지 않는 범위에서 구조를 개선한다.
      - 중복 제거, 명확한 네이밍, 책임 분리를 우선 적용한다.
      - 리팩터링 후 전체 테스트 통과와 커버리지 유지 여부를 확인한다.
    must_not:
      - 신규 기능 추가나 기존 요구사항 변경을 하지 않는다.
      - 테스트를 약화하거나 삭제해 품질 지표를 낮추지 않는다.

################################################################################
# testing
testing:
  framework: pytest
  pattern: AAA (Arrange-Act-Assert)
  fixture_rules:
    default_scope: function
    policy:
      - 테스트 독립성을 기본 원칙으로 유지한다.
      - class/module/session scope는 성능 또는 공유 상태 필요 시에만 사용한다.
      - fixture 이름은 의도와 책임이 드러나도록 작성한다.
  coverage:
    minimum: "80%"
    target: 핵심 도메인(entity/control) 90% 이상 권장
  naming_convention:
    test_file_prefix: test_
    test_function_prefix: test_

################################################################################
# forbidden
forbidden:
  - pattern: print() 디버깅 출력
    reason: 로그 관리 일관성을 깨고 운영 환경에서 불필요 출력이 남을 수 있음
    alternative: logging 모듈의 레벨 기반 로깅 또는 pytest caplog 사용
  - pattern: except: 단독 사용
    reason: 예외 원인 추적이 어려워지고 시스템 예외까지 숨길 위험이 있음
    alternative: 구체 예외 타입 지정(except ValueError as e) 후 처리/재전파
  - pattern: 하드코딩된 매직 넘버/문자열
    reason: 변경 비용 증가와 의미 불명확성으로 유지보수성이 저하됨
    alternative: 상수 모듈에 의미 있는 이름으로 선언하여 참조
  - pattern: boundary에서 entity 직접 호출
    reason: 레이어 경계가 무너져 책임 분리가 약화됨
    alternative: boundary -> control -> entity 의존 방향을 준수

################################################################################
# file_structure
file_structure:
  example:
    - src/
    - src/boundary/
    - src/boundary/cli/
    - src/boundary/api/
    - src/control/
    - src/control/use_cases/
    - src/entity/
    - src/entity/models/
    - src/entity/rules/
    - tests/
    - tests/boundary/
    - tests/control/
    - tests/entity/

################################################################################
# ai_behavior
ai_behavior:
  before_codegen:
    - 관련 테스트 파일을 먼저 확인하고 테스트 의도를 요약한다.
    - ECB 레이어 경계와 의존 방향 위반 가능성을 사전 점검한다.
  during_codegen:
    - 타입힌트 없는 함수 생성을 금지한다.
    - public 함수/메서드에는 Google 스타일 docstring을 작성한다.
    - tdd_rules의 현재 단계 규칙을 벗어나는 변경을 금지한다.
  after_codegen:
    - pytest로 변경 영향 테스트를 실행해 결과를 확인한다.
    - tdd_rules 위반이 감지되면 즉시 경고를 출력하고 수정안을 제시한다.
    - 커버리지 기준 미달 시 누락 테스트 후보를 제안한다.

