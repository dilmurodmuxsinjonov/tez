---
title: "💻 Obsidian CLI Skill"
type: "Obsidian CLI"
difficulty: "Easy"
status: "pending-cli-activation"
tags:
  - skill
  - obsidian
  - cli
---

# 💻 Obsidian CLI

Obsidian CLI (`obsidian` buyrug'i) yordamida terminallar orqali Obsidian dasturini masofadan turib boshqarish va integratsiya qilish mumkin.

## 📌 Asosiy buyruqlar:
* Loyihada yangi qayd ochish:
  ```bash
  obsidian create name="Yangi Qayd" content="# Salom"
  ```
* Qaydni o'qish:
  ```bash
  obsidian read file="Yangi Qayd"
  ```
* Qayd oxiriga ma'lumot qo'shish:
  ```bash
  obsidian append file="Yangi Qayd" content="Yangi qator matni"
  ```
* Vault bo'yicha matnli qidiruv qilish:
  ```bash
  obsidian search query="qidirilayotgan matn"
  ```
* Plaginni dasturni o'chirmasdan qayta yuklash (dasturchilar uchun):
  ```bash
  obsidian plugin:reload id=plagin-id
  ```
* Xatoliklarni terminalda ko'rish:
  ```bash
  obsidian dev:errors
  ```
