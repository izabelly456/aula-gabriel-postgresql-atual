import streamlit as st
from crud import criar_aluno, ler_alunos, atualizar_aluno, deletar_aluno  

st.set_page_config(page_title="Gerenciamento de Alunos", page_icon="👀")

st.title("Sistema de alunos com PostgreSQL")

menu = st.sidebar.selectbox("Menu", ["Inserir", "Listar Alunos", "Atualizar", "Deletar"])

if menu == "Inserir":
    st.subheader(" Inserir novo aluno")
    nome = st.text_input("Nome", placeholder= "Seu nome ")
    idade = st.number_input("Idade", min_value=16, step=1,)
    if st.button("Cadastrar"):
        if nome.strip() == "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} cadastrado com sucesso!")
        else:
            st.warning("O campo nome não pode sser vazio.")