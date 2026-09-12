---
title: "🛡️ Xavfsizlik Auditi Shabloni (Security Audit Template)"
type: template
template-type: security-audit
status: active
created: {{date}}
aliases:
  - "Security Audit"
  - "Security Audit Template"
tags:
  - template
  - security-audit
  - white-hat
  - cybersecurity
  - ethical-hacking
language: "uz-UZ, en-US"
---

# 🛡️ Xavfsizlik Auditi Shabloni (Security Audit Template)

> *Loyiha kod bazalari, muhit konfiguratsiyalari va AI agent ekotizimlari uchun White-Hat xavfsizlik auditi, tahdidlarni modellashtirish va zaifliklarni bartaraf etish shabloni.*

---

## 🧭 Asosiy Boshqaruv Havolalari (Core Navigation & Backlinks)

- 🧠 **[[AI Sozlangan Miyyasi|🧠 AI Sozlangan Miyyasi — Universal AI Second Brain]]** (Bosh Markaz)
- 📖 **[[30 Resources/Codex Skills Encyclopedia|📚 Codex Skills Encyclopedia]]**
- 🛡️ **[[20 Areas/Quality & Testing Standards|🛡️ Quality & Testing Standards]]**
- 🛡️ **[[20 Areas/20 Areas|🛡️ 20 Areas Asosiy Qaydnomasi]]**

---

## 1. 📋 Audit Doirasi va Metama'lumotlar (Audit Scope & Metadata)

| Parametr | Qiymat / Tavsif | Izoh |
| :--- | :--- | :--- |
| **Loyiha / Repozitoriy** | `<Loyiha Nomi>` | Audit qilinayotgan loyiha |
| **Audit Sanasi** | {{date}} | Audit o'tkazilgan vaqt |
| **Auditor Agent** | Codex (`oq_haker_muhiti` & `xavfsizlik_qoidalari`) | Mas'ul auditor |
| **Tekshirilgan Yo'llar (Paths)** | `src/`, `tests/`, `.env.example`, `.agents/` | Qamrab olingan fayllar doirasi |
| **Tizim Qoidalari Nazorati** | `RULE[user_global]`, `[[Concurrency & Sync Protocol]]` | Majburiy standartlar |
| **Umumiy Xavfsizlik Holati** | 🟢 Xavfsiz / 🟡 Ogohlantirishlar / 🔴 Kritik Zaiflik | Yakuniy umumiy baho |

---

## 2. 🛡️ White-Hat Xavfsizlik Nazorat Ro'yxati (Zero-Trust Security Checklist)

`oq_haker_muhiti`, `oq_haker_vositalari` va `xavfsizlik_qoidalari` maxsus ko'nikmalari talablariga muvofiq quyidagi 5 ta muhim soha tekshiriladi:

### 2.1 Maxfiy Ma'lumotlar va Kalitlar Himoyasi (Credential & Secret Leakage)
- [ ] Git repozitoriyasiga `.env`, API kalitlari, tokenlar yoki shaxsiy sertifikatlar kommit qilinmagan.
- [ ] `.gitignore` faylida barcha maxfiy kataloglar va fayllar to'g'ri ko'rsatilgan.
- [ ] Kod ichida (hardcoded) parollar, API kalitlari yoki sessiya ma'lumotlari mavjud emas.
- [ ] Maxfiy o'zgaruvchilar faqat tizim muhitidan (`process.env` yoki `os.environ`) xavfsiz o'qiladi.

### 2.2 Ruxsatlar va Qat'iy Chegaralar (Permissions & Sandbox Barriers)
- [ ] Agent vositalari faqat ruxsat etilgan ishchi kataloglarda amalga oshiriladi.
- [ ] Tizim buyruqlari (shell) va fayl yozish amallari eng kam imtiyoz (Least Privilege) tamoyiliga bo'ysunadi.
- [ ] Tashqi CLI vositalari faqat belgilangan parametrlar bilan xavfsiz subshell orqali yurgiziladi.

