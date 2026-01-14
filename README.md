# 🚀 Automação de Processos Corporativos com Python

> Portfólio de ferramentas desenvolvidas para automatizar tarefas repetitivas de ETL (Extract, Transform, Load), Web Scraping e RPA (Robotic Process Automation), focadas em eficiência, agendamento automático e redução de custos operacionais.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Status](https://img.shields.io/badge/Status-Concluído-success) ![Selenium](https://img.shields.io/badge/Selenium-Automated-green)

## 📋 Sobre o Projeto

Este repositório contém soluções profissionais para resolver dores reais do setor administrativo e financeiro:

1.  **Consolidador de Relatórios Financeiros (ETL):** Lê múltiplos arquivos Excel (ex: relatórios de filiais), unifica os dados, padroniza colunas e gera um Relatório Executivo formatado automaticamente.
2.  **Monitor de Cotações (Web Crawler):** Robô que navega por múltiplas páginas de um site, extrai dados de interesse (preços/citações) e gera uma base de dados estruturada em Excel.
3.  **Bot de Acesso Seguro (RPA/Selenium):** Automação de navegador real capaz de quebrar barreiras de login, preencher formulários dinâmicos e navegar em sistemas fechados. **(Suporta modo Headless/Invisível)**.
4.  **Agendamento Inteligente:** Scripts de orquestração (`.bat` e `.vbs`) para execução silenciosa e recorrente via Agendador de Tarefas do Windows.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Selenium WebDriver:** Automação de browser com suporte a execução em segundo plano (Headless).
* **Pandas & OpenPyXL:** Manipulação avançada de dados e formatação de Excel (Data Engineering).
* **BeautifulSoup4 & Requests:** Extração de dados web leve e rápida.
* **Windows Batch & VBScript:** Integração com o sistema operacional para agendamento de tarefas.

## 📦 Como Usar

### Pré-requisitos

Você precisa ter o Python instalado. Instale todas as dependências do projeto com:

```bash
pip install pandas openpyxl requests beautifulsoup4 selenium webdriver-manager
```

1. Consolidador de Excel (ETL)
Ferramenta para unificar planilhas dispersas.

Preparação: Coloque seus arquivos na pasta raiz com o padrão vendas_*.xlsx.

Execução:

```Bash

python consolidador.py
```

Resultado: Gera o arquivo Relatorio_Executivo_Formatado.xlsx com colunas ajustadas automaticamente.

2. Robô de Cotações (Crawler)
Ferramenta para extração de dados em massa (Data Mining).

Execução:

```Bash

python extrator_quotes.py
```

Resultado: O robô navega por 5 páginas e salva o arquivo citacoes_famosas_completo.xlsx.

3. Robô de Login (RPA)
Demonstração de acesso a sistemas fechados (Simulador de Usuário).

Execução Manual:

```Bash

python robo_login.py
```

Resultado: O script acessa o sistema, realiza login seguro e valida a entrada via XPath.

4. Automação Avançada (Agendamento)
Para rodar os robôs automaticamente sem intervenção humana:

Execução via Batch (executar_robo.bat): Script ponte que ativa o ambiente virtual e roda o robô. Ideal para usar no Agendador de Tarefas do Windows.

Execução Invisível (launcher_invisivel.vbs): Script para rodar o processo em total silêncio (sem abrir janelas de terminal ou navegador), ideal para execução em background enquanto o usuário utiliza o computador.

👨‍💻 Autor
David Barcellos Cardoso

E-mail: dbcbr@hotmail.com

WhatsApp: (21) 98605-8337

GitHub: github.com/DBCBR
