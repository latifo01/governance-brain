param(
    [switch]$CheckOnly,
    [switch]$WithOffice
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

function Require-Command {
    param([Parameter(Mandatory = $true)][string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' is not available on PATH."
    }
}

function Invoke-Checked {
    param(
        [Parameter(Mandatory = $true)][string]$Command,
        [Parameter(ValueFromRemainingArguments = $true)][string[]]$Arguments
    )
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code $LASTEXITCODE: $Command"
    }
}

Push-Location $RepositoryRoot
try {
    Require-Command git
    Require-Command uv
    Require-Command opencode

    if (-not $CheckOnly) {
        Invoke-Checked uv python install
        $SyncArguments = @("sync", "--frozen", "--extra", "dev", "--extra", "data")
        if ($WithOffice) {
            $SyncArguments += @("--extra", "office-windows")
        }
        Invoke-Checked uv @SyncArguments
    }

    $PythonPath = (& uv run --offline --no-sync python -c "import sys; print(sys.executable)").Trim()
    if ($LASTEXITCODE -ne 0 -or $PythonPath -notmatch "[\\/]\.venv[\\/]Scripts[\\/]python\.exe$") {
        throw "uv does not use the repository Windows virtual environment."
    }

    Invoke-Checked uv run --offline --no-sync python -m gov360_brain.workshop validate
    Invoke-Checked uv run --offline --no-sync python -m gov360_brain.workshop check-derived
    Invoke-Checked uv run --offline --no-sync gov360 brain build --check
    Invoke-Checked uv run --offline --no-sync pytest -q

    & opencode debug config *> $null
    if ($LASTEXITCODE -ne 0) {
        throw "OpenCode could not load the project configuration."
    }
    & opencode debug agent cdo-program-lead *> $null
    if ($LASTEXITCODE -ne 0) {
        throw "OpenCode could not load the cdo-program-lead agent."
    }

    Write-Host "Governance Brain Windows checks: PASS"
    Write-Host "Repository: $RepositoryRoot"
    Write-Host "Python: $PythonPath"
}
finally {
    Pop-Location
}
