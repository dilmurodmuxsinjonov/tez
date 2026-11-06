---
title: "🗺️ AI Agent Ecosystem Map — Ko'p Agentli Tizim Arxitekturasi va Koordinatsiya Protokoli"
version: "1.0.0"
created: 2026-09-12
updated: 2026-09-12
status: active
type: resource-guide
tags:
  - resource
  - ai-fleet
  - orchestration
  - multi-agent
  - multt-protocol
  - architecture
  - codex
language: "uz-UZ, en-US"
---

# 🗺️ AI Agent Ecosystem Map — Ko'p Agentli Tizim Arxitekturasi va Koordinatsiya Protokoli

> *"Yagona arxitektura, ixtisoslashgan rollar va to'qnashuvsiz hamkorlik — murakkab tizimlarni mukammal boshqarish garovidir."*

---

## 🧭 Asosiy Boshqaruv Havolalari (Core Navigation & Backlinks)

- 🧠 **[[AI Sozlangan Miyyasi|🧠 AI Sozlangan Miyyasi — Universal AI Second Brain]]** (Bosh Markaz)
- 📊 **[[Dashboard|Mening Ikkinchi Miyyam (Dashboard)]]**
- 📚 **[[30 Resources/30 Resources|📚 30 Resources Asosiy Qaydnomasi]]**
- 🛡️ **[[20 Areas/20 Areas|🛡️ 20 Areas Asosiy Qaydnomasi]]**
- ⚖️ **[[30 Resources/Free LLM Models Registry|🌐 Free LLM Models Registry]]**
- 📖 **[[30 Resources/Codex Skills Encyclopedia|📚 Codex Skills Encyclopedia]]**

---

## 1. 🏗️ Ekotizim Arxitekturasi (Hierarchical Ecosystem Topology)

Foydalanuvchi **Dilmurod Muhsinjanov**ning ko'p agentli sun'iy intellekt ekotizimi ierarxik va modulli arxitekturaga asoslangan. Tizim markazida **OpenAI Codex** (`codex.exe`) bosh arxitektor va koordinator (Master Orchestrator) sifatida joylashgan bo'lib, ixtisoslashgan vazifalarni tashqi CLI agentlariga (`hermes`, `copilot`, `opencode`, `agy`, `ruflo`) delegatsiya qiladi va natijalarni yagona haqiqat manbai (**[[AI Sozlangan Miyyasi]]**) atrofida sintezlaydi.

```
                         ┌──────────────────────────────────────────┐
                         │           Foydalanuvchi / SSOT           │
                         │         [[AI Sozlangan Miyyasi]]         │
                         └────────────────────┬─────────────────────┘
                                              │ /multt <task>
                                              ▼
                         ┌──────────────────────────────────────────┐
                         │               OpenAI Codex               │
                         │          (Master Orchestrator)           │
                         │    `codex.exe` (Model: gpt-6-astra)      │
                         │   - Rejalashtirish va dekompozitsiya     │
                         │   - Asosiy arxitektura va kod sintezi    │
                         │   - Natijalarni birlashtirish & audit    │
                         └──────┬──────────┬──────────┬──────────┬──┘
                                │          │          │          │
            ┌───────────────────┘          │          │          └───────────────────┐
            ▼                              ▼          ▼                              ▼
┌───────────────────────┐   ┌───────────────────────────┐   ┌───────────────────────────┐   ┌───────────────────────┐
│      Nous Hermes      │   │      GitHub Copilot       │   │       OpenCode CLI        │   │ Google Antigravity CLI│
│     (`hermes.exe`)    │   │       (`copilot.ps1`)     │   │      (`opencode.ps1`)     │   │      (`agy.exe`)      │
│ - Chuqur tadqiqot     │   │ - Git lifecycle nazorati  │   │ - Ochiq modellar sinovi   │   │ - Tizimli arxitektura │
│ - Ikkinchi fikr       │   │ - PR va commit auditi     │   │ - Nol xarajatli refaktor  │   │ - Katta monorepo kod  │
│ - Mantiqiy tahlil     │   │ - Repozitoriy tuzilmasi   │   │ - Birlik (unit) testlar   │   │ - Chuqur nosozliklar  │
└───────────────────────┘   └───────────────────────────┘   └───────────────────────────┘   └───────────────────────┘
            │                              │                             │                              │
            └──────────────────────────────┼─────────────────────────────┴──────────────────────────────┘
                                           │
                                           ▼
                         ┌──────────────────────────────────────────┐
                         │           Ruflo Swarm Platform           │
                         │         (`ruflo.ps1` v3.38.23)           │
                         │   - 15-agentli ierarxik to'r (mesh)      │
                         │   - Mahalliy AgentDB HNSW vektor xotirasi │
                         │   - 35+ Model Context Protocol (MCP)     │
                         └──────────────────────────────────────────┘
```

