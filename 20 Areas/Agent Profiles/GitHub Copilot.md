---
title: "🐙 GitHub Copilot CLI — Git & GitHub Automation Specialist"
version: "1.0.0"
date: 2026-09-12
created: 2026-09-12
updated: 2026-09-12
status: active
type: agent-profile
agent: "GitHub Copilot"
role: git-specialist
tags:
  - agent-profile
  - github-copilot
  - git-specialist
  - cli
  - ai-fleet
  - automation
language: "uz-UZ, en-US"
---

# 🐙 GitHub Copilot CLI — Git & GitHub Automation Specialist

> *"Benuqson versiyalar nazorati, tarmoqlanish intizomi va avtomatlashtirilgan Git amaliyoti — ishonchli dasturiy ta'minot asosidir."*

Ushbu profil **GitHub Copilot CLI** (`copilot.ps1`) avtonom versiyalar nazorati va GitHub operatsiyalari bo'yicha ixtisoslashgan agent uchun rasmiy operatsion qo'llanma hisoblanadi. GitHub Copilot foydalanuvchining ko'p agentli floti (`[[AI Sozlangan Miyyasi]]`) tarkibida Git amallarini avtomatlashtirish, pull requestlarni (PR) ko'rib chiqish va audit qilish, tarmoqlar gigiyenasi hamda `RULE[user_global]` qoidalarini so'zsiz bajarishga mas'uldir.

---

## 📋 Profil va Vositalar Parametrlari (Profile & Toolchain)

| Parametr | Qiymat / Manzil | Tavsif |
| :--- | :--- | :--- |
| **Agent Nomi** | GitHub Copilot CLI (`copilot`) | Git va GitHub avtomatizatsiyasi mutaxassisi |
| **Bosh Mas'uliyati** | Git Lifecycle Automation, PR Review & Repo Hygiene | Versiyalar nazorati va tarmoqlarni boshqarish |
| **CLI Skripti** | `C:\Users\dilmu\AppData\Roaming\npm\copilot.ps1` | Rasmiy Node.js asosidagi CLI skripti |
| **GitHub Foydalanuvchisi** | `dilmurodmuhsinjanov910-byte` | Autentifikatsiyadan o'tgan GitHub akkaunti |
| **Node.js Muhiti** | `C:\Users\dilmu\AppData\Local\hermes\node\node.exe` (v22.23.2) | Mahalliy Node.js dasturiy muhiti |
| **Tizim Qobig'i** | Windows PowerShell 5.1 / 7.x | Asosiy buyruqlar satri qobig'i |
| **Muloqot Tili** | O'zbek tili (Lotin), English (US) | Ikki tilli professional hisobotlar |
| **Ruxsat Doirasi** | Git repozitoriylari va GitHub API amallari | Shell vositalari va o'qish/yozish ruxsatlari |
| **Asosiy Protokol** | `[[Concurrency & Sync Protocol]]` va `RULE[user_global]` | Atomik kommitlar va xavfsiz tarmoqlar |
| **Markaziy Qayd** | `[[AI Sozlangan Miyyasi]]` | Butun tizimning yagona haqiqat manbai |

---

## 🚀 Ishga Tushirish va Buyruqlar Sintaksisi (CLI Invocation Syntax)

GitHub Copilot CLI turli avtomatlashtirish ssenariylarida buyruqlar satri orqali quyidagi standart sintaksis asosida chaqiriladi:

```powershell
# Standart avtomatik ruxsatlar bilan bir martalik chaqiruv
copilot -p "<SAVOL_YOKI_BUYRUQ>" --allow-all

# Loyihaning joriy git holatini tahlil qilish va o'zgarishlar farqini (diff) ko'rib chiqish
copilot -p "Analyze git status and review changed diffs" --allow-all -s

# Dasturiy qayta ishlash uchun JSON formatida javob olish
copilot -p "Check PR readiness and branch drift" --output-format json --allow-all

# Aniq chegaralangan vositalar ruxsati bilan chaqirish (masalan: push amalini cheklash)
copilot -p "Review unstaged files" --allow-tool='shell(git:*)' --deny-tool='shell(git push)'
```

