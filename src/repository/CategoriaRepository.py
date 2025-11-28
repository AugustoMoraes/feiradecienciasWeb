from sqlalchemy import select
from sqlalchemy.orm import Session
from src.database.Database import engine
from src.model.Categoria import Categoria
from src.controller.CategoriaController import limitName


def createCategoria(nome):
    
    with Session(bind = engine) as session:
        if limitName(nome):
            categoria = Categoria(nome = nome)
            session.add(categoria)
            session.commit()
            print('Cadastrado com sucesso!')
        else:
            print('Error ao cadastrar o produto!')
            print('A palavra não pode conter mais de 15 caracteres')

def listar_todas_categorias():
    with Session(bind=engine) as session:
        sql = select(Categoria)
        categorias = session.execute(sql).fetchall()
        categorias = [categoria[0] for categoria in categorias]
        return categorias

