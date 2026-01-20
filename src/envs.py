import os
from dotenv import load_dotenv


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_EMBEDDING_MODEL = os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001")
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash-lite")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-nano")
DATABASE_URL = os.getenv("DATABASE_URL")
PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME", "ia_desafio")
PDF_PATH = os.getenv("PDF_PATH", "document.pdf")
ACTIVE_EMBEDDING_PROVIDER = os.getenv("ACTIVE_EMBEDDING_PROVIDER", "openai")  # or "google"
ACTIVE_CHAT_PROVIDER = os.getenv("ACTIVE_CHAT_PROVIDER", "openai")  # or "google"