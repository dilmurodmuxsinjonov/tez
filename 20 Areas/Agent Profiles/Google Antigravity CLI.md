---
title: "🏛️ Google Antigravity CLI — Systems Architecture & Deep Debugging Engine"
version: "1.0.0"
date: 2026-09-12
created: 2026-09-12
updated: 2026-09-12
status: active
type: agent-profile
agent: "Google Antigravity CLI"
role: systems-architect
tags:
  - agent-profile
  - antigravity-cli
  - google-deepmind
  - architecture
  - cli
  - ai-fleet
language: "uz-UZ, en-US"
---

# 🏛️ Google Antigravity CLI — Systems Architecture & Deep Debugging Engine

> *"Tizimli tahlil, monorepo me'morchiligi va qat'iy tekshiruv — yuqori yuklamali dasturiy muhitlarning mustahkam poydevoridir."*

Ushbu profil **Google Antigravity CLI** (`agy.exe`) korporativ darajadagi tizimlar arxitekturasi, murakkab nosozliklarni bartaraf etish (deep debugging) va loyiha tuzilmalarini audit qilish dvigateli uchun rasmiy operatsion qo'llanma hisoblanadi. Google Antigravity foydalanuvchining ko'p agentli floti (`[[AI Sozlangan Miyyasi]]`) tarkibida Google DeepMind muhandislik standartlari asosida yirik monorepolarni tahlil qilish, asinxron to'qnashuvlarni tekshirish va yuqori ishonchlilikdagi me'moriy rejalarni tuzishga ixtisoslashgan.

---

## 📋 Profil va Vositalar Parametrlari (Profile & Toolchain)

| Parametr | Qiymat / Manzil | Tavsif |
| :--- | :--- | :--- |
| **Agent Nomi** | Google Antigravity CLI (`agy`) | Tizimlar arxitektori va chuqur nosozliklar auditori |
| **Bosh Mas'uliyati** | Codebase Architecture, Concurrency Design & Monorepo Debugging | Yirik dasturiy arxitekturalarni tahlil qilish |
| **Asosiy Binar Fayl** | `C:\Users\dilmu\AppData\Local\agy\bin\agy.exe` | Go tilida yozilgan rasmiy binar ilova |
| **Google Akkaunti** | `dilmurodmuhsinjanov910@gmail.com` | Autentifikatsiyadan o'tgan Google sessiyasi |
| **Ikki Tomonlama Rol (Dual Roles)**| `[[Antigravity 1]]` (Vault arxitektori) & `[[Antigravity 2]]` (Sandbox) | Interaktiv va izolyatsiyalangan sinov rollari |
| **CLI Ijro Muhiti** | Headless CLI auditor (`agy -p ...`) | Avtomatlashtirilgan tahlil va rejalashtirish |
| **Muloqot Tili** | O'zbek tili (Lotin), English (US) | Ikki tilli professional hisobotlar |
| **Ruxsat Doirasi** | Tizim arxitekturasi tahlili va loyiha fayllari | Read/Write vakolatlari |
| **Asosiy Protokol** | `[[Concurrency & Sync Protocol]]` va `RULE[user_global]` | Atomik qulflash va doimiy versiyalash |
| **Markaziy Qayd** | `[[AI Sozlangan Miyyasi]]` | Butun tizimning yagona haqiqat manbai |

---

## 🚀 Ishga Tushirish va Buyruqlar Sintaksisi (CLI Invocation Syntax)

Google Antigravity CLI turli tahliliy va me'moriy audit jarayonlarida quyidagi standart sintaksis asosida chaqiriladi:

```powershell
# Interaktiv bo'lmagan to'g'ridan-to'g'ri chiqish (print) bilan chaqirish
agy -p "<SAVOL_YOKI_TOPSHIRIQ>"

# Yuqori fikrlash chuqurligi va ruxsatlarni avtomatik tasdiqlash bilan chaqirish
agy -p "<TOPIC>" --effort high --dangerously-skip-permissions

# Dasturiy integratsiya uchun tuzilmaviy JSON formatida javob olish
agy -p "<TOPIC>" --output-format json

# Oxirgi faol muloqot sessiyasini davom ettirish
agy -c -p "<DAVOM_ETISH_SO'ROVI>"
```

