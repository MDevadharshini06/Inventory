Run the app using the project's virtual environment to avoid ModuleNotFoundError for Flask.

Quick options:

1) Run directly (no activation required):

```powershell
C:\Users\Welcome\Desktop\flask\.venv\Scripts\python.exe c:\Users\Welcome\Desktop\flask\app.py
```

2) Use the included helper scripts:

PowerShell:
```powershell
.\run_app.ps1
```

Windows (cmd):
```
run_app.bat
```

3) In VS Code: open Command Palette -> "Python: Select Interpreter" -> choose
`c:\Users\Welcome\Desktop\flask\.venv\Scripts\python.exe`. After selecting, use the Run or Debug button; the workspace settings already point to the venv interpreter.

Why this is needed:
- Your system `python` may point to a different installation that doesn't have Flask installed. The project's virtualenv contains the correct packages.
