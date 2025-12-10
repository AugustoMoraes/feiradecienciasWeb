import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..')))

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

pasta_atual = Path(__file__).parent
PATH_TO_BD = pasta_atual / 'bd_feira_ciencias.sqlite'

SQLALCHEMY_DATABASE_URL = f"sqlite:///{PATH_TO_BD}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


