from flask import request, jsonify
import uuid

from .. import db
from ..models.treatments import Treatments

# ----------------------------------------------- #

def list_all_treatments_controller():
    try:
        treatments = Treatments.query.all()
        response = []
        for treatment in treatments: response.append(treatment.to_dict())
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_treatment_controller():
    try:
        request_data = request.get_json()
        required_fields = ['treatment']
        for field in required_fields:
            if field not in request_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        id = str(uuid.uuid4())
        new_treatment = Treatments(
            id=id,
            treatment=request_data['treatment'],
        )
        db.session.add(new_treatment)
        db.session.commit()
        response = new_treatment.to_dict()
        return jsonify(response), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def retrieve_treatment_controller(treatment_id):
    try:
        response = Treatments.query.get(treatment_id).to_dict()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_treatment_controller(treatment_id):
    try:
        request_form = request.form.to_dict()
        form = Treatments.query.get(treatment_id)

        form.treatment = request_form['treatment'],

        db.session.commit()

        response = Treatments.query.get(treatment_id).to_dict()
        return jsonify(response)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def delete_treatment_controller(treatment_id):
    try:
        Treatments.query.filter_by(id=treatment_id).delete()
        db.session.commit()
        return ('Treatment with Id "{}" deleted successfully!').format(treatment_id)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500