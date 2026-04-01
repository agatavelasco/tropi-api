# app/main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import clientes, atendimentos, cep

load_dotenv()

# IMPORTANTE: Nao usar mais Base.metadata.create_all().
# Toda alteracao no schema deve ser feita via Alembic:
#   alembic revision --autogenerate -m "descricao"
#   alembic upgrade head

app = FastAPI(
    title="Tropi API",
    description="API do sistema Tropi - gestao de clientes e atendimentos",
    version="0.1.0",
    redirect_slashes=False,
)

# CORS - lido do .env ou fallback para localhost
cors_origins_str = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000")
origins = [origin.strip() for origin in cors_origins_str.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router)
app.include_router(atendimentos.router)
app.include_router(cep.router)


@app.get("/")
def root():
    return {"message": "Tropi API is running 🌿"}
