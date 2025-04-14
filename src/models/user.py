from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy.orm import validates

from ..db_manage import Db_manager

db = Db_manager().get_db()

class User(db.Model):
    __tablename__ = 'APP_USER'
    # Auto Generated Fields:
    id                  = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created_at          = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at          = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    # Input by User Fields:
    name                = db.Column(db.String(200), nullable=False)
    password            = db.Column(db.String(200), nullable=False)
    date_of_birth       = db.Column(db.Date)
    email               = db.Column(db.String(100), nullable=False, unique=True)
    phone_number        = db.Column(db.String(20))
    genre               = db.Column(db.String(20))
    marital_status      = db.Column(db.String(20))
    education_level     = db.Column(db.String(20))
    weight              = db.Column(db.String(8))
    waist_circumference = db.Column(db.String(8))
    height              = db.Column(db.String(8))
    cancer_patient      = db.Column(db.Boolean)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'date_of_birth': self.date_of_birth,
            'email': self.email,
            'phone_number': self.phone_number,
            'genre': self.genre,
            'marital_status': self.marital_status,
            'education_level': self.education_level,
            'weight': self.weight,
            'waist_circumference': self.waist_circumference, 
            'height': self.height,
            'cancer_patient': self.cancer_patient
        }
