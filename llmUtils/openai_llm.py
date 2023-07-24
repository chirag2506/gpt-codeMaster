from langchain.llms import OpenAI

models = ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'text-davinci-003', 'gpt-4']

def openaiLLM(model: str, temp: int, top_p: int, top_k: int, max_tokens: int):
    if model not in models:
        raise NameError("Model Not Found")
    llm = OpenAI()
    return llm