import streamlit as st
from main import pergunta
from criar_banco import criar_db, carregar_documentos
from pathlib import Path
import os
import shutil
from criar_banco import criar_db

PASTA = "base"




st.set_page_config(
    page_title='PDFLimpo',
    page_icon='logo/PDFLimpo.png',
    layout='wide',
    initial_sidebar_state='expanded'
)

col_logo, col_texto = st.columns([1, 10])


with col_logo:
    st.image('logo/PDFLimpo.png', width=1000)


st.markdown(
      """
    <h1 style='text-align: center;
    color: white'>
        Insira aqui seu PDF
    </h1>
    """,
    unsafe_allow_html=True
    
)
st.markdown("""
<style>

/* Caixa externa */
[data-testid="stFileUploader"] {
    max-width: 768px !important;
    height: 172px !important;
    margin: 14px auto !important;
    padding: 12px !important;
    background: #172033 !important;
    border-radius: 14px !important;
    box-sizing: border-box !important;
}

/* Área interna */
[data-testid="stFileUploaderDropzone"] {
    height: 160px !important;
    min-height: 160px !important;
    padding: 12px !important;
    border: 1px dashed #2878ff !important;
    border-radius: 12px !important;

    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;

    box-sizing: border-box !important;
}

/* Botão */
[data-testid="stFileUploaderDropzone"] button {
    background: #2864ed !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    font-size: 13px !important;
    padding: 8px 18px !important;
    margin: 0 auto !important;
}

/* Texto de limite */
[data-testid="stFileUploaderDropzone"] small {
    font-size: 12px !important;
    color: #b8c5d8 !important;
    text-align: center !important;
}

/* Remover espaçamentos desnecessários */
[data-testid="stFileUploaderDropzone"] > div {
    justify-content: center !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-bottom:8px;">
    <div style="font-size:25px;">📁</div>
    <div style="font-size:16px; font-weight:600;">
        Selecione seu PDF
    </div>
    <div style="font-size:12px; color:#b8c5d8; margin-top:5px;">
        Arraste seu arquivo ou clique para procurar
    </div>
</div>
""", unsafe_allow_html=True)


arquivo = st.file_uploader(
    "Anexe seu PDF aqui",
    type=["pdf"],
    label_visibility="collapsed"
)

if arquivo:
    if st.session_state.get("ultimo_arquivo") != arquivo.name:
        shutil.rmtree(PASTA, ignore_errors=True)
        os.makedirs(PASTA, exist_ok=True)
        caminho= Path(PASTA) / arquivo.name
        with open(caminho, "wb") as f: 
            f.write(arquivo.getvalue())
        with st.spinner("Processando PDF"):
            criar_db()
        st.session_state["ultimo_arquivo"] = arquivo.name
        st.success("PDF processado")





st.markdown(
    """
    <style>
    [data-testid="stTextInput"],
    [data-testid="stElementContainer"]:has([data-testid="stTextInput"]) {
        width: 100% !important;
        max-width: 768px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

usuario = st.text_input("",placeholder="Qual sua Pergunta?",width=150,label_visibility="collapsed")
st.markdown(
    """
    <style>
    [data-testid="stButton"] button {
        background-color: #1E6FFF;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        transition: transform 0.2s ease, background-color 0.2s ease;
        width: 100% !important;
        max-width: 200px !important;
        margin-left: 785px !important;
        margin-right: auto !important;
    }

    [data-testid="stButton"] button:hover {
        background-color: #1558CC;
        color: white;
        transform: scale(1.1);
    }

    [data-testid="stButton"] button:active {
        background-color: #0F44A0;
        color: white;
        transform: scale(1.03);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button("Perguntar"):
    st.divider()
    if not arquivo:
            st.error("Selecione um arquivo primeiro")
    elif not usuario:
            st.error("Não entendi sua pergunta!")
    else:
        with st.spinner("pensando..."):
            resposta = pergunta(usuario)
        st.markdown(f"""
<div class="card-ia">
    <div class="card-header">
        <span class="titulo-ia">Resposta da IA</span>
        <span class="badge-ia">✨ Assistente IA</span>
        <span class="subtitulo-ia">Resposta gerada automaticamente</span>
    </div>

{resposta}

</div>
""", unsafe_allow_html=True)
  



