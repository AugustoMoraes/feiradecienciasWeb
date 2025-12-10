from sqlalchemy.orm import Session
from src.database.Database import engine
from src.model.Projeto import Projeto

def createProjeto(nome: str, id_categoria: int):

    with Session(bind=engine) as session:
        try:
            projeto = Projeto(nome = nome, id_categoria = id_categoria)
            session.add(projeto)
            session.commit()
            print('Projeto cadastrado com sucesso!')
        except Exception as e:
            print(f'Error: {e}')