---

## 2. 📋 Agentlar Floti Parametrlari va Rollar Matritsasi

| Agent | CLI Binar / Skript Manzili | Model / Muhit | Asosiy Rol va Maydoni | Havola |
| :--- | :--- | :--- | :--- | :--- |
| **OpenAI Codex** | `C:\Users\dilmu\AppData\Local\Programs\OpenAI\Codex\bin\codex.exe` | `gpt-6-astra` (priority tier) | Bosh tizim koordinatori, arxitektura rejalashtirish, kod sintezi | [[Codex LLM Assistant]] |
| **Nous Hermes** | `C:\Users\dilmu\AppData\Local\hermes\bin\hermes.exe` | OpenRouter Free (`openrouter/free`) | Chuqur tadqiqot, mustaqil tahlil, ikkinchi fikr (second opinion) | [[Nous Hermes]] |
| **GitHub Copilot** | `C:\Users\dilmu\AppData\Roaming\npm\copilot.ps1` | GitHub User (`dilmurodmuxsinjonov`) | Git lifecycle operatsiyalari, PR auditi, repozitoriy tekshiruvi | [[GitHub Copilot]] |
| **OpenCode CLI** | `C:\Users\dilmu\AppData\Roaming\npm\opencode.ps1` | OpenCode Zen (Nemotron, MiMo, Qwen) | Ochiq kodli modellar sinovi, nol xarajatli refaktoring, unit testlar | [[OpenCode CLI]] |
| **Google Antigravity CLI** | `C:\Users\dilmu\AppData\Local\agy\bin\agy.exe` | Google DeepMind (`dilmurodmuhsinjanov910@gmail.com`) | Chuqur arxitektura tekshiruvi, monorepo tahlili, kompleks debugging | [[Google Antigravity CLI]] |
| **Ruflo Swarm** | `C:\Users\dilmu\AppData\Local\hermes\node\ruflo.ps1` | Local AgentDB + Vector Bridge | Ko'p agentli swarm klasteri, HNSW semantik qidiruv, 35+ MCP integratsiyasi | [[Ruflo Swarm]] |
| **Antigravity 1** | Obsidian Interfaol Sessiyasi | Primary Google Account | Bosh interaktiv me'mor, loyihalar rejalashtiruvchisi, foydalanuvchi aloqasi | [[Antigravity 1]] |
| **Antigravity 2** | Sandbox Izolyatsiyalangan Sessiyasi | Secondary Isolated Google Account | Katta hisoblashlar, mustaqil testlar, toza xona (clean-room) tadqiqotlari | [[Antigravity 2]] |

---

## 3. ⚡ Codex Ko'p Agentli Muvofiqlashtirish Protokoli (`/multt`)

`C:\Users\dilmu\.codex\AGENTS.md` va `tashqi_ai_agentlar` maxsus ko'nikmasida belgilanganidek, ko'p agentli rejim quyidagi qat'iy tamoyillar asosida ishlaydi:

### 3.1 Faollashtirish va Boshqarish Sintaksisi (Activation & Lifecycle)

```powershell
# 1. Ko'p agentli rejimni faollashtirish va vazifani boshlash
/multt <topshiriq_matni>

# 2. Faol agentlar holatini tekshirish
/multt status

# 3. Ko'p agentli rejimni o'chirish va yagona agent rejimiga qaytish
/multt off
```

- `/multt` rejimi bir marta yoqilgach, butun seans davomida faol bo'lib qoladi va har bir murakkab topshiriqda Codex avtomatik ravishda tashqi yordamchilarni jalb qiladi.
- Faqat `/multt off` kiritilganda tashqi agentlarni chaqirish to'xtatiladi.

