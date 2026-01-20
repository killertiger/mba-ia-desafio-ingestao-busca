from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

from envs import (
    DATABASE_URL,
    GOOGLE_EMBEDDING_MODEL,
    OPENAI_EMBEDDING_MODEL,
    PG_VECTOR_COLLECTION_NAME,
    ACTIVE_EMBEDDING_PROVIDER,
)

def get_db():
    if ACTIVE_EMBEDDING_PROVIDER == "google":
        embeddings = GoogleGenerativeAIEmbeddings(model=GOOGLE_EMBEDDING_MODEL)
    else:
        embeddings = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL)

    store = PGVector(
        embeddings=embeddings,
        collection_name=PG_VECTOR_COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True,
    )

    return store
