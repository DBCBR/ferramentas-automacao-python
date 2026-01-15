# 🚀 Automação de Processos Corporativos & Inteligência de Dados

> Portfólio de ferramentas desenvolvidas para automatizar tarefas de ETL, Web Scraping, RPA e Enriquecimento de Dados, focadas em eficiência e redução de custos operacionais.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![SQLite](https://img.shields.io/badge/SQLite-Database-blue) ![Selenium](https://img.shields.io/badge/Selenium-Automated-green) ![Status](https://img.shields.io/badge/Status-Ativo-success)

## 📋 Sobre o Projeto

Este repositório evoluiu de uma coleção de scripts para uma **Suíte de Automação Profissional**. O foco principal é o **Robô Caçador de Contratos (V3.0)**, uma solução completa de monitoramento e enriquecimento de dados cadastrais.

### 🔥 Destaque Principal: Robô Caçador de Contratos (V3.0)

Uma aplicação robusta que realiza o ciclo completo de ETL (Extração, Transformação e Carga):

1. **Ingestão Híbrida:** Aceita entrada de dados via **Arquivos Locais** (.txt, .xlsx, .csv) ou **Web Scraping** direto de URLs (via Selenium).
2. **Mineração de Dados (Regex):** Localiza padrões de CNPJ em textos desestruturados.
3. **Enriquecimento (API):** Consulta automaticamente a situação cadastral na Receita Federal (via BrasilAPI) com tratamento de erros (404, 429, 500).
4. **Armazenamento e Relatórios:** Salva o histórico em banco de dados **SQLite** e gera relatórios formatados em **Excel** automaticamente.
5. **Interface Amigável:** Menu interativo e janelas de seleção de arquivos nativas do Windows.

---

## 📂 Estrutura do Projeto

O projeto foi reestruturado seguindo padrões de arquitetura limpa:

```text
/ferramentas-automacao-python
│
├── 📁 dados/                  # Onde ficam os inputs (arquivos) e outputs (relatórios e banco)
├── 📁 estudos/                # Scripts de ferramentas anteriores e testes (Legado)
├── 📄 main.py                 # O Cérebro do Robô V3.0 (Arquivo Principal)
├── 📄 api_brasil_service.py   # Módulo de conexão e tratamento de API
├── 📄 web_scraper_service.py  # Módulo de visão computacional (Selenium)
├── ⚙️ run.bat                 # Lançador Automático (Clique e Rode)
└── 📄 requirements.txt        # Lista de dependências
