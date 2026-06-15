param(
    [Parameter(Mandatory = $true)]
    [string]$Version,

    [string]$OutputDir = "dist"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$PyTag = "py38"

New-Item -ItemType Directory -Force -Path (Join-Path $Root $OutputDir) | Out-Null

function New-PlatformZip {
    param([string]$Name, [string]$LibPath)

    if (-not (Test-Path (Join-Path $Root $LibPath))) {
        Write-Warning "Skipping missing path: $LibPath"
        return
    }

    $staging = Join-Path ([System.IO.Path]::GetTempPath()) ("xcore-py-pack-" + [guid]::NewGuid().ToString())
    New-Item -ItemType Directory -Force -Path $staging | Out-Null

    try {
        $parent = Split-Path $LibPath -Parent
        New-Item -ItemType Directory -Force -Path (Join-Path $staging $parent) | Out-Null
        Copy-Item -Path (Join-Path $Root $LibPath) -Destination (Join-Path $staging $LibPath) -Recurse -Force

        $zipPath = Join-Path $Root "$OutputDir/$Name"
        if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
        Compress-Archive -Path (Join-Path $staging $parent) -DestinationPath $zipPath -Force
        Write-Host "Created $zipPath"
    } finally {
        Remove-Item $staging -Recurse -Force -ErrorAction SilentlyContinue
    }
}

function New-PlatformTarGz {
    param([string]$Name, [string]$LibPath)

    if (-not (Test-Path (Join-Path $Root $LibPath))) {
        Write-Warning "Skipping missing path: $LibPath"
        return
    }

    if (-not (Get-Command tar -ErrorAction SilentlyContinue)) {
        Write-Warning "tar not found; skipped $Name"
        return
    }

    $parent = Split-Path $LibPath -Parent
    $tarPath = Join-Path $Root "$OutputDir/$Name"
    Push-Location $Root
    try {
        if (Test-Path $tarPath) { Remove-Item $tarPath -Force }
        & tar -czf $tarPath -C $Root $LibPath
        Write-Host "Created $tarPath"
    } finally {
        Pop-Location
    }
}

$linuxDir = "rokae_SDK_linux_v${Version}_${PyTag}"
$winDir = "rokae_SDK_win_v${Version}_${PyTag}"

New-PlatformTarGz -Name "xCoreSDK-Python-$Version-linux-$PyTag.tar.gz" -LibPath "$linuxDir/lib"
New-PlatformZip -Name "xCoreSDK-Python-$Version-win-$PyTag.zip" -LibPath "$winDir/lib"

Write-Host ""
Write-Host "Done. Upload dist/* to GitHub Release v$Version"
