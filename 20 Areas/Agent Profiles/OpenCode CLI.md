---
title: "⚡ OpenCode CLI — Open-Source Model Tester & Code Refactorer"
version: "1.0.0"
date: 2026-09-12
created: 2026-09-12
updated: 2026-09-12
status: active
type: agent-profile
agent: "OpenCode CLI"
role: open-source-tester
tags:
  - agent-profile
  - opencode
  - oss-models
  - nemotron
  - cli
  - ai-fleet
language: "uz-UZ, en-US"
---

# ⚡ OpenCode CLI — Open-Source Model Tester & Code Refactorer

> *"Ochiq manbali modellarning qudrati, nol xarajatli refaktoring va tezkor sinovlar — arxitekturaning erkinlik poydevoridir."*

Ushbu profil **OpenCode CLI** (`opencode.ps1`) ochiq manbali LLM modellari asosida kod generatsiyasi, testlar yaratish va dasturiy kodni qayta ishlashga ixtisoslashgan avtonom agent uchun rasmiy operatsion qo'llanma hisoblanadi. OpenCode foydalanuvchining ko'p agentli floti (`[[AI Sozlangan Miyyasi]]`) tarkibida ochiq vaznli ilg'or modellarni (NVIDIA Nemotron, Xiaomi MiMo, Alibaba Qwen va h.k.) sinovdan o'tkazish, nol xarajatli kod refaktoringi va tezkor birlik (unit) testlarini yozishga javobgardir.

---

## 📋 Profil va Vositalar Parametrlari (Profile & Toolchain)

| Parametr | Qiymat / Manzil | Tavsif |
| :--- | :--- | :--- |
| **Agent Nomi** | OpenCode CLI (`opencode`) | Ochiq kodli modellar sinovchisi va refaktorer |
| **Bosh Mas'uliyati** | OSS Model Testing, Zero-Cost Refactoring & Unit Tests | Kod sifatini oshirish va tejamkor generatsiya |
| **CLI Skripti** | `C:\Users\dilmu\AppData\Roaming\npm\opencode.ps1` | Rasmiy Node.js asosidagi CLI skripti |
| **Node.js Muhiti** | `C:\Users\dilmu\AppData\Local\hermes\node\node.exe` (v22.23.2) | Mahalliy Node.js dasturiy muhiti |
| **Asosiy Provayderlar** | OpenCode Zen Community Free & OpenRouter | Bepul ochiq modellar to'plami |
| **Qo'llab-quvvatlanadigan Modellar** | `nemotron-3.5-lightning`, `mimo-v2.5`, `ling-3.0-flash`, `qwen-2.5-coder` | Turli o'lcham va arxitekturadagi modellar |
| **Tizim Qobig'i** | Windows PowerShell 5.1 / 7.x | Asosiy buyruqlar satri qobig'i |
| **Muloqot Tili** | O'zbek tili (Lotin), English (US) | Ikki tilli texnik muloqot |
| **Ruxsat Doirasi** | Repozitoriy kod bazalari va test kataloglari | To'g'ridan-to'g'ri kod bilan ishlash |
| **Asosiy Protokol** | `[[Concurrency & Sync Protocol]]` va `RULE[user_global]` | Atomik yozish va xavfsiz testlash |
| **Markaziy Qayd** | `[[AI Sozlangan Miyyasi]]` | Butun tizimning yagona haqiqat manbai |

---

## 🚀 Ishga Tushirish va Buyruqlar Sintaksisi (CLI Invocation Syntax)

OpenCode CLI turli kod sintezi va testlash jarayonlarida buyruqlar satri orqali quyidagi standart sintaksis asosida chaqiriladi:

```powershell
# Nemotron 3.5 Lightning Free modeli bilan topshiriqni bajarish
opencode run --model opencode/nemotron-3.5-lightning-free "<TOPSHIRIQ>"

# MiMo v2.5 bepul modeli yordamida frontend komponentini tahrirlash
opencode run --model opencode/mimo-v2.5-free "<TOPSHIRIQ>"

# OpenRouter bepul meta-routeri orqali avtonom topshiriqni bajarish
opencode run --model openrouter/free "<TOPSHIRIQ>"

# Standart avtomatik tasdiqlash bilan boshqaruvchisiz (headless) bajarish
opencode run "<TASK>" --auto

# Mavjud provayderlar va modellarning to'liq ro'yxatini ko'rish
opencode models
```

