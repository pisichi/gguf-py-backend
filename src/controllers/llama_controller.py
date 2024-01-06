from flask import request, jsonify
from models.llama_model import LlamaModel
import os
from dotenv import load_dotenv

load_dotenv()

model_path = os.getenv("MODEL_PATH")
n_gpu_layers = int(os.getenv("N_GPU_LAYERS"))
n_ctx = int(os.getenv("N_CTX"))
n_batch = int(os.getenv("N_BATCH"))

llama_model = LlamaModel(model_path, n_gpu_layers, n_ctx, n_batch)

def generate_text():
    data = request.get_json()
    input_text = data.get('input_text', '')
    max_tokens = data.get('max_tokens', 32)

    output = llama_model.generate_text(input_text, max_tokens)
    return jsonify({'output': output})
