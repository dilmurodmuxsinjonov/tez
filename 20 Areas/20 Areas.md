---
title: "🛡️ 20 Areas — Map of Content (MOC)"
created: 2026-09-12
updated: 2026-09-12
status: active
type: moc
tags:
  - areas
  - para
  - moc
  - agent-profiles
language: "uz-UZ, en-US"
---

# 🛡️ 20 Areas — Map of Content (MOC)

> *"Vaqt chegarasiga ega bo'lmagan, doimiy e'tibor va yuqori standartlarni talab qiluvchi mas'uliyat sohalari."*

Ushbu MOC foydalanuvchining shaxsiy va texnologik mas'uliyat sohalarini, xususan **Universal AI Agentlar Floti** profillari, ularning operatsion vakolatlari va o'zaro to'qnashuvsiz hamkorlik protokollarini birlashtiradi.

---

## 🧭 Asosiy Boshqaruv Havolalari

- 🧠 **[[AI Sozlangan Miyyasi|🧠 AI Sozlangan Miyyasi — Universal AI Second Brain]]** (Bosh Markaz)
- 📊 **[[Dashboard|Mening Ikkinchi Miyyam (Dashboard)]]**
- ⚖️ **[[30 Resources/Agent Skills/git-workflow|Git Ish Tartibi (RULE[user_global])]]**

---

## 🤖 AI Agentlar Floti Profillari (Agent Fleet Index)

| Agent / Protokol | Mas'uliyat Doirasi va Muhiti | Ruxsatlar va Qoidalar | Havola |
| :--- | :--- | :--- | :--- |
| **Antigravity 1** | Bosh tizim arxitektori, foydalanuvchi bilan asosiy muloqotchi (Primary Google Account) | Vault markaziy xotirasini boshqarish, loyihalar holatini yangilash, vazifalarni taqsimlash | [[Antigravity 1]] |
| **Antigravity 2** | Izolyatsiyalangan tadqiqotchi va sandbox sinovchi (Secondary Google Account) | Katta hisoblashlar, mustaqil testlar, tadqiqot qaydlari; asosiy xotiraga faqat tekshirilgan xulosalarni kiritish | [[Antigravity 2]] |
| **Codex LLM Assistant** | Avtonom kod generatsiyasi va refaktoring dvigateli (`codex.exe`, `opencode.ps1`) | Loyiha kod bazalarida to'g'ridan-to'g'ri ishlash, testlarni yurgizish, sintaksis va kontraktlarga qat'iy rioya qilish | [[Codex LLM Assistant]] |
| **Concurrency & Sync Protocol** | Ko'p agentli hamkorlikda fayllarni qulflash va to'qnashuvlarning oldini olish protokoli | `.agents/locks/<hash>.lock` qulflash tizimi, 300s TTL, ikki bosqichli atomik saqlash (temp-rename) | [[Concurrency & Sync Protocol]] |

---

## 📐 Muhandislik va Sifat Sohalari (Engineering Excellence)

- **Me'moriy standartlar**: Toza kod, tiplashtirish, xavfsizlik va mustahkam modulli tuzilma.
- **Versiyalar nazorati**: Har bir faoliyat `RULE[user_global]` asosida avtomatik Git boshqaruvi bilan himoyalangan.
- **Xotira yaxlitligi**: Barcha o'zgarishlar atomik yangilanadi, feyk yoki soxta ma'lumotlarga yo'l qo'yilmaydi.
