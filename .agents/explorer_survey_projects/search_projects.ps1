$targets = @("MobCreator", "Nagoya", "Osaka", "The_AI", "Pipeline", "Orol", "Medical", "Clinic")
$roots = @("D:\", "C:\Users\dilmu", "C:\Users\dilmu\.gemini\antigravity\scratch")

foreach ($r in $roots) {
    if (Test-Path $r) {
        Write-Host "=== Searching in $r ==="
        Get-ChildItem -Path $r -Recurse -Depth 4 -ErrorAction SilentlyContinue | Where-Object {
            $name = $_.Name
            foreach ($t in $targets) {
                if ($name -match $t) { return $true }
            }
            return $false
        } | Select-Object -Property FullName
    }
}
