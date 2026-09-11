---
title: "🧪 Sifat va Sinov Standartlari (Quality & Testing Standards)"
created: 2026-09-12
updated: 2026-09-12
status: active
type: operational-manual
tags:
  - quality-assurance
  - e2e-testing
  - adversarial-testing
  - zero-defects
language: "uz-UZ, en-US"
---

# 🧪 Sifat va Sinov Standartlari (Quality & Testing Standards)

> *"Sifat — hech kim qaramayotganda ham ishni to'g'ri bajarishdir."* — Henry Ford

Ushbu standart barcha loyihalar va Obsidian vaultida nol xatolik (Zero Defects) tamoyilini amalga oshirish qoidalarini belgilaydi.

---

## 🏛️ 5 Bosqichli Sinov Piramidasi (5-Tier Testing Pyramid)

1. **Tier 1: Feature Coverage (Funksional Talablar)**: Asosiy fayllar, tuzilmalar va talablar mavjudligini tekshirish.
2. **Tier 2: Boundary & Corner Cases (Chegara Holatlari)**: Maxsus belgilar, uzunlik chegaralari (`60-85 chars`), bo'sh qatorlar.
3. **Tier 3: Pairwise Combinations (O'zaro Bog'liqlik)**: Fayllararo havolalar va MOC integratsiyasi.
4. **Tier 4: Real-World Workloads (Haqiqiy Ish Oqimlari)**: Agentlarning qulflash, saqlash va sinxronizatsiya sikllari.
5. **Tier 5: Adversarial Probing (Qat'iy Hujumkor Sinov)**: Buzilgan havolalar, BOM xatolari va sintaktik chetlanishlarni aniqlash.
