function Inspect-Dir($path, $name) {
    Write-Host "=========================================="
    Write-Host "PROJECT: $name"
    Write-Host "PATH: $path"
    Write-Host "=========================================="
    if (Test-Path $path) {
        Write-Host "--- Top-level files/dirs ---"
        Get-ChildItem -Path $path | Select-Object Name, Length, LastWriteTime | Format-Table -AutoSize
        
        $pkg = Join-Path $path "package.json"
        if (Test-Path $pkg) {
            Write-Host "--- package.json ---"
            Get-Content $pkg -Raw
        }
        $readme = Join-Path $path "README.md"
        if (Test-Path $readme) {
            Write-Host "--- README.md (first 30 lines) ---"
            Get-Content $readme -TotalCount 30
        }
        $gitDir = Join-Path $path ".git"
        if (Test-Path $gitDir) {
            Write-Host "--- Git Status / Remote ---"
            Push-Location $path
            git status -s
            git remote -v
            git branch -a
            Pop-Location
        } else {
            Write-Host "--- No .git repository found ---"
        }
    } else {
        Write-Host "PATH NOT FOUND: $path"
    }
}

Inspect-Dir "C:\Users\dilmu\.gemini\antigravity\scratch\MobCreatorWebApp" "MobCreatorWebApp"
Inspect-Dir "C:\Users\dilmu\.gemini\antigravity\scratch\NagoyaCastle" "NagoyaCastle"
Inspect-Dir "C:\Users\dilmu\.gemini\antigravity\scratch\The_AI_Pipeline" "The_AI_Pipeline"
Inspect-Dir "C:\Users\dilmu\OneDrive\Desktop\orol-shahar-qirollik-loyiha" "Orol Shahar (orol-shahar-qirollik-loyiha)"
Inspect-Dir "C:\Users\dilmu\OneDrive\Desktop\game23v1" "Orol Shahar Game (game23v1)"
Inspect-Dir "C:\Users\dilmu\OneDrive\Desktop\DOCTOR A" "Medical Clinic (DOCTOR A)"
Inspect-Dir "C:\Users\dilmu\OneDrive\Desktop\DOCTOR A\doctor-a-med-clinic" "Medical Clinic (doctor-a-med-clinic)"
