# routers/clientes.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..deps import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"],
)


@router.get("/", response_model=List[schemas.ClienteOut])
def listar_clientes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    clientes = db.query(models.Cliente).offset(skip).limit(limit).all()
    return clientes


@router.get("/{cliente_id}", response_model=schemas.ClienteOut)
def obter_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    return cliente


@router.post("/", response_model=schemas.ClienteOut, status_code=status.HTTP_201_CREATED)
def criar_cliente(
    cliente_in: schemas.ClienteCreate,
    db: Session = Depends(get_db)
):
    # Poderia validar CPF/Email aqui se quiser
    cliente = models.Cliente(**cliente_in.dict())
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    db.refresh(cliente)
    return cliente


@router.put("/{cliente_id}", response_model=schemas.ClienteOut)
def atualizar_cliente(
    cliente_id: int,
    cliente_in: schemas.ClienteUpdate,
    db: Session = Depends(get_db)
):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    for campo, valor in cliente_in.dict(exclude_unset=True).items():
        setattr(cliente, campo, valor)

    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    db.delete(cliente)
    db.commit()
    return None
