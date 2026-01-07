#from __future__ import annotations

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from database.Database import Base

class Projeto(Base):
    __tablename__ = 'projetos'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String, index=True)
    id_categoria = Column(Integer, ForeignKey("categorias.id"))
    
    categoria = relationship('Categoria', back_populates='projetos')
    alunos = relationship('Aluno', back_populates='projeto')
    projeto_avaliado = relationship('ProjetoAvaliado', back_populates='projeto')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'id_categoria': self.id_categoria,
            'categoria': self.categoria.to_dict() if self.categoria else None,
            'alunos': [aluno.to_dict() for aluno in self.alunos]
        }
