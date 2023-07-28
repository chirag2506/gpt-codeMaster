from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

sqlRouter = Blueprint('sqlRouter', __name__, url_prefix= '/database')

@sqlRouter.route('/addUser', methods = ['POST'])
def addUser():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(username, email, password)
    return jsonify({'message': 'added'})

@sqlRouter.route('/getHistory', methods = ['GET'])
@jwt_required()
def getUserHistory():
    # user = request.args.get('user')
    print(get_jwt_identity())
    return jsonify({'message': 'done'})

