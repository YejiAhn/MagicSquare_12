# MagicSquare 4x4 — 구현 To-Do (`docs`)

## 문서 역할

- **`docs/TODO.md`**: Epic·User Story·주요 Task를 **한 화면에서 체크**하기 위한 요약 보드이다.
- **Report 보고서**: 동일 계열 요약은 [`Report/09_MagicSquare_Implementation_Todo_Summary_Report.md`](../Report/09_MagicSquare_Implementation_Todo_Summary_Report.md)에도 둔다.
- **정본(전체 TASK·RED/GREEN/REFACTOR·체크포인트)**: [`Report/06_MagicSquare_4x4_Implementation_Todo_Report.md`](../Report/06_MagicSquare_4x4_Implementation_Todo_Report.md)

## 추적 한 줄

**Task → Req → Scenario(L0~L3) → Test → Code (ECB)** — 하위 `TASK-xxx-n`은 **RED → GREEN → REFACTOR** 순서.

---

## Epic

- [ ] **Epic-001** — 부분 보드 입력 → 규칙 충족 시 완성 / 위반 시 거부 (Logic-Track + UI-Track, 규칙은 Logic에만)

## User Story (요약)

- [ ] **US-000** — Phase 0: 계약·스캐폴딩 (REQ-ARCH) — `TASK-000`
- [ ] **US-001** — 보드 표현·생성 (Entity) — `TASK-001`
- [ ] **US-002** — 보드 유효성 검사 (Logic) — `TASK-004` ~ `TASK-012`
- [ ] **US-003** — 빈칸 탐지 (Logic) — `TASK-013` ~ `TASK-015`
- [ ] **US-004** — 누락 숫자 쌍 (Logic) — `TASK-017` ~ `TASK-019`
- [ ] **US-005** — 마방진 판정·배치 해결 (Logic) — `TASK-021` ~ `TASK-029`
- [ ] **US-006** — 파싱·오류 표현 (Boundary) — `TASK-035`, `TASK-037`
- [ ] **US-007** — Control 유스케이스 — `TASK-030` ~ `TASK-034`
- [ ] **US-008** — UI-Track — `TASK-039` ~ `TASK-043`
- [ ] **US-009** — 품질·추적성 — `TASK-044`, `TASK-045` (`docs/traceability.md` 등)

## 주요 Task ID (정본과 동일 번호)

체크는 Report 06 또는 본 문서에서 일관되게 갱신하면 된다.

| Task | 한 줄 |
|------|--------|
| TASK-000 | ECB·오류 코드·추적 초안 |
| TASK-001 | `MagicSquare4x4` Entity |
| TASK-004~012 | `BoardValidator` 파이프라인 |
| TASK-013~015 | `BlankLocator` |
| TASK-017~019 | `MissingNumbersFinder` |
| TASK-021~029 | `MagicSquareJudge` · `DualPlacementResolver` |
| TASK-030~034 | `CompleteMagicSquareUseCase` |
| TASK-035,037 | `StdioMagicSquareAdapter` · `ErrorPresenter` |
| TASK-039~043 | 콘솔 UI · 출력 · `Application` |
| TASK-044~045 | 커버리지 · Concept-to-Code 매트릭스 |

**구현 순서 힌트**: US-002~005 Logic 먼저 → US-007 Control → US-006 Boundary · US-008 UI.

## PRD·문제 정의

- [PRD (`docs`)](./PRD.md) · [PRD 요약 (`Report`)](../Report/08_MagicSquare_PRD_Summary_Report.md) · [PRD 정본](../Report/05_MagicSquare_PRD.md)
- [문제 정의](../Report/01_4x4_Magic_Square_Problem_Definition_Report.md)
