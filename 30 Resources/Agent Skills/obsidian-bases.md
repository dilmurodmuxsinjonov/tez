---
title: "📊 Obsidian Bases Skill"
type: "Obsidian Database"
difficulty: "Medium"
status: "installed"
tags:
  - skill
  - obsidian
  - databases
---

# 📊 Obsidian Bases

Obsidian Bases (`.base` kengaytmali fayllar) yordamida qaydlarni ma'lumotlar bazasi ko'rinishida guruhlash, filtrlash va jadvallar hosil qilish mumkin.

## 📐 Baza tuzilishi (.base fayl namunasi):
```yaml
filters:
  and:
    - file.hasTag("task") # faqat #task tegi bor qaydlar
    - 'status != "done"'  # statusi bajarilmaganlar

formulas:
  days_left: 'if(due, (date(due) - today()).days, "")' # muddatgacha qolgan kunlar

properties:
  status:
    displayName: "Holati"
  formula.days_left:
    displayName: "Qolgan kunlar"

views:
  - type: table
    name: "Faol Vazifalar"
    order:
      - file.name
      - status
      - due
      - formula.days_left
```

## 🔌 Markdown fayl ichiga joylash:
Baza jadvallarini oddiy qayd ichida ko'rsatish:
`![[Vazifalar.base#Faol Vazifalar]]`

---

## 🧭 Navigatsiya
- 🧠 **[[AI Sozlangan Miyyasi|AI Sozlangan Miyyasi — Universal AI Second Brain]]**
- 📚 **[[30 Resources/30 Resources|30 Resources MOC]]**
