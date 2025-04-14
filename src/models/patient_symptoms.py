from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy.orm import validates

from ..db_manage import Db_manager

db = Db_manager().get_db()

class Patient_Symptoms(db.Model):
    __tablename__ = 'APP_PATIENT_SYMPTOMS'
    # Auto Generated Fields:
    id                  = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created_at          = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at          = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    # Input by User Fields:
    user_id        = db.Column(db.String(50), nullable=False)
    cancer_form_id = db.Column(db.String(50), nullable=False)
    symptoms_id   = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'cancer_form_id': self.cancer_form_id,
            'symptoms_id': self.symptoms_id,
        }