from dotenv import load_dotenv
load_dotenv()
from app_utils import *
from flask import Flask, jsonify, render_template, request, session, redirect, abort, url_for
from waitress import serve

configFile = "config/app.setting.json"
configuration = readJson(configFile)

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def render_page():
    return render_template("index.html")

@app.route('/botInfo', methods = ['POST'])
def process_info():
    resp = {}

    messages = json.loads(request.form["question"])
    question = messages['content']
    response = generateResponse(question)
    # def percy():
    #     print("chirag")

    # if __name__ == "__main__":
    #     percy()
    resp["answer"] = response

    return jsonify(resp)

if __name__ == "__main__":
    if configuration["App"]["Mode"] == 0:
        app.run(host=configuration["App"]["Host"],
                port=configuration["App"]["Port"],
                debug=True,
                threaded=True)
    else:
        serve(app, host=configuration["App"]["Host"],
                port=configuration["App"]["Port"])