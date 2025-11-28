import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..')))


def limitName(nome: str):

    nome_formatado = nome.replace(' ', '')
    limit = True if len(nome_formatado) <= 15 else False

    return limit    