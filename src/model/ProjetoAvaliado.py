from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from database.Database import Base

class ProjetoAvaliado(Base):
    __tablename__ = 'projetos_avaliados'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    av_apresentacao = Column(Integer, index=True)
    av_banner = Column(Integer, index=True)
    av_conhecimento_assunto = Column(Integer, index=True)
    av_postura = Column(Integer, index=True)
    
    
    id_projeto = Column(Integer, ForeignKey("projetos.id"))
    id_avaliador = Column(Integer, ForeignKey("avaliadores.id"))
    
    projeto = relationship('Projeto', back_populates='projeto_avaliado')
    avaliador = relationship('Avaliador', back_populates='projeto_avaliado')

    def to_dict(self):
        return {
            'id': self.id,
            "nome": self.nome,
            "id_projeto": self.id_projeto,
            "id_avaliador": self.id_avaliador,
            "av_apresentacao": self.av_apresentacao,
            "av_banner": self.av_banner,
            "av_conhecimento_assunto": self.av_conhecimento_assunto,
            "av_postura": self.av_postura
        }