---
title: "🧠 AI Sozlangan Miyyasi — Universal AI Second Brain"
version: "1.0.0"
created: 2026-09-11
updated: 2026-09-11
status: active
type: master-brain
author: "Dilmurod Muhsinjanov & AI Fleet"
tags:
  - second-brain
  - master-entrypoint
  - gemini-topics
  - antigravity
  - codex
  - system-protocol
language: "uz-UZ, en-US"
---

# 🧠 AI Sozlangan Miyyasi — Universal AI Second Brain

> *"Miyangiz g'oyalarni saqlash uchun emas, ularni yaratish uchun xizmat qiladi."* — David Allen

Ushbu hujjat foydalanuvchi **Dilmurod Muhsinjanov**ning barcha sun'iy intellekt yordamchilari (**Antigravity 1**, **Antigravity 2**, **OpenAI Codex** va boshqa avtonom agentlar) uchun yagona haqiqat manbai (**Single Source of Truth — SSOT**) hisoblanadi. Mazkur vault (`D:\obsidian file`) ichidagi barcha bilimlar, faol loyihalar holati, tizim qoidalari va xotira tuzilmalari shu yerda markazlashgan holda boshqariladi.

---

## ⚡ Universal AI Startup Directive (Read-First Protocol)

> [!important] Har bir AI agent uchun majburiy boshlang'ich yo'riqnoma
> Vault ichida ish boshlayotgan har qanday AI agenti (Antigravity 1, Antigravity 2, Codex va boshqalar) har qanday vazifani bajarishdan oldin ushbu yo'riqnomaga qat'iy rioya qilishi shart:
> 
> 1. **Boshlang'ich kontekstni yuklash**: Har bir yangi sessiya boshida `AI Sozlangan Miyyasi.md` faylini o'qib chiqing. Foydalanuvchi shaxsiyati, muloqot tili, majburiy Git qoidalari va mahalliy dasturiy vositalar ro'yxatini to'liq qabul qiling.
> 2. **Konkurentlik va xavfsizlikni tekshirish**: Fayllarga yozishdan oldin `.agents/locks/` katalogini tekshiring. Agar o'zgartirilayotgan fayl boshqa agent tomonidan bloklangan bo'lsa, qulf bo'shashini kuting. Qulf muddati (TTL: 300 soniya) o'tgan bo'lsa, zaxira qoidasi bo'yicha tozalang.
> 3. **Loyiha xotirasini bog'lash**: Agar foydalanuvchi ma'lum bir loyiha ustida ishlashni so'rasa, `10 Projects/` ichidagi tegishli loyiha xotira qaydini yuklang va undagi oxirgi holat (`📋 Latest State Summary`) hamda me'moriy qarorlar jurnalini (`💡 Goals & Decisions Log`) o'rganing.
> 4. **Muloqot dinamikasini qo'llash**: Gemini Topics arxitekturasidagi 10 ta salomlashish uslubidan joriy holatga eng mosini tanlab, `# <Sarlavha>` formatida kontekstual salomlashish va 2–4 ta harakat fe'li bilan boshlanuvchi (~75 belgi) aniq takliflarni bering.
> 5. **Sessiya yakunida xotirani yangilash**: Ish tugagach, bajargan o'zgarishlaringizni tegishli loyiha qaydiga yozib qoldiring (Write-Back Protocol) va `RULE[user_global]` bo'yicha avtomatik Git kommitini amalga oshiring.

---

## 👤 Foydalanuvchi Profili va Shaxsiyati (User Identity & Persona)

| Parametr | Qiymat | Izoh |
| :--- | :--- | :--- |
| **Foydalanuvchi** | Dilmurod Muhsinjanov | Tizim egasi va bosh loyiha rahbari |
| **Email / Google Account** | `dilmurodmuhsinjanov910@gmail.com` | Antigravity 1 va asosiy servislar uchun asosiy hisob |
| **GitHub profili** | `dilmurodmuhsinjanov910-byte` | Barcha loyihalar va repozitoriylar egasi |
| **Muloqot tili** | O'zbek tili (Lotin alifbosida) | Tabiiy, do'stona, hurmatli, ravon va hamkorlik ruhiyati |
| **Texnik hujjatlar va kod** | English (US) | Xalqaro standartlar, toza kod, aniq tiplashtirish va testlar |
| **Falsafa va Tamoyil** | Getting Things Done & Second Brain | Haqiqiy va mustahkam yechimlar; feyk yoki soxta ko'rinishlarga yo'l qo'yilmaydi |

