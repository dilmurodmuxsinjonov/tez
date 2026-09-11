---
title: "🐙 Git & GitHub Automation Workflow"
type: "Workflow / Git"
difficulty: "Medium"
status: "active"
tags:
  - skill
  - git
  - github
  - automation
---

# 🐙 Git & GitHub Avtomatlashtirilgan Ish Tartibi

Ushbu ko'nikma barcha loyihalarimizda Git va GitHub buyruqlarini eslatishlarsiz, avtomatik rejimda bajarilishini ta'minlaydi.

## 🤖 Men bajaradigan avtomatik amallar:
1. **`git init`**: Loyiha papkasida Git mavjud bo'lmasa, avtomatik ravishda initsializatsiya qilaman.
2. **`git pull`**: Ish boshlashdan oldin GitHub'dagi so'nggi yangilanishlarni mahalliy kompyuterga tortib olaman.
3. **`git status` va `git add .`**: Loyihadagi o'zgarishlarni va yangi fayllarni keshga (staging area) qo'shaman.
4. **`git commit -m "..."`**: Har bir o'zgarishni qisqa va aniq izoh bilan Git tarixiga yozib boraman.
5. **`git push`**: Ish yakunlangach, kodni avtomatik ravishda GitHub-ga yuklayman.
6. **Avtomatik Shoxlar (Branching)**: Muhim va katta o'zgarishlar kiritayotganda `main` shoxidan yangi shox (`feature/...` yoki `fix/...`) yaratib, ishni o'sha yerda davom ettiraman.
