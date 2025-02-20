import streamlit as st
import os

with open("inf.css") as editor:
    st.markdown(f"<style>{editor.read()}</style>",unsafe_allow_html=True)

st.title("Cadastro de Paciente")
st.write('<p style="color:black;font-size:20px;text-size:20px;text-align:center">Por favor, preencha os dados abaixo para o seu cadastro.</p>', unsafe_allow_html=True)
image_path = os.path.join("img", "logo.png")
st.sidebar.image(image_path)
image_url = "https://img.freepik.com/premium-vector/white-abstract-background-design_1208459-106.jpg?semt=ais_hybrid"  # Exemplo: "imagens/fundo.jpg"

# Adicione a imagem de fundo com HTML e CSS

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
        .stTextInput input {
            background-color: white;
            color: black;
            border: 2px solid cyan;
            font-size: 16px;
        }<style>"""
            , unsafe_allow_html=True)
st.markdown("""
    <style>
        .stTextInput label {
        color: black;
        font-size: 35px;
    }</style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        /* Cor do fundo do campo de texto */
        .stTextInput>div>div>input {
            background-color: #f0f8ff;  /* Cor de fundo (exemplo: Alice Blue) */
            color: #333333;
}
        .stTextInput>div>div>input::placeholder {
            color: #333333;
}
    </style>
""", unsafe_allow_html=True)

if "cadastro" in st.session_state and st.session_state["cadastro"]:
    st.success("Seu cadastro realizado com sucesso! Seja Bem-Vindo(a)!")
else:
    with st.form("saúde"):
        st.header("Informacoes de Saude")

        altura = st.number_input("Altura (cm)", min_value=50, max_value=250, step=1, value=170)
        peso = st.number_input("Peso (kg)", min_value=10, max_value=300, step=1, value=70)
        condições = st.text_area("Condições de Saúde", placeholder="Ex.: diabetes, hipertensão, etc.")
        
        enviado = st.form_submit_button("Enviar Cadastro")

    if enviado:
        if altura and peso and condições:
            st.session_state["altura"] = altura
            st.session_state["peso"] = peso
            st.session_state["condições"] = condições
            st.session_state["cadastro"] = True
            st.switch_page("pages\Ingestão de Àgua.py")
        else:
            st.error("Por favor, verifique se todos os campos estão preenchidos.")

