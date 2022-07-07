from telnetlib import RCP
from fastapi import FastAPI

from infrastructure.treatment.categoria import Categoria
from infrastructure.treatment.despesa import Despesa
from infrastructure.treatment.receita import Receita
# from infrastructure.treatment.saldo import Saldo
from infrastructure.treatment.tipo import Tipo


app = FastAPI()

@app.get("/")
async def root():

    return {"message": "Hello World"}

################## ROTAS RECEITA ####################
@app.get("/receita/list")
async def root():
    receita = Receita()
    list_receitas = receita.list_receita()

    return {
        "message": "Listagem de Receitas",
        "receitas": list_receitas
        }

@app.post("/receita")
async def add_receita(name: str, descricao: str,valor: float, tipo: int):
    receita = Receita()
    receita.create_receita(name,descricao,valor,tipo)

    return {"message": "Cadastro de receitas realizado com sucesso"}

# @app.get("/receita/{id}")
# async def receita_id(id: int):
#     return {"message": "Detalhameto de Receita"}

# @app.put("/receita/{id}")
# async def update_receita_id(id: int):
#     return {"message": "Atualização de Receita"}

# @app.delete("/receita/{id}")
# async def delete_receita_id(id: int):
#     return {"message": "Exclusão de Receita"}

# ################## ROTAS DESPESAS ####################

@app.get("/despesa/list")
async def root():
    despesa = Despesa()
    list_despesas = despesa.list_despesa()

    return {
        "message": "Listagem de Despesas",
        "receitas": list_despesas
        }

@app.post("/despesa")
async def add_despesa( name: str, descricao: str, valor: float, categoria: int, tipo: int):
    despesa = Despesa()
    despesa.create_despesa(name,descricao,valor,categoria,tipo)
    return {"message": "Cadastro de despesa realizado com sucesso"}

# @app.get("/despesa/{id}")
# async def despesa_id(id: int):
#     return {"message": "Detalhamento de Despesa"}

# @app.put("/despesa/{id}")
# async def put_despesa_id(id: int):
#     return {"message": "Atualização de Despesa"}

# @app.delete("/despesa/{id}")
# async def delete_despesa_id(id: int):
#     return {"message": "Exclusão de Despesa"}

# ################## ROTAS CATEGORIA ####################

@app.get("/categoria/list")
async def root():
    categoria = Categoria()
    list_categorias = categoria.list_categoria()
    return {
        "message": "Listagem de Categorias",
        "receitas": list_categorias
        }

# ################## ROTAS TIPO ####################

@app.get("/tipo/list")
async def root():
    tipo = Tipo()
    list_tipos = tipo.list_tipo()
    return {
        "message": "Listagem de Tipos",
        "receitas": list_tipos
        }