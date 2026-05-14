param(
    [string]$Root = "C:\Creations",
    [string]$ArtifactName = "loop_test_artifact.json",
    [string]$PacketName = "loop_packet.json",
    [string]$OriginName = "loop_origin.origin.json",
    [string]$Lineage = ".N/example-root"
)

$ErrorActionPreference = "Stop"

$LoopRepo = Join-Path $Root "project-512d"
$SunTanRepo = Join-Path $Root "Sun_Tan"
$NeonRepo = Join-Path $Root ".Neon"
$NeonVault = Join-Path $NeonRepo ".neon-vault"

$ArtifactPath = Join-Path $LoopRepo $ArtifactName
$PacketPath = Join-Path $LoopRepo $PacketName
$OriginPath = Join-Path $LoopRepo $OriginName

function Write-Step($Message) {
    Write-Host ""
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function Require-Path($Path, $Label) {
    if (-not (Test-Path $Path)) {
        throw "$Label not found: $Path"
    }
}

Write-Step "Checking repositories"
Require-Path $LoopRepo "Loop / project-512d repo"
Require-Path $SunTanRepo "Sun_Tan repo"
Require-Path $NeonRepo ".Neon repo"

Write-Step "Installing Sun_Tan locally"
Push-Location $SunTanRepo
python -m pip install -e .
python -m pytest -q
Pop-Location

Write-Step "Installing .Neon locally"
Push-Location $NeonRepo
python -m pip install -e .
Pop-Location

Write-Step "Creating Loop artifact"
$ArtifactJson = @{
    artifact_type = "manual_loop_test"
    source_system = "project-512d"
    task = "one_command_product_spine_test"
    summary = "Manual Loop artifact exported into Sun_Tan and imported by .Neon."
    metrics = @{
        retention_gate = "pass"
        quality_gate = "pass"
        forgetting_delta = 0.0
    }
} | ConvertTo-Json -Depth 10

Set-Content -Path $ArtifactPath -Value $ArtifactJson -Encoding UTF8
Write-Host "artifact: $ArtifactPath"

Write-Step "Exporting Loop artifact to Sun_Tan packet"
Push-Location $LoopRepo
python suntan_export.py $ArtifactName --lineage $Lineage --out $PacketName
Pop-Location
Require-Path $PacketPath "Sun_Tan packet"

Write-Step "Verifying Sun_Tan packet"
Push-Location $SunTanRepo
$VerifyOutput = suntan verify $PacketPath --artifact $ArtifactPath
Write-Host $VerifyOutput
if ($VerifyOutput -notmatch "valid") {
    throw "Sun_Tan packet verification failed"
}
Pop-Location

Write-Step "Exporting .Neon origin claim"
Push-Location $SunTanRepo
suntan export-neon $PacketPath --artifact $ArtifactPath --out $OriginPath
Pop-Location
Require-Path $OriginPath ".Neon origin claim"

Write-Step "Initializing .Neon vault"
Push-Location $NeonRepo
neon init
Pop-Location

Write-Step "Importing Sun_Tan claim into .Neon"
Push-Location $NeonRepo
neon import-suntan $OriginPath
Pop-Location

Write-Step "Checking .Neon import receipts"
$ReceiptDir = Join-Path $NeonVault "imports\suntan"
Require-Path $ReceiptDir ".Neon Sun_Tan import receipt directory"
Get-ChildItem $ReceiptDir

Write-Host ""
Write-Host "SUCCESS: Loop -> Sun_Tan -> .Neon product spine completed." -ForegroundColor Green
Write-Host "artifact: $ArtifactPath"
Write-Host "packet:   $PacketPath"
Write-Host "claim:    $OriginPath"
Write-Host "receipts: $ReceiptDir"
