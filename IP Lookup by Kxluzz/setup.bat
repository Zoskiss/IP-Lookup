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
        echo Python n'est pas installé. Tentative de téléchargement et d'installation...

        REM Définir l'URL de téléchargement de Python
        set PY_URL=https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe
        set PY_INSTALLER=python-installer.exe

        REM Télécharger l'installateur de Python
        echo Téléchargement de Python...
        powershell -Command "Invoke-WebRequest -Uri %PY_URL% -OutFile %PY_INSTALLER%"

        REM Installer Python
        echo Installation de Python...
        %PY_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1

        REM Nettoyage
        del %PY_INSTALLER%

        REM Vérifier si l'installation a réussi
        python --version >nul 2>&1
        if %ERRORLEVEL% EQU 0 (
            set PY_CMD=python
            echo Python a été installé avec succès.
        ) else (
            echo Échec de l'installation de Python. Veuillez installer Python manuellement depuis https://www.python.org/downloads/
            pause
            exit /b 1
        )
    )
)

REM Mettre à jour pip
echo Mise à jour de pip...
%PY_CMD% -m pip install --upgrade pip
if %ERRORLEVEL% NEQ 0 (
    echo Une erreur s'est produite lors de la mise à jour de pip.
    pause
    exit /b 1
)
echo Pip a été mis à jour avec succès.

REM Installer les bibliothèques nécessaires
echo Installation des bibliothèques nécessaires...
%PY_CMD% -m pip install requests
if %ERRORLEVEL% NEQ 0 (
    echo Une erreur s'est produite lors de l'installation de requests.
    pause
    exit /b 1
)
echo La bibliothèque requests a été installée avec succès.

REM Afficher les versions des bibliothèques installées
echo Vérification des versions installées...
%PY_CMD% -m pip show requests
if %ERRORLEVEL% NEQ 0 (
    echo Impossible de vérifier la version de requests.
    pause
    exit /b 1
)

echo Toutes les bibliothèques nécessaires sont installées.
pause
