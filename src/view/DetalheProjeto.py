import streamlit as st


def detalhe_projeto():
    st.title("Detalhes do Projeto")
    projeto_id = st.session_state.get('projeto_selecionado')
    st.write(f"Exibindo detalhes para o projeto com ID: {projeto_id}")
    # Aqui você pode adicionar mais detalhes do projeto conforme necessário

