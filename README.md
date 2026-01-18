# 🚀 Portfólio: Backend Engineering & Automação Python

> Repositório central de projetos focados em Desenvolvimento Backend (APIs), Engenharia de Dados (ETL) e Automação de Processos (RPA).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

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

### 2. 🤖 Robô Caçador de Contratos V3.0 (Automação ETL)
**Foco:** Web Scraping, Tratamento de Dados e Integração de Sistemas.

Uma aplicação robusta que realiza o ciclo completo de ETL (Extração, Transformação e Carga) para monitoramento e enriquecimento de dados cadastrais (CNPJ).

* **Tecnologias:** Selenium WebDriver, Pandas, Requests, Regex.
* **Pipeline:**
    1.  **Ingestão Híbrida:** Lê arquivos locais (.xlsx) ou varre URLs via Selenium.
    2.  **Mineração (Regex):** Localiza padrões de CNPJ em textos desestruturados.
    3.  **Enriquecimento (API):** Consulta Receita Federal/BrasilAPI com tratamento de exceções.
    4.  **Relatórios:** Gera planilhas Excel formatadas automaticamente.

---

## 📂 Estrutura do Repositório

```text
/ferramentas-automacao-python
│
├── 🚀 BACKEND (API)
│   ├── gestor_tarefas.py      # Aplicação FastAPI (Controller & Routes)
│   └── tarefas.db             # Banco de Dados SQLite (Gerado automaticamente)
│
├── 🤖 AUTOMAÇÃO (ROBÔ)
│   ├── main.py                # O Cérebro do Robô V3.0 (ETL)
│   ├── api_brasil_service.py  # Módulo de conexão com APIs externas
│   ├── web_scraper_service.py # Módulo de visão computacional (Selenium)
│   ├── run.bat                # Lançador Automático
│   └── dados/                 # Inputs e Relatórios gerados
│
└── 📚 LEGADO (ESTUDOS)
    └── estudos/               # Scripts anteriores (Crawlers, Login RPA)
```

---

🛠️ Tech Stack & Ferramentas
Categoria,Tecnologias
Linguagem,Python 3.10+
Backend & API,"FastAPI, Uvicorn, Pydantic"
Banco de Dados,"SQLite3, SQLAlchemy (ORM)"
Engenharia de Dados,"Pandas, OpenPyXL, Regex"
Automação Web,"Selenium WebDriver, Requests"
Outros,"Git, Tkinter, JSON"

---

📦 Como Executar os Projetos
Pré-requisito: Instale as dependências.

```Bash

pip install fastapi uvicorn sqlalchemy requests pandas selenium openpyxl
```

▶️ Opção A: Rodar a API (Gestor de Tarefas)

No terminal, execute o servidor Uvicorn:

```Bash

uvicorn gestor_tarefas:app --reload
```

Acesse a documentação interativa (Swagger) no navegador:

👉 http://127.0.0.1:8000/docs

▶️ Opção B: Rodar o Robô de Automação

Execute o arquivo principal:

```Bash

python main.py
```

Ou use o lançador run.bat para a interface interativa.

---

👨‍💻 Autor
David Barcellos Cardoso Desenvolvedor Python | Backend & Automação

📧 E-mail: dbcbr@hotmail.com

📱 WhatsApp: (21) 98605-8337

🌐 GitHub: github.com/DBCBR

💼 LinkedIn: linkedin.com/in/david-barcellos-cardoso

---

Este portfólio demonstra a capacidade de transitar entre Scripts de Automação e Engenharia de Software (Backend), aplicando Clean Code, POO e arquiteturas escaláveis.
