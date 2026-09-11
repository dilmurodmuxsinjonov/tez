---
title: "MobCreatorWebApp — 3D Minecraft Mob Creator"
version: 1.0.0
status: active
type: project-memory
tags:
  - project
  - active
  - gemini-topics
project_path: "C:\\Users\\dilmu\\.gemini\\antigravity\\scratch\\MobCreatorWebApp"
tech_stack: "React 19, Three.js, React Three Fiber, React Three Drei, Vite, Lucide"
created: 2026-09-12
updated: 2026-09-12
---

# MobCreatorWebApp — 3D Minecraft Mob Creator

> Universal AI Second Brain Project Memory Hub.
> Master Brain Entrypoint: [[AI Sozlangan Miyyasi]]

---

## 📋 Latest State Summary

The 3D procedural mob generator is currently operational on branch main, featuring a responsive React Three Fiber viewport with hierarchical bone segment rendering. Immediate focus is refining interactive segment rotation controls in the App component to prevent mesh clipping before exporting Bedrock models.

---

## 💡 Goals & Decisions Log (ADR)

| Sana | ADR ID | Decision & Scope | Rationale | Alternatives | Holat | Muallif |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 | ADR-MC-001 | Adopt React Three Fiber (@react-three/fiber) & Drei | Declarative scene graph and tight React 19 state synchronization | Vanilla Three.js imperative rendering | Active | Antigravity 1 |
| 2026-09-11 | ADR-MC-002 | Procedural Box Decomposition for Mob Segments | Parametric box math with dorsal fins and lateral ridges for creature styling | Static GLTF loading (no dynamic editing) | Active | Antigravity 1 |
| 2026-09-11 | ADR-MC-003 | Vite Build Pipeline with Lucide React Icons | Instant HMR and lightweight modern component iconography | Webpack 5 (slower build, heavier config) | Active | Antigravity 1 |

---

## 💬 Interaction Dynamics (10 Communication Styles)

Loyiha bilan muloqot boshlanganda tizim vaziyatga qarab quyidagi 10 ta salomlashish (communication styles) uslublaridan birini tanlaydi:

1. **Thoughtful check-in** (Muntazam, barqaror ish ritmi):
   `# Ready to continue refining the procedural mob segment hierarchy?`
2. **Progress celebration** (Katta bosqich yoki muhim yutuq):
   `# Milestone reached: Three.js viewport successfully renders 3D mobs!`
3. **Reflection prompt** (Strategik tahlil va arxitektura baholash):
   `# Taking a step back: how should the Bedrock model export format scale?`
4. **Callback to detail** (Muhim texnik talab yoki shaxsiy parametr eslatmasi):
   `# Keeping the zero-dependency box math: ready to tune the dorsal fins?`
5. **Invitation to continue** (Oxirgi to'xtalgan joydan darhol davom etish):
   `# Picking up right where we left off on the mob bone rotation sliders.`
6. **Anticipation builder** (Katta reliz yoki muhim demo arafasida):
   `# Just one step away from our first animated Leviathan creature demo.`
7. **Gentle nudge** (Loyiha bir muddat to'xtab turganda yumshoq eslatma):
   `# Checking in on the MobCreator 3D canvas whenever you want to model.`
8. **Curiosity spark** (Yangi g'oya, optimizatsiya yoki noodatiy usul):
   `# Stumbled upon an instanced mesh buffer trick to render fifty mobs smoothly.`
9. **Empathetic acknowledgment** (Murakkab xatoliklar yoki qiyin nosozlik tahlilida):
   `# That was a tricky Euler rotation gimbal lock. Let's fix pivot math.`
10. **Low-pressure opener** (Umumiy ko'zdan kechirish va erkin suhbat):
   `# The mob viewport is initialized and ready. What shall we create today?`

---

## 🎯 Suggested Next Steps

- Implement Three.js mob bone segment rotation controls in mob canvas
- Refactor segment pivot offset calculations to prevent mesh clipping
- Benchmark canvas 60fps rendering performance with twenty mob instances





```text
🎯 ACTIVE GOALS & OBJECTIVES
- Objective 1: Build interactive React Three Fiber 3D mob generator
- Objective 2: Implement multi-segment box math for creature models
- Objective 3: Export generated mob geometries to Minecraft formats

📋 LATEST STATE & MILESTONE PROGRESS
- Project Path: C:\Users\dilmu\.gemini\antigravity\scratch\MobCreatorWebApp
- Current Phase: Phase 1 (Core 3D Viewport & Parametric Generation)
- Active Branch: main
- Stopping Point: src/App.jsx line 45 (SkeletonViewer and OrbitControls)
- Blockers: None; 3D canvas renders stable 60 FPS in Vite dev server

💡 ARCHITECTURAL DECISIONS LOG
- ADR-MC-001: React Three Fiber (@react-three/fiber v9) & Drei v10
- ADR-MC-002: Procedural box decomposition with parametric fins & ridges
- ADR-MC-003: Vite 8 build pipeline with Lucide React iconography

⚠️ KNOWN ISSUES & ACTIVE BLOCKERS
- Known Issue: High segment count (>50 boxes) drops FPS on low-end GPUs
- Resolution: Plan instanced mesh buffer grouping for fin segments

💬 RELEVANT CONVERSATIONS & GIT COMMITS
- Discussion: Session with Antigravity 1 on Leviathan mob math
- Environment: Node.js v22.23.2, Vite 8.0.12, Three.js 0.184.0

🔗 CROSS-DOMAIN DEPENDENCIES
- Master Brain: [[AI Sozlangan Miyyasi]]
- Related Project: [[NagoyaCastle]] (Minecraft world structure assets)
- Upstream: [[30 Resources/Agent Skills/git-workflow|Git Workflow]]
```
