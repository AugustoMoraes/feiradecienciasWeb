from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from database.Database import Base, engine

class Projeto(Base):
    __tablename__ = 'projetos'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String, index=True)
    id_categoria = Column(Integer, ForeignKey("categorias.id"))
    
    categoria = relationship('Categoria', back_populates='projetos')
    #alunos = relationship('Aluno', back_populates='projetos')

Base.metadata.create_all(bind=engine)