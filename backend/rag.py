from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM

import os

# Load file safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data.txt")

with open(file_path, "r") as f:
    text = f.read()

# Split
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = splitter.split_text(text)

# NEW embeddings (fixed)
embeddings = OllamaEmbeddings(model="phi")

# Vector DB
db = FAISS.from_texts(docs, embeddings)

# NEW LLM
llm = OllamaLLM(model="phi")

def get_answer(query):
    docs = db.similarity_search(query)
    context = " ".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer based only on context:
    {context}

    Question: {query}
    """

    return llm.invoke(prompt)