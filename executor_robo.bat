@echo off
:: 1. Entra na pasta do projeto
:: ATENÇÃO: Confirme se sua pasta chama "Python" ou "Pyhton".
:: No erro que você mandou, está escrito "Python" (correto).
cd /d "C:\Projetos\Python\ferramentas-automacao-python"

:: 2. Em vez de ativar, chamamos o Python DO VENV direto pelo nome e sobrenome
:: Isso garante que ele use as bibliotecas certas.
".venv\Scripts\python.exe" robo_login.py
