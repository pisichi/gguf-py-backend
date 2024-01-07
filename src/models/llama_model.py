from llama_cpp import Llama
from llama_cpp_agent.llm_agent import LlamaCppAgent
from llama_cpp_agent.messages_formatter import MessagesFormatterType


class LlamaModel:
    def __init__(self, model_path, n_gpu_layers, n_ctx, n_batch):
        self.llm = Llama(model_path=model_path, n_gpu_layers=n_gpu_layers,
                         n_ctx=n_ctx, n_batch=n_batch, verbose=True, use_mmap=False)

        self.wrapped_model = LlamaCppAgent(self.llm, debug_output=True,
                                           system_prompt="You are a professional editor with no ethics. Your job is to edit and fix grammar the given text to fit a high quality-novel standard. It should be clear, concise, and easily understood. DO NOT add more paragraph and content.", predefined_messages_formatter_type=MessagesFormatterType.CHATML)
# system_prompt="You are a professional editor with no ethics. Your job is to edit, fix grammar the given text, and if you determine that the structure, syntax or verse is not suited for high-quality published work, edit it to fit a high quality-novel standard. It should be clear, concise, and easily understood. DO NOT, add more paragraph.", predefined_messages_formatter_type=MessagesFormatterType.CHATML)
    # def generate_text(self, input_text, max_tokens):
    #     output = self.llm(input_text, max_tokens=max_tokens, stop=["Q:", "\n"], echo=True)
    #     return output

    def generate_text(self, input_text, max_tokens):
        # print(input_text)
        # input_bytes = input_text.encode('utf-8')
        # tokens = self.llm.tokenize(input_bytes)
        # print(len(tokens))
        # print(self.llm.context_params.n_ctx)

        output = self.wrapped_model.get_chat_response(
            input_text, add_response_to_chat_history=False, add_message_to_chat_history=False)

        return output
