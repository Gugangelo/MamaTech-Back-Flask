from flask import request, jsonify
import uuid

from .. import db
from ..models.patient_symptoms import Patient_Symptoms

# ----------------------------------------------- #

def list_all_patient_symptoms_controller():
    try:
        patient_symptoms = Patient_Symptoms.query.all()
        response = []
        for patient_symptoms in patient_symptoms: response.append(patient_symptoms.to_dict())
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def create_patient_symptoms_controller():
    try:
        request_data = request.get_json()
        required_fields = ['user_id', 'cancer_form_id', 'symptoms_id']
        for field in required_fields:
            if field not in request_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        id = str(uuid.uuid4())
        new_patient_symptoms = Patient_Symptoms(
            id=id,
            user_id=request_data['user_id'],
            cancer_form_id=request_data['cancer_form_id'],
            symptoms_id=request_data['symptoms_id']
        )
        db.session.add(new_patient_symptoms)
        db.session.commit()
        response = new_patient_symptoms.to_dict()
        return jsonify(response), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


def retrieve_patient_symptoms_controller(patient_symptoms_id):
    try:
        response = Patient_Symptoms.query.get(patient_symptoms_id).to_dict()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_patient_symptoms_controller(patient_symptoms_id):
    try:
        request_form = request.form.to_dict()
        form = Patient_Symptoms.query.get(patient_symptoms_id)

        form.user_id        = request_form['user_id'],
        form.cancer_form_id = request_form['cancer_form_id'],
        form.symptoms_id   = request_form['symptoms_id']

        db.session.commit()

        response = Patient_Symptoms.query.get(patient_symptoms_id).to_dict()
        return jsonify(response)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def delete_patient_symptoms_controller(patient_symptoms_id):
    try:
        Patient_Symptoms.query.filter_by(id=patient_symptoms_id).delete()
        db.session.commit()
        return ('Patient Symptoms with Id "{}" deleted successfully!').format(patient_symptoms_id)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500