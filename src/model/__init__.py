import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..')))

from database.Database import Base, engine
#from model import Categoria, Projeto 

Base.metadata.create_all(bind=engine)
#print('Tabelas Criadas com sucesso!')