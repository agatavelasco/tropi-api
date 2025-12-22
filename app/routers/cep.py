# app/routers/cep.py
from fastapi import APIRouter, HTTPException
from app.services.cep import consultar_cep

router = APIRouter(prefix="/cep", tags=["CEP"])


@router.get("/{cep}")
def buscar_cep(cep: str):
    try:
        return consultar_cep(cep)
    except ValueError as e:
        # erro de CEP inválido ou não encontrado
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # em DEV é bom ver o erro de verdade 😉
        raise HTTPException(
            status_code=502,
            detail=f"Erro ao consultar serviço de CEP: {e}"
        )