### Kalit Bayroqlar (CLI Flags Reference)
- `-p, --print`: Yagona promptni interaktiv bo'lmagan tarzda bajarish va natijani stdout'ga chiqarish.
- `--dangerously-skip-permissions`: Barcha asbob va fayl ruxsatlarini avtomatik tasdiqlash.
- `--effort <low|medium|high>`: Ichki mulohaza va deduksiya chuqurligini belgilash.
- `-c, --continue`: Eng so'nggi faol suhbat kontekstini davom ettirish.
- `--mode <accept-edits|plan>`: Agentning ishlash rejimini belgilash (tahrirlash yoki rejalashtirish).
- `--output-format <text|json|stream-json>`: Chiqish ma'lumotlari formatini tanlash.

---

## 🎭 Ikki Tomonlama Seans Rollari (Dual Session Roles Architecture)

Google Antigravity ekotizimda uch xil yondashuv orqali faoliyat yuritadi:

1. **`[[Antigravity 1]]` (Primary User Liaison & Vault Architect)**:
   - Asosiy Google hisobi orqali ishlaydi.
   - Foydalanuvchi bilan bevosita muloqot qiladi, ikkinchi miyya (`[[AI Sozlangan Miyyasi]]`) yaxlitligini ta'minlaydi va loyiha xotirasini boshqaradi.

2. **`[[Antigravity 2]]` (Isolated Sandbox & Clean-Room Builder)**:
   - Alohida izolyatsiyalangan Google hisobi sessiyasida ishlaydi.
   - Katta hisoblashlar, mustaqil sinovlar va xavfsiz sandbox muhitida tajribalar o'tkazadi.

3. **Google Antigravity CLI (`agy` Headless CLI)**:
   - Terminal orqali chaqiriluvchi avtomatlashtirilgan buyruqlar dvigateli.
   - Loyiha repozitoriylarida statik tahlil, me'moriy qoidalar tekshiruvi va CI/CD auditlarini bajaradi.

---

## 🎯 Asosiy Vazifalar va Imkoniyatlar (Capabilities & Use Cases)

1. **Monorepo va Qaramliklar Grafigi Tahlili (Dependency Graph Analysis)**:
   - Katta kod bazalarida siklik bog'liqliklar va arxitektura buzilishlarini fosh etadi.
   - Modullar orasidagi interfeys kontraktlari qat'iyligini nazorat qiladi.

2. **Konkurentlik va Asinxron Dizayn (Concurrency & Race Condition Auditing)**:
   - Ko'p oqimli yoki asinxron arxitekturalarda poyga holatlarini (race conditions) va blokirovka xatolarini aniqlaydi.
   - `[[Concurrency & Sync Protocol]]` qoidalariga muvofiqlikni tekshiradi.

3. **Arxitektura Qarorlari Jurnali (ADR Validation)**:
   - Loyihalarda qabul qilingan me'moriy tanlovlarning (ADR) matematik va mantiqiy asoslanishini audit qiladi.

---

## 🔒 Xavfsizlik va Konkurentlik Standartlari (Security & Concurrency)

- **Qat'iy Atomiklik**: Fayllarga o'zgartirish kiritishda vaqtinchalik nusxalar orqali yozish va `.agents/locks/` mexanizmidan foydalanadi.
- **Git Intizomi**: Har qanday arxitekturaviy kiritma `RULE[user_global]` talablariga mos ravishda tavsifli kommit bilan muhrlanadi.

---

## 🔗 Aloqador Havolalar (Related Links)

- Bosh Boshqaruv Markazi: [[AI Sozlangan Miyyasi]]
- Asosiy Boshqaruv Paneli: [[Dashboard]]
- Ekotizim Xaritasi: [[30 Resources/AI Agent Ecosystem Map|AI Agent Ecosystem Map]]
- Bosh Tizim Arxitektori: [[Antigravity 1]]
- Sandbox Sinovchi Agent: [[Antigravity 2]]
- Kod Generatsiyasi Dvigateli: [[Codex LLM Assistant]]
- Fayllarni Qulflash va Sinxronizatsiya: [[Concurrency & Sync Protocol]]
- Sohalar Xaritasi: [[20 Areas/20 Areas|20 Areas]]
- Sohalar To'liq Xaritasi: [[20 Areas/20 Areas MOC|20 Areas MOC]]
- Git Ish Tartibi: [[30 Resources/Agent Skills/git-workflow|git-workflow]]
