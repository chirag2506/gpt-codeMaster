from langchain.llms import VertexAI

models = ['text-bison@001', 'code-bison@001']

def vertexLLM(model: str, temp: int, top_p: int, top_k: int, max_tokens: int):
    if model not in models:
        raise NameError("Model Not Found")
    llm = VertexAI(model_name= model, temperature= temp, top_p= top_p, top_k= top_k, max_output_tokens= max_tokens)
    return llm