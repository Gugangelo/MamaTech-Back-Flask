from flask import request, jsonify
import uuid

from .. import db
from ..models.patient_treatment import Patient_Treatment

# ----------------------------------------------- #

def list_all_patient_treatments_controller():
    try:
        patient_treatments = Patient_Treatment.query.all()
        response = []
        for patient_treatment in patient_treatments: response.append(patient_treatment.to_dict())
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_patient_treatment_controller():
    try:
        request_data = request.get_json()
        required_fields = ['user_id', 'cancer_form_id', 'treatment_id']
        for field in required_fields:
            if field not in request_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        id = str(uuid.uuid4())
        new_patient_treatment = Patient_Treatment(
            id=id,
            user_id=request_data['user_id'],
            cancer_form_id=request_data['cancer_form_id'],
            treatment_id=request_data['treatment_id']
        )
        db.session.add(new_patient_treatment)
        db.session.commit()
        response = new_patient_treatment.to_dict()
        return jsonify(response), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def retrieve_patient_treatment_controller(patient_treatment_id):
    try:
        response = Patient_Treatment.query.get(patient_treatment_id).to_dict()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_patient_treatment_controller(patient_treatment_id):
    try:
        request_form = request.form.to_dict()
        form = Patient_Treatment.query.get(patient_treatment_id)

        form.user_id        = request_form['user_id'],
        form.cancer_form_id = request_form['cancer_form_id'],
        form.treatment_id   = request_form['treatment_id']

        db.session.commit()

        response = Patient_Treatment.query.get(patient_treatment_id).to_dict()
        return jsonify(response)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def delete_patient_treatment_controller(patient_treatment_id):
    try:
        Patient_Treatment.query.filter_by(id=patient_treatment_id).delete()
        db.session.commit()
        return ('Patient Treatment with Id "{}" deleted successfully!').format(patient_treatment_id)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500