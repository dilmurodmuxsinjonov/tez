---
title: "🔒 Concurrency & Sync Protocol — Multi-Agent File Locking & Synchronization"
version: "1.0.0"
created: 2026-09-11
updated: 2026-09-11
status: active
type: protocol
tags:
  - protocol
  - concurrency
  - file-locking
  - synchronization
language: "uz-UZ, en-US"
---

# 🔒 Concurrency & Sync Protocol — Multi-Agent File Locking & Synchronization

> *"To'qnashuvsiz parallelizm — mustahkam taqsimlangan tizimlar va ko'p agentli arxitekturaning poydevoridir."*

Ushbu hujjat **Universal AI Second Brain** (`[[AI Sozlangan Miyyasi]]`) tizimida bir vaqtda ishlayotgan barcha sun'iy intellekt agentlari (**Antigravity 1**, **Antigravity 2**, **Codex LLM Assistant** va tashqi avtonom agentlar) uchun umumiy fayllarni xavfsiz o'zgartirish, blokirovka qilish va ma'lumotlar yo'qolishining oldini olish protokolidir.

---

## 🏛️ Arxitektura va Qulflash Katalogi (Locks Architecture)

Ko'p agentli muhitda barcha blokirovkalar markaziy katalogda saqlanadi:
- **Blokirovka Katalogi**: `D:\obsidian file\.agents\locks\`
- **Audit Jurnali**: `D:\obsidian file\.agents\locks\audit.log`

Har qanday faylga (masalan, `AI Sozlangan Miyyasi.md` yoki `10 Projects/MobCreatorWebApp.md`) yozishdan oldin unga mos qulf fayli olinadi.

### 🔑 Qulf Fayli Nomi Sxemasi (Lockfile Naming)
Qulf fayli nomi maqsadli faylning vaultga nisbatan kichik harflarga keltirilgan va to'g'ri chiziq bilan ajratilgan nisbiy yo'lining **SHA-256 xeshi** asosida shakllanadi:
```text
hash = SHA256(normalize_path(target_rel_path))
lockfile_path = .agents/locks/<hash>.lock
```
*Misol*: `10 projects/mobcreatorwebapp.md` -> `.agents/locks/4f2a...8c1b.lock`.

---

## 📄 Qulf Faylining JSON Sxemasi (Lockfile Schema)

Har bir `.lock` fayli quyidagi standart JSON tuzilmasiga ega bo'lishi shart:

```json
{
  "target_file": "10 Projects/MobCreatorWebApp.md",
  "locked_by": "Antigravity_1",
  "agent_conv_id": "e911061f-fabc-4105-bfef-4e8e0237293d",
  "pid": 14208,
  "timestamp": "2026-09-11T18:50:00Z",
  "acquired_at": "2026-09-11T18:50:00Z",
  "acquired_timestamp": 1789152600.0,
  "ttl_seconds": 300,
  "expires_at": "2026-09-11T18:55:00Z",
  "purpose": "Updating active project latest state summary and next steps"
}
```

### Parametrlar Tavsifi:
- `target_file`: O'zgartirilayotgan maqsadli faylning nisbiy yo'li.
- `locked_by`: Qulfni olgan agent identifikatori (`Antigravity_1`, `Antigravity_2`, `Codex`).
- `agent_conv_id`: Agentning faol sessiya identifikatori.
- `pid`: Jarayon identifikatori (Process ID).
- `acquired_at` / `timestamp`: Qulf olingan vaqt (ISO 8601).
- `acquired_timestamp`: Qulf olingan vaqt soniyalarda (epoch float).
- `ttl_seconds`: Qulfning yashash muddati (standart: 300 soniya / 5 daqiqa).
- `expires_at`: Qulfning amal qilish muddati tugash vaqti (ISO 8601).
- `purpose`: Bajarilayotgan operatsiyaning qisqacha maqsadi.

---

## ⚙️ Qulflash Algoritmi va Ish Tartibi (Locking Lifecycle)

```
       [Faylga yozish talabi]
                 │
                 ▼
     [.lock fayli mavjudmi?]
        ├── Yo'q ──────────────────────────────────────────┐
        │                                                  │
       Ha                                                  ▼
        │                                        [Yangi .lock yozish]
        ▼                                                  │
