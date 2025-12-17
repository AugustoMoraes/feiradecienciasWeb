import streamlit as st
from time import sleep
from src.repository.ProjetoRepository import getProjetos, createProjeto, getProjetoById
from src.repository.CategoriaRepository import listar_todas_categorias, createCategoria
from src.view.Alunos import alunos, getAlunos
from src.view.DetalheProjeto import detalhe_projeto


projetos = getProjetos() 
def alunos_projeto():
    projeto_selecionado = st.session_state.get('projeto_selecionado')
    projetos = getProjetoById(projeto_selecionado)
    #st.markdown("Lista de Alunos")
    st.text(f'{projetos["alunos"]}')
    projetos_alunos = projetos['alunos']
    for aluno in projetos_alunos:
        st.subheader(aluno['nome'])
        
        #alunos_do_projeto = getAlunos()
        
        #st.write("Alunos:")

@st.dialog("Adicionar Projeto")
def add_projeto():
    categorias = listar_todas_categorias()
    categorias_names = [[categoria.nome, categoria.id] for categoria in categorias]
    nome_projeto = st.text_input("Nome")
    categoria_selected = st.selectbox("Selecionar Categoria", options=categorias_names, format_func=lambda x: x[0])
    if st.button('Salvar', icon="💾"):
        createProjeto(nome_projeto, categoria_selected[1])
        st.success('Projeto salvo com sucesso!', icon="✅")
        sleep(2)
        st.rerun()

@st.dialog("Adicionar Categoria")
def add_categoria():
    #st.dialog("Adicionar Projeto")
    nome_categoria = st.text_input("Nome")
    if st.button('Salvar', icon="💾"):
        createCategoria(nome_categoria)
        st.success("Categoria salva com sucesso!", icon="✅")
        sleep(2)
        st.rerun()

def painel_inicial():
    container_header = st.container(vertical_alignment="distribute", horizontal_alignment="center", horizontal=True)
    col1, col2 , col3 = container_header.columns([3, 2, 1], vertical_alignment="center", )
    col1.title("Projetos")
    col2.button("Projeto", key="add_projeto", on_click=add_projeto, icon="➕")
    col3.button("Categoria", key="add_categoria", on_click=add_categoria, icon="➕", use_container_width=True)
    st.markdown("Projetos selecionados")
    
       
    
    print(projetos)
    #col1, col2 = st.columns(2)
    for projeto in projetos:
        container_projeto = st.container(border= True, vertical_alignment="center", horizontal=True)
        col1, col2 = container_projeto.columns([2,1], border=True)
        col1.subheader(f"Nome: {projeto['nome']}")
        if col2.button("Detalhes", key=f'detalhe_{projeto['id']}', icon="ℹ️"):
                st.session_state['projeto_selecionado'] = projeto['id']
                #detalhe_projeto()
                #st.switch_page("DetalheProjeto.py")
                alunos_projeto()
                #st.rerun()    
        
        #st.write(f"Categoria: {projeto['categoria']['nome']}")
        #st.write("Alunos:")
        #for aluno in projeto['alunos']:
            #st.write(f"- {aluno['nome']}")
    # Adicione mais componentes do painel conforme necessário

#painel_inicial()