---
title: "🤖 Yangi Agent Integratsiyasi Shabloni (New Agent Integration Template)"
type: template
template-type: agent-integration
status: active
created: {{date}}
aliases:
  - "New Agent Integration"
  - "New Agent Integration Template"
tags:
  - template
  - agent-integration
  - ai-fleet
  - orchestration
language: "uz-UZ, en-US"
---

# 🤖 Yangi Agent Integratsiyasi Shabloni (New Agent Integration Template)

> *Yangi AI agent CLI vositasi yoki modelini "AI Sozlangan Miyyasi" ko'p agentli ekotizimiga integratsiya qilish uchun rasmiy operatsion shablon.*

---

## 🧭 Asosiy Boshqaruv Havolalari (Core Navigation & Backlinks)

- 🧠 **[[AI Sozlangan Miyyasi|🧠 AI Sozlangan Miyyasi — Universal AI Second Brain]]** (Bosh Markaz)
- 🗺️ **[[30 Resources/AI Agent Ecosystem Map|🗺️ AI Agent Ecosystem Map]]**
- 🛡️ **[[20 Areas/20 Areas|🛡️ 20 Areas Asosiy Qaydnomasi]]**
- ⚖️ **[[30 Resources/Free LLM Models Registry|🌐 Free LLM Models Registry]]**

---

## 1. 📋 Agent Identifikatsiyasi va Texnik Parametrlari (Agent Identification)

| Parametr | Qiymat / Konfiguratsiya | Tavsif |
| :--- | :--- | :--- |
| **Agent Rasmiy Nomi** | `<Agent Nomi>` | Tizimdagi to'liq nomi |
| **CLI Buyrug'i / Prefiksi** | `<command>` | Terminalda chaqiriladigan CLI binar nomi |
| **Binar / Skript Manzili (Path)** | `<C:\Users\...>` | Diskdagi to'liq absolyut binar yoki skript manzili |
| **Runtime Muhiti** | Node.js / Python / Go / Rust / Native Binary | Ishga tushuvchi platforma |
| **Model / API Provayder** | OpenRouter / Groq / Google AI Studio / NIM / Mahalliy | Asosiy intellektual manba |
| **API Kalit Muhit O'zgaruvchisi** | `<ENV_VAR_NAME>` | Tizim muhit o'zgaruvchisi nomi |
| **So'rov Cheklovlari (Rate Limits)** | `<RPM / RPD / Tokens>` | Bepul yoki pullik limitlar |
| **Bosh Mas'uliyat Sohasi (Role)** | Orchestrator / Researcher / Coder / Reviewer / Swarm | Flotdagi ixtisoslashuvi |
| **Ruxsatlar Doirasi (Permissions)** | Read-Only / Repository Code / Full Sandbox | Vakolat va faylga yozish huquqi |
| **Bog'langan Profil Qaydi** | `[[20 Areas/Agent Profiles/<Agent Nomi>\|Profil]]` | Vault ichidagi doimiy profili |

---

## 2. 🚀 Ishga Tushirish va Chaqiruv Sintaksisi (CLI Invocation Syntax)

```powershell
# 1. Standart boshqaruvchisiz (headless) bir martalik chaqiruv
<command> -q "<SAVOL_YOKI_TOPSHIRIQ>" --auto

# 2. Xavfsiz, sokin (silent) chiqish rejimi (skriptlar uchun)
<command> --query "<PROMPT>" --silent

# 3. Modelni dinamik almashtirib chaqirish
<command> --model <provider/model-id> "<TASK>"

# 4. JSON formatida tuzilmaviy chiqish olish
<command> -p "<PROMPT>" --output-format json
```

### Kalit Bayroqlar (CLI Flags)
- `-q, --query <text>`: Asosiy topshiriq prompti.
- `--auto`: Xavfli bo'lmagan ruxsatlarni avtomatik tasdiqlash.
- `-m, --model <id>`: Modelni dinamik almashtirish.
- `-s, --silent`: Metadata va keraksiz loglarni yashirish.

---

## 3. 🤝 Codex Master Delegatsiya Qoidalari (/multt Coordination Protocol)

1. **Qachon ushbu agentga vazifa topshiriladi (Delegation Triggers)**:
   - `<Ushbu agentga qaysi turdagi muammolar yoki vazifalar topshirilishi kerakligini aniq belgilang>`
2. **Kiritish (Input) formati**:
   - `<Agentga uzatiladigan prompt tuzilmasi, fayl yo'llari va kontekst talablari>`
3. **Chiqish (Output) formati va sintez**:
   - `<Agent javobi qanday formatda olinadi (stdout, markdown, JSON) va Master Orchestrator uni qanday sintezlaydi>`
4. **Haqiqiylik nazorati (Integrity Check)**:
   - Faqat haqiqiy chaqiruv natijasi hisobotga kiritiladi; hech qachon soxta (dummy) chiqish qabul qilinmaydi.

---

## 4. 🔒 Konkurentlik va Xavfsizlik Standartlari (Concurrency & Security)

- **Fayllarni qulflash**: Ushbu agent fayllarni o'zgartirishdan oldin `[[Concurrency & Sync Protocol]]` bo'yicha `.agents/locks/<hash>.lock` qulfini tekshirishi va olishi shart.
- **Git Worktree**: Katta o'zgarishlar uchun asosiy ishchi daraxtdan alohida Git worktree yaratiladi.
- **Vault Himoyasi**: Agent Obsidian xotira fayllarini to'g'ridan-to'g'ri tahrirlamaydi; faqat loyiha kod bazalarida ishlaydi.
- **Maxfiylik**: Hech qanday tokenlar yoki API kalitlari loglarda aks etmaydi.
- **Git tartibi**: Har qanday o'zgarish `RULE[user_global]` bo'yicha avtomatik kommit qilinadi.

---

## 5. 🧪 Sinov va Tasdiqlash Buyruqlari (Smoke Test & Verification)

```powershell
# 1. Binar mavjudligi va versiyani tekshirish
Get-Command <command>
<command> --version

# 2. Oddiy test promptini bajarish
<command> -q "Ping test: Return OK" --auto

# 3. Test paketini yurgizish
python -m unittest discover -s tests/e2e
```

---

## 🔗 Aloqador Tizim Havolalari

- Bosh Haqiqat Manbai: [[AI Sozlangan Miyyasi]]
- Ekotizim Xaritasi: [[30 Resources/AI Agent Ecosystem Map|AI Agent Ecosystem Map]]
- Konkurentlik Protokoli: [[Concurrency & Sync Protocol]]
- Sohalar Xaritasi: [[20 Areas/20 Areas|20 Areas]]
- Shablonlar Boshqaruvi: [[50 Templates/Agent Profile Template|Agent Profile Template]]
