---
title: "🌐 Browser Automation Playbook — Autonomous Agentic Web Operations"
created: 2026-09-12
updated: 2026-09-12
status: active
type: operational-playbook
tags:
  - browser-automation
  - cdp
  - accessibility-tree
  - playwright
  - defuddle
  - session-isolation
  - error-recovery
language: "uz-UZ, en-US"
---

# 🌐 Browser Automation Playbook — Autonomous Agentic Web Operations

> *"Brittle CSS selectors and volatile XPath queries belong to the era of rigid scripts. Modern autonomous agents interact with web environments through accessibility tree abstraction, perceptual visual feedback, isolated persistent sessions, and self-healing action loops."*

Ushbu operatsion playbook avtonom AI agentlarining veb-brauzerlar bilan ishlash standartlari, Accessibility Tree orqali navigatsiya qilish, seanslar va profillar izolyatsiyasi hamda xatoliklarni o'z-o'zidan tuzatish mexanizmlarini to'liq belgilab beradi.

---

## 🧭 Asosiy Boshqaruv Havolalari (Core Navigation & Backlinks)

- 🧠 **[[AI Sozlangan Miyyasi|🧠 AI Sozlangan Miyyasi — Universal AI Second Brain]]** (Bosh Markaz)
- 📊 **[[Dashboard|Mening Ikkinchi Miyyam (Dashboard)]]**
- 🛡️ **[[20 Areas/20 Areas|20 Areas MOC]]**
- 🌐 **[[30 Resources/Browser & Automation Guides/Advanced Agentic Browser Playbook|Ilg'or Brauzer Playbooki]]**
- 📖 **[[30 Resources/Browser & Automation Guides/Browser Automation Operations Manual|Browser Automation Manual]]**
- 🔍 **[[30 Resources/Agent Skills/defuddle|Defuddle Web Extraction]]**
- 👤 **[[20 Areas/Agent Profiles/Antigravity 1|Antigravity 1 Profili]]**
- 👤 **[[20 Areas/Agent Profiles/Antigravity 2|Antigravity 2 Profili]]**

---

## 🏗️ 1. Modern Agentic Web Interaction Architecture

Eski skriptlar sahifaning HTML tuzilmasiga bog'lanib qolganligi sababli, veb-sayt dizayni biroz o'zgarsa ham sinib qolar edi. Zamonaviy agentik yondashuv ikki qatlamli idrok modeliga (Dual-Layer Perceptual Model) tayanadi:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          LIVE BROWSER TAB (PAGE)                            │
└───────────────────────┬─────────────────────────────▲───────────────────────┘
                        │ CDP Snapshot                │ Synthetic Dispatch
┌───────────────────────▼─────────────────────────────┴───────────────────────┐
│                     AGENT PERCEPTUAL ENGINE (AOM + DOM)                     │
├─────────────────────────────────────────┬───────────────────────────────────┤
│    ACCESSIBILITY OBJECT MODEL (AOM)     │    DEFUDDLE DISTILLED CONTENT     │
│ • ARIA Roles (button, link, textbox)    │ • Markdown article extraction     │
│ • Interactive Synthetic UIDs            │ • Stripped advertisements / CSS   │
│ • Coordinate-free action dispatch       │ • Token-efficient text payload    │
└─────────────────────────────────────────┴───────────────────────────────────┘
```

---

## 🎯 2. Accessibility Tree Routing & Synthetic UIDs

### 2.1 Accessibility Tree Afzalliklari
Veb-sahifaning Accessibility Tree (a11y) daraxti brauzer tomonidan ekranni o'quvchi qurilmalar (screen readers) uchun generatsiya qilinadi. U quyidagi xususiyatlarga ega:
- Keraksiz `<div>`, `<span>` va styling teglari filtrlanadi.
- Faqat interaktiv (bosiladigan, yoziladigan, tanlanadigan) elementlar qoladi.
- Token sarfi odatiy HTMLga nisbatan **85–90% ga kamayadi**.

### 2.2 Synthetic UID Mapping
Agent sahifadagi interaktiv tugunlarga maxsus identifikatorlar (UIDs) belgilaydi:
```text
[#01] link "Home"
[#02] link "Documentation"
[#03] searchbox "Search repository, code, or documentation..."
[#04] button "Log In"
[#05] button "Get Started Free"
```
Agent harakatni amalga oshirishda murakkab selektorlar o'rniga aniq UID orqali murojaat qiladi:
- `interact(action="click", uid="#04")`
- `interact(action="type", uid="#03", text="Model Context Protocol")`

---

## 🧼 3. Clean DOM Extraction & Defuddle Distillation

Agent veb-tadqiqot olib borayotganda millionlab tokenlik HTML o'rniga faqat toza semantik ma'lumotni yuklaydi:

### 3.1 Keraksiz Elementlarni Tozalash (DOM Sanitization)
Quyidagi elementlar darhol olib tashlanadi:
- `<script>`, `<style>`, `<noscript>`, `<template>`
- Reklama va kuzatuv iframelari
- Inline SVG va Base64 rasm kodlari

### 3.2 Defuddle Vositasidan Foydalanish
`defuddle` vositasi orqali veb-sahifa to'g'ridan-to'g'ri toza Markdown formatiga o'tkaziladi:
- Asosiy maqola matni, sarlavhalar va jadvallar to'liq saqlanadi.
- Navigatsiya menyulari, footer va keraksiz bannerlar avtomatik qirqib tashlanadi.

---

## 🛡️ 4. Resilient Action Replay & Error Recovery Loops

Avtonom agentlar real dunyo veb-saytlaridagi kutilmagan hodisalarni mustaqil bartaraf etishi shart:

```
┌─────────────────┐
│ Action Dispatch │ ──► [#04] click "Submit"
└────────┬────────┘
         │
         ▼
┌─────────────────┐       NO (Timeout / DOM unchanged)
│ DOM Mutation?   │ ──────────────────────────────────────┐
└────────┬────────┘                                       │
         │ YES                                            ▼
         ▼                                      ┌───────────────────┐
┌─────────────────┐                             │ Recovery Strategy │
│ Verify Success  │                             │ 1. Re-query AOM   │
└─────────────────┘                             │ 2. Scroll element │
                                                │ 3. Alt text match │
                                                │ 4. Exp. backoff   │
                                                └───────────────────┘
```

### 4.1 Qadam-baqadam Qayta Tiklash Strategiyasi (Recovery Playbook)
1. **Mutation Observer kutishi**: Bosish amali bajarilgandan keyin kamida DOM mutatsiyasi yoki tarmoq so'rovi sodir bo'lishi tekshiriladi.
2. **Stale Element xatosi**: Agar sahifa yangilanib, UID eskirgan bo'lsa, agent yangi AOM snapshoti oladi va elementni semantik nomi bo'yicha qayta qidiradi.
3. **Modal va Dialoglarni yopish**: Ko'pincha kutilmagan "Cookie Banner" yoki "Subscribe" popup oynalari paydo bo'ladi. Agent ularni aniqlab, `dismiss` yoki `close` tugmasini bosib, asosiy oqimga qaytadi.
4. **Eksponentsial orqaga chekinish (Exponential Backoff)**: 500ms, 1500ms, 4500ms oraliqlar bilan 3 martagacha qayta urinish.

---

## 🔒 5. Profile Isolation, Session Persistence & Auth Isolation

Ko'p agentli tizimda hisoblar va seanslarning aralashib ketmasligi hal qiluvchi ahamiyatga ega.

### 5.1 Brauzer Profillari Matritsasi
| Agent | Foydalanuvchi Profili | Cookie & Auth Storage | Vazifa Doirasi |
| :--- | :--- | :--- | :--- |
| **Antigravity 1** | Primary Google Session (`dilmurodmuhsinjanov910@gmail.com`) | `~/.browser/profiles/antigravity1/` | Asosiy servislar, Google Docs, Firebase, GitHub |
| **Antigravity 2** | Secondary Isolated Sandbox Session | `~/.browser/profiles/antigravity2/` | Xavfli skriptlar, tajribaviy tadqiqotlar, ommaviy veb-skreyping |
| **Codex Runner** | Headless Ephemeral Session | Xotiradagi vaqtinchalik xotira (RAM) | Mahalliy testlar, e2e sinovlar, localhost API tekshiruvi |

### 5.2 Xavfsizlik Qoidalari
- Antigravity 2 hech qachon Antigravity 1 ning cookie fayllariga kirish huquqiga ega emas.
- Maxfiy parollar va tokenlar hech qachon matnli qaydlarga yozilmaydi; ular faqat muhit o'zgaruvchilari orqali uzatiladi.

---

## ⚙️ 6. Practical Workflows with Chrome DevTools MCP & Playwright

### 6.1 Chrome DevTools Protocol (CDP) orqali Boshqaruv
Chrome DevTools MCP serveri yordamida agent quyidagi chuqur diagnostika amallarini bajaradi:
1. **Network Interception**: API so'rovlarini tahlil qilish, JSON javoblarni to'g'ridan-to'g'ri o'qib olish.
2. **Console Error Auditing**: Sahifadagi barcha JavaScript xatoliklarini (`console.error`) monitoring qilish.
3. **Headless Execution**: GUI interfeysisiz yuqori tezlikda fon rejimida ishlash.

### 6.2 Amaliy Namuna: Defuddle orqali Hujjat O'rganish
```bash
# 1. Sahifaga o'tish va toza markdown yuklab olish
defuddle parse "https://modelcontextprotocol.io/introduction" --output ./mcp_intro.md

# 2. Chrome DevTools orqali faol tugmalarni tekshirish
mcp_devtools_eval "document.querySelectorAll('a.interactive-link')"
```

---

## 📊 7. Playbook Verification & Quality Standards

- **Zero Unhandled Errors**: Har bir brauzer harakati aniq `try/catch` va qayta tiklash bloki bilan himoyalangan.
- **Strict Verification**: Har bir veb-operatsiyadan keyin natija skrinshot yoki semantik matn orqali tekshiriladi.
- **Atomic State Logging**: Barcha brauzer operatsiyalari loyiha xotirasiga qayd qilib boriladi.
