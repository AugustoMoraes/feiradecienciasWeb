import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.view.Painel_Inicial.painel import painel_inicial
from src.repository.CategoriaRepository import createCategoria
from src.repository.ProjetoRepository import createProjeto

if __name__ == "__main__":

    #createCategoria('Ciências Humanas')
    #createProjeto('Teste de projeto de ciências exatas', 1)
    painel_inicial()