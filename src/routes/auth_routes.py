from flask import request, jsonify
from ..controller.user_controller import retrieve_user_by_email_controller
from ..security.hash_provider import check_password
from ..security.token_provider import create_token, token_required

from ..app import app

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_email = data['email']
    user = retrieve_user_by_email_controller(user_email)
    if check_password(data['password'], user['password']) == False or user['email'] != data['email']:
        return jsonify({'message': 'Invalid credentials'})
    token = create_token({'sub': data})
    return jsonify({'token': token})

@app.route('/user', methods=['GET'])
@token_required
def protected_route(current_user):
    return jsonify({'message': f'{current_user}'})