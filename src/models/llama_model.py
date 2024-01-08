from llama_cpp import Llama
from llama_cpp_agent.llm_agent import LlamaCppAgent
from llama_cpp_agent.messages_formatter import MessagesFormatterType

class LlamaModel:
    def __init__(self, model_path, n_gpu_layers, n_ctx, n_batch, system_prompt, predefined_messages_formatter_type, debug_output):
        self.llm = Llama(model_path=model_path, n_gpu_layers=n_gpu_layers,
                         n_ctx=n_ctx, n_batch=n_batch, verbose=True, use_mmap=False)

        self.wrapped_model = LlamaCppAgent(self.llm, debug_output=debug_output,
                                           system_prompt=system_prompt, predefined_messages_formatter_type=MessagesFormatterType[predefined_messages_formatter_type])

    def generate(self, input_text, max_tokens):
        output = self.wrapped_model.get_chat_response(
            input_text, add_response_to_chat_history=False, add_message_to_chat_history=False, max_tokens=max_tokens)

        return output
