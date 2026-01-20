from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from envs import PDF_PATH
from db import get_db


def ingest_pdf():
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150, add_start_index=False
    )

    splits = splitter.split_documents(docs)

    if not splits:
        print("No document splits were created.")
        raise SystemError(0)

    # Remove empty metadata entires
    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in (None, "")},
        )
        for d in splits
    ]

    ids = [f"doc-{i}" for i in range(len(enriched))]

    store = get_db()

    store.add_documents(documents=enriched, ids=ids)

    print(f"Ingested {len(enriched)} documents into the vector store.")


if __name__ == "__main__":
    ingest_pdf()
