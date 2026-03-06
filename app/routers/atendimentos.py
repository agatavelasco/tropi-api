# routers/atendimentos.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.deps import get_db
from app.auth import get_current_user

router = APIRouter(
    prefix="/atendimentos",
    tags=["Atendimentos"],
)


@router.get("/", response_model=List[schemas.AtendimentoOut])
def listar_atendimentos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    atendimentos = db.query(models.Atendimento).offset(skip).limit(limit).all()
    return atendimentos


@router.get("/{atendimento_id}", response_model=schemas.AtendimentoOut)
def obter_atendimento(
    atendimento_id: int,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    atendimento = (
        db.query(models.Atendimento)
        .filter(models.Atendimento.id == atendimento_id)
        .first()
    )
    if not atendimento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Atendimento não encontrado"
        )
    return atendimento


@router.post("/", response_model=schemas.AtendimentoOut, status_code=status.HTTP_201_CREATED)
def criar_atendimento(
    atendimento_in: schemas.AtendimentoCreate,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):

    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == atendimento_in.cliente_id
    ).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cliente informado não existe"
        )

    if atendimento_in.data_hora_inicio >= atendimento_in.data_hora_fim:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="data_hora_inicio deve ser anterior a data_hora_fim"
        )

    atendimento = models.Atendimento(**atendimento_in.dict())
    db.add(atendimento)
    db.commit()
    db.refresh(atendimento)
    return atendimento


@router.put("/{atendimento_id}", response_model=schemas.AtendimentoOut)
def atualizar_atendimento(
    atendimento_id: int,
    atendimento_in: schemas.AtendimentoUpdate,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    atendimento = (
        db.query(models.Atendimento)
        .filter(models.Atendimento.id == atendimento_id)
        .first()
    )
    if not atendimento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Atendimento não encontrado"
        )

    dados_atualizados = atendimento_in.dict(exclude_unset=True)

    nova_data_inicio = dados_atualizados.get("data_hora_inicio", atendimento.data_hora_inicio)
    nova_data_fim = dados_atualizados.get("data_hora_fim", atendimento.data_hora_fim)
    if nova_data_inicio >= nova_data_fim:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="data_hora_inicio deve ser anterior a data_hora_fim"
        )

    for campo, valor in dados_atualizados.items():
        setattr(atendimento, campo, valor)

    db.add(atendimento)
    db.commit()
    db.refresh(atendimento)
    return atendimento


@router.delete("/{atendimento_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_atendimento(
    atendimento_id: int,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    atendimento = (
        db.query(models.Atendimento)
        .filter(models.Atendimento.id == atendimento_id)
        .first()
    )
    if not atendimento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Atendimento não encontrado"
        )

    db.delete(atendimento)
    db.commit()
    return None