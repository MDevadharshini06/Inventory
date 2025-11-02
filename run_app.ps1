
$venv = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-Not (Test-Path $venv)) {
	Write-Error "Virtualenv python not found at $venv"
	exit 1
}
& $venv -u (Join-Path $PSScriptRoot 'app.py')
