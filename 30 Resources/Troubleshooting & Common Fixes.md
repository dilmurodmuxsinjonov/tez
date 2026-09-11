---
title: "🔧 Troubleshooting & Common Fixes"
type: resource
status: active
created: 2026-09-12
tags:
  - resource
  - troubleshooting
  - fixes
  - debugging
---

# 🔧 Troubleshooting & Common Fixes

> *Loyihalar davomida uchragan muammolar va ularning hal qilish yo'llari.*

---

## 🐛 PowerShell Escaping Muammolari

### Muammo
Inline Python/Node.js skriptlarda Obsidian wikilink pipe `|` belgisi va backtick `` ` `` PowerShell parser'ini buzadi.

### Yechim
Skriptlarni doim alohida faylga yozing, keyin `python <path>` orqali ishga tushiring:
```python
# ❌ Noto'g'ri — PowerShell'da inline
python -c "print('[[Target|Name]]')"

# ✅ To'g'ri — faylga yozib ishlatish
# scratch/my_script.py ga yozing, keyin:
python scratch/my_script.py
```

---

## 🧪 Test Xatoliklari

### `ModuleNotFoundError: check_visual_separation`
**Sabab**: `adversarial_m3_test.py` da import qilish esdan chiqarilgan.
**Yechim**: `from helpers import ..., check_visual_separation` qo'shing.

### `TC3.05 / TC3.06 Backlink Failure`
**Sabab**: `20 Areas/Agent Profiles/` yoki `10 Projects/` ichidagi yangi fayl `[[AI Sozlangan Miyyasi]]` havolasini o'z ichiga olmagan.
**Yechim**: Har bir yangi agent profil va loyiha fayliga `[[AI Sozlangan Miyyasi]]` wikilink'ini qo'shing.

### `UTF-8 BOM Detection`
**Sabab**: Windows'da ba'zi matn muharrirlari avtomatik BOM qo'shadi.
**Yechim**: Fayllarni `encoding='utf-8'` bilan yarating, `utf-8-sig` emas.

---

## 🔒 Agent Lock Muammolari

### Stale Lock
**Sabab**: Agent ishdan chiqqanda qulfni bo'shatmay qolishi.
**Yechim**: `.agents/locks/` katalogidagi 300+ soniya (5 daqiqa) davom etgan qulf fayllarini o'chirib tashlang.

```python
import os, time
locks_dir = r"D:\obsidian file\.agents\locks"
now = time.time()
for f in os.listdir(locks_dir):
    fp = os.path.join(locks_dir, f)
    if now - os.path.getmtime(fp) > 300:
        os.remove(fp)
        print(f"Stale lock removed: {f}")
```

---

## 🌐 Git Push Muammolari

### `fatal: No configured push destination`
**Yechim**: Remote qo'shing:
```bash
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin feature/universal-ai-second-brain
```

### `rejected: non-fast-forward`
**Yechim**: Avval pull qiling:
```bash
git pull --rebase origin main
git push
```

---

## 📊 Vault Validatsiya Xatoliklari

### Broken Wikilinks
**Tekshirish**: `python .agents/explorer_survey_projects/validate_vault.py`
**Odatiy sabablar**: Legacy fayllar (obsidian-markdown.md, Welcome.md) tashqi havolalarga ega — bular emas, faqat o'zimiz yaratgan fayllar muhim.

---

**Bosh Markaz:** [[AI Sozlangan Miyyasi]] | **Resources MOC:** [[30 Resources/30 Resources|30 Resources]]
