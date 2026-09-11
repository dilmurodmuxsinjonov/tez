import os
from pathlib import Path

paths = {
    "MobCreatorWebApp": Path(r"C:\Users\dilmu\.gemini\antigravity\scratch\MobCreatorWebApp"),
    "NagoyaCastle": Path(r"C:\Users\dilmu\.gemini\antigravity\scratch\NagoyaCastle"),
    "The_AI_Pipeline": Path(r"C:\Users\dilmu\.gemini\antigravity\scratch\The_AI_Pipeline"),
    "Orol Shahar": Path(r"C:\Users\dilmu\OneDrive\Desktop\game23v1"),
    "Doctor A": Path(r"C:\Users\dilmu\OneDrive\Desktop\DOCTOR A"),
}

print("=== PHYSICAL PROJECT REPOSITORY INTEGRITY AUDIT ===")
for name, p in paths.items():
    print(f"\nProject: {name} at {p}")
    if not p.exists():
        print("  [ERROR] Directory not found!")
        continue
    files = list(p.glob("*"))
    print(f"  Item count: {len(files)}")
    sub_sample = [f.name for f in files[:8]]
    print(f"  Sample items: {sub_sample}")

    # Specific checks per project
    if name == "MobCreatorWebApp":
        app_jsx = p / "src" / "App.jsx"
        pkg = p / "package.json"
        print(f"  src/App.jsx exists: {app_jsx.exists()}")
        print(f"  package.json exists: {pkg.exists()}")
    elif name == "NagoyaCastle":
        dl = p / "download_osaka.py"
        print(f"  download_osaka.py exists: {dl.exists()}")
    elif name == "The_AI_Pipeline":
        uz = p / "uzbek"
        en = p / "english"
        print(f"  uzbek/ exists: {uz.exists()}, english/ exists: {en.exists()}")
    elif name == "Orol Shahar":
        pkg = p / "package.json"
        prisma = p / "prisma" / "schema.prisma"
        print(f"  package.json exists: {pkg.exists()}, prisma/schema.prisma exists: {prisma.exists()}")
    elif name == "Doctor A":
        pkg = p / "package.json"
        booking = p / "components" / "BookingModal.tsx"
        print(f"  package.json exists: {pkg.exists()}, BookingModal.tsx exists: {booking.exists()}")
