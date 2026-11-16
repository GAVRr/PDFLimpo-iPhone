from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

PASTA_BASE = "base"


def criar_db():
    documentos = carregar_documentos()
    chunks = dividir_chunks(documentos)
    vetorizar_chunks(chunks)
   
    #ajustar para salvar um arquivo que o usuario mandar
def carregar_documentos():
    carregador = PyPDFDirectoryLoader(PASTA_BASE,glob="*.pdf")
    documentos = carregador.load()
    return documentos

def dividir_chunks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap = 500,
        length_function = len,
        add_start_index = True
    )
    chunks = separador_documentos.split_documents(documentos)
    return chunks

def vetorizar_chunks(chunks):
    Chroma(persist_directory="db", embedding_function=OpenAIEmbeddings()).delete_collection()
    db = Chroma.from_documents(chunks,OpenAIEmbeddings(),persist_directory="db")
    print("Banco de dados criado")