### 2.3 Prompt Injection va Jailbreak Himoyasi (Prompt Defense)
- [ ] Tashqi manbalardan (veb-sahifalar, foydalanuvchi xabarlari) olingan kiritmalar xom holatda promptga kiritilmaydi (sanitization o'tkazilgan).
- [ ] Ko'rsatmalarni chetlab o'tishga (jailbreak) qarshi tizimli ko'rsatmalar mustahkamlangan.

### 2.4 Fayllarni Qulflash va Poyga Holatlari (Concurrency & Race Condition Checks)
- [ ] Fayllarga yozishdan oldin `[[Concurrency & Sync Protocol]]` bo'yicha `.agents/locks/` tekshiriladi.
- [ ] Qulflar muddati (300s TTL) va ikki bosqichli atomik saqlash (temp-rename) qoidasiga amal qilinadi.
- [ ] Bir vaqtning o'zida bir nechta agentning bitta faylni buzib qo'yish (race condition) xavfi yo'q.

### 2.5 Kod va Infratuzilma Butunligi (Code & Integrity Audit)
- [ ] SQL/NoSQL inyeksiyalari, XSS va CSRF zaifliklariga qarshi tekshiruvdan o'tkazilgan.
- [ ] Bog'liqliklar (dependencies) auditi o'tkazilgan (`npm audit` yoki `pip-audit`).
- [ ] `loyiha_infratuzilmasi_qoidalari` bo'yicha "Project Brain" 5 ta jild tuzilmasi mavjud.

---

## 3. 🔍 Zaifliklar Matritsasi (Vulnerability Matrix)

| ID | Xavf Darajasi | Zaiflik Turi | Komponent / Fayl | Tavsif va Ekspluatatsiya Senariysi | Bartaraf Holati |
| :--- | :---: | :--- | :--- | :--- | :---: |
| **SEC-01** | Kritik (P0) | Masalan: Secret Exposure | `.env` / `config.ts` | API kaliti ochiq matnda qolib ketgan | ⏳ / ✅ |
| **SEC-02** | Yuqori (P1) | Masalan: Race Condition | `storage/cache.json` | Fayl qulflanmasdan yozilmoqda | ⏳ / ✅ |
| **SEC-03** | O'rta (P2) | Masalan: Missing Validation | `api/routes.py` | Kiritilgan parametrlar tekshirilmagan | ⏳ / ✅ |
| **SEC-04** | Quyi (P3) | Masalan: Verbose Error | `server.js` | Ichki stack trace foydalanuvchiga ko'rinmoqda | ⏳ / ✅ |

---

## 4. 🛠️ White-Hat Pen-Test va Sinov Skriptlari (Verification Scripts)

```powershell
# 1. Repozitoriyda maxfiy kalitlarni qidirish (Secret scanning)
git log -p -S "AIzaSy" --all
git status

# 2. Xavfsizlik va E2E testlarini yurgizish
python -m unittest discover -s tests/e2e
python run_e2e_tests.py

# 3. Zaif bog'liqliklarni tekshirish
npm audit
```

---

## 5. 📋 Bartaraf Etish Rejasi va Himoya Qatlamlari (Hardening Actions & Defense)

`oq_haker_vositalari` talabiga ko'ra, aniqlangan har bir zaiflik uchun majburiy mudofaa kodi kiritiladi:

1. [ ] **Zaiflik 1 bartaraf etilishi**: Kod tuzatildi va commit qilindi.
2. [ ] **Zaiflik 2 bartaraf etilishi**: Fayl qulflash protokoli kuchaytirildi.
3. [ ] **Regressiya testi**: Yangi himoya kodi testlar orqali tasdiqlandi.

---

## 🔗 Aloqador Tizim Havolalari

- Bosh Haqiqat Manbai: [[AI Sozlangan Miyyasi]]
- Codex Ko'nikmalar Qomusi: [[30 Resources/Codex Skills Encyclopedia|Codex Skills Encyclopedia]]
- Konkurentlik Protokoli: [[Concurrency & Sync Protocol]]
- Sifat va Sinov Standartlari: [[20 Areas/Quality & Testing Standards|Quality & Testing Standards]]
- Sohalar Xaritasi: [[20 Areas/20 Areas|20 Areas]]
