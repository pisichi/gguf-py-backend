from llama_cpp import Llama

class LlamaModel:
    def __init__(self, model_path, n_gpu_layers, n_ctx, n_batch):
        self.llm = Llama(model_path=model_path, n_gpu_layers=n_gpu_layers, n_ctx=n_ctx, n_batch=n_batch, verbose=True, use_mmap=False)

    def generate_text(self, input_text, max_tokens):
        output = self.llm(input_text, max_tokens=max_tokens, stop=["Q:", "\n"], echo=True)
        return output