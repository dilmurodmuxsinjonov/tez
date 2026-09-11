---
title: "🌐 Brauzer Avtomatizatsiyasi Qo'llanmasi (Browser Automation Manual)"
created: 2026-09-12
updated: 2026-09-12
status: active
type: operational-manual
tags:
  - browser-automation
  - puppeteer
  - devtools
  - web-interaction
language: "uz-UZ, en-US"
---

# 🌐 Brauzer Avtomatizatsiyasi Qo'llanmasi (Browser Automation Manual)

> *"Foydalanuvchi nomidan internetda murakkab ishlarni bajaruvchi avtonom brauzer agenti."*

Ushbu qo'llanma AI agentlari (Antigravity 1, Antigravity 2, Browser agent) uchun veb-sahifalarga kirish, elementlarni topish, shakllarni to'ldirish, tugmalarni bosish va skrinshot olish amallarini xatosiz bajarish qoidalarini belgilaydi.

---

## 🧭 Asosiy Operatsion Sikl (The Automation Loop)

Har qanday veb-saytda topshiriq bajarishda quyidagi 4 qadam ketma-ket bajariladi:

```
  [1. Navigate] ➡️ [2. Wait & Snapshot] ➡️ [3. Interact (Click/Fill)] ➡️ [4. Verify & Capture]
```

### 1. Sahifani Ochish (Navigation)
- Sahifaga kirish: `navigate_page` yoki `new_page`.
- To'liq yuklanishini kutish: tarmoq so'rovlari va asosiy DOM elementlari tayyor bo'lishi.

### 2. Holatni Tahlil Qilish (DOM Snapshot)
- `take_snapshot` orqali sahifadagi barcha interaktiv elementlarning unikal identifikatorlarini (`uid`) olish.
- Elementlar mavjudligini va ko'rinishini tasdiqlash.

### 3. Harakatlarni Amalga Oshirish (Interaction)
- Matn kiritish: `fill(uid, text)` orqali input maydonlarini to'ldirish.
- Bosish: `click(uid)` orqali tugmalar va havolalarni bosish.
- Aylantirish (Scroll): agar element pastda bo'lsa, uni ko'rinadigan sohaga olib chiqish.

### 4. Natijani Tasdiqlash va Rasmga Olish (Verification & Capture)
- Kutilgan o'zgarish sodir bo'lganini yangi snapshot orqali tekshirish.
- `take_screenshot` orqali natijani vizual tasdiqlash.