---

## ⚖️ Majburiy Global Git Qoidalari (Inviolable Git Workflow: RULE[user_global])

Barcha loyihalarda va ushbu vaultda ishlayotgan har bir AI agenti quyidagi qoidalarni istisnosiz va avtomatik ravishda bajarishi shart:

```markdown
<RULE[user_global]>
# Custom Agent Rules

## Git and GitHub Workflow
- **Default to Git**: Always use Git and GitHub when working on any project.
- **Automatic Lifecycle Operations**: Perform Git commands automatically during development without requiring the user to type them:
  - **Initialization**: Run `git init` automatically if the folder is not already a Git repository.
  - **Status & Tracking**: Run `git status` to inspect changed files, and `git add .` to stage them.
  - **Commits**: Make incremental commits with descriptive messages using `git commit -m "Descriptive commit message"`.
  - **Syncing**: Run `git pull` to fetch latest changes before editing, and `git push` to upload completed work to GitHub.
- **Automatic Branching for Major Changes**: When implementing significant features, bug fixes, refactoring, or any major changes, automatically create a new Git branch with a descriptive name (e.g., `feature/description` or `fix/description`) instead of working directly on `main` or `master`.
</RULE[user_global]>
```

> [!warning] AI Agentlar uchun qat'iy eslatma:
> Foydalanuvchiga "Git kommandalarini terminalda bajaring" deb yozish TAQIQLANADI. Barcha Git operatsiyalari (`git status`, `git add .`, `git commit -m "..."`, yangi tarmoq ochish) agent vositalari orqali avtomatik tarzda bajarilishi shart. Katta o'zgarishlar alohida `feature/...` yoki `fix/...` tarmoqlarida bajariladi.

---

## 🛠️ Mahalliy Dasturiy Vositalar (Local Software Toolchain Directory)

Tizimdagi barcha skriptlar, kompilyatsiya jarayonlari va sinovlar foydalanuvchi kompyuteridagi quyidagi tasdiqlangan dasturiy ta'minot vositalariga tayanadi:

| Asbob / Muhit | Versiya | O'rnatilgan Manzil (Path) | Asosiy Vazifasi va Qo'llanilishi |
| :--- | :--- | :--- | :--- |
| **Node.js** | `v22.23.2` | `C:\Users\dilmu\AppData\Local\hermes\node\node.exe` | Asosiy JavaScript/TypeScript runtime muhiti, Vite, Next.js, React 19 |
| **NPM** | `10.9.8` | `C:\Users\dilmu\AppData\Local\hermes\node\npm.cmd` | Paketlar menejeri (Corepack 0.34.6 yoqilgan) |
| **Python** | `3.12.10` | `C:\Users\dilmu\AppData\Local\Programs\Python\Python312\python.exe` | Skriptlar, AI quvurlari, data scraperlar, vault validatsiya skriptlari |
| **PowerShell** | `5.1.26100.9444 Desktop` | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` | Windows tizim buyruqlari, avtomatlashtirish, jarayonlarni boshqarish |
| **Git** | `2.54.0.windows.1` | `C:\Program Files\Git\cmd\git.exe` | Versiyalar nazorati, GitHub sinxronizatsiyasi, avtomatik lifecycle |
| **Obsidian** | Electron Desktop App | `D:\obsidian me\Obsidian.exe` | Ikkinchi miyya vizual interfeysi, bilimlar grafigi, Bases va Canvas |
| **Codex CLI / OpenCode** | `codex.exe` & `opencode.ps1` | `C:\Users\dilmu\AppData\Local\Programs\OpenAI\Codex\bin\codex.exe`<br>`C:\Users\dilmu\AppData\Roaming\npm\opencode.ps1` | Avtonom kod generatsiyasi, CLI refaktoring va avtomatik testlash |

---

## 🤖 AI Agentlar Floti Indeksi (AI Agent Fleet Index)

Vault va foydalanuvchi loyihalarida birgalikda ish olib boruvchi AI agentlar profillari va ularning mas'uliyat doirasi:

| Agent / Protokol | Asosiy Rol va Muhit | Ruxsatlar va Qoidalar | Havola |
| :--- | :--- | :--- | :--- |
| **Antigravity 1** | Bosh tizim arxitektori, foydalanuvchi bilan asosiy muloqotchi (Primary Google Account: `dilmurodmuhsinjanov910@gmail.com`) | Vault markaziy xotirasini boshqarish, loyihalar holatini yangilash, vazifalarni taqsimlash | [[Antigravity 1]] |
| **Antigravity 2** | Izolyatsiyalangan tadqiqotchi va sandbox sinovchi (Secondary Google Account, mustaqil brauzer profili) | Katta hisoblashlar, mustaqil testlar, tadqiqot qaydlari; asosiy xotiraga faqat tekshirilgan xulosalarni kiritish | [[Antigravity 2]] |
| **Codex LLM Assistant** | Avtonom kod generatsiyasi va refaktoring dvigateli (`codex.exe`, `opencode.ps1`) | Loyiha kod bazalarida to'g'ridan-to'g'ri ishlash, testlarni yurgizish, sintaksis va kontraktlarga qat'iy rioya qilish | [[Codex LLM Assistant]] |
| **Concurrency & Sync Protocol** | Ko'p agentli hamkorlikda fayllarni qulflash va to'qnashuvlarning oldini olish protokoli | `.agents/locks/<hash>.lock` qulflash tizimi, 300s TTL, ikki bosqichli atomik saqlash (temp-rename) | [[Concurrency & Sync Protocol]] |

---

## 🗂️ Faol Loyihalar Markazi (Active Projects Hub)

Foydalanuvchining ayni paytda faol bo'lgan 5 ta asosiy loyihasi va ularning Gemini Topics xotira markazlari:

| Loyiha Nomi | Soha va Texnologiyalar | Diskdagi Asosiy Manzil | Git Tarmoq | Mavzu Xotirasi (Topic Memory) |
| :--- | :--- | :--- | :--- | :--- |
| **MobCreatorWebApp** | Web-based 3D Mob Creator<br>React 19, Three.js, R3F, Vite, Lucide | `C:\Users\dilmu\.gemini\antigravity\scratch\MobCreatorWebApp` | `main` | [[MobCreatorWebApp]] |
| **NagoyaCastle** | Minecraft 3D Japanese Castle & NBT pipeline<br>Python 3, Anvil MCA, MediaFire Scraper | `C:\Users\dilmu\.gemini\antigravity\scratch\NagoyaCastle` | `main` | [[NagoyaCastle]] |
| **The_AI_Pipeline** | 30-Day AI Media Automation Course<br>Python, Markdown (60 ta UZ/EN video skriptlar) | `C:\Users\dilmu\.gemini\antigravity\scratch\The_AI_Pipeline` | `main` | [[The_AI_Pipeline]] |
| **Orol Shahar Qirollik** | Web3 / Economic Simulation Game Monorepo<br>Express 5, Prisma 7, PostgreSQL, React 19, R3F | `C:\Users\dilmu\OneDrive\Desktop\game23v1` | `feature/v1-p3` | [[Orol Shahar Qirollik]] |
| **Doctor A Med Clinic** | Healthcare Clinic Portal & Booking Platform<br>Next.js 16, Tailwind CSS v4, Prisma 5, SQLite | `C:\Users\dilmu\OneDrive\Desktop\DOCTOR A` | `feature/doctor-a-med-clinic-website` | [[Doctor A Med Clinic]] |
| **AI Story & Media Engine** | Multimodal Video & Audio Pipeline<br>Google Flow, Vids, Imagen 3, MusicFX, FFmpeg | `D:\obsidian file\10 Projects\AI Story & Media Engine` | `main` | [[AI Story & Media Engine]] |
| **Universal Multi-Agent Swarm** | Autonomous Multi-Agent Swarm Framework<br>Antigravity Swarm, Python 3.12, Node.js | `D:\obsidian file\10 Projects\Universal Multi-Agent Swarm Framework` | `main` | [[Universal Multi-Agent Swarm Framework]] |

---

## 🎨 Uslubiy Qo'llanmalar va Discovery Markazi (Style Guides & Discovery Hub)

Foydalanuvchi bilan muloqot qilish, loyiha talablarini chuqur aniqlashtirish va veb-dizayn standartlari:

| Qo'llanma Nomi | Asosiy Vazifasi va Qo'llanilishi | Havola |
| :--- | :--- | :--- |
| **Gemini Topics Style Guide** | 10 ta salomlashish uslubi, ~75 belgilik fe'lli takliflar va xotira bloklari | [[30 Resources/Style Guides/Gemini Topics Style Guide\|Gemini Topics Style Guide]] |
| **Project Discovery Questionnaire** | Yangi loyiha boshlashda talablarni 100% aniqlashtiruvchi 15 ta savol | [[30 Resources/Style Guides/Project Discovery Questionnaire\|Project Discovery Questionnaire]] |
| **UI/UX & Web Design Standards** | Tailwind v4, Three.js 3D, Material Clinical va zamonaviy veb standartlari | [[30 Resources/Style Guides/UI UX & Modern Web Design Standards\|UI UX & Web Standards]] |
| **Prompt Engineering & Compression** | Kontekstni tejash, ma'lumot zichligini oshirish va samarali promptlar | [[30 Resources/Style Guides/Prompt Engineering & Context Compression\|Prompt Engineering Guide]] |

---

## 🌐 Brauzer Avtomatizatsiyasi va Tashqi AI Vositalari (Browser & External AI Tools)

Foydalanuvchi nomidan internetda avtonom vazifalarni bajarish va multimodal kontent yaratish:

| Qo'llanma / Vosita | Vazifasi va Imkoniyatlari | Havola |
| :--- | :--- | :--- |
| **Autonomous Agent Architectures** | Kognitiv xotira, Model Context Protocol (MCP), ReAct/Plan-and-Solve va swarm arxitekturasi | [[Autonomous Agent Architectures\|Autonomous Agent Architectures]] |
| **Browser Automation Playbook** | Accessibility Tree, seanslar izolyatsiyasi, CDP diagnostikasi va self-healing | [[Browser Automation Playbook\|Browser Automation Playbook]] |
| **Multimodal Generation Workflows** | Google Flow, Imagen 3, Veo, Vids, MusicFX, Whisper audio sync va FFmpeg | [[Multimodal Generation Workflows\|Multimodal Generation Workflows]] |
| **Browser Automation Manual** | Brauzer orqali veb-sahifalarga kirish, elementlarni bosish va ma'lumot yig'ish | [[30 Resources/Browser & Automation Guides/Browser Automation Operations Manual\|Browser Automation Manual]] |
| **Google Labs & AI Tools Manual** | Google Flow, Vids, Imagen 3, MusicFX va NotebookLM boshqaruv yo'riqnomasi | [[30 Resources/Browser & Automation Guides/Google Labs & AI Tools Manual\|Google Labs & Flow Manual]] |
| **Story to Video Pipeline** | Hikoyadan ssenariy, rasmlar, animatsiyalar va yaxlit video montaj quvuri | [[30 Resources/Browser & Automation Guides/Multimodal Story to Video Pipeline\|Story to Video Pipeline]] |
| **Web Scraping Protocol** | Defuddle va DevTools orqali internetdan toza faktik ma'lumot to'plash | [[30 Resources/Browser & Automation Guides/Web Scraping & Research Protocol\|Web Scraping Protocol]] |
| **External AI Fleet Integration** | Gemini, Claude, OpenAI Codex va mahalliy modellarning o'zaro hamkorligi | [[30 Resources/External AI Integrations/External AI Fleet Integration\|External AI Fleet Integration]] |
| **OpenAI Codex & OpenCode** | `codex.exe` va `opencode.ps1` orqali terminalda avtonom kod yozish | [[30 Resources/External AI Integrations/OpenAI Codex & OpenCode Manual\|OpenAI Codex Manual]] |
| **LLM Handoff Format** | Turli AI modellari o'rtasida kontekstni yo'qotmasdan uzatish formati | [[30 Resources/External AI Integrations/LLM Interoperability & Handoff Format\|LLM Handoff Format]] |
| **Autonomous Decision Protocol** | Foydalanuvchi dam olayotganda agentlarning mustaqil qaror qabul qilish chegaralari | [[20 Areas/Agent Profiles/Autonomous Decision Protocols\|Autonomous Decision Protocols]] |
| **Agent Memory Architecture** | Ko'p qatlamli kognitiv xotira, Mem0 va Letta arxitekturasi | [[30 Resources/AI Research/Autonomous Agent Memory Architecture\|Agent Memory Architecture]] |
| **Next-Gen Generative Suite** | Google Flow, Veo, Imagen 3 va MusicFX prompt muhandisligi | [[30 Resources/AI Research/Google Labs & Next-Gen Generative Suite\|Next-Gen Generative Suite]] |
| **Advanced Browser Playbook** | Accessibility Tree va CDP orqali avtonom brauzer operatsiyalari | [[30 Resources/Browser & Automation Guides/Advanced Agentic Browser Playbook\|Advanced Browser Playbook]] |
| **Master Production Prompts** | Rasm, video va kod generatsiyasi uchun sinovdan o'tgan andozalar | [[30 Resources/Prompt Engineering/Master Production Prompts\|Master Production Prompts]] |

---

## 🗺️ Obsidian PARA & Skills Navigatsiya Xaritasi (PARA Structure & Skills Navigation)

Ushbu vault Tiago Fortening **PARA** (Projects, Areas, Resources, Archives) metodologiyasiga to'liq moslashtirilgan:

| Bo'lim / Hub | Tavsif | Asosiy Havola (MOC) |
| :--- | :--- | :--- |
| 📥 **00 Inbox** | Tezkor fikrlar, yangi g'oyalar va kunlik yozuvlar (Daily Notes) qabulxonasi | [[00 Inbox/00 Inbox\|00 Inbox]] • [[00 Inbox/00 Inbox MOC\|00 Inbox MOC]] |
| 🚀 **10 Projects** | Aniq maqsad, natija va muddatga ega bo'lgan barcha faol loyihalar | [[10 Projects/10 Projects\|10 Projects]] • [[10 Projects/10 Projects MOC\|10 Projects MOC]] |
| 🛡️ **20 Areas** | Doimiy mas'uliyat sohalari, standartlar va AI Agent profillari | [[20 Areas/20 Areas\|20 Areas]] • [[20 Areas/20 Areas MOC\|20 Areas MOC]] |
| 📚 **30 Resources** | Ma'lumotlar bazasi, qo'llanmalar, kitoblar va agent ko'nikmalari | [[30 Resources/30 Resources\|30 Resources]] • [[30 Resources/30 Resources MOC\|30 Resources MOC]] |
| 🗄️ **40 Archives** | Yakunlangan, muzlatilgan yoki tarixiy loyihalar arxivi | [[40 Archives/40 Archives\|40 Archives]] • [[40 Archives/40 Archives MOC\|40 Archives MOC]] |
| 🤖 **Agent Skills Hub** | Agentlarning rasmiy Obsidian va workflow ko'nikmalari boshqaruv paneli | [[30 Resources/Agent Skills/Skills Dashboard\|Skills Dashboard]] |
| 📅 **Daily Template** | Kunlik rejalar va sarhisoblar uchun rasmiy shablon | [[50 Templates/Daily Note Template\|Daily Note Template]] |
| 📋 **Project Template** | Yangi loyihalar ochish uchun standart shablon | [[50 Templates/Project Template\|Project Template]] |
| 📑 **Resource Template** | Yangi resurslar va o'rganilgan mavzular uchun shablon | [[50 Templates/Resource Template\|Resource Template]] |
| 🤖 **Agent Profile Template** | Yangi AI agent profili ochish uchun standart shablon | [[50 Templates/Agent Profile Template\|Agent Profile Template]] |
| 🛡️ **Area Template** | Yangi mas'uliyat sohasi yaratish uchun standart shablon | [[50 Templates/Area Template\|Area Template]] |

---

| **Development Workflow & CI/CD** | Git branching strategiyasi, testing pyramid va conventional commits standarti | [[20 Areas/Development Workflow & CI-CD Standards\|Dev Workflow & CI/CD]] |
| **Learning & Knowledge Base** | O'rganilgan texnologiyalar ro'yxati, kitoblar va amaliy darslar | [[30 Resources/Learning & Knowledge Base\|Learning & Knowledge Base]] |
| **Troubleshooting & Common Fixes** | PowerShell escaping, test xatolari va vault validatsiya yechimlari | [[30 Resources/Troubleshooting & Common Fixes\|Troubleshooting & Fixes]] |

---

## 🔄 Sessiya Boshlash va Yakunlash Protokollari (Session Lifecycle Protocols)

### 1. Ish Boshlash Protokoli (5-Step Startup Protocol)

Har qanday AI agenti yangi sessiyani boshlaganda quyidagi 5 bosqichni ketma-ketlikda bajaradi:

1. **Master Brain'ni o'qish**: Ushbu `AI Sozlangan Miyyasi.md` faylini o'qib, foydalanuvchi shaxsiyati, Git qoidalari va tizim parametrlarini xotirada tiklang.
2. **Blokirovkalarni tekshirish**: `.agents/locks/` katalogini tekshirib, ishlanadigan faylda faol qulf yo'qligiga ishonch hosil qiling.
3. **Loyiha xotirasini yuklash**: Foydalanuvchi murojaat qilgan loyihaning xotira qaydidan oxirgi holatni (`📋 Latest State Summary`) va qabul qilingan me'moriy qarorlar jurnalini (`💡 Goals & Decisions Log`) o'qing.
4. **Muloqot uslubini tanlash**: Gemini Topics tizimidagi 10 ta salomlashish uslubidan (Thoughtful check-in, Progress celebration, Reflection prompt, Callback to detail, Invitation to continue, Anticipation builder, Gentle nudge, Curiosity spark, Empathetic acknowledgment, Low-pressure opener) vaziyatga mos bittasini tanlab, `# <Sarlavha>` ko'rinishida salomlashing.
5. **Navbatdagi qadamlarni taklif qilish**: Loyiha holatiga tayangan holda 2 tadan 4 tagacha harakat fe'li bilan boshlanuvchi, ~75 belgi uzunlikdagi (60–85 belgi oralig'ida) aniq va amaliy takliflarni taqdim eting.