### 3.2 Ish Oldi Tekshiruvlari (Pre-Flight Checks)

Har qanday tashqi agentni chaqirishdan oldin Codex quyidagilarni tekshiradi:
1. **Binar mavjudligi**: PowerShell'da `Get-Command <cli>` orqali bajariluvchi fayl mavjudligi tekshiriladi.
2. **API kalitlari va autentifikatsiya**: Kerakli muhit o'zgaruvchilari (`OPENROUTER_API_KEY`, `GROQ_API_KEY`, GitHub tokenlari) faolligi aniqlanadi.
3. **Qulflar holati**: `.agents/locks/` katalogida to'qnashuv yo'qligi tekshiriladi (`[[Concurrency & Sync Protocol]]`).

### 3.3 Delegatsiya Matritsasi (Delegation Matrix)

Codex topshiriqning tabiati bo'yicha agentlarni quyidagi qoidalar asosida tanlaydi:

| Vazifa Turi | Tanlangan Agent | CLI Chaqiruv Namunasi |
| :--- | :--- | :--- |
| **Noma'lum muammo bo'yicha tadqiqot & tahlil** | Nous Hermes | `hermes chat -q "<SAVOL>" -Q --oneshot` |
| **Git operatsiyalari, PR va commit tekshiruvi** | GitHub Copilot | `copilot -p "<BUYRUQ>" --allow-all -s` |
| **Ochiq modelda test yoki tezkor refaktoring** | OpenCode CLI | `opencode run --model opencode/nemotron-3.5-lightning-free "<TASK>" --auto` |
| **Katta tizim arxitekturasi va monorepo tahlili** | Antigravity CLI | `agy -p "<SAVOL>" --effort high --dangerously-skip-permissions` |
| **Vektor xotiradan semantik qidiruv yoki swarm** | Ruflo Swarm | `ruflo memory search -q "<QIDIRUV>"` yoki `ruflo swarm init` |

---

## 4. 🔒 Concurrency, Izolyatsiya va To'qnashuvlarning Oldini Olish

Ko'p agentli tizimda fayllar butunligi va izchilligini ta'minlash uchun 4 ta mustahkam to'siq o'rnatilgan:

1. **Yagona Tahrir Qoidasi (Exclusive Write Invariant)**:
   - Hech qachon ikki agent bir vaqtning o'zida bitta faylni tahrirlashi mumkin emas.
   - Har bir tahrir qilinadigan fayl uchun `.agents/locks/<sha256_hash>.lock` qulf fayli yaratiladi.
   - Qulf muddati: **300 soniya** (5 daqiqa). Agar muddat o'tib ketsa, eskirgan (stale) qulf deb hisoblanib, qayta tiklanadi.

2. **Git Worktree Izolyatsiyasi (Isolated Worktrees)**:
   - Nous Hermes yoki OpenCode CLI katta hajmdagi mustaqil sinovlarni o'tkazganda `-w, --worktree` bayrog'i yordamida asosiy ishchi daraxtga teginmasdan alohida Git nusxasida ishlaydi.

3. **Ikki Bosqichli Atomik Saqlash (Atomic Two-Stage Write)**:
   - O'zgarishlar avval vaqtinchalik faylga (`<file>.tmp.<agent_id>`) yoziladi.
   - Sintaksis, UTF-8 kodlash va havolalar tekshirilgach, fayl asosiy nomga atomik ravishda ko'chiriladi (`Move-Item -Force`).

4. **Vault Himoyasi (Vault Write Barrier)**:
   - Tashqi CLI agentlar (`hermes`, `opencode`, `copilot`) loyiha kod bazalarida (`C:\Users\dilmu\...`) ishlaydi, ammo Obsidian vault (`D:\obsidian file`) ichidagi xotira fayllarini to'g'ridan-to'g'ri o'zgartirmaydi.
   - Vault qaydlarini faqat Master Orchestrator (**OpenAI Codex**) yoki **Antigravity 1** yangilaydi.

---

## 5. ⚡ Parallel Bajarish va Sintez Oqimi (Parallel Execution & Synthesis)

