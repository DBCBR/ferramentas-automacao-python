# 🚀 Portfólio: Backend Engineering, GenAI & Automação

> Repositório central de projetos focados em Desenvolvimento Backend (APIs), Integração com Inteligência Artificial (GenAI) e Automação de Processos (RPA).

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)](https://ai.google.dev/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge)](https://www.sqlalchemy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)

---

## 🏆 Projetos em Destaque

### 1. 🏗️ API Gestor de Tarefas (Backend RESTful)

**Foco:** Desenvolvimento Backend, APIs REST, Persistência de Dados e Arquitetura MVC.

Um microsserviço completo para gerenciamento de tarefas, implementando o ciclo **CRUD** (Create, Read, Update, Delete) com validação de dados rigorosa e persistência em banco de dados relacional.

* **Tecnologias:** FastAPI, SQL Alchemy (ORM), Pydantic, SQLite.
* **Funcionalidades:**
  * ✅ **CRUD Completo:** Criação, leitura, atualização e remoção de registros.
  * ✅ **Persistência Real:** Dados salvos em disco (`tarefas.db`) via SQL.
  * ✅ **Tratamento de Erros:** Respostas HTTP semânticas (201, 204, 404).
  * ✅ **Documentação Automática:** Swagger UI integrado.

---

### 2. 🧠 API Financeira Inteligente (GenAI + Backend)

**Foco:** Integração com IA Generativa, Engenharia de Prompt e ETL via LLM.

Este projeto eleva o nível do CRUD tradicional ao integrar um **Agente de Inteligência Artificial**. O sistema é capaz de interpretar linguagem natural e transformá-la em dados estruturados para o banco de dados.

* **Tecnologias:** FastAPI, Google Gemini API (1.5 Flash / 2.5 Lite), Python-Dotenv.
* **Fluxo da Solução:**
    1. **Input Natural:** Usuário envia: *"Gastei 50 reais no mercado"*.
    2. **Processamento (LLM):** O Gemini analisa a intenção, extrai entidades e converte para JSON.
    3. **Persistência:** O Backend valida e salva automaticamente no SQLite.
* **Diferencial:** Implementação de segurança com Variáveis de Ambiente (`.env`) e tratamento de cotas da API.

---

### 3. 🤖 Robô Caçador de Contratos V3.0 (Automação ETL)

**Foco:** Web Scraping, Tratamento de Dados e Integração de Sistemas.

Uma aplicação robusta que realiza o ciclo completo de ETL (Extração, Transformação e Carga) para monitoramento e enriquecimento de dados cadastrais (CNPJ).

* **Tecnologias:** Selenium WebDriver, Pandas, Requests, Regex.
* **Pipeline:**
    1. **Ingestão Híbrida:** Lê arquivos locais (.xlsx) ou varre URLs via Selenium.
    2. **Mineração (Regex):** Localiza padrões de CNPJ em textos desestruturados.
    3. **Enriquecimento (API):** Consulta Receita Federal/BrasilAPI com tratamento de exceções.
    4. **Relatórios:** Gera planilhas Excel formatadas automaticamente.

---

## 📂 Estrutura do Repositório

```text
/ferramentas-automacao-python
│
├── 🚀 BACKEND & IA (APIs)
│   ├── financas.py            # API com Integração Gemini (Novo!)
│   ├── gestor_tarefas.py      # Aplicação FastAPI (Controller & Routes)
│   ├── .env                   # Variáveis de Ambiente (Segurança)
│   └── *.db                   # Bancos de Dados SQLite
│
├── 🤖 AUTOMAÇÃO (ROBÔ)
│   ├── main.py                # O Cérebro do Robô V3.0 (ETL)
│   ├── api_brasil_service.py  # Módulo de conexão com APIs externas
│   ├── web_scraper_service.py # Módulo de visão computacional (Selenium)
│   └── dados/                 # Inputs e Relatórios gerados
│
└── 📚 LEGADO (ESTUDOS)
    └── estudos/               # Scripts anteriores (Crawlers, Login RPA)
```

---

🛠️ Tech Stack & Ferramentas

```table
Categoria,Tecnologias
Linguagem,Python 3.10+
IA & GenAI,"Google Gemini API, Prompt Engineering"
Backend & API,"FastAPI, Uvicorn, Pydantic"
Banco de Dados,"SQLite3, SQLAlchemy (ORM)"
Engenharia de Dados,"Pandas, OpenPyXL, Regex"
Automação Web,"Selenium WebDriver, Requests"
Outros,"Git, JSON, Dotenv (Security)"
```

---

📦 Como Executar os Projetos
Pré-requisito
Instale as dependências (incluindo as novas libs de IA):

```Bash

pip install fastapi uvicorn sqlalchemy requests pandas selenium openpyxl google-genai python-dotenv
```

▶️ Opção A: Rodar a API Financeira com IA
Crie um arquivo .env na raiz do projeto e adicione sua chave:

Plaintext

GENAI_API_KEY=SuaChaveDoGoogleAqui
Execute o servidor:

```Bash

uvicorn financas:app --reload
```

Teste a IA no Swagger: POST /analisar-transacao-ia

▶️ Opção B: Rodar o Robô de Automação
Execute o arquivo principal:

```Bash

python main.py
```

---

```text 👨‍💻 Autor
David Barcellos Cardoso Desenvolvedor Python | Backend & Automação

📧 E-mail: <dbcbr@hotmail.com>

📱 WhatsApp: (21) 98605-8337

🌐 GitHub: github.com/DBCBR

💼 LinkedIn: linkedin.com/in/david-barcellos-cardoso
```

---

Este portfólio demonstra a capacidade de transitar entre Scripts de Automação, Engenharia de Software e Integração com Inteligência Artificial, aplicando Clean Code e arquiteturas modernas.
