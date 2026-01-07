from sqlalchemy.orm import Session
from database.Database import engine
from src.model.Avaliador import Avaliador
from src.model.ProjetoAvaliado import ProjetoAvaliado    

def createProjetoAvaliado(av_apresentacao: int, av_banner: int, av_conhecimento_assunto: int, av_postura: int, id_projeto: int, id_avaliador: int):
    with Session(bind=engine) as session:
        try:
            projeto_avaliado = ProjetoAvaliado(
                av_apresentacao=av_apresentacao,
                av_banner=av_banner,
                av_conhecimento_assunto=av_conhecimento_assunto,
                av_postura=av_postura,
                id_projeto=id_projeto,
                id_avaliador=id_avaliador
            )
            session.add(projeto_avaliado)
            session.commit()
            print('Projeto Avaliado cadastrado com sucesso!')
        except Exception as e:
            print(f'Error: {e}')  


def getProjetosAvaliados():
    with Session(bind=engine) as session:
        try:
            projetos_avaliados = session.query(ProjetoAvaliado).all()
            return [projeto_avaliado.to_dict() for projeto_avaliado in projetos_avaliados]
        except Exception as e:
            print(f'Error: {e}')
            return []