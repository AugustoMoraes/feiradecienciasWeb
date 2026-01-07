from sqlalchemy.orm import Session
from database.Database import engine
from src.model.Avaliador import Avaliador

def createAvaliador(nome: str):
    with Session(bind=engine) as session:
        try:
            avaliador = Avaliador(nome=nome)
            session.add(avaliador)
            session.commit()
            print('Avaliador cadastrado com sucesso!')
        except Exception as e:
            print(f'Error: {e}')

def getAvaliadores():
    with Session(bind=engine) as session:
        try:
            avaliadores = session.query(Avaliador).all()
            return [avaliador.to_dict() for avaliador in avaliadores]
        except Exception as e:
            print(f'Error: {e}')
            return []