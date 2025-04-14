from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy.orm import validates

from ..db_manage import Db_manager

db = Db_manager().get_db()

class Form_Cancer_Patient(db.Model):
    __tablename__ = 'APP_FORM_CANCER_PATIENT'
    # Auto Generated Fields:
    id                  = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created_at          = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at          = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    # Input by User Fields:
    user_id                = db.Column(db.String(50), nullable=False, unique=True)
    cancer_type_region     = db.Column(db.String(50), nullable=False)
    regular_health_check   = db.Column(db.String(100))
    cancer_treatment       = db.Column(db.String(100))
    treatment_complication = db.Column(db.String(100))
    life_after_treatment   = db.Column(db.String(100))
    side_effect_care       = db.Column(db.String(100))
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'cancer_type_region': self.cancer_type_region,
            'regular_health_check': self.regular_health_check,
            'cancer_treatment': self.cancer_treatment,
            'treatment_complicationr': self.treatment_complication,
            'life_after_treatment': self.life_after_treatment,
            'side_effect_care': self.side_effect_care
        }
