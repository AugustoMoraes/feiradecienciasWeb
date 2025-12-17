import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from src.view.PainelInicial import painel_inicial
from src.view.Alunos import alunos    
from src.repository.CategoriaRepository import createCategoria
from src.repository.ProjetoRepository import createProjeto, getProjetos
from src.repository.AlunoRepository import createAluno


if __name__ == "__main__":

    
    #createCategoria('Humanas')
    #createProjeto('Projeto Teste 2', 1)
    tab1, tab2, tab3 = st.tabs(["Projetos", "Categorias", "Alunos"])
    with tab1:
        painel_inicial()
    with tab2:
        st.header("Categorias")
        #createCategoria('Categoria Teste 2')
        #print('Categorias:\n', listar_todas_categorias())
    with tab3:
        alunos()
        #createAluno('Aluno Teste 1', 1)