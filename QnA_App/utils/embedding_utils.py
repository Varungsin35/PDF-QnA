from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def embed_and_index(chunks):
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))
    return index, embeddings, chunks

def get_relevant_chunk(question, index, chunks, model):
    question_embedding = model.encode([question])
    D, I = index.search(np.array(question_embedding), k=1)
    return chunks[I[0][0]]
