---
title: "🧠 Avtonom Kognitiv Agentlar Xotirasi Arxitekturasi"
created: 2026-09-12
updated: 2026-09-12
status: active
type: research-note
tags:
  - agent-memory
  - cognitive-architecture
  - episodic-memory
  - semantic-memory
  - mem0
  - letta
language: "uz-UZ, en-US"
---

# 🧠 Avtonom Kognitiv Agentlar Xotirasi Arxitekturasi

> *"Haqiqiy intellekt — shunchaki javob berish emas, balki o'z tajribasidan saboq olish, bilimlarni qatlamlarga ajratish va xotirani o'z vaqtida tozalashdir."*

Ushbu tadqiqot qaydi inson miyasi kognitiv modeliga asoslangan **ko'p qatlamli agent xotirasi** (Hierarchical Cognitive Agent Memory) tizimini va uni **"AI Sozlangan Miyyasi"** ekotizimida qo'llash standartlarini belgilaydi.

---

## 🧭 Asosiy Boshqaruv Havolalari

- 🧠 **[[AI Sozlangan Miyyasi|🧠 AI Sozlangan Miyyasi — Universal AI Second Brain]]** (Bosh Markaz)
- 📚 **[[30 Resources/30 Resources|30 Resources MOC]]**
- 🤖 **[[20 Areas/Agent Profiles/Concurrency & Sync Protocol|Concurrency & Sync Protocol]]**

---

## 🏛️ 4 Qatlamli Kognitiv Xotira Modeli

```
┌─────────────────────────────────────────────────────────────┐
│                    1. ISHCHI XOTIRA (Working Memory)        │
│  Joriy kontekst oynasi, faol maqsad va vaqtinchalik xotira  │
└──────────────┬───────────────────────────────▲──────────────┘
               │ Saqlash & Qisqartirish        │ Tiklash & Faollashtirish
┌──────────────▼───────────────────────────────┴──────────────┐
│                UZ OQ MUDDATLI XOTIRA (Long-Term Memory)     │
├──────────────────────┬───────────────────────┬──────────────┤
│ 2. EPIZODIK XOTIRA   │  3. SEMANTIK XOTIRA   │4. PROSEDURAVIY│
│ (Voqealar, xatolar va│  (Tushunchalar, bilim,│(Ko'nikmalar, │
│  aniq tajribalar)    │   faktlar va graph)   │ API andozalari)
└──────────────────────┴───────────────────────┴──────────────┘
```

### 1. Ishchi Xotira (Working Memory / Scratchpad)
- **Tavsif:** Modelning joriy prompt va kontekst oynasida (`2M tokens`) turgan faol ma'lumotlar.
- **Vazifasi:** Bir vaqtning o'zida yechilayotgan muammo bo'yicha oraliq mulohazalarni ushlab turish.
- **Optimizatsiya:** Tokenlar to'lib ketmasligi uchun qadamma-qadam xotirani qisqartirish (`context pruning`).

### 2. Epizodik Xotira (Episodic Memory — Temporal & Reflective)
- **Tavsif:** Vaqt ketma-ketligi (timestamps) bilan saqlanadigan harakatlar tarixi: qaysi kommit qilindi, qaysi xatoga duch kelindi va qanday yechildi.
- **Refleksiya (Self-Correction):** Agent muvaffaqiyatsiz bo'lgan harakatlarni tahlil qiladi va xuddi shu xatoni takrorlamaydi.

### 3. Semantik Xotira (Semantic Memory — Knowledge & GraphRAG)
- **Tavsif:** Faktlar, tushunchalar va ularning o'zaro bog'liqliklari (Obsidian wikilink tarmog'i va vektor bazalar).
- **Qidiruv:** Gibrid qidiruv (Keyword BM25 + Vector Similarity + Graph Traversal).

### 4. Proseduraviy Xotira (Procedural Memory — Skills & Protocols)
- **Tavsif:** Agent qanday ishlashi kerakligi haqidagi qat'iy ko'nikmalar: `RULE[user_global]`, Git operatsiyalari, test skriptlari va brauzer protokollari.

---

## 🛠️ Zamonaviy Xotira Frameworklari (Mem0 va Letta)

- **Mem0**: Foydalanuvchi afzalliklari va agent tajribasini gibrid (Graph + Vector) tarzda saqlovchi zamonaviy qatlam.
- **Letta (sobiq MemGPT)**: Operatsion tizim kabi kontekstni disk va RAM o'rtasida sahifalab (paging) boshqaruvchi tizim.
