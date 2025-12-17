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

def getProjetos():
    with Session(bind=engine) as session:
        try:
            projetos = session.query(Projeto).all()
            return [projeto.to_dict() for projeto in projetos]
        except Exception as e:
            print(f'Error: {e}')
            return []   
        
def getProjetoById(id_projeto: int):
    with Session(bind=engine) as session:
        try:
            projeto = session.query(Projeto).filter(Projeto.id == id_projeto).first()
            if projeto:
                return projeto.to_dict()
            else:
                return None
        except Exception as e:
            print(f'Error: {e}')
            return None
        

