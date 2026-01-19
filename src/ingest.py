import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "gpt-5-nano")
PG_VECTOR_COLLECTION_NAME = os.getenv("PGVECTOR_COLLECTION", "documents")
DATABASE_URL = os.getenv("DATABASE_URL")

def ingest_pdf():
    loader = PyPDFLoader("document.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150, add_start_index=False)

    splits = splitter.split_documents(docs)

    if not splits:
        print("No document splits were created.")
        raise SystemError(0)
    
    # Remove empty metadata entires
    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in (None, "")}
        )
        for d in splits
    ]

    ids = [f"doc-{i}" for i in range(len(enriched))]

    embeddings = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL)

    # Store in Postgres
    store = PGVector

    store = PGVector(
        embeddings=embeddings,
        collection_name=PG_VECTOR_COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True,
    )

    store.add_documents(documents=enriched, ids=ids)

    print(f"Ingested {len(enriched)} documents into the vector store.")

if __name__ == "__main__":
    ingest_pdf()