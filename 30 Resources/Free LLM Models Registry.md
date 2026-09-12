---
title: "🌐 Free LLM Models Registry — Bepul Modellar va API Provayderlar Katalogi"
version: "1.0.0"
created: 2026-09-12
updated: 2026-09-12
status: active
type: resource-guide
tags:
  - resource
  - llm-registry
  - free-models
  - openrouter
  - groq
  - google-ai-studio
  - nvidia-nim
  - opencode-zen
  - github-models
  - cloudflare
language: "uz-UZ, en-US"
---

# 🌐 Free LLM Models Registry — Bepul Modellar va API Provayderlar Katalogi

> *"Resurslarni to'g'ri taqsimlash — nol xarajat bilan cheksiz intellektual quvvatga ega bo'lish san'atidir."*

---

## 🧭 Asosiy Boshqaruv Havolalari (Core Navigation & Backlinks)

- 🧠 **[[AI Sozlangan Miyyasi|🧠 AI Sozlangan Miyyasi — Universal AI Second Brain]]** (Bosh Markaz)
- 📊 **[[Dashboard|Mening Ikkinchi Miyyam (Dashboard)]]**
- 🗺️ **[[30 Resources/AI Agent Ecosystem Map|🗺️ AI Agent Ecosystem Map]]**
- 📚 **[[30 Resources/30 Resources|📚 30 Resources Asosiy Qaydnomasi]]**
- 📖 **[[30 Resources/Codex Skills Encyclopedia|📚 Codex Skills Encyclopedia]]**
- ⚖️ **[[50 Templates/Model Evaluation Template|⚖️ Model Evaluation Template]]**

---

## 1. 📊 Asosiy Bepul Modellar Registri (Master Models Registry Matrix)

Ushbu registr foydalanuvchining ko'p agentli floti (**[[Nous Hermes]]**, **[[OpenCode CLI]]**, **[[Codex LLM Assistant]]**) foydalanishi mumkin bo'lgan 7 ta mustaqil provayder orqali taqdim etiladigan 22+ bepul LLM modellarini jamlaydi.

