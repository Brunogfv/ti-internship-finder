@echo off
chcp 65001 >nul
cls
echo ==========================================
echo   TI Internship Finder - Busca Manual
echo ==========================================
echo.
python main.py
if %errorlevel% neq 0 (
    echo.
    echo ERRO na execução!
    pause
) else (
    echo.
    echo Busca concluída com sucesso!
    echo Verifique os logs em: logs\system.log
    echo Dados salvos em: jobs.csv e jobs.db
    pause
)
