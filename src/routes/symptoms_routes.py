from ..security.token_provider import token_required

from ..app import app
from ..controller.symptoms_controller import (
    list_all_symptoms_controller, 
    create_symptoms_controller, 
    retrieve_symptoms_controller, 
    update_symptoms_controller, 
    delete_symptoms_controller
)

@app.route("/symptoms", methods=['GET'])
def list_symptoms():
    return list_all_symptoms_controller()
    

@app.route("/symptoms", methods=['POST'])
def create_symptoms():
    return create_symptoms_controller()

@app.route("/symptoms/<symptoms_id>", methods=['GET'])
@token_required
def retrieve_symptom(symptoms_id, current_user=None):
    return retrieve_symptoms_controller(symptoms_id)

@app.route("/symptoms/<symptoms_id>", methods=['PUT'])
@token_required
def update_symptom(symptoms_id, current_user=None):
    return update_symptoms_controller(symptoms_id)
    

@app.route("/symptoms/<symptoms_id>", methods=['DELETE'])
@token_required
def delete_symptom(symptoms_id, current_user=None):
    return delete_symptoms_controller(symptoms_id)