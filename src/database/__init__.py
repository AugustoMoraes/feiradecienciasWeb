import sys
import os

from database.Database import Base, engine

from src.model.Aluno import Aluno
from src.model.Projeto import Projeto
from src.model.Categoria import Categoria

Base.metadata.create_all(bind=engine)