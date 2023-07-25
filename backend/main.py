from dotenv import load_dotenv
load_dotenv()
from app_utils import *
from flask import Flask, jsonify, render_template, request, session, redirect, abort, url_for
from flask_cors import CORS
from waitress import serve
from flask_jwt_extended import create_access_token, set_access_cookies, JWTManager

app = Flask(__name__)
CORS(app, resource={"/*": {"origins": "*"}})
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


@app.route('/', methods = ['GET'])
def render_page():
    return jsonify({"message": "welcome"})

@app.route('/login', methods=['POST'])
def login():
    response = {'msg': 'login successful'}
    email = request.json.get('email')
    password = request.json.get('password')
    if email is None or password is None:
        response['msg'] = 'unauthorized'

    access_token = create_access_token(identity=email)
    print(access_token)
    set_access_cookies(response, access_token)
    return jsonify(response)

@app.route('/botInfo', methods = ['POST'])
def process_info():
    resp = {}

    messages = json.loads(request.form['question'])
    question = messages['content']
    response = generateResponse(question)
    # response = formatAnswer(response)
    resp['answer'] = response

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