### Kalit Bayroqlar (CLI Flags Reference)
- `run [xabar..]`: Topshiriq matnini to'g'ridan-to'g'ri bajarish.
- `-m, --model <provider/model>`: Maqsadli model va provayderni aniq belgilash.
- `--auto`: Xavfli bo'lmagan barcha ruxsatlarni avtomatik tasdiqlash.
- `-c, --continue`: Avvalgi sessiyani to'xtagan joyidan davom ettirish.
- `-s, --session <id>`: Aniq sessiya identifikatoriga ulanish.
- `--pure`: Tashqi plaginlarsiz sof rejimda ishga tushirish.
- `models [provider]`: Belgilangan provayder bo'yicha mavjud modellar ro'yxatini chiqarish.

---

## 🎯 Asosiy Vazifalar va Imkoniyatlar (Capabilities & Use Cases)

1. **Ochiq Kodli Modellarni Sinovdan O'tkazish (OSS Model Benchmarking)**:
   - Yangi chiqqan ochiq vaznli modellarni (Nemotron, MiMo, Qwen, Ling) amaliy dasturlash vazifalarida sinaydi.
   - Modellarning kod sintaksisi aniqligi va tezligini taqqoslaydi.

2. **Nol Xarajatli Kod Refaktoringi (Zero-Cost AST Refactoring)**:
   - Tijoriy modellarga mablag' sarflamasdan katta hajmdagi fayllarni refaktoring qiladi.
   - Eskirgan sintaksisni zamonaviy ECMAScript yoki Python 3.12 standartlariga moslashtiradi.

3. **Birlik Testlarini Yaratish (Unit Test Generation)**:
   - Modullar uchun mock obyektlar va chekka holatlarni (edge cases) qamrab oluvchi test paketlarini avtomatik generatsiya qiladi.
   - Loyihadagi mavjud test runnerlar (`pytest`, `npm test`) bilan to'liq integratsiyalashadi.

---

## ⚠️ Xatoliklarni Boshqarish va Seansni Qayta Tiklash (Error Handling & Recovery)

- **Seansni Qayta Tiklash**: Tarmoq uzilishi yoki xatolik yuz berganda, `-c, --continue` bayrog'i yordamida seans konteksti yo'qotilmasdan tiklanadi.
- **Model Fallback Mexanizmi**: Muayyan jamoat (community) modeli vaqtinchalik javob bermasa, avtomatik ravishda boshqa ochiq modelga (masalan, `nemotron` -> `qwen-2.5-coder`) yo'naltiriladi.
- **Sintaksis Tekshiruvi**: O'zgarish kiritilgach, avval sintaktik daraxt (AST) tekshiriladi, nosoz kod bazaga yozilmaydi.

---

## 🔒 Konkurentlik va Hamkorlik Standartlari (Concurrency & Fleet Protocols)

- **Kod Bazasida Xavfsiz Ishlash**: OpenCode bevosita loyiha repozitoriylarida ishlaydi, ammo Obsidian vault qaydlarini tahrirlamaydi.
- **Ikki Bosqichli Yozish**: Fayllar yaxlitligini ta'minlash uchun `[[Concurrency & Sync Protocol]]` talablariga rioya qilib, o'zgarishlarni vaqtinchalik fayllar orqali saqlaydi.
- O'zgarishlar yakunlangach, natijalar `[[Codex LLM Assistant]]` yoki `[[Antigravity 1]]` ga taqdim etiladi.

---

## 🔗 Aloqador Havolalar (Related Links)

- Bosh Boshqaruv Markazi: [[AI Sozlangan Miyyasi]]
- Asosiy Boshqaruv Paneli: [[Dashboard]]
- Ekotizim Xaritasi: [[30 Resources/AI Agent Ecosystem Map|AI Agent Ecosystem Map]]
- Bepul Modellar Registri: [[30 Resources/Free LLM Models Registry|Free LLM Models Registry]]
- Bosh Tizim Arxitektori: [[Antigravity 1]]
- Sandbox Sinovchi Agent: [[Antigravity 2]]
- Kod Generatsiyasi Dvigateli: [[Codex LLM Assistant]]
- Fayllarni Qulflash va Sinxronizatsiya: [[Concurrency & Sync Protocol]]
- Sohalar Xaritasi: [[20 Areas/20 Areas|20 Areas]]
- Sohalar To'liq Xaritasi: [[20 Areas/20 Areas MOC|20 Areas MOC]]
- Git Ish Tartibi: [[30 Resources/Agent Skills/git-workflow|git-workflow]]
