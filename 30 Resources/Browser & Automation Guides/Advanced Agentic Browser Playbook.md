---
title: "🌐 Ilg'or Agentik Brauzer Playbooki (Advanced Browser Playbook)"
created: 2026-09-12
updated: 2026-09-12
status: active
type: operational-manual
tags:
  - browser-playbook
  - cdp
  - accessibility-tree
  - stagehand
  - crawl4ai
language: "uz-UZ, en-US"
---

# 🌐 Ilg'or Agentik Brauzer Playbooki (Advanced Browser Playbook)

> *"Eski XPath va CSS selektorlari eskirgan. Zamonaviy avtonom agent veb-sahifani inson ko'zi va Accessibility Tree orqali boshqaradi."*

Ushbu playbook murakkab veb-saytlar, SPA ilovalar va dinamik interfeyslarni brauzer agenti orqali to'liq avtomatlashtirishning ilg'or metodlarini belgilaydi.

---

## 🧭 Asosiy Boshqaruv Havolalari

- 🧠 **[[AI Sozlangan Miyyasi|🧠 AI Sozlangan Miyyasi — Universal AI Second Brain]]** (Bosh Markaz)
- 📚 **[[30 Resources/30 Resources|30 Resources MOC]]**
- 🌐 **[[30 Resources/Browser & Automation Guides/Browser Automation Operations Manual|Browser Operations Manual]]**

---

## 🔍 Accessibility Tree (a11y) & Semantic UIDs

Oddiy HTML kod juda katta va keraksiz teglar bilan to'la. Accessibility Tree esa faqat ekranda ko'rinadigan va bosish mumkin bo'lgan elementlarni saqlaydi:

```
[12] button "Sign in with Google"
[15] textbox "Email or phone"
[18] checkbox "Remember me"
[21] button "Next"
```

Agent to'g'ridan-to'g'ri `click(12)` yoki `fill(15, "user@example.com")` buyrug'ini bajaradi, bu esa xatolik ehtimolini 99% ga kamaytiradi.

---

## 🛡️ Self-Healing Selectors va Xavfsizlik

1. **Self-Healing Selectors**: Agar sayt dizayni o'zgarsa, agent semantik matn ("Sign in", "Submit", "Search") orqali elementni o'zi qayta topadi.
2. **CDP (Chrome DevTools Protocol)**: Tarmoq so'rovlarini tahlil qilish, javoblarni ushlash va konsol xatoliklarini monitoring qilish.
3. **Crawl4AI & Stagehand**: Veb-sahifalardan LLM uchun toza Markdown ajratib olish va form-filling amallarini xavfsiz bajarish.
