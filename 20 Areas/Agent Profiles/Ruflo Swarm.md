---
title: "🐝 Ruflo Swarm — Multi-Agent Swarm Orchestrator & Vector Memory Engine"
version: "1.0.0"
date: 2026-09-12
created: 2026-09-12
updated: 2026-09-12
status: active
type: agent-profile
agent: "Ruflo Swarm"
role: swarm-orchestrator
tags:
  - agent-profile
  - ruflo
  - swarm
  - vector-memory
  - hnsw
  - cli
  - ai-fleet
language: "uz-UZ, en-US"
---

# 🐝 Ruflo Swarm — Multi-Agent Swarm Orchestrator & Vector Memory Engine

> *"Ierarxik to'da koordinatsiyasi, HNSW semantik vektor xotirasi va chaqmoqdek tez kontekst qidiruvi — avtonom ko'p agentli intellekt ustunidir."*

Ushbu profil **Ruflo Swarm Orchestrator** (`ruflo.ps1` v3.38.23) ko'p agentli to'dalar (swarms) va yuqori tezlikdagi HNSW vektor xotirasi boshqaruv dvigateli uchun rasmiy operatsion qo'llanma hisoblanadi. Ruflo Swarm foydalanuvchining ko'p agentli floti (`[[AI Sozlangan Miyyasi]]`) tarkibida 15 tagacha ixtisoslashgan subagentlarni ierarxik to'r (mesh) topologiyasida muvofiqlashtirish, mahalliy AgentDB orqali semantik qidiruvni amalga oshirish hamda 35+ MCP plaginlarini boshqarishga mas'uldir.

---

## 📋 Profil va Vositalar Parametrlari (Profile & Toolchain)

| Parametr | Qiymat / Manzil | Tavsif |
| :--- | :--- | :--- |
| **Agent Nomi** | Ruflo Swarm Orchestrator (`ruflo`) | Ko'p agentli to'dalar va vektor xotira koordinatori |
| **Bosh Mas'uliyati** | Swarm Topology Coordination, HNSW Vector Memory & MCP Plugins | To'dani boshqarish va semantik xotira qidiruvi |
| **CLI Skripti** | `C:\Users\dilmu\AppData\Local\hermes\node\ruflo.ps1` (v3.38.23) | Rasmiy Node.js asosidagi CLI skripti |
| **Node.js Muhiti** | `C:\Users\dilmu\AppData\Local\hermes\node\node.exe` (v22.23.2) | Mahalliy Node.js dasturiy muhiti |
| **Vektor Xotira Dvigateli** | AgentDB + HNSW (Hierarchical Navigable Small World) | Relyatsion qidiruvdan 150x–12,500x tezroq qidiruv |
| **Ma'lumotlar Ko'prigi** | Vector PostgreSQL Bridge & Local Storage | Doimiy vektor ko'rsatkichlari bazasi |
| **Plaginlar Ekotizimi** | 35+ Model Context Protocol (MCP) serverlari | Asboblar, xavfsizlik va ma'lumotlar integratsiyasi |
| **Tizim Qobig'i** | Windows PowerShell 5.1 / 7.x | Asosiy buyruqlar satri qobig'i |
| **Muloqot Tili** | O'zbek tili (Lotin), English (US) | Ikki tilli tizimli hisobotlar |
| **Asosiy Protokol** | `[[Concurrency & Sync Protocol]]` va `RULE[user_global]` | Qulflash va xavfsiz to'da operatsiyalari |
| **Markaziy Qayd** | `[[AI Sozlangan Miyyasi]]` | Butun tizimning yagona haqiqat manbai |

---

## 🚀 Ishga Tushirish va Buyruqlar Sintaksisi (CLI Invocation Syntax)

Ruflo Swarm turli to'da operatsiyalari va xotira boshqaruvida quyidagi standart sintaksis asosida chaqiriladi:

