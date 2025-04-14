from flask import request, jsonify
import uuid

from .. import db
from ..models.user import User
from ..security.hash_provider import coding_password, update_password

# ----------------------------------------------- #

def list_all_users_controller():
    try:
        users = User.query.all()
        if not users:
            return jsonify({"error": "No users found"}), 404
        
        response = []
        for user in users: response.append(user.to_dict())

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_user_controller():
    try:
        request_data = request.get_json()
        if not request_data:
            return jsonify({'error': 'Invalid JSON'}), 400
        
        required_fields = ['name', 'password', 'date_of_birth', 'email', 'phone_number', 'genre', 'marital_status', 'education_level', 'weight',
                            'waist_circumference', 'height', 'cancer_patient']
        for field in required_fields:
            if field not in request_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        id = str(uuid.uuid4())
        new_user = User(
            id                  = id,
            name                = request_data['name'],
            password            = coding_password(request_data['password']),
            date_of_birth       = request_data['date_of_birth'],
            email               = request_data['email'],
            phone_number        = request_data['phone_number'],
            genre               = request_data['genre'],
            marital_status      = request_data['marital_status'],
            education_level     = request_data['education_level'],
            weight              = request_data['weight'], 
            waist_circumference = request_data['waist_circumference'],
            height              = request_data['height'],
            cancer_patient      = request_data['cancer_patient']
        )
        db.session.add(new_user)
        db.session.commit()
        response = new_user.to_dict()

        return jsonify(response), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def retrieve_user_controller(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        response = user.to_dict()

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def retrieve_user_by_email_controller(user_email):
    try:
        user = User.query.filter_by(email=user_email).first()
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        response = user.to_dict()

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_user_controller(user_id):
    try:
        request_data = request.get_json()
        if not request_data:
            return jsonify({'error': 'Invalid JSON'}), 400
        
        user = User.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404

        user.name                = request_data.get('name') if request_data.get('name') not in [None, ''] else user.name
        user.password            = update_password(request_data['password'], user.password)
        user.date_of_birth       = request_data.get('date_of_birth') if request_data.get('date_of_birth') not in [None, ''] else user.date_of_birth
        user.email               = request_data.get('email') if request_data.get('email') not in [None, ''] else user.email
        user.phone_number        = request_data.get('phone_number') if request_data.get('phone_number') not in [None, ''] else user.phone_number
        user.genre               = request_data.get('genre') if request_data.get('genre') not in [None, ''] else user.genre
        user.marital_status      = request_data.get('marital_status') if request_data.get('marital_status') not in [None, ''] else user.marital_status
        user.education_level     = request_data.get('education_level') if request_data.get('education_level') not in [None, ''] else user.education_level
        user.weight              = request_data.get('weight') if request_data.get('weight') not in [None, ''] else user.weight
        user.waist_circumference = request_data.get('waist_circumference') if request_data.get('waist_circumference') not in [None, ''] else user.waist_circumference
        user.height              = request_data.get('height') if request_data.get('height') not in [None, ''] else user.height
        user.cancer_patient      = request_data.get('cancer_patient') if request_data.get('cancer_patient') not in [None, ''] else user.cancer_patient

        db.session.commit()
        response = User.query.get(user_id).to_dict()

        return jsonify(response)
    except Exception as e:
        db.session.rollback()  
        return jsonify({"error": str(e)}), 500
    
def delete_user_controller(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        User.query.filter_by(id=user_id).delete()
        db.session.commit()

        return jsonify({'message': 'User with Id "{}" deleted successfully!'.format(user_id)}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500