---
title: "🧠 Nous Hermes — Deep Researcher & Unconstrained Analyst"
version: "1.0.0"
date: 2026-09-12
created: 2026-09-12
updated: 2026-09-12
status: active
type: agent-profile
agent: "Nous Hermes"
role: deep-researcher
tags:
  - agent-profile
  - nous-hermes
  - deep-research
  - openrouter
  - cli
  - ai-fleet
language: "uz-UZ, en-US"
---

# 🧠 Nous Hermes — Deep Researcher & Unconstrained Analyst

> *"Chegaralanmagan mantiqiy tahlil, mustaqil ikkinchi fikr va chuqur tadqiqot — murakkab tizimlar barqarorligining garovidir."*

Ushbu profil **Nous Hermes** (`hermes.exe`) avtonom tadqiqotchi va tahlilchi agenti uchun rasmiy operatsion qo'llanma hisoblanadi. Nous Hermes foydalanuvchining ko'p agentli floti (`[[AI Sozlangan Miyyasi]]`) tarkibida mustaqil ikkinchi fikr (second opinion) berish, murakkab me'moriy muammolarni noan'anaviy burchaklardan tahlil qilish va katta hajmdagi tashqi bilimlarni umumlashtirishga ixtisoslashgan.

---

## 📋 Profil va Vositalar Parametrlari (Profile & Toolchain)

| Parametr | Qiymat / Manzil | Tavsif |
| :--- | :--- | :--- |
| **Agent Nomi** | Nous Hermes (`hermes`) | Chuqur tadqiqotchi va mustaqil tahlilchi |
| **Bosh Mas'uliyati** | Deep Research, Logic Verification & Second Opinion | Murakkab tizimlarni xolisona tahlil qilish |
| **Asosiy Binar Fayl** | `C:\Users\dilmu\AppData\Local\hermes\bin\hermes.exe` | Rasmiy CLI ijrochi fayli |
| **Node.js Muhiti** | `C:\Users\dilmu\AppData\Local\hermes\node\node.exe` (v22.23.2) | Mahalliy Node.js dasturiy muhiti |
| **Model / API Provayder** | OpenRouter Free (`openrouter/free` endpoint) | Bepul ochiq vaznli yirik modellar |
| **Asosiy Modellar** | `meta-llama/llama-3.3-70b-instruct:free`, `deepseek/deepseek-r1:free` | 128k–164k kontekstli yetakchi modellar |
| **Muloqot Tili** | O'zbek tili (Lotin), English (US) | Ikki tilli chuqur tahlil |
| **Ruxsat Doirasi** | Read-only tadqiqot, worktree izolyatsiyasi | Vault xotirasiga to'g'ridan-to'g'ri yozish taqiqlanadi |
| **Asosiy Protokol** | `[[Concurrency & Sync Protocol]]` va `RULE[user_global]` | To'qnashuvsiz parallel ishlash |
| **Markaziy Qayd** | `[[AI Sozlangan Miyyasi]]` | Butun tizimning yagona haqiqat manbai |

---

## 🚀 Ishga Tushirish va Buyruqlar Sintaksisi (CLI Invocation Syntax)

Nous Hermes turli tahlil rejimlarida buyruqlar satri orqali quyidagi standart sintaksis asosida chaqiriladi:

```powershell
# Standart boshqaruvchisiz (headless) bir martalik so'rov
hermes chat -q "<SAVOL_YOKI_TOPSHIRIQ>" -Q --oneshot

# Chuqur mulohaza (deep reasoning) uchun LLaMA 3.3 70B modeli bilan chaqirish
hermes -z "<PROMPT>" -m meta-llama/llama-3.3-70b-instruct:free

# Multi-agent to'qnashuvlarining oldini olish uchun Git Worktree izolyatsiyasida bajarish
hermes -w chat -q "<TASK>" -Q --oneshot

# Interaktiv zamonaviy TUI terminal interfeysini ishga tushirish
hermes --tui

# Mahalliy veb-boshqaruv panelini ishga tushirish (Port 9119)
hermes dashboard
```

