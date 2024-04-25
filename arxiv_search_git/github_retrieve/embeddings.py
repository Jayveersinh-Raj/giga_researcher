import sentence_transformers

# Embeddings model
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2" 
sentence_encoder = sentence_transformers.SentenceTransformer(embedding_model_name)