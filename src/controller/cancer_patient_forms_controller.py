from flask import request, jsonify
import uuid

from .. import db
from ..models.cancer_patient_forms import Form_Cancer_Patient
from ..models.patient_symptoms import Patient_Symptoms
from ..models.patient_treatment import Patient_Treatment
from ..models.symptoms import Symptoms
from ..models.treatments import Treatments
# ----------------------------------------------- #

def list_all_forms_controller():
    try:
        forms = Form_Cancer_Patient.query.all()
        response = []
        for form in forms:
            form_dict = form.to_dict()
            patient_symptoms = Patient_Symptoms.query.filter_by(user_id=form.user_id).all()
            symptoms_list = []
            for patient_symptom in patient_symptoms:
                symptom = Symptoms.query.get(patient_symptom.symptoms_id)
                symptoms_list.append({'id': symptom.id, 'symptoms': symptom.symptoms})
            form_dict['patient_symptoms'] = symptoms_list
            patient_treatments = Patient_Treatment.query.filter_by(user_id=form.user_id).all()
            treatments_list = []
            for patient_treatment in patient_treatments:
                treatment = Treatments.query.get(patient_treatment.treatment_id)
                treatments_list.append({'id': treatment.id, 'symptoms': treatment.treatment})
            form_dict['patient_treatments'] = treatments_list
            response.append(form_dict)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_form_controller():
    try:
        request_data = request.get_json()
        required_fields = ['user_id', 'cancer_type_region', 'regular_health_check', 'cancer_treatment', 'treatment_complication', 
                        'life_after_treatment', 'side_effect_care']
        for field in required_fields:
            if field not in request_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
            
        if 'symptoms' not in request_data:
            symptoms = []
        elif not isinstance(request_data['symptoms'], list):
            return jsonify({'error': 'Field "symptoms" must be a list of objects'}), 400
        else:
            symptoms = request_data['symptoms']
        
        if 'treatments' not in request_data:
            treatments = []
        elif not isinstance(request_data['treatments'], list):
            return jsonify({'error': 'Field "treatments" must be a list of objects'}), 400
        else:
            symptoms = request_data['treatments']
            
        with db.session.begin_nested():
            id = str(uuid.uuid4())
            new_forms = Form_Cancer_Patient(
                id=id,
                user_id=request_data['user_id'],
                cancer_type_region=request_data['cancer_type_region'],
                regular_health_check=request_data['regular_health_check'],
                cancer_treatment=request_data['cancer_treatment'],
                treatment_complication=request_data['treatment_complication'],
                life_after_treatment=request_data['life_after_treatment'],
                side_effect_care=request_data['side_effect_care'],
            )
            db.session.add(new_forms)
            db.session.flush()

            for symptom_data in symptoms:
                id = str(uuid.uuid4())
                new_patient_symptoms = Patient_Symptoms(
                    id=id,
                    user_id=request_data['user_id'],
                    cancer_form_id=new_forms.id,
                    symptoms_id=symptom_data['id']
                )
                db.session.add(new_patient_symptoms)
            for treatments_data in treatments:
                id = str(uuid.uuid4())
                new_patient_treatments = Patient_Treatment(
                    id=id,
                    user_id=request_data['user_id'],
                    cancer_form_id=new_forms.id,
                    treatment_id=treatments_data['id']
                )
                db.session.add(new_patient_treatments)
        db.session.commit()

        response = new_forms.to_dict()
        response['symptoms'] = symptoms
        response['treatments'] = treatments
        return jsonify(response), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def retrieve_form_controller(form_id):
    try:
        response = Form_Cancer_Patient.query.get(form_id).to_dict()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_form_controller(form_id):
    try:
        request_form = request.form.to_dict()
        form = Form_Cancer_Patient.query.get(form_id)

        form.user_id                = request_form['user_id'],
        form.cancer_type_region     = request_form['cancer_type_region'],
        form.regular_health_check   = request_form['regular_health_check'],
        form.cancer_treatment       = request_form['cancer_treatment'],
        form.treatment_complication = request_form['treatment_complication'],
        form.life_after_treatment   = request_form['life_after_treatment'],
        form.side_effect_care       = request_form['side_effect_care']

        db.session.commit()

        response = Form_Cancer_Patient.query.get(form_id).to_dict()
        return jsonify(response)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def delete_form_controller(form_id):
    try:
        Form_Cancer_Patient.query.filter_by(id=form_id).delete()
        db.session.commit()
        return ('Cancer Form with Id "{}" deleted successfully!').format(form_id)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500