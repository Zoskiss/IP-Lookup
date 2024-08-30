@echo off
setlocal

REM Vérifiez si `py` est disponible
py --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=py
) else (
    REM Vérifiez si `python` est disponible
    python --version >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set PY_CMD=python
    ) else (
        echo Python n'est pas installé. Veuillez installer Python depuis https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

REM Exécuter le script Python
%PY_CMD% main.py
if %ERRORLEVEL% NEQ 0 (
    echo Une erreur s'est produite lors de l'exécution du script.
    pause
    exit /b 1
)

echo Le script a été exécuté avec succès.
pause
