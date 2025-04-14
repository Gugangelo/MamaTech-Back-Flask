from flasgger import swag_from
from ..security.token_provider import  token_required


from ..app import app
from ..controller.user_controller import (
    list_all_users_controller,
    create_user_controller,
    retrieve_user_controller,
    update_user_controller,
    delete_user_controller,
)

@app.route("/users", methods=['GET'])
def list_all_users():
    return list_all_users_controller()

@app.route("/users", methods=['POST'])
def create_user():
    return create_user_controller()

@app.route("/users/<user_id>", methods=['GET'])
@token_required
def retrieve_user(user_id, current_user=None):
    return retrieve_user_controller(user_id)

@app.route("/users/<user_id>", methods=['PUT'])
@token_required
def update_user(user_id, current_user=None):
    return update_user_controller(user_id)

@app.route("/users/<user_id>", methods=['DELETE'])
@token_required
def delete_user(user_id, current_user=None):
    return delete_user_controller(user_id)
