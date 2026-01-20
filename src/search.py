import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.runnables import RunnableLambda

from db import get_db
from envs import (
    GOOGLE_MODEL,
    OPENAI_MODEL,
    ACTIVE_CHAT_PROVIDER,
)

load_dotenv()

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def get_chat_model():
    if ACTIVE_CHAT_PROVIDER == "google":
        return ChatGoogleGenerativeAI(model=GOOGLE_MODEL, temperature=0.7)
    else:
        return ChatOpenAI(model=OPENAI_MODEL, temperature=0.7)


def search_prompt(question=None):
    store = get_db()

    # print(f"Searching for relevant documents for question: {question}")
    results = store.similarity_search_with_score(question, k=10)

    formatted_result = "\n\n".join([doc.page_content for doc, score in results])
    # print("Formatted Result:", formatted_result)

    question_template = PromptTemplate(
        input_variables=["contexto", "pergunta"],
        template=PROMPT_TEMPLATE,
        partial_variables={
            "contexto": formatted_result,
        },
    )

    model = get_chat_model()

    chain = question_template | model

    return chain