### 2. Yozib Qoldirish Protokoli (4-Step Write-Back Protocol)

Sessiya yakunlanganda yoki muhim natijaga erishilganda xotira yo'qolishining oldini olish uchun quyidagi 4 bosqich bajariladi:

1. **Fayl qulfini olish**: Maqsadli xotira fayliga mos SHA-256 xeshli qulf (`.agents/locks/<hash>.lock`) faylini yozing.
2. **Xotira blokini yangilash**:
   - `📋 LATEST STATE & MILESTONE PROGRESS` bo'limiga yangi erishilgan natija, faol Git tarmog'i, kommit xeshi va to'xtash nuqtasini kiriting.
   - Yangi arxitektura yoki kutubxona tanlovlari bo'lsa, ularni `💡 Goals & Decisions Log` jadvaliga yangi ADR sifatida qo'shing.
   - Yangi 2–4 ta taklif qilinadigan qadamlarni (~75 belgi, fe'l bilan boshlanuvchi) yangilang.
3. **Atomik saqlash va qulfni bo'shatish**: O'zgarishlarni avval vaqtinchalik faylga (`<file>.tmp.<agent_id>`) yozing, sintaksis va havolalarni tekshiring, so'ngra asosiy faylga atomik almashtirib, `.agents/locks/` dagi qulf faylini o'chiring.
4. **Avtomatik Git sinxronizatsiyasi**: `RULE[user_global]` talabiga binoan `git status`, `git add .` va aniq tavsifga ega `git commit -m "..."` buyruqlarini bajaring.

---

> [!tip] Tizim Integrity Qoidasi
> Hech qachon soxta (dummy/facade) ma'lumotlar yoki yuzaki hisobotlar yozmang. Barcha qaydlar diskdagi haqiqiy fayllar, tasdiqlangan kodlar va real Git holatiga asoslanishi shart.