[(hozir - acquired) < TTL (300s)?]                         ▼
   ├── Ha ──> [TO'QNASHUV (Collision)]               [Ikki bosqichli]
   │          Kutish (2000ms) va qayta urinish       [atomik yozish]
   │                                                       │
  Yo'q (Eski qulf: Stale Lock)                             ▼
   │                                                [.lock o'chirish]
   ▼                                                       │
[Auditga yozish: STALE_LOCK_BROKEN]                        ▼
Eski qulfni o'chirish va yangisini olish ────────> [Ish yakunlandi]
```

### 1. Qulfni Olish (Acquire Lock)
1. Maqsadli fayl yo'liga mos `.agents/locks/<hash>.lock` mavjudligini tekshiring.
2. Agar qulf mavjud bo'lsa:
   - Faylni o'qing. Agar `hozirgi_vaqt - acquired_timestamp < ttl_seconds` (300s) bo'lsa: **Faol to'qnashuv**. Jarayon 2000ms kutib, 3 martagacha qayta urinadi.
   - Agar qulf yoshi 300 soniyadan oshgan bo'lsa yoki fayl buzilgan (corrupt/empty) bo'lsa: **Stale Lock**. Agent qulfni bekor qiladi, audit jurnaliga (`.agents/locks/audit.log`) yozadi va o'z qulfini o'rnatadi.
3. Yangi qulf ma'lumotlarini avval `.agents/locks/<hash>.tmp.<agent_id>` ga yozib, atomik ravishda `<hash>.lock` ga almashtiradi.

### 2. Qulfni Bo'shatish (Release Lock)
- Yozish operatsiyasi yakunlangach, agent zudlik bilan `.lock` faylini o'chiradi va audit jurnaliga `LOCK_RELEASED` yozuvini kiritadi.

---

## 🛡️ Ikki Bosqichli Atomik Yozish Standarti (Two-Stage Atomic Write)

Fayllarga yozish paytida tizim o'chib qolishi yoki xatoliklar tufayli ma'lumotlar buzilishining oldini olish uchun quyidagi tartib majburiydir:

1. **Vaqtinchalik Faylga Yozish**:
   - Yangi ma'lumotlar asosiy fayl bilan bir katalogda joylashgan `<maqsadli_fayl>.tmp.<agent_id>` vaqtinchalik fayliga yoziladi.
2. **Sintaktik va Yaxlitlik Tekshiruvi (Integrity Validation)**:
   - Vaqtinchalik faylning YAML frontmatter'i to'g'riligi, Markdown formatining yopiqligi (juft ```) va wikilinklar mavjudligi tekshiriladi.
   - Agar tekshiruv muvaffaqiyatsiz tugasa: vaqtinchalik fayl zudlik bilan o'chiriladi, asosiy faylga tegilmaydi va xatolik qaytariladi.
3. **Atomik Almashtirish (Atomic Replace)**:
   - Tekshiruvdan muvaffaqiyatli o'tgach, tizim operatsion sathi orqali (`replace` / `rename`) vaqtinchalik fayl asosiy fayl ustiga atomik ravishda ko'chiriladi.

---

## 🪟 Windows Tizimida Qayta Urinish Sikli (Windows WinError 32 Mitigation)

Windows operatsion tizimida fayl qidiruv indeksatorlari (Windows Search Indexer), antivirus dasturlari yoki ochiq dasturlar (Obsidian, VS Code) faylni qisqa vaqtga bloklashi (`PermissionError: [WinError 32] The process cannot access the file`) mumkin.

Bunga qarshi kurashish uchun barcha agentlar quyidagi qayta urinish taktikasini qo'llaydi:
- **Urinishlar soni**: 3 ta urinish.
- **Kutish vaqti (Jitter)**: 50 dan 100 millisoniyagacha tasodifiy kutish (exponential backoff with jitter).
- Ushbu sikl tranzit blokirovkalarni foydalanuvchiga xatolik bermasdan avtomatik yechish imkonini beradi.

---

## 🌿 Git Tarmoqlarini Ajratish Standarti (Git Branch Partitioning)

Bir vaqtning o'zida bir nechta agent ishlayotganda Git to'qnashuvlarining (merge conflicts) oldini olish maqsadida har bir agent alohida shoxlarda ishlaydi:

| Agent | Ishchi Tarmoq Andozasi | Vazifasi |
| :--- | :--- | :--- |
| **[[Antigravity 1]]** | `main` yoki `feature/arch-...` | Markaziy arxitektura, xotira bloklari va umumiy integratsiya |
| **[[Antigravity 2]]** | `feature/antigravity2-...` yoki `feature/research-...` | Izolyatsiyalangan sinovlar, benchmarklar va tadqiqotlar |
| **[[Codex LLM Assistant]]** | `feature/codex-...` yoki `fix/codex-...` | Modullar kodi, OpenAPI marshrutlari va avtomatlashtirilgan testlar |

### Birlashtirish (Merge) Qoidasi:
- Agentlar tomonidan ochilgan alohida tarmoqlar faqatgina to'liq avtomatlashtirilgan testlar to'plami (`run_e2e_tests.py` va `validate_vault.py`) 100% muvaffaqiyatli o'tgandan so'ng `main` tarmog'iga birlashtiriladi.
- Barcha amallar `RULE[user_global]` talablariga mos ravishda avtomatik tarzda bajariladi.

---

## 🔗 Aloqador Bog'lanishlar (Related Links)

- Bosh Boshqaruv Markazi: `[[AI Sozlangan Miyyasi]]`
- Bosh Tizim Arxitektori: `[[Antigravity 1]]`
- Sandbox Sinovchi Agent: `[[Antigravity 2]]`
- Avtonom Kod Generatsiyasi Dvigateli: `[[Codex LLM Assistant]]`
- Majburiy Git Qoidalari: `[[30 Resources/Agent Skills/git-workflow|git-workflow]]`
