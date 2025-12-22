# app/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    telefone = Column(String, nullable=True)

    cep = Column(String(9), nullable=True)         
    logradouro = Column(String, nullable=True)
    numero = Column(String, nullable=True)
    complemento = Column(String, nullable=True)
    bairro = Column(String, nullable=True)
    localidade = Column(String, nullable=True)
    uf = Column(String(2), nullable=True)
    estado = Column(String, nullable=True)

    criado_em = Column(DateTime, default=datetime.utcnow)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    atendimentos = relationship("Atendimento", back_populates="cliente")


class Atendimento(Base):
    __tablename__ = "atendimento"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    data_hora_inicio = Column(DateTime, nullable=False)
    data_hora_fim = Column(DateTime, nullable=False)
    tipo_servico = Column(String, nullable=False)
    duracao = Column(String, nullable=False)
    resumo = Column(String, nullable=False)
    observacoes = Column(String, nullable=False)
    intervencoes = Column(String, nullable=False)
    recomendacoes = Column(String, nullable=False)
    status = Column(String, nullable=False, default="AGENDADO")
    criado_em = Column(DateTime, default=datetime.utcnow)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    cliente = relationship("Cliente", back_populates="atendimentos")
