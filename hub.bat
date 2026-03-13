@echo off
title TI Internship Finder - Hub de Controle
chcp 65001 >nul
cls

:menu
cls
echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║                                                        ║
echo ║      🔍  TI INTERNSHIP FINDER - HUB DE CONTROLE       ║
echo ║                                                        ║
echo ╚════════════════════════════════════════════════════════╝
echo.
echo  📋 EXECUTAR:
echo  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo    1 ▶ Busca Manual (UMA VEZ)
echo    2 ▶ Agendador Diário (9:00 todo dia)
echo.
echo  📊 MONITORAR:
echo  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo    3 ▶ Monitor Terminal (com cores e logs)
echo    4 ▶ Dashboard Web (visual bonito)
echo.
echo  📖 INFORMAÇÕES:
echo  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo    5 ▶ Ver Guia de Monitoramento
echo    6 ▶ Ver Logs (system.log)
echo    7 ▶ Ver Arquivo de Vagas (jobs.csv)
echo    8 ▶ Editar Configurações
echo.
echo  ⚙️  SISTEMA:
echo  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo    9 ▶ Abrir Pasta do Projeto
echo    0 ▶ SAIR
echo.
echo ════════════════════════════════════════════════════════
echo.

set /p choice="Escolha uma opção (0-9): "

if "%choice%"=="1" (
    cls
    echo Iniciando Busca Manual...
    echo.
    python main.py
    pause
    goto menu
)

if "%choice%"=="2" (
    cls
    echo Iniciando Agendador...
    python scheduler.py
    pause
    goto menu
)

if "%choice%"=="3" (
    cls
    python monitor.py
    goto menu
)

if "%choice%"=="4" (
    cls
    echo Iniciando API...
    echo.
    echo 🌐 Dashboard disponível em: http://127.0.0.1:8000
    echo.
    python -m uvicorn api:app --reload
)

if "%choice%"=="5" (
    start notepad MONITORAMENTO.md
    goto menu
)

if "%choice%"=="6" (
    start notepad logs\system.log
    goto menu
)

if "%choice%"=="7" (
    start excel jobs.csv 2>nul || start notepad jobs.csv
    goto menu
)

if "%choice%"=="8" (
    start notepad config.py
    goto menu
)

if "%choice%"=="9" (
    explorer .
    goto menu
)

if "%choice%"=="0" (
    cls
    echo Até logo!
    pause
    exit /b
)

cls
echo Opção inválida!
pause
goto menu
