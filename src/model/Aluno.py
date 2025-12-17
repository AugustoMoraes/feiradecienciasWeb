
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from database.Database import Base

class Aluno(Base):
    __tablename__ = 'alunos'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String, index=True)
    id_projeto = Column(Integer, ForeignKey("projetos.id"))

    projeto = relationship('Projeto', back_populates='alunos')
    
    def to_dict(self):
        return {
            'id': self.id,
            "nome": self.nome,
            "id_projeto": self.id_projeto
        }
#Base.metadata.create_all(bind=engine)