Codex ko'p agentli topshiriqlarni quyidagi konveyer bo'yicha bajaradi:

```
[1. Rejalashtirish] ──► Codex topshiriqni mustaqil qismlarga ajratadi
                              │
         ┌────────────────────┴────────────────────┐
         ▼                                         ▼
[2. Tashqi Chaqiruv]                      [3. Asosiy Ish]
Codex fon rejimida CLI agentni            Codex kutib o'tirmasdan,
ishga tushiradi (subshell/async)          asosiy tizim kodini yozishda
(masalan: hermes tahlil qilmoqda)         davom etadi
         │                                         │
         └────────────────────┬────────────────────┘
                              ▼
[4. Audit va Diff Tekshiruvi] ──► Codex tashqi agent chiqishini (stdout/JSON) o'qiydi,
                                  git diff va testlarni (`pytest`, `npm test`) tekshiradi
                              ▼
[5. Yaxlit Sintez] ────────────► Codex barcha ma'lumotlarni birlashtirib,
                                  foydalanuvchiga yagona yakuniy natijani taqdim etadi
```

### Haqiqiy Natijalar Qoidasi (Integrity Mandate)
- Codex hech qachon chaqirilmagan agent nomidan yolg'on hisobot bermaydi.
- Agar tashqi agent ishlatilmagan bo'lsa, javobda faqat Codex bajargan ish aks etadi.
- Agar tashqi agent chaqirilsa, uning haqiqiy buyrug'i va qaytargan faktik natijasi ko'rsatiladi.

---

## 6. 🛠️ Nosozliklarni Boshqarish va Qayta Tiklash (Failure Handling & Fallback)

| Nosozlik Holati | Alomat / Xatolik | Avtomatik Qayta Tiklash Chorasi |
| :--- | :--- | :--- |
| **CLI Binar topilmadi** | `CommandNotFoundException` | Codex darhol o'zining ichki sintez mexanizmiga o'tadi va foydalanuvchiga binar yetishmovchiligini xabar qiladi. |
| **API Limit (Rate Limit / 429)** | `Rate limit exceeded` | OpenRouter yoki Groq limiti to'lganda, `[[30 Resources/Free LLM Models Registry\|Free LLM Models Registry]]` bo'yicha zaxira bepul modelga yo'naltiriladi. |
| **Jarayon qotib qolishi (Timeout)** | 120s dan ortiq sukunat | Subshell jarayoni to'xtatiladi (`Stop-Process`), vaqtinchalik ishchi daraxt tozalanadi va vazifani Codex o'zi bajaradi. |
| **Git Merge to'qnashuvi** | Git conflict markers | Qaytarish (`git merge --abort`), toza holatni tiklash va o'zgarishlarni ketma-ket qo'lda birlashtirish. |

---

## 7. 📑 Yangi Agentlarni Qo'shish Standarti (Workflow Integration)

Kelgusida yangi AI agent yoki CLI vositasini ushbu tizimga integratsiya qilishda rasmiy **[[50 Templates/New Agent Integration Template|New Agent Integration Template]]** shablonidan foydalaniladi. Har bir yangi agent uchun:
1. `20 Areas/Agent Profiles/` katalogida yangi profil qaydi yaratiladi.
2. `AI Sozlangan Miyyasi.md` va ushbu xaritaga binar manzillari kiritiladi.
3. `/multt` delegatsiya qoidalarida uning mas'uliyat doirasi belgilanadi.

---

## 🔗 Aloqador Tizim Havolalari

- Bosh Haqiqat Manbai: [[AI Sozlangan Miyyasi]]
- Boshqaruv Paneli: [[Dashboard]]
- Bepul LLM Modellar Katalogi: [[30 Resources/Free LLM Models Registry|Free LLM Models Registry]]
- Codex Ko'nikmalar Qomusi: [[30 Resources/Codex Skills Encyclopedia|Codex Skills Encyclopedia]]
- Konkurentlik Protokoli: [[Concurrency & Sync Protocol]]
- Sohalar Xaritasi: [[20 Areas/20 Areas|20 Areas]]
- Resurslar Xaritasi: [[30 Resources/30 Resources|30 Resources]]
