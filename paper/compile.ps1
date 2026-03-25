Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$tectonic = Join-Path $repoRoot "tectonic.exe"

if (-not (Test-Path $tectonic)) {
    throw "tectonic.exe was not found at $tectonic"
}

Push-Location $PSScriptRoot
try {
    & $tectonic -X compile --keep-logs --keep-intermediates main.tex
} finally {
    Pop-Location
}
