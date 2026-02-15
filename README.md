
# 🌱 Tropi API

API REST do projeto **Tropi**, desenvolvida para gerenciar **clientes**, **atendimentos** e **consultas de CEP**.
O objetivo da API é fornecer uma base simples, organizada e escalável para o MVP do sistema, utilizando boas práticas de desenvolvimento com **FastAPI**.

---

## 📝 Descrição do Projeto

A **Tropi API** é responsável por:

* Cadastro e listagem de clientes
* Registro de atendimentos vinculados aos clientes
* Consulta de endereços a partir de CEP
* Persistência de dados em **PostgreSQL** (Supabase)
* Autenticação via **Supabase Auth** (JWT)
* Exposição de documentação automática via **Swagger**

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11**
* **FastAPI**
* **Uvicorn**
* **Pydantic v2**
* **SQLAlchemy**
* **PostgreSQL** (Supabase)
* **Alembic** (migrações)
* **Supabase Auth** (JWT)
* **Sentry** (monitoramento)
* **Docker**

---

## 🚀 Instruções de Instalação

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/agatavelasco/tropi-api.git
cd tropi-api
```

---

### 🔹 2. Criar e ativar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 🔹 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Configurar variáveis de ambiente

```bash
cp .env.example .env
```

Preencha o `.env` com suas credenciais do Supabase:
- `DATABASE_URL` — Connection string do PostgreSQL (Settings > Database > URI)
- `SUPABASE_URL` — URL do projeto (Settings > API)
- `SUPABASE_ANON_KEY` — Chave pública anon (Settings > API)
- `SUPABASE_SERVICE_ROLE_KEY` — Chave service role (Settings > API)
- `SUPABASE_JWT_SECRET` — JWT secret (Settings > API > JWT)

---

### 🔹 5. Executar a aplicação localmente

```bash
uvicorn app.main:app --reload --port 8000
```

A API ficará disponível em:

* **[http://localhost:8000](http://localhost:8000)**
* **Documentação Swagger:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Executando com Docker

### 🔹 1. Build da imagem Docker

```bash
docker build -t tropi-api .
```

---

### 🔹 2. Executar o container

```bash
docker run --rm -p 8000:8000 --env-file .env tropi-api
```

---

## 📚 Documentação da API

A documentação dos endpoints é gerada automaticamente pelo FastAPI e pode ser acessada em:

👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 📌 Estrutura do Projeto

```text
tropi-api/
├── .env.example
├── .github/workflows/ci.yml
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
├── requirements.txt
├── dockerfile
└── README.md
```

---

## 📎 Considerações

* O banco de dados é **PostgreSQL** hospedado no **Supabase**
* Autenticação via **JWT** do Supabase Auth
* CI configurado com **GitHub Actions** (ruff + mypy)
* Dockerfile com **multi-stage build** para imagens menores e mais seguras

