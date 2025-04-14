from ..security.token_provider import token_required

from ..app import app
from ..controller.cancer_patient_forms_controller import (
    list_all_forms_controller, 
    create_form_controller, 
    retrieve_form_controller, 
    update_form_controller, 
    delete_form_controller
)

@app.route("/cancer_patient_forms", methods=['GET'])
def list_forms():
    return list_all_forms_controller()

@app.route("/cancer_patient_forms", methods=['POST'])
def create_forms():
    return create_form_controller()

@app.route("/cancer_patient_forms/<form_id>", methods=['GET'])
@token_required
def retrieve_forms(form_id, current_user=None):
    return retrieve_form_controller(form_id)

@app.route("/cancer_patient_forms/<form_id>", methods=['PUT'])
@token_required
def update_forms(form_id, current_user=None):
    return update_form_controller(form_id)

@app.route("/cancer_patient_forms/<form_id>", methods=['DELETE'])
@token_required
def delete_forms(form_id, current_user=None):
    return delete_form_controller(form_id)