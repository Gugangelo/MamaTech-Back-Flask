from ..security.token_provider import token_required

from ..app import app
from ..controller.patient_symptoms_controller import (
    list_all_patient_symptoms_controller, 
    create_patient_symptoms_controller, 
    retrieve_patient_symptoms_controller, 
    update_patient_symptoms_controller, 
    delete_patient_symptoms_controller
)

@app.route("/patient_symptoms", methods=['GET'])
def list_patient_symptoms():
    return list_all_patient_symptoms_controller()
    

@app.route("/patient_symptoms", methods=['POST'])
def create_patient_symptoms():
    return create_patient_symptoms_controller()

@app.route("/patient_symptoms/<patient_symptoms_id>", methods=['GET'])
@token_required
def retrieve_symptoms(patient_symptoms_id, current_user=None):
    return retrieve_patient_symptoms_controller(patient_symptoms_id)
    
@app.route("/patient_symptoms/<patient_symptoms_id>", methods=['PUT'])
@token_required
def update_patient_symptoms(patient_symptoms_id, current_user=None):
    return update_patient_symptoms_controller(patient_symptoms_id)

@app.route("/patient_symptoms/<patient_symptoms_id>", methods=['DELETE'])
@token_required
def delete_patient_symptoms(patient_symptoms_id, current_user=None):
    return delete_patient_symptoms_controller(patient_symptoms_id)