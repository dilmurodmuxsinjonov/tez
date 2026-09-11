---
title: "🧠 Obsidian Best Practices Skill"
type: "Obsidian Development"
difficulty: "Medium"
status: "installed"
tags:
  - skill
  - obsidian
  - development
---

# 🧠 Obsidian Best Practices

Ushbu ko'nikma Obsidian plaginlari va dizaynlarini ishlab chiqishda, xatolarni tuzatishda va interfeysni to'g'ri moslashtirishda qo'llaniladi.

## 🛡️ Xavfsiz Kodlash (Null Checking)
Obsidian ichki yoki hujjatsiz API'lari bilan ishlashda doimo xavfsiz o'tishlar (`?.`) qo'llanilishi shart:
```javascript
// To'g'ri:
const activeWorkspace = app.internalPlugins?.plugins?.workspaces?.instance?.activeWorkspace || "";
```

## 📝 Tahrirlagich & CodeMirror 6
Obsidian-ning "Live Preview" rejimi CodeMirror 6 yordamida ishlaydi. Editor ichidagi koordinatalar va havolalarni sichqoncha turgan joy bo'yicha to'g'ri olish:
1. `EditorView` (`cm`) obyektini olish: `app.workspace.getMostRecentLeaf()?.view?.editor?.cm`
2. Sichqoncha koordinatalarini joylashuv pozitsiyasiga o'tkazish: `cmView.posAtCoords({ x: event.clientX, y: event.clientY })`
3. Pozitsiya bo'yicha qator matnini ajratib olish.

## 🎨 UI va CSS Variables
Dizaynda ranglar, shriftlar va cursorlar uchun doim Obsidian-ning ichki o'zgaruvchilari ishlatilishi kerak:
- Matnlar: `var(--text-normal)`, `var(--text-muted)`
- Hover effekti: `var(--nav-item-color-hover)`
- UI elementlarida qimirlashlarning oldini olish uchun `display: none` o'rniga `visibility: hidden` ishlatiladi.

---

## 🧭 Navigatsiya
- 🧠 **[[AI Sozlangan Miyyasi|AI Sozlangan Miyyasi — Universal AI Second Brain]]**
- 📚 **[[30 Resources/30 Resources|30 Resources MOC]]**
