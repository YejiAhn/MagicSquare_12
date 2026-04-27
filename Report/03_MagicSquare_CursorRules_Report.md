# MagicSquare .cursorrules Report

## 최종 .cursorrules

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
