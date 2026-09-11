---
title: "🔄 Development Workflow & CI/CD Standards"
type: area
status: active
created: 2026-09-12
tags:
  - area
  - development
  - ci-cd
  - workflow
  - standards
---

# 🔄 Development Workflow & CI/CD Standards

> *Barcha loyihalarda qo'llaniladigan ishlab chiqish jarayoni, sifat nazorati va doimiy integratsiya standartlari.*

---

## 📋 Git Branching Strategiyasi

| Strategiya | Qo'llanilishi |
| :--- | :--- |
| **`main` / `master`** | Barqaror, ishlab chiqarishga tayyor kod |
| **`feature/<nom>`** | Yangi xususiyatlar uchun alohida tarmoq |
| **`fix/<nom>`** | Xato tuzatish uchun alohida tarmoq |
| **`hotfix/<nom>`** | Shoshilinch tuzatishlar |
| **`release/<versiya>`** | Reliz tayyorlash (ixtiyoriy) |

> [!important] Avtomatik Branching Qoidasi
> `RULE[user_global]` bo'yicha barcha katta o'zgarishlar avtomatik ravishda `feature/...` yoki `fix/...` tarmoqlarida bajariladi. Agent foydalanuvchidan ruxsat so'ramasdan branchni o'zi ochadi.

---

## 🧪 Testing Pyramid (5-Tier)

| Tier | Nomi | Testlar Soni | Maqsadi |
| :--- | :--- | :--- | :--- |
| **Tier 1** | Feature Coverage | 29 | Asosiy xususiyatlar va talablar |
| **Tier 2** | Boundary Cases | 15 | Chegaraviy holatlar va edge case'lar |
| **Tier 3** | Cross-Feature | 7 | Xususiyatlar o'rtasidagi integratsiya |
| **Tier 4** | Real-World Workload | 5 | Haqiqiy ish yuklari simulyatsiyasi |
| **Tier 5** | Adversarial | 38 | Ziddiyatli va stress-testlar |

---

## 🔄 Commit Message Standarti (Conventional Commits)

```
<type>(<scope>): <description>

Masalan:
feat(m3): implement Gemini Topics Memory Architecture
fix(dashboard): repair broken wikilink in Quick Guides
docs(readme): update installation instructions
test(tier5): add adversarial vault hygiene tests
refactor(agent): simplify lock acquisition logic
```

**Ruxsat etilgan `type`'lar:** `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `perf`, `ci`, `style`

---

## 📊 Sifat Tekshiruvlari (Quality Gates)

1. **Statik Analiz**: Barcha fayllar UTF-8 (BOM'siz), YAML frontmatter to'g'ri
2. **Wikilink Validatsiya**: Vault ichidagi barcha wikilink'lar haqiqiy fayllarga ishora qilishi kerak
3. **Test Suite**: `python -m unittest discover -s tests/e2e` — 100% o'tishi shart
4. **Tier Runner**: `python .agents/test_track/run_e2e_tests.py` — barcha tierlar PASS
5. **Adversarial**: `python .agents/reviewer_m3/adversarial_m3_test.py` — nol xato

---

## 🛠️ Loyiha Yaratish Checklist'i

- [ ] Git repo'ni `git init` bilan boshlash yoki mavjud repo'ni `git clone` qilish
- [ ] `feature/<loyiha-nomi>` branch ochish
- [ ] `[[10 Projects/<Loyiha Nomi>]]` qaydini yaratish (Project Template'dan)
- [ ] `AI Sozlangan Miyyasi.md` dagi Faol Loyihalar jadvaliga qo'shish
- [ ] `10 Projects/10 Projects.md` MOC'ga havola qo'shish
- [ ] Boshlang'ich commit: `feat(<scope>): initialize project structure`

---

**Bosh Markaz:** [[AI Sozlangan Miyyasi]] | **Areas MOC:** [[20 Areas/20 Areas|20 Areas]]
