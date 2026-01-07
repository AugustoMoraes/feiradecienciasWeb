import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from src.view.PainelInicial import painel_inicial
from src.view.Alunos import alunos    
from src.repository.CategoriaRepository import createCategoria
from src.repository.ProjetoRepository import createProjeto, getProjetos
from src.repository.AlunoRepository import createAluno
from src.repository.AvaliadorRepository import createAvaliador
from src.repository.ProjetoAvaliadoRepository import createProjetoAvaliado

if __name__ == "__main__":

    
    #createCategoria('Humanas')
    #createCategoria('Exatas')
    #createCategoria('Biológicas')
    #createCategoria('Engenharia')
    
    #createAluno('Aluno Teste 1', 1)
    #createAluno('Aluno Teste 2', 1)
    #createAluno('Aluno Teste 3', 2) 
    #createAluno('Aluno Teste 4', 2)
    #createAluno('Aluno Teste 5', 3)
    #createAluno('Aluno Teste 6', 3)
        
    #createProjeto('Projeto Teste 1', 1)
    #createProjeto('Projeto Teste 1', 2)
    #createProjeto('Projeto Teste 2', 3)
    #createProjeto('Projeto Teste 2', 4)
    
    #createAvaliador('Avaliador Teste 1')
    #createAvaliador('Avaliador Teste 2')

    createProjetoAvaliado(8, 9, 7, 10, 1, 1)
    createProjetoAvaliado(7, 8, 7, 9, 1, 2)
    createProjetoAvaliado(7, 8, 7, 9, 2, 2)

    #tab1, tab2, tab3 = st.tabs(["Projetos", "Categorias", "Alunos"])
    #with tab1:
    #    painel_inicial()
    #with tab2:
    #    st.header("Categorias")
        #createCategoria('Categoria Teste 2')
        #print('Categorias:\n', listar_todas_categorias())
    #with tab3:
    #    alunos()
        #createAluno('Aluno Teste 1', 1)