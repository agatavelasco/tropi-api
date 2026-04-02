# app/schemas.py
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


# ---------------------- CLIENTE ---------------------- #

class ClienteBase(BaseModel):
    nome: str
    cpf: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    localidade: Optional[str] = None
    uf: Optional[str] = None
    estado: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    localidade: Optional[str] = None
    uf: Optional[str] = None
    estado: Optional[str] = None


class ClienteOut(ClienteBase):
    id: int

    class Config:
        from_attributes = True


# ---------------------- ATENDIMENTO ---------------------- #

class AtendimentoBase(BaseModel):
    cliente_id: int
    data_hora_inicio: datetime
    data_hora_fim: datetime
    tipo_servico: str

    duracao: str
    resumo: str
    observacoes: str
    intervencoes: str
    recomendacoes: str

    status: Optional[str] = "AGENDADO"

class AtendimentoCreate(AtendimentoBase):
    pass

class AtendimentoUpdate(BaseModel):
    data_hora_inicio: Optional[datetime] = None
    data_hora_fim: Optional[datetime] = None
    tipo_servico: Optional[str] = None

    duracao: Optional[str] = None
    resumo: Optional[str] = None
    observacoes: Optional[str] = None
    intervencoes: Optional[str] = None
    recomendacoes: Optional[str] = None

    status: Optional[str] = None

class AtendimentoOut(AtendimentoBase):
    id: int

    class Config:
        from_attributes = True