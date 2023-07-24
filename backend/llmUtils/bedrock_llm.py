from langchain.llms import Bedrock
import boto3

models = ['amazon.titan-tg1-large', 'ai21.j2-grande-instruct', 'ai21.j2-jumbo-instruct']

def bedrockLLM(model: str, temp: int, top_p: int, max_tokens: int, region: str):
    if model not in models:
        raise NameError("Model Not Found")
    
    provider = model.split(".")[0]
    if provider=='amazon':
        model_kwargs = {'maxTokenCount': max_tokens, 'temperature': temp, 'topP': top_p}
    elif provider == 'ai21':
        model_kwargs = {'maxTokens': max_tokens, 'temperature': temp, 'topP': top_p}
    else:
        model_kwargs = {}

    client = boto3.client("bedrock", region_name = region)
    llm = Bedrock(client= client, model_id=model, model_kwargs=model_kwargs)
    return llm