| # | Provayder | Model ID | Kontekst Oynasi | So'rov Cheklovi (Rate Limits) | Asosiy Kuchli Jihatlari va Sohasi | API Kalit Manzili |
| :- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **OpenRouter** | `openrouter/free` | Dinamik | 20 RPM / 200 RPD | Meta-router: eng yaxshi mavjud bepul modelga avtomatik yo'naltiruvchi endpoint | `https://openrouter.ai/keys` |
| 2 | **OpenRouter** | `meta-llama/llama-3.3-70b-instruct:free` | 128k | 20 RPM / 200 RPD | Kuchli umumiy mantiq, chuqur dasturlash, function calling va agentik ishlar | `https://openrouter.ai/keys` |
| 3 | **OpenRouter** | `deepseek/deepseek-r1:free` | 164k | 20 RPM / 200 RPD | Reinforcement Learning asosidagi chuqur mantiq, matematika va qiyin algoritmlar | `https://openrouter.ai/keys` |
| 4 | **OpenRouter** | `deepseek/deepseek-chat:free` (V3) | 64k | 20 RPM / 200 RPD | Yuqori tezlikdagi MoE arxitekturasi, tezkor umumiy sintez va qisqa javoblar | `https://openrouter.ai/keys` |
| 5 | **OpenRouter** | `google/gemini-2.0-flash-exp:free` | 1M+ | 20 RPM / 200 RPD | Ultra-katta kontekst, multimodal kirishlar (rasm/video/audio), tezkor kod auditi | `https://openrouter.ai/keys` |
| 6 | **OpenRouter** | `qwen/qwen-2.5-coder-32b-instruct:free` | 32k | 20 RPM / 200 RPD | Dasturlashga maxsus ixtisoslashgan model, AST tahlili va birlik testlar | `https://openrouter.ai/keys` |
| 7 | **OpenRouter** | `qwen/qwen-2.5-72b-instruct:free` | 128k | 20 RPM / 200 RPD | Umumiy mulohaza, ko'p tilli ustunlik (O'zbek, Rus, Ingliz), tizimli arxitektura | `https://openrouter.ai/keys` |
| 8 | **OpenRouter** | `nvidia/nemotron-3-ultra-550b-a55b:free` | 64k | 20 RPM / 200 RPD | 550B MoE giganti, korporativ tizimli dasturlash, C/C++/Rust va quyi darajali kod | `https://openrouter.ai/keys` |
| 9 | **OpenRouter** | `mistralai/mistral-small-24b-instruct-2501:free` | 32k | 20 RPM / 200 RPD | Samarali mantiqiy mulohaza, qisqa va aniq kod generatsiyasi, minimal kechikish | `https://openrouter.ai/keys` |
| 10 | **Groq** | `llama-3.1-8b-instant` | 8k | 30 RPM / 14.4k RPD | Groq LPU tezligi (500+ tok/s), real vaqtda vositalarni boshqarish va orkestratsiya | `https://console.groq.com/keys` |
| 11 | **Groq** | `gemma-2-9b-it` | 8k | 30 RPM / 14.4k RPD | Yuqori tezlikda buyruqlarga bo'ysunish, matnlarni saralash va tezkor javoblar | `https://console.groq.com/keys` |
| 12 | **Google AI Studio** | `gemini-2.0-flash` | 1,048,576 | 15 RPM / 1.5k RPD | 1 million token kontekst, multimodal tahlil, qat'iy JSON strukturasini ta'minlash | `https://aistudio.google.com/app/apikey` |
| 13 | **Google AI Studio** | `gemini-2.0-flash-lite` | 1,048,576 | 15 RPM / 1.5k RPD | Yuqori o'tkazuvchanlikka ega bepul model, real vaqtli oqimli (streaming) amallar | `https://aistudio.google.com/app/apikey` |
| 14 | **NVIDIA NIM** | `moonshotai/kimi-k3` | 128k | 40-60 RPM (Kreditlar) | Uzoq kontekstli ikki tilli tahlil, hujjatlar sintezi va agentlik oqimlari | `https://build.nvidia.com/settings/api-keys` |
| 15 | **NVIDIA NIM** | `deepseek-ai/deepseek-v4-flash` | 64k | 40-60 RPM (Kreditlar) | TensorRT-LLM tezlashuvi, ultra past kechikishdagi kod yozish va tahlil | `https://build.nvidia.com/settings/api-keys` |
| 16 | **NVIDIA NIM** | `minimax/minimax-m3` | 128k | 40-60 RPM (Kreditlar) | Yuqori parallellikdagi multimodal tushunish va murakkab mantiqiy mulohaza | `https://build.nvidia.com/settings/api-keys` |
| 17 | **OpenCode Zen** | `opencode/nemotron-3.5-lightning-free` | 64k | Jamoat Bepul | Ixtisoslashgan kod sintezi, testlar generatsiyasi va xatolarni tuzatish | `https://opencode.ai/auth` |
| 18 | **OpenCode Zen** | `opencode/mimo-v2.5-free` | 32k | Jamoat Bepul | Frontend mantiq, mobil freymvorklar, komponentlar va UI arxitekturasi | `https://opencode.ai/auth` |
| 19 | **OpenCode Zen** | `opencode/ling-3.0-flash-free` | 32k | Jamoat Bepul | Strukturali ma'lumotlar, sintaktik daraxtlar va qat'iy tekshiruvlar | `https://opencode.ai/auth` |
| 20 | **OpenCode Zen** | `opencode/muse-spark-1.3-free` | 32k | Jamoat Bepul | Ijodiy arxitektura g'oyalari, boshlang'ich boilerplate kodlari | `https://opencode.ai/auth` |
| 21 | **GitHub Models** | `gpt-4o` | 128k | 15 RPM / 150 RPD | OpenAI flagman modeli (Azure/GitHub orqali), nol narxli shaxsiy token | `https://github.com/settings/tokens` |
| 22 | **GitHub Models** | `o3-mini` | 128k | 15 RPM / 150 RPD | Ilg'or mantiqiy mushohada, olimpiada darajasidagi kod va qat'iy tekshiruv | `https://github.com/settings/tokens` |
| 23 | **Cloudflare Workers** | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | 128k | 10k Neyron/kun | Global edge (300+ shahar) serverless hisoblash, nol sovuq start | `https://dash.cloudflare.com/` |

---

## 2. 🔌 Provayderlar Bo'yicha Integratsiya va Sozlamalar

### 2.1 OpenRouter
- **Endpoint**: `https://openrouter.ai/api/v1`
- **Muhit O'zgaruvchisi**: `OPENROUTER_API_KEY`
- **Asosiy Agent**: `[[Nous Hermes]]` (`hermes.exe`) va `[[OpenCode CLI]]`.
- **Foydalanish Qoidasi**: Agar model ko'rsatilmasa, `openrouter/free` meta-routeri avtomatik tarzda eng kam yuklangan modelni tanlaydi. Agar maxsus mantiq talab qilinsa, `deepseek/deepseek-r1:free` yoki `meta-llama/llama-3.3-70b-instruct:free` chaqiriladi.

### 2.2 Groq LPU
- **Endpoint**: `https://api.groq.com/openai/v1`
- **Muhit O'zgaruvchisi**: `GROQ_API_KEY`
- **Asosiy Kuch**: 500+ token/sekund tezlik. Real vaqtli agent vositalarini boshqarish, tezkor testlarni o'tkazish va suhbat orqali rejalashtirishda tengsizdir.
- **Tavsiya etilgan Model**: `llama-3.1-8b-instant`.