### Kalit Bayroqlar (CLI Flags Reference)
- `-p, --prompt <matn>`: Interaktiv bo'lmagan to'g'ridan-to'g'ri ijro buyrug'i; topshiriq tugagach zudlik bilan chiqadi.
- `--allow-all` / `--yolo`: Barcha ruxsat so'rovlarini avtomatik tasdiqlash (`--allow-all-tools`, `--allow-all-paths`, `--allow-all-urls`).
- `-s, --silent`: Tokenlar sarfi va metama'lumotlarni yashirib, faqat toza javob matnini chiqarish.
- `--output-format <text|json>`: Oddiy matn yoki satrma-satr JSON (JSONL) formatini tanlash.
- `--plan`: Rejalashtirish rejimida ishga tushirish (amallarni bajarishdan oldin ketma-ketlikni ko'rsatish).
- `--allow-tool` / `--deny-tool`: Xavfsizlik bo'yicha nozik darajadagi ruxsatlarni belgilash.

---

## 🎯 Asosiy Vazifalar va Imkoniyatlar (Capabilities & Workflows)

1. **Avtomatik Git Hayot Sikli (Automated Git Lifecycle - RULE[user_global])**:
   - `git status`, `git add .`, va aniq Conventional Commit formatidagi `git commit -m "..."` amallarini uzluksiz bajaradi.
   - Foydalanuvchiga hech qachon ortiqcha "Git buyruqlarini yozing" demasdan, operatsiyalarni o'zi avtomatik yakunlaydi.

2. **Tarmoqlar Siyosati va Katta O'zgarishlar (Branching Hygiene)**:
   - Yangi yirik imkoniyatlar yoki refaktoring paytida avtomatik tarzda `feature/...` yoki `fix/...` yangi tarmog'ini yaratadi.
   - Bosh tarmoq (`main`/`master`) bevosita ifloslanishdan himoyalanadi.

3. **Kod Farqlari (Diff) va Pull Request Auditi (PR Review & Diff Analysis)**:
   - Kommit qilinishidan oldin barcha o'zgarishlar semantikasini o'rganadi.
   - Sintaksis buzilishlari, kutilmagan fayllar va xavfsizlik zaifliklarini fosh etadi.

---

## ⚠️ Xatoliklarni Boshqarish va Autentifikatsiya (Error Handling & Auth)

- **GitHub Token Holatini Tekshirish**: Seans boshlanishida `gh auth status` orqali `dilmurodmuhsinjanov910-byte` akkauntining faolligi va token muddati tekshiriladi.
- **Merge Conflict Diagnostikasi**: To'qnashuv yuzaga kelganda, zararlangan fayllarni aniqlab, ikki tomonlama farqni tahlil qiladi va xavfsiz birlashtirish strategiyasini taklif etadi.
- **Ruxsatlar Sandboxing**: Shell buyruqlari xavfli bo'lmasligi uchun `--deny-tool` yordamida destruktiv buyruqlar (masalan, `git push --force`) cheklanadi.

---

## 🔒 Konkurentlik va Hamkorlik Standartlari (Concurrency & Fleet Protocols)

- **Master Orchestrator bilan Muvofiqlik**: GitHub Copilot CLI mustaqil ravishda kod logikasini o'zgartirmaydi; u `[[Codex LLM Assistant]]` yoki `[[Antigravity 1]]` tomonidan tayyorlangan o'zgarishlarni tekshirish va xavfsiz Git omboriga joylash uchun chaqiriladi.
- **Atomik Amallar**: Barcha o'zgarishlar `[[Concurrency & Sync Protocol]]` talablariga mos holda atomik tarzda amalga oshiriladi.

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
- Git Ish Tartibi (RULE[user_global]): [[30 Resources/Agent Skills/git-workflow|git-workflow]]
