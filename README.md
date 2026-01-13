# 🚀 Automação de Processos Corporativos com Python

> Ferramentas desenvolvidas para automatizar tarefas repetitivas de ETL (Extract, Transform, Load) e Web Scraping, focadas em redução de custos operacionais.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Status](https://img.shields.io/badge/Status-Concluído-success)

## 📋 Sobre o Projeto

Este repositório contém scripts profissionais para resolver dores reais do setor administrativo e financeiro:

1.  **Consolidador de Relatórios Financeiros (ETL):** Lê múltiplos arquivos Excel (ex: relatórios de filiais), unifica os dados, remove colunas desnecessárias e gera um Relatório Executivo formatado automaticamente.
2.  **Monitor de Cotações (Web Crawler):** Robô que navega por múltiplas páginas de um site, extrai dados de interesse (preços/citações) e gera uma base de dados estruturada em Excel.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas & OpenPyXL:** Manipulação avançada de dados e formatação de Excel.
* **BeautifulSoup4 & Requests:** Extração de dados web (Web Scraping).
* **Glob:** Gerenciamento de arquivos do sistema.

## 📦 Como Usar

### Pré-requisitos
Você precisa ter o Python instalado. Instale as dependências com:

```bash
pip install pandas openpyxl requests beautifulsoup4

1. Consolidador de Excel
Coloque seus arquivos de vendas na pasta arquivos_entrada/ com o padrão vendas_*.xlsx. Execute:

Bash

python consolidador.py
Resultado: Será gerado o arquivo Relatorio_Executivo_Formatado.xlsx pronto para envio.

2. Robô de Cotações
Execute o script para iniciar a varredura:

Bash

python robo_citacoes.py
Resultado: O robô navegará pelas páginas e salvará o arquivo citacoes_famosas_completo.xlsx.

Autor: David [github.com/DBCBR] | [dbcbr@hotmail.com]