### Kalit Bayroqlar (CLI Flags Reference)
- `-q, --query <matn>`: Prompt yoki topshiriq matni.
- `-Q, --quiet`: Barcha ortiqcha bannerlar va spinnorlarni yashirish (toza matn chiqishi).
- `-z, --oneshot`: Interaktiv bo'lmagan bir martalik rejim; faqat yakuniy javob matnini stdout'ga chiqaradi.
- `-m, --model <model>`: Modelni dinamik ravishda o'zgartirish.
- `--provider <provider>`: Provayderni ko'rsatish (`openrouter`, `groq`, va h.k.).
- `--reasoning <daraja>`: Fikrlash chuqurligini sozlash (`none`, `low`, `medium`, `high`, `max`).
- `-w, --worktree`: Fayl to'qnashuvlarini oldini olish uchun alohida Git worktree'da xavfsiz bajarish.
- `--yolo`: Barcha so'rovlar va ruxsatlarni avtomatik tasdiqlash.

---

## 🎯 Asosiy Vazifalar va Imkoniyatlar (Capabilities & Responsibilities)

1. **Mustaqil Ikkinchi Fikr (Architectural Second Opinion)**:
   - Me'moriy yechimlar va kod tuzilmalariga nisbatan xolis, tanqidiy baho beradi.
   - Yashirin zaifliklar, masshtablashdagi to'siqlar va chekka holatlarni (edge cases) aniqlaydi.

2. **Katta Hajmli Hujjatlarni Tahlil Qilish (Deep Research & Synthesis)**:
   - Ilmiy maqolalar, API spetsifikatsiyalari va tizim loglarini sintez qiladi.
   - OpenRouter bepul modellarining katta kontekst oynalaridan (128k–164k) samarali foydalanadi.

3. **Mantiqiy Deduksiya va Fikrlash Zanjiri (Reasoning Chains)**:
   - Algoritmik murakkablik (Big O), kesh lokalizatsiyasi va asinxron holatlar tahlilida `deepseek/deepseek-r1:free` modelidan foydalanadi.

---

## ⚠️ Xatoliklarni Boshqarish va Cheklovlar (Error Handling & Rate Limits)

- **OpenRouter Rate Limits**: Bepul tier odatda 20 RPM (Requests Per Minute) va 200 RPD (Requests Per Day) bilan cheklangan.
- **Eksponensial Orqaga Chekinish (Exponential Backoff)**: 429 (Too Many Requests) xatosi yuz berganda, 2 soniya, 4 soniya, 8 soniya oraliqlar bilan 3 martagacha qayta urinadi.
- **Model Zaxirasi (Dynamic Fallback)**: Asosiy model band yoki limitga yetganda, Hermes avtomatik ravishda boshqa bepul modelga o'tadi (masalan, `meta-llama/llama-3.3-70b-instruct:free` -> `deepseek/deepseek-chat:free` -> `qwen/qwen-2.5-72b-instruct:free`).

---

## 🔒 Konkurentlik va Hamkorlik Standartlari (Concurrency & Fleet Protocols)

- **Git Worktree Izolyatsiyasi**: Boshqa agentlar (`[[Codex LLM Assistant]]`, `[[Antigravity 1]]`) bilan parallel ishlaganda `-w, --worktree` bayrog'i orqali alohida vaqtinchalik nusxada ishlaydi.
- **Xotiraga Yozish Cheklovi**: Nous Hermes bevosita Obsidian vault fayllarini tahrirlamaydi; uning tahliliy xulosalari Master Orchestrator orqali `[[AI Sozlangan Miyyasi]]` yoki tegishli loyiha xotirasiga kiritiladi.
- Har qanday operatsiyada `[[Concurrency & Sync Protocol]]` qoidalariga amal qilinadi.

---

## 🔗 Aloqador Havolalar (Related Links)

- Bosh Boshqaruv Markazi: [[AI Sozlangan Miyyasi]]
- Asosiy Boshqaruv Paneli: [[Dashboard]]
- Bosh Tizim Arxitektori: [[Antigravity 1]]
- Sandbox Sinovchi Agent: [[Antigravity 2]]
- Kod Generatsiyasi Dvigateli: [[Codex LLM Assistant]]
- Fayllarni Qulflash va Sinxronizatsiya: [[Concurrency & Sync Protocol]]
- Sohalar Xaritasi: [[20 Areas/20 Areas|20 Areas]]
- Sohalar To'liq Xaritasi: [[20 Areas/20 Areas MOC|20 Areas MOC]]
- Git Ish Tartibi: [[30 Resources/Agent Skills/git-workflow|git-workflow]]
