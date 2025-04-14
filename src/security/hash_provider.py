from flask import jsonify
import bcrypt

salt = bcrypt.gensalt(8)

def coding_password(password: str):
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, salt).decode('utf-8')

def update_password(password: str, hash: str):
    password = password.encode('utf-8')
    hash = hash.encode('utf-8')
    if bool(bcrypt.checkpw(password, hash)):
        return "The password is already being used"
    else: return bcrypt.hashpw(password, salt).decode('utf-8')

def check_password(password: str, hash:str):
    password = password.encode('utf-8')
    hash = hash.encode('utf-8') 
    check = bcrypt.checkpw(password, hash)
    return bool(check)