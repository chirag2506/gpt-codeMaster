from dotenv import load_dotenv
load_dotenv()
from app_utils import *
from flask import Flask, jsonify, render_template, request, session, redirect, abort, url_for
from datetime import datetime, timedelta, timezone
from flask_cors import CORS
from waitress import serve
from flask_jwt_extended import create_access_token, set_access_cookies, JWTManager, get_jwt, get_jwt_identity, jwt_required, unset_jwt_cookies

app = Flask(__name__)
CORS(app, resource={"/*": {"origins": "http://localhost:3000/"}}, supports_credentials= True, expose_headers= ['Set-Cookie'])
app.config["JWT_COOKIE_SECURE"] = False # True for prod (JWTs to be sent over https)
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = os.environ['JWT_SECRET_KEY'] 
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)


@app.route('/', methods = ['GET'])
def render_page():
    return jsonify({"message": "welcome"})

# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token, timedelta(hours=1))
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response

@app.route('/login', methods=['POST'])
def login():
    response = {'msg': 'login successful'}
    email = request.json.get('email')
    password = request.json.get('password')
    if email is None or password is None:
        response['msg'] = 'unauthorized'
        return jsonify(response)

    access_token = create_access_token(identity=email)
    # print(access_token)
    response = jsonify(response)
    set_access_cookies(response, access_token, timedelta(hours=1))
    return response

@app.route("/getUser")
@jwt_required()
def userIdentity():
    identity=get_jwt_identity()
    return jsonify(user = identity)

@app.route("/logout", methods=['POST'])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

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