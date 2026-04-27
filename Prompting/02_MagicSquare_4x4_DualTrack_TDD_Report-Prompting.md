# Magic Square TDD design and architecture
_Exported on 4/27/2026 at 16:52:45 GMT+9 from Cursor (3.2.11)_

---

**User**

당신은 Dual-Track UI + Logic TDD 및 Clean Architecture 설계 전문가입니다.

프로젝트: Magic Square (4x4) — TDD 연습용
목적: 알고리즘 난이도보다 “레이어 분리 + 계약 기반 테스트 + 리팩토링” 훈련
제약:
- 구현 코드는 작성하지 마십시오. (설계/계약/테스트/통합 계획만)
- UI는 실제 화면이 아니라 “입력/출력 경계(Boundary)”로 정의
- Data Layer는 DB가 아니라 “저장/로드 인터페이스(메모리/파일 교체 가능)” 수준만
- 입력/출력은 명확히 고정

입력 계약:
- 4x4 int[][] (0은 빈칸)
- 빈칸은 정확히 2개
- 값 범위: 0 또는 1~16
- 0 제외 중복 금지
출력 계약:
- int[6]
- 좌표는 1-index
- 반환 형식: [r1,c1,n1,r2,c2,n2]
- n1,n2는 두 누락 숫자이며, (작은수→첫빈칸, 큰수→둘째빈칸) 조합이 마방진이면 그 순서로, 아니면 반대로

------------------------------------------------------------
출력 형식 (반드시 이 구조로)
------------------------------------------------------------

# 1) Logic Layer (Domain Layer) 설계
## 1.1 도메인 개념
- Entities / Value Objects / Domain Services 목록과 책임(SRP)
## 1.2 도메인 불변조건(Invariants)
- 행/열/대각선 합 일치, Magic Constant 등
## 1.3 핵심 유스케이스(도메인 관점)
- 빈칸 찾기, 누락 숫자 찾기, 마방진 판정, 두 조합 시도
## 1.4 Domain API(내부 계약)
- 메서드 시그니처 수준(코드 X) + 입력/출력/실패조건
## 1.5 Domain 단위 테스트 설계(RED 우선)
- 테스트 케이스 목록(정상/비정상/엣지)
- 각 테스트가 보호하는 invariant 명시

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)
## 2.1 사용자/호출자 관점 시나리오
- “행렬 입력 → 검증 → 결과 출력” 흐름
## 2.2 UI 계약(외부 계약)
- Input schema / Output schema / Error schema
## 2.3 UI 레벨 테스트(Contract-first, RED 우선)
- 잘못된 크기, 빈칸 개수 오류, 값 범위 오류, 중복 오류, 반환 포맷 검증
- Domain은 Mock으로 가정
## 2.4 UX/출력 규칙
- 에러 메시지 표준(정확한 문구 규칙까지)

# 3) Data Layer 설계 (Data Layer)
## 3.1 목적 정의
- “저장/로드”의 필요성과 범위(학습용)
## 3.2 인터페이스 계약
- 예: MatrixRepository.save/load (메서드 수준, 코드 X)
- 저장 대상: 입력 행렬, 실행 결과(선택)
## 3.3 구현 옵션 비교(메모리/파일)
- 옵션 A: InMemory / 옵션 B: File(JSON/CSV)
- 추천안 1개 선택 + 이유
## 3.4 Data 레이어 테스트
- 저장/로드 정합성, 예외(파일 없음/형식 오류), 불변조건(4x4 유지)

# 4) Integration & Verification (통합 및 검증)
## 4.1 통합 경로 정의
- UI → Application(선택) → Domain → Data 흐름(의존성 방향 포함)
## 4.2 통합 테스트 시나리오
- 정상 시나리오 2개 이상
- 실패 시나리오 3개 이상(입력 오류, 도메인 실패, 데이터 실패)
## 4.3 회귀 보호 규칙
- 기존 테스트 유지 정책
- 변경 금지 규칙(계약/출력 포맷)
## 4.4 커버리지 목표
- Domain Logic 95%+
- UI Boundary 85%+
- Data 80%+
## 4.5 Traceability Matrix (필수)
- Concept(Invariant) → Rule → Use Case → Contract → Test → Component

