from ..security.token_provider import token_required

from ..app import app
from ..controller.treatments_controller import (
    list_all_treatments_controller, 
    create_treatment_controller, 
    retrieve_treatment_controller, 
    update_treatment_controller, 
    delete_treatment_controller
)

@app.route("/treatments", methods=['GET'])
def list_create_treatments():
    return list_all_treatments_controller()

@app.route("/treatments", methods=['POST'])
def create_treatments():
    return create_treatment_controller()

@app.route("/treatments/<treatment_id>", methods=['GET'])
def retrieve_treatments(treatment_id, current_user=None):
    return retrieve_treatment_controller(treatment_id)
    

@app.route("/treatments/<treatment_id>", methods=['PUT'])
@token_required
def update_treatments(treatment_id, current_user=None):
    return update_treatment_controller(treatment_id)
    
@app.route("/treatments/<treatment_id>", methods=['DELETE'])
@token_required
def delete_treatments(treatment_id, current_user=None):
    return delete_treatment_controller(treatment_id)