### 2.3 Google AI Studio (Gemini API)
- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta`
- **Muhit O'zgaruvchisi**: `GEMINI_API_KEY`
- **Asosiy Kuch**: 1,048,576 token kontekst oynasi. Katta hajmdagi hujjatlar, butun boshli loyiha repozitoriylarini bir martada xotiraga yuklash va multimodal tahlil qilish uchun yagona bepul yechim.
- **Tavsiya etilgan Model**: `gemini-2.0-flash`.

### 2.4 NVIDIA NIM (Inference Microservices)
- **Endpoint**: `https://integrate.api.nvidia.com/v1`
- **Muhit O'zgaruvchisi**: `NVIDIA_API_KEY`
- **Asosiy Kuch**: NVIDIA TensorRT-LLM klasterlarida ishga tushirilgan Moonshot Kimi, DeepSeek V4 va MiniMax modellari. Dasturlash va uzoq kontekstli tahlilda juda yuqori aniqlik.

### 2.5 OpenCode Zen
- **Asosiy Agent**: `[[OpenCode CLI]]` (`opencode.ps1`).
- **Autentifikatsiya**: Bepul jamoat ruxsati (`opencode models`).
- **Asosiy Kuch**: Dasturchilar uchun maxsus o'rgatilgan Nemotron va MiMo modellari.

### 2.6 GitHub Models
- **Endpoint**: `https://models.inference.ai.azure.com`
- **Muhit O'zgaruvchisi**: `GITHUB_TOKEN`
- **Asosiy Kuch**: Shaxsiy GitHub hisobi orqali rasmiy GPT-4o va o3-mini modellaridan bepul foydalanish. Git commit auditi va murakkab algoritmlarni yechishda ideal.

### 2.7 Cloudflare Workers AI
- **Endpoint**: `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run`
- **Muhit O'zgaruvchisi**: `CLOUDFLARE_API_TOKEN`
- **Asosiy Kuch**: Edge darajasidagi serverless infratuzilma. Foydalanuvchiga eng yaqin serverdan tezkor javob.

---

## 3. 🎯 Modellarni Tanlash Qarorlar Matritsasi (Model Selection Heuristics)

Har qanday vazifa kelib tushganda, agentlar modelni quyidagi matritsa bo'yicha saralaydi:

```
[Vazifa Kirishi] 
      │
      ├─► Murakkab matematika, algoritm yoki RL mantiq? 
      │         └──► 1-tanlov: `deepseek-r1:free` | 2-tanlov: `o3-mini`
      │
      ├─► Katta kod bazasi sintezi, arxitektura va testlar?
      │         └──► 1-tanlov: `llama-3.3-70b-instruct:free` | 2-tanlov: `qwen-2.5-coder-32b`
      │
      ├─► Butun repozitoriy (100k+ token) tahlili yoki multimodal media?
      │         └──► 1-tanlov: `gemini-2.0-flash` (1M ctx)
      │
      ├─► Real vaqtli agent instrumentlari va tezkor orkestratsiya?
      │         └──► 1-tanlov: `llama-3.1-8b-instant` (Groq 500 tok/s)
      │
      └─► Nol xarajatli mahalliy AST refaktoring va birlik testlar?
                └──► 1-tanlov: `opencode/nemotron-3.5-lightning-free`
```

---

## 4. 🔄 Rate Limit va Fallback Protokoli (Rate Limit & Fallback Strategy)

Bepul darajalarda (Free Tier) uzluksiz ishlashni ta'minlash uchun agentlar quyidagi zaxira (fallback) zanjiriga amal qiladi:

1. **Boshlang'ich so'rov**: Belgilangan asosiy modelga (masalan, `deepseek-r1:free`) yuboriladi.
2. **429 (Too Many Requests) xatoligi olinganda**:
   - 1-zaxira: OpenRouter orqali `meta-llama/llama-3.3-70b-instruct:free` ga o'tiladi.
   - 2-zaxira: Groq orqali `llama-3.1-8b-instant` ga o'tiladi.
   - 3-zaxira: Google AI Studio orqali `gemini-2.0-flash` ga o'tiladi.
3. **Qayta urinish (Exponential Backoff)**: 2s, 4s, 8s interval bilan 3 martagacha qayta uriniladi.
4. **Holat jurnali**: Agar barcha bepul provayderlar limitga uchrasa, xatolik `[[AI Sozlangan Miyyasi]]` ga qayd etilib, master modelga (`gpt-6-astra`) topshiriladi.

---

## 5. ⚖️ Yangi Modellarni Baholash Qoidalari

Har qanday yangi e'lon qilingan bepul model ushbu registrga kiritilishidan oldin rasmiy **[[50 Templates/Model Evaluation Template|Model Evaluation Template]]** shabloni yordamida empirik sinovdan o'tkaziladi va baland ball to'plagan taqdirdagina asosiy ro'yxatga qo'shiladi.

---

## 🔗 Aloqador Tizim Havolalari

- Bosh Haqiqat Manbai: [[AI Sozlangan Miyyasi]]
- Ekotizim Xaritasi: [[30 Resources/AI Agent Ecosystem Map|AI Agent Ecosystem Map]]
- Nous Hermes Profili: [[Nous Hermes]]
- OpenCode CLI Profili: [[OpenCode CLI]]
- Model Baholash Shabloni: [[50 Templates/Model Evaluation Template|Model Evaluation Template]]
- Resurslar Xaritasi: [[30 Resources/30 Resources|30 Resources]]
