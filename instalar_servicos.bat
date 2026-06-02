@echo off
chcp 65001 >nul
title Instalar Servicos - TI Internship Finder
cls

echo ==========================================
echo   Instalar Servicos Automaticos
echo   TI Internship Finder
echo ==========================================
echo.
echo Esse script vai configurar:
echo   1. Busca diaria as 09:00 (Task Scheduler)
echo   2. API/Dashboard na inicializacao do Windows
echo.
echo EXECUTE COMO ADMINISTRADOR (botao direito - Executar como adm)
echo.
pause

set "PROJECT_DIR=%~dp0"
set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"

echo.
echo [1/2] Criando tarefa: Busca diaria as 09:00...
schtasks /create /tn "TIInternshipFinder-Diario" /tr "'%PROJECT_DIR%\run_daily.bat'" /sc daily /st 09:00 /ru %USERNAME% /f 2>nul

if %errorlevel% equ 0 (
    echo   OK - Todo dia as 09:00 (silencioso)
) else (
    echo   ERRO - Execute como Administrador
)

echo.
echo [2/2] Criando tarefa: API na inicializacao...
schtasks /create /tn "TIInternshipFinder-API" /tr "'%PROJECT_DIR%\run_api.bat'" /sc onlogon /ru %USERNAME% /f 2>nul

if %errorlevel% equ 0 (
    echo   OK - API inicia automaticamente ao fazer login
) else (
    echo   ERRO - Execute como Administrador
)

echo.
echo ==========================================
echo   Instalacao concluida!
echo ==========================================
echo.
echo   Busca automatica: todo dia as 09:00
echo   Dashboard: http://127.0.0.1:8000
echo.
echo   Para REMOVER os servicos:
echo     schtasks /delete /tn "TIInternshipFinder-Diario" /f
echo     schtasks /delete /tn "TIInternshipFinder-API" /f
echo.
pause
