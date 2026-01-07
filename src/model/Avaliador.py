from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from database.Database import Base

class Avaliador(Base):
    __tablename__ = 'avaliadores'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String, index=True)

    projeto_avaliado = relationship('ProjetoAvaliado', back_populates='avaliador')    

    def to_dict(self):
        return {
            'id': self.id,
            "nome": self.nome,
        }