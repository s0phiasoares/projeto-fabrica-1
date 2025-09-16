import streamlit as st

st.subheader ("Bem vindo a calculadora de media escolar 😁")
st.title ("calculadora de média escolar🎒📱")

nota1=st.number_input("digite a nota do 1ª Bimestre",min_value=0.0)
nota2=st.number_input("digite a nota do 2ª Bimestre",min_value=0.0)
nota3=st.number_input("digite a nota do 3ª Bimestre",min_value=0.0)
nota4=st.number_input("digite a nota do 4ª Bimestre",min_value=0.0)

btn_calcular = st.button ("Calcular")

if btn_calcular:
    media = (nota1 + nota2 + nota3 + nota4 ) / 4
    if media>= 7:
        st.success("Parabens! você foi aprovado 😁✅")


    elif media>=5.0:
        st.warning ("Você ficou de recuperaçâo, CUIDADO ⚠️ ")

    elif media< 5.0: 
        st.error("REPROVADO ❌")

