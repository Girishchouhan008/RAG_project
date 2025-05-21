from transformers import AutoTokenizer, AutoModelForCausalLM
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch
from sentence_transformers import SentenceTransformer

MODEL_PATH = "models/distilgpt2"

# Load models once
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, local_files_only=True)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def get_answer(question, context_text):
    text_chunks = [context_text[i:i+500] for i in range(0, len(context_text), 500)]

    text_emb = embedder.encode(text_chunks)
    question_embedding = embedder.encode([question])[0]

    same = cosine_similarity([question_embedding], text_emb)[0]
    best_chunk = text_chunks[np.argmax(same)]

    prompt = f"Context: {best_chunk}\nQuestion: {question}\nAnswer:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    output = model.generate(input_ids, max_new_tokens=100, pad_token_id=tokenizer.eos_token_id)
    answer = tokenizer.decode(output[0], skip_special_tokens=True)

    return answer.split("Answer:")[-1].strip()
