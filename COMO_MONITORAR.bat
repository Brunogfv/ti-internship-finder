@echo off
chcp 65001 >nul
cls
echo.
echo ========================================
echo   TI Internship Finder - Como Monitorar
echo ========================================
echo.
echo Existem 3 formas de acompanhar o programa:
echo.
echo 1. TERMINAL COM LOGS COLORIDOS
echo    Clique duplo em: monitor.bat
echo.
echo    • Vê o status em tempo real com cores
echo    • Últimos 15 logs do sistema
echo    • Menu de opções (R/S/A/L/C/Q)
echo    • Auto-atualiza a cada atualização
echo.
echo 2. DASHBOARD WEB (RECOMENDADO)
echo    Clique duplo em: api_start.bat
echo    Acesse: http://127.0.0.1:8000
echo.
echo    • Interface moderna e colorida
echo    • Todas as vagas com imagens
echo    • Auto-atualiza a cada 5 segundos
echo    • Ver links diretos para aplicar
echo.
echo 3. ARQUIVO DE LOGS
echo    Abra: logs\system.log
echo.
echo    • Histórico completo de execuções
echo    • Data e hora de cada operação
echo    • Erros e avisos
echo.
echo ========================================
echo COMO FUNCIONA:
echo ========================================
echo.
echo • executar.bat = Busca UMA VEZ
echo • agendador.bat = Roda DIARIAMENTE às 9h
echo • monitor.bat = Acompanha com logs
echo • api_start.bat = Dashboard web
echo.
echo Você receberá notificações por:
echo • EMAIL: bruno.gfv@gmail.com
echo • TELEGRAM: Chat ID 969624447
echo.
echo ========================================
echo.
pause
