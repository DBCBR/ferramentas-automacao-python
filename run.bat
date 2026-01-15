@echo off
TITLE ROBO CACADOR DE CONTRATOS - V3.0
color 0A

REM --- CONFIGURAÇÃO DE AMBIENTE ---
cd /d "%~dp0"

echo ==========================================
echo      SISTEMA DE MONITORAMENTO DE CONTRATOS
echo      Status: Inicializando...
echo ==========================================
echo.

REM --- EXECUÇÃO DO ROBÔ ---
REM O Python vai assumir o controle e imprimir os resultados na tela
".venv\Scripts\python.exe" main.py

REM --- FINALIZAÇÃO ---
echo.
echo ==========================================
echo      EXECUCAO FINALIZADA
echo.
echo      Verifique a mensagem do Robo acima para
echo      saber se o relatorio foi gerado.
echo ==========================================
echo.
pause