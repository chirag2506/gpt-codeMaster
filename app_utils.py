import json
import os
from llmUtils import vertexLLM

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

try:
    llm = vertexLLM('text-bison@001', 0.1, 0.95, 10, 1000)
except Exception as e:
    print(e)


def generateResponse(code):
    try:
        # ans = llm.predict("For the following code, add comments wherever it makes sense and improve the overall quality of code:\n"+code)
        # response = ans
        response = code
    except Exception as e:
        print(e)
        response = "Error in generating comment. Please try later."
    return response

