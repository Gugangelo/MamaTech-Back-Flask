from flask import request, jsonify
from datetime import datetime, timedelta
from jose import jwt
from functools import wraps

# Configurações
SECRET_KEY = '7751a23fa55170a57e90374df13a3ab78efe0e99'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def create_token(user_id='fixed_user'):
    expiration = datetime.now() + timedelta(minutes=EXPIRES_IN_MIN)
    data = {
        'exp': expiration,
        'sub': str(user_id)  # Garante que 'sub' seja sempre uma string
    }
    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def check_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split(" ")[1]
            except IndexError:
                return jsonify({'message': 'Token format is invalid!'}), 400

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            current_user = check_token(token)
            if not current_user:
                return jsonify({'message': 'Token is invalid or expired!'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.JWTError as e:
            return jsonify({'message': f'Token is invalid! {str(e)}'}), 401

        kwargs['current_user'] = current_user  # Passa o usuário nos kwargs
        return f(*args, **kwargs)
    return decorator