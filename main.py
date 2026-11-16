from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


CAMINHO_DB = "db"

prompt_tamplate = """
Você é um especialista no assunto.

Responda a pergunta do usuário:{pergunta}

com base nessas informações:{base_conhecimento}

se você não encontar a resposta para a pergunta do usuário nessas informações, responda procure um especialista da área!

"""
def pergunta(texto_usuario):

    # carregar o banco de dados
    funcao_embedding = OpenAIEmbeddings()
    db = Chroma(persist_directory= CAMINHO_DB, embedding_function = funcao_embedding)



    # comparar a pergunta do usuário (embedding) com o meu banco de dados
    resultados = db.similarity_search_with_relevance_scores(texto_usuario, k=3)
    if len(resultados) == 0 or resultados[0][1] < 0.7:
        print("Não conseguiu encontrar alguma informação relevante na base")
        return "Não encontrei informação relevante no PDF para essa pergunta."


    textos_resultado= []
    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultado.append(texto)

    base_conhecimento = "\n\n----\n\n".join(textos_resultado)
    prompt = ChatPromptTemplate. from_template(prompt_tamplate)
    prompt = prompt.invoke({"pergunta":texto_usuario,"base_conhecimento":base_conhecimento})

    modelo= ChatOpenAI(model="gpt-4o-mini")
    texto_resposta = modelo.invoke(prompt).content
    return texto_resposta


