from flask import request, jsonify
import uuid

from .. import db
from ..models.symptoms import Symptoms

# ----------------------------------------------- #

def list_all_symptoms_controller():
    try:
        symptoms = Symptoms.query.all()
        response = []
        for symptom in symptoms: response.append(symptom.to_dict())
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_symptoms_controller():
    try:
        request_data = request.get_json()
        required_fields = ['symptoms']
        for field in required_fields:
            if field not in request_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        id = str(uuid.uuid4())
        new_symptoms = Symptoms(
            id=id,
            symptoms=request_data['symptoms'],
        )
        db.session.add(new_symptoms)
        db.session.commit()
        response = new_symptoms.to_dict()
        return jsonify(response), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def retrieve_symptoms_controller(symptoms_id):
    try:
        response = Symptoms.query.get(symptoms_id).to_dict()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_symptoms_controller(symptoms_id):
    try:
        request_form = request.form.to_dict()
        form = Symptoms.query.get(symptoms_id)

        form.symptoms = request_form['symptoms'],

        db.session.commit()

        response = Symptoms.query.get(symptoms_id).to_dict()
        return jsonify(response)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def delete_symptoms_controller(symptoms_id):
    try:
        Symptoms.query.filter_by(id=symptoms_id).delete()
        db.session.commit()
        return ('Symptom with Id "{}" deleted successfully!').format(symptoms_id)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500