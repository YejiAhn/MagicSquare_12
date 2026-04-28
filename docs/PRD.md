# MagicSquare 4x4 — Product Requirements Document (`docs`)

## 1. 문서 역할

- **`docs/PRD.md`**: 저장소 루트·`docs`에서 바로 열 수 있는 **제품 요구 요약본**이다.
- **정본(상세)**: [`Report/05_MagicSquare_PRD.md`](../Report/05_MagicSquare_PRD.md) — 범위·계약·오류·비기능 요구의 전체 서술.

## 2. 제품 한 줄

부분적으로 비어 있는 **4×4 Magic Square**(빈칸 `0` 정확히 두 칸)를 입력으로 받아, **도메인 규칙을 만족하면** 빈칸을 채운 결과를 내고, **위반 시 일관되게 거부**하는 학습용 완성 시스템이다.

## 3. 비즈니스 목표

- Invariant·I/O **계약을 먼저 고정**하고, **Dual-Track(UI + Logic) TDD**로 구현한다.
- **ECB(Entity / Control / Boundary)**로 책임을 나누고, **비즈니스 규칙은 Logic(및 Control 조율)**에만 둔다.
- **Task → Req → Scenario(L0~L3) → Test → Code** 추적이 가능한 산출물을 유지한다.

## 4. 도메인 불변조건(요약)

| 항목 | 규칙 |
|------|------|
| 크기 | 4×4 |
| 값 | `0`(빈칸) 또는 1~16 |
| 빈칸 | `0` 정확히 2개 |
| 중복 | `0`을 제외한 중복 불가 |
| 완성 판정 | 모든 행·열·두 대각선의 합 **34** |
| 비정상 보드 | 거부(명확한 오류 계약) |

## 5. 범위

**포함**: 형태·값·빈칸·중복 검증, 빈칸 좌표(결정적 순서), 누락 두 수 산출, 마방진 판정, 두 빈칸 배치(정순 우선·역순 폴백), Boundary 파싱·오류 매핑, UI는 수집·표시만.

**제외**: 일반 N×N 최적화, 인증·네트워크, 프로덕션급 UI 고도화 등 — 상세는 Report PRD §5 참고.

## 6. 출력·오류 계약(요약)

- 성공 시 보드 완성 규칙은 PRD 정본(행·열·합 34, 배치 순서)을 따른다.
- 실패 시 **도메인 오류 코드**를 경계에서 **사용자 메시지**로 매핑한다(UI에 규칙 로직을 넣지 않음).

## 7. 관련 문서

| 문서 | 용도 |
|------|------|
| [문제 정의](../Report/01_4x4_Magic_Square_Problem_Definition_Report.md) | 불변조건·문제 정의 |
| [Dual-Track TDD](../Report/02_MagicSquare_4x4_DualTrack_TDD_Report.md) | RED 목록·UI/Logic 트랙 |
| [사용자 여정](../Report/04_MagicSquare_User_Journey_Report.md) | Epic·스토리·Gherkin |
| [구현 To-Do 정본](./TODO.md) · [Report 06](../Report/06_MagicSquare_4x4_Implementation_Todo_Report.md) | TASK 체계·시나리오·테스트 이름 |
