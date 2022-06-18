from fastapi import FastAPI
from datetime import datetime

# from infrastructure.treatment.categoria import Categoria
# from infrastructure.treatment.despesa import Despesa
# from infrastructure.treatment.receita import Receita
# from infrastructure.treatment.saldo import Saldo
# from infrastructure.treatment.tipo import Tipo


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

################## ROTAS RECEITA ####################
# @app.get("/receita/list")
# async def root():
#     return {"message": "Listagem de Receitas"}

# @app.post("/receita")
# async def add_receita(
#     name: str, descricao: str, 
#     valor: float, date:datetime, 
#     categoria: int, tipo: int
#     ):
#     return {"message": "Cadastro de Receitas"}

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

# @app.get("/despesa/list")
# async def root():
#     return {"message": "Listagem de Despesas"}

# @app.post("/despesa")
# async def add_despesa(
#     name: str, descricao: str, 
#     valor: float, date:datetime, 
#     categoria: int, tipo: int
#     ):
#     return {"message": "Cadastro de Despesas"}

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

# @app.get("/categoria/list")
# async def root():
#     return {"message": "Listagem das Categorias"}

# ################## ROTAS TIPO ####################

# @app.get("/tipo/list")
# async def root():
#     return {"message": "Listagem dos Tipos"}