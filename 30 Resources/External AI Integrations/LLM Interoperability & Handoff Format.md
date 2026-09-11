---
title: "🔄 Modellararo Hamkorlik va Ma'lumot Uzatish Formati (Handoff Format)"
created: 2026-09-12
updated: 2026-09-12
status: active
type: operational-manual
tags:
  - interoperability
  - handoff
  - json-schema
  - context-sharing
language: "uz-UZ, en-US"
---

# 🔄 Modellararo Hamkorlik va Ma'lumot Uzatish Formati (Handoff Format)

> *"Bir AI agenti to'xtagan joydan boshqa AI agenti hech qanday ma'lumot yo'qotmasdan davom eta olishi shart."*

Ushbu standart turli AI modellari (Gemini, Claude, Codex) o'rtasida ish topshirilganda (handoff) ishlatiladigan universal JSON/Markdown tuzilmasini belgilaydi.

---

## 📦 Handoff Paketi Tuzilishi (Handoff Payload)

Har qanday agent boshqasiga ish uzatganda quyidagi 5 ta maydonni to'ldiradi:

```json
{
  "project_name": "Loyiha Nomi",
  "active_git_branch": "feature/nomi",
  "latest_state_summary": "Qisqa 1-2 jumlalik xulosa",
  "completed_milestones": ["M1", "M2"],
  "unresolved_blockers": ["Aniq muammo yoki yo'q"],
  "suggested_immediate_actions": [
    "Fe'l bilan boshlanuvchi 1-qadam",
    "Fe'l bilan boshlanuvchi 2-qadam"
  ]
}
```
