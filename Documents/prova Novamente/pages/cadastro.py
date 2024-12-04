import streamlit as st
import os
# Configuração da página
st.set_page_config(page_title="Cadastro de Paciente - Saúde")

with open("Cadastro.css") as editor:
    st.markdown(f"<style>{editor.read()}</style>",unsafe_allow_html=True)

# Título da página
st.title("Cadastro de Paciente")
st.write('<p style="font-size:20px;color:black;text-align:center">Por favor, preencha os dados abaixo para o seu cadastro.</p>',unsafe_allow_html=True)
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

if "cadastro_realizado" in st.session_state and st.session_state["cadastro_realizado"]:
    st.success("Cadastro realizado com sucesso! Seja Bem-Vindo(a)!")
else:
    with st.form("cadastro"):
        # Informações pessoais
        nome = st.text_input("Nome", placeholder = "Digite seu nome")
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino","Outro"])
        email = st.text_input("Email", placeholder= "emailaqui@gmail.com")
        senha = st.text_input("Senha", placeholder= "(mín 8 caracteres)", type="password")
        telefone = st.text_input("Telefone", placeholder= "(**) *****-****")
        enviado = st.form_submit_button("Continue")

# Exibe mensagem após envio do formulário
    if enviado:
        if nome == "" or email == "" or senha == "" and len(senha) < 8 or telefone == "":
            st.error("Por favor, preencha todos os campos obrigatórios.") 
        elif nome and email and telefone and senha and len(senha) < 8:
            st.error("A senha deve ter no mínimo 8 caracteres.")       
        elif nome == "" and email == "" and senha == "" and telefone == "":
            st.error("Por favor, preencha todos os campos obrigatórios.") 
        elif "@" not in email:
            st.error("Digite seu email corretamente")
        else:
            st.session_state["nome"] = nome
            st.session_state["sexo"] = sexo
            st.session_state["email"] = email
            st.session_state["senha"] = senha
            st.session_state["telefone"] = telefone
            st.session_state["cadastro_realizado"] = True           
            st.switch_page("pages\Informações Pessoais.py")
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
st.markdown(
    """
    <style>
    /* Alterando o fundo e o estilo do selectbox */
    div.stSelectbox > div > div > div {
        background-color: #f0f8ff;  /* Cor de fundo azul claro */
        color: black;  /* Cor do texto */
        border-radius: 8px;  /* Bordas arredondadas */
        border: 2px solid cyan;  /* Borda azul */
        padding: 5px;  /* Padding interno */
        cursor: pointer;  /* Cursor de ponteiro */
    }
    </style>
    """, 
    unsafe_allow_html=True
)