```powershell
# Joriy ish maydonida V3 rejimdagi ko'p agentli to'dani initsializatsiya qilish
ruflo swarm init --v3-mode

# Mahalliy vektor xotirasidan semantik qidiruv o'tkazish
ruflo memory search -q "<QIDIRUV_SO'ROVI>"

# Maxsus ixtisoslashgan agentni dinamik tarzda ishga tushirish (masalan: coder, architect, reviewer)
ruflo agent spawn -t coder

# Ruflo Model Context Protocol (MCP) serverini ishga tushirish
ruflo mcp start

# Tizim bo'yicha xavfsizlik va zaifliklar skanerini yurgizish
ruflo security scan
```

### Kalit Buyruqlar va Bayroqlar (CLI Command Reference)
- `swarm init [--v3-mode]`: Ko'p agentli to'da arxitekturasini faollashtirish.
- `memory search -q <matn>`: HNSW indeksi bo'yicha tabiiy tilda semantik o'xshashlikni qidirish.
- `agent spawn -t <tur>`: Berilgan turdagi yangi subagentni to'daga qo'shish (`coder`, `tester`, `reviewer`, `architect`).
- `mcp start`: Barcha ulangan 35+ MCP plaginlari uchun markaziy marshrutizatorni ishga tushirish.
- `security scan`: Repozitoriy va agent amallari bo'yicha zaifliklarni skanerlash.

---

## 🧠 HNSW Vektor Xotirasi Arxitekturasi (Vector Memory Engine)

Ruflo an'anaviy relyatsion ma'lumotlar bazalariga qaraganda keskin samarali bo'lgan vektorli arxitekturaga tayanadi:

1. **HNSW Indekslash (Hierarchical Navigable Small World)**:
   - Ko'p o'lchamli vektor fazosida logarifmik vaqt murakkabligida ($O(\log N)$) eng yaqin qo'shnilarni topadi.
   - Matn va kod parchalarini 150x dan 12,500x gacha tezroq indekslaydi va qidiradi.

2. **Semantik Qidiruv va Kontekstni Tiklash**:
   - Avvalgi topshiriqlar, xatolar tarixi va yechimlarni vektorli xotirada saqlab, yangi topshiriqlarda darhol kerakli kontekstni chiqaradi.
   - Flash Attention mexanizmi yordamida kontekstni ixchamlashtiradi.

---

## 🕸️ To'da Topologiyasi va Ierarxik Muvofiqlashtirish (Swarm Topology)

Ruflo ko'p agentli tizimida to'r (mesh) va ierarxik boshqaruv birlashtirilgan:

```
                  ┌──────────────────────────────┐
                  │    Ruflo Swarm Coordinator   │
                  │        (Queen / Leader)      │
                  └──────────────┬───────────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Worker: Coder  │     │ Worker: Tester  │     │Worker: Reviewer │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │   Local AgentDB Vector Store │
                  │     (HNSW Semantic Memory)   │
                  └──────────────────────────────┘
```

- **Lider (Queen Agent)**: Topshiriqni mayda bo'laklarga ajratadi va tegishli subagentlarga yo'naltiradi.
- **Ishchi Agentlar (Specialized Workers)**: Har bir agent o'z yo'nalishi bo'yicha bir vaqtning o'zida parallel faoliyat olib boradi.
- **O'z-o'zini Tiklash (Self-Healing)**: Biror subagent nosozlikka uchrasa, uning vazifasi avtomatik tarzda boshqa agentga qayta taqsimlanadi.

---

## 🔒 Konkurentlik va Xavfsizlik Qoidalari (Concurrency & Security)

- **Fayllar Xavfsizligi**: Ko'p sonli agentlar bir vaqtda ishlaganda fayllar to'qnashuvini oldini olish uchun `[[Concurrency & Sync Protocol]]` qoidalari to'liq tatbiq etiladi.
- **Xotira Yaxlitligi**: Vektor xotirasi nosozliklar paytida yo'qolmasligi uchun muntazam atomik nazorat nuqtalari (checkpoints) olinadi.

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
