from sqlalchemy.orm import Session
from database.Database import engine
from src.model.Aluno import Aluno

def createAluno(nome: str, id_projeto: int):
    
    with Session(bind=engine) as session:
        try:
            aluno = Aluno(nome=nome, id_projeto=id_projeto)
            session.add(aluno)
            session.commit()
            print('Aluno cadastrado com sucesso!')
        except Exception as e:
            print(f'Error: {e}')

def getAlunos():
    with Session(bind=engine) as session:
        try:
            alunos = session.query(Aluno).all()
            return [aluno.to_dict() for aluno in alunos]
        except Exception as e:
            print(f'Error: {e}')
            return []
        

        