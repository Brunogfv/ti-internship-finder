@echo off
chcp 65001 >nul
cls
echo ==========================================
echo   TI Internship Finder - API REST
echo ==========================================
echo.
echo API iniciada em: http://127.0.0.1:8000
echo Documentação em: http://127.0.0.1:8000/docs
echo.
python -m uvicorn api:app --reload
