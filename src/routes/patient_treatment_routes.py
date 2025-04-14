from ..security.token_provider import token_required 

from ..app import app
from ..controller.patient_treatment_controller import (
    list_all_patient_treatments_controller, 
    create_patient_treatment_controller, 
    retrieve_patient_treatment_controller, 
    update_patient_treatment_controller, 
    delete_patient_treatment_controller
)

@app.route("/patient_treatment", methods=['GET'])
def list_patient_treatments():
    return list_all_patient_treatments_controller()

@app.route("/patient_treatment", methods=['POST'])
def create_patient_treatments():
    return create_patient_treatment_controller()

@app.route("/patient_treatment/<patient_treatment_id>", methods=['GET'])
@token_required
def retrieve_patient_treatments(patient_treatment_id, current_user=None):
    return retrieve_patient_treatment_controller(patient_treatment_id)
    

@app.route("/patient_treatment/<patient_treatment_id>", methods=['PUT'])
@token_required
def update_patient_treatments(patient_treatment_id, current_user=None):
    return update_patient_treatment_controller(patient_treatment_id)

@app.route("/patient_treatment/<patient_treatment_id>", methods=['DELETE'])
@token_required
def delete_patient_treatments(patient_treatment_id, current_user=None):
    return delete_patient_treatment_controller(patient_treatment_id)