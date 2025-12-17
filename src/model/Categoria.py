#from __future__ import annotations

from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from database.Database import Base

class Categoria(Base):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String, index=True)

    projetos = relationship('Projeto', back_populates='categoria')

    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }

#Base.metadata.create_all(bind=engine)