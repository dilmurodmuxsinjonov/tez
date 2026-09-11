---
title: "🎨 UI/UX va Zamonaviy Veb Standartlari (Modern Web Design Standards)"
created: 2026-09-12
updated: 2026-09-12
status: active
type: style-guide
tags:
  - ui-ux
  - tailwindcss
  - threejs
  - web-standards
language: "uz-UZ, en-US"
---

# 🎨 UI/UX va Zamonaviy Veb Standartlari (Modern Web Design Standards)

> *"Dizayn shunchaki qanday ko'rinishi emas, balki qanday ishlashidir."* — Steve Jobs

Ushbu standart foydalanuvchining barcha web va interfeys loyihalarida (MobCreatorWebApp, Orol Shahar, Doctor A Med Clinic) yuqori estetik did, zamonaviy CSS imkoniyatlari va 60fps render tezligini kafolatlaydi.

---

## 💎 Dizayn Tizimlari va Vizual Qoidalar

### 1. Material Clinical Precision (Doctor A Med Clinic)
- **Ranglar palitrasi:** Toza oq (`#FFFFFF`), tibbiy osmon ko'k (`#0284C7`), xotirjam neytral kulrang (`#F8FAFC`).
- **Tipografika:** Google Sans Flex, Inter — aniq o'qiluvchan va yuqori kontrastli.
- **Komponentlar:** Yumaloq burchaklar (`rounded-2xl`), mayin soyalar (`shadow-sm`, `shadow-md`), ortiqcha elementlarsiz toza bo'shliqlar (`whitespace`).

### 2. Three.js / React Three Fiber 3D Modeler (MobCreatorWebApp & Orol Shahar)
- **Render optimizatsiyasi:** 60fps barqarorlik, ortiqcha poligonlarsiz geometriyalar (`BoxGeometry`), to'g'ri pivot nuqtalari.
- **Yoritish (Lighting):** `ambientLight` (yumshoq umumiy nur) + `directionalLight` (soya hosil qiluvchi yo'naltirilgan nur).
- **Kamera nazorati:** `OrbitControls` orqali erkin aylantirish, yaqinlashtirish va markazlashtirish.

### 3. Zamonaviy CSS va Layout Qoidalari (Modern CSS 2026)
- **Container Queries & Grid:** Moslashuvchan kartalar va adaptiv boshqaruv panellari.
- **Glassmorphism / Backdrop Filter:** `backdrop-blur-md`, yarim shaffof orqa fonlar.
- **Animatsiyalar:** CSS GPU-accelerated transforms (`translate3d`, `scale`) — silliq o'tishlar (`transition: all 0.2s ease`).

---

## 🧭 Navigatsiya
- 🧠 **[[AI Sozlangan Miyyasi|AI Sozlangan Miyyasi — Universal AI Second Brain]]**
- 📚 **[[30 Resources/30 Resources|30 Resources MOC]]**
