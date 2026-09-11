---
title: "🧪 Google Labs va AI Vositalarini Boshqarish Qo'llanmasi"
created: 2026-09-12
updated: 2026-09-12
status: active
type: operational-manual
tags:
  - google-labs
  - google-flow
  - imagen3
  - google-vids
  - notebooklm
language: "uz-UZ, en-US"
---

# 🧪 Google Labs va AI Vositalarini Boshqarish Qo'llanmasi

> *"Google'ning eng ilg'or generativ vositalarini bitta aqlli markazdan to'liq avtomat boshqarish."*

Ushbu yo'riqnoma foydalanuvchining murakkab ijodiy buyruqlarini (masalan, "Google Flow/Labs'ga kir, butun sayt uchun kerakli rasmlarni tayyorla, hikoya asosida video yarat") AI agentlari qanday qilib qadamma-qadam bajarishini ko'rsatadi.

---

## 🛠️ Google Labs Asboblari va Vazifalar Xaritasi

| Vosita Nomi | Asosiy Imkoniyati | Agent Harakati va Prompt Standarti |
| :--- | :--- | :--- |
| **Google Flow / Labs** | Multimodal generativ oqimlar va tajribaviy AI modellar | Promptlar ketma-ketligini kiritish, vizual stsenariylarni modellashtirish |
| **Google Vids** | AI video yaratish, slaydlar, montaj va diktor ovozi | Ssenariy matnini yuklash, sahna uslublarini tanlash, video eksport qilish |
| **Google Imagen 3** | Fotorealistik va badiiy yuqori aniqlikdagi rasmlar | Aniq yoritish, uslub, kamera burchagi va nisbat (`16:9`, `1:1`) ko'rsatilgan promptlar |
| **Google MusicFX** | Musiqiy fon, saundtrek va audio atmosferalar | Janr, BPM, kayfiyat va asboblar tavsifi bo'yicha audio generatsiya |
| **NotebookLM** | Hujjatlar tahlili, manbaali podkastlar va chuqur xulosalar | Katta matnlarni manba sifatida yuklash, savol-javob va audio-sharh generatsiya |

---

## 📋 Avtomat Boshqaruv Qadamlari (Execution Workflow)

1. **Kirish va Autentifikatsiya**: Foydalanuvchining faol sessiyasi orqali tegishli servis sahifasiga kirish.
2. **Topshiriqni Parchalash**: Foydalanuvchining umumiy g'oyasini (masalan, "klinika sayti uchun rasmlar") 5–10 ta aniq generativ promptlarga ajratish.
3. **Generatsiya va Tekshiruv**: Har bir promptni kiritish, natija yuklanishini kutish va sifatini tekshirish.
4. **Fayllarni Saqlash**: Olingan vizual va media aktivlarni loyihaning tegishli `assets/` papkasiga yuklab olish.

---

## 🧭 Navigatsiya
- 🧠 **[[AI Sozlangan Miyyasi|AI Sozlangan Miyyasi — Universal AI Second Brain]]**
- 📚 **[[30 Resources/30 Resources|30 Resources MOC]]**
