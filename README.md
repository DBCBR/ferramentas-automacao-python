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

🛠️ Tecnologias Utilizadas
Python 3 (Linguagem Core)

Selenium WebDriver: Automação de browser e extração de dados dinâmicos.

Pandas & OpenPyXL: Engenharia de dados e geração de relatórios Excel.

SQLite3: Persistência de dados local leve e eficiente.

Requests & JSON: Consumo de APIs REST.

Tkinter: Interfaces gráficas nativas.

Regex: Expressões regulares para mineração de texto.

📦 Como Usar
Pré-requisitos
Instale todas as dependências do projeto com o comando:

```Bash

pip install -r requirements.txt
```

▶️ Executando o Robô Principal (V3.0)
A maneira mais fácil é utilizar o lançador automático:

Dê um duplo clique no arquivo run.bat.

Siga as instruções no terminal (Escolha entre ler um Arquivo ou um Site).

Ao finalizar, verifique a pasta dados/ para acessar o relatório Excel gerado.

Se preferir rodar manualmente via terminal:

```Bash

python main.py
```

📚 Módulos de Estudo (Ferramentas Anteriores)
As ferramentas desenvolvidas anteriormente foram migradas para a pasta estudos/ e continuam funcionais:

1. Consolidador de Excel (ETL)
Unifica planilhas dispersas (ex: vendas_jan.xlsx, vendas_fev.xlsx) em um único relatório.

Execução: python estudos/consolidador.py

2. Robô de Cotações (Crawler)
Navega por múltiplas páginas web para extrair citações e autores.

Execução: python estudos/aula_selenium.py (Antigo extrator_quotes)

3. Robô de Login (RPA)
Demonstração de acesso seguro a sistemas fechados com preenchimento de formulários.

Execução: python estudos/robo_login.py

👨‍💻 Autor
David Barcellos Cardoso

E-mail: dbcbr@hotmail.com

WhatsApp: (21) 98605-8337

GitHub: github.com/DBCBR

Projeto desenvolvido com foco em Clean Code e escalabilidade.
