from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from api.utils.auth_util import cadastro, authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/auth/cadastrar", tags=["Authentication"])
def cadastrar(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para cadastro de usuário.
    """
    if not cadastro(form_data.username, form_data.password):
        return "Usuário já cadastrado anteriormente."
    return "Usuário cadastrado"
