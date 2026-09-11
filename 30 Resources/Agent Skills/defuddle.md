---
title: "🌐 Defuddle Web Clipper Skill"
type: "Web Extraction"
difficulty: "Easy"
status: "installed"
tags:
  - skill
  - web-clip
  - markdown
---

# 🌐 Defuddle Web Clipper

Defuddle veb-sahifalardagi keraksiz reklamalar, menyu va navigatsiya tugmalarini tozalab, faqat asosiy matnni chiroyli Markdown formatida ajratib olish uchun ishlatiladi.

## 🛠️ O'rnatish
```bash
npm install -g defuddle
```

## 📋 Foydalanish
* Veb-havolani toza Markdown formatiga o'tkazish:
  ```bash
  defuddle parse <havola-url> --md
  ```
* Natijani to'g'ridan-to'g'ri faylga yozish:
  ```bash
  defuddle parse <havola-url> --md -o maqola.md
  ```
* Sahifaning faqat sarlavhasi yoki tavsifini ajratib olish:
  ```bash
  defuddle parse <havola-url> -p title
  defuddle parse <havola-url> -p description
  ```
