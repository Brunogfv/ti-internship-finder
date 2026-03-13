@echo off
chcp 65001 >nul
cls
echo ==========================================
echo   TI Internship Finder - Scheduler
echo ==========================================
echo.
echo O sistema irá rodar DIARIAMENTE às 9:00
echo Pressione Ctrl+C para parar
echo.
python scheduler.py
