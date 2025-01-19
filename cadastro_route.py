from fastapi import FastAPI
from api.Controller import cadastro
from api.utils import auth_util

app = FastAPI()

# Rotas de cadastro
app.include_router(cadastro.router)