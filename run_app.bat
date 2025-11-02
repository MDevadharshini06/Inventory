@echo off
REM 
set VENV=%~dp0.venv\Scripts\python.exe
if not exist "%VENV%" (
  echo Virtualenv python not found at %VENV%
  exit /b 1
)
"%VENV%" -u "%~dp0app.py"
