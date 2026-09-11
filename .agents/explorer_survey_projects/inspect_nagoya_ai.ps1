Write-Host "=== NAGOYA / OSAKA CASTLE ==="
Get-ChildItem -Path "C:\Users\dilmu\.gemini\antigravity\scratch\NagoyaCastle" -Recurse | Select-Object FullName, Length | Format-List

Write-Host "=== THE_AI_PIPELINE ==="
Get-ChildItem -Path "C:\Users\dilmu\.gemini\antigravity\scratch\The_AI_Pipeline" -Recurse | Select-Object FullName, Length | Format-List

Write-Host "=== DESKTOP OROL / GAME ==="
Get-ChildItem -Path "C:\Users\dilmu\OneDrive\Desktop" -Filter "*orol*" | Select-Object FullName, Length
Get-ChildItem -Path "C:\Users\dilmu\OneDrive\Desktop" -Filter "*game*" | Select-Object FullName, Length
