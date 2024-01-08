from flask import request, jsonify
from models.llama_model import LlamaModel
import os

model_path = os.getenv("MODEL_PATH")
n_gpu_layers = int(os.getenv("N_GPU_LAYERS"))
n_ctx = int(os.getenv("N_CTX"))
n_batch = int(os.getenv("N_BATCH"))
agent_prompt = os.getenv("AGENT_PROMPT")
predefined_messages_formatter_type = os.getenv("PREDEFINED_MESSAGES_FORMATTER_TYPE")
debug_output = os.getenv("DEBUG_OUTPUT") == "True"

llama_model = LlamaModel(model_path, n_gpu_layers, n_ctx, n_batch, agent_prompt, predefined_messages_formatter_type, debug_output)

def generate():
    data = request.get_json()
    input_text = data.get('input_text', '')
    max_tokens = data.get('max_tokens', 32)

    output = llama_model.generate(input_text, max_tokens)
    return jsonify({'output': output})