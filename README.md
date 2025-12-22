
# 🌱 Tropi API

API REST do projeto **Tropi**, desenvolvida para gerenciar **clientes**, **atendimentos** e **consultas de CEP**.
O objetivo da API é fornecer uma base simples, organizada e escalável para o MVP do sistema, utilizando boas práticas de desenvolvimento com **FastAPI**.

---

## 📝 Descrição do Projeto

A **Tropi API** é responsável por:

* Cadastro e listagem de clientes
* Registro de atendimentos vinculados aos clientes
* Consulta de endereços a partir de CEP
* Persistência de dados em banco **SQLite** (ambiente local)
* Exposição de documentação automática via **Swagger**

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11**
* **FastAPI**
* **Uvicorn**
* **Pydantic v2**
* **SQLAlchemy**
* **SQLite**
* **Docker**
* **Docker Compose**

---

## 🚀 Instruções de Instalação

A seguir estão descritas as etapas para configurar o ambiente local e executar a API.

---

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/agatavelasco/tropi-api.git
cd tropi-api
```

---

### 🔹 2. Criar e ativar ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 🔹 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

> ⚠️ Observação: o projeto utiliza o tipo `EmailStr` do Pydantic, portanto a dependência
> `email-validator` já deve estar listada no `requirements.txt`.

---

### 🔹 4. Executar a aplicação localmente

```bash
uvicorn app.main:app --reload
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
docker run --rm -p 8000:8000 tropi-api
```

---

### 🔹 3. Acessar a aplicação

* API: [http://localhost:8000](http://localhost:8000)
* Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Compose (opcional)

Para facilitar o uso e manter o banco SQLite persistido:

```bash
docker compose up --build
```

---

## 📚 Documentação da API

A documentação dos endpoints é gerada automaticamente pelo FastAPI e pode ser acessada em:

👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

No Swagger é possível:

* Visualizar todos os endpoints
* Ver os schemas de requisição e resposta
* Executar chamadas de teste diretamente pelo navegador

---

## 📌 Estrutura Básica do Projeto

```text
tropi-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
├── tropi.db
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 📎 Considerações Finais

* Este projeto utiliza **SQLite** para facilitar o desenvolvimento local
* A estrutura já está preparada para evoluir para **PostgreSQL**
* O uso de Docker garante um ambiente padronizado para qualquer desenvolvedor

