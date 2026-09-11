---
title: "⚡ Prompt Engineering va Kontekst Qisqartirish (Context Compression)"
created: 2026-09-12
updated: 2026-09-12
status: active
type: style-guide
tags:
  - prompt-engineering
  - context-compression
  - token-optimization
language: "uz-UZ, en-US"
---

# ⚡ Prompt Engineering va Kontekst Qisqartirish (Context Compression)

> *"Keraksiz so'zlarni qisqartirish orqali fikrning quvvati oshadi."*

Sun'iy intellekt modellari (Gemini, Claude, GPT) bilan ishlashda kontekst oynasini tejash, xatoliklarni kamaytirish va modellar o'rtasida katta hajmdagi xotirani yo'qotishlarsiz uzatish qoidalari.

---

## 📐 Qisqartirish Tamoyillari (Compression Rules)

1. **Information Density (Axborot Zichligi)**:
   - Ortiqcha kirish va xushomad so'zlarini olib tashlash.
   - Jadvallar, bullet-pointlar va kalit-qiymat juftliklaridan foydalanish.
2. **Deterministic State Representation**:
   - Loyiha holatini hikoya tarzida emas, parametrlar orqali ko'rsatish (`Git: feature/x`, `Milestone: 3/5`, `Status: PASS`).
3. **Structured Memory Blocks**:
   - Gemini Topics arxitekturasidagi kabi maxsus kod bloklari ichida emoji-belgilar bilan tartiblash.
