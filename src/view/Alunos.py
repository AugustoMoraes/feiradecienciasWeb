import streamlit as st
from time import sleep

from src.repository.ProjetoRepository import getProjetoById, getProjetos
from src.repository.AlunoRepository import getAlunos, createAluno


@st.dialog("Adicionar Aluno")
def add_aluno_projeto():
    projetos = getProjetos()
    nome_aluno = st.text_input("Nome")
    projeto_selected = st.selectbox("Selecionar Categoria", options=projetos, format_func=lambda x: x['nome'])
    if st.button('Salvar', icon="💾"):
        #createAluno(nome_aluno, projeto_selected['id'])
        st.text(f"Aluno: {nome_aluno}, Projeto ID: {projeto_selected['id']}")
        createAluno(nome_aluno, projeto_selected['id'])
        st.success('Aluno salvo com Sucesso!', icon="✅")
        sleep(2)
        st.rerun()

def alunos():
    alunos = getAlunos()
    cols = st.columns([0.7, 0.3])
    with cols[0]:
        st.title("Alunos Cadastrados")
    with cols[1]:
        if st.button("Cadastrar aluno", icon="➕"):
            add_aluno_projeto()
    
    st.markdown("Lista de Alunos")
    
    for aluno in alunos:
        st.subheader(aluno['nome'])
        projeto = getProjetoById(aluno['id_projeto'])
        if projeto:
            st.write(f"Projeto: {projeto['nome']}")
        else:
            st.write("Projeto: Não encontrado")
        st.write("-----")
        st.write("Alunos:")


#alunos()  