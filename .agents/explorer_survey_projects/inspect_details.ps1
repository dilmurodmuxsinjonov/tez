Write-Host "=== NagoyaCastle / Osaka Castle contents ==="
Get-ChildItem -Path "C:\Users\dilmu\.gemini\antigravity\scratch\NagoyaCastle" -Recurse | Select-Object FullName, Length, LastWriteTime | Format-Table -AutoSize

Write-Host "=== The_AI_Pipeline contents ==="
Get-ChildItem -Path "C:\Users\dilmu\.gemini\antigravity\scratch\The_AI_Pipeline" -Recurse | Select-Object FullName, Length, LastWriteTime | Format-Table -AutoSize

Write-Host "=== DOCTOR A contents ==="
Get-ChildItem -Path "C:\Users\dilmu\OneDrive\Desktop\DOCTOR A" -Recurse -Depth 2 | Select-Object FullName, Length, LastWriteTime | Format-Table -AutoSize

Write-Host "=== orol-shahar-qirollik-loyiha contents ==="
Get-ChildItem -Path "C:\Users\dilmu\OneDrive\Desktop\orol-shahar-qirollik-loyiha" | Select-Object FullName, Length, LastWriteTime | Format-Table -AutoSize