------------------------------------------------------------
추가 조건
------------------------------------------------------------
- 모호한 표현 금지(“적절히/충분히” 금지)
- 모든 규칙은 검증 가능해야 함(테스트로 확인 가능)
- 구현 코드 작성 금지
- 표/체크리스트를 적극 사용

---

**Cursor**

요청하신 구조에 맞춰 구현 코드 없이, 검증 가능한 계약/테스트 중심 설계를 작성하겠습니다. 먼저 Canvas 사용 규칙을 확인한 뒤, 바로 1~4번 섹션을 표/체크리스트 기반으로 정리하겠습니다.

설계를 표 중심으로 전달해야 해서, 채팅 본문 대신 열람 가능한 Canvas 아티팩트로 작성하겠습니다. 지금 Canvas SDK 타입을 확인한 뒤 바로 문서를 생성하겠습니다.

이제 요청하신 1~4번 구조를 그대로 담은 설계 산출물을 Canvas 파일로 생성하겠습니다. 각 규칙을 테스트 가능 형태(계약/실패조건/검증 케이스)로 고정해 넣겠습니다.

요청하신 산출물을 **구현 코드 없이**, 지정한 `#1 ~ #4` 구조와 검증 가능한 규칙/계약/테스트/추적성 매트릭스로 정리해 Canvas로 작성했습니다.

파일: `C:\Users\usejen_id\.cursor\projects\c-DEV-MagicSquare-XXX\canvases\magic-square-dual-track-design.canvas.tsx`

Canvas는 채팅 옆에서 여는 라이브 문서 형태라서, 이번처럼 표/체크리스트/매트릭스가 많은 설계를 한 번에 검토하고 확장하기에 적합해서 이 형식으로 제공했습니다.  
내용에는 아래가 모두 포함되어 있습니다:

- `# 1) Logic Layer` : 도메인 개념, 불변조건, 유스케이스, 내부 API 계약, RED 우선 단위 테스트
- `# 2) Screen Layer` : 경계 시나리오, 외부 계약(Input/Output/Error schema), Domain Mock 기반 UI 계약 테스트, 에러 메시지 표준
- `# 3) Data Layer` : 저장/로드 목적, Repository 인터페이스 계약, InMemory vs File 비교 + 권장안, 데이터 레이어 테스트
- `# 4) Integration & Verification` : 통합 경로/의존성 방향, 정상 2+ 실패 3+ 시나리오, 회귀 보호 규칙, 커버리지 목표, 필수 Traceability Matrix

원하시면 다음 단계로, 이 설계를 기준으로 **테스트 파일 목차(패키지/클래스/테스트명 규약)**까지 바로 쪼개서 드리겠습니다.

---

**User**

Report 폴더에 보고서로 내보내줘.

---

**Cursor**

요청하신 대로 작업 결과를 `Report` 폴더용 보고서 파일로 내보내겠습니다. 먼저 폴더 존재 여부를 확인한 뒤, 없으면 생성하고 보고서 파일을 작성하겠습니다.

워크스페이스 실제 경로를 다시 확인한 뒤 그 위치의 `Report` 폴더에 생성하겠습니다.

`Report` 폴더가 이미 있어서, 해당 위치에 바로 제출용 마크다운 보고서를 생성하겠습니다.

`Report` 폴더로 보고서 내보내기 완료했습니다.

- 생성 파일: `C:\DEV\MagicSquare_XXX\Report\MagicSquare_4x4_DualTrack_TDD_Report.md`
- 내용: 요청하신 `#1~#4` 구조 전체(Logic/UI/Data/Integration), 계약/테스트/체크리스트/Traceability Matrix 포함
- 제약 준수: 구현 코드 없이 설계/계약/검증 계획만 포함

원하시면 같은 내용을 `pdf` 또는 `docx` 형식으로도 변환해 드릴게요.

