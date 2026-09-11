---
title: "✍️ Obsidian Markdown Skill"
type: "Obsidian Markdown"
difficulty: "Easy"
status: "installed"
tags:
  - skill
  - obsidian
  - formatting
---

# ✍️ Obsidian Markdown

Obsidian o'zining maxsus Markdown sintaksisiga (Obsidian Flavored Markdown) ega. Bu sintaksis yordamida qaydlarni o'zaro bog'lash va chiroyli dizayn qilish mumkin.

## 🔗 Wikilinks (Ichki bog'lanishlar)
* Oddiy havola: `[[Qayd Nomi]]`
* Boshqa matn bilan ko'rsatish: `[[Qayd Nomi|Ko'rsatiladigan Matn]]`
* Qayd ichidagi sarlavhaga havola: `[[Qayd Nomi#Sarlavha]]`

## 🗃️ Properties (YAML Frontmatter)
Har bir qaydning eng yuqori qismida meta-ma'lumotlarni saqlash mumkin:
```yaml
---
title: Qaydning nomi
tags:
  - muhim
  - loyiha
status: faol
---
```

## 🖼️ Embeds (Fayllarni matn ichiga joylash)
* Rasmni joylash (o'lchami bilan): `![[rasm.png|300]]`
* Boshqa qaydni to'liq ko'rsatib qo'yish: `![[Boshqa Qayd]]`

## ⚠️ Callouts (Eslatmalar bloklari)
Matnlarni chiroyli bloklarga olish:
```markdown
> [!NOTE]
> Bu oddiy eslatma bloki.

> [!WARNING]
> Bu ogohlantirish bloki.
```
Boshqa turlar: `[!tip]`, `[!important]`, `[!danger]`, `[!faq]`.
