import json
import os
from langchain.prompts import PromptTemplate

def readFile(filename):
    content = ""

    try:
        with open(filename, 'r') as fileContent:
            content = fileContent.read()
    except Exception as Err:
        print("{}".format(Err))

    return content

def readJson(filename):
    content = {}

    try:
        content = json.loads(readFile(filename))
    except Exception as Err:
        print("{}".format(Err),exc_info=True)

    return content

def writeFile(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    status = "success"
    try:
        with open(filename, 'w') as fileSource:
            fileSource.write(content)
    except Exception as Err:
        print("{}".format(Err))
        status = "failed"

    return status

def writeJson(filename, content):
    status = "Success"

    try:
        contentDump = json.dumps(content, indent=4, sort_keys=True)
        writeFile(filename, contentDump)
    except Exception as Err:
        print("{}".format(Err))
        status = "Failed"

    return status

configFile = "config/app.setting.json"
configuration = readJson(configFile)

llmProvider = configuration['LLM']['Provider']
temperature = configuration['LLM']['Temperature']
topP = configuration['LLM']['TopP']
topK = configuration['LLM']['TopK']

try:
    if llmProvider == 'GCP':
        from llmUtils import vertexLLM
        model = configuration['Models']['GCP']['Model']
        tokens = configuration['Models']['GCP']['MaxTokens']
        llm = vertexLLM(model, temperature, topP, topK, tokens)
    elif llmProvider == 'AWS':
        from llmUtils import bedrockLLM
        model = configuration['Models']['AWS']['Model']
        tokens = configuration['Models']['AWS']['MaxTokens']
        region = configuration['Models']['AWS']['Region']
        llm = bedrockLLM(model, temperature, topP, tokens, region)
    else:
        from llmUtils import openaiLLM
        model = configuration['Models']['OpenAI']['Model']
        tokens = configuration['Models']['OpenAI']['MaxTokens']
        llm = openaiLLM(model, temperature, topP, topK, tokens)

except Exception as e:
    print(e)


def generateResponse(code):
    try:
        basePrompt = '''For the following code, add comments wherever it makes sense and improve the overall quality of code:
        {code}
        '''
        promptTemplate = PromptTemplate(input_variables=['code'], template= basePrompt)
        prompt = promptTemplate.format(code= code)
        ans = llm.predict(prompt)
        response = ans
        # response = code
    except Exception as e:
        print(e)
        response = "Error in generating comment. Please try later."
    return response

def formatAnswer(text: str):
    try:
        text = text.replace('<','&lt;')
        text = text.replace('>','&gt;')
        n = text.count('```')
        for i in range(n):
            if(i%2 != 0):
                text = text.replace('```', '<div class="code"> <pre> <code>' ,1 ); 
                text = text.replace('```', '</code> </pre> </div>' ,1 ); 
        return text
    except Exception as e:
        print